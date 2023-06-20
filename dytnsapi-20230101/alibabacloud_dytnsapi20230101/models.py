# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetPhoneNumberIdentificationResultRequest(TeaModel):
    def __init__(self, auth_code=None, out_id=None, owner_id=None, phone_number=None, resource_owner_account=None,
                 resource_owner_id=None, session_id=None, session_payload=None):
        self.auth_code = auth_code  # type: str
        self.out_id = out_id  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_number = phone_number  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.session_id = session_id  # type: str
        self.session_payload = session_payload  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberIdentificationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_payload is not None:
            result['SessionPayload'] = self.session_payload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionPayload') is not None:
            self.session_payload = m.get('SessionPayload')
        return self


class GetPhoneNumberIdentificationResultResponseBodyData(TeaModel):
    def __init__(self, is_identified=None):
        self.is_identified = is_identified  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberIdentificationResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_identified is not None:
            result['IsIdentified'] = self.is_identified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsIdentified') is not None:
            self.is_identified = m.get('IsIdentified')
        return self


class GetPhoneNumberIdentificationResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetPhoneNumberIdentificationResultResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPhoneNumberIdentificationResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhoneNumberIdentificationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneNumberIdentificationResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPhoneNumberIdentificationResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPhoneNumberIdentificationResultResponse, self).to_map()
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
            temp_model = GetPhoneNumberIdentificationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneNumberIdentificationUrlRequest(TeaModel):
    def __init__(self, auth_code=None, ip=None, out_id=None, owner_id=None, phone_number=None,
                 remember_phone_number=None, resource_owner_account=None, resource_owner_id=None):
        self.auth_code = auth_code  # type: str
        self.ip = ip  # type: str
        self.out_id = out_id  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_number = phone_number  # type: str
        self.remember_phone_number = remember_phone_number  # type: bool
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberIdentificationUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.remember_phone_number is not None:
            result['RememberPhoneNumber'] = self.remember_phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('RememberPhoneNumber') is not None:
            self.remember_phone_number = m.get('RememberPhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetPhoneNumberIdentificationUrlResponseBodyData(TeaModel):
    def __init__(self, identification_url=None, session_id=None):
        self.identification_url = identification_url  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberIdentificationUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identification_url is not None:
            result['IdentificationUrl'] = self.identification_url
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentificationUrl') is not None:
            self.identification_url = m.get('IdentificationUrl')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class GetPhoneNumberIdentificationUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetPhoneNumberIdentificationUrlResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPhoneNumberIdentificationUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhoneNumberIdentificationUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneNumberIdentificationUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPhoneNumberIdentificationUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPhoneNumberIdentificationUrlResponse, self).to_map()
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
            temp_model = GetPhoneNumberIdentificationUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


