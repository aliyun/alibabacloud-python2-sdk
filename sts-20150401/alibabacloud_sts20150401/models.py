# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AssumeRoleRequest(TeaModel):
    def __init__(self, duration_seconds=None, policy=None, role_arn=None, role_session_name=None):
        self.duration_seconds = duration_seconds  # type: long
        self.policy = policy  # type: str
        self.role_arn = role_arn  # type: str
        self.role_session_name = role_session_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.role_session_name is not None:
            result['RoleSessionName'] = self.role_session_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('RoleSessionName') is not None:
            self.role_session_name = m.get('RoleSessionName')
        return self


class AssumeRoleResponseBodyAssumedRoleUser(TeaModel):
    def __init__(self, assumed_role_id=None, arn=None):
        self.assumed_role_id = assumed_role_id  # type: str
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleResponseBodyAssumedRoleUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assumed_role_id is not None:
            result['AssumedRoleId'] = self.assumed_role_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssumedRoleId') is not None:
            self.assumed_role_id = m.get('AssumedRoleId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class AssumeRoleResponseBodyCredentials(TeaModel):
    def __init__(self, security_token=None, expiration=None, access_key_secret=None, access_key_id=None):
        self.security_token = security_token  # type: str
        self.expiration = expiration  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.access_key_id = access_key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleResponseBodyCredentials, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        return self


class AssumeRoleResponseBody(TeaModel):
    def __init__(self, request_id=None, assumed_role_user=None, credentials=None):
        self.request_id = request_id  # type: str
        self.assumed_role_user = assumed_role_user  # type: AssumeRoleResponseBodyAssumedRoleUser
        self.credentials = credentials  # type: AssumeRoleResponseBodyCredentials

    def validate(self):
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        _map = super(AssumeRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.assumed_role_user is not None:
            result['AssumedRoleUser'] = self.assumed_role_user.to_map()
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AssumedRoleUser') is not None:
            temp_model = AssumeRoleResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m['AssumedRoleUser'])
        if m.get('Credentials') is not None:
            temp_model = AssumeRoleResponseBodyCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        return self


class AssumeRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssumeRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssumeRoleResponse, self).to_map()
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
            temp_model = AssumeRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssumeRoleWithOIDCRequest(TeaModel):
    def __init__(self, oidcprovider_arn=None, role_arn=None, oidctoken=None, policy=None, duration_seconds=None,
                 role_session_name=None):
        # OIDC Provider的ARN
        self.oidcprovider_arn = oidcprovider_arn  # type: str
        # 需要扮演的角色的ARN
        self.role_arn = role_arn  # type: str
        # OIDC的ID Token，需输入原始Token，无需Base64解码
        self.oidctoken = oidctoken  # type: str
        # 权限策略。 生成STS Token时可以指定一个额外的权限策略，以进一步限制STS Token的权限。若不指定则返回的Token拥有指定角色的所有权限。
        self.policy = policy  # type: str
        # Session过期时间，单位为秒。
        self.duration_seconds = duration_seconds  # type: long
        # 用户自定义参数。此参数用来区分不同的令牌，可用于用户级别的访问审计。
        self.role_session_name = role_session_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleWithOIDCRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oidcprovider_arn is not None:
            result['OIDCProviderArn'] = self.oidcprovider_arn
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.oidctoken is not None:
            result['OIDCToken'] = self.oidctoken
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.role_session_name is not None:
            result['RoleSessionName'] = self.role_session_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OIDCProviderArn') is not None:
            self.oidcprovider_arn = m.get('OIDCProviderArn')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('OIDCToken') is not None:
            self.oidctoken = m.get('OIDCToken')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('RoleSessionName') is not None:
            self.role_session_name = m.get('RoleSessionName')
        return self


class AssumeRoleWithOIDCResponseBodyOIDCTokenInfo(TeaModel):
    def __init__(self, subject=None, issuer=None, client_ids=None):
        self.subject = subject  # type: str
        self.issuer = issuer  # type: str
        self.client_ids = client_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleWithOIDCResponseBodyOIDCTokenInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')
        return self


class AssumeRoleWithOIDCResponseBodyAssumedRoleUser(TeaModel):
    def __init__(self, assumed_role_id=None, arn=None):
        self.assumed_role_id = assumed_role_id  # type: str
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleWithOIDCResponseBodyAssumedRoleUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assumed_role_id is not None:
            result['AssumedRoleId'] = self.assumed_role_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssumedRoleId') is not None:
            self.assumed_role_id = m.get('AssumedRoleId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class AssumeRoleWithOIDCResponseBodyCredentials(TeaModel):
    def __init__(self, security_token=None, expiration=None, access_key_secret=None, access_key_id=None):
        self.security_token = security_token  # type: str
        self.expiration = expiration  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.access_key_id = access_key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleWithOIDCResponseBodyCredentials, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        return self


class AssumeRoleWithOIDCResponseBody(TeaModel):
    def __init__(self, request_id=None, oidctoken_info=None, assumed_role_user=None, credentials=None):
        self.request_id = request_id  # type: str
        self.oidctoken_info = oidctoken_info  # type: AssumeRoleWithOIDCResponseBodyOIDCTokenInfo
        self.assumed_role_user = assumed_role_user  # type: AssumeRoleWithOIDCResponseBodyAssumedRoleUser
        self.credentials = credentials  # type: AssumeRoleWithOIDCResponseBodyCredentials

    def validate(self):
        if self.oidctoken_info:
            self.oidctoken_info.validate()
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        _map = super(AssumeRoleWithOIDCResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.oidctoken_info is not None:
            result['OIDCTokenInfo'] = self.oidctoken_info.to_map()
        if self.assumed_role_user is not None:
            result['AssumedRoleUser'] = self.assumed_role_user.to_map()
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OIDCTokenInfo') is not None:
            temp_model = AssumeRoleWithOIDCResponseBodyOIDCTokenInfo()
            self.oidctoken_info = temp_model.from_map(m['OIDCTokenInfo'])
        if m.get('AssumedRoleUser') is not None:
            temp_model = AssumeRoleWithOIDCResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m['AssumedRoleUser'])
        if m.get('Credentials') is not None:
            temp_model = AssumeRoleWithOIDCResponseBodyCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        return self


class AssumeRoleWithOIDCResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssumeRoleWithOIDCResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssumeRoleWithOIDCResponse, self).to_map()
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
            temp_model = AssumeRoleWithOIDCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssumeRoleWithSAMLRequest(TeaModel):
    def __init__(self, samlprovider_arn=None, role_arn=None, samlassertion=None, policy=None, duration_seconds=None):
        self.samlprovider_arn = samlprovider_arn  # type: str
        self.role_arn = role_arn  # type: str
        self.samlassertion = samlassertion  # type: str
        self.policy = policy  # type: str
        self.duration_seconds = duration_seconds  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleWithSAMLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.samlprovider_arn is not None:
            result['SAMLProviderArn'] = self.samlprovider_arn
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.samlassertion is not None:
            result['SAMLAssertion'] = self.samlassertion
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SAMLProviderArn') is not None:
            self.samlprovider_arn = m.get('SAMLProviderArn')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SAMLAssertion') is not None:
            self.samlassertion = m.get('SAMLAssertion')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        return self


class AssumeRoleWithSAMLResponseBodySAMLAssertionInfo(TeaModel):
    def __init__(self, subject_type=None, subject=None, issuer=None, recipient=None):
        self.subject_type = subject_type  # type: str
        self.subject = subject  # type: str
        self.issuer = issuer  # type: str
        self.recipient = recipient  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleWithSAMLResponseBodySAMLAssertionInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subject_type is not None:
            result['SubjectType'] = self.subject_type
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.recipient is not None:
            result['Recipient'] = self.recipient
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubjectType') is not None:
            self.subject_type = m.get('SubjectType')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Recipient') is not None:
            self.recipient = m.get('Recipient')
        return self


class AssumeRoleWithSAMLResponseBodyAssumedRoleUser(TeaModel):
    def __init__(self, assumed_role_id=None, arn=None):
        self.assumed_role_id = assumed_role_id  # type: str
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleWithSAMLResponseBodyAssumedRoleUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assumed_role_id is not None:
            result['AssumedRoleId'] = self.assumed_role_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssumedRoleId') is not None:
            self.assumed_role_id = m.get('AssumedRoleId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class AssumeRoleWithSAMLResponseBodyCredentials(TeaModel):
    def __init__(self, security_token=None, expiration=None, access_key_secret=None, access_key_id=None):
        self.security_token = security_token  # type: str
        self.expiration = expiration  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.access_key_id = access_key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleWithSAMLResponseBodyCredentials, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        return self


class AssumeRoleWithSAMLResponseBody(TeaModel):
    def __init__(self, request_id=None, samlassertion_info=None, assumed_role_user=None, credentials=None):
        self.request_id = request_id  # type: str
        self.samlassertion_info = samlassertion_info  # type: AssumeRoleWithSAMLResponseBodySAMLAssertionInfo
        self.assumed_role_user = assumed_role_user  # type: AssumeRoleWithSAMLResponseBodyAssumedRoleUser
        self.credentials = credentials  # type: AssumeRoleWithSAMLResponseBodyCredentials

    def validate(self):
        if self.samlassertion_info:
            self.samlassertion_info.validate()
        if self.assumed_role_user:
            self.assumed_role_user.validate()
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        _map = super(AssumeRoleWithSAMLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.samlassertion_info is not None:
            result['SAMLAssertionInfo'] = self.samlassertion_info.to_map()
        if self.assumed_role_user is not None:
            result['AssumedRoleUser'] = self.assumed_role_user.to_map()
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SAMLAssertionInfo') is not None:
            temp_model = AssumeRoleWithSAMLResponseBodySAMLAssertionInfo()
            self.samlassertion_info = temp_model.from_map(m['SAMLAssertionInfo'])
        if m.get('AssumedRoleUser') is not None:
            temp_model = AssumeRoleWithSAMLResponseBodyAssumedRoleUser()
            self.assumed_role_user = temp_model.from_map(m['AssumedRoleUser'])
        if m.get('Credentials') is not None:
            temp_model = AssumeRoleWithSAMLResponseBodyCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        return self


class AssumeRoleWithSAMLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssumeRoleWithSAMLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssumeRoleWithSAMLResponse, self).to_map()
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
            temp_model = AssumeRoleWithSAMLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCallerIdentityResponseBody(TeaModel):
    def __init__(self, identity_type=None, account_id=None, request_id=None, principal_id=None, user_id=None,
                 arn=None, role_id=None):
        self.identity_type = identity_type  # type: str
        self.account_id = account_id  # type: str
        self.request_id = request_id  # type: str
        self.principal_id = principal_id  # type: str
        self.user_id = user_id  # type: str
        self.arn = arn  # type: str
        self.role_id = role_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCallerIdentityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class GetCallerIdentityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCallerIdentityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCallerIdentityResponse, self).to_map()
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
            temp_model = GetCallerIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


