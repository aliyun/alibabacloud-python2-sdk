# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AcceptHandshakeRequest(TeaModel):
    def __init__(self, handshake_id=None):
        self.handshake_id = handshake_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptHandshakeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class AcceptHandshakeResponseBodyHandshake(TeaModel):
    def __init__(self, create_time=None, expire_time=None, handshake_id=None, master_account_id=None,
                 master_account_name=None, modify_time=None, note=None, resource_directory_id=None, status=None, target_entity=None,
                 target_type=None):
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.handshake_id = handshake_id  # type: str
        self.master_account_id = master_account_id  # type: str
        self.master_account_name = master_account_name  # type: str
        self.modify_time = modify_time  # type: str
        self.note = note  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.target_entity = target_entity  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptHandshakeResponseBodyHandshake, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class AcceptHandshakeResponseBody(TeaModel):
    def __init__(self, handshake=None, request_id=None):
        self.handshake = handshake  # type: AcceptHandshakeResponseBodyHandshake
        self.request_id = request_id  # type: str

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        _map = super(AcceptHandshakeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = AcceptHandshakeResponseBodyHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AcceptHandshakeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AcceptHandshakeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcceptHandshakeResponse, self).to_map()
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
            temp_model = AcceptHandshakeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachControlPolicyRequest(TeaModel):
    def __init__(self, policy_id=None, target_id=None):
        self.policy_id = policy_id  # type: str
        self.target_id = target_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class AttachControlPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachControlPolicyResponseBody, self).to_map()
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


class AttachControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachControlPolicyResponse, self).to_map()
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
            temp_model = AttachControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachPolicyRequest(TeaModel):
    def __init__(self, policy_name=None, policy_type=None, principal_name=None, principal_type=None,
                 resource_group_id=None):
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.principal_name = principal_name  # type: str
        self.principal_type = principal_type  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class AttachPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachPolicyResponseBody, self).to_map()
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


class AttachPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachPolicyResponse, self).to_map()
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
            temp_model = AttachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindSecureMobilePhoneRequest(TeaModel):
    def __init__(self, account_id=None, secure_mobile_phone=None, verification_code=None):
        self.account_id = account_id  # type: str
        self.secure_mobile_phone = secure_mobile_phone  # type: str
        self.verification_code = verification_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindSecureMobilePhoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.secure_mobile_phone is not None:
            result['SecureMobilePhone'] = self.secure_mobile_phone
        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('SecureMobilePhone') is not None:
            self.secure_mobile_phone = m.get('SecureMobilePhone')
        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')
        return self


class BindSecureMobilePhoneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindSecureMobilePhoneResponseBody, self).to_map()
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


class BindSecureMobilePhoneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindSecureMobilePhoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindSecureMobilePhoneResponse, self).to_map()
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
            temp_model = BindSecureMobilePhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCreateCloudAccountRequest(TeaModel):
    def __init__(self, record_id=None):
        self.record_id = record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelCreateCloudAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class CancelCreateCloudAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelCreateCloudAccountResponseBody, self).to_map()
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


class CancelCreateCloudAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelCreateCloudAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelCreateCloudAccountResponse, self).to_map()
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
            temp_model = CancelCreateCloudAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelHandshakeRequest(TeaModel):
    def __init__(self, handshake_id=None):
        self.handshake_id = handshake_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelHandshakeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class CancelHandshakeResponseBodyHandshake(TeaModel):
    def __init__(self, create_time=None, expire_time=None, handshake_id=None, master_account_id=None,
                 master_account_name=None, modify_time=None, note=None, resource_directory_id=None, status=None, target_entity=None,
                 target_type=None):
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.handshake_id = handshake_id  # type: str
        self.master_account_id = master_account_id  # type: str
        self.master_account_name = master_account_name  # type: str
        self.modify_time = modify_time  # type: str
        self.note = note  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.target_entity = target_entity  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelHandshakeResponseBodyHandshake, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CancelHandshakeResponseBody(TeaModel):
    def __init__(self, handshake=None, request_id=None):
        self.handshake = handshake  # type: CancelHandshakeResponseBodyHandshake
        self.request_id = request_id  # type: str

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        _map = super(CancelHandshakeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = CancelHandshakeResponseBodyHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelHandshakeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelHandshakeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelHandshakeResponse, self).to_map()
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
            temp_model = CancelHandshakeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPromoteResourceAccountRequest(TeaModel):
    def __init__(self, record_id=None):
        self.record_id = record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelPromoteResourceAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class CancelPromoteResourceAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelPromoteResourceAccountResponseBody, self).to_map()
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


class CancelPromoteResourceAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelPromoteResourceAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelPromoteResourceAccountResponse, self).to_map()
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
            temp_model = CancelPromoteResourceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAccountDeleteRequest(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAccountDeleteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class CheckAccountDeleteResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAccountDeleteResponseBody, self).to_map()
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


class CheckAccountDeleteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckAccountDeleteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckAccountDeleteResponse, self).to_map()
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
            temp_model = CheckAccountDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCloudAccountRequest(TeaModel):
    def __init__(self, display_name=None, email=None, parent_folder_id=None, payer_account_id=None):
        self.display_name = display_name  # type: str
        self.email = email  # type: str
        self.parent_folder_id = parent_folder_id  # type: str
        self.payer_account_id = payer_account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCloudAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        return self


class CreateCloudAccountResponseBodyAccount(TeaModel):
    def __init__(self, account_id=None, account_name=None, display_name=None, folder_id=None, join_method=None,
                 modify_time=None, record_id=None, resource_directory_id=None, status=None, type=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.display_name = display_name  # type: str
        self.folder_id = folder_id  # type: str
        self.join_method = join_method  # type: str
        self.modify_time = modify_time  # type: str
        self.record_id = record_id  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCloudAccountResponseBodyAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateCloudAccountResponseBody(TeaModel):
    def __init__(self, account=None, request_id=None):
        self.account = account  # type: CreateCloudAccountResponseBodyAccount
        self.request_id = request_id  # type: str

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super(CreateCloudAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = CreateCloudAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCloudAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCloudAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCloudAccountResponse, self).to_map()
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
            temp_model = CreateCloudAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateControlPolicyRequest(TeaModel):
    def __init__(self, description=None, effect_scope=None, policy_document=None, policy_name=None):
        self.description = description  # type: str
        self.effect_scope = effect_scope  # type: str
        self.policy_document = policy_document  # type: str
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class CreateControlPolicyResponseBodyControlPolicy(TeaModel):
    def __init__(self, attachment_count=None, create_date=None, description=None, effect_scope=None, policy_id=None,
                 policy_name=None, policy_type=None, update_date=None):
        self.attachment_count = attachment_count  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.effect_scope = effect_scope  # type: str
        self.policy_id = policy_id  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateControlPolicyResponseBodyControlPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateControlPolicyResponseBody(TeaModel):
    def __init__(self, control_policy=None, request_id=None):
        self.control_policy = control_policy  # type: CreateControlPolicyResponseBodyControlPolicy
        self.request_id = request_id  # type: str

    def validate(self):
        if self.control_policy:
            self.control_policy.validate()

    def to_map(self):
        _map = super(CreateControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policy is not None:
            result['ControlPolicy'] = self.control_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlPolicy') is not None:
            temp_model = CreateControlPolicyResponseBodyControlPolicy()
            self.control_policy = temp_model.from_map(m['ControlPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateControlPolicyResponse, self).to_map()
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
            temp_model = CreateControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFolderRequest(TeaModel):
    def __init__(self, folder_name=None, parent_folder_id=None):
        self.folder_name = folder_name  # type: str
        self.parent_folder_id = parent_folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFolderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class CreateFolderResponseBodyFolder(TeaModel):
    def __init__(self, create_time=None, folder_id=None, folder_name=None, parent_folder_id=None):
        self.create_time = create_time  # type: str
        self.folder_id = folder_id  # type: str
        self.folder_name = folder_name  # type: str
        self.parent_folder_id = parent_folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFolderResponseBodyFolder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class CreateFolderResponseBody(TeaModel):
    def __init__(self, folder=None, request_id=None):
        self.folder = folder  # type: CreateFolderResponseBodyFolder
        self.request_id = request_id  # type: str

    def validate(self):
        if self.folder:
            self.folder.validate()

    def to_map(self):
        _map = super(CreateFolderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Folder') is not None:
            temp_model = CreateFolderResponseBodyFolder()
            self.folder = temp_model.from_map(m['Folder'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFolderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFolderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFolderResponse, self).to_map()
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
            temp_model = CreateFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(self, description=None, policy_document=None, policy_name=None):
        self.description = description  # type: str
        self.policy_document = policy_document  # type: str
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class CreatePolicyResponseBodyPolicy(TeaModel):
    def __init__(self, create_date=None, default_version=None, description=None, policy_name=None, policy_type=None):
        self.create_date = create_date  # type: str
        self.default_version = default_version  # type: str
        self.description = description  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyResponseBodyPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(self, policy=None, request_id=None):
        self.policy = policy  # type: CreatePolicyResponseBodyPolicy
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(CreatePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = CreatePolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePolicyResponse, self).to_map()
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
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyVersionRequest(TeaModel):
    def __init__(self, policy_document=None, policy_name=None, set_as_default=None):
        self.policy_document = policy_document  # type: str
        self.policy_name = policy_name  # type: str
        self.set_as_default = set_as_default  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.set_as_default is not None:
            result['SetAsDefault'] = self.set_as_default
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('SetAsDefault') is not None:
            self.set_as_default = m.get('SetAsDefault')
        return self


class CreatePolicyVersionResponseBodyPolicyVersion(TeaModel):
    def __init__(self, create_date=None, is_default_version=None, version_id=None):
        self.create_date = create_date  # type: str
        self.is_default_version = is_default_version  # type: bool
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyVersionResponseBodyPolicyVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreatePolicyVersionResponseBody(TeaModel):
    def __init__(self, policy_version=None, request_id=None):
        self.policy_version = policy_version  # type: CreatePolicyVersionResponseBodyPolicyVersion
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        _map = super(CreatePolicyVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyVersion') is not None:
            temp_model = CreatePolicyVersionResponseBodyPolicyVersion()
            self.policy_version = temp_model.from_map(m['PolicyVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePolicyVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePolicyVersionResponse, self).to_map()
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
            temp_model = CreatePolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceAccountRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceAccountRequestTag, self).to_map()
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


class CreateResourceAccountRequest(TeaModel):
    def __init__(self, account_name_prefix=None, display_name=None, parent_folder_id=None, payer_account_id=None,
                 tag=None):
        self.account_name_prefix = account_name_prefix  # type: str
        self.display_name = display_name  # type: str
        self.parent_folder_id = parent_folder_id  # type: str
        self.payer_account_id = payer_account_id  # type: str
        self.tag = tag  # type: list[CreateResourceAccountRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateResourceAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNamePrefix') is not None:
            self.account_name_prefix = m.get('AccountNamePrefix')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateResourceAccountRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateResourceAccountResponseBodyAccount(TeaModel):
    def __init__(self, account_id=None, account_name=None, display_name=None, folder_id=None, join_method=None,
                 join_time=None, modify_time=None, resource_directory_id=None, status=None, type=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.display_name = display_name  # type: str
        self.folder_id = folder_id  # type: str
        self.join_method = join_method  # type: str
        self.join_time = join_time  # type: str
        self.modify_time = modify_time  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceAccountResponseBodyAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateResourceAccountResponseBody(TeaModel):
    def __init__(self, account=None, request_id=None):
        self.account = account  # type: CreateResourceAccountResponseBodyAccount
        self.request_id = request_id  # type: str

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super(CreateResourceAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = CreateResourceAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateResourceAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceAccountResponse, self).to_map()
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
            temp_model = CreateResourceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceGroupRequest(TeaModel):
    def __init__(self, display_name=None, name=None):
        self.display_name = display_name  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(self, region_id=None, status=None):
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateResourceGroupResponseBodyResourceGroupRegionStatuses(TeaModel):
    def __init__(self, region_status=None):
        self.region_status = region_status  # type: list[CreateResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus]

    def validate(self):
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateResourceGroupResponseBodyResourceGroupRegionStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = CreateResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class CreateResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(self, account_id=None, create_date=None, display_name=None, id=None, name=None,
                 region_statuses=None, status=None):
        self.account_id = account_id  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.region_statuses = region_statuses  # type: CreateResourceGroupResponseBodyResourceGroupRegionStatuses
        self.status = status  # type: str

    def validate(self):
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        _map = super(CreateResourceGroupResponseBodyResourceGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = CreateResourceGroupResponseBodyResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_group=None):
        self.request_id = request_id  # type: str
        self.resource_group = resource_group  # type: CreateResourceGroupResponseBodyResourceGroup

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super(CreateResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = CreateResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class CreateResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceGroupResponse, self).to_map()
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
            temp_model = CreateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoleRequest(TeaModel):
    def __init__(self, assume_role_policy_document=None, description=None, max_session_duration=None,
                 role_name=None):
        self.assume_role_policy_document = assume_role_policy_document  # type: str
        self.description = description  # type: str
        self.max_session_duration = max_session_duration  # type: long
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateRoleResponseBodyRole(TeaModel):
    def __init__(self, arn=None, assume_role_policy_document=None, create_date=None, description=None,
                 max_session_duration=None, role_id=None, role_name=None, role_principal_name=None):
        self.arn = arn  # type: str
        self.assume_role_policy_document = assume_role_policy_document  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.max_session_duration = max_session_duration  # type: long
        self.role_id = role_id  # type: str
        self.role_name = role_name  # type: str
        self.role_principal_name = role_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoleResponseBodyRole, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        return self


class CreateRoleResponseBody(TeaModel):
    def __init__(self, request_id=None, role=None):
        self.request_id = request_id  # type: str
        self.role = role  # type: CreateRoleResponseBodyRole

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super(CreateRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = CreateRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class CreateRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRoleResponse, self).to_map()
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
            temp_model = CreateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(self, custom_suffix=None, description=None, service_name=None):
        self.custom_suffix = custom_suffix  # type: str
        self.description = description  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_suffix is not None:
            result['CustomSuffix'] = self.custom_suffix
        if self.description is not None:
            result['Description'] = self.description
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomSuffix') is not None:
            self.custom_suffix = m.get('CustomSuffix')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateServiceLinkedRoleResponseBodyRole(TeaModel):
    def __init__(self, arn=None, assume_role_policy_document=None, create_date=None, description=None,
                 is_service_linked_role=None, role_id=None, role_name=None, role_principal_name=None):
        self.arn = arn  # type: str
        self.assume_role_policy_document = assume_role_policy_document  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.is_service_linked_role = is_service_linked_role  # type: bool
        self.role_id = role_id  # type: str
        self.role_name = role_name  # type: str
        self.role_principal_name = role_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponseBodyRole, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(self, request_id=None, role=None):
        self.request_id = request_id  # type: str
        self.role = role  # type: CreateServiceLinkedRoleResponseBodyRole

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = CreateServiceLinkedRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceLinkedRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponse, self).to_map()
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
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeclineHandshakeRequest(TeaModel):
    def __init__(self, handshake_id=None):
        self.handshake_id = handshake_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeclineHandshakeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class DeclineHandshakeResponseBodyHandshake(TeaModel):
    def __init__(self, create_time=None, expire_time=None, handshake_id=None, master_account_id=None,
                 master_account_name=None, modify_time=None, note=None, resource_directory_id=None, status=None, target_entity=None,
                 target_type=None):
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.handshake_id = handshake_id  # type: str
        self.master_account_id = master_account_id  # type: str
        self.master_account_name = master_account_name  # type: str
        self.modify_time = modify_time  # type: str
        self.note = note  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.target_entity = target_entity  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeclineHandshakeResponseBodyHandshake, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DeclineHandshakeResponseBody(TeaModel):
    def __init__(self, handshake=None, request_id=None):
        self.handshake = handshake  # type: DeclineHandshakeResponseBodyHandshake
        self.request_id = request_id  # type: str

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        _map = super(DeclineHandshakeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = DeclineHandshakeResponseBodyHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeclineHandshakeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeclineHandshakeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeclineHandshakeResponse, self).to_map()
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
            temp_model = DeclineHandshakeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(self, abandonable_check_id=None, account_id=None):
        self.abandonable_check_id = abandonable_check_id  # type: list[str]
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandonable_check_id is not None:
            result['AbandonableCheckId'] = self.abandonable_check_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbandonableCheckId') is not None:
            self.abandonable_check_id = m.get('AbandonableCheckId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DeleteAccountShrinkRequest(TeaModel):
    def __init__(self, abandonable_check_id_shrink=None, account_id=None):
        self.abandonable_check_id_shrink = abandonable_check_id_shrink  # type: str
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandonable_check_id_shrink is not None:
            result['AbandonableCheckId'] = self.abandonable_check_id_shrink
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbandonableCheckId') is not None:
            self.abandonable_check_id_shrink = m.get('AbandonableCheckId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(self, deletion_type=None, request_id=None):
        self.deletion_type = deletion_type  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_type is not None:
            result['DeletionType'] = self.deletion_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeletionType') is not None:
            self.deletion_type = m.get('DeletionType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccountResponse, self).to_map()
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
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteControlPolicyRequest(TeaModel):
    def __init__(self, policy_id=None):
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DeleteControlPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteControlPolicyResponseBody, self).to_map()
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


class DeleteControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteControlPolicyResponse, self).to_map()
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
            temp_model = DeleteControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFolderRequest(TeaModel):
    def __init__(self, folder_id=None):
        self.folder_id = folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFolderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class DeleteFolderResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFolderResponseBody, self).to_map()
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


class DeleteFolderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFolderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFolderResponse, self).to_map()
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
            temp_model = DeleteFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(self, policy_name=None):
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class DeletePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyResponseBody, self).to_map()
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


class DeletePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePolicyResponse, self).to_map()
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
            temp_model = DeletePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyVersionRequest(TeaModel):
    def __init__(self, policy_name=None, version_id=None):
        self.policy_name = policy_name  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeletePolicyVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyVersionResponseBody, self).to_map()
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


class DeletePolicyVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePolicyVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePolicyVersionResponse, self).to_map()
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
            temp_model = DeletePolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceGroupRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(self, region_id=None, status=None):
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteResourceGroupResponseBodyResourceGroupRegionStatuses(TeaModel):
    def __init__(self, region_status=None):
        self.region_status = region_status  # type: list[DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus]

    def validate(self):
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteResourceGroupResponseBodyResourceGroupRegionStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = DeleteResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class DeleteResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(self, account_id=None, create_date=None, display_name=None, id=None, name=None,
                 region_statuses=None, status=None):
        self.account_id = account_id  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.region_statuses = region_statuses  # type: DeleteResourceGroupResponseBodyResourceGroupRegionStatuses
        self.status = status  # type: str

    def validate(self):
        if self.region_statuses:
            self.region_statuses.validate()

    def to_map(self):
        _map = super(DeleteResourceGroupResponseBodyResourceGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = DeleteResourceGroupResponseBodyResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_group=None):
        self.request_id = request_id  # type: str
        self.resource_group = resource_group  # type: DeleteResourceGroupResponseBodyResourceGroup

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super(DeleteResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = DeleteResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class DeleteResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceGroupResponse, self).to_map()
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
            temp_model = DeleteResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoleRequest(TeaModel):
    def __init__(self, role_name=None):
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class DeleteRoleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRoleResponseBody, self).to_map()
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


class DeleteRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRoleResponse, self).to_map()
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
            temp_model = DeleteRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceLinkedRoleRequest(TeaModel):
    def __init__(self, role_name=None):
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class DeleteServiceLinkedRoleResponseBody(TeaModel):
    def __init__(self, deletion_task_id=None, request_id=None):
        self.deletion_task_id = deletion_task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceLinkedRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceLinkedRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServiceLinkedRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceLinkedRoleResponse, self).to_map()
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
            temp_model = DeleteServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeregisterDelegatedAdministratorRequest(TeaModel):
    def __init__(self, account_id=None, service_principal=None):
        self.account_id = account_id  # type: str
        self.service_principal = service_principal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterDelegatedAdministratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class DeregisterDelegatedAdministratorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterDelegatedAdministratorResponseBody, self).to_map()
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


class DeregisterDelegatedAdministratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeregisterDelegatedAdministratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeregisterDelegatedAdministratorResponse, self).to_map()
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
            temp_model = DeregisterDelegatedAdministratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DestroyResourceDirectoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DestroyResourceDirectoryResponseBody, self).to_map()
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


class DestroyResourceDirectoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DestroyResourceDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DestroyResourceDirectoryResponse, self).to_map()
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
            temp_model = DestroyResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachControlPolicyRequest(TeaModel):
    def __init__(self, policy_id=None, target_id=None):
        self.policy_id = policy_id  # type: str
        self.target_id = target_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class DetachControlPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachControlPolicyResponseBody, self).to_map()
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


class DetachControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachControlPolicyResponse, self).to_map()
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
            temp_model = DetachControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachPolicyRequest(TeaModel):
    def __init__(self, policy_name=None, policy_type=None, principal_name=None, principal_type=None,
                 resource_group_id=None):
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.principal_name = principal_name  # type: str
        self.principal_type = principal_type  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DetachPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachPolicyResponseBody, self).to_map()
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


class DetachPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachPolicyResponse, self).to_map()
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
            temp_model = DetachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableControlPolicyResponseBody(TeaModel):
    def __init__(self, enablement_status=None, request_id=None):
        self.enablement_status = enablement_status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enablement_status is not None:
            result['EnablementStatus'] = self.enablement_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablementStatus') is not None:
            self.enablement_status = m.get('EnablementStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableControlPolicyResponse, self).to_map()
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
            temp_model = DisableControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableControlPolicyResponseBody(TeaModel):
    def __init__(self, enablement_status=None, request_id=None):
        self.enablement_status = enablement_status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enablement_status is not None:
            result['EnablementStatus'] = self.enablement_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablementStatus') is not None:
            self.enablement_status = m.get('EnablementStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableControlPolicyResponse, self).to_map()
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
            temp_model = EnableControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableResourceDirectoryRequest(TeaModel):
    def __init__(self, enable_mode=None, maname=None, masecure_mobile_phone=None, verification_code=None):
        self.enable_mode = enable_mode  # type: str
        self.maname = maname  # type: str
        self.masecure_mobile_phone = masecure_mobile_phone  # type: str
        self.verification_code = verification_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableResourceDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_mode is not None:
            result['EnableMode'] = self.enable_mode
        if self.maname is not None:
            result['MAName'] = self.maname
        if self.masecure_mobile_phone is not None:
            result['MASecureMobilePhone'] = self.masecure_mobile_phone
        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMode') is not None:
            self.enable_mode = m.get('EnableMode')
        if m.get('MAName') is not None:
            self.maname = m.get('MAName')
        if m.get('MASecureMobilePhone') is not None:
            self.masecure_mobile_phone = m.get('MASecureMobilePhone')
        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')
        return self


class EnableResourceDirectoryResponseBodyResourceDirectory(TeaModel):
    def __init__(self, create_time=None, master_account_id=None, master_account_name=None,
                 resource_directory_id=None, root_folder_id=None):
        self.create_time = create_time  # type: str
        self.master_account_id = master_account_id  # type: str
        self.master_account_name = master_account_name  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.root_folder_id = root_folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableResourceDirectoryResponseBodyResourceDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')
        return self


class EnableResourceDirectoryResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_directory=None):
        self.request_id = request_id  # type: str
        self.resource_directory = resource_directory  # type: EnableResourceDirectoryResponseBodyResourceDirectory

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super(EnableResourceDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectory') is not None:
            temp_model = EnableResourceDirectoryResponseBodyResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        return self


class EnableResourceDirectoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableResourceDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableResourceDirectoryResponse, self).to_map()
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
            temp_model = EnableResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountRequest(TeaModel):
    def __init__(self, account_id=None, include_tags=None):
        self.account_id = account_id  # type: str
        self.include_tags = include_tags  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        return self


class GetAccountResponseBodyAccountTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountResponseBodyAccountTags, self).to_map()
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


class GetAccountResponseBodyAccount(TeaModel):
    def __init__(self, account_id=None, account_name=None, display_name=None, folder_id=None,
                 identity_information=None, join_method=None, join_time=None, location=None, modify_time=None,
                 resource_directory_id=None, resource_directory_path=None, status=None, tags=None, type=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.display_name = display_name  # type: str
        self.folder_id = folder_id  # type: str
        self.identity_information = identity_information  # type: str
        self.join_method = join_method  # type: str
        self.join_time = join_time  # type: str
        self.location = location  # type: str
        self.modify_time = modify_time  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.resource_directory_path = resource_directory_path  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: list[GetAccountResponseBodyAccountTags]
        self.type = type  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAccountResponseBodyAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.identity_information is not None:
            result['IdentityInformation'] = self.identity_information
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.location is not None:
            result['Location'] = self.location
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('IdentityInformation') is not None:
            self.identity_information = m.get('IdentityInformation')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetAccountResponseBodyAccountTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAccountResponseBody(TeaModel):
    def __init__(self, account=None, request_id=None):
        self.account = account  # type: GetAccountResponseBodyAccount
        self.request_id = request_id  # type: str

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super(GetAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = GetAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountResponse, self).to_map()
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
            temp_model = GetAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountDeletionCheckResultRequest(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountDeletionCheckResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoAbandonableChecks(TeaModel):
    def __init__(self, check_id=None, check_name=None, description=None):
        self.check_id = check_id  # type: str
        self.check_name = check_name  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoAbandonableChecks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoNotAllowReason(TeaModel):
    def __init__(self, check_id=None, check_name=None, description=None):
        self.check_id = check_id  # type: str
        self.check_name = check_name  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoNotAllowReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['CheckId'] = self.check_id
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfo(TeaModel):
    def __init__(self, abandonable_checks=None, allow_delete=None, not_allow_reason=None, status=None):
        self.abandonable_checks = abandonable_checks  # type: list[GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoAbandonableChecks]
        self.allow_delete = allow_delete  # type: str
        self.not_allow_reason = not_allow_reason  # type: list[GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoNotAllowReason]
        self.status = status  # type: str

    def validate(self):
        if self.abandonable_checks:
            for k in self.abandonable_checks:
                if k:
                    k.validate()
        if self.not_allow_reason:
            for k in self.not_allow_reason:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AbandonableChecks'] = []
        if self.abandonable_checks is not None:
            for k in self.abandonable_checks:
                result['AbandonableChecks'].append(k.to_map() if k else None)
        if self.allow_delete is not None:
            result['AllowDelete'] = self.allow_delete
        result['NotAllowReason'] = []
        if self.not_allow_reason is not None:
            for k in self.not_allow_reason:
                result['NotAllowReason'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.abandonable_checks = []
        if m.get('AbandonableChecks') is not None:
            for k in m.get('AbandonableChecks'):
                temp_model = GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoAbandonableChecks()
                self.abandonable_checks.append(temp_model.from_map(k))
        if m.get('AllowDelete') is not None:
            self.allow_delete = m.get('AllowDelete')
        self.not_allow_reason = []
        if m.get('NotAllowReason') is not None:
            for k in m.get('NotAllowReason'):
                temp_model = GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfoNotAllowReason()
                self.not_allow_reason.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAccountDeletionCheckResultResponseBody(TeaModel):
    def __init__(self, account_deletion_check_result_info=None, request_id=None):
        self.account_deletion_check_result_info = account_deletion_check_result_info  # type: GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.account_deletion_check_result_info:
            self.account_deletion_check_result_info.validate()

    def to_map(self):
        _map = super(GetAccountDeletionCheckResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_deletion_check_result_info is not None:
            result['AccountDeletionCheckResultInfo'] = self.account_deletion_check_result_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDeletionCheckResultInfo') is not None:
            temp_model = GetAccountDeletionCheckResultResponseBodyAccountDeletionCheckResultInfo()
            self.account_deletion_check_result_info = temp_model.from_map(m['AccountDeletionCheckResultInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountDeletionCheckResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountDeletionCheckResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountDeletionCheckResultResponse, self).to_map()
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
            temp_model = GetAccountDeletionCheckResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountDeletionStatusRequest(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountDeletionStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class GetAccountDeletionStatusResponseBodyRdAccountDeletionStatusFailReasonList(TeaModel):
    def __init__(self, description=None, name=None):
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountDeletionStatusResponseBodyRdAccountDeletionStatusFailReasonList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAccountDeletionStatusResponseBodyRdAccountDeletionStatus(TeaModel):
    def __init__(self, account_id=None, create_time=None, deletion_time=None, deletion_type=None,
                 fail_reason_list=None, status=None):
        self.account_id = account_id  # type: str
        self.create_time = create_time  # type: str
        self.deletion_time = deletion_time  # type: str
        self.deletion_type = deletion_type  # type: str
        self.fail_reason_list = fail_reason_list  # type: list[GetAccountDeletionStatusResponseBodyRdAccountDeletionStatusFailReasonList]
        self.status = status  # type: str

    def validate(self):
        if self.fail_reason_list:
            for k in self.fail_reason_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAccountDeletionStatusResponseBodyRdAccountDeletionStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_time is not None:
            result['DeletionTime'] = self.deletion_time
        if self.deletion_type is not None:
            result['DeletionType'] = self.deletion_type
        result['FailReasonList'] = []
        if self.fail_reason_list is not None:
            for k in self.fail_reason_list:
                result['FailReasonList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionTime') is not None:
            self.deletion_time = m.get('DeletionTime')
        if m.get('DeletionType') is not None:
            self.deletion_type = m.get('DeletionType')
        self.fail_reason_list = []
        if m.get('FailReasonList') is not None:
            for k in m.get('FailReasonList'):
                temp_model = GetAccountDeletionStatusResponseBodyRdAccountDeletionStatusFailReasonList()
                self.fail_reason_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAccountDeletionStatusResponseBody(TeaModel):
    def __init__(self, rd_account_deletion_status=None, request_id=None):
        self.rd_account_deletion_status = rd_account_deletion_status  # type: GetAccountDeletionStatusResponseBodyRdAccountDeletionStatus
        self.request_id = request_id  # type: str

    def validate(self):
        if self.rd_account_deletion_status:
            self.rd_account_deletion_status.validate()

    def to_map(self):
        _map = super(GetAccountDeletionStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rd_account_deletion_status is not None:
            result['RdAccountDeletionStatus'] = self.rd_account_deletion_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RdAccountDeletionStatus') is not None:
            temp_model = GetAccountDeletionStatusResponseBodyRdAccountDeletionStatus()
            self.rd_account_deletion_status = temp_model.from_map(m['RdAccountDeletionStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountDeletionStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountDeletionStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountDeletionStatusResponse, self).to_map()
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
            temp_model = GetAccountDeletionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetControlPolicyRequest(TeaModel):
    def __init__(self, language=None, policy_id=None):
        self.language = language  # type: str
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class GetControlPolicyResponseBodyControlPolicy(TeaModel):
    def __init__(self, attachment_count=None, create_date=None, description=None, effect_scope=None,
                 policy_document=None, policy_id=None, policy_name=None, policy_type=None, update_date=None):
        self.attachment_count = attachment_count  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.effect_scope = effect_scope  # type: str
        self.policy_document = policy_document  # type: str
        self.policy_id = policy_id  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetControlPolicyResponseBodyControlPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetControlPolicyResponseBody(TeaModel):
    def __init__(self, control_policy=None, request_id=None):
        self.control_policy = control_policy  # type: GetControlPolicyResponseBodyControlPolicy
        self.request_id = request_id  # type: str

    def validate(self):
        if self.control_policy:
            self.control_policy.validate()

    def to_map(self):
        _map = super(GetControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policy is not None:
            result['ControlPolicy'] = self.control_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlPolicy') is not None:
            temp_model = GetControlPolicyResponseBodyControlPolicy()
            self.control_policy = temp_model.from_map(m['ControlPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetControlPolicyResponse, self).to_map()
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
            temp_model = GetControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetControlPolicyEnablementStatusResponseBody(TeaModel):
    def __init__(self, enablement_status=None, request_id=None):
        self.enablement_status = enablement_status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetControlPolicyEnablementStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enablement_status is not None:
            result['EnablementStatus'] = self.enablement_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablementStatus') is not None:
            self.enablement_status = m.get('EnablementStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetControlPolicyEnablementStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetControlPolicyEnablementStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetControlPolicyEnablementStatusResponse, self).to_map()
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
            temp_model = GetControlPolicyEnablementStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFolderRequest(TeaModel):
    def __init__(self, folder_id=None):
        self.folder_id = folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFolderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        return self


class GetFolderResponseBodyFolder(TeaModel):
    def __init__(self, create_time=None, folder_id=None, folder_name=None, parent_folder_id=None,
                 resource_directory_path=None):
        self.create_time = create_time  # type: str
        self.folder_id = folder_id  # type: str
        self.folder_name = folder_name  # type: str
        self.parent_folder_id = parent_folder_id  # type: str
        self.resource_directory_path = resource_directory_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFolderResponseBodyFolder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')
        return self


class GetFolderResponseBody(TeaModel):
    def __init__(self, folder=None, request_id=None):
        self.folder = folder  # type: GetFolderResponseBodyFolder
        self.request_id = request_id  # type: str

    def validate(self):
        if self.folder:
            self.folder.validate()

    def to_map(self):
        _map = super(GetFolderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Folder') is not None:
            temp_model = GetFolderResponseBodyFolder()
            self.folder = temp_model.from_map(m['Folder'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFolderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFolderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFolderResponse, self).to_map()
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
            temp_model = GetFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHandshakeRequest(TeaModel):
    def __init__(self, handshake_id=None):
        self.handshake_id = handshake_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHandshakeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        return self


class GetHandshakeResponseBodyHandshake(TeaModel):
    def __init__(self, create_time=None, expire_time=None, handshake_id=None, invited_account_real_name=None,
                 master_account_id=None, master_account_name=None, master_account_real_name=None, modify_time=None, note=None,
                 resource_directory_id=None, status=None, target_entity=None, target_type=None):
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.handshake_id = handshake_id  # type: str
        self.invited_account_real_name = invited_account_real_name  # type: str
        self.master_account_id = master_account_id  # type: str
        self.master_account_name = master_account_name  # type: str
        self.master_account_real_name = master_account_real_name  # type: str
        self.modify_time = modify_time  # type: str
        self.note = note  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.target_entity = target_entity  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHandshakeResponseBodyHandshake, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.invited_account_real_name is not None:
            result['InvitedAccountRealName'] = self.invited_account_real_name
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.master_account_real_name is not None:
            result['MasterAccountRealName'] = self.master_account_real_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('InvitedAccountRealName') is not None:
            self.invited_account_real_name = m.get('InvitedAccountRealName')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('MasterAccountRealName') is not None:
            self.master_account_real_name = m.get('MasterAccountRealName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetHandshakeResponseBody(TeaModel):
    def __init__(self, handshake=None, request_id=None):
        self.handshake = handshake  # type: GetHandshakeResponseBodyHandshake
        self.request_id = request_id  # type: str

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        _map = super(GetHandshakeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = GetHandshakeResponseBodyHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHandshakeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHandshakeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHandshakeResponse, self).to_map()
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
            temp_model = GetHandshakeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPayerForAccountRequest(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPayerForAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class GetPayerForAccountResponseBody(TeaModel):
    def __init__(self, payer_account_id=None, payer_account_name=None, request_id=None):
        self.payer_account_id = payer_account_id  # type: str
        self.payer_account_name = payer_account_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPayerForAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id
        if self.payer_account_name is not None:
            result['PayerAccountName'] = self.payer_account_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')
        if m.get('PayerAccountName') is not None:
            self.payer_account_name = m.get('PayerAccountName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPayerForAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPayerForAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPayerForAccountResponse, self).to_map()
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
            temp_model = GetPayerForAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyRequest(TeaModel):
    def __init__(self, language=None, policy_name=None, policy_type=None):
        self.language = language  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class GetPolicyResponseBodyPolicy(TeaModel):
    def __init__(self, attachment_count=None, create_date=None, default_version=None, description=None,
                 policy_document=None, policy_name=None, policy_type=None, update_date=None):
        self.attachment_count = attachment_count  # type: int
        self.create_date = create_date  # type: str
        self.default_version = default_version  # type: str
        self.description = description  # type: str
        self.policy_document = policy_document  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolicyResponseBodyPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetPolicyResponseBody(TeaModel):
    def __init__(self, policy=None, request_id=None):
        self.policy = policy  # type: GetPolicyResponseBodyPolicy
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(GetPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = GetPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPolicyResponse, self).to_map()
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
            temp_model = GetPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyVersionRequest(TeaModel):
    def __init__(self, policy_name=None, policy_type=None, version_id=None):
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolicyVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetPolicyVersionResponseBodyPolicyVersion(TeaModel):
    def __init__(self, create_date=None, is_default_version=None, policy_document=None, version_id=None):
        self.create_date = create_date  # type: str
        self.is_default_version = is_default_version  # type: bool
        self.policy_document = policy_document  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolicyVersionResponseBodyPolicyVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetPolicyVersionResponseBody(TeaModel):
    def __init__(self, policy_version=None, request_id=None):
        self.policy_version = policy_version  # type: GetPolicyVersionResponseBodyPolicyVersion
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy_version:
            self.policy_version.validate()

    def to_map(self):
        _map = super(GetPolicyVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyVersion') is not None:
            temp_model = GetPolicyVersionResponseBodyPolicyVersion()
            self.policy_version = temp_model.from_map(m['PolicyVersion'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolicyVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPolicyVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPolicyVersionResponse, self).to_map()
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
            temp_model = GetPolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceDirectoryResponseBodyResourceDirectory(TeaModel):
    def __init__(self, control_policy_status=None, create_time=None, identity_information=None,
                 master_account_id=None, master_account_name=None, member_deletion_status=None, resource_directory_id=None,
                 root_folder_id=None):
        self.control_policy_status = control_policy_status  # type: str
        self.create_time = create_time  # type: str
        self.identity_information = identity_information  # type: str
        self.master_account_id = master_account_id  # type: str
        self.master_account_name = master_account_name  # type: str
        self.member_deletion_status = member_deletion_status  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.root_folder_id = root_folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceDirectoryResponseBodyResourceDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policy_status is not None:
            result['ControlPolicyStatus'] = self.control_policy_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.identity_information is not None:
            result['IdentityInformation'] = self.identity_information
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.member_deletion_status is not None:
            result['MemberDeletionStatus'] = self.member_deletion_status
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlPolicyStatus') is not None:
            self.control_policy_status = m.get('ControlPolicyStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IdentityInformation') is not None:
            self.identity_information = m.get('IdentityInformation')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('MemberDeletionStatus') is not None:
            self.member_deletion_status = m.get('MemberDeletionStatus')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')
        return self


class GetResourceDirectoryResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_directory=None):
        self.request_id = request_id  # type: str
        self.resource_directory = resource_directory  # type: GetResourceDirectoryResponseBodyResourceDirectory

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super(GetResourceDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectory') is not None:
            temp_model = GetResourceDirectoryResponseBodyResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        return self


class GetResourceDirectoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceDirectoryResponse, self).to_map()
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
            temp_model = GetResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupRequest(TeaModel):
    def __init__(self, include_tags=None, resource_group_id=None):
        self.include_tags = include_tags  # type: bool
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus(TeaModel):
    def __init__(self, region_id=None, status=None):
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetResourceGroupResponseBodyResourceGroupRegionStatuses(TeaModel):
    def __init__(self, region_status=None):
        self.region_status = region_status  # type: list[GetResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus]

    def validate(self):
        if self.region_status:
            for k in self.region_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourceGroupResponseBodyResourceGroupRegionStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionStatus'] = []
        if self.region_status is not None:
            for k in self.region_status:
                result['RegionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region_status = []
        if m.get('RegionStatus') is not None:
            for k in m.get('RegionStatus'):
                temp_model = GetResourceGroupResponseBodyResourceGroupRegionStatusesRegionStatus()
                self.region_status.append(temp_model.from_map(k))
        return self


class GetResourceGroupResponseBodyResourceGroupTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceGroupResponseBodyResourceGroupTagsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetResourceGroupResponseBodyResourceGroupTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[GetResourceGroupResponseBodyResourceGroupTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourceGroupResponseBodyResourceGroupTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetResourceGroupResponseBodyResourceGroupTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(self, account_id=None, create_date=None, display_name=None, id=None, name=None,
                 region_statuses=None, status=None, tags=None):
        self.account_id = account_id  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.region_statuses = region_statuses  # type: GetResourceGroupResponseBodyResourceGroupRegionStatuses
        self.status = status  # type: str
        self.tags = tags  # type: GetResourceGroupResponseBodyResourceGroupTags

    def validate(self):
        if self.region_statuses:
            self.region_statuses.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(GetResourceGroupResponseBodyResourceGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_statuses is not None:
            result['RegionStatuses'] = self.region_statuses.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionStatuses') is not None:
            temp_model = GetResourceGroupResponseBodyResourceGroupRegionStatuses()
            self.region_statuses = temp_model.from_map(m['RegionStatuses'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = GetResourceGroupResponseBodyResourceGroupTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class GetResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_group=None):
        self.request_id = request_id  # type: str
        self.resource_group = resource_group  # type: GetResourceGroupResponseBodyResourceGroup

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super(GetResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = GetResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class GetResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceGroupResponse, self).to_map()
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
            temp_model = GetResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupListAclModeResponseBody(TeaModel):
    def __init__(self, mode=None, request_id=None):
        self.mode = mode  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceGroupListAclModeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceGroupListAclModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceGroupListAclModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceGroupListAclModeResponse, self).to_map()
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
            temp_model = GetResourceGroupListAclModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleRequest(TeaModel):
    def __init__(self, language=None, role_name=None):
        self.language = language  # type: str
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetRoleResponseBodyRoleLatestDeletionTask(TeaModel):
    def __init__(self, create_date=None, deletion_task_id=None):
        self.create_date = create_date  # type: str
        self.deletion_task_id = deletion_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRoleResponseBodyRoleLatestDeletionTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class GetRoleResponseBodyRole(TeaModel):
    def __init__(self, arn=None, assume_role_policy_document=None, create_date=None, description=None,
                 is_service_linked_role=None, latest_deletion_task=None, max_session_duration=None, role_id=None, role_name=None,
                 role_principal_name=None, update_date=None):
        self.arn = arn  # type: str
        self.assume_role_policy_document = assume_role_policy_document  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.is_service_linked_role = is_service_linked_role  # type: bool
        self.latest_deletion_task = latest_deletion_task  # type: GetRoleResponseBodyRoleLatestDeletionTask
        self.max_session_duration = max_session_duration  # type: long
        self.role_id = role_id  # type: str
        self.role_name = role_name  # type: str
        self.role_principal_name = role_principal_name  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        _map = super(GetRoleResponseBodyRole, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('LatestDeletionTask') is not None:
            temp_model = GetRoleResponseBodyRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m['LatestDeletionTask'])
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetRoleResponseBody(TeaModel):
    def __init__(self, request_id=None, role=None):
        self.request_id = request_id  # type: str
        self.role = role  # type: GetRoleResponseBodyRole

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super(GetRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = GetRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class GetRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRoleResponse, self).to_map()
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
            temp_model = GetRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceLinkedRoleDeletionStatusRequest(TeaModel):
    def __init__(self, deletion_task_id=None):
        self.deletion_task_id = deletion_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceLinkedRoleDeletionStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources(TeaModel):
    def __init__(self, resource=None):
        self.resource = resource  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage(TeaModel):
    def __init__(self, region=None, resources=None):
        self.region = region  # type: str
        self.resources = resources  # type: GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super(GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsageResources()
            self.resources = temp_model.from_map(m['Resources'])
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages(TeaModel):
    def __init__(self, role_usage=None):
        self.role_usage = role_usage  # type: list[GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage]

    def validate(self):
        if self.role_usage:
            for k in self.role_usage:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoleUsage'] = []
        if self.role_usage is not None:
            for k in self.role_usage:
                result['RoleUsage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.role_usage = []
        if m.get('RoleUsage') is not None:
            for k in m.get('RoleUsage'):
                temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsagesRoleUsage()
                self.role_usage.append(temp_model.from_map(k))
        return self


class GetServiceLinkedRoleDeletionStatusResponseBodyReason(TeaModel):
    def __init__(self, message=None, role_usages=None):
        self.message = message  # type: str
        self.role_usages = role_usages  # type: GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages

    def validate(self):
        if self.role_usages:
            self.role_usages.validate()

    def to_map(self):
        _map = super(GetServiceLinkedRoleDeletionStatusResponseBodyReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.role_usages is not None:
            result['RoleUsages'] = self.role_usages.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RoleUsages') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReasonRoleUsages()
            self.role_usages = temp_model.from_map(m['RoleUsages'])
        return self


class GetServiceLinkedRoleDeletionStatusResponseBody(TeaModel):
    def __init__(self, reason=None, request_id=None, status=None):
        self.reason = reason  # type: GetServiceLinkedRoleDeletionStatusResponseBodyReason
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super(GetServiceLinkedRoleDeletionStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Reason') is not None:
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBodyReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetServiceLinkedRoleDeletionStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServiceLinkedRoleDeletionStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceLinkedRoleDeletionStatusResponse, self).to_map()
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
            temp_model = GetServiceLinkedRoleDeletionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitResourceDirectoryResponseBodyResourceDirectory(TeaModel):
    def __init__(self, create_time=None, master_account_id=None, master_account_name=None,
                 resource_directory_id=None, root_folder_id=None):
        self.create_time = create_time  # type: str
        self.master_account_id = master_account_id  # type: str
        self.master_account_name = master_account_name  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.root_folder_id = root_folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitResourceDirectoryResponseBodyResourceDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.root_folder_id is not None:
            result['RootFolderId'] = self.root_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('RootFolderId') is not None:
            self.root_folder_id = m.get('RootFolderId')
        return self


class InitResourceDirectoryResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_directory=None):
        self.request_id = request_id  # type: str
        self.resource_directory = resource_directory  # type: InitResourceDirectoryResponseBodyResourceDirectory

    def validate(self):
        if self.resource_directory:
            self.resource_directory.validate()

    def to_map(self):
        _map = super(InitResourceDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory is not None:
            result['ResourceDirectory'] = self.resource_directory.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectory') is not None:
            temp_model = InitResourceDirectoryResponseBodyResourceDirectory()
            self.resource_directory = temp_model.from_map(m['ResourceDirectory'])
        return self


class InitResourceDirectoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitResourceDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitResourceDirectoryResponse, self).to_map()
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
            temp_model = InitResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InviteAccountToResourceDirectoryRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InviteAccountToResourceDirectoryRequestTag, self).to_map()
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


class InviteAccountToResourceDirectoryRequest(TeaModel):
    def __init__(self, note=None, tag=None, target_entity=None, target_type=None):
        self.note = note  # type: str
        self.tag = tag  # type: list[InviteAccountToResourceDirectoryRequestTag]
        self.target_entity = target_entity  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InviteAccountToResourceDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.note is not None:
            result['Note'] = self.note
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Note') is not None:
            self.note = m.get('Note')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = InviteAccountToResourceDirectoryRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class InviteAccountToResourceDirectoryResponseBodyHandshake(TeaModel):
    def __init__(self, create_time=None, expire_time=None, handshake_id=None, master_account_id=None,
                 master_account_name=None, modify_time=None, note=None, resource_directory_id=None, status=None, target_entity=None,
                 target_type=None):
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.handshake_id = handshake_id  # type: str
        self.master_account_id = master_account_id  # type: str
        self.master_account_name = master_account_name  # type: str
        self.modify_time = modify_time  # type: str
        self.note = note  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.target_entity = target_entity  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InviteAccountToResourceDirectoryResponseBodyHandshake, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class InviteAccountToResourceDirectoryResponseBody(TeaModel):
    def __init__(self, handshake=None, request_id=None):
        self.handshake = handshake  # type: InviteAccountToResourceDirectoryResponseBodyHandshake
        self.request_id = request_id  # type: str

    def validate(self):
        if self.handshake:
            self.handshake.validate()

    def to_map(self):
        _map = super(InviteAccountToResourceDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshake is not None:
            result['Handshake'] = self.handshake.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Handshake') is not None:
            temp_model = InviteAccountToResourceDirectoryResponseBodyHandshake()
            self.handshake = temp_model.from_map(m['Handshake'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InviteAccountToResourceDirectoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InviteAccountToResourceDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InviteAccountToResourceDirectoryResponse, self).to_map()
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
            temp_model = InviteAccountToResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountsRequestTag, self).to_map()
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


class ListAccountsRequest(TeaModel):
    def __init__(self, include_tags=None, page_number=None, page_size=None, tag=None):
        self.include_tags = include_tags  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.tag = tag  # type: list[ListAccountsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccountsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAccountsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAccountsResponseBodyAccountsAccountTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountsResponseBodyAccountsAccountTagsTag, self).to_map()
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


class ListAccountsResponseBodyAccountsAccountTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[ListAccountsResponseBodyAccountsAccountTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccountsResponseBodyAccountsAccountTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAccountsResponseBodyAccountsAccountTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAccountsResponseBodyAccountsAccount(TeaModel):
    def __init__(self, account_id=None, display_name=None, folder_id=None, join_method=None, join_time=None,
                 modify_time=None, resource_directory_id=None, resource_directory_path=None, status=None, tags=None, type=None):
        self.account_id = account_id  # type: str
        self.display_name = display_name  # type: str
        self.folder_id = folder_id  # type: str
        self.join_method = join_method  # type: str
        self.join_time = join_time  # type: str
        self.modify_time = modify_time  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.resource_directory_path = resource_directory_path  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: ListAccountsResponseBodyAccountsAccountTags
        self.type = type  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(ListAccountsResponseBodyAccountsAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = ListAccountsResponseBodyAccountsAccountTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAccountsResponseBodyAccounts(TeaModel):
    def __init__(self, account=None):
        self.account = account  # type: list[ListAccountsResponseBodyAccountsAccount]

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccountsResponseBodyAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListAccountsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListAccountsResponseBody(TeaModel):
    def __init__(self, accounts=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.accounts = accounts  # type: ListAccountsResponseBodyAccounts
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super(ListAccountsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = ListAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccountsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccountsResponse, self).to_map()
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
            temp_model = ListAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsForParentRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountsForParentRequestTag, self).to_map()
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


class ListAccountsForParentRequest(TeaModel):
    def __init__(self, include_tags=None, page_number=None, page_size=None, parent_folder_id=None,
                 query_keyword=None, tag=None):
        self.include_tags = include_tags  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.parent_folder_id = parent_folder_id  # type: str
        self.query_keyword = query_keyword  # type: str
        self.tag = tag  # type: list[ListAccountsForParentRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccountsForParentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAccountsForParentRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAccountsForParentResponseBodyAccountsAccountTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountsForParentResponseBodyAccountsAccountTagsTag, self).to_map()
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


class ListAccountsForParentResponseBodyAccountsAccountTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[ListAccountsForParentResponseBodyAccountsAccountTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccountsForParentResponseBodyAccountsAccountTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAccountsForParentResponseBodyAccountsAccountTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAccountsForParentResponseBodyAccountsAccount(TeaModel):
    def __init__(self, account_id=None, display_name=None, folder_id=None, join_method=None, join_time=None,
                 modify_time=None, resource_directory_id=None, status=None, tags=None, type=None):
        self.account_id = account_id  # type: str
        self.display_name = display_name  # type: str
        self.folder_id = folder_id  # type: str
        self.join_method = join_method  # type: str
        self.join_time = join_time  # type: str
        self.modify_time = modify_time  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: ListAccountsForParentResponseBodyAccountsAccountTags
        self.type = type  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(ListAccountsForParentResponseBodyAccountsAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = ListAccountsForParentResponseBodyAccountsAccountTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAccountsForParentResponseBodyAccounts(TeaModel):
    def __init__(self, account=None):
        self.account = account  # type: list[ListAccountsForParentResponseBodyAccountsAccount]

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccountsForParentResponseBodyAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListAccountsForParentResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListAccountsForParentResponseBody(TeaModel):
    def __init__(self, accounts=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.accounts = accounts  # type: ListAccountsForParentResponseBodyAccounts
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super(ListAccountsForParentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = ListAccountsForParentResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccountsForParentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccountsForParentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccountsForParentResponse, self).to_map()
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
            temp_model = ListAccountsForParentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAncestorsRequest(TeaModel):
    def __init__(self, child_id=None):
        self.child_id = child_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAncestorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_id is not None:
            result['ChildId'] = self.child_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChildId') is not None:
            self.child_id = m.get('ChildId')
        return self


class ListAncestorsResponseBodyFoldersFolder(TeaModel):
    def __init__(self, create_time=None, folder_id=None, folder_name=None):
        self.create_time = create_time  # type: str
        self.folder_id = folder_id  # type: str
        self.folder_name = folder_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAncestorsResponseBodyFoldersFolder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        return self


class ListAncestorsResponseBodyFolders(TeaModel):
    def __init__(self, folder=None):
        self.folder = folder  # type: list[ListAncestorsResponseBodyFoldersFolder]

    def validate(self):
        if self.folder:
            for k in self.folder:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAncestorsResponseBodyFolders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Folder'] = []
        if self.folder is not None:
            for k in self.folder:
                result['Folder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.folder = []
        if m.get('Folder') is not None:
            for k in m.get('Folder'):
                temp_model = ListAncestorsResponseBodyFoldersFolder()
                self.folder.append(temp_model.from_map(k))
        return self


class ListAncestorsResponseBody(TeaModel):
    def __init__(self, folders=None, request_id=None):
        self.folders = folders  # type: ListAncestorsResponseBodyFolders
        self.request_id = request_id  # type: str

    def validate(self):
        if self.folders:
            self.folders.validate()

    def to_map(self):
        _map = super(ListAncestorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Folders') is not None:
            temp_model = ListAncestorsResponseBodyFolders()
            self.folders = temp_model.from_map(m['Folders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAncestorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAncestorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAncestorsResponse, self).to_map()
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
            temp_model = ListAncestorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListControlPoliciesRequest(TeaModel):
    def __init__(self, language=None, page_number=None, page_size=None, policy_type=None):
        self.language = language  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policy_type = policy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListControlPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListControlPoliciesResponseBodyControlPoliciesControlPolicy(TeaModel):
    def __init__(self, attachment_count=None, create_date=None, description=None, effect_scope=None, policy_id=None,
                 policy_name=None, policy_type=None, update_date=None):
        self.attachment_count = attachment_count  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.effect_scope = effect_scope  # type: str
        self.policy_id = policy_id  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListControlPoliciesResponseBodyControlPoliciesControlPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListControlPoliciesResponseBodyControlPolicies(TeaModel):
    def __init__(self, control_policy=None):
        self.control_policy = control_policy  # type: list[ListControlPoliciesResponseBodyControlPoliciesControlPolicy]

    def validate(self):
        if self.control_policy:
            for k in self.control_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListControlPoliciesResponseBodyControlPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ControlPolicy'] = []
        if self.control_policy is not None:
            for k in self.control_policy:
                result['ControlPolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.control_policy = []
        if m.get('ControlPolicy') is not None:
            for k in m.get('ControlPolicy'):
                temp_model = ListControlPoliciesResponseBodyControlPoliciesControlPolicy()
                self.control_policy.append(temp_model.from_map(k))
        return self


class ListControlPoliciesResponseBody(TeaModel):
    def __init__(self, control_policies=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.control_policies = control_policies  # type: ListControlPoliciesResponseBodyControlPolicies
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.control_policies:
            self.control_policies.validate()

    def to_map(self):
        _map = super(ListControlPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policies is not None:
            result['ControlPolicies'] = self.control_policies.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlPolicies') is not None:
            temp_model = ListControlPoliciesResponseBodyControlPolicies()
            self.control_policies = temp_model.from_map(m['ControlPolicies'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListControlPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListControlPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListControlPoliciesResponse, self).to_map()
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
            temp_model = ListControlPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListControlPolicyAttachmentsForTargetRequest(TeaModel):
    def __init__(self, language=None, target_id=None):
        self.language = language  # type: str
        self.target_id = target_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListControlPolicyAttachmentsForTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachmentsControlPolicyAttachment(TeaModel):
    def __init__(self, attach_date=None, description=None, effect_scope=None, policy_id=None, policy_name=None,
                 policy_type=None):
        self.attach_date = attach_date  # type: str
        self.description = description  # type: str
        self.effect_scope = effect_scope  # type: str
        self.policy_id = policy_id  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachmentsControlPolicyAttachment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachments(TeaModel):
    def __init__(self, control_policy_attachment=None):
        self.control_policy_attachment = control_policy_attachment  # type: list[ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachmentsControlPolicyAttachment]

    def validate(self):
        if self.control_policy_attachment:
            for k in self.control_policy_attachment:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ControlPolicyAttachment'] = []
        if self.control_policy_attachment is not None:
            for k in self.control_policy_attachment:
                result['ControlPolicyAttachment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.control_policy_attachment = []
        if m.get('ControlPolicyAttachment') is not None:
            for k in m.get('ControlPolicyAttachment'):
                temp_model = ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachmentsControlPolicyAttachment()
                self.control_policy_attachment.append(temp_model.from_map(k))
        return self


class ListControlPolicyAttachmentsForTargetResponseBody(TeaModel):
    def __init__(self, control_policy_attachments=None, request_id=None):
        self.control_policy_attachments = control_policy_attachments  # type: ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachments
        self.request_id = request_id  # type: str

    def validate(self):
        if self.control_policy_attachments:
            self.control_policy_attachments.validate()

    def to_map(self):
        _map = super(ListControlPolicyAttachmentsForTargetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policy_attachments is not None:
            result['ControlPolicyAttachments'] = self.control_policy_attachments.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlPolicyAttachments') is not None:
            temp_model = ListControlPolicyAttachmentsForTargetResponseBodyControlPolicyAttachments()
            self.control_policy_attachments = temp_model.from_map(m['ControlPolicyAttachments'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListControlPolicyAttachmentsForTargetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListControlPolicyAttachmentsForTargetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListControlPolicyAttachmentsForTargetResponse, self).to_map()
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
            temp_model = ListControlPolicyAttachmentsForTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDelegatedAdministratorsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, service_principal=None):
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.service_principal = service_principal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDelegatedAdministratorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class ListDelegatedAdministratorsResponseBodyAccountsAccount(TeaModel):
    def __init__(self, account_id=None, delegation_enabled_time=None, display_name=None, join_method=None,
                 service_principal=None):
        self.account_id = account_id  # type: str
        self.delegation_enabled_time = delegation_enabled_time  # type: str
        self.display_name = display_name  # type: str
        self.join_method = join_method  # type: str
        self.service_principal = service_principal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDelegatedAdministratorsResponseBodyAccountsAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.delegation_enabled_time is not None:
            result['DelegationEnabledTime'] = self.delegation_enabled_time
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DelegationEnabledTime') is not None:
            self.delegation_enabled_time = m.get('DelegationEnabledTime')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class ListDelegatedAdministratorsResponseBodyAccounts(TeaModel):
    def __init__(self, account=None):
        self.account = account  # type: list[ListDelegatedAdministratorsResponseBodyAccountsAccount]

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDelegatedAdministratorsResponseBodyAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = ListDelegatedAdministratorsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class ListDelegatedAdministratorsResponseBody(TeaModel):
    def __init__(self, accounts=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.accounts = accounts  # type: ListDelegatedAdministratorsResponseBodyAccounts
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super(ListDelegatedAdministratorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = ListDelegatedAdministratorsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDelegatedAdministratorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDelegatedAdministratorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDelegatedAdministratorsResponse, self).to_map()
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
            temp_model = ListDelegatedAdministratorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDelegatedServicesForAccountRequest(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDelegatedServicesForAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService(TeaModel):
    def __init__(self, delegation_enabled_time=None, service_principal=None, status=None):
        self.delegation_enabled_time = delegation_enabled_time  # type: str
        self.service_principal = service_principal  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delegation_enabled_time is not None:
            result['DelegationEnabledTime'] = self.delegation_enabled_time
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DelegationEnabledTime') is not None:
            self.delegation_enabled_time = m.get('DelegationEnabledTime')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDelegatedServicesForAccountResponseBodyDelegatedServices(TeaModel):
    def __init__(self, delegated_service=None):
        self.delegated_service = delegated_service  # type: list[ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService]

    def validate(self):
        if self.delegated_service:
            for k in self.delegated_service:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDelegatedServicesForAccountResponseBodyDelegatedServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DelegatedService'] = []
        if self.delegated_service is not None:
            for k in self.delegated_service:
                result['DelegatedService'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.delegated_service = []
        if m.get('DelegatedService') is not None:
            for k in m.get('DelegatedService'):
                temp_model = ListDelegatedServicesForAccountResponseBodyDelegatedServicesDelegatedService()
                self.delegated_service.append(temp_model.from_map(k))
        return self


class ListDelegatedServicesForAccountResponseBody(TeaModel):
    def __init__(self, delegated_services=None, request_id=None):
        self.delegated_services = delegated_services  # type: ListDelegatedServicesForAccountResponseBodyDelegatedServices
        self.request_id = request_id  # type: str

    def validate(self):
        if self.delegated_services:
            self.delegated_services.validate()

    def to_map(self):
        _map = super(ListDelegatedServicesForAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delegated_services is not None:
            result['DelegatedServices'] = self.delegated_services.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DelegatedServices') is not None:
            temp_model = ListDelegatedServicesForAccountResponseBodyDelegatedServices()
            self.delegated_services = temp_model.from_map(m['DelegatedServices'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDelegatedServicesForAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDelegatedServicesForAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDelegatedServicesForAccountResponse, self).to_map()
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
            temp_model = ListDelegatedServicesForAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoldersForParentRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, parent_folder_id=None, query_keyword=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.parent_folder_id = parent_folder_id  # type: str
        self.query_keyword = query_keyword  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFoldersForParentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        return self


class ListFoldersForParentResponseBodyFoldersFolder(TeaModel):
    def __init__(self, create_time=None, folder_id=None, folder_name=None):
        self.create_time = create_time  # type: str
        self.folder_id = folder_id  # type: str
        self.folder_name = folder_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFoldersForParentResponseBodyFoldersFolder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        return self


class ListFoldersForParentResponseBodyFolders(TeaModel):
    def __init__(self, folder=None):
        self.folder = folder  # type: list[ListFoldersForParentResponseBodyFoldersFolder]

    def validate(self):
        if self.folder:
            for k in self.folder:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFoldersForParentResponseBodyFolders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Folder'] = []
        if self.folder is not None:
            for k in self.folder:
                result['Folder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.folder = []
        if m.get('Folder') is not None:
            for k in m.get('Folder'):
                temp_model = ListFoldersForParentResponseBodyFoldersFolder()
                self.folder.append(temp_model.from_map(k))
        return self


class ListFoldersForParentResponseBody(TeaModel):
    def __init__(self, folders=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.folders = folders  # type: ListFoldersForParentResponseBodyFolders
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.folders:
            self.folders.validate()

    def to_map(self):
        _map = super(ListFoldersForParentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Folders') is not None:
            temp_model = ListFoldersForParentResponseBodyFolders()
            self.folders = temp_model.from_map(m['Folders'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFoldersForParentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFoldersForParentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFoldersForParentResponse, self).to_map()
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
            temp_model = ListFoldersForParentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHandshakesForAccountRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHandshakesForAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHandshakesForAccountResponseBodyHandshakesHandshake(TeaModel):
    def __init__(self, create_time=None, expire_time=None, handshake_id=None, master_account_id=None,
                 master_account_name=None, modify_time=None, note=None, resource_directory_id=None, status=None, target_entity=None,
                 target_type=None):
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.handshake_id = handshake_id  # type: str
        self.master_account_id = master_account_id  # type: str
        self.master_account_name = master_account_name  # type: str
        self.modify_time = modify_time  # type: str
        self.note = note  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.target_entity = target_entity  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHandshakesForAccountResponseBodyHandshakesHandshake, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListHandshakesForAccountResponseBodyHandshakes(TeaModel):
    def __init__(self, handshake=None):
        self.handshake = handshake  # type: list[ListHandshakesForAccountResponseBodyHandshakesHandshake]

    def validate(self):
        if self.handshake:
            for k in self.handshake:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHandshakesForAccountResponseBodyHandshakes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Handshake'] = []
        if self.handshake is not None:
            for k in self.handshake:
                result['Handshake'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.handshake = []
        if m.get('Handshake') is not None:
            for k in m.get('Handshake'):
                temp_model = ListHandshakesForAccountResponseBodyHandshakesHandshake()
                self.handshake.append(temp_model.from_map(k))
        return self


class ListHandshakesForAccountResponseBody(TeaModel):
    def __init__(self, handshakes=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.handshakes = handshakes  # type: ListHandshakesForAccountResponseBodyHandshakes
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.handshakes:
            self.handshakes.validate()

    def to_map(self):
        _map = super(ListHandshakesForAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshakes is not None:
            result['Handshakes'] = self.handshakes.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Handshakes') is not None:
            temp_model = ListHandshakesForAccountResponseBodyHandshakes()
            self.handshakes = temp_model.from_map(m['Handshakes'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHandshakesForAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHandshakesForAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHandshakesForAccountResponse, self).to_map()
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
            temp_model = ListHandshakesForAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHandshakesForResourceDirectoryRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHandshakesForResourceDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListHandshakesForResourceDirectoryResponseBodyHandshakesHandshake(TeaModel):
    def __init__(self, create_time=None, expire_time=None, handshake_id=None, master_account_id=None,
                 master_account_name=None, modify_time=None, note=None, resource_directory_id=None, status=None, target_entity=None,
                 target_type=None):
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.handshake_id = handshake_id  # type: str
        self.master_account_id = master_account_id  # type: str
        self.master_account_name = master_account_name  # type: str
        self.modify_time = modify_time  # type: str
        self.note = note  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.target_entity = target_entity  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHandshakesForResourceDirectoryResponseBodyHandshakesHandshake, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.handshake_id is not None:
            result['HandshakeId'] = self.handshake_id
        if self.master_account_id is not None:
            result['MasterAccountId'] = self.master_account_id
        if self.master_account_name is not None:
            result['MasterAccountName'] = self.master_account_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.note is not None:
            result['Note'] = self.note
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HandshakeId') is not None:
            self.handshake_id = m.get('HandshakeId')
        if m.get('MasterAccountId') is not None:
            self.master_account_id = m.get('MasterAccountId')
        if m.get('MasterAccountName') is not None:
            self.master_account_name = m.get('MasterAccountName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListHandshakesForResourceDirectoryResponseBodyHandshakes(TeaModel):
    def __init__(self, handshake=None):
        self.handshake = handshake  # type: list[ListHandshakesForResourceDirectoryResponseBodyHandshakesHandshake]

    def validate(self):
        if self.handshake:
            for k in self.handshake:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHandshakesForResourceDirectoryResponseBodyHandshakes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Handshake'] = []
        if self.handshake is not None:
            for k in self.handshake:
                result['Handshake'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.handshake = []
        if m.get('Handshake') is not None:
            for k in m.get('Handshake'):
                temp_model = ListHandshakesForResourceDirectoryResponseBodyHandshakesHandshake()
                self.handshake.append(temp_model.from_map(k))
        return self


class ListHandshakesForResourceDirectoryResponseBody(TeaModel):
    def __init__(self, handshakes=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.handshakes = handshakes  # type: ListHandshakesForResourceDirectoryResponseBodyHandshakes
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.handshakes:
            self.handshakes.validate()

    def to_map(self):
        _map = super(ListHandshakesForResourceDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handshakes is not None:
            result['Handshakes'] = self.handshakes.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Handshakes') is not None:
            temp_model = ListHandshakesForResourceDirectoryResponseBodyHandshakes()
            self.handshakes = temp_model.from_map(m['Handshakes'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHandshakesForResourceDirectoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHandshakesForResourceDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHandshakesForResourceDirectoryResponse, self).to_map()
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
            temp_model = ListHandshakesForResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesRequest(TeaModel):
    def __init__(self, language=None, page_number=None, page_size=None, policy_type=None):
        self.language = language  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policy_type = policy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPoliciesResponseBodyPoliciesPolicy(TeaModel):
    def __init__(self, attachment_count=None, create_date=None, default_version=None, description=None,
                 policy_name=None, policy_type=None, update_date=None):
        self.attachment_count = attachment_count  # type: int
        self.create_date = create_date  # type: str
        self.default_version = default_version  # type: str
        self.description = description  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPoliciesResponseBodyPoliciesPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListPoliciesResponseBodyPolicies(TeaModel):
    def __init__(self, policy=None):
        self.policy = policy  # type: list[ListPoliciesResponseBodyPoliciesPolicy]

    def validate(self):
        if self.policy:
            for k in self.policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPoliciesResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policy'] = []
        if self.policy is not None:
            for k in self.policy:
                result['Policy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policy = []
        if m.get('Policy') is not None:
            for k in m.get('Policy'):
                temp_model = ListPoliciesResponseBodyPoliciesPolicy()
                self.policy.append(temp_model.from_map(k))
        return self


class ListPoliciesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, policies=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policies = policies  # type: ListPoliciesResponseBodyPolicies
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        _map = super(ListPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Policies') is not None:
            temp_model = ListPoliciesResponseBodyPolicies()
            self.policies = temp_model.from_map(m['Policies'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPoliciesResponse, self).to_map()
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
            temp_model = ListPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyAttachmentsRequest(TeaModel):
    def __init__(self, language=None, page_number=None, page_size=None, policy_name=None, policy_type=None,
                 principal_name=None, principal_type=None, resource_group_id=None):
        self.language = language  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.principal_name = principal_name  # type: str
        self.principal_type = principal_type  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPolicyAttachmentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment(TeaModel):
    def __init__(self, attach_date=None, description=None, policy_name=None, policy_type=None, principal_name=None,
                 principal_type=None, resource_group_id=None):
        self.attach_date = attach_date  # type: str
        self.description = description  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.principal_name = principal_name  # type: str
        self.principal_type = principal_type  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListPolicyAttachmentsResponseBodyPolicyAttachments(TeaModel):
    def __init__(self, policy_attachment=None):
        self.policy_attachment = policy_attachment  # type: list[ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment]

    def validate(self):
        if self.policy_attachment:
            for k in self.policy_attachment:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPolicyAttachmentsResponseBodyPolicyAttachments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyAttachment'] = []
        if self.policy_attachment is not None:
            for k in self.policy_attachment:
                result['PolicyAttachment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policy_attachment = []
        if m.get('PolicyAttachment') is not None:
            for k in m.get('PolicyAttachment'):
                temp_model = ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment()
                self.policy_attachment.append(temp_model.from_map(k))
        return self


class ListPolicyAttachmentsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, policy_attachments=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policy_attachments = policy_attachments  # type: ListPolicyAttachmentsResponseBodyPolicyAttachments
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.policy_attachments:
            self.policy_attachments.validate()

    def to_map(self):
        _map = super(ListPolicyAttachmentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_attachments is not None:
            result['PolicyAttachments'] = self.policy_attachments.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyAttachments') is not None:
            temp_model = ListPolicyAttachmentsResponseBodyPolicyAttachments()
            self.policy_attachments = temp_model.from_map(m['PolicyAttachments'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPolicyAttachmentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPolicyAttachmentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPolicyAttachmentsResponse, self).to_map()
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
            temp_model = ListPolicyAttachmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyVersionsRequest(TeaModel):
    def __init__(self, policy_name=None, policy_type=None):
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPolicyVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion(TeaModel):
    def __init__(self, create_date=None, is_default_version=None, version_id=None):
        self.create_date = create_date  # type: str
        self.is_default_version = is_default_version  # type: bool
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ListPolicyVersionsResponseBodyPolicyVersions(TeaModel):
    def __init__(self, policy_version=None):
        self.policy_version = policy_version  # type: list[ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion]

    def validate(self):
        if self.policy_version:
            for k in self.policy_version:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPolicyVersionsResponseBodyPolicyVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyVersion'] = []
        if self.policy_version is not None:
            for k in self.policy_version:
                result['PolicyVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policy_version = []
        if m.get('PolicyVersion') is not None:
            for k in m.get('PolicyVersion'):
                temp_model = ListPolicyVersionsResponseBodyPolicyVersionsPolicyVersion()
                self.policy_version.append(temp_model.from_map(k))
        return self


class ListPolicyVersionsResponseBody(TeaModel):
    def __init__(self, policy_versions=None, request_id=None):
        self.policy_versions = policy_versions  # type: ListPolicyVersionsResponseBodyPolicyVersions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy_versions:
            self.policy_versions.validate()

    def to_map(self):
        _map = super(ListPolicyVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_versions is not None:
            result['PolicyVersions'] = self.policy_versions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyVersions') is not None:
            temp_model = ListPolicyVersionsResponseBodyPolicyVersions()
            self.policy_versions = temp_model.from_map(m['PolicyVersions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPolicyVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPolicyVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPolicyVersionsResponse, self).to_map()
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
            temp_model = ListPolicyVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceGroupsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceGroupsRequestTag, self).to_map()
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


class ListResourceGroupsRequest(TeaModel):
    def __init__(self, display_name=None, include_tags=None, name=None, page_number=None, page_size=None,
                 resource_group_id=None, resource_group_ids=None, status=None, tag=None):
        self.display_name = display_name  # type: str
        self.include_tags = include_tags  # type: bool
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.resource_group_ids = resource_group_ids  # type: list[str]
        self.status = status  # type: str
        self.tag = tag  # type: list[ListResourceGroupsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListResourceGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListResourceGroupsResponseBodyResourceGroupsResourceGroupTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceGroupsResponseBodyResourceGroupsResourceGroupTagsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListResourceGroupsResponseBodyResourceGroupsResourceGroupTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[ListResourceGroupsResponseBodyResourceGroupsResourceGroupTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceGroupsResponseBodyResourceGroupsResourceGroupTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListResourceGroupsResponseBodyResourceGroupsResourceGroupTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListResourceGroupsResponseBodyResourceGroupsResourceGroup(TeaModel):
    def __init__(self, account_id=None, create_date=None, display_name=None, id=None, name=None, status=None,
                 tags=None):
        self.account_id = account_id  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: ListResourceGroupsResponseBodyResourceGroupsResourceGroupTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(ListResourceGroupsResponseBodyResourceGroupsResourceGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = ListResourceGroupsResponseBodyResourceGroupsResourceGroupTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class ListResourceGroupsResponseBodyResourceGroups(TeaModel):
    def __init__(self, resource_group=None):
        self.resource_group = resource_group  # type: list[ListResourceGroupsResponseBodyResourceGroupsResourceGroup]

    def validate(self):
        if self.resource_group:
            for k in self.resource_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceGroupsResponseBodyResourceGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceGroup'] = []
        if self.resource_group is not None:
            for k in self.resource_group:
                result['ResourceGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource_group = []
        if m.get('ResourceGroup') is not None:
            for k in m.get('ResourceGroup'):
                temp_model = ListResourceGroupsResponseBodyResourceGroupsResourceGroup()
                self.resource_group.append(temp_model.from_map(k))
        return self


class ListResourceGroupsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, resource_groups=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.resource_groups = resource_groups  # type: ListResourceGroupsResponseBodyResourceGroups
        self.total_count = total_count  # type: int

    def validate(self):
        if self.resource_groups:
            self.resource_groups.validate()

    def to_map(self):
        _map = super(ListResourceGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_groups is not None:
            result['ResourceGroups'] = self.resource_groups.to_map()
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
        if m.get('ResourceGroups') is not None:
            temp_model = ListResourceGroupsResponseBodyResourceGroups()
            self.resource_groups = temp_model.from_map(m['ResourceGroups'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceGroupsResponse, self).to_map()
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
            temp_model = ListResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region=None, resource_group_id=None, resource_id=None,
                 resource_type=None, service=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region = region  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.service = service  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class ListResourcesResponseBodyResourcesResource(TeaModel):
    def __init__(self, create_date=None, region_id=None, resource_group_id=None, resource_id=None,
                 resource_type=None, service=None):
        self.create_date = create_date  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.service = service  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesResponseBodyResourcesResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class ListResourcesResponseBodyResources(TeaModel):
    def __init__(self, resource=None):
        self.resource = resource  # type: list[ListResourcesResponseBodyResourcesResource]

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = ListResourcesResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, resources=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.resources = resources  # type: ListResourcesResponseBodyResources
        self.total_count = total_count  # type: int

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super(ListResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
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
        if m.get('Resources') is not None:
            temp_model = ListResourcesResponseBodyResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourcesResponse, self).to_map()
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
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesRequest(TeaModel):
    def __init__(self, language=None, page_number=None, page_size=None):
        self.language = language  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRolesResponseBodyRolesRoleLatestDeletionTask(TeaModel):
    def __init__(self, create_date=None, deletion_task_id=None):
        self.create_date = create_date  # type: str
        self.deletion_task_id = deletion_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesResponseBodyRolesRoleLatestDeletionTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        return self


class ListRolesResponseBodyRolesRole(TeaModel):
    def __init__(self, arn=None, create_date=None, description=None, is_service_linked_role=None,
                 latest_deletion_task=None, max_session_duration=None, role_id=None, role_name=None, role_principal_name=None,
                 update_date=None):
        self.arn = arn  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.is_service_linked_role = is_service_linked_role  # type: bool
        self.latest_deletion_task = latest_deletion_task  # type: ListRolesResponseBodyRolesRoleLatestDeletionTask
        self.max_session_duration = max_session_duration  # type: long
        self.role_id = role_id  # type: str
        self.role_name = role_name  # type: str
        self.role_principal_name = role_principal_name  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        _map = super(ListRolesResponseBodyRolesRole, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role
        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')
        if m.get('LatestDeletionTask') is not None:
            temp_model = ListRolesResponseBodyRolesRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m['LatestDeletionTask'])
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListRolesResponseBodyRoles(TeaModel):
    def __init__(self, role=None):
        self.role = role  # type: list[ListRolesResponseBodyRolesRole]

    def validate(self):
        if self.role:
            for k in self.role:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRolesResponseBodyRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Role'] = []
        if self.role is not None:
            for k in self.role:
                result['Role'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k in m.get('Role'):
                temp_model = ListRolesResponseBodyRolesRole()
                self.role.append(temp_model.from_map(k))
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, roles=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.roles = roles  # type: ListRolesResponseBodyRoles
        self.total_count = total_count  # type: int

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        _map = super(ListRolesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
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
        if m.get('Roles') is not None:
            temp_model = ListRolesResponseBodyRoles()
            self.roles = temp_model.from_map(m['Roles'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRolesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRolesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRolesResponse, self).to_map()
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
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, key_filter=None, max_results=None, next_token=None, resource_type=None):
        self.key_filter = key_filter  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_filter is not None:
            result['KeyFilter'] = self.key_filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyFilter') is not None:
            self.key_filter = m.get('KeyFilter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyTags(TeaModel):
    def __init__(self, key=None):
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tags=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[ListTagKeysResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagKeysResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
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
    def __init__(self, max_results=None, next_token=None, resource_id=None, resource_type=None, tag=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
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


class ListTagValuesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_type=None, tag_key=None, value_filter=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.value_filter = value_filter  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagValuesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.value_filter is not None:
            result['ValueFilter'] = self.value_filter
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('ValueFilter') is not None:
            self.value_filter = m.get('ValueFilter')
        return self


class ListTagValuesResponseBodyTags(TeaModel):
    def __init__(self, value=None):
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagValuesResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tags=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[ListTagValuesResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagValuesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagValuesResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagValuesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagValuesResponse, self).to_map()
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTargetAttachmentsForControlPolicyRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, policy_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTargetAttachmentsForControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachmentsTargetAttachment(TeaModel):
    def __init__(self, attach_date=None, target_id=None, target_name=None, target_type=None):
        self.attach_date = attach_date  # type: str
        self.target_id = target_id  # type: str
        self.target_name = target_name  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachmentsTargetAttachment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachments(TeaModel):
    def __init__(self, target_attachment=None):
        self.target_attachment = target_attachment  # type: list[ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachmentsTargetAttachment]

    def validate(self):
        if self.target_attachment:
            for k in self.target_attachment:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TargetAttachment'] = []
        if self.target_attachment is not None:
            for k in self.target_attachment:
                result['TargetAttachment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.target_attachment = []
        if m.get('TargetAttachment') is not None:
            for k in m.get('TargetAttachment'):
                temp_model = ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachmentsTargetAttachment()
                self.target_attachment.append(temp_model.from_map(k))
        return self


class ListTargetAttachmentsForControlPolicyResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, target_attachments=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.target_attachments = target_attachments  # type: ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachments
        self.total_count = total_count  # type: int

    def validate(self):
        if self.target_attachments:
            self.target_attachments.validate()

    def to_map(self):
        _map = super(ListTargetAttachmentsForControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.target_attachments is not None:
            result['TargetAttachments'] = self.target_attachments.to_map()
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
        if m.get('TargetAttachments') is not None:
            temp_model = ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachments()
            self.target_attachments = temp_model.from_map(m['TargetAttachments'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTargetAttachmentsForControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTargetAttachmentsForControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTargetAttachmentsForControlPolicyResponse, self).to_map()
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
            temp_model = ListTargetAttachmentsForControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrustedServiceStatusRequest(TeaModel):
    def __init__(self, admin_account_id=None, page_number=None, page_size=None):
        self.admin_account_id = admin_account_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrustedServiceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_account_id is not None:
            result['AdminAccountId'] = self.admin_account_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdminAccountId') is not None:
            self.admin_account_id = m.get('AdminAccountId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal(TeaModel):
    def __init__(self, enable_time=None, service_principal=None):
        self.enable_time = enable_time  # type: str
        self.service_principal = service_principal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class ListTrustedServiceStatusResponseBodyEnabledServicePrincipals(TeaModel):
    def __init__(self, enabled_service_principal=None):
        self.enabled_service_principal = enabled_service_principal  # type: list[ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal]

    def validate(self):
        if self.enabled_service_principal:
            for k in self.enabled_service_principal:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTrustedServiceStatusResponseBodyEnabledServicePrincipals, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnabledServicePrincipal'] = []
        if self.enabled_service_principal is not None:
            for k in self.enabled_service_principal:
                result['EnabledServicePrincipal'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.enabled_service_principal = []
        if m.get('EnabledServicePrincipal') is not None:
            for k in m.get('EnabledServicePrincipal'):
                temp_model = ListTrustedServiceStatusResponseBodyEnabledServicePrincipalsEnabledServicePrincipal()
                self.enabled_service_principal.append(temp_model.from_map(k))
        return self


class ListTrustedServiceStatusResponseBody(TeaModel):
    def __init__(self, enabled_service_principals=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.enabled_service_principals = enabled_service_principals  # type: ListTrustedServiceStatusResponseBodyEnabledServicePrincipals
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.enabled_service_principals:
            self.enabled_service_principals.validate()

    def to_map(self):
        _map = super(ListTrustedServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_service_principals is not None:
            result['EnabledServicePrincipals'] = self.enabled_service_principals.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnabledServicePrincipals') is not None:
            temp_model = ListTrustedServiceStatusResponseBodyEnabledServicePrincipals()
            self.enabled_service_principals = temp_model.from_map(m['EnabledServicePrincipals'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTrustedServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTrustedServiceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTrustedServiceStatusResponse, self).to_map()
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
            temp_model = ListTrustedServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveAccountRequest(TeaModel):
    def __init__(self, account_id=None, destination_folder_id=None):
        self.account_id = account_id  # type: str
        self.destination_folder_id = destination_folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.destination_folder_id is not None:
            result['DestinationFolderId'] = self.destination_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DestinationFolderId') is not None:
            self.destination_folder_id = m.get('DestinationFolderId')
        return self


class MoveAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveAccountResponseBody, self).to_map()
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


class MoveAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MoveAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveAccountResponse, self).to_map()
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
            temp_model = MoveAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourcesRequestResources(TeaModel):
    def __init__(self, region_id=None, resource_id=None, resource_type=None, service=None):
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.service = service  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourcesRequestResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class MoveResourcesRequest(TeaModel):
    def __init__(self, resource_group_id=None, resources=None):
        self.resource_group_id = resource_group_id  # type: str
        self.resources = resources  # type: list[MoveResourcesRequestResources]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(MoveResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = MoveResourcesRequestResources()
                self.resources.append(temp_model.from_map(k))
        return self


class MoveResourcesResponseBodyResponses(TeaModel):
    def __init__(self, error_code=None, error_msg=None, region_id=None, request_id=None, resource_id=None,
                 resource_type=None, service=None, status=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.service = service  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourcesResponseBodyResponses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service is not None:
            result['Service'] = self.service
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class MoveResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, responses=None):
        self.request_id = request_id  # type: str
        self.responses = responses  # type: list[MoveResourcesResponseBodyResponses]

    def validate(self):
        if self.responses:
            for k in self.responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(MoveResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Responses'] = []
        if self.responses is not None:
            for k in self.responses:
                result['Responses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.responses = []
        if m.get('Responses') is not None:
            for k in m.get('Responses'):
                temp_model = MoveResourcesResponseBodyResponses()
                self.responses.append(temp_model.from_map(k))
        return self


class MoveResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MoveResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveResourcesResponse, self).to_map()
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
            temp_model = MoveResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PromoteResourceAccountRequest(TeaModel):
    def __init__(self, account_id=None, email=None):
        self.account_id = account_id  # type: str
        self.email = email  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PromoteResourceAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.email is not None:
            result['Email'] = self.email
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        return self


class PromoteResourceAccountResponseBodyAccount(TeaModel):
    def __init__(self, account_id=None, account_name=None, display_name=None, folder_id=None, join_method=None,
                 join_time=None, modify_time=None, record_id=None, resource_directory_id=None, status=None, type=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.display_name = display_name  # type: str
        self.folder_id = folder_id  # type: str
        self.join_method = join_method  # type: str
        self.join_time = join_time  # type: str
        self.modify_time = modify_time  # type: str
        self.record_id = record_id  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PromoteResourceAccountResponseBodyAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PromoteResourceAccountResponseBody(TeaModel):
    def __init__(self, account=None, request_id=None):
        self.account = account  # type: PromoteResourceAccountResponseBodyAccount
        self.request_id = request_id  # type: str

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super(PromoteResourceAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = PromoteResourceAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PromoteResourceAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PromoteResourceAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PromoteResourceAccountResponse, self).to_map()
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
            temp_model = PromoteResourceAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDelegatedAdministratorRequest(TeaModel):
    def __init__(self, account_id=None, service_principal=None):
        self.account_id = account_id  # type: str
        self.service_principal = service_principal  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterDelegatedAdministratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')
        return self


class RegisterDelegatedAdministratorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterDelegatedAdministratorResponseBody, self).to_map()
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


class RegisterDelegatedAdministratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterDelegatedAdministratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterDelegatedAdministratorResponse, self).to_map()
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
            temp_model = RegisterDelegatedAdministratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveCloudAccountRequest(TeaModel):
    def __init__(self, account_id=None):
        self.account_id = account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveCloudAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class RemoveCloudAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveCloudAccountResponseBody, self).to_map()
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


class RemoveCloudAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveCloudAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveCloudAccountResponse, self).to_map()
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
            temp_model = RemoveCloudAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendCreateCloudAccountEmailRequest(TeaModel):
    def __init__(self, record_id=None):
        self.record_id = record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResendCreateCloudAccountEmailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class ResendCreateCloudAccountEmailResponseBodyAccount(TeaModel):
    def __init__(self, account_id=None, account_name=None, display_name=None, folder_id=None, join_method=None,
                 join_time=None, modify_time=None, record_id=None, resource_directory_id=None, status=None, type=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.display_name = display_name  # type: str
        self.folder_id = folder_id  # type: str
        self.join_method = join_method  # type: str
        self.join_time = join_time  # type: str
        self.modify_time = modify_time  # type: str
        self.record_id = record_id  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResendCreateCloudAccountEmailResponseBodyAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ResendCreateCloudAccountEmailResponseBody(TeaModel):
    def __init__(self, account=None, request_id=None):
        self.account = account  # type: ResendCreateCloudAccountEmailResponseBodyAccount
        self.request_id = request_id  # type: str

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super(ResendCreateCloudAccountEmailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = ResendCreateCloudAccountEmailResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResendCreateCloudAccountEmailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResendCreateCloudAccountEmailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResendCreateCloudAccountEmailResponse, self).to_map()
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
            temp_model = ResendCreateCloudAccountEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendPromoteResourceAccountEmailRequest(TeaModel):
    def __init__(self, record_id=None):
        self.record_id = record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResendPromoteResourceAccountEmailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class ResendPromoteResourceAccountEmailResponseBodyAccount(TeaModel):
    def __init__(self, account_id=None, account_name=None, display_name=None, folder_id=None, join_method=None,
                 join_time=None, modify_time=None, record_id=None, resource_directory_id=None, status=None, type=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.display_name = display_name  # type: str
        self.folder_id = folder_id  # type: str
        self.join_method = join_method  # type: str
        self.join_time = join_time  # type: str
        self.modify_time = modify_time  # type: str
        self.record_id = record_id  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResendPromoteResourceAccountEmailResponseBodyAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ResendPromoteResourceAccountEmailResponseBody(TeaModel):
    def __init__(self, account=None, request_id=None):
        self.account = account  # type: ResendPromoteResourceAccountEmailResponseBodyAccount
        self.request_id = request_id  # type: str

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super(ResendPromoteResourceAccountEmailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = ResendPromoteResourceAccountEmailResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResendPromoteResourceAccountEmailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResendPromoteResourceAccountEmailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResendPromoteResourceAccountEmailResponse, self).to_map()
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
            temp_model = ResendPromoteResourceAccountEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerificationCodeForBindSecureMobilePhoneRequest(TeaModel):
    def __init__(self, account_id=None, secure_mobile_phone=None):
        self.account_id = account_id  # type: str
        self.secure_mobile_phone = secure_mobile_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerificationCodeForBindSecureMobilePhoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.secure_mobile_phone is not None:
            result['SecureMobilePhone'] = self.secure_mobile_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('SecureMobilePhone') is not None:
            self.secure_mobile_phone = m.get('SecureMobilePhone')
        return self


class SendVerificationCodeForBindSecureMobilePhoneResponseBody(TeaModel):
    def __init__(self, expiration_date=None, request_id=None):
        self.expiration_date = expiration_date  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerificationCodeForBindSecureMobilePhoneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendVerificationCodeForBindSecureMobilePhoneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendVerificationCodeForBindSecureMobilePhoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendVerificationCodeForBindSecureMobilePhoneResponse, self).to_map()
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
            temp_model = SendVerificationCodeForBindSecureMobilePhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerificationCodeForEnableRDRequest(TeaModel):
    def __init__(self, secure_mobile_phone=None):
        self.secure_mobile_phone = secure_mobile_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerificationCodeForEnableRDRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secure_mobile_phone is not None:
            result['SecureMobilePhone'] = self.secure_mobile_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecureMobilePhone') is not None:
            self.secure_mobile_phone = m.get('SecureMobilePhone')
        return self


class SendVerificationCodeForEnableRDResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerificationCodeForEnableRDResponseBody, self).to_map()
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


class SendVerificationCodeForEnableRDResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendVerificationCodeForEnableRDResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendVerificationCodeForEnableRDResponse, self).to_map()
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
            temp_model = SendVerificationCodeForEnableRDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultPolicyVersionRequest(TeaModel):
    def __init__(self, policy_name=None, version_id=None):
        self.policy_name = policy_name  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultPolicyVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class SetDefaultPolicyVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultPolicyVersionResponseBody, self).to_map()
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


class SetDefaultPolicyVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDefaultPolicyVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDefaultPolicyVersionResponse, self).to_map()
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
            temp_model = SetDefaultPolicyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMemberDeletionPermissionRequest(TeaModel):
    def __init__(self, status=None):
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMemberDeletionPermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetMemberDeletionPermissionResponseBody(TeaModel):
    def __init__(self, management_account_id=None, member_deletion_status=None, request_id=None,
                 resource_directory_id=None):
        self.management_account_id = management_account_id  # type: str
        self.member_deletion_status = member_deletion_status  # type: str
        self.request_id = request_id  # type: str
        self.resource_directory_id = resource_directory_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMemberDeletionPermissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.management_account_id is not None:
            result['ManagementAccountId'] = self.management_account_id
        if self.member_deletion_status is not None:
            result['MemberDeletionStatus'] = self.member_deletion_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ManagementAccountId') is not None:
            self.management_account_id = m.get('ManagementAccountId')
        if m.get('MemberDeletionStatus') is not None:
            self.member_deletion_status = m.get('MemberDeletionStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        return self


class SetMemberDeletionPermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetMemberDeletionPermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetMemberDeletionPermissionResponse, self).to_map()
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
            temp_model = SetMemberDeletionPermissionResponseBody()
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
    def __init__(self, resource_id=None, resource_type=None, tag=None):
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


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, resource_id=None, resource_type=None, tag_key=None):
        self.all = all  # type: bool
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


class UpdateAccountRequest(TeaModel):
    def __init__(self, account_id=None, new_account_type=None, new_display_name=None):
        self.account_id = account_id  # type: str
        self.new_account_type = new_account_type  # type: str
        self.new_display_name = new_display_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.new_account_type is not None:
            result['NewAccountType'] = self.new_account_type
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('NewAccountType') is not None:
            self.new_account_type = m.get('NewAccountType')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        return self


class UpdateAccountResponseBodyAccount(TeaModel):
    def __init__(self, account_id=None, account_name=None, display_name=None, folder_id=None, join_method=None,
                 join_time=None, modify_time=None, resource_directory_id=None, status=None, type=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.display_name = display_name  # type: str
        self.folder_id = folder_id  # type: str
        self.join_method = join_method  # type: str
        self.join_time = join_time  # type: str
        self.modify_time = modify_time  # type: str
        self.resource_directory_id = resource_directory_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAccountResponseBodyAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.join_method is not None:
            result['JoinMethod'] = self.join_method
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateAccountResponseBody(TeaModel):
    def __init__(self, account=None, request_id=None):
        self.account = account  # type: UpdateAccountResponseBodyAccount
        self.request_id = request_id  # type: str

    def validate(self):
        if self.account:
            self.account.validate()

    def to_map(self):
        _map = super(UpdateAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = UpdateAccountResponseBodyAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAccountResponse, self).to_map()
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
            temp_model = UpdateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateControlPolicyRequest(TeaModel):
    def __init__(self, new_description=None, new_policy_document=None, new_policy_name=None, policy_id=None):
        self.new_description = new_description  # type: str
        self.new_policy_document = new_policy_document  # type: str
        self.new_policy_name = new_policy_name  # type: str
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_policy_document is not None:
            result['NewPolicyDocument'] = self.new_policy_document
        if self.new_policy_name is not None:
            result['NewPolicyName'] = self.new_policy_name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewPolicyDocument') is not None:
            self.new_policy_document = m.get('NewPolicyDocument')
        if m.get('NewPolicyName') is not None:
            self.new_policy_name = m.get('NewPolicyName')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class UpdateControlPolicyResponseBodyControlPolicy(TeaModel):
    def __init__(self, attachment_count=None, create_date=None, description=None, effect_scope=None, policy_id=None,
                 policy_name=None, policy_type=None, update_date=None):
        self.attachment_count = attachment_count  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.effect_scope = effect_scope  # type: str
        self.policy_id = policy_id  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateControlPolicyResponseBodyControlPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_count is not None:
            result['AttachmentCount'] = self.attachment_count
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachmentCount') is not None:
            self.attachment_count = m.get('AttachmentCount')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateControlPolicyResponseBody(TeaModel):
    def __init__(self, control_policy=None, request_id=None):
        self.control_policy = control_policy  # type: UpdateControlPolicyResponseBodyControlPolicy
        self.request_id = request_id  # type: str

    def validate(self):
        if self.control_policy:
            self.control_policy.validate()

    def to_map(self):
        _map = super(UpdateControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_policy is not None:
            result['ControlPolicy'] = self.control_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlPolicy') is not None:
            temp_model = UpdateControlPolicyResponseBodyControlPolicy()
            self.control_policy = temp_model.from_map(m['ControlPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateControlPolicyResponse, self).to_map()
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
            temp_model = UpdateControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFolderRequest(TeaModel):
    def __init__(self, folder_id=None, new_folder_name=None):
        self.folder_id = folder_id  # type: str
        self.new_folder_name = new_folder_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFolderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.new_folder_name is not None:
            result['NewFolderName'] = self.new_folder_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('NewFolderName') is not None:
            self.new_folder_name = m.get('NewFolderName')
        return self


class UpdateFolderResponseBodyFolder(TeaModel):
    def __init__(self, create_time=None, folder_id=None, folder_name=None, parent_folder_id=None):
        self.create_time = create_time  # type: str
        self.folder_id = folder_id  # type: str
        self.folder_name = folder_name  # type: str
        self.parent_folder_id = parent_folder_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFolderResponseBodyFolder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name
        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')
        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')
        return self


class UpdateFolderResponseBody(TeaModel):
    def __init__(self, folder=None, request_id=None):
        self.folder = folder  # type: UpdateFolderResponseBodyFolder
        self.request_id = request_id  # type: str

    def validate(self):
        if self.folder:
            self.folder.validate()

    def to_map(self):
        _map = super(UpdateFolderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Folder') is not None:
            temp_model = UpdateFolderResponseBodyFolder()
            self.folder = temp_model.from_map(m['Folder'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFolderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFolderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFolderResponse, self).to_map()
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
            temp_model = UpdateFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceGroupRequest(TeaModel):
    def __init__(self, new_display_name=None, resource_group_id=None):
        self.new_display_name = new_display_name  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class UpdateResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(self, account_id=None, create_date=None, display_name=None, id=None, name=None):
        self.account_id = account_id  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceGroupResponseBodyResourceGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_group=None):
        self.request_id = request_id  # type: str
        self.resource_group = resource_group  # type: UpdateResourceGroupResponseBodyResourceGroup

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super(UpdateResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = UpdateResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        return self


class UpdateResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceGroupResponse, self).to_map()
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
            temp_model = UpdateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRoleRequest(TeaModel):
    def __init__(self, new_assume_role_policy_document=None, new_description=None, new_max_session_duration=None,
                 role_name=None):
        self.new_assume_role_policy_document = new_assume_role_policy_document  # type: str
        self.new_description = new_description  # type: str
        self.new_max_session_duration = new_max_session_duration  # type: long
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_assume_role_policy_document is not None:
            result['NewAssumeRolePolicyDocument'] = self.new_assume_role_policy_document
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_max_session_duration is not None:
            result['NewMaxSessionDuration'] = self.new_max_session_duration
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewAssumeRolePolicyDocument') is not None:
            self.new_assume_role_policy_document = m.get('NewAssumeRolePolicyDocument')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewMaxSessionDuration') is not None:
            self.new_max_session_duration = m.get('NewMaxSessionDuration')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdateRoleResponseBodyRole(TeaModel):
    def __init__(self, arn=None, assume_role_policy_document=None, create_date=None, description=None,
                 max_session_duration=None, role_id=None, role_name=None, role_principal_name=None, update_date=None):
        self.arn = arn  # type: str
        self.assume_role_policy_document = assume_role_policy_document  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.max_session_duration = max_session_duration  # type: long
        self.role_id = role_id  # type: str
        self.role_name = role_name  # type: str
        self.role_principal_name = role_principal_name  # type: str
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRoleResponseBodyRole, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateRoleResponseBody(TeaModel):
    def __init__(self, request_id=None, role=None):
        self.request_id = request_id  # type: str
        self.role = role  # type: UpdateRoleResponseBodyRole

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super(UpdateRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            temp_model = UpdateRoleResponseBodyRole()
            self.role = temp_model.from_map(m['Role'])
        return self


class UpdateRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRoleResponse, self).to_map()
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
            temp_model = UpdateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


