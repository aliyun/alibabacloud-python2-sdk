# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddClientIdToOIDCProviderRequest(TeaModel):
    def __init__(self, client_id=None, oidcprovider_name=None):
        self.client_id = client_id  # type: str
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
        self.arn = arn  # type: str
        self.client_ids = client_ids  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.fingerprints = fingerprints  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.issuer_url = issuer_url  # type: str
        self.oidcprovider_name = oidcprovider_name  # type: str
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
        self.oidcprovider = oidcprovider  # type: AddClientIdToOIDCProviderResponseBodyOIDCProvider
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddClientIdToOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddClientIdToOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFingerprintToOIDCProviderRequest(TeaModel):
    def __init__(self, fingerprint=None, oidcprovider_name=None):
        self.fingerprint = fingerprint  # type: str
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
        self.arn = arn  # type: str
        self.client_ids = client_ids  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.fingerprints = fingerprints  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.issuer_url = issuer_url  # type: str
        self.oidcprovider_name = oidcprovider_name  # type: str
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
        self.oidcprovider = oidcprovider  # type: AddFingerprintToOIDCProviderResponseBodyOIDCProvider
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddFingerprintToOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddFingerprintToOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToGroupRequest(TeaModel):
    def __init__(self, group_name=None, user_principal_name=None):
        self.group_name = group_name  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUserToGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindMFADeviceRequest(TeaModel):
    def __init__(self, authentication_code_1=None, authentication_code_2=None, serial_number=None,
                 user_principal_name=None):
        self.authentication_code_1 = authentication_code_1  # type: str
        self.authentication_code_2 = authentication_code_2  # type: str
        self.serial_number = serial_number  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BindMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangePasswordRequest(TeaModel):
    def __init__(self, new_password=None, old_password=None):
        self.new_password = new_password  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChangePasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChangePasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessKeyRequest(TeaModel):
    def __init__(self, user_principal_name=None):
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
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.create_date = create_date  # type: str
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
        self.access_key = access_key  # type: CreateAccessKeyResponseBodyAccessKey
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAccessKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAppSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(self, comments=None, display_name=None, group_name=None):
        self.comments = comments  # type: str
        self.display_name = display_name  # type: str
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
        self.comments = comments  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
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
        self.group = group  # type: CreateGroupResponseBodyGroup
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoginProfileRequest(TeaModel):
    def __init__(self, mfabind_required=None, password=None, password_reset_required=None, status=None,
                 user_principal_name=None):
        self.mfabind_required = mfabind_required  # type: bool
        self.password = password  # type: str
        self.password_reset_required = password_reset_required  # type: bool
        self.status = status  # type: str
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
        self.mfabind_required = mfabind_required  # type: bool
        self.password_reset_required = password_reset_required  # type: bool
        self.status = status  # type: str
        self.update_date = update_date  # type: str
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
        self.login_profile = login_profile  # type: CreateLoginProfileResponseBodyLoginProfile
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateLoginProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOIDCProviderRequest(TeaModel):
    def __init__(self, client_ids=None, description=None, fingerprints=None, issuer_url=None,
                 oidcprovider_name=None):
        self.client_ids = client_ids  # type: str
        self.description = description  # type: str
        self.fingerprints = fingerprints  # type: str
        self.issuer_url = issuer_url  # type: str
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
        self.arn = arn  # type: str
        self.client_ids = client_ids  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.fingerprints = fingerprints  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.issuer_url = issuer_url  # type: str
        self.oidcprovider_name = oidcprovider_name  # type: str
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
        self.oidcprovider = oidcprovider  # type: CreateOIDCProviderResponseBodyOIDCProvider
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSAMLProviderRequest(TeaModel):
    def __init__(self, description=None, encoded_samlmetadata_document=None, samlprovider_name=None):
        self.description = description  # type: str
        self.encoded_samlmetadata_document = encoded_samlmetadata_document  # type: str
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
        self.arn = arn  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.samlprovider_name = samlprovider_name  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSAMLProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(self, comments=None, display_name=None, email=None, mobile_phone=None, user_principal_name=None):
        self.comments = comments  # type: str
        self.display_name = display_name  # type: str
        self.email = email  # type: str
        self.mobile_phone = mobile_phone  # type: str
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

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
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateUserResponseBodyUser(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, email=None, last_login_date=None,
                 mobile_phone=None, update_date=None, user_id=None, user_principal_name=None):
        self.comments = comments  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.email = email  # type: str
        self.last_login_date = last_login_date  # type: str
        self.mobile_phone = mobile_phone  # type: str
        self.update_date = update_date  # type: str
        self.user_id = user_id  # type: str
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

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
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user=None):
        self.request_id = request_id  # type: str
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


class CreateVirtualMFADeviceRequest(TeaModel):
    def __init__(self, virtual_mfadevice_name=None):
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
        self.base_32string_seed = base_32string_seed  # type: str
        self.qrcode_png = qrcode_png  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateVirtualMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessKeyRequest(TeaModel):
    def __init__(self, user_access_key_id=None, user_principal_name=None):
        self.user_access_key_id = user_access_key_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAccessKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAppSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(self, group_name=None):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoginProfileRequest(TeaModel):
    def __init__(self, user_principal_name=None):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteLoginProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOIDCProviderRequest(TeaModel):
    def __init__(self, oidcprovider_name=None):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSAMLProviderRequest(TeaModel):
    def __init__(self, samlprovider_name=None):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSAMLProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, user_id=None, user_principal_name=None):
        self.user_id = user_id  # type: str
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


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(self, serial_number=None):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteVirtualMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableVirtualMFARequest(TeaModel):
    def __init__(self, user_principal_name=None):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableVirtualMFAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableVirtualMFAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCredentialReportResponseBody(TeaModel):
    def __init__(self, request_id=None, state=None):
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateCredentialReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateCredentialReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessKeyLastUsedRequest(TeaModel):
    def __init__(self, user_access_key_id=None, user_principal_name=None):
        self.user_access_key_id = user_access_key_id  # type: str
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
    def __init__(self, last_used_date=None):
        self.last_used_date = last_used_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_used_date is not None:
            result['LastUsedDate'] = self.last_used_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastUsedDate') is not None:
            self.last_used_date = m.get('LastUsedDate')
        return self


class GetAccessKeyLastUsedResponseBody(TeaModel):
    def __init__(self, access_key_last_used=None, request_id=None):
        self.access_key_last_used = access_key_last_used  # type: GetAccessKeyLastUsedResponseBodyAccessKeyLastUsed
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAccessKeyLastUsedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAccessKeyLastUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountMFAInfoResponseBody(TeaModel):
    def __init__(self, is_mfaenable=None, request_id=None):
        self.is_mfaenable = is_mfaenable  # type: bool
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAccountMFAInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAccountMFAInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo(TeaModel):
    def __init__(self, bind_mfa=None, old_ak_num=None, root_with_access_key=None, sub_user=None,
                 sub_user_bind_mfa=None, sub_user_pwd_level=None, sub_user_with_old_access_key=None,
                 sub_user_with_unused_access_key=None, unused_ak_num=None):
        self.bind_mfa = bind_mfa  # type: bool
        self.old_ak_num = old_ak_num  # type: int
        self.root_with_access_key = root_with_access_key  # type: int
        self.sub_user = sub_user  # type: int
        self.sub_user_bind_mfa = sub_user_bind_mfa  # type: int
        self.sub_user_pwd_level = sub_user_pwd_level  # type: str
        self.sub_user_with_old_access_key = sub_user_with_old_access_key  # type: int
        self.sub_user_with_unused_access_key = sub_user_with_unused_access_key  # type: int
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
        self.account_security_practice_user_info = account_security_practice_user_info  # type: GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfoAccountSecurityPracticeUserInfo
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
        self.account_security_practice_info = account_security_practice_info  # type: GetAccountSecurityPracticeReportResponseBodyAccountSecurityPracticeInfo
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAccountSecurityPracticeReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.access_keys_per_user_quota = access_keys_per_user_quota  # type: int
        self.attached_policies_per_group_quota = attached_policies_per_group_quota  # type: int
        self.attached_policies_per_role_quota = attached_policies_per_role_quota  # type: int
        self.attached_policies_per_user_quota = attached_policies_per_user_quota  # type: int
        self.attached_system_policies_per_group_quota = attached_system_policies_per_group_quota  # type: int
        self.attached_system_policies_per_role_quota = attached_system_policies_per_role_quota  # type: int
        self.attached_system_policies_per_user_quota = attached_system_policies_per_user_quota  # type: int
        self.groups = groups  # type: int
        self.groups_per_user_quota = groups_per_user_quota  # type: int
        self.groups_quota = groups_quota  # type: int
        self.mfadevices = mfadevices  # type: int
        self.mfadevices_in_use = mfadevices_in_use  # type: int
        self.policies = policies  # type: int
        self.policies_quota = policies_quota  # type: int
        self.policy_size_quota = policy_size_quota  # type: int
        self.roles = roles  # type: int
        self.roles_quota = roles_quota  # type: int
        self.users = users  # type: int
        self.users_quota = users_quota  # type: int
        self.versions_per_policy_quota = versions_per_policy_quota  # type: int
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAccountSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAppSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCredentialReportResponseBody(TeaModel):
    def __init__(self, content=None, generated_time=None, request_id=None):
        self.content = content  # type: str
        self.generated_time = generated_time  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCredentialReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCredentialReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultDomainResponseBody(TeaModel):
    def __init__(self, default_domain_name=None, request_id=None):
        self.default_domain_name = default_domain_name  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDefaultDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDefaultDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(self, group_name=None):
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
        self.comments = comments  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
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
        self.group = group  # type: GetGroupResponseBodyGroup
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginProfileRequest(TeaModel):
    def __init__(self, user_principal_name=None):
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
        self.last_login_time = last_login_time  # type: str
        self.mfabind_required = mfabind_required  # type: bool
        self.password_reset_required = password_reset_required  # type: bool
        self.status = status  # type: str
        self.update_date = update_date  # type: str
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
        self.login_profile = login_profile  # type: GetLoginProfileResponseBodyLoginProfile
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLoginProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOIDCProviderRequest(TeaModel):
    def __init__(self, oidcprovider_name=None):
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
        self.arn = arn  # type: str
        self.client_ids = client_ids  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.fingerprints = fingerprints  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.issuer_url = issuer_url  # type: str
        self.oidcprovider_name = oidcprovider_name  # type: str
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
        self.oidcprovider = oidcprovider  # type: GetOIDCProviderResponseBodyOIDCProvider
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPasswordPolicyResponseBodyPasswordPolicy(TeaModel):
    def __init__(self, hard_expire=None, max_login_attemps=None, max_password_age=None,
                 minimum_password_different_character=None, minimum_password_length=None, password_not_contain_user_name=None,
                 password_reuse_prevention=None, require_lowercase_characters=None, require_numbers=None, require_symbols=None,
                 require_uppercase_characters=None):
        self.hard_expire = hard_expire  # type: bool
        self.max_login_attemps = max_login_attemps  # type: int
        self.max_password_age = max_password_age  # type: int
        self.minimum_password_different_character = minimum_password_different_character  # type: int
        self.minimum_password_length = minimum_password_length  # type: int
        self.password_not_contain_user_name = password_not_contain_user_name  # type: bool
        self.password_reuse_prevention = password_reuse_prevention  # type: int
        self.require_lowercase_characters = require_lowercase_characters  # type: bool
        self.require_numbers = require_numbers  # type: bool
        self.require_symbols = require_symbols  # type: bool
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
        self.password_policy = password_policy  # type: GetPasswordPolicyResponseBodyPasswordPolicy
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPasswordPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSAMLProviderRequest(TeaModel):
    def __init__(self, samlprovider_name=None):
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
        self.arn = arn  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.encoded_samlmetadata_document = encoded_samlmetadata_document  # type: str
        self.samlprovider_name = samlprovider_name  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSAMLProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(self, allow_user_to_manage_access_keys=None):
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
    def __init__(self, allow_user_to_change_password=None, enable_save_mfaticket=None, enforce_mfafor_login=None,
                 login_network_masks=None, login_session_duration=None):
        self.allow_user_to_change_password = allow_user_to_change_password  # type: bool
        self.enable_save_mfaticket = enable_save_mfaticket  # type: bool
        self.enforce_mfafor_login = enforce_mfafor_login  # type: bool
        self.login_network_masks = login_network_masks  # type: str
        self.login_session_duration = login_session_duration  # type: int

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
        if self.enforce_mfafor_login is not None:
            result['EnforceMFAForLogin'] = self.enforce_mfafor_login
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('EnforceMFAForLogin') is not None:
            self.enforce_mfafor_login = m.get('EnforceMFAForLogin')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        return self


class GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(TeaModel):
    def __init__(self, allow_user_to_manage_mfadevices=None):
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


class GetSecurityPreferenceResponseBodySecurityPreference(TeaModel):
    def __init__(self, access_key_preference=None, login_profile_preference=None, mfapreference=None,
                 personal_info_preference=None):
        self.access_key_preference = access_key_preference  # type: GetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference
        self.login_profile_preference = login_profile_preference  # type: GetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference
        self.mfapreference = mfapreference  # type: GetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference
        self.personal_info_preference = personal_info_preference  # type: GetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()
        if self.personal_info_preference:
            self.personal_info_preference.validate()

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
        return self


class GetSecurityPreferenceResponseBody(TeaModel):
    def __init__(self, request_id=None, security_preference=None):
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSecurityPreferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSecurityPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(self, user_access_key_id=None, user_id=None, user_principal_name=None):
        self.user_access_key_id = user_access_key_id  # type: str
        self.user_id = user_id  # type: str
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


class GetUserResponseBodyUser(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, email=None, last_login_date=None,
                 mobile_phone=None, update_date=None, user_id=None, user_principal_name=None):
        self.comments = comments  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.email = email  # type: str
        self.last_login_date = last_login_date  # type: str
        self.mobile_phone = mobile_phone  # type: str
        self.update_date = update_date  # type: str
        self.user_id = user_id  # type: str
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

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
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
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


class GetUserMFAInfoRequest(TeaModel):
    def __init__(self, user_principal_name=None):
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
        self.serial_number = serial_number  # type: str
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
        self.is_mfaenable = is_mfaenable  # type: bool
        self.mfadevice = mfadevice  # type: GetUserMFAInfoResponseBodyMFADevice
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserMFAInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserMFAInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserSsoSettingsResponseBodyUserSsoSettings(TeaModel):
    def __init__(self, auxiliary_domain=None, metadata_document=None, sso_enabled=None):
        self.auxiliary_domain = auxiliary_domain  # type: str
        self.metadata_document = metadata_document  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserSsoSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserSsoSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessKeysRequest(TeaModel):
    def __init__(self, user_principal_name=None):
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
        self.access_key_id = access_key_id  # type: str
        self.create_date = create_date  # type: str
        self.status = status  # type: str
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
        self.access_keys = access_keys  # type: ListAccessKeysResponseBodyAccessKeys
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAccessKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAppSecretIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListApplicationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker  # type: str
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
        self.comments = comments  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
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
        self.groups = groups  # type: ListGroupsResponseBodyGroups
        self.is_truncated = is_truncated  # type: bool
        self.marker = marker  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsForUserRequest(TeaModel):
    def __init__(self, user_principal_name=None):
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
        self.comments = comments  # type: str
        self.display_name = display_name  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
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
        self.groups = groups  # type: ListGroupsForUserResponseBodyGroups
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGroupsForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGroupsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOIDCProvidersRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker  # type: str
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
        self.arn = arn  # type: str
        self.client_ids = client_ids  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.fingerprints = fingerprints  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.issuer_url = issuer_url  # type: str
        self.oidcprovider_name = oidcprovider_name  # type: str
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
        self.is_truncated = is_truncated  # type: bool
        self.marker = marker  # type: str
        self.oidcproviders = oidcproviders  # type: ListOIDCProvidersResponseBodyOIDCProviders
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOIDCProvidersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPredefinedScopesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPredefinedScopesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSAMLProvidersRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker  # type: str
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
        self.arn = arn  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.samlprovider_name = samlprovider_name  # type: str
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
        self.is_truncated = is_truncated  # type: bool
        self.marker = marker  # type: str
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSAMLProvidersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSAMLProvidersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserBasicInfosRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker  # type: str
        self.max_items = max_items  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserBasicInfosRequest, self).to_map()
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


class ListUserBasicInfosResponseBodyUserBasicInfosUserBasicInfo(TeaModel):
    def __init__(self, display_name=None, user_id=None, user_principal_name=None):
        self.display_name = display_name  # type: str
        self.user_id = user_id  # type: str
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
        self.is_truncated = is_truncated  # type: bool
        self.marker = marker  # type: str
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserBasicInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserBasicInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker  # type: str
        self.max_items = max_items  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
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


class ListUsersResponseBodyUsersUser(TeaModel):
    def __init__(self, comments=None, create_date=None, display_name=None, email=None, last_login_date=None,
                 mobile_phone=None, update_date=None, user_id=None, user_principal_name=None):
        self.comments = comments  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.email = email  # type: str
        self.last_login_date = last_login_date  # type: str
        self.mobile_phone = mobile_phone  # type: str
        self.update_date = update_date  # type: str
        self.user_id = user_id  # type: str
        self.user_principal_name = user_principal_name  # type: str

    def validate(self):
        pass

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
        self.is_truncated = is_truncated  # type: bool
        self.marker = marker  # type: str
        self.request_id = request_id  # type: str
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


class ListUsersForGroupRequest(TeaModel):
    def __init__(self, group_name=None, marker=None, max_items=None):
        self.group_name = group_name  # type: str
        self.marker = marker  # type: str
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
        self.display_name = display_name  # type: str
        self.join_date = join_date  # type: str
        self.user_id = user_id  # type: str
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
        self.is_truncated = is_truncated  # type: bool
        self.marker = marker  # type: str
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUsersForGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUsersForGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualMFADevicesRequest(TeaModel):
    def __init__(self, marker=None, max_items=None):
        self.marker = marker  # type: str
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
        self.display_name = display_name  # type: str
        self.user_id = user_id  # type: str
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
        self.activate_date = activate_date  # type: str
        self.serial_number = serial_number  # type: str
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
        self.is_truncated = is_truncated  # type: bool
        self.marker = marker  # type: str
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListVirtualMFADevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVirtualMFADevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClientIdFromOIDCProviderRequest(TeaModel):
    def __init__(self, client_id=None, oidcprovider_name=None):
        self.client_id = client_id  # type: str
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
        self.arn = arn  # type: str
        self.client_ids = client_ids  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.fingerprints = fingerprints  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.issuer_url = issuer_url  # type: str
        self.oidcprovider_name = oidcprovider_name  # type: str
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
        self.oidcprovider = oidcprovider  # type: RemoveClientIdFromOIDCProviderResponseBodyOIDCProvider
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveClientIdFromOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveClientIdFromOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFingerprintFromOIDCProviderRequest(TeaModel):
    def __init__(self, fingerprint=None, oidcprovider_name=None):
        self.fingerprint = fingerprint  # type: str
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
        self.arn = arn  # type: str
        self.client_ids = client_ids  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.fingerprints = fingerprints  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.issuer_url = issuer_url  # type: str
        self.oidcprovider_name = oidcprovider_name  # type: str
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
        self.oidcprovider = oidcprovider  # type: RemoveFingerprintFromOIDCProviderResponseBodyOIDCProvider
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveFingerprintFromOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveFingerprintFromOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromGroupRequest(TeaModel):
    def __init__(self, group_name=None, user_principal_name=None):
        self.group_name = group_name  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveUserFromGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveUserFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultDomainRequest(TeaModel):
    def __init__(self, default_domain_name=None):
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
        self.default_domain_name = default_domain_name  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDefaultDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDefaultDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPasswordPolicyRequest(TeaModel):
    def __init__(self, hard_expire=None, max_login_attemps=None, max_password_age=None,
                 minimum_password_different_character=None, minimum_password_length=None, password_not_contain_user_name=None,
                 password_reuse_prevention=None, require_lowercase_characters=None, require_numbers=None, require_symbols=None,
                 require_uppercase_characters=None):
        self.hard_expire = hard_expire  # type: bool
        self.max_login_attemps = max_login_attemps  # type: int
        self.max_password_age = max_password_age  # type: int
        self.minimum_password_different_character = minimum_password_different_character  # type: int
        self.minimum_password_length = minimum_password_length  # type: int
        self.password_not_contain_user_name = password_not_contain_user_name  # type: bool
        self.password_reuse_prevention = password_reuse_prevention  # type: int
        self.require_lowercase_characters = require_lowercase_characters  # type: bool
        self.require_numbers = require_numbers  # type: bool
        self.require_symbols = require_symbols  # type: bool
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
        self.hard_expire = hard_expire  # type: bool
        self.max_login_attemps = max_login_attemps  # type: int
        self.max_password_age = max_password_age  # type: int
        self.minimum_password_different_character = minimum_password_different_character  # type: int
        self.minimum_password_length = minimum_password_length  # type: int
        self.password_not_contain_user_name = password_not_contain_user_name  # type: bool
        self.password_reuse_prevention = password_reuse_prevention  # type: int
        self.require_lowercase_characters = require_lowercase_characters  # type: bool
        self.require_numbers = require_numbers  # type: bool
        self.require_symbols = require_symbols  # type: bool
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
        self.password_policy = password_policy  # type: SetPasswordPolicyResponseBodyPasswordPolicy
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetPasswordPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSecurityPreferenceRequest(TeaModel):
    def __init__(self, allow_user_to_change_password=None, allow_user_to_manage_access_keys=None,
                 allow_user_to_manage_mfadevices=None, allow_user_to_manage_personal_ding_talk=None, enable_save_mfaticket=None,
                 enforce_mfafor_login=None, login_network_masks=None, login_session_duration=None):
        self.allow_user_to_change_password = allow_user_to_change_password  # type: bool
        self.allow_user_to_manage_access_keys = allow_user_to_manage_access_keys  # type: bool
        self.allow_user_to_manage_mfadevices = allow_user_to_manage_mfadevices  # type: bool
        self.allow_user_to_manage_personal_ding_talk = allow_user_to_manage_personal_ding_talk  # type: bool
        self.enable_save_mfaticket = enable_save_mfaticket  # type: bool
        self.enforce_mfafor_login = enforce_mfafor_login  # type: bool
        self.login_network_masks = login_network_masks  # type: str
        self.login_session_duration = login_session_duration  # type: int

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
        if self.enforce_mfafor_login is not None:
            result['EnforceMFAForLogin'] = self.enforce_mfafor_login
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
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
        if m.get('EnforceMFAForLogin') is not None:
            self.enforce_mfafor_login = m.get('EnforceMFAForLogin')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference(TeaModel):
    def __init__(self, allow_user_to_manage_access_keys=None):
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
    def __init__(self, allow_user_to_change_password=None, enable_save_mfaticket=None, enforce_mfafor_login=None,
                 login_network_masks=None, login_session_duration=None):
        self.allow_user_to_change_password = allow_user_to_change_password  # type: bool
        self.enable_save_mfaticket = enable_save_mfaticket  # type: bool
        self.enforce_mfafor_login = enforce_mfafor_login  # type: bool
        self.login_network_masks = login_network_masks  # type: str
        self.login_session_duration = login_session_duration  # type: int

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
        if self.enforce_mfafor_login is not None:
            result['EnforceMFAForLogin'] = self.enforce_mfafor_login
        if self.login_network_masks is not None:
            result['LoginNetworkMasks'] = self.login_network_masks
        if self.login_session_duration is not None:
            result['LoginSessionDuration'] = self.login_session_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowUserToChangePassword') is not None:
            self.allow_user_to_change_password = m.get('AllowUserToChangePassword')
        if m.get('EnableSaveMFATicket') is not None:
            self.enable_save_mfaticket = m.get('EnableSaveMFATicket')
        if m.get('EnforceMFAForLogin') is not None:
            self.enforce_mfafor_login = m.get('EnforceMFAForLogin')
        if m.get('LoginNetworkMasks') is not None:
            self.login_network_masks = m.get('LoginNetworkMasks')
        if m.get('LoginSessionDuration') is not None:
            self.login_session_duration = m.get('LoginSessionDuration')
        return self


class SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference(TeaModel):
    def __init__(self, allow_user_to_manage_mfadevices=None):
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


class SetSecurityPreferenceResponseBodySecurityPreference(TeaModel):
    def __init__(self, access_key_preference=None, login_profile_preference=None, mfapreference=None,
                 personal_info_preference=None):
        self.access_key_preference = access_key_preference  # type: SetSecurityPreferenceResponseBodySecurityPreferenceAccessKeyPreference
        self.login_profile_preference = login_profile_preference  # type: SetSecurityPreferenceResponseBodySecurityPreferenceLoginProfilePreference
        self.mfapreference = mfapreference  # type: SetSecurityPreferenceResponseBodySecurityPreferenceMFAPreference
        self.personal_info_preference = personal_info_preference  # type: SetSecurityPreferenceResponseBodySecurityPreferencePersonalInfoPreference

    def validate(self):
        if self.access_key_preference:
            self.access_key_preference.validate()
        if self.login_profile_preference:
            self.login_profile_preference.validate()
        if self.mfapreference:
            self.mfapreference.validate()
        if self.personal_info_preference:
            self.personal_info_preference.validate()

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
        return self


class SetSecurityPreferenceResponseBody(TeaModel):
    def __init__(self, request_id=None, security_preference=None):
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetSecurityPreferenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetSecurityPreferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserSsoSettingsRequest(TeaModel):
    def __init__(self, auxiliary_domain=None, metadata_document=None, sso_enabled=None):
        self.auxiliary_domain = auxiliary_domain  # type: str
        self.metadata_document = metadata_document  # type: str
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
        self.auxiliary_domain = auxiliary_domain  # type: str
        self.metadata_document = metadata_document  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetUserSsoSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetUserSsoSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindMFADeviceRequest(TeaModel):
    def __init__(self, user_principal_name=None):
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
        self.mfadevice = mfadevice  # type: UnbindMFADeviceResponseBodyMFADevice
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnbindMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccessKeyRequest(TeaModel):
    def __init__(self, status=None, user_access_key_id=None, user_principal_name=None):
        self.status = status  # type: str
        self.user_access_key_id = user_access_key_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAccessKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(self, group_name=None, new_comments=None, new_display_name=None, new_group_name=None):
        self.group_name = group_name  # type: str
        self.new_comments = new_comments  # type: str
        self.new_display_name = new_display_name  # type: str
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
        self.comments = comments  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
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
        self.group = group  # type: UpdateGroupResponseBodyGroup
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoginProfileRequest(TeaModel):
    def __init__(self, mfabind_required=None, password=None, password_reset_required=None, status=None,
                 user_principal_name=None):
        self.mfabind_required = mfabind_required  # type: bool
        self.password = password  # type: str
        self.password_reset_required = password_reset_required  # type: bool
        self.status = status  # type: str
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
        self.mfabind_required = mfabind_required  # type: bool
        self.password_reset_required = password_reset_required  # type: bool
        self.status = status  # type: str
        self.update_date = update_date  # type: str
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
        self.login_profile = login_profile  # type: UpdateLoginProfileResponseBodyLoginProfile
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateLoginProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateLoginProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOIDCProviderRequest(TeaModel):
    def __init__(self, client_ids=None, new_description=None, oidcprovider_name=None):
        self.client_ids = client_ids  # type: str
        self.new_description = new_description  # type: str
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
        self.arn = arn  # type: str
        self.client_ids = client_ids  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.fingerprints = fingerprints  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.issuer_url = issuer_url  # type: str
        self.oidcprovider_name = oidcprovider_name  # type: str
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
        self.oidcprovider = oidcprovider  # type: UpdateOIDCProviderResponseBodyOIDCProvider
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateOIDCProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateOIDCProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSAMLProviderRequest(TeaModel):
    def __init__(self, new_description=None, new_encoded_samlmetadata_document=None, samlprovider_name=None):
        self.new_description = new_description  # type: str
        self.new_encoded_samlmetadata_document = new_encoded_samlmetadata_document  # type: str
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
        self.arn = arn  # type: str
        self.create_date = create_date  # type: str
        self.description = description  # type: str
        self.samlprovider_name = samlprovider_name  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSAMLProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSAMLProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(self, new_comments=None, new_display_name=None, new_email=None, new_mobile_phone=None,
                 new_user_principal_name=None, user_id=None, user_principal_name=None):
        self.new_comments = new_comments  # type: str
        self.new_display_name = new_display_name  # type: str
        self.new_email = new_email  # type: str
        self.new_mobile_phone = new_mobile_phone  # type: str
        self.new_user_principal_name = new_user_principal_name  # type: str
        self.user_id = user_id  # type: str
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
                 mobile_phone=None, update_date=None, user_id=None, user_principal_name=None):
        self.comments = comments  # type: str
        self.create_date = create_date  # type: str
        self.display_name = display_name  # type: str
        self.email = email  # type: str
        self.last_login_date = last_login_date  # type: str
        self.mobile_phone = mobile_phone  # type: str
        self.update_date = update_date  # type: str
        self.user_id = user_id  # type: str
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
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user=None):
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


