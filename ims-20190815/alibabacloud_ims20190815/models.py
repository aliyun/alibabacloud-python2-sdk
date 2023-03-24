# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddClientIdToOIDCProviderRequest(TeaModel):
    def __init__(self, client_id=None, oidcprovider_name=None):
        # The client ID that you want to add.
        # 
        # The client ID can contain letters, digits, and special characters and cannot start with the special characters. The special characters are `periods, (.), hyphens (-), underscores (_), colons (:), and forward slashes (/)`.
        # 
        # The client ID can be up to 64 characters in length.
        self.client_id = client_id  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddClientIdToOIDCProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class AddClientIdToOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(self, arn=None, client_ids=None, create_date=None, description=None, fingerprints=None,
                 gmt_create=None, gmt_modified=None, issuer_url=None, oidcprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn  # type: str
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids  # type: str
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date  # type: str
        # The description of the OIDC IdP.
        self.description = description  # type: str
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints  # type: str
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create  # type: str
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified  # type: str
        # The URL of the issuer.
        self.issuer_url = issuer_url  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddClientIdToOIDCProviderResponseBodyOIDCProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class AddClientIdToOIDCProviderResponseBody(TeaModel):
    def __init__(self, oidcprovider=None, request_id=None):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider  # type: AddClientIdToOIDCProviderResponseBodyOIDCProvider
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super(AddClientIdToOIDCProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = AddClientIdToOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddClientIdToOIDCProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddClientIdToOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddClientIdToOIDCProviderResponse, self).to_map()
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
            temp_model = AddClientIdToOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFingerprintToOIDCProviderRequest(TeaModel):
    def __init__(self, fingerprint=None, oidcprovider_name=None):
        # The fingerprint of the HTTPS certificate.
        # 
        # The fingerprint can contain letters and digits.
        # 
        # The fingerprint can be up to 40 characters in length.
        self.fingerprint = fingerprint  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFingerprintToOIDCProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class AddFingerprintToOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(self, arn=None, client_ids=None, create_date=None, description=None, fingerprints=None,
                 gmt_create=None, gmt_modified=None, issuer_url=None, oidcprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn  # type: str
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids  # type: str
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date  # type: str
        # The description of the OIDC IdP.
        self.description = description  # type: str
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints  # type: str
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create  # type: str
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified  # type: str
        # The URL of the issuer.
        self.issuer_url = issuer_url  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFingerprintToOIDCProviderResponseBodyOIDCProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class AddFingerprintToOIDCProviderResponseBody(TeaModel):
    def __init__(self, oidcprovider=None, request_id=None):
        # The name of the OIDC IdP.
        self.oidcprovider = oidcprovider  # type: AddFingerprintToOIDCProviderResponseBodyOIDCProvider
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super(AddFingerprintToOIDCProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = AddFingerprintToOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddFingerprintToOIDCProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddFingerprintToOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddFingerprintToOIDCProviderResponse, self).to_map()
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
            temp_model = AddFingerprintToOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToGroupRequest(TeaModel):
    def __init__(self, group_name=None, user_principal_name=None):
        # The name of the RAM user group.
        self.group_name = group_name  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class AddUserToGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToGroupResponseBody, self).to_map()
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


class AddUserToGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddUserToGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserToGroupResponse, self).to_map()
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
            temp_model = AddUserToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindMFADeviceRequest(TeaModel):
    def __init__(self, authentication_code_1=None, authentication_code_2=None, serial_number=None,
                 user_principal_name=None):
        # The first verification code.
        # 
        # >  You can call the [CreateVirtualMFADevice](~~186179~~) operation to create an MFA device and generate a key (value of `Base32StringSeed`). Then, use the key on the Alibaba Cloud app to manually add an MFA device, and obtain the two consecutive verification codes.
        self.authentication_code_1 = authentication_code_1  # type: str
        # The second verification code.
        # 
        # >  You can call the [CreateVirtualMFADevice](~~186179~~) operation to create an MFA device and generate a key (value of `Base32StringSeed`). Then, use the key on the Alibaba Cloud app to manually add an MFA device, and obtain the two consecutive verification codes.
        self.authentication_code_2 = authentication_code_2  # type: str
        # The serial number of the MFA device.
        # 
        # >  You can call the [CreateVirtualMFADevice](~~186179~~) operation to obtain the serial number of the MFA device.
        self.serial_number = serial_number  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindMFADeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_code_1 is not None:
            result['AuthenticationCode1'] = self.authentication_code_1
        if self.authentication_code_2 is not None:
            result['AuthenticationCode2'] = self.authentication_code_2
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthenticationCode1') is not None:
            self.authentication_code_1 = m.get('AuthenticationCode1')
        if m.get('AuthenticationCode2') is not None:
            self.authentication_code_2 = m.get('AuthenticationCode2')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class BindMFADeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindMFADeviceResponseBody, self).to_map()
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


class BindMFADeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindMFADeviceResponse, self).to_map()
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
            temp_model = BindMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangePasswordRequest(TeaModel):
    def __init__(self, new_password=None, old_password=None):
        # The new password that is used to log on to the console.
        # 
        # The password must meet the complexity requirements. For more information, see [GetPasswordPolicy](~~186691~~).
        self.new_password = new_password  # type: str
        # The old password that is used to log on to the console.
        self.old_password = old_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangePasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.old_password is not None:
            result['OldPassword'] = self.old_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')
        return self


class ChangePasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangePasswordResponseBody, self).to_map()
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


class ChangePasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangePasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangePasswordResponse, self).to_map()
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
            temp_model = ChangePasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessKeyRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        # The logon name of the RAM user.
        # 
        # If this parameter is empty, an AccessKey pair is created for the current user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateAccessKeyResponseBodyAccessKey(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, create_date=None, status=None):
        # The AccessKey ID provided to you by Alibaba Cloud.
        self.access_key_id = access_key_id  # type: str
        # The AccessKey secret provided to you by Alibaba Cloud.
        self.access_key_secret = access_key_secret  # type: str
        # The time when the AccessKey pair was created.
        self.create_date = create_date  # type: str
        # The status of the AccessKey pair. Valid values:
        # 
        # *   Active
        # *   Inactive
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessKeyResponseBodyAccessKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateAccessKeyResponseBody(TeaModel):
    def __init__(self, access_key=None, request_id=None):
        # The information of the AccessKey pair.
        self.access_key = access_key  # type: CreateAccessKeyResponseBodyAccessKey
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.access_key:
            self.access_key.validate()

    def to_map(self):
        _map = super(CreateAccessKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            temp_model = CreateAccessKeyResponseBodyAccessKey()
            self.access_key = temp_model.from_map(m['AccessKey'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAccessKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccessKeyResponse, self).to_map()
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
            temp_model = CreateAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSecretRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CreateAppSecretResponseBodyAppSecret(TeaModel):
    def __init__(self, app_id=None, app_secret_id=None, app_secret_value=None, create_date=None):
        self.app_id = app_id  # type: str
        self.app_secret_id = app_secret_id  # type: str
        self.app_secret_value = app_secret_value  # type: str
        self.create_date = create_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSecretResponseBodyAppSecret, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('AppSecretValue') is not None:
            self.app_secret_value = m.get('AppSecretValue')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class CreateAppSecretResponseBody(TeaModel):
    def __init__(self, app_secret=None, request_id=None):
        self.app_secret = app_secret  # type: CreateAppSecretResponseBodyAppSecret
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        _map = super(CreateAppSecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppSecret') is not None:
            temp_model = CreateAppSecretResponseBodyAppSecret()
            self.app_secret = temp_model.from_map(m['AppSecret'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppSecretResponse, self).to_map()
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
            temp_model = CreateAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(self, access_token_validity=None, app_name=None, app_type=None, display_name=None,
                 is_multi_tenant=None, predefined_scopes=None, redirect_uris=None, refresh_token_validity=None,
                 secret_required=None):
        self.access_token_validity = access_token_validity  # type: int
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.display_name = display_name  # type: str
        self.is_multi_tenant = is_multi_tenant  # type: bool
        self.predefined_scopes = predefined_scopes  # type: str
        self.redirect_uris = redirect_uris  # type: str
        self.refresh_token_validity = refresh_token_validity  # type: int
        self.secret_required = secret_required  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('PredefinedScopes') is not None:
            self.predefined_scopes = m.get('PredefinedScopes')
        if m.get('RedirectUris') is not None:
            self.redirect_uris = m.get('RedirectUris')
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        return self


class CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(self, description=None, name=None):
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope, self).to_map()
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


class CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(self, predefined_scope=None):
        self.predefined_scope = predefined_scope  # type: list[CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope]

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class CreateApplicationResponseBodyApplicationDelegatedScope(TeaModel):
    def __init__(self, predefined_scopes=None):
        self.predefined_scopes = predefined_scopes  # type: CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super(CreateApplicationResponseBodyApplicationDelegatedScope, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = CreateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class CreateApplicationResponseBodyApplicationRedirectUris(TeaModel):
    def __init__(self, redirect_uri=None):
        self.redirect_uri = redirect_uri  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationResponseBodyApplicationRedirectUris, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class CreateApplicationResponseBodyApplication(TeaModel):
    def __init__(self, access_token_validity=None, account_id=None, app_id=None, app_name=None, app_type=None,
                 create_date=None, delegated_scope=None, display_name=None, is_multi_tenant=None, redirect_uris=None,
                 refresh_token_validity=None, secret_required=None, update_date=None):
        self.access_token_validity = access_token_validity  # type: int
        self.account_id = account_id  # type: str
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.create_date = create_date  # type: str
        self.delegated_scope = delegated_scope  # type: CreateApplicationResponseBodyApplicationDelegatedScope
        self.display_name = display_name  # type: str
        self.is_multi_tenant = is_multi_tenant  # type: bool
        self.redirect_uris = redirect_uris  # type: CreateApplicationResponseBodyApplicationRedirectUris
        self.refresh_token_validity = refresh_token_validity  # type: int
        self.secret_required = secret_required  # type: bool
        self.update_date = update_date  # type: str

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super(CreateApplicationResponseBodyApplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = CreateApplicationResponseBodyApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('RedirectUris') is not None:
            temp_model = CreateApplicationResponseBodyApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(self, application=None, request_id=None):
        self.application = application  # type: CreateApplicationResponseBodyApplication
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super(CreateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = CreateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationResponse, self).to_map()
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
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(self, comments=None, display_name=None, group_name=None):
        # The description.
        # 
        # The value can be up to 128 characters in length.
        self.comments = comments  # type: str
        # The display name of the RAM user group.
        # 
        # The name can be up to 24 characters in length.
        self.display_name = display_name  # type: str
        # The name of the RAM user group. You must specify this parameter.
        # 
        # The name can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        self.group_name = group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class CreateGroupResponseBodyGroup(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, group_id=None, group_name=None,
                 update_date=None):
        # The description.
        self.comments = comments  # type: str
        # The creation time.
        self.create_date = create_date  # type: str
        # The display name of the RAM user group.
        self.display_name = display_name  # type: str
        # The ID of the RAM user group.
        self.group_id = group_id  # type: str
        # The name of the RAM user group.
        self.group_name = group_name  # type: str
        # The update time.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupResponseBodyGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(self, group=None, request_id=None):
        # The information of the RAM user group.
        self.group = group  # type: CreateGroupResponseBodyGroup
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super(CreateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = CreateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupResponse, self).to_map()
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoginProfileRequest(TeaModel):
    def __init__(self, mfabind_required=None, password=None, password_reset_required=None, status=None,
                 user_principal_name=None):
        # Specifies whether multi-factor authentication (MFA) must be enabled. Valid values:
        # 
        # *   true: MFA must be enabled. The RAM user must bind an MFA device at the next logon.
        # *   false: MFA is not enabled. This is the default value.
        self.mfabind_required = mfabind_required  # type: bool
        # The password that is used to log on to the console.
        # 
        # The password must meet the complexity requirements.
        self.password = password  # type: str
        # Specifies whether the RAM user must reset the password at the next logon. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.password_reset_required = password_reset_required  # type: bool
        # The status of password-based logon. Valid values:
        # 
        # *   Active: Password-based logon is enabled. This is the default value.
        # *   Inactive: Password-based logon is disabled.
        self.status = status  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLoginProfileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.password is not None:
            result['Password'] = self.password
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.status is not None:
            result['Status'] = self.status
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(self, mfabind_required=None, password_reset_required=None, status=None, update_date=None,
                 user_principal_name=None):
        # Indicates whether MFA must be enabled.
        self.mfabind_required = mfabind_required  # type: bool
        # Indicates whether the RAM user must reset the password at the next logon.
        self.password_reset_required = password_reset_required  # type: bool
        # The status of password-based logon.
        self.status = status  # type: str
        # The update time.
        self.update_date = update_date  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLoginProfileResponseBodyLoginProfile, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateLoginProfileResponseBody(TeaModel):
    def __init__(self, login_profile=None, request_id=None):
        # The logon information.
        self.login_profile = login_profile  # type: CreateLoginProfileResponseBodyLoginProfile
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        _map = super(CreateLoginProfileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginProfile') is not None:
            temp_model = CreateLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLoginProfileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLoginProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLoginProfileResponse, self).to_map()
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
            temp_model = CreateLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOIDCProviderRequest(TeaModel):
    def __init__(self, client_ids=None, description=None, fingerprints=None, issuer_url=None,
                 oidcprovider_name=None):
        # The ID of the client, which is provided by the external IdP Okta. If you want to specify multiple client IDs, separate the client IDs with commas (,).
        # 
        # The client ID can contain letters, digits, and special characters and cannot start with the special characters. The special characters are `periods, (.), hyphens (-), underscores (_), colons (:), and forward slashes (/)`.``
        # 
        # The client ID can be up to 64 characters in length.
        self.client_ids = client_ids  # type: str
        # The description of the OIDC IdP.
        # 
        # The description can be up to 256 characters in length.
        self.description = description  # type: str
        # The fingerprint of the HTTPS certificate, which is provided by the external IdP Okta. If you want to specify multiple fingerprints, separate the fingerprints with commas (,).
        # 
        # The fingerprint can contain letters and digits.
        # 
        # The fingerprint can be up to 40 characters in length.
        self.fingerprints = fingerprints  # type: str
        # The URL of the issuer, which is provided by the external IdP Okta. The URL of the issuer must be unique within an Alibaba Cloud account.
        # 
        # The URL of the issuer must start with `https` and be in the valid URL format. The URL cannot contain query parameters that follow a question mark (`?`) or logon information that is identified by at signs (`@`). The URL cannot be a fragment URL that contains number signs (`#`).
        # 
        # The URL can be up to 255 characters in length.
        self.issuer_url = issuer_url  # type: str
        # The name of the OIDC IdP.
        # 
        # The name can contain letters, digits, and special characters and cannot start or end with the special characters. The special characters are `periods, (.), hyphens (-), and underscores (_)`.
        # 
        # The name can be up to 128 characters in length.
        self.oidcprovider_name = oidcprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOIDCProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class CreateOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(self, arn=None, client_ids=None, create_date=None, description=None, fingerprints=None,
                 gmt_create=None, gmt_modified=None, issuer_url=None, oidcprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn  # type: str
        # The ID of the client.
        self.client_ids = client_ids  # type: str
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date  # type: str
        # The description of the OIDC IdP.
        self.description = description  # type: str
        # The fingerprint of the HTTPS certificate.
        self.fingerprints = fingerprints  # type: str
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create  # type: str
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified  # type: str
        # The URL of the issuer.
        self.issuer_url = issuer_url  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOIDCProviderResponseBodyOIDCProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateOIDCProviderResponseBody(TeaModel):
    def __init__(self, oidcprovider=None, request_id=None):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider  # type: CreateOIDCProviderResponseBodyOIDCProvider
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super(CreateOIDCProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = CreateOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOIDCProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOIDCProviderResponse, self).to_map()
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
            temp_model = CreateOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSAMLProviderRequest(TeaModel):
    def __init__(self, description=None, encoded_samlmetadata_document=None, samlprovider_name=None):
        # The description.
        self.description = description  # type: str
        # The metadata file, which is Base64 encoded.
        # 
        # The file is provided by an IdP that supports SAML 2.0.
        self.encoded_samlmetadata_document = encoded_samlmetadata_document  # type: str
        # The name of the IdP.
        # 
        # The value can be up to 128 characters in length. The name can contain letters, digits,`  periods (.), hyphens (-), and underscores (_) `. The name cannot start or end with`  periods (.), hyphens (-), or underscores (_) `.
        self.samlprovider_name = samlprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSAMLProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = m.get('EncodedSAMLMetadataDocument')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        return self


class CreateSAMLProviderResponseBodySAMLProvider(TeaModel):
    def __init__(self, arn=None, create_date=None, description=None, samlprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the IdP.
        self.arn = arn  # type: str
        # The creation time.
        self.create_date = create_date  # type: str
        # The description.
        self.description = description  # type: str
        # The name of the IdP.
        self.samlprovider_name = samlprovider_name  # type: str
        # The update time.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSAMLProviderResponseBodySAMLProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
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
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateSAMLProviderResponseBody(TeaModel):
    def __init__(self, request_id=None, samlprovider=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the IdP.
        self.samlprovider = samlprovider  # type: CreateSAMLProviderResponseBodySAMLProvider

    def validate(self):
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        _map = super(CreateSAMLProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProvider') is not None:
            temp_model = CreateSAMLProviderResponseBodySAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class CreateSAMLProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSAMLProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSAMLProviderResponse, self).to_map()
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
            temp_model = CreateSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. You cannot specify empty strings as tag keys. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key  # type: str
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be a up to128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserRequestTag, self).to_map()
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


class CreateUserRequest(TeaModel):
    def __init__(self, comments=None, display_name=None, email=None, mobile_phone=None, tag=None,
                 user_principal_name=None):
        # The description.
        # 
        # The description must be 1 to 128 characters in length.
        self.comments = comments  # type: str
        # The display name of the RAM user.
        # 
        # The name must be 1 to 24 characters in length.
        self.display_name = display_name  # type: str
        # The email address of the RAM user.
        # 
        # >  This parameter is valid only on the China site (aliyun.com).
        self.email = email  # type: str
        # The mobile phone number of the RAM user.
        # 
        # Format: Country code-Mobile phone number.
        # 
        # >  This parameter is valid only on the China site (aliyun.com).
        self.mobile_phone = mobile_phone  # type: str
        self.tag = tag  # type: list[CreateUserRequestTag]
        # The logon name of the RAM user.
        # 
        # The name is in the format of `<username>@<AccountAlias>.onaliyun.com`. `<username>` indicates the name of the RAM user. `<AccountAlias>.onaliyun.com` indicates the default domain name. For more information about how to obtain the default domain name, see [GetDefaultDomain](~~186720~~).
        # 
        # The value of `UserPrincipalName` must be 1 to 128 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (\_). The value of `<AccountAlias>.onaliyun.com` must be 1 to 64 characters in length.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateUserRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateUserResponseBodyUserTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserResponseBodyUserTagsTag, self).to_map()
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


class CreateUserResponseBodyUserTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[CreateUserResponseBodyUserTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateUserResponseBodyUserTags, self).to_map()
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
                temp_model = CreateUserResponseBodyUserTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateUserResponseBodyUser(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, email=None, last_login_date=None,
                 mobile_phone=None, provision_type=None, tags=None, update_date=None, user_id=None, user_principal_name=None):
        # The description.
        self.comments = comments  # type: str
        # The time when the RAM user was created.
        self.create_date = create_date  # type: str
        # The display name of the RAM user.
        self.display_name = display_name  # type: str
        # The email address of the RAM user.
        # 
        # >  This parameter is valid only on the China site (aliyun.com).
        self.email = email  # type: str
        # The last time when the RAM user logged on to the Alibaba Cloud Management Console.
        self.last_login_date = last_login_date  # type: str
        # The mobile phone number of the RAM user.
        # 
        # >  This parameter is valid only on the China site (aliyun.com).
        self.mobile_phone = mobile_phone  # type: str
        # The source of the RAM user. Valid values:
        # 
        # *   Manual: The RAM user is manually created in the RAM console.
        # *   SCIM: The RAM user is mapped by using System for Cross-domain Identity Management (SCIM).
        # *   CloudSSO: The RAM user is mapped from a CloudSSO user.
        self.provision_type = provision_type  # type: str
        # An array that consists of the details of the returned tags.
        self.tags = tags  # type: CreateUserResponseBodyUserTags
        # The time when the information about the RAM user was updated.
        self.update_date = update_date  # type: str
        # The ID of the RAM user.
        self.user_id = user_id  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(CreateUserResponseBodyUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Tags') is not None:
            temp_model = CreateUserResponseBodyUserTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the RAM user.
        self.user = user  # type: CreateUserResponseBodyUser

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super(CreateUserResponseBody, self).to_map()
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
            temp_model = CreateUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
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


class CreateVirtualMFADeviceRequest(TeaModel):
    def __init__(self, virtual_mfadevice_name=None):
        # The name of the MFA device.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, and hyphens (-).
        self.virtual_mfadevice_name = virtual_mfadevice_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVirtualMFADeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.virtual_mfadevice_name is not None:
            result['VirtualMFADeviceName'] = self.virtual_mfadevice_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VirtualMFADeviceName') is not None:
            self.virtual_mfadevice_name = m.get('VirtualMFADeviceName')
        return self


class CreateVirtualMFADeviceResponseBodyVirtualMFADevice(TeaModel):
    def __init__(self, base_32string_seed=None, qrcode_png=None, serial_number=None):
        # The key of the MFA device.
        self.base_32string_seed = base_32string_seed  # type: str
        # The Base64-encoded QR code of the key.
        self.qrcode_png = qrcode_png  # type: str
        # The serial number of the MFA device.
        self.serial_number = serial_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVirtualMFADeviceResponseBodyVirtualMFADevice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_32string_seed is not None:
            result['Base32StringSeed'] = self.base_32string_seed
        if self.qrcode_png is not None:
            result['QRCodePNG'] = self.qrcode_png
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Base32StringSeed') is not None:
            self.base_32string_seed = m.get('Base32StringSeed')
        if m.get('QRCodePNG') is not None:
            self.qrcode_png = m.get('QRCodePNG')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class CreateVirtualMFADeviceResponseBody(TeaModel):
    def __init__(self, request_id=None, virtual_mfadevice=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the MFA device.
        self.virtual_mfadevice = virtual_mfadevice  # type: CreateVirtualMFADeviceResponseBodyVirtualMFADevice

    def validate(self):
        if self.virtual_mfadevice:
            self.virtual_mfadevice.validate()

    def to_map(self):
        _map = super(CreateVirtualMFADeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.virtual_mfadevice is not None:
            result['VirtualMFADevice'] = self.virtual_mfadevice.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VirtualMFADevice') is not None:
            temp_model = CreateVirtualMFADeviceResponseBodyVirtualMFADevice()
            self.virtual_mfadevice = temp_model.from_map(m['VirtualMFADevice'])
        return self


class CreateVirtualMFADeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVirtualMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVirtualMFADeviceResponse, self).to_map()
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
            temp_model = CreateVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessKeyRequest(TeaModel):
    def __init__(self, user_access_key_id=None, user_principal_name=None):
        # The ID of the AccessKey pair that you want to delete.
        self.user_access_key_id = user_access_key_id  # type: str
        # The logon name of the RAM user.
        # 
        # If this parameter is empty, the AccessKey pair of the current user is deleted.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DeleteAccessKeyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessKeyResponseBody, self).to_map()
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


class DeleteAccessKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAccessKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccessKeyResponse, self).to_map()
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
            temp_model = DeleteAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppSecretRequest(TeaModel):
    def __init__(self, app_id=None, app_secret_id=None):
        self.app_id = app_id  # type: str
        self.app_secret_id = app_secret_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        return self


class DeleteAppSecretResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppSecretResponseBody, self).to_map()
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


class DeleteAppSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppSecretResponse, self).to_map()
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
            temp_model = DeleteAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationResponseBody, self).to_map()
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


class DeleteApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApplicationResponse, self).to_map()
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
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(self, group_name=None):
        # The name of the RAM user group.
        self.group_name = group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DeleteGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupResponseBody, self).to_map()
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


class DeleteGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGroupResponse, self).to_map()
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
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoginProfileRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLoginProfileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DeleteLoginProfileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLoginProfileResponseBody, self).to_map()
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


class DeleteLoginProfileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLoginProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLoginProfileResponse, self).to_map()
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
            temp_model = DeleteLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOIDCProviderRequest(TeaModel):
    def __init__(self, oidcprovider_name=None):
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOIDCProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class DeleteOIDCProviderResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOIDCProviderResponseBody, self).to_map()
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


class DeleteOIDCProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteOIDCProviderResponse, self).to_map()
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
            temp_model = DeleteOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSAMLProviderRequest(TeaModel):
    def __init__(self, samlprovider_name=None):
        # The name of the IdP that you want to delete.
        self.samlprovider_name = samlprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSAMLProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        return self


class DeleteSAMLProviderResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSAMLProviderResponseBody, self).to_map()
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


class DeleteSAMLProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSAMLProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSAMLProviderResponse, self).to_map()
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
            temp_model = DeleteSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, user_id=None, user_principal_name=None):
        # The ID of the RAM user.
        # 
        # >  You must specify only one of the following parameters: `UserPrincipalName` and `UserId`.
        self.user_id = user_id  # type: str
        # The logon name of the RAM user.
        # 
        # >  You must specify only one of the following parameters: `UserPrincipalName` and `UserId`.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(self, serial_number=None):
        # The serial number of the MFA device.
        self.serial_number = serial_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVirtualMFADeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class DeleteVirtualMFADeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVirtualMFADeviceResponseBody, self).to_map()
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


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVirtualMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVirtualMFADeviceResponse, self).to_map()
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
            temp_model = DeleteVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableVirtualMFARequest(TeaModel):
    def __init__(self, user_principal_name=None):
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableVirtualMFARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class DisableVirtualMFAResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableVirtualMFAResponseBody, self).to_map()
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


class DisableVirtualMFAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableVirtualMFAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableVirtualMFAResponse, self).to_map()
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
            temp_model = DisableVirtualMFAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCredentialReportResponseBody(TeaModel):
    def __init__(self, request_id=None, state=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The generation status of the user credential report. Valid values:
        # 
        # *   STARTED: The user credential report starts to generate.
        # *   INPROGRESS: The user credential report is being generated.
        # *   COMPLETED: The user credential report is generated.
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateCredentialReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GenerateCredentialReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateCredentialReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateCredentialReportResponse, self).to_map()
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
            temp_model = GenerateCredentialReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessKeyLastUsedRequest(TeaModel):
    def __init__(self, user_access_key_id=None, user_principal_name=None):
        # The ID of the AccessKey pair that you want to query.
        self.user_access_key_id = user_access_key_id  # type: str
        # The logon name of the RAM user.
        # 
        # If this parameter is empty, the AccessKey pair of the current user is queried.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccessKeyLastUsedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed(TeaModel):
    def __init__(self, last_used_date=None, service_name=None):
        # The time when the AccessKey pair was used for the last time.
        self.last_used_date = last_used_date  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_used_date is not None:
            result['LastUsedDate'] = self.last_used_date
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastUsedDate') is not None:
            self.last_used_date = m.get('LastUsedDate')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetAccessKeyLastUsedResponseBody(TeaModel):
    def __init__(self, access_key_last_used=None, request_id=None):
        # The details of the time when the AccessKey pair was used for the last time.
        self.access_key_last_used = access_key_last_used  # type: GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.access_key_last_used:
            self.access_key_last_used.validate()

    def to_map(self):
        _map = super(GetAccessKeyLastUsedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_last_used is not None:
            result['AccessKeyLastUsed'] = self.access_key_last_used.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyLastUsed') is not None:
            temp_model = GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed()
            self.access_key_last_used = temp_model.from_map(m['AccessKeyLastUsed'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessKeyLastUsedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccessKeyLastUsedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccessKeyLastUsedResponse, self).to_map()
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
            temp_model = GetAccessKeyLastUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountMFAInfoResponseBody(TeaModel):
    def __init__(self, is_mfaenable=None, request_id=None):
        # Indicates whether MFA is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.is_mfaenable = is_mfaenable  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountMFAInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_mfaenable is not None:
            result['IsMFAEnable'] = self.is_mfaenable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsMFAEnable') is not None:
            self.is_mfaenable = m.get('IsMFAEnable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountMFAInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountMFAInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountMFAInfoResponse, self).to_map()
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
            temp_model = GetAccountMFAInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo(TeaModel):
    def __init__(self, bind_mfa=None, old_ak_num=None, root_with_access_key=None, sub_user=None,
                 sub_user_bind_mfa=None, sub_user_pwd_level=None, sub_user_with_old_access_key=None,
                 sub_user_with_unused_access_key=None, unused_ak_num=None):
        # Indicates whether MFA is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.bind_mfa = bind_mfa  # type: bool
        # The number of old AccessKey pairs for the Alibaba Cloud account.
        self.old_ak_num = old_ak_num  # type: int
        # The number of AccessKey pairs for the Alibaba Cloud account.
        self.root_with_access_key = root_with_access_key  # type: int
        # The number of RAM users within the Alibaba Cloud account.
        self.sub_user = sub_user  # type: int
        # The number of RAM users that have MFA devices bound.
        self.sub_user_bind_mfa = sub_user_bind_mfa  # type: int
        # The complexity level of the password for the RAM user. Valid values:
        # 
        # *   low
        # *   mid
        # *   high
        self.sub_user_pwd_level = sub_user_pwd_level  # type: str
        # The number of RAM users that use the old AccessKey pairs.
        self.sub_user_with_old_access_key = sub_user_with_old_access_key  # type: int
        # The number of RAM users that have no AccessKey pairs.
        self.sub_user_with_unused_access_key = sub_user_with_unused_access_key  # type: int
        # The number of AccessKey pairs that are not used for the Alibaba Cloud account.
        self.unused_ak_num = unused_ak_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_mfa is not None:
            result['BindMfa'] = self.bind_mfa
        if self.old_ak_num is not None:
            result['OldAkNum'] = self.old_ak_num
        if self.root_with_access_key is not None:
            result['RootWithAccessKey'] = self.root_with_access_key
        if self.sub_user is not None:
            result['SubUser'] = self.sub_user
        if self.sub_user_bind_mfa is not None:
            result['SubUserBindMfa'] = self.sub_user_bind_mfa
        if self.sub_user_pwd_level is not None:
            result['SubUserPwdLevel'] = self.sub_user_pwd_level
        if self.sub_user_with_old_access_key is not None:
            result['SubUserWithOldAccessKey'] = self.sub_user_with_old_access_key
        if self.sub_user_with_unused_access_key is not None:
            result['SubUserWithUnusedAccessKey'] = self.sub_user_with_unused_access_key
        if self.unused_ak_num is not None:
            result['UnusedAkNum'] = self.unused_ak_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindMfa') is not None:
            self.bind_mfa = m.get('BindMfa')
        if m.get('OldAkNum') is not None:
            self.old_ak_num = m.get('OldAkNum')
        if m.get('RootWithAccessKey') is not None:
            self.root_with_access_key = m.get('RootWithAccessKey')
        if m.get('SubUser') is not None:
            self.sub_user = m.get('SubUser')
        if m.get('SubUserBindMfa') is not None:
            self.sub_user_bind_mfa = m.get('SubUserBindMfa')
        if m.get('SubUserPwdLevel') is not None:
            self.sub_user_pwd_level = m.get('SubUserPwdLevel')
        if m.get('SubUserWithOldAccessKey') is not None:
            self.sub_user_with_old_access_key = m.get('SubUserWithOldAccessKey')
        if m.get('SubUserWithUnusedAccessKey') is not None:
            self.sub_user_with_unused_access_key = m.get('SubUserWithUnusedAccessKey')
        if m.get('UnusedAkNum') is not None:
            self.unused_ak_num = m.get('UnusedAkNum')
        return self


class GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo(TeaModel):
    def __init__(self, account_security_practice_user_info=None, score=None):
        # The information of the security report for the Alibaba Cloud account.
        self.account_security_practice_user_info = account_security_practice_user_info  # type: GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo
        # The security score of the Alibaba Cloud account.
        self.score = score  # type: int

    def validate(self):
        if self.account_security_practice_user_info:
            self.account_security_practice_user_info.validate()

    def to_map(self):
        _map = super(GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_security_practice_user_info is not None:
            result['AccountSecurityPracticeUserInfo'] = self.account_security_practice_user_info.to_map()
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountSecurityPracticeUserInfo') is not None:
            temp_model = GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo()
            self.account_security_practice_user_info = temp_model.from_map(m['AccountSecurityPracticeUserInfo'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class GetAccountSecurityPracticeReportResponseBody(TeaModel):
    def __init__(self, account_security_practice_info=None, request_id=None):
        # The information of the security report for the Alibaba Cloud account.
        self.account_security_practice_info = account_security_practice_info  # type: GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.account_security_practice_info:
            self.account_security_practice_info.validate()

    def to_map(self):
        _map = super(GetAccountSecurityPracticeReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_security_practice_info is not None:
            result['AccountSecurityPracticeInfo'] = self.account_security_practice_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountSecurityPracticeInfo') is not None:
            temp_model = GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo()
            self.account_security_practice_info = temp_model.from_map(m['AccountSecurityPracticeInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccountSecurityPracticeReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountSecurityPracticeReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountSecurityPracticeReportResponse, self).to_map()
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
            temp_model = GetAccountSecurityPracticeReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountSummaryResponseBodySummaryMap(TeaModel):
    def __init__(self, access_keys_per_user_quota=None, attached_policies_per_group_quota=None,
                 attached_policies_per_role_quota=None, attached_policies_per_user_quota=None, attached_system_policies_per_group_quota=None,
                 attached_system_policies_per_role_quota=None, attached_system_policies_per_user_quota=None, groups=None, groups_per_user_quota=None,
                 groups_quota=None, mfadevices=None, mfadevices_in_use=None, policies=None, policies_quota=None,
                 policy_size_quota=None, roles=None, roles_quota=None, users=None, users_quota=None, versions_per_policy_quota=None,
                 virtual_mfadevices_quota=None):
        # The maximum number of AccessKey pairs that a RAM user can have.
        self.access_keys_per_user_quota = access_keys_per_user_quota  # type: int
        # The maximum number of custom policies that can be added to a RAM user group.
        self.attached_policies_per_group_quota = attached_policies_per_group_quota  # type: int
        # The maximum number of custom policies that can be added to a RAM role.
        self.attached_policies_per_role_quota = attached_policies_per_role_quota  # type: int
        # The maximum number of custom policies that can be added to a RAM user.
        self.attached_policies_per_user_quota = attached_policies_per_user_quota  # type: int
        # The maximum number of system policies that can be added to a RAM user group.
        self.attached_system_policies_per_group_quota = attached_system_policies_per_group_quota  # type: int
        # The maximum number of system policies that can be added to a RAM role.
        self.attached_system_policies_per_role_quota = attached_system_policies_per_role_quota  # type: int
        # The maximum number of system policies that can be added to a RAM user.
        self.attached_system_policies_per_user_quota = attached_system_policies_per_user_quota  # type: int
        # The number of RAM user groups.
        self.groups = groups  # type: int
        # The maximum number of RAM user groups to which a RAM user can be added.
        self.groups_per_user_quota = groups_per_user_quota  # type: int
        # The maximum number of RAM user groups that can be created.
        self.groups_quota = groups_quota  # type: int
        # The number of virtual multi-factor authentication (MFA) devices.
        self.mfadevices = mfadevices  # type: int
        # The number of virtual MFA devices in use.
        self.mfadevices_in_use = mfadevices_in_use  # type: int
        # The number of custom policies.
        self.policies = policies  # type: int
        # The maximum number of custom policies that can be created.
        self.policies_quota = policies_quota  # type: int
        # The maximum length of the policy content.
        self.policy_size_quota = policy_size_quota  # type: int
        # The number of RAM roles.
        self.roles = roles  # type: int
        # The maximum number of RAM roles that can be created.
        self.roles_quota = roles_quota  # type: int
        # The number of RAM users.
        self.users = users  # type: int
        # The maximum number of RAM users that can be created.
        self.users_quota = users_quota  # type: int
        # The maximum number of policy versions.
        self.versions_per_policy_quota = versions_per_policy_quota  # type: int
        # The maximum number of virtual MFA devices that can be created.
        self.virtual_mfadevices_quota = virtual_mfadevices_quota  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountSummaryResponseBodySummaryMap, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_keys_per_user_quota is not None:
            result['AccessKeysPerUserQuota'] = self.access_keys_per_user_quota
        if self.attached_policies_per_group_quota is not None:
            result['AttachedPoliciesPerGroupQuota'] = self.attached_policies_per_group_quota
        if self.attached_policies_per_role_quota is not None:
            result['AttachedPoliciesPerRoleQuota'] = self.attached_policies_per_role_quota
        if self.attached_policies_per_user_quota is not None:
            result['AttachedPoliciesPerUserQuota'] = self.attached_policies_per_user_quota
        if self.attached_system_policies_per_group_quota is not None:
            result['AttachedSystemPoliciesPerGroupQuota'] = self.attached_system_policies_per_group_quota
        if self.attached_system_policies_per_role_quota is not None:
            result['AttachedSystemPoliciesPerRoleQuota'] = self.attached_system_policies_per_role_quota
        if self.attached_system_policies_per_user_quota is not None:
            result['AttachedSystemPoliciesPerUserQuota'] = self.attached_system_policies_per_user_quota
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.groups_per_user_quota is not None:
            result['GroupsPerUserQuota'] = self.groups_per_user_quota
        if self.groups_quota is not None:
            result['GroupsQuota'] = self.groups_quota
        if self.mfadevices is not None:
            result['MFADevices'] = self.mfadevices
        if self.mfadevices_in_use is not None:
            result['MFADevicesInUse'] = self.mfadevices_in_use
        if self.policies is not None:
            result['Policies'] = self.policies
        if self.policies_quota is not None:
            result['PoliciesQuota'] = self.policies_quota
        if self.policy_size_quota is not None:
            result['PolicySizeQuota'] = self.policy_size_quota
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.roles_quota is not None:
            result['RolesQuota'] = self.roles_quota
        if self.users is not None:
            result['Users'] = self.users
        if self.users_quota is not None:
            result['UsersQuota'] = self.users_quota
        if self.versions_per_policy_quota is not None:
            result['VersionsPerPolicyQuota'] = self.versions_per_policy_quota
        if self.virtual_mfadevices_quota is not None:
            result['VirtualMFADevicesQuota'] = self.virtual_mfadevices_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeysPerUserQuota') is not None:
            self.access_keys_per_user_quota = m.get('AccessKeysPerUserQuota')
        if m.get('AttachedPoliciesPerGroupQuota') is not None:
            self.attached_policies_per_group_quota = m.get('AttachedPoliciesPerGroupQuota')
        if m.get('AttachedPoliciesPerRoleQuota') is not None:
            self.attached_policies_per_role_quota = m.get('AttachedPoliciesPerRoleQuota')
        if m.get('AttachedPoliciesPerUserQuota') is not None:
            self.attached_policies_per_user_quota = m.get('AttachedPoliciesPerUserQuota')
        if m.get('AttachedSystemPoliciesPerGroupQuota') is not None:
            self.attached_system_policies_per_group_quota = m.get('AttachedSystemPoliciesPerGroupQuota')
        if m.get('AttachedSystemPoliciesPerRoleQuota') is not None:
            self.attached_system_policies_per_role_quota = m.get('AttachedSystemPoliciesPerRoleQuota')
        if m.get('AttachedSystemPoliciesPerUserQuota') is not None:
            self.attached_system_policies_per_user_quota = m.get('AttachedSystemPoliciesPerUserQuota')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('GroupsPerUserQuota') is not None:
            self.groups_per_user_quota = m.get('GroupsPerUserQuota')
        if m.get('GroupsQuota') is not None:
            self.groups_quota = m.get('GroupsQuota')
        if m.get('MFADevices') is not None:
            self.mfadevices = m.get('MFADevices')
        if m.get('MFADevicesInUse') is not None:
            self.mfadevices_in_use = m.get('MFADevicesInUse')
        if m.get('Policies') is not None:
            self.policies = m.get('Policies')
        if m.get('PoliciesQuota') is not None:
            self.policies_quota = m.get('PoliciesQuota')
        if m.get('PolicySizeQuota') is not None:
            self.policy_size_quota = m.get('PolicySizeQuota')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('RolesQuota') is not None:
            self.roles_quota = m.get('RolesQuota')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        if m.get('UsersQuota') is not None:
            self.users_quota = m.get('UsersQuota')
        if m.get('VersionsPerPolicyQuota') is not None:
            self.versions_per_policy_quota = m.get('VersionsPerPolicyQuota')
        if m.get('VirtualMFADevicesQuota') is not None:
            self.virtual_mfadevices_quota = m.get('VirtualMFADevicesQuota')
        return self


class GetAccountSummaryResponseBody(TeaModel):
    def __init__(self, request_id=None, summary_map=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The overview information of the Alibaba Cloud account.
        self.summary_map = summary_map  # type: GetAccountSummaryResponseBodySummaryMap

    def validate(self):
        if self.summary_map:
            self.summary_map.validate()

    def to_map(self):
        _map = super(GetAccountSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.summary_map is not None:
            result['SummaryMap'] = self.summary_map.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SummaryMap') is not None:
            temp_model = GetAccountSummaryResponseBodySummaryMap()
            self.summary_map = temp_model.from_map(m['SummaryMap'])
        return self


class GetAccountSummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountSummaryResponse, self).to_map()
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
            temp_model = GetAccountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppSecretRequest(TeaModel):
    def __init__(self, app_id=None, app_secret_id=None):
        self.app_id = app_id  # type: str
        self.app_secret_id = app_secret_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        return self


class GetAppSecretResponseBodyAppSecret(TeaModel):
    def __init__(self, app_id=None, app_secret_id=None, app_secret_value=None, create_date=None):
        self.app_id = app_id  # type: str
        self.app_secret_id = app_secret_id  # type: str
        self.app_secret_value = app_secret_value  # type: str
        self.create_date = create_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppSecretResponseBodyAppSecret, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.app_secret_value is not None:
            result['AppSecretValue'] = self.app_secret_value
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('AppSecretValue') is not None:
            self.app_secret_value = m.get('AppSecretValue')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class GetAppSecretResponseBody(TeaModel):
    def __init__(self, app_secret=None, request_id=None):
        self.app_secret = app_secret  # type: GetAppSecretResponseBodyAppSecret
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_secret:
            self.app_secret.validate()

    def to_map(self):
        _map = super(GetAppSecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppSecret') is not None:
            temp_model = GetAppSecretResponseBodyAppSecret()
            self.app_secret = temp_model.from_map(m['AppSecret'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppSecretResponse, self).to_map()
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
            temp_model = GetAppSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(self, description=None, name=None):
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope, self).to_map()
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


class GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(self, predefined_scope=None):
        self.predefined_scope = predefined_scope  # type: list[GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope]

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class GetApplicationResponseBodyApplicationDelegatedScope(TeaModel):
    def __init__(self, predefined_scopes=None):
        self.predefined_scopes = predefined_scopes  # type: GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super(GetApplicationResponseBodyApplicationDelegatedScope, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = GetApplicationResponseBodyApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class GetApplicationResponseBodyApplicationRedirectUris(TeaModel):
    def __init__(self, redirect_uri=None):
        self.redirect_uri = redirect_uri  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationResponseBodyApplicationRedirectUris, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class GetApplicationResponseBodyApplication(TeaModel):
    def __init__(self, access_token_validity=None, account_id=None, app_id=None, app_name=None, app_type=None,
                 create_date=None, delegated_scope=None, display_name=None, is_multi_tenant=None, redirect_uris=None,
                 refresh_token_validity=None, secret_required=None, update_date=None):
        self.access_token_validity = access_token_validity  # type: int
        self.account_id = account_id  # type: str
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.create_date = create_date  # type: str
        self.delegated_scope = delegated_scope  # type: GetApplicationResponseBodyApplicationDelegatedScope
        self.display_name = display_name  # type: str
        self.is_multi_tenant = is_multi_tenant  # type: bool
        self.redirect_uris = redirect_uris  # type: GetApplicationResponseBodyApplicationRedirectUris
        self.refresh_token_validity = refresh_token_validity  # type: int
        self.secret_required = secret_required  # type: bool
        self.update_date = update_date  # type: str

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super(GetApplicationResponseBodyApplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = GetApplicationResponseBodyApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('RedirectUris') is not None:
            temp_model = GetApplicationResponseBodyApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(self, application=None, request_id=None):
        self.application = application  # type: GetApplicationResponseBodyApplication
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super(GetApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = GetApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApplicationResponse, self).to_map()
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
            temp_model = GetApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCredentialReportResponseBody(TeaModel):
    def __init__(self, content=None, generated_time=None, request_id=None):
        # The content of the user credential report.
        # 
        # The report is Base64-encoded. After you decode the report, the credential report is in the CSV format.
        self.content = content  # type: str
        # The time when the user credential report was generated.
        self.generated_time = generated_time  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCredentialReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.generated_time is not None:
            result['GeneratedTime'] = self.generated_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GeneratedTime') is not None:
            self.generated_time = m.get('GeneratedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCredentialReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCredentialReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCredentialReportResponse, self).to_map()
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
            temp_model = GetCredentialReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultDomainResponseBody(TeaModel):
    def __init__(self, default_domain_name=None, request_id=None):
        # The default domain name.
        self.default_domain_name = default_domain_name  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDefaultDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDefaultDomainResponse, self).to_map()
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
            temp_model = GetDefaultDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(self, group_name=None):
        # The name of the RAM user group.
        self.group_name = group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetGroupResponseBodyGroup(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, group_id=None, group_name=None,
                 update_date=None):
        # The description.
        self.comments = comments  # type: str
        # The creation time.
        self.create_date = create_date  # type: str
        # The display name of the RAM user group.
        self.display_name = display_name  # type: str
        # The ID of the RAM user group.
        self.group_id = group_id  # type: str
        # The name of the RAM user group.
        self.group_name = group_name  # type: str
        # The update time.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupResponseBodyGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetGroupResponseBody(TeaModel):
    def __init__(self, group=None, request_id=None):
        # The information of the RAM user group.
        self.group = group  # type: GetGroupResponseBodyGroup
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super(GetGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = GetGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGroupResponse, self).to_map()
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
            temp_model = GetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginProfileRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoginProfileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(self, last_login_time=None, mfabind_required=None, password_reset_required=None, status=None,
                 update_date=None, user_principal_name=None):
        # The last time when the RAM user logged on to the console.
        self.last_login_time = last_login_time  # type: str
        # Indicates whether multi-factor authentication (MFA) must be enabled.
        self.mfabind_required = mfabind_required  # type: bool
        # Indicates whether the RAM user must reset the password at the next logon.
        self.password_reset_required = password_reset_required  # type: bool
        # The status of password-based logon.
        self.status = status  # type: str
        # The update time.
        self.update_date = update_date  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoginProfileResponseBodyLoginProfile, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetLoginProfileResponseBody(TeaModel):
    def __init__(self, login_profile=None, request_id=None):
        # The logon information.
        self.login_profile = login_profile  # type: GetLoginProfileResponseBodyLoginProfile
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        _map = super(GetLoginProfileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginProfile') is not None:
            temp_model = GetLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLoginProfileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLoginProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLoginProfileResponse, self).to_map()
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
            temp_model = GetLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOIDCProviderRequest(TeaModel):
    def __init__(self, oidcprovider_name=None):
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOIDCProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class GetOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(self, arn=None, client_ids=None, create_date=None, description=None, fingerprints=None,
                 gmt_create=None, gmt_modified=None, issuer_url=None, oidcprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn  # type: str
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids  # type: str
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date  # type: str
        # The description of the OIDC IdP.
        self.description = description  # type: str
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints  # type: str
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create  # type: str
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified  # type: str
        # The URL of the issuer.
        self.issuer_url = issuer_url  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOIDCProviderResponseBodyOIDCProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetOIDCProviderResponseBody(TeaModel):
    def __init__(self, oidcprovider=None, request_id=None):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider  # type: GetOIDCProviderResponseBodyOIDCProvider
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super(GetOIDCProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = GetOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOIDCProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOIDCProviderResponse, self).to_map()
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
            temp_model = GetOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPasswordPolicyResponseBodyPasswordPolicy(TeaModel):
    def __init__(self, hard_expire=None, max_login_attemps=None, max_password_age=None,
                 minimum_password_different_character=None, minimum_password_length=None, password_not_contain_user_name=None,
                 password_reuse_prevention=None, require_lowercase_characters=None, require_numbers=None, require_symbols=None,
                 require_uppercase_characters=None):
        # Indicates whether to disable logon after the password expires.
        self.hard_expire = hard_expire  # type: bool
        # The maximum number of password retries.
        self.max_login_attemps = max_login_attemps  # type: int
        # The validity period of the password.
        self.max_password_age = max_password_age  # type: int
        # The minimum number of unique characters in the password.
        self.minimum_password_different_character = minimum_password_different_character  # type: int
        # The minimum number of characters in the password.
        self.minimum_password_length = minimum_password_length  # type: int
        # Indicates whether to exclude the username from the password.
        self.password_not_contain_user_name = password_not_contain_user_name  # type: bool
        # The policy for password history check.
        self.password_reuse_prevention = password_reuse_prevention  # type: int
        # Indicates whether the password must contain lowercase letters.
        self.require_lowercase_characters = require_lowercase_characters  # type: bool
        # Indicates whether the password must contain digits.
        self.require_numbers = require_numbers  # type: bool
        # Indicates whether the password must contain special characters.
        self.require_symbols = require_symbols  # type: bool
        # Indicates whether the password must contain uppercase letters.
        self.require_uppercase_characters = require_uppercase_characters  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPasswordPolicyResponseBodyPasswordPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        return self


class GetPasswordPolicyResponseBody(TeaModel):
    def __init__(self, password_policy=None, request_id=None):
        # The details of the password policy.
        self.password_policy = password_policy  # type: GetPasswordPolicyResponseBodyPasswordPolicy
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        _map = super(GetPasswordPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordPolicy') is not None:
            temp_model = GetPasswordPolicyResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPasswordPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPasswordPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPasswordPolicyResponse, self).to_map()
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
            temp_model = GetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSAMLProviderRequest(TeaModel):
    def __init__(self, samlprovider_name=None):
        # The name of the IdP.
        self.samlprovider_name = samlprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSAMLProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        return self


class GetSAMLProviderResponseBodySAMLProvider(TeaModel):
    def __init__(self, arn=None, create_date=None, description=None, encoded_samlmetadata_document=None,
                 samlprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the IdP.
        self.arn = arn  # type: str
        # The creation time.
        self.create_date = create_date  # type: str
        # The description.
        self.description = description  # type: str
        # The metadata file, which is Base64 encoded.
        self.encoded_samlmetadata_document = encoded_samlmetadata_document  # type: str
        # The name of the IdP.
        self.samlprovider_name = samlprovider_name  # type: str
        # The update time.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSAMLProviderResponseBodySAMLProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.encoded_samlmetadata_document is not None:
            result['EncodedSAMLMetadataDocument'] = self.encoded_samlmetadata_document
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
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
        if m.get('EncodedSAMLMetadataDocument') is not None:
            self.encoded_samlmetadata_document = m.get('EncodedSAMLMetadataDocument')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetSAMLProviderResponseBody(TeaModel):
    def __init__(self, request_id=None, samlprovider=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the IdP.
        self.samlprovider = samlprovider  # type: GetSAMLProviderResponseBodySAMLProvider

    def validate(self):
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        _map = super(GetSAMLProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProvider') is not None:
            temp_model = GetSAMLProviderResponseBodySAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class GetSAMLProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSAMLProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSAMLProviderResponse, self).to_map()
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
            temp_model = GetSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(self, allow_user_to_manage_access_keys=None):
        # Specifies whether RAM users can manage their AccessKey pairs. Valid values:
        # 
        # *   true: yes
        # *   false: no
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(self, allow_user_to_change_password=None, enable_save_mfaticket=None, login_network_masks=None,
                 login_session_duration=None, mfaoperation_for_login=None, operation_for_risk_login=None):
        # Specifies whether RAM users can change their passwords. Valid values:
        # 
        # *   true: yes
        # *   false: no
        self.allow_user_to_change_password = allow_user_to_change_password  # type: bool
        # Specifies whether to remember the multi-factor authentication (MFA) devices for seven days. Valid values:
        # 
        # *   true: yes
        # *   false: no
        self.enable_save_mfaticket = enable_save_mfaticket  # type: bool
        # The subnet mask.
        self.login_network_masks = login_network_masks  # type: str
        # The validity period of the logon session of RAM users. Unit: hours.
        self.login_session_duration = login_session_duration  # type: int
        # Specifies whether MFA is required for all RAM users when they log on to the Alibaba Cloud Management Console. This parameter is used to replace the EnforceMFAForLogin parameter. The EnforceMFAForLogin parameter is still valid. However, we recommend that you use the MFAOperationForLogin parameter. Valid values:
        # 
        # *   mandatory: MFA is required for all RAM users. If you use the EnforceMFAForLogin parameter, set the value to true.
        # *   independent: User-specific settings are applied. This is the default value. If you use the EnforceMFAForLogin parameter, set the value to false.
        # *   adaptive: MFA is required only for RAM users who initiated unusual logons.
        self.mfaoperation_for_login = mfaoperation_for_login  # type: str
        # Specifies whether to enable MFA for RAM users who initiated unusual logons. Valid values:
        # 
        # *   autonomous: yes. MFA is prompted for RAM users who initiated unusual logons. However, the RAM users are allowed to skip MFA. This is the default value.
        # *   enforceVerify: no.
        self.operation_for_risk_login = operation_for_risk_login  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.mfaoperation_for_login is not None:
            result['MFAOperationForLogin'] = self.mfaoperation_for_login
        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('MFAOperationForLogin') is not None:
            self.mfaoperation_for_login = m.get('MFAOperationForLogin')
        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(TeaModel):
    def __init__(self, allow_user_to_manage_mfadevices=None):
        # Indicates whether RAM users can manage their MFA devices. Valid values:
        # 
        # *   true: yes
        # *   false: no
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference(TeaModel):
    def __init__(self, allow_user_to_manage_personal_ding_talk=None):
        # Specifies whether RAM users can manage their personal DingTalk accounts, such as binding and unbinding of the accounts. Valid values:
        # 
        # *   true: yes
        # *   false: no
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_personal_ding_talk is not None:
            result['AllowUserToManagePersonalDingTalk'] = self.allow_user_to_manage_personal_ding_talk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToManagePersonalDingTalk') is not None:
            self.allow_user_to_manage_personal_ding_talk = m.get('AllowUserToManagePersonalDingTalk')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference(TeaModel):
    def __init__(self, verification_types=None):
        self.verification_types = verification_types  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_types is not None:
            result['VerificationTypes'] = self.verification_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VerificationTypes') is not None:
            self.verification_types = m.get('VerificationTypes')
        return self


class GetSecurityPreferenceResponseBodySecurityPreference(TeaModel):
    def __init__(self, access_key_preference=None, login_profile_preference=None, mfapreference=None,
                 personal_info_preference=None, verification_preference=None):
        # The AccessKey pair preference.
        self.access_key_preference = access_key_preference  # type: GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference
        # The logon preference.
        self.login_profile_preference = login_profile_preference  # type: GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference
        # The MFA preference.
        self.mfapreference = mfapreference  # type: GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference
        # The personal information preference.
        self.personal_info_preference = personal_info_preference  # type: GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference
        self.verification_preference = verification_preference  # type: GetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()
        if self.personal_info_preference:
            self.personal_info_preference.validate()
        if self.verification_preference:
            self.verification_preference.validate()

    def to_map(self):
        _map = super(GetSecurityPreferenceResponseBodySecurityPreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        if self.personal_info_preference is not None:
            result['PersonalInfoPreference'] = self.personal_info_preference.to_map()
        if self.verification_preference is not None:
            result['VerificationPreference'] = self.verification_preference.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m['AccessKeyPreference'])
        if m.get('LoginProfilePreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m['LoginProfilePreference'])
        if m.get('MFAPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m['MFAPreference'])
        if m.get('PersonalInfoPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference()
            self.personal_info_preference = temp_model.from_map(m['PersonalInfoPreference'])
        if m.get('VerificationPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference()
            self.verification_preference = temp_model.from_map(m['VerificationPreference'])
        return self


class GetSecurityPreferenceResponseBody(TeaModel):
    def __init__(self, request_id=None, security_preference=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of security preferences.
        self.security_preference = security_preference  # type: GetSecurityPreferenceResponseBodySecurityPreference

    def validate(self):
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        _map = super(GetSecurityPreferenceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPreference') is not None:
            temp_model = GetSecurityPreferenceResponseBodySecurityPreference()
            self.security_preference = temp_model.from_map(m['SecurityPreference'])
        return self


class GetSecurityPreferenceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSecurityPreferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSecurityPreferenceResponse, self).to_map()
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
            temp_model = GetSecurityPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(self, user_access_key_id=None, user_id=None, user_principal_name=None):
        # The AccessKey ID of the RAM user.
        # 
        # >  You must specify only one of the following parameters: `UserPrincipalName`, `UserId`, and `UserAccessKeyId`.
        self.user_access_key_id = user_access_key_id  # type: str
        # The ID of the RAM user.
        # 
        # >  You must specify only one of the following parameters: `UserPrincipalName`, `UserId`, and `UserAccessKeyId`.
        self.user_id = user_id  # type: str
        # The logon name of the RAM user.
        # 
        # The name is in the format of `<username>@<AccountAlias>.onaliyun.com`. `<username>` indicates the name of the RAM user. `<AccountAlias>.onaliyun.com` indicates the default domain name.
        # 
        # The value of `UserPrincipalName` must be 1 to 128 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (\_). The value of `<AccountAlias>.onaliyun.com` must be 1 to 64 characters in length.
        # 
        # >  You must specify only one of the following parameters: `UserPrincipalName`, `UserId`, and `UserAccessKeyId`.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetUserResponseBodyUserTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyUserTagsTag, self).to_map()
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


class GetUserResponseBodyUserTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[GetUserResponseBodyUserTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserResponseBodyUserTags, self).to_map()
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
                temp_model = GetUserResponseBodyUserTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, email=None, last_login_date=None,
                 mobile_phone=None, provision_type=None, tags=None, update_date=None, user_id=None, user_principal_name=None):
        # The description.
        self.comments = comments  # type: str
        # The time when the RAM user was created.
        self.create_date = create_date  # type: str
        # The display name of the RAM user.
        self.display_name = display_name  # type: str
        # The email address of the RAM user.
        # 
        # >  This parameter is valid only on the China site (aliyun.com).
        self.email = email  # type: str
        # The last time when the RAM user logged on to the Alibaba Cloud Management Console.
        self.last_login_date = last_login_date  # type: str
        # The mobile phone number of the RAM user.
        # 
        # >  This parameter is valid only on the China site (aliyun.com).
        self.mobile_phone = mobile_phone  # type: str
        # The source of the RAM user. Valid values:
        # 
        # *   Manual: The RAM user is manually created in the RAM console.
        # *   SCIM: The RAM user is mapped by using System for Cross-domain Identity Management (SCIM).
        # *   CloudSSO: The RAM user is mapped from a CloudSSO user.
        self.provision_type = provision_type  # type: str
        # An array that consists of tags.
        self.tags = tags  # type: GetUserResponseBodyUserTags
        # The time when the information about the RAM user was updated.
        self.update_date = update_date  # type: str
        # The ID of the RAM user.
        self.user_id = user_id  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(GetUserResponseBodyUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Tags') is not None:
            temp_model = GetUserResponseBodyUserTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the RAM user.
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


class GetUserMFAInfoRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        # The logon name of the RAM user. This parameter is differently set in the following scenarios:
        # 
        # *   If you use a RAM user to call this operation, this parameter can be left empty. If you do not specify this parameter, the information of the MFA device that is bound to the RAM user is queried.
        # *   If you use an Alibaba Cloud account to call this operation, you must set this parameter to the logon name of the RAM user that you want to query.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserMFAInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class GetUserMFAInfoResponseBodyMFADevice(TeaModel):
    def __init__(self, serial_number=None, type=None):
        # The serial number of the MFA device.
        self.serial_number = serial_number  # type: str
        # The type of the MFA device. Valid values:
        # 
        # *   VMFA: virtual MFA device
        # *   U2F: Universal 2nd Factor (U2F) security key
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserMFAInfoResponseBodyMFADevice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetUserMFAInfoResponseBody(TeaModel):
    def __init__(self, is_mfaenable=None, mfadevice=None, request_id=None):
        # Indicates whether the MFA device is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.is_mfaenable = is_mfaenable  # type: bool
        # The information about the MFA device.
        self.mfadevice = mfadevice  # type: GetUserMFAInfoResponseBodyMFADevice
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        _map = super(GetUserMFAInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_mfaenable is not None:
            result['IsMFAEnable'] = self.is_mfaenable
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsMFAEnable') is not None:
            self.is_mfaenable = m.get('IsMFAEnable')
        if m.get('MFADevice') is not None:
            temp_model = GetUserMFAInfoResponseBodyMFADevice()
            self.mfadevice = temp_model.from_map(m['MFADevice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserMFAInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserMFAInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserMFAInfoResponse, self).to_map()
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
            temp_model = GetUserMFAInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserSsoSettingsResponseBodyUserSsoSettings(TeaModel):
    def __init__(self, auxiliary_domain=None, metadata_document=None, sso_enabled=None):
        # The auxiliary domain name.
        self.auxiliary_domain = auxiliary_domain  # type: str
        # The metadata file, which is Base64-encoded.
        self.metadata_document = metadata_document  # type: str
        # Indicates whether user-based SSO is enabled.
        self.sso_enabled = sso_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserSsoSettingsResponseBodyUserSsoSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        return self


class GetUserSsoSettingsResponseBody(TeaModel):
    def __init__(self, request_id=None, user_sso_settings=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The configurations of user-based SSO.
        self.user_sso_settings = user_sso_settings  # type: GetUserSsoSettingsResponseBodyUserSsoSettings

    def validate(self):
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        _map = super(GetUserSsoSettingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_sso_settings is not None:
            result['UserSsoSettings'] = self.user_sso_settings.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSsoSettings') is not None:
            temp_model = GetUserSsoSettingsResponseBodyUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(m['UserSsoSettings'])
        return self


class GetUserSsoSettingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserSsoSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserSsoSettingsResponse, self).to_map()
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
            temp_model = GetUserSsoSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessKeysRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        # The logon name of the RAM user.
        # 
        # If this parameter is empty, the AccessKey pairs of the current user are queried.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccessKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListAccessKeysResponseBodyAccessKeysAccessKey(TeaModel):
    def __init__(self, access_key_id=None, create_date=None, status=None, update_date=None):
        # The AccessKey ID.
        self.access_key_id = access_key_id  # type: str
        # The time when the AccessKey pair was created.
        self.create_date = create_date  # type: str
        # The status of the AccessKey pair. Valid values:
        # 
        # *   Active
        # *   Inactive
        self.status = status  # type: str
        # The time when the AccessKey pair was updated.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccessKeysResponseBodyAccessKeysAccessKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListAccessKeysResponseBodyAccessKeys(TeaModel):
    def __init__(self, access_key=None):
        self.access_key = access_key  # type: list[ListAccessKeysResponseBodyAccessKeysAccessKey]

    def validate(self):
        if self.access_key:
            for k in self.access_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccessKeysResponseBodyAccessKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessKey'] = []
        if self.access_key is not None:
            for k in self.access_key:
                result['AccessKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.access_key = []
        if m.get('AccessKey') is not None:
            for k in m.get('AccessKey'):
                temp_model = ListAccessKeysResponseBodyAccessKeysAccessKey()
                self.access_key.append(temp_model.from_map(k))
        return self


class ListAccessKeysResponseBody(TeaModel):
    def __init__(self, access_keys=None, request_id=None):
        # The list of AccessKey pairs.
        self.access_keys = access_keys  # type: ListAccessKeysResponseBodyAccessKeys
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.access_keys:
            self.access_keys.validate()

    def to_map(self):
        _map = super(ListAccessKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_keys is not None:
            result['AccessKeys'] = self.access_keys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeys') is not None:
            temp_model = ListAccessKeysResponseBodyAccessKeys()
            self.access_keys = temp_model.from_map(m['AccessKeys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccessKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccessKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccessKeysResponse, self).to_map()
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
            temp_model = ListAccessKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppSecretIdsRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppSecretIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListAppSecretIdsResponseBodyAppSecretsAppSecret(TeaModel):
    def __init__(self, app_id=None, app_secret_id=None, create_date=None):
        self.app_id = app_id  # type: str
        self.app_secret_id = app_secret_id  # type: str
        self.create_date = create_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppSecretIdsResponseBodyAppSecretsAppSecret, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret_id is not None:
            result['AppSecretId'] = self.app_secret_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecretId') is not None:
            self.app_secret_id = m.get('AppSecretId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        return self


class ListAppSecretIdsResponseBodyAppSecrets(TeaModel):
    def __init__(self, app_secret=None):
        self.app_secret = app_secret  # type: list[ListAppSecretIdsResponseBodyAppSecretsAppSecret]

    def validate(self):
        if self.app_secret:
            for k in self.app_secret:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppSecretIdsResponseBodyAppSecrets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppSecret'] = []
        if self.app_secret is not None:
            for k in self.app_secret:
                result['AppSecret'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_secret = []
        if m.get('AppSecret') is not None:
            for k in m.get('AppSecret'):
                temp_model = ListAppSecretIdsResponseBodyAppSecretsAppSecret()
                self.app_secret.append(temp_model.from_map(k))
        return self


class ListAppSecretIdsResponseBody(TeaModel):
    def __init__(self, app_secrets=None, request_id=None):
        self.app_secrets = app_secrets  # type: ListAppSecretIdsResponseBodyAppSecrets
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_secrets:
            self.app_secrets.validate()

    def to_map(self):
        _map = super(ListAppSecretIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_secrets is not None:
            result['AppSecrets'] = self.app_secrets.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppSecrets') is not None:
            temp_model = ListAppSecretIdsResponseBodyAppSecrets()
            self.app_secrets = temp_model.from_map(m['AppSecrets'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppSecretIdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppSecretIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppSecretIdsResponse, self).to_map()
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
            temp_model = ListAppSecretIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(self, description=None, name=None):
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope, self).to_map()
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


class ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(self, predefined_scope=None):
        self.predefined_scope = predefined_scope  # type: list[ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope]

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBodyApplicationsApplicationDelegatedScope(TeaModel):
    def __init__(self, predefined_scopes=None):
        self.predefined_scopes = predefined_scopes  # type: ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super(ListApplicationsResponseBodyApplicationsApplicationDelegatedScope, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class ListApplicationsResponseBodyApplicationsApplicationRedirectUris(TeaModel):
    def __init__(self, redirect_uri=None):
        self.redirect_uri = redirect_uri  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsResponseBodyApplicationsApplicationRedirectUris, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class ListApplicationsResponseBodyApplicationsApplication(TeaModel):
    def __init__(self, access_token_validity=None, account_id=None, app_id=None, app_name=None, app_type=None,
                 create_date=None, delegated_scope=None, display_name=None, is_multi_tenant=None, redirect_uris=None,
                 refresh_token_validity=None, secret_required=None, update_date=None):
        self.access_token_validity = access_token_validity  # type: int
        self.account_id = account_id  # type: str
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.create_date = create_date  # type: str
        self.delegated_scope = delegated_scope  # type: ListApplicationsResponseBodyApplicationsApplicationDelegatedScope
        self.display_name = display_name  # type: str
        self.is_multi_tenant = is_multi_tenant  # type: bool
        self.redirect_uris = redirect_uris  # type: ListApplicationsResponseBodyApplicationsApplicationRedirectUris
        self.refresh_token_validity = refresh_token_validity  # type: int
        self.secret_required = secret_required  # type: bool
        self.update_date = update_date  # type: str

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super(ListApplicationsResponseBodyApplicationsApplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('RedirectUris') is not None:
            temp_model = ListApplicationsResponseBodyApplicationsApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListApplicationsResponseBodyApplications(TeaModel):
    def __init__(self, application=None):
        self.application = application  # type: list[ListApplicationsResponseBodyApplicationsApplication]

    def validate(self):
        if self.application:
            for k in self.application:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsResponseBodyApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = ListApplicationsResponseBodyApplicationsApplication()
                self.application.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(self, applications=None, request_id=None):
        self.applications = applications  # type: ListApplicationsResponseBodyApplications
        self.request_id = request_id  # type: str

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        _map = super(ListApplicationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Applications') is not None:
            temp_model = ListApplicationsResponseBodyApplications()
            self.applications = temp_model.from_map(m['Applications'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationsResponse, self).to_map()
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
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 100. Default value: 100.
        self.max_items = max_items  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListGroupsResponseBodyGroupsGroup(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, group_id=None, group_name=None,
                 update_date=None):
        # The description.
        self.comments = comments  # type: str
        # The creation time.
        self.create_date = create_date  # type: str
        # The display name of the RAM user group.
        self.display_name = display_name  # type: str
        # The ID of the RAM user group.
        self.group_id = group_id  # type: str
        # The name of the RAM user group.
        self.group_name = group_name  # type: str
        # The update time.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsResponseBodyGroupsGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListGroupsResponseBodyGroups(TeaModel):
    def __init__(self, group=None):
        self.group = group  # type: list[ListGroupsResponseBodyGroupsGroup]

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupsResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = ListGroupsResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(self, groups=None, is_truncated=None, marker=None, request_id=None):
        # The information of the RAM user groups.
        self.groups = groups  # type: ListGroupsResponseBodyGroups
        # Indicates whether the response is truncated. Valid values:
        # 
        # - true
        # - false
        self.is_truncated = is_truncated  # type: bool
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        _map = super(ListGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Groups') is not None:
            temp_model = ListGroupsResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupsResponse, self).to_map()
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
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsForUserRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsForUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListGroupsForUserResponseBodyGroupsGroup(TeaModel):
    def __init__(self, comments=None, display_name=None, group_id=None, group_name=None, join_date=None):
        # The description.
        self.comments = comments  # type: str
        # The display name of the RAM user group.
        self.display_name = display_name  # type: str
        # The ID of the RAM user group.
        self.group_id = group_id  # type: str
        # The name of the RAM user group.
        self.group_name = group_name  # type: str
        # The time when the RAM user was added.
        self.join_date = join_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsForUserResponseBodyGroupsGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')
        return self


class ListGroupsForUserResponseBodyGroups(TeaModel):
    def __init__(self, group=None):
        self.group = group  # type: list[ListGroupsForUserResponseBodyGroupsGroup]

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupsForUserResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = ListGroupsForUserResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class ListGroupsForUserResponseBody(TeaModel):
    def __init__(self, groups=None, request_id=None):
        # The information of the RAM user groups.
        self.groups = groups  # type: ListGroupsForUserResponseBodyGroups
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        _map = super(ListGroupsForUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Groups') is not None:
            temp_model = ListGroupsForUserResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGroupsForUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupsForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupsForUserResponse, self).to_map()
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
            temp_model = ListGroupsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOIDCProvidersRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 100. Default value: 100.
        self.max_items = max_items  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOIDCProvidersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListOIDCProvidersResponseBodyOIDCProvidersOIDCProvider(TeaModel):
    def __init__(self, arn=None, client_ids=None, create_date=None, description=None, fingerprints=None,
                 gmt_create=None, gmt_modified=None, issuer_url=None, oidcprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn  # type: str
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids  # type: str
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date  # type: str
        # The description of the OIDC IdP.
        self.description = description  # type: str
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints  # type: str
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create  # type: str
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified  # type: str
        # The URL of the issuer.
        self.issuer_url = issuer_url  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOIDCProvidersResponseBodyOIDCProvidersOIDCProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListOIDCProvidersResponseBodyOIDCProviders(TeaModel):
    def __init__(self, oidcprovider=None):
        self.oidcprovider = oidcprovider  # type: list[ListOIDCProvidersResponseBodyOIDCProvidersOIDCProvider]

    def validate(self):
        if self.oidcprovider:
            for k in self.oidcprovider:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOIDCProvidersResponseBodyOIDCProviders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OIDCProvider'] = []
        if self.oidcprovider is not None:
            for k in self.oidcprovider:
                result['OIDCProvider'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.oidcprovider = []
        if m.get('OIDCProvider') is not None:
            for k in m.get('OIDCProvider'):
                temp_model = ListOIDCProvidersResponseBodyOIDCProvidersOIDCProvider()
                self.oidcprovider.append(temp_model.from_map(k))
        return self


class ListOIDCProvidersResponseBody(TeaModel):
    def __init__(self, is_truncated=None, marker=None, oidcproviders=None, request_id=None):
        # Indicates whether the response is truncated. Valid values:
        # 
        # - true
        # - false
        self.is_truncated = is_truncated  # type: bool
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The information about the OIDC IdP.
        self.oidcproviders = oidcproviders  # type: ListOIDCProvidersResponseBodyOIDCProviders
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oidcproviders:
            self.oidcproviders.validate()

    def to_map(self):
        _map = super(ListOIDCProvidersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.oidcproviders is not None:
            result['OIDCProviders'] = self.oidcproviders.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('OIDCProviders') is not None:
            temp_model = ListOIDCProvidersResponseBodyOIDCProviders()
            self.oidcproviders = temp_model.from_map(m['OIDCProviders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOIDCProvidersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOIDCProvidersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOIDCProvidersResponse, self).to_map()
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
            temp_model = ListOIDCProvidersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPredefinedScopesRequest(TeaModel):
    def __init__(self, app_type=None):
        self.app_type = app_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPredefinedScopesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope(TeaModel):
    def __init__(self, description=None, name=None):
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope, self).to_map()
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


class ListPredefinedScopesResponseBodyPredefinedScopes(TeaModel):
    def __init__(self, predefined_scope=None):
        self.predefined_scope = predefined_scope  # type: list[ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope]

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPredefinedScopesResponseBodyPredefinedScopes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class ListPredefinedScopesResponseBody(TeaModel):
    def __init__(self, predefined_scopes=None, request_id=None):
        self.predefined_scopes = predefined_scopes  # type: ListPredefinedScopesResponseBodyPredefinedScopes
        self.request_id = request_id  # type: str

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super(ListPredefinedScopesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = ListPredefinedScopesResponseBodyPredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPredefinedScopesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPredefinedScopesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPredefinedScopesResponse, self).to_map()
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
            temp_model = ListPredefinedScopesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSAMLProvidersRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 100. Default value: 100.
        self.max_items = max_items  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSAMLProvidersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider(TeaModel):
    def __init__(self, arn=None, create_date=None, description=None, samlprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the IdP.
        self.arn = arn  # type: str
        # The creation time.
        self.create_date = create_date  # type: str
        # The description.
        self.description = description  # type: str
        # The name of the IdP.
        self.samlprovider_name = samlprovider_name  # type: str
        # The update time.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
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
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListSAMLProvidersResponseBodySAMLProviders(TeaModel):
    def __init__(self, samlprovider=None):
        self.samlprovider = samlprovider  # type: list[ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider]

    def validate(self):
        if self.samlprovider:
            for k in self.samlprovider:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSAMLProvidersResponseBodySAMLProviders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SAMLProvider'] = []
        if self.samlprovider is not None:
            for k in self.samlprovider:
                result['SAMLProvider'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.samlprovider = []
        if m.get('SAMLProvider') is not None:
            for k in m.get('SAMLProvider'):
                temp_model = ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider()
                self.samlprovider.append(temp_model.from_map(k))
        return self


class ListSAMLProvidersResponseBody(TeaModel):
    def __init__(self, is_truncated=None, marker=None, request_id=None, samlproviders=None):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated  # type: bool
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the IdP.
        self.samlproviders = samlproviders  # type: ListSAMLProvidersResponseBodySAMLProviders

    def validate(self):
        if self.samlproviders:
            self.samlproviders.validate()

    def to_map(self):
        _map = super(ListSAMLProvidersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlproviders is not None:
            result['SAMLProviders'] = self.samlproviders.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProviders') is not None:
            temp_model = ListSAMLProvidersResponseBodySAMLProviders()
            self.samlproviders = temp_model.from_map(m['SAMLProviders'])
        return self


class ListSAMLProvidersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSAMLProvidersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSAMLProvidersResponse, self).to_map()
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
            temp_model = ListSAMLProvidersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.key = key  # type: str
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
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
    def __init__(self, next_token=None, page_size=None, resource_id=None, resource_principal_name=None,
                 resource_type=None, tag=None):
        # The token that is used to initiate the next request if the response of the current request is truncated. You can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The number of entries to return. If a response is truncated because it reaches the value of PageSize, the value of IsTruncated will be true.
        # 
        # Valid values: 1 to 100. Default value: 100.
        self.page_size = page_size  # type: int
        self.resource_id = resource_id  # type: list[str]
        self.resource_principal_name = resource_principal_name  # type: list[str]
        # The type of the resource. Valid values:
        # 
        # *   user: a RAM user
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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_principal_name is not None:
            result['ResourcePrincipalName'] = self.resource_principal_name
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
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourcePrincipalName') is not None:
            self.resource_principal_name = m.get('ResourcePrincipalName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The type of the resource. Valid values:
        # 
        # *   user: a RAM user
        self.resource_type = resource_type  # type: str
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
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


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: list[ListTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, is_truncated=None, next_token=None, request_id=None, tag_resources=None):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated  # type: bool
        # The marker. This parameter is returned only if the value of IsTruncated is true. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array consisting of tags that are added to resources.
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
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


class ListUserBasicInfosRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.key = key  # type: str
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserBasicInfosRequestTag, self).to_map()
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


class ListUserBasicInfosRequest(TeaModel):
    def __init__(self, marker=None, max_items=None, tag=None):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 1000. Default value: 100.
        self.max_items = max_items  # type: int
        self.tag = tag  # type: list[ListUserBasicInfosRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserBasicInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListUserBasicInfosRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo(TeaModel):
    def __init__(self, display_name=None, user_id=None, user_principal_name=None):
        # The display name of the RAM user.
        self.display_name = display_name  # type: str
        # The ID of the RAM user.
        self.user_id = user_id  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListUserBasicInfosResponseBodyUserBasicInfos(TeaModel):
    def __init__(self, user_basic_info=None):
        self.user_basic_info = user_basic_info  # type: list[ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo]

    def validate(self):
        if self.user_basic_info:
            for k in self.user_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserBasicInfosResponseBodyUserBasicInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserBasicInfo'] = []
        if self.user_basic_info is not None:
            for k in self.user_basic_info:
                result['UserBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user_basic_info = []
        if m.get('UserBasicInfo') is not None:
            for k in m.get('UserBasicInfo'):
                temp_model = ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo()
                self.user_basic_info.append(temp_model.from_map(k))
        return self


class ListUserBasicInfosResponseBody(TeaModel):
    def __init__(self, is_truncated=None, marker=None, request_id=None, user_basic_infos=None):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated  # type: bool
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of the information about the RAM user.
        self.user_basic_infos = user_basic_infos  # type: ListUserBasicInfosResponseBodyUserBasicInfos

    def validate(self):
        if self.user_basic_infos:
            self.user_basic_infos.validate()

    def to_map(self):
        _map = super(ListUserBasicInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_basic_infos is not None:
            result['UserBasicInfos'] = self.user_basic_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserBasicInfos') is not None:
            temp_model = ListUserBasicInfosResponseBodyUserBasicInfos()
            self.user_basic_infos = temp_model.from_map(m['UserBasicInfos'])
        return self


class ListUserBasicInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserBasicInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserBasicInfosResponse, self).to_map()
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
            temp_model = ListUserBasicInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.key = key  # type: str
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. N must be consecutive.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequestTag, self).to_map()
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


class ListUsersRequest(TeaModel):
    def __init__(self, marker=None, max_items=None, tag=None):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be true.
        # 
        # Valid values: 1 to 1000. Default value: 1000.
        self.max_items = max_items  # type: int
        self.tag = tag  # type: list[ListUsersRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListUsersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListUsersResponseBodyUsersUserTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersResponseBodyUsersUserTagsTag, self).to_map()
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


class ListUsersResponseBodyUsersUserTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[ListUsersResponseBodyUsersUserTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersResponseBodyUsersUserTags, self).to_map()
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
                temp_model = ListUsersResponseBodyUsersUserTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListUsersResponseBodyUsersUser(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, email=None, last_login_date=None,
                 mobile_phone=None, provision_type=None, tags=None, update_date=None, user_id=None, user_principal_name=None):
        # The description.
        self.comments = comments  # type: str
        # The time when the RAM user was created.
        self.create_date = create_date  # type: str
        # The display name of the RAM user.
        self.display_name = display_name  # type: str
        # The email address of the RAM user.
        # 
        # >  This parameter is valid only on the China site (aliyun.com).
        self.email = email  # type: str
        # The last time when the RAM user logged on to the Alibaba Cloud Management Console.
        self.last_login_date = last_login_date  # type: str
        # The mobile phone number of the RAM user.
        # 
        # >  This parameter is valid only on the China site (aliyun.com).
        self.mobile_phone = mobile_phone  # type: str
        # The source of the RAM user. Valid values:
        # 
        # *   Manual: The RAM user is manually created in the RAM console.
        # *   SCIM: The RAM user is mapped by using System for Cross-domain Identity Management (SCIM).
        # *   CloudSSO: The RAM user is mapped from a CloudSSO user.
        self.provision_type = provision_type  # type: str
        # An array that consists of tags.
        self.tags = tags  # type: ListUsersResponseBodyUsersUserTags
        # The time when the information about the RAM user was updated.
        self.update_date = update_date  # type: str
        # The ID of the RAM user.
        self.user_id = user_id  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(ListUsersResponseBodyUsersUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('Tags') is not None:
            temp_model = ListUsersResponseBodyUsersUserTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(self, user=None):
        self.user = user  # type: list[ListUsersResponseBodyUsersUser]

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListUsersResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, is_truncated=None, marker=None, request_id=None, users=None):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated  # type: bool
        # The parameter that is used to obtain the truncated part. It takes effect only when `IsTruncated` is set to `true`.
        self.marker = marker  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of the information about the RAM user.
        self.users = users  # type: ListUsersResponseBodyUsers

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super(ListUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Users') is not None:
            temp_model = ListUsersResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
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


class ListUsersForGroupRequest(TeaModel):
    def __init__(self, group_name=None, marker=None, max_items=None):
        # The name of the RAM user group.
        self.group_name = group_name  # type: str
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 100. Default value: 100.
        self.max_items = max_items  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersForGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListUsersForGroupResponseBodyUsersUser(TeaModel):
    def __init__(self, display_name=None, join_date=None, user_id=None, user_principal_name=None):
        # The display name of the RAM user.
        self.display_name = display_name  # type: str
        # The time when the RAM user was added.
        self.join_date = join_date  # type: str
        # The ID of the RAM user.
        self.user_id = user_id  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersForGroupResponseBodyUsersUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.join_date is not None:
            result['JoinDate'] = self.join_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListUsersForGroupResponseBodyUsers(TeaModel):
    def __init__(self, user=None):
        self.user = user  # type: list[ListUsersForGroupResponseBodyUsersUser]

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersForGroupResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListUsersForGroupResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersForGroupResponseBody(TeaModel):
    def __init__(self, is_truncated=None, marker=None, request_id=None, users=None):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated  # type: bool
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of RAM users.
        self.users = users  # type: ListUsersForGroupResponseBodyUsers

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super(ListUsersForGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Users') is not None:
            temp_model = ListUsersForGroupResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersForGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUsersForGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersForGroupResponse, self).to_map()
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
            temp_model = ListUsersForGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualMFADevicesRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 100. Default value: 100.
        self.max_items = max_items  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVirtualMFADevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser(TeaModel):
    def __init__(self, display_name=None, user_id=None, user_principal_name=None):
        # The display name of the RAM user.
        self.display_name = display_name  # type: str
        # The ID of the RAM user.
        self.user_id = user_id  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice(TeaModel):
    def __init__(self, activate_date=None, serial_number=None, user=None):
        # The time when the MFA device was activated.
        self.activate_date = activate_date  # type: str
        # The serial number of the MFA device.
        self.serial_number = serial_number  # type: str
        # The information of the RAM user that has an MFA device bound.
        self.user = user  # type: ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super(ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activate_date is not None:
            result['ActivateDate'] = self.activate_date
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivateDate') is not None:
            self.activate_date = m.get('ActivateDate')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('User') is not None:
            temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser()
            self.user = temp_model.from_map(m['User'])
        return self


class ListVirtualMFADevicesResponseBodyVirtualMFADevices(TeaModel):
    def __init__(self, virtual_mfadevice=None):
        self.virtual_mfadevice = virtual_mfadevice  # type: list[ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice]

    def validate(self):
        if self.virtual_mfadevice:
            for k in self.virtual_mfadevice:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVirtualMFADevicesResponseBodyVirtualMFADevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VirtualMFADevice'] = []
        if self.virtual_mfadevice is not None:
            for k in self.virtual_mfadevice:
                result['VirtualMFADevice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.virtual_mfadevice = []
        if m.get('VirtualMFADevice') is not None:
            for k in m.get('VirtualMFADevice'):
                temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice()
                self.virtual_mfadevice.append(temp_model.from_map(k))
        return self


class ListVirtualMFADevicesResponseBody(TeaModel):
    def __init__(self, is_truncated=None, marker=None, request_id=None, virtual_mfadevices=None):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated  # type: bool
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.
        self.marker = marker  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the MFA device.
        self.virtual_mfadevices = virtual_mfadevices  # type: ListVirtualMFADevicesResponseBodyVirtualMFADevices

    def validate(self):
        if self.virtual_mfadevices:
            self.virtual_mfadevices.validate()

    def to_map(self):
        _map = super(ListVirtualMFADevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.virtual_mfadevices is not None:
            result['VirtualMFADevices'] = self.virtual_mfadevices.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VirtualMFADevices') is not None:
            temp_model = ListVirtualMFADevicesResponseBodyVirtualMFADevices()
            self.virtual_mfadevices = temp_model.from_map(m['VirtualMFADevices'])
        return self


class ListVirtualMFADevicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVirtualMFADevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVirtualMFADevicesResponse, self).to_map()
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
            temp_model = ListVirtualMFADevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClientIdFromOIDCProviderRequest(TeaModel):
    def __init__(self, client_id=None, oidcprovider_name=None):
        # The client ID that you want to remove.
        # 
        # The client ID can contain letters, digits, and special characters and cannot start with the special characters. The special characters are `periods, (.), hyphens (-), underscores (_), colons (:), and forward slashes (/)`.
        # 
        # The client ID can be up to 64 characters in length.
        self.client_id = client_id  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveClientIdFromOIDCProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class RemoveClientIdFromOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(self, arn=None, client_ids=None, create_date=None, description=None, fingerprints=None,
                 gmt_create=None, gmt_modified=None, issuer_url=None, oidcprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn  # type: str
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids  # type: str
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date  # type: str
        # The description of the OIDC IdP.
        self.description = description  # type: str
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints  # type: str
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create  # type: str
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified  # type: str
        # The URL of the issuer.
        self.issuer_url = issuer_url  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveClientIdFromOIDCProviderResponseBodyOIDCProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class RemoveClientIdFromOIDCProviderResponseBody(TeaModel):
    def __init__(self, oidcprovider=None, request_id=None):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider  # type: RemoveClientIdFromOIDCProviderResponseBodyOIDCProvider
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super(RemoveClientIdFromOIDCProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = RemoveClientIdFromOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveClientIdFromOIDCProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveClientIdFromOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveClientIdFromOIDCProviderResponse, self).to_map()
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
            temp_model = RemoveClientIdFromOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFingerprintFromOIDCProviderRequest(TeaModel):
    def __init__(self, fingerprint=None, oidcprovider_name=None):
        # The fingerprint that you want to remove.
        self.fingerprint = fingerprint  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveFingerprintFromOIDCProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class RemoveFingerprintFromOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(self, arn=None, client_ids=None, create_date=None, description=None, fingerprints=None,
                 gmt_create=None, gmt_modified=None, issuer_url=None, oidcprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn  # type: str
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids  # type: str
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date  # type: str
        # The description of the OIDC IdP.
        self.description = description  # type: str
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints  # type: str
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create  # type: str
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified  # type: str
        # The URL of the issuer.
        self.issuer_url = issuer_url  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveFingerprintFromOIDCProviderResponseBodyOIDCProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class RemoveFingerprintFromOIDCProviderResponseBody(TeaModel):
    def __init__(self, oidcprovider=None, request_id=None):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider  # type: RemoveFingerprintFromOIDCProviderResponseBodyOIDCProvider
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super(RemoveFingerprintFromOIDCProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = RemoveFingerprintFromOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveFingerprintFromOIDCProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveFingerprintFromOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveFingerprintFromOIDCProviderResponse, self).to_map()
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
            temp_model = RemoveFingerprintFromOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromGroupRequest(TeaModel):
    def __init__(self, group_name=None, user_principal_name=None):
        # The name of the RAM user group.
        self.group_name = group_name  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserFromGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class RemoveUserFromGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserFromGroupResponseBody, self).to_map()
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


class RemoveUserFromGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveUserFromGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveUserFromGroupResponse, self).to_map()
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
            temp_model = RemoveUserFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultDomainRequest(TeaModel):
    def __init__(self, default_domain_name=None):
        # The default domain name.
        # 
        # The name is in the format of `<AccountAlias>.onaliyun.com`. `<AccountAlias>` indicates the account alias. By default, the value of AccountAlias is the ID of the Alibaba Cloud account. The default domain name must end with `.onaliyun.com`.
        # 
        # The default domain name can contain up to 64 characters in length. The name can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        # 
        # >  The default domain name cannot start or end with a hyphen (-) and cannot have two consecutive hyphens (-).
        self.default_domain_name = default_domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')
        return self


class SetDefaultDomainResponseBody(TeaModel):
    def __init__(self, default_domain_name=None, request_id=None):
        # The default domain name.
        self.default_domain_name = default_domain_name  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_domain_name is not None:
            result['DefaultDomainName'] = self.default_domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultDomainName') is not None:
            self.default_domain_name = m.get('DefaultDomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDefaultDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDefaultDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDefaultDomainResponse, self).to_map()
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
            temp_model = SetDefaultDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPasswordPolicyRequest(TeaModel):
    def __init__(self, hard_expire=None, max_login_attemps=None, max_password_age=None,
                 minimum_password_different_character=None, minimum_password_length=None, password_not_contain_user_name=None,
                 password_reuse_prevention=None, require_lowercase_characters=None, require_numbers=None, require_symbols=None,
                 require_uppercase_characters=None):
        # Specifies whether to disable logon after the password expires. Valid values:
        # 
        # *   true: After the password expires, you cannot use the password to log on to the console. You can log on to the console only after you reset the password by using your Alibaba Cloud account or as a RAM user that has administrative rights.
        # *   false: After the password expires, you can change the password to log on to the console. This is the default value.
        self.hard_expire = hard_expire  # type: bool
        # The maximum number of password retries. If you enter the wrong passwords for the specified consecutive times, the account is locked for one hour.
        # 
        # Valid values: 0 to 32.
        # 
        # The default value is 0, which indicates that the password retries are not limited.
        self.max_login_attemps = max_login_attemps  # type: int
        # The validity period of the password.
        # 
        # Valid values: 0 to 1095. Unit: days.
        # 
        # The default value is 0, which indicates that the password never expires.
        self.max_password_age = max_password_age  # type: int
        # The minimum number of unique characters in the password.
        # 
        # Valid values: 0 to 8.
        # 
        # The default value is 0, which indicates that no limits are imposed on the number of unique characters in a password.
        self.minimum_password_different_character = minimum_password_different_character  # type: int
        # The minimum number of characters in the password.
        # 
        # Valid values: 8 to 32. Default value: 8.
        self.minimum_password_length = minimum_password_length  # type: int
        # Specifies whether to exclude the username from the password. Valid values:
        # 
        # *   true: A password cannot contain the username.
        # *   false: A password can contain the username. This is the default value.
        self.password_not_contain_user_name = password_not_contain_user_name  # type: bool
        # The policy for password history check.
        # 
        # The previous N passwords cannot be reused. Valid values of N: 0 to 24.
        # 
        # The default value is 0, which indicates that RAM users can reuse previous passwords.
        self.password_reuse_prevention = password_reuse_prevention  # type: int
        # Specifies whether the password must contain lowercase letters. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.require_lowercase_characters = require_lowercase_characters  # type: bool
        # Specifies whether the password must contain digits. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.require_numbers = require_numbers  # type: bool
        # Specifies whether the password must contain special characters. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.require_symbols = require_symbols  # type: bool
        # Specifies whether the password must contain uppercase letters. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.require_uppercase_characters = require_uppercase_characters  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPasswordPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        return self


class SetPasswordPolicyResponseBodyPasswordPolicy(TeaModel):
    def __init__(self, hard_expire=None, max_login_attemps=None, max_password_age=None,
                 minimum_password_different_character=None, minimum_password_length=None, password_not_contain_user_name=None,
                 password_reuse_prevention=None, require_lowercase_characters=None, require_numbers=None, require_symbols=None,
                 require_uppercase_characters=None):
        # Indicates whether to disable logon after the password expires.
        self.hard_expire = hard_expire  # type: bool
        # The maximum number of password retries.
        self.max_login_attemps = max_login_attemps  # type: int
        # The validity period of the password.
        self.max_password_age = max_password_age  # type: int
        # The minimum number of unique characters in the password.
        self.minimum_password_different_character = minimum_password_different_character  # type: int
        # The minimum number of characters in the password.
        self.minimum_password_length = minimum_password_length  # type: int
        # Indicates whether to exclude the username from the password.
        self.password_not_contain_user_name = password_not_contain_user_name  # type: bool
        # The policy for password history check.
        self.password_reuse_prevention = password_reuse_prevention  # type: int
        # Indicates whether the password must contain lowercase letters.
        self.require_lowercase_characters = require_lowercase_characters  # type: bool
        # Indicates whether the password must contain digits.
        self.require_numbers = require_numbers  # type: bool
        # Indicates whether the password must contain special characters.
        self.require_symbols = require_symbols  # type: bool
        # Indicates whether the password must contain uppercase letters.
        self.require_uppercase_characters = require_uppercase_characters  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPasswordPolicyResponseBodyPasswordPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire
        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps
        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age
        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character
        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length
        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name
        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention
        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters
        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers
        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols
        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')
        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')
        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')
        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')
        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')
        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')
        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')
        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')
        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')
        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')
        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')
        return self


class SetPasswordPolicyResponseBody(TeaModel):
    def __init__(self, password_policy=None, request_id=None):
        # The details of the password policy.
        self.password_policy = password_policy  # type: SetPasswordPolicyResponseBodyPasswordPolicy
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        _map = super(SetPasswordPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordPolicy') is not None:
            temp_model = SetPasswordPolicyResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m['PasswordPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetPasswordPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetPasswordPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetPasswordPolicyResponse, self).to_map()
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
            temp_model = SetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSecurityPreferenceRequest(TeaModel):
    def __init__(self, allow_user_to_change_password=None, allow_user_to_manage_access_keys=None,
                 allow_user_to_manage_mfadevices=None, allow_user_to_manage_personal_ding_talk=None, enable_save_mfaticket=None,
                 login_network_masks=None, login_session_duration=None, mfaoperation_for_login=None, operation_for_risk_login=None,
                 verification_types=None):
        # Specifies whether RAM users can change their passwords. Valid values:
        # 
        # *   true: yes. This is the default value.
        # *   false: no.
        self.allow_user_to_change_password = allow_user_to_change_password  # type: bool
        # Specifies whether RAM users can manage their AccessKey pairs. Valid values:
        # 
        # *   true: yes.
        # *   false: no. This is the default value.
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys  # type: bool
        # Specifies whether RAM users can manage their MFA devices. Valid values:
        # 
        # *   true: yes. This is the default value.
        # *   false: no.
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices  # type: bool
        # Specifies whether RAM users can manage their personal DingTalk accounts, such as binding and unbinding of the accounts. Valid values:
        # 
        # *   true: yes. This is the default value.
        # *   false: no.
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk  # type: bool
        # Specifies whether to remember the MFA devices for seven days. Valid values:
        # 
        # *   true: yes.
        # *   false: no. This is the default value.
        self.enable_save_mfaticket = enable_save_mfaticket  # type: bool
        # The subnet mask that specifies the IP addresses from which you can log on to the Alibaba Cloud Management Console. This parameter takes effect on password-based logon and single sign-on (SSO). However, this parameter does not take effect on API calls that are authenticated by using AccessKey pairs.
        # 
        # *   If you specify a subnet mask, RAM users can use only the IP addresses in the subnet mask to log on to the Alibaba Cloud Management Console.
        # *   If you do not specify a subnet mask, RAM users can use all IP addresses to log on to the Alibaba Cloud Management Console.
        # 
        # If you need to specify multiple subnet masks, separate the subnet masks with semicolons (;). Example: 192.168.0.0/16;10.0.0.0/8.
        # 
        # You can specify up to 25 subnet masks. The total length of the subnet masks can be a maximum of 512 characters.
        self.login_network_masks = login_network_masks  # type: str
        # The validity period of the logon session of RAM users.
        # 
        # Valid values: 1 to 24. Unit: hours.
        # 
        # Default value: 6.
        self.login_session_duration = login_session_duration  # type: int
        # Specifies whether MFA is required for all RAM users when they log on to the Alibaba Cloud Management Console. This parameter is used to replace the EnforceMFAForLogin parameter. The EnforceMFAForLogin parameter is still valid. However, we recommend that you use the MFAOperationForLogin parameter. Valid values:
        # 
        # *   mandatory: MFA is required for all RAM users. If you use the EnforceMFAForLogin parameter, set the value to true.
        # *   independent: User-specific settings are applied. This is the default value. If you use the EnforceMFAForLogin parameter, set the value to false.
        # *   adaptive: MFA is required only for RAM users who initiated unusual logons.
        self.mfaoperation_for_login = mfaoperation_for_login  # type: str
        # Specifies whether to enable MFA for RAM users who initiated unusual logons. Valid values:
        # 
        # *   autonomous: yes. MFA is prompted for RAM users who initiated unusual logons. However, the RAM users are allowed to skip MFA. This is the default value.
        # *   enforceVerify: no.
        self.operation_for_risk_login = operation_for_risk_login  # type: str
        self.verification_types = verification_types  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSecurityPreferenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        if self.allow_user_to_manage_personal_ding_talk is not None:
            result['AllowUserToManagePersonalDingTalk'] = self.allow_user_to_manage_personal_ding_talk
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.mfaoperation_for_login is not None:
            result['MFAOperationForLogin'] = self.mfaoperation_for_login
        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login
        if self.verification_types is not None:
            result['VerificationTypes'] = self.verification_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        if m.get('AllowUserToManagePersonalDingTalk') is not None:
            self.allow_user_to_manage_personal_ding_talk = m.get('AllowUserToManagePersonalDingTalk')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('MFAOperationForLogin') is not None:
            self.mfaoperation_for_login = m.get('MFAOperationForLogin')
        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')
        if m.get('VerificationTypes') is not None:
            self.verification_types = m.get('VerificationTypes')
        return self


class SetSecurityPreferenceShrinkRequest(TeaModel):
    def __init__(self, allow_user_to_change_password=None, allow_user_to_manage_access_keys=None,
                 allow_user_to_manage_mfadevices=None, allow_user_to_manage_personal_ding_talk=None, enable_save_mfaticket=None,
                 login_network_masks=None, login_session_duration=None, mfaoperation_for_login=None, operation_for_risk_login=None,
                 verification_types_shrink=None):
        # Specifies whether RAM users can change their passwords. Valid values:
        # 
        # *   true: yes. This is the default value.
        # *   false: no.
        self.allow_user_to_change_password = allow_user_to_change_password  # type: bool
        # Specifies whether RAM users can manage their AccessKey pairs. Valid values:
        # 
        # *   true: yes.
        # *   false: no. This is the default value.
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys  # type: bool
        # Specifies whether RAM users can manage their MFA devices. Valid values:
        # 
        # *   true: yes. This is the default value.
        # *   false: no.
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices  # type: bool
        # Specifies whether RAM users can manage their personal DingTalk accounts, such as binding and unbinding of the accounts. Valid values:
        # 
        # *   true: yes. This is the default value.
        # *   false: no.
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk  # type: bool
        # Specifies whether to remember the MFA devices for seven days. Valid values:
        # 
        # *   true: yes.
        # *   false: no. This is the default value.
        self.enable_save_mfaticket = enable_save_mfaticket  # type: bool
        # The subnet mask that specifies the IP addresses from which you can log on to the Alibaba Cloud Management Console. This parameter takes effect on password-based logon and single sign-on (SSO). However, this parameter does not take effect on API calls that are authenticated by using AccessKey pairs.
        # 
        # *   If you specify a subnet mask, RAM users can use only the IP addresses in the subnet mask to log on to the Alibaba Cloud Management Console.
        # *   If you do not specify a subnet mask, RAM users can use all IP addresses to log on to the Alibaba Cloud Management Console.
        # 
        # If you need to specify multiple subnet masks, separate the subnet masks with semicolons (;). Example: 192.168.0.0/16;10.0.0.0/8.
        # 
        # You can specify up to 25 subnet masks. The total length of the subnet masks can be a maximum of 512 characters.
        self.login_network_masks = login_network_masks  # type: str
        # The validity period of the logon session of RAM users.
        # 
        # Valid values: 1 to 24. Unit: hours.
        # 
        # Default value: 6.
        self.login_session_duration = login_session_duration  # type: int
        # Specifies whether MFA is required for all RAM users when they log on to the Alibaba Cloud Management Console. This parameter is used to replace the EnforceMFAForLogin parameter. The EnforceMFAForLogin parameter is still valid. However, we recommend that you use the MFAOperationForLogin parameter. Valid values:
        # 
        # *   mandatory: MFA is required for all RAM users. If you use the EnforceMFAForLogin parameter, set the value to true.
        # *   independent: User-specific settings are applied. This is the default value. If you use the EnforceMFAForLogin parameter, set the value to false.
        # *   adaptive: MFA is required only for RAM users who initiated unusual logons.
        self.mfaoperation_for_login = mfaoperation_for_login  # type: str
        # Specifies whether to enable MFA for RAM users who initiated unusual logons. Valid values:
        # 
        # *   autonomous: yes. MFA is prompted for RAM users who initiated unusual logons. However, the RAM users are allowed to skip MFA. This is the default value.
        # *   enforceVerify: no.
        self.operation_for_risk_login = operation_for_risk_login  # type: str
        self.verification_types_shrink = verification_types_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSecurityPreferenceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        if self.allow_user_to_manage_personal_ding_talk is not None:
            result['AllowUserToManagePersonalDingTalk'] = self.allow_user_to_manage_personal_ding_talk
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.mfaoperation_for_login is not None:
            result['MFAOperationForLogin'] = self.mfaoperation_for_login
        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login
        if self.verification_types_shrink is not None:
            result['VerificationTypes'] = self.verification_types_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        if m.get('AllowUserToManagePersonalDingTalk') is not None:
            self.allow_user_to_manage_personal_ding_talk = m.get('AllowUserToManagePersonalDingTalk')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('MFAOperationForLogin') is not None:
            self.mfaoperation_for_login = m.get('MFAOperationForLogin')
        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')
        if m.get('VerificationTypes') is not None:
            self.verification_types_shrink = m.get('VerificationTypes')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(self, allow_user_to_manage_access_keys=None):
        # Indicates whether RAM users can manage their AccessKey pairs.
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_access_keys is not None:
            result['AllowUserToManageAccessKeys'] = self.allow_user_to_manage_access_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToManageAccessKeys') is not None:
            self.allow_user_to_manage_access_keys = m.get('AllowUserToManageAccessKeys')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference(TeaModel):
    def __init__(self, allow_user_to_change_password=None, enable_save_mfaticket=None, login_network_masks=None,
                 login_session_duration=None, mfaoperation_for_login=None, operation_for_risk_login=None):
        # Indicates whether RAM users can change their passwords.
        self.allow_user_to_change_password = allow_user_to_change_password  # type: bool
        # Indicates whether RAM users can remember the MFA devices for seven days.
        self.enable_save_mfaticket = enable_save_mfaticket  # type: bool
        # The subnet mask.
        self.login_network_masks = login_network_masks  # type: str
        # The validity period of the logon session of RAM users.
        self.login_session_duration = login_session_duration  # type: int
        # Indicates whether MFA is required for all RAM users when they log on to the Alibaba Cloud Management Console.
        self.mfaoperation_for_login = mfaoperation_for_login  # type: str
        # Indicates whether to enable MFA for RAM users who initiated unusual logons.
        self.operation_for_risk_login = operation_for_risk_login  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_change_password is not None:
            result['AllowUserToChangePassword'] = self.allow_user_to_change_password
        if self.enable_save_mfaticket is not None:
            result['EnableSaveMFATicket'] = self.enable_save_mfaticket
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        if self.mfaoperation_for_login is not None:
            result['MFAOperationForLogin'] = self.mfaoperation_for_login
        if self.operation_for_risk_login is not None:
            result['OperationForRiskLogin'] = self.operation_for_risk_login
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        if m.get('MFAOperationForLogin') is not None:
            self.mfaoperation_for_login = m.get('MFAOperationForLogin')
        if m.get('OperationForRiskLogin') is not None:
            self.operation_for_risk_login = m.get('OperationForRiskLogin')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(TeaModel):
    def __init__(self, allow_user_to_manage_mfadevices=None):
        # Indicates whether RAM users can manage their MFA devices.
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_mfadevices is not None:
            result['AllowUserToManageMFADevices'] = self.allow_user_to_manage_mfadevices
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToManageMFADevices') is not None:
            self.allow_user_to_manage_mfadevices = m.get('AllowUserToManageMFADevices')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference(TeaModel):
    def __init__(self, allow_user_to_manage_personal_ding_talk=None):
        # Indicates whether RAM users can manage their personal DingTalk accounts, such as binding and unbinding of the accounts.
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_user_to_manage_personal_ding_talk is not None:
            result['AllowUserToManagePersonalDingTalk'] = self.allow_user_to_manage_personal_ding_talk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToManagePersonalDingTalk') is not None:
            self.allow_user_to_manage_personal_ding_talk = m.get('AllowUserToManagePersonalDingTalk')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference(TeaModel):
    def __init__(self, verification_types=None):
        self.verification_types = verification_types  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verification_types is not None:
            result['VerificationTypes'] = self.verification_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VerificationTypes') is not None:
            self.verification_types = m.get('VerificationTypes')
        return self


class SetSecurityPreferenceResponseBodySecurityPreference(TeaModel):
    def __init__(self, access_key_preference=None, login_profile_preference=None, mfapreference=None,
                 personal_info_preference=None, verification_preference=None):
        # The AccessKey pair preference.
        self.access_key_preference = access_key_preference  # type: SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference
        # The logon preference.
        self.login_profile_preference = login_profile_preference  # type: SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference
        # The MFA preference.
        self.mfapreference = mfapreference  # type: SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference
        # The personal information preference.
        self.personal_info_preference = personal_info_preference  # type: SetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference
        self.verification_preference = verification_preference  # type: SetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()
        if self.personal_info_preference:
            self.personal_info_preference.validate()
        if self.verification_preference:
            self.verification_preference.validate()

    def to_map(self):
        _map = super(SetSecurityPreferenceResponseBodySecurityPreference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_preference is not None:
            result['AccessKeyPreference'] = self.access_key_preference.to_map()
        if self.login_profile_preference is not None:
            result['LoginProfilePreference'] = self.login_profile_preference.to_map()
        if self.mfapreference is not None:
            result['MFAPreference'] = self.mfapreference.to_map()
        if self.personal_info_preference is not None:
            result['PersonalInfoPreference'] = self.personal_info_preference.to_map()
        if self.verification_preference is not None:
            result['VerificationPreference'] = self.verification_preference.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference()
            self.access_key_preference = temp_model.from_map(m['AccessKeyPreference'])
        if m.get('LoginProfilePreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference()
            self.login_profile_preference = temp_model.from_map(m['LoginProfilePreference'])
        if m.get('MFAPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference()
            self.mfapreference = temp_model.from_map(m['MFAPreference'])
        if m.get('PersonalInfoPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference()
            self.personal_info_preference = temp_model.from_map(m['PersonalInfoPreference'])
        if m.get('VerificationPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreferenceVerificationPreference()
            self.verification_preference = temp_model.from_map(m['VerificationPreference'])
        return self


class SetSecurityPreferenceResponseBody(TeaModel):
    def __init__(self, request_id=None, security_preference=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of security preferences.
        self.security_preference = security_preference  # type: SetSecurityPreferenceResponseBodySecurityPreference

    def validate(self):
        if self.security_preference:
            self.security_preference.validate()

    def to_map(self):
        _map = super(SetSecurityPreferenceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_preference is not None:
            result['SecurityPreference'] = self.security_preference.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPreference') is not None:
            temp_model = SetSecurityPreferenceResponseBodySecurityPreference()
            self.security_preference = temp_model.from_map(m['SecurityPreference'])
        return self


class SetSecurityPreferenceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetSecurityPreferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetSecurityPreferenceResponse, self).to_map()
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
            temp_model = SetSecurityPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserSsoSettingsRequest(TeaModel):
    def __init__(self, auxiliary_domain=None, metadata_document=None, sso_enabled=None):
        # The auxiliary domain name.
        self.auxiliary_domain = auxiliary_domain  # type: str
        # The metadata file, which is Base64-encoded.
        # 
        # The file is provided by an IdP that supports SAML 2.0.
        self.metadata_document = metadata_document  # type: str
        # Specifies whether to enable SSO for the RAM user. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.sso_enabled = sso_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserSsoSettingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        return self


class SetUserSsoSettingsResponseBodyUserSsoSettings(TeaModel):
    def __init__(self, auxiliary_domain=None, metadata_document=None, sso_enabled=None):
        # The auxiliary domain name.
        self.auxiliary_domain = auxiliary_domain  # type: str
        # The metadata file, which is Base64-encoded.
        self.metadata_document = metadata_document  # type: str
        # Indicates whether user-based SSO is enabled.
        self.sso_enabled = sso_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserSsoSettingsResponseBodyUserSsoSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auxiliary_domain is not None:
            result['AuxiliaryDomain'] = self.auxiliary_domain
        if self.metadata_document is not None:
            result['MetadataDocument'] = self.metadata_document
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('AuxiliaryDomain')
        if m.get('MetadataDocument') is not None:
            self.metadata_document = m.get('MetadataDocument')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        return self


class SetUserSsoSettingsResponseBody(TeaModel):
    def __init__(self, request_id=None, user_sso_settings=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The configurations of user-based SSO.
        self.user_sso_settings = user_sso_settings  # type: SetUserSsoSettingsResponseBodyUserSsoSettings

    def validate(self):
        if self.user_sso_settings:
            self.user_sso_settings.validate()

    def to_map(self):
        _map = super(SetUserSsoSettingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_sso_settings is not None:
            result['UserSsoSettings'] = self.user_sso_settings.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserSsoSettings') is not None:
            temp_model = SetUserSsoSettingsResponseBodyUserSsoSettings()
            self.user_sso_settings = temp_model.from_map(m['UserSsoSettings'])
        return self


class SetUserSsoSettingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetUserSsoSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetUserSsoSettingsResponse, self).to_map()
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
            temp_model = SetUserSsoSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20. You cannot specify empty strings as tag keys. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key  # type: str
        # The value of tag N.
        # 
        # Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be a up to128 characters in length and cannot contain `http://` or `https://`.
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
    def __init__(self, resource_id=None, resource_principal_name=None, resource_type=None, tag=None):
        self.resource_id = resource_id  # type: list[str]
        self.resource_principal_name = resource_principal_name  # type: list[str]
        # The type of the resource. Valid value:
        # 
        # *   user: a RAM user
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
        if self.resource_principal_name is not None:
            result['ResourcePrincipalName'] = self.resource_principal_name
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
        if m.get('ResourcePrincipalName') is not None:
            self.resource_principal_name = m.get('ResourcePrincipalName')
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
        # The ID of the request.
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


class UnbindMFADeviceRequest(TeaModel):
    def __init__(self, user_principal_name=None):
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindMFADeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UnbindMFADeviceResponseBodyMFADevice(TeaModel):
    def __init__(self, serial_number=None):
        # The serial number of the MFA device.
        self.serial_number = serial_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindMFADeviceResponseBodyMFADevice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class UnbindMFADeviceResponseBody(TeaModel):
    def __init__(self, mfadevice=None, request_id=None):
        # The information of the MFA device.
        self.mfadevice = mfadevice  # type: UnbindMFADeviceResponseBodyMFADevice
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        _map = super(UnbindMFADeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MFADevice') is not None:
            temp_model = UnbindMFADeviceResponseBodyMFADevice()
            self.mfadevice = temp_model.from_map(m['MFADevice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindMFADeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindMFADeviceResponse, self).to_map()
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
            temp_model = UnbindMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, resource_id=None, resource_principal_name=None, resource_type=None, tag_key=None):
        # Specifies whether to remove all tags from the resources. Valid values:
        # 
        # *   true: remove all tags from the resources.
        # *   false: does not remove all tags from the resources. This is the default value.
        # 
        # >  This parameter takes effect only when the TagKey.N parameter is not specified in the request.
        self.all = all  # type: bool
        self.resource_id = resource_id  # type: list[str]
        self.resource_principal_name = resource_principal_name  # type: list[str]
        # The type of the resource. Valid values:
        # 
        # *   user: a RAM user
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
        if self.resource_principal_name is not None:
            result['ResourcePrincipalName'] = self.resource_principal_name
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
        if m.get('ResourcePrincipalName') is not None:
            self.resource_principal_name = m.get('ResourcePrincipalName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class UpdateAccessKeyRequest(TeaModel):
    def __init__(self, status=None, user_access_key_id=None, user_principal_name=None):
        # The status of the AccessKey pair. Valid values:
        # 
        # *   Active
        # *   Inactive
        self.status = status  # type: str
        # The AccessKey ID of the AccessKey pair for which you want to modify the status.
        self.user_access_key_id = user_access_key_id  # type: str
        # The logon name of the RAM user.
        # 
        # If this parameter is empty, the status of the AccessKey pair for the current user is modified.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAccessKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateAccessKeyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAccessKeyResponseBody, self).to_map()
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


class UpdateAccessKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAccessKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAccessKeyResponse, self).to_map()
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
            temp_model = UpdateAccessKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationRequest(TeaModel):
    def __init__(self, app_id=None, new_access_token_validity=None, new_display_name=None,
                 new_is_multi_tenant=None, new_predefined_scopes=None, new_redirect_uris=None, new_refresh_token_validity=None,
                 new_secret_required=None):
        self.app_id = app_id  # type: str
        self.new_access_token_validity = new_access_token_validity  # type: int
        self.new_display_name = new_display_name  # type: str
        self.new_is_multi_tenant = new_is_multi_tenant  # type: bool
        self.new_predefined_scopes = new_predefined_scopes  # type: str
        self.new_redirect_uris = new_redirect_uris  # type: str
        self.new_refresh_token_validity = new_refresh_token_validity  # type: int
        self.new_secret_required = new_secret_required  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.new_access_token_validity is not None:
            result['NewAccessTokenValidity'] = self.new_access_token_validity
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_is_multi_tenant is not None:
            result['NewIsMultiTenant'] = self.new_is_multi_tenant
        if self.new_predefined_scopes is not None:
            result['NewPredefinedScopes'] = self.new_predefined_scopes
        if self.new_redirect_uris is not None:
            result['NewRedirectUris'] = self.new_redirect_uris
        if self.new_refresh_token_validity is not None:
            result['NewRefreshTokenValidity'] = self.new_refresh_token_validity
        if self.new_secret_required is not None:
            result['NewSecretRequired'] = self.new_secret_required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('NewAccessTokenValidity') is not None:
            self.new_access_token_validity = m.get('NewAccessTokenValidity')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewIsMultiTenant') is not None:
            self.new_is_multi_tenant = m.get('NewIsMultiTenant')
        if m.get('NewPredefinedScopes') is not None:
            self.new_predefined_scopes = m.get('NewPredefinedScopes')
        if m.get('NewRedirectUris') is not None:
            self.new_redirect_uris = m.get('NewRedirectUris')
        if m.get('NewRefreshTokenValidity') is not None:
            self.new_refresh_token_validity = m.get('NewRefreshTokenValidity')
        if m.get('NewSecretRequired') is not None:
            self.new_secret_required = m.get('NewSecretRequired')
        return self


class UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope(TeaModel):
    def __init__(self, description=None, name=None):
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope, self).to_map()
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


class UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes(TeaModel):
    def __init__(self, predefined_scope=None):
        self.predefined_scope = predefined_scope  # type: list[UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope]

    def validate(self):
        if self.predefined_scope:
            for k in self.predefined_scope:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k in self.predefined_scope:
                result['PredefinedScope'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k in m.get('PredefinedScope'):
                temp_model = UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k))
        return self


class UpdateApplicationResponseBodyApplicationDelegatedScope(TeaModel):
    def __init__(self, predefined_scopes=None):
        self.predefined_scopes = predefined_scopes  # type: UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        _map = super(UpdateApplicationResponseBodyApplicationDelegatedScope, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = UpdateApplicationResponseBodyApplicationDelegatedScopePredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m['PredefinedScopes'])
        return self


class UpdateApplicationResponseBodyApplicationRedirectUris(TeaModel):
    def __init__(self, redirect_uri=None):
        self.redirect_uri = redirect_uri  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationResponseBodyApplicationRedirectUris, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        return self


class UpdateApplicationResponseBodyApplication(TeaModel):
    def __init__(self, access_token_validity=None, account_id=None, app_id=None, app_name=None, app_type=None,
                 create_date=None, delegated_scope=None, display_name=None, is_multi_tenant=None, redirect_uris=None,
                 refresh_token_validity=None, secret_required=None, update_date=None):
        self.access_token_validity = access_token_validity  # type: int
        self.account_id = account_id  # type: str
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.create_date = create_date  # type: str
        self.delegated_scope = delegated_scope  # type: UpdateApplicationResponseBodyApplicationDelegatedScope
        self.display_name = display_name  # type: str
        self.is_multi_tenant = is_multi_tenant  # type: bool
        self.redirect_uris = redirect_uris  # type: UpdateApplicationResponseBodyApplicationRedirectUris
        self.refresh_token_validity = refresh_token_validity  # type: int
        self.secret_required = secret_required  # type: bool
        self.update_date = update_date  # type: str

    def validate(self):
        if self.delegated_scope:
            self.delegated_scope.validate()
        if self.redirect_uris:
            self.redirect_uris.validate()

    def to_map(self):
        _map = super(UpdateApplicationResponseBodyApplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_validity is not None:
            result['AccessTokenValidity'] = self.access_token_validity
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.delegated_scope is not None:
            result['DelegatedScope'] = self.delegated_scope.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.is_multi_tenant is not None:
            result['IsMultiTenant'] = self.is_multi_tenant
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris.to_map()
        if self.refresh_token_validity is not None:
            result['RefreshTokenValidity'] = self.refresh_token_validity
        if self.secret_required is not None:
            result['SecretRequired'] = self.secret_required
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenValidity') is not None:
            self.access_token_validity = m.get('AccessTokenValidity')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DelegatedScope') is not None:
            temp_model = UpdateApplicationResponseBodyApplicationDelegatedScope()
            self.delegated_scope = temp_model.from_map(m['DelegatedScope'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('IsMultiTenant') is not None:
            self.is_multi_tenant = m.get('IsMultiTenant')
        if m.get('RedirectUris') is not None:
            temp_model = UpdateApplicationResponseBodyApplicationRedirectUris()
            self.redirect_uris = temp_model.from_map(m['RedirectUris'])
        if m.get('RefreshTokenValidity') is not None:
            self.refresh_token_validity = m.get('RefreshTokenValidity')
        if m.get('SecretRequired') is not None:
            self.secret_required = m.get('SecretRequired')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateApplicationResponseBody(TeaModel):
    def __init__(self, application=None, request_id=None):
        self.application = application  # type: UpdateApplicationResponseBodyApplication
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super(UpdateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = UpdateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationResponse, self).to_map()
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
            temp_model = UpdateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(self, group_name=None, new_comments=None, new_display_name=None, new_group_name=None):
        # The name of the RAM user group.
        self.group_name = group_name  # type: str
        # The new description.
        # 
        # The value can be up to 128 characters in length.
        self.new_comments = new_comments  # type: str
        # The new display name of the RAM user group.
        # 
        # The name can be up to 24 characters in length.
        self.new_display_name = new_display_name  # type: str
        # The new name of the RAM user group.
        # 
        # The name can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        self.new_group_name = new_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_group_name is not None:
            result['NewGroupName'] = self.new_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewGroupName') is not None:
            self.new_group_name = m.get('NewGroupName')
        return self


class UpdateGroupResponseBodyGroup(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, group_id=None, group_name=None,
                 update_date=None):
        # The description.
        self.comments = comments  # type: str
        # The creation time.
        self.create_date = create_date  # type: str
        # The display name of the RAM user group.
        self.display_name = display_name  # type: str
        # The ID of the RAM user group.
        self.group_id = group_id  # type: str
        # The name of the RAM user group.
        self.group_name = group_name  # type: str
        # The update time.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupResponseBodyGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateGroupResponseBody(TeaModel):
    def __init__(self, group=None, request_id=None):
        # The information of the RAM user group.
        self.group = group  # type: UpdateGroupResponseBodyGroup
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super(UpdateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = UpdateGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupResponse, self).to_map()
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
            temp_model = UpdateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoginProfileRequest(TeaModel):
    def __init__(self, mfabind_required=None, password=None, password_reset_required=None, status=None,
                 user_principal_name=None):
        # Specifies whether multi-factor authentication (MFA) must be enabled. Valid values:
        # 
        # *   true. The value true indicates that the RAM user must bind an MFA device at the next logon.
        # *   false.
        self.mfabind_required = mfabind_required  # type: bool
        # The new password that is used to log on to the console.
        # 
        # The password must meet the complexity requirements.
        self.password = password  # type: str
        # Specifies whether the RAM user must reset the password at the next logon. Valid values:
        # 
        # *   true
        # *   false
        self.password_reset_required = password_reset_required  # type: bool
        # The status of password-based logon. Valid values:
        # 
        # *   Active
        # *   Inactive
        self.status = status  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoginProfileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.password is not None:
            result['Password'] = self.password
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.status is not None:
            result['Status'] = self.status
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateLoginProfileResponseBodyLoginProfile(TeaModel):
    def __init__(self, mfabind_required=None, password_reset_required=None, status=None, update_date=None,
                 user_principal_name=None):
        # Indicates whether MFA must be enabled.
        self.mfabind_required = mfabind_required  # type: bool
        # Indicates whether the RAM user must reset the password at the next logon.
        self.password_reset_required = password_reset_required  # type: bool
        # The status of password-based logon.
        self.status = status  # type: str
        # The update time.
        self.update_date = update_date  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoginProfileResponseBodyLoginProfile, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfabind_required is not None:
            result['MFABindRequired'] = self.mfabind_required
        if self.password_reset_required is not None:
            result['PasswordResetRequired'] = self.password_reset_required
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MFABindRequired') is not None:
            self.mfabind_required = m.get('MFABindRequired')
        if m.get('PasswordResetRequired') is not None:
            self.password_reset_required = m.get('PasswordResetRequired')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateLoginProfileResponseBody(TeaModel):
    def __init__(self, login_profile=None, request_id=None):
        # The logon information.
        self.login_profile = login_profile  # type: UpdateLoginProfileResponseBodyLoginProfile
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.login_profile:
            self.login_profile.validate()

    def to_map(self):
        _map = super(UpdateLoginProfileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_profile is not None:
            result['LoginProfile'] = self.login_profile.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginProfile') is not None:
            temp_model = UpdateLoginProfileResponseBodyLoginProfile()
            self.login_profile = temp_model.from_map(m['LoginProfile'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoginProfileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLoginProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLoginProfileResponse, self).to_map()
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
            temp_model = UpdateLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOIDCProviderRequest(TeaModel):
    def __init__(self, client_ids=None, new_description=None, oidcprovider_name=None):
        # The ID of the client. If you want to specify multiple fingerprints, separate the fingerprints with commas (,).
        # 
        # The client ID can contain letters, digits, and special characters and cannot start with the special characters. The special characters are `periods, (.), hyphens (-), underscores (_), colons (:), and forward slashes (/)`.
        # 
        # The client ID can be up to 64 characters in length.
        # 
        # >  If you specify this parameter, all the client IDs of the OIDC IdP are replaced. If you need to only add or remove a client ID, call the AddClientIdToOIDCProvider or RemoveClientIdFromOIDCProvider operation. For more information, see [AddClientIdToOIDCProvider](~~332057~~) or [RemoveClientIdFromOIDCProvider](~~332058~~).
        self.client_ids = client_ids  # type: str
        # The description of the OIDC IdP.
        # 
        # The description can be up to 256 characters in length.
        self.new_description = new_description  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOIDCProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        return self


class UpdateOIDCProviderResponseBodyOIDCProvider(TeaModel):
    def __init__(self, arn=None, client_ids=None, create_date=None, description=None, fingerprints=None,
                 gmt_create=None, gmt_modified=None, issuer_url=None, oidcprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the OIDC IdP.
        self.arn = arn  # type: str
        # The ID of the client. If multiple client IDs are returned, the client IDs are separated by commas (,).
        self.client_ids = client_ids  # type: str
        # The time when the OIDC IdP was created. The time is displayed in UTC.
        self.create_date = create_date  # type: str
        # The description of the OIDC IdP.
        self.description = description  # type: str
        # The fingerprint of the HTTPS certificate. If multiple fingerprints are returned, the fingerprints are separated by commas (,).
        self.fingerprints = fingerprints  # type: str
        # The timestamp when the OIDC IdP was created.
        self.gmt_create = gmt_create  # type: str
        # The timestamp when the OIDC IdP was modified.
        self.gmt_modified = gmt_modified  # type: str
        # The URL of the issuer.
        self.issuer_url = issuer_url  # type: str
        # The name of the OIDC IdP.
        self.oidcprovider_name = oidcprovider_name  # type: str
        # The time when the OIDC IdP was modified. The time is displayed in UTC.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOIDCProviderResponseBodyOIDCProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url
        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')
        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateOIDCProviderResponseBody(TeaModel):
    def __init__(self, oidcprovider=None, request_id=None):
        # The information about the OIDC IdP.
        self.oidcprovider = oidcprovider  # type: UpdateOIDCProviderResponseBodyOIDCProvider
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oidcprovider:
            self.oidcprovider.validate()

    def to_map(self):
        _map = super(UpdateOIDCProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider is not None:
            result['OIDCProvider'] = self.oidcprovider.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OIDCProvider') is not None:
            temp_model = UpdateOIDCProviderResponseBodyOIDCProvider()
            self.oidcprovider = temp_model.from_map(m['OIDCProvider'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOIDCProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateOIDCProviderResponse, self).to_map()
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
            temp_model = UpdateOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSAMLProviderRequest(TeaModel):
    def __init__(self, new_description=None, new_encoded_samlmetadata_document=None, samlprovider_name=None):
        # The new description.
        # 
        # >  You must specify at least one of the `NewDescription` and `NewEncodedSAMLMetadataDocument` parameters.
        self.new_description = new_description  # type: str
        # The new metadata file.
        # 
        # >  You must specify at least one of the `NewDescription` and `NewEncodedSAMLMetadataDocument` parameters.
        self.new_encoded_samlmetadata_document = new_encoded_samlmetadata_document  # type: str
        # The name of the IdP whose information you want to modify.
        self.samlprovider_name = samlprovider_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSAMLProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_description is not None:
            result['NewDescription'] = self.new_description
        if self.new_encoded_samlmetadata_document is not None:
            result['NewEncodedSAMLMetadataDocument'] = self.new_encoded_samlmetadata_document
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')
        if m.get('NewEncodedSAMLMetadataDocument') is not None:
            self.new_encoded_samlmetadata_document = m.get('NewEncodedSAMLMetadataDocument')
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        return self


class UpdateSAMLProviderResponseBodySAMLProvider(TeaModel):
    def __init__(self, arn=None, create_date=None, description=None, samlprovider_name=None, update_date=None):
        # The Alibaba Cloud Resource Name (ARN) of the IdP.
        self.arn = arn  # type: str
        # The point in time at which the IdP was created. The time is displayed in UTC.
        self.create_date = create_date  # type: str
        # The description of the IdP.
        self.description = description  # type: str
        # The name of the IdP.
        self.samlprovider_name = samlprovider_name  # type: str
        # The point in time at which the information about the IdP was modified. The time is displayed in UTC.
        self.update_date = update_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSAMLProviderResponseBodySAMLProvider, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name
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
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateSAMLProviderResponseBody(TeaModel):
    def __init__(self, request_id=None, samlprovider=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the IdP.
        self.samlprovider = samlprovider  # type: UpdateSAMLProviderResponseBodySAMLProvider

    def validate(self):
        if self.samlprovider:
            self.samlprovider.validate()

    def to_map(self):
        _map = super(UpdateSAMLProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlprovider is not None:
            result['SAMLProvider'] = self.samlprovider.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLProvider') is not None:
            temp_model = UpdateSAMLProviderResponseBodySAMLProvider()
            self.samlprovider = temp_model.from_map(m['SAMLProvider'])
        return self


class UpdateSAMLProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSAMLProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSAMLProviderResponse, self).to_map()
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
            temp_model = UpdateSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(self, new_comments=None, new_display_name=None, new_email=None, new_mobile_phone=None,
                 new_user_principal_name=None, user_id=None, user_principal_name=None):
        # The new description of the RAM user.
        # 
        # The description must be 1 to 128 characters in length.
        self.new_comments = new_comments  # type: str
        # The new display name of the RAM user.
        # 
        # The name must be 1 to 24 characters in length.
        self.new_display_name = new_display_name  # type: str
        # The new email address of the RAM user.
        # 
        # >  This parameter applies only to the China site (aliyun.com).
        self.new_email = new_email  # type: str
        # The new mobile phone number of the RAM user.
        # 
        # Format: Country calling code-Mobile phone number.
        # 
        # >  This parameter applies only to the China site (aliyun.com).
        self.new_mobile_phone = new_mobile_phone  # type: str
        # The new logon name of the RAM user.
        # 
        # The name is in the format of `<username>@<AccountAlias>.onaliyun.com`. `<username>` is the name of the RAM user. `<AccountAlias>.onaliyun.com` is the default domain name.
        # 
        # The value of `UserPrincipalName` must be 1 to 128 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (\_). The value of `<username>` must be 1 to 64 characters in length.
        self.new_user_principal_name = new_user_principal_name  # type: str
        # The ID of the RAM user.
        # 
        # >  You must specify only one of the following parameters: `UserPrincipalName` and `UserId`.
        self.user_id = user_id  # type: str
        # The logon name of the RAM user.
        # 
        # >  You must specify only one of the following parameters: `UserPrincipalName` and `UserId`.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_comments is not None:
            result['NewComments'] = self.new_comments
        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name
        if self.new_email is not None:
            result['NewEmail'] = self.new_email
        if self.new_mobile_phone is not None:
            result['NewMobilePhone'] = self.new_mobile_phone
        if self.new_user_principal_name is not None:
            result['NewUserPrincipalName'] = self.new_user_principal_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')
        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')
        if m.get('NewEmail') is not None:
            self.new_email = m.get('NewEmail')
        if m.get('NewMobilePhone') is not None:
            self.new_mobile_phone = m.get('NewMobilePhone')
        if m.get('NewUserPrincipalName') is not None:
            self.new_user_principal_name = m.get('NewUserPrincipalName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateUserResponseBodyUser(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, email=None, last_login_date=None,
                 mobile_phone=None, provision_type=None, update_date=None, user_id=None, user_principal_name=None):
        # The description of the RAM user.
        self.comments = comments  # type: str
        # The time when the RAM user was created.
        self.create_date = create_date  # type: str
        # The display name of the RAM user.
        self.display_name = display_name  # type: str
        # The email address of the RAM user.
        # 
        # >  This parameter applies only to the China site (aliyun.com).
        self.email = email  # type: str
        # The last time when the RAM user logged on to the console.
        self.last_login_date = last_login_date  # type: str
        # The mobile phone number of the RAM user.
        # 
        # >  This parameter applies only to the China site (aliyun.com).
        self.mobile_phone = mobile_phone  # type: str
        self.provision_type = provision_type  # type: str
        # The time when the information of the RAM user was updated.
        self.update_date = update_date  # type: str
        # The ID of the RAM user.
        self.user_id = user_id  # type: str
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserResponseBodyUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.last_login_date is not None:
            result['LastLoginDate'] = self.last_login_date
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLoginDate') is not None:
            self.last_login_date = m.get('LastLoginDate')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the RAM user.
        self.user = user  # type: UpdateUserResponseBodyUser

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super(UpdateUserResponseBody, self).to_map()
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
            temp_model = UpdateUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class UpdateUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserResponse, self).to_map()
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
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


