# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateAuthenticatorRegistrationRequest(TeaModel):
    def __init__(self, application_external_id=None, authenticator_type=None, client_extend_params_json=None,
                 client_extend_params_json_sign=None, registration_context=None, server_extend_params_json=None, user_display_name=None,
                 user_id=None, user_name=None):
        # 应用外部Id
        self.application_external_id = application_external_id  # type: str
        # 认证器类型
        self.authenticator_type = authenticator_type  # type: str
        # 客户端SDK生成认证上下文
        self.client_extend_params_json = client_extend_params_json  # type: str
        # 客户端SDK生成认证上下文签名信息
        self.client_extend_params_json_sign = client_extend_params_json_sign  # type: str
        # 注册上下文
        self.registration_context = registration_context  # type: str
        # 服务端配置项，决定认证要求属性
        self.server_extend_params_json = server_extend_params_json  # type: str
        # 用户展示名
        self.user_display_name = user_display_name  # type: str
        # 用户id
        self.user_id = user_id  # type: str
        # 用户姓名
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthenticatorRegistrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.client_extend_params_json is not None:
            result['ClientExtendParamsJson'] = self.client_extend_params_json
        if self.client_extend_params_json_sign is not None:
            result['ClientExtendParamsJsonSign'] = self.client_extend_params_json_sign
        if self.registration_context is not None:
            result['RegistrationContext'] = self.registration_context
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.user_display_name is not None:
            result['UserDisplayName'] = self.user_display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('ClientExtendParamsJson') is not None:
            self.client_extend_params_json = m.get('ClientExtendParamsJson')
        if m.get('ClientExtendParamsJsonSign') is not None:
            self.client_extend_params_json_sign = m.get('ClientExtendParamsJsonSign')
        if m.get('RegistrationContext') is not None:
            self.registration_context = m.get('RegistrationContext')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('UserDisplayName') is not None:
            self.user_display_name = m.get('UserDisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateAuthenticatorRegistrationResponseBody(TeaModel):
    def __init__(self, challenge_base_64=None, options=None, request_id=None):
        # 防重放挑战码
        self.challenge_base_64 = challenge_base_64  # type: str
        # 创建认证器的Options
        self.options = options  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthenticatorRegistrationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.challenge_base_64 is not None:
            result['ChallengeBase64'] = self.challenge_base_64
        if self.options is not None:
            result['Options'] = self.options
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChallengeBase64') is not None:
            self.challenge_base_64 = m.get('ChallengeBase64')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAuthenticatorRegistrationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAuthenticatorRegistrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAuthenticatorRegistrationResponse, self).to_map()
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
            temp_model = CreateAuthenticatorRegistrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserAuthenticateOptionsRequest(TeaModel):
    def __init__(self, application_external_id=None, authenticator_type=None, bind_hash_base_64=None,
                 client_extend_params_json=None, client_extend_params_json_sign=None, server_extend_params_json=None, user_id=None):
        # 应用外部Id
        self.application_external_id = application_external_id  # type: str
        # 认证器类型
        self.authenticator_type = authenticator_type  # type: str
        # 操作hash，用来和认证绑定
        self.bind_hash_base_64 = bind_hash_base_64  # type: str
        # 客户端SDK生成认证上下文
        self.client_extend_params_json = client_extend_params_json  # type: str
        # 客户端SDK生成认证上下文签名信息
        self.client_extend_params_json_sign = client_extend_params_json_sign  # type: str
        # 服务端配置项，决定认证要求属性
        self.server_extend_params_json = server_extend_params_json  # type: str
        # 用户id
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserAuthenticateOptionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.bind_hash_base_64 is not None:
            result['BindHashBase64'] = self.bind_hash_base_64
        if self.client_extend_params_json is not None:
            result['ClientExtendParamsJson'] = self.client_extend_params_json
        if self.client_extend_params_json_sign is not None:
            result['ClientExtendParamsJsonSign'] = self.client_extend_params_json_sign
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('BindHashBase64') is not None:
            self.bind_hash_base_64 = m.get('BindHashBase64')
        if m.get('ClientExtendParamsJson') is not None:
            self.client_extend_params_json = m.get('ClientExtendParamsJson')
        if m.get('ClientExtendParamsJsonSign') is not None:
            self.client_extend_params_json_sign = m.get('ClientExtendParamsJsonSign')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateUserAuthenticateOptionsResponseBody(TeaModel):
    def __init__(self, challenge_base_64=None, options=None, request_id=None):
        # 防重放挑战码
        self.challenge_base_64 = challenge_base_64  # type: str
        # 创建认证的Options，内容是JSON
        self.options = options  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserAuthenticateOptionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.challenge_base_64 is not None:
            result['ChallengeBase64'] = self.challenge_base_64
        if self.options is not None:
            result['Options'] = self.options
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChallengeBase64') is not None:
            self.challenge_base_64 = m.get('ChallengeBase64')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUserAuthenticateOptionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUserAuthenticateOptionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserAuthenticateOptionsResponse, self).to_map()
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
            temp_model = CreateUserAuthenticateOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeregisterAuthenticatorRequest(TeaModel):
    def __init__(self, application_external_id=None, authenticator_uuid=None, user_id=None):
        # 应用外部Id
        self.application_external_id = application_external_id  # type: str
        # 认证器uuid
        self.authenticator_uuid = authenticator_uuid  # type: str
        # 用户id
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterAuthenticatorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeregisterAuthenticatorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterAuthenticatorResponseBody, self).to_map()
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


class DeregisterAuthenticatorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeregisterAuthenticatorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeregisterAuthenticatorResponse, self).to_map()
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
            temp_model = DeregisterAuthenticatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchAccessTokenRequest(TeaModel):
    def __init__(self, application_external_id=None, mobile_extend_params_json=None,
                 mobile_extend_params_json_sign=None, server_extend_params_json=None, xclient_ip=None):
        self.application_external_id = application_external_id  # type: str
        self.mobile_extend_params_json = mobile_extend_params_json  # type: str
        self.mobile_extend_params_json_sign = mobile_extend_params_json_sign  # type: str
        self.server_extend_params_json = server_extend_params_json  # type: str
        self.xclient_ip = xclient_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FetchAccessTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.mobile_extend_params_json is not None:
            result['MobileExtendParamsJson'] = self.mobile_extend_params_json
        if self.mobile_extend_params_json_sign is not None:
            result['MobileExtendParamsJsonSign'] = self.mobile_extend_params_json_sign
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.xclient_ip is not None:
            result['XClientIp'] = self.xclient_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('MobileExtendParamsJson') is not None:
            self.mobile_extend_params_json = m.get('MobileExtendParamsJson')
        if m.get('MobileExtendParamsJsonSign') is not None:
            self.mobile_extend_params_json_sign = m.get('MobileExtendParamsJsonSign')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('XClientIp') is not None:
            self.xclient_ip = m.get('XClientIp')
        return self


class FetchAccessTokenResponseBodyData(TeaModel):
    def __init__(self, access_token=None, expires_in=None, id_token=None, refresh_token=None, scope=None,
                 token_type=None):
        self.access_token = access_token  # type: str
        self.expires_in = expires_in  # type: str
        self.id_token = id_token  # type: str
        self.refresh_token = refresh_token  # type: str
        self.scope = scope  # type: str
        self.token_type = token_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FetchAccessTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['Access_token'] = self.access_token
        if self.expires_in is not None:
            result['Expires_in'] = self.expires_in
        if self.id_token is not None:
            result['Id_token'] = self.id_token
        if self.refresh_token is not None:
            result['Refresh_token'] = self.refresh_token
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.token_type is not None:
            result['Token_type'] = self.token_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Access_token') is not None:
            self.access_token = m.get('Access_token')
        if m.get('Expires_in') is not None:
            self.expires_in = m.get('Expires_in')
        if m.get('Id_token') is not None:
            self.id_token = m.get('Id_token')
        if m.get('Refresh_token') is not None:
            self.refresh_token = m.get('Refresh_token')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Token_type') is not None:
            self.token_type = m.get('Token_type')
        return self


class FetchAccessTokenResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: FetchAccessTokenResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(FetchAccessTokenResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = FetchAccessTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FetchAccessTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FetchAccessTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FetchAccessTokenResponse, self).to_map()
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
            temp_model = FetchAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthenticatorRequest(TeaModel):
    def __init__(self, application_external_id=None, authenticator_uuid=None, user_id=None):
        # 应用外部Id
        self.application_external_id = application_external_id  # type: str
        # 认证器uuid
        self.authenticator_uuid = authenticator_uuid  # type: str
        # 用户ID
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthenticatorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetAuthenticatorResponseBodyAuthenticator(TeaModel):
    def __init__(self, authenticator_name=None, authenticator_uuid=None, credential_id=None,
                 custom_authenticator=None, last_verify_source_ip=None, last_verify_time=None, last_verify_user_agent=None,
                 register_source_ip=None, register_time=None, type=None):
        # 认证器名字
        self.authenticator_name = authenticator_name  # type: str
        self.authenticator_uuid = authenticator_uuid  # type: str
        # 创建认证器的Options
        self.credential_id = credential_id  # type: str
        self.custom_authenticator = custom_authenticator  # type: str
        # 用户最后签名IP
        self.last_verify_source_ip = last_verify_source_ip  # type: str
        # 最后验证时间
        self.last_verify_time = last_verify_time  # type: long
        # 用户最后签名userAgent
        self.last_verify_user_agent = last_verify_user_agent  # type: str
        # 用户注册IP
        self.register_source_ip = register_source_ip  # type: str
        # 注册时间
        self.register_time = register_time  # type: long
        # 认证器类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthenticatorResponseBodyAuthenticator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.custom_authenticator is not None:
            result['CustomAuthenticator'] = self.custom_authenticator
        if self.last_verify_source_ip is not None:
            result['LastVerifySourceIp'] = self.last_verify_source_ip
        if self.last_verify_time is not None:
            result['LastVerifyTime'] = self.last_verify_time
        if self.last_verify_user_agent is not None:
            result['LastVerifyUserAgent'] = self.last_verify_user_agent
        if self.register_source_ip is not None:
            result['RegisterSourceIp'] = self.register_source_ip
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('CustomAuthenticator') is not None:
            self.custom_authenticator = m.get('CustomAuthenticator')
        if m.get('LastVerifySourceIp') is not None:
            self.last_verify_source_ip = m.get('LastVerifySourceIp')
        if m.get('LastVerifyTime') is not None:
            self.last_verify_time = m.get('LastVerifyTime')
        if m.get('LastVerifyUserAgent') is not None:
            self.last_verify_user_agent = m.get('LastVerifyUserAgent')
        if m.get('RegisterSourceIp') is not None:
            self.register_source_ip = m.get('RegisterSourceIp')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAuthenticatorResponseBody(TeaModel):
    def __init__(self, authenticator=None, request_id=None):
        self.authenticator = authenticator  # type: GetAuthenticatorResponseBodyAuthenticator
        self.request_id = request_id  # type: str

    def validate(self):
        if self.authenticator:
            self.authenticator.validate()

    def to_map(self):
        _map = super(GetAuthenticatorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authenticator is not None:
            result['Authenticator'] = self.authenticator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Authenticator') is not None:
            temp_model = GetAuthenticatorResponseBodyAuthenticator()
            self.authenticator = temp_model.from_map(m['Authenticator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuthenticatorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAuthenticatorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuthenticatorResponse, self).to_map()
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
            temp_model = GetAuthenticatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthenticationLogsRequest(TeaModel):
    def __init__(self, application_external_id=None, authenticator_type=None, authenticator_uuid=None,
                 credential_id=None, from_time=None, log_tag=None, page_number=None, page_size=None, to_time=None, user_id=None):
        self.application_external_id = application_external_id  # type: str
        self.authenticator_type = authenticator_type  # type: str
        self.authenticator_uuid = authenticator_uuid  # type: str
        self.credential_id = credential_id  # type: str
        self.from_time = from_time  # type: long
        self.log_tag = log_tag  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.to_time = to_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthenticationLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.from_time is not None:
            result['FromTime'] = self.from_time
        if self.log_tag is not None:
            result['LogTag'] = self.log_tag
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.to_time is not None:
            result['ToTime'] = self.to_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('FromTime') is not None:
            self.from_time = m.get('FromTime')
        if m.get('LogTag') is not None:
            self.log_tag = m.get('LogTag')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ToTime') is not None:
            self.to_time = m.get('ToTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAuthenticationLogsResponseBodyAuthenticationLogContent(TeaModel):
    def __init__(self, ali_uid=None, application_external_id=None, application_uuid=None,
                 authentication_action=None, authentication_time=None, authenticator_name=None, authenticator_type=None,
                 authenticator_uuid=None, challenge_base_64=None, credential_id=None, error_code=None, error_message=None,
                 log_params=None, log_tag=None, raw_authentication_context=None, tenant_id=None, user_agent=None, user_id=None,
                 user_source_ip=None, verify_result=None):
        self.ali_uid = ali_uid  # type: str
        self.application_external_id = application_external_id  # type: str
        self.application_uuid = application_uuid  # type: str
        self.authentication_action = authentication_action  # type: str
        self.authentication_time = authentication_time  # type: long
        self.authenticator_name = authenticator_name  # type: str
        self.authenticator_type = authenticator_type  # type: str
        self.authenticator_uuid = authenticator_uuid  # type: str
        self.challenge_base_64 = challenge_base_64  # type: str
        self.credential_id = credential_id  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.log_params = log_params  # type: str
        self.log_tag = log_tag  # type: str
        self.raw_authentication_context = raw_authentication_context  # type: str
        self.tenant_id = tenant_id  # type: str
        self.user_agent = user_agent  # type: str
        self.user_id = user_id  # type: str
        self.user_source_ip = user_source_ip  # type: str
        self.verify_result = verify_result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthenticationLogsResponseBodyAuthenticationLogContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.application_uuid is not None:
            result['ApplicationUuid'] = self.application_uuid
        if self.authentication_action is not None:
            result['AuthenticationAction'] = self.authentication_action
        if self.authentication_time is not None:
            result['AuthenticationTime'] = self.authentication_time
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.challenge_base_64 is not None:
            result['ChallengeBase64'] = self.challenge_base_64
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.log_params is not None:
            result['LogParams'] = self.log_params
        if self.log_tag is not None:
            result['LogTag'] = self.log_tag
        if self.raw_authentication_context is not None:
            result['RawAuthenticationContext'] = self.raw_authentication_context
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_agent is not None:
            result['UserAgent'] = self.user_agent
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source_ip is not None:
            result['UserSourceIp'] = self.user_source_ip
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('ApplicationUuid') is not None:
            self.application_uuid = m.get('ApplicationUuid')
        if m.get('AuthenticationAction') is not None:
            self.authentication_action = m.get('AuthenticationAction')
        if m.get('AuthenticationTime') is not None:
            self.authentication_time = m.get('AuthenticationTime')
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('ChallengeBase64') is not None:
            self.challenge_base_64 = m.get('ChallengeBase64')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogParams') is not None:
            self.log_params = m.get('LogParams')
        if m.get('LogTag') is not None:
            self.log_tag = m.get('LogTag')
        if m.get('RawAuthenticationContext') is not None:
            self.raw_authentication_context = m.get('RawAuthenticationContext')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserAgent') is not None:
            self.user_agent = m.get('UserAgent')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSourceIp') is not None:
            self.user_source_ip = m.get('UserSourceIp')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class ListAuthenticationLogsResponseBody(TeaModel):
    def __init__(self, authentication_log_content=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.authentication_log_content = authentication_log_content  # type: list[ListAuthenticationLogsResponseBodyAuthenticationLogContent]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        # 返回列表长度
        self.total_count = total_count  # type: long

    def validate(self):
        if self.authentication_log_content:
            for k in self.authentication_log_content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAuthenticationLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthenticationLogContent'] = []
        if self.authentication_log_content is not None:
            for k in self.authentication_log_content:
                result['AuthenticationLogContent'].append(k.to_map() if k else None)
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
        self.authentication_log_content = []
        if m.get('AuthenticationLogContent') is not None:
            for k in m.get('AuthenticationLogContent'):
                temp_model = ListAuthenticationLogsResponseBodyAuthenticationLogContent()
                self.authentication_log_content.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAuthenticationLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAuthenticationLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAuthenticationLogsResponse, self).to_map()
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
            temp_model = ListAuthenticationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthenticatorOpsLogsRequest(TeaModel):
    def __init__(self, application_external_id=None, authenticator_type=None, authenticator_uuid=None,
                 from_time=None, page_number=None, page_size=None, to_time=None, user_id=None):
        self.application_external_id = application_external_id  # type: str
        self.authenticator_type = authenticator_type  # type: str
        self.authenticator_uuid = authenticator_uuid  # type: str
        self.from_time = from_time  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.to_time = to_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthenticatorOpsLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.from_time is not None:
            result['FromTime'] = self.from_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.to_time is not None:
            result['ToTime'] = self.to_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('FromTime') is not None:
            self.from_time = m.get('FromTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ToTime') is not None:
            self.to_time = m.get('ToTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAuthenticatorOpsLogsResponseBodyAuthenticationLogContent(TeaModel):
    def __init__(self, ali_uid=None, application_external_id=None, application_uuid=None, authenticator_name=None,
                 authenticator_type=None, authenticator_uuid=None, challenge_base_64=None, credential_id=None, error_code=None,
                 error_message=None, log_params=None, operation_action=None, operation_result=None, operation_time=None,
                 raw_context=None, tenant_id=None, user_agent=None, user_id=None, user_source_ip=None):
        self.ali_uid = ali_uid  # type: str
        self.application_external_id = application_external_id  # type: str
        self.application_uuid = application_uuid  # type: str
        self.authenticator_name = authenticator_name  # type: str
        self.authenticator_type = authenticator_type  # type: str
        self.authenticator_uuid = authenticator_uuid  # type: str
        self.challenge_base_64 = challenge_base_64  # type: str
        self.credential_id = credential_id  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.log_params = log_params  # type: str
        self.operation_action = operation_action  # type: str
        self.operation_result = operation_result  # type: bool
        self.operation_time = operation_time  # type: long
        self.raw_context = raw_context  # type: str
        self.tenant_id = tenant_id  # type: str
        self.user_agent = user_agent  # type: str
        self.user_id = user_id  # type: str
        self.user_source_ip = user_source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthenticatorOpsLogsResponseBodyAuthenticationLogContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.application_uuid is not None:
            result['ApplicationUuid'] = self.application_uuid
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.challenge_base_64 is not None:
            result['ChallengeBase64'] = self.challenge_base_64
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.log_params is not None:
            result['LogParams'] = self.log_params
        if self.operation_action is not None:
            result['OperationAction'] = self.operation_action
        if self.operation_result is not None:
            result['OperationResult'] = self.operation_result
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.raw_context is not None:
            result['RawContext'] = self.raw_context
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_agent is not None:
            result['UserAgent'] = self.user_agent
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source_ip is not None:
            result['UserSourceIp'] = self.user_source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('ApplicationUuid') is not None:
            self.application_uuid = m.get('ApplicationUuid')
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('ChallengeBase64') is not None:
            self.challenge_base_64 = m.get('ChallengeBase64')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogParams') is not None:
            self.log_params = m.get('LogParams')
        if m.get('OperationAction') is not None:
            self.operation_action = m.get('OperationAction')
        if m.get('OperationResult') is not None:
            self.operation_result = m.get('OperationResult')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('RawContext') is not None:
            self.raw_context = m.get('RawContext')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserAgent') is not None:
            self.user_agent = m.get('UserAgent')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSourceIp') is not None:
            self.user_source_ip = m.get('UserSourceIp')
        return self


class ListAuthenticatorOpsLogsResponseBody(TeaModel):
    def __init__(self, authentication_log_content=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.authentication_log_content = authentication_log_content  # type: list[ListAuthenticatorOpsLogsResponseBodyAuthenticationLogContent]
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        # 返回列表长度
        self.total_count = total_count  # type: long

    def validate(self):
        if self.authentication_log_content:
            for k in self.authentication_log_content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAuthenticatorOpsLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthenticationLogContent'] = []
        if self.authentication_log_content is not None:
            for k in self.authentication_log_content:
                result['AuthenticationLogContent'].append(k.to_map() if k else None)
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
        self.authentication_log_content = []
        if m.get('AuthenticationLogContent') is not None:
            for k in m.get('AuthenticationLogContent'):
                temp_model = ListAuthenticatorOpsLogsResponseBodyAuthenticationLogContent()
                self.authentication_log_content.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAuthenticatorOpsLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAuthenticatorOpsLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAuthenticatorOpsLogsResponse, self).to_map()
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
            temp_model = ListAuthenticatorOpsLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthenticatorsRequest(TeaModel):
    def __init__(self, application_external_id=None, authenticator_type=None, page_number=None, page_size=None,
                 user_id=None):
        # 应用外部Id
        self.application_external_id = application_external_id  # type: str
        # 认证器类型
        self.authenticator_type = authenticator_type  # type: str
        # 当前开始读取的位置，不设置时默认为1
        self.page_number = page_number  # type: long
        # 本次读取的最大数据记录数量，不指定时使用默认值
        self.page_size = page_size  # type: long
        # 用户id
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthenticatorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAuthenticatorsResponseBodyAuthenticator(TeaModel):
    def __init__(self, application_external_id=None, authenticator_name=None, authenticator_uuid=None,
                 credential_id=None, last_verify_time=None, register_time=None, type=None):
        # 应用ID
        self.application_external_id = application_external_id  # type: str
        # 身份认证对应的认证器名称
        self.authenticator_name = authenticator_name  # type: str
        # 认证器uuid
        self.authenticator_uuid = authenticator_uuid  # type: str
        # 身份认证ID
        self.credential_id = credential_id  # type: str
        # 最后验证时间，如果新注册则为注册时间
        self.last_verify_time = last_verify_time  # type: long
        # 创建时间
        self.register_time = register_time  # type: long
        # 认证器类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthenticatorsResponseBodyAuthenticator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.last_verify_time is not None:
            result['LastVerifyTime'] = self.last_verify_time
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('LastVerifyTime') is not None:
            self.last_verify_time = m.get('LastVerifyTime')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAuthenticatorsResponseBody(TeaModel):
    def __init__(self, authenticator=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.authenticator = authenticator  # type: list[ListAuthenticatorsResponseBodyAuthenticator]
        # 读取到的位置
        self.page_number = page_number  # type: long
        # 每页记录数量
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        # 查询结果数据总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.authenticator:
            for k in self.authenticator:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAuthenticatorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Authenticator'] = []
        if self.authenticator is not None:
            for k in self.authenticator:
                result['Authenticator'].append(k.to_map() if k else None)
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
        self.authenticator = []
        if m.get('Authenticator') is not None:
            for k in m.get('Authenticator'):
                temp_model = ListAuthenticatorsResponseBodyAuthenticator()
                self.authenticator.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAuthenticatorsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAuthenticatorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAuthenticatorsResponse, self).to_map()
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
            temp_model = ListAuthenticatorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPwnedPasswordsRequest(TeaModel):
    def __init__(self, prefix_hex_password_sha_1hash=None):
        # 泄露密码SHA1值前6位
        self.prefix_hex_password_sha_1hash = prefix_hex_password_sha_1hash  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPwnedPasswordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prefix_hex_password_sha_1hash is not None:
            result['PrefixHexPasswordSha1Hash'] = self.prefix_hex_password_sha_1hash
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrefixHexPasswordSha1Hash') is not None:
            self.prefix_hex_password_sha_1hash = m.get('PrefixHexPasswordSha1Hash')
        return self


class ListPwnedPasswordsResponseBodyPwnedPasswordInfos(TeaModel):
    def __init__(self, hex_password_sha_1hash=None, pwned_count=None):
        # 泄露密码SHA1值
        self.hex_password_sha_1hash = hex_password_sha_1hash  # type: str
        # 泄露次数
        self.pwned_count = pwned_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPwnedPasswordsResponseBodyPwnedPasswordInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hex_password_sha_1hash is not None:
            result['HexPasswordSha1Hash'] = self.hex_password_sha_1hash
        if self.pwned_count is not None:
            result['PwnedCount'] = self.pwned_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HexPasswordSha1Hash') is not None:
            self.hex_password_sha_1hash = m.get('HexPasswordSha1Hash')
        if m.get('PwnedCount') is not None:
            self.pwned_count = m.get('PwnedCount')
        return self


class ListPwnedPasswordsResponseBody(TeaModel):
    def __init__(self, pwned_password_infos=None, request_id=None, total_count=None):
        self.pwned_password_infos = pwned_password_infos  # type: list[ListPwnedPasswordsResponseBodyPwnedPasswordInfos]
        self.request_id = request_id  # type: str
        # 返回列表长度
        self.total_count = total_count  # type: long

    def validate(self):
        if self.pwned_password_infos:
            for k in self.pwned_password_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPwnedPasswordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PwnedPasswordInfos'] = []
        if self.pwned_password_infos is not None:
            for k in self.pwned_password_infos:
                result['PwnedPasswordInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.pwned_password_infos = []
        if m.get('PwnedPasswordInfos') is not None:
            for k in m.get('PwnedPasswordInfos'):
                temp_model = ListPwnedPasswordsResponseBodyPwnedPasswordInfos()
                self.pwned_password_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPwnedPasswordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPwnedPasswordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPwnedPasswordsResponse, self).to_map()
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
            temp_model = ListPwnedPasswordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, application_external_id=None, user_id=None):
        # 应用外部Id
        self.application_external_id = application_external_id  # type: str
        # 用户id
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(self, user_display_name=None, user_id=None, user_name=None):
        self.user_display_name = user_display_name  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_display_name is not None:
            result['UserDisplayName'] = self.user_display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserDisplayName') is not None:
            self.user_display_name = m.get('UserDisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, users=None):
        self.request_id = request_id  # type: str
        # 查询结果数据总数
        self.total_count = total_count  # type: long
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


class RegisterAuthenticatorRequest(TeaModel):
    def __init__(self, application_external_id=None, authenticator_name=None, authenticator_type=None,
                 client_extend_params_json=None, client_extend_params_json_sign=None, log_params=None, registration_context=None,
                 require_challenge_base_64=None, server_extend_params_json=None, user_id=None, user_source_ip=None):
        # 应用外部Id
        self.application_external_id = application_external_id  # type: str
        # 认证器名字
        self.authenticator_name = authenticator_name  # type: str
        # 认证器类型
        self.authenticator_type = authenticator_type  # type: str
        # 客户端SDK生成认证上下文
        self.client_extend_params_json = client_extend_params_json  # type: str
        # 客户端SDK生成认证上下文签名信息
        self.client_extend_params_json_sign = client_extend_params_json_sign  # type: str
        # 用户自定义记录审计日志信息
        self.log_params = log_params  # type: str
        # 注册上下文
        self.registration_context = registration_context  # type: str
        # 会话绑定的challenge base64标识
        self.require_challenge_base_64 = require_challenge_base_64  # type: str
        # 服务端配置项，决定认证要求属性
        self.server_extend_params_json = server_extend_params_json  # type: str
        # 用户id
        self.user_id = user_id  # type: str
        # 用户端来源IP地址，用于审计
        self.user_source_ip = user_source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterAuthenticatorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.client_extend_params_json is not None:
            result['ClientExtendParamsJson'] = self.client_extend_params_json
        if self.client_extend_params_json_sign is not None:
            result['ClientExtendParamsJsonSign'] = self.client_extend_params_json_sign
        if self.log_params is not None:
            result['LogParams'] = self.log_params
        if self.registration_context is not None:
            result['RegistrationContext'] = self.registration_context
        if self.require_challenge_base_64 is not None:
            result['RequireChallengeBase64'] = self.require_challenge_base_64
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source_ip is not None:
            result['UserSourceIp'] = self.user_source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('ClientExtendParamsJson') is not None:
            self.client_extend_params_json = m.get('ClientExtendParamsJson')
        if m.get('ClientExtendParamsJsonSign') is not None:
            self.client_extend_params_json_sign = m.get('ClientExtendParamsJsonSign')
        if m.get('LogParams') is not None:
            self.log_params = m.get('LogParams')
        if m.get('RegistrationContext') is not None:
            self.registration_context = m.get('RegistrationContext')
        if m.get('RequireChallengeBase64') is not None:
            self.require_challenge_base_64 = m.get('RequireChallengeBase64')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSourceIp') is not None:
            self.user_source_ip = m.get('UserSourceIp')
        return self


class RegisterAuthenticatorResponseBody(TeaModel):
    def __init__(self, authenticator_uuid=None, request_id=None):
        # 认证器UUID
        self.authenticator_uuid = authenticator_uuid  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterAuthenticatorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterAuthenticatorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RegisterAuthenticatorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterAuthenticatorResponse, self).to_map()
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
            temp_model = RegisterAuthenticatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ServiceInvokeRequest(TeaModel):
    def __init__(self, application_external_id=None, doraemon_action=None, mobile_extend_params_json=None,
                 mobile_extend_params_json_sign=None, server_extend_params_json=None, service_code=None, test_model=None, xclient_ip=None):
        self.application_external_id = application_external_id  # type: str
        self.doraemon_action = doraemon_action  # type: str
        self.mobile_extend_params_json = mobile_extend_params_json  # type: str
        self.mobile_extend_params_json_sign = mobile_extend_params_json_sign  # type: str
        self.server_extend_params_json = server_extend_params_json  # type: str
        self.service_code = service_code  # type: str
        self.test_model = test_model  # type: bool
        self.xclient_ip = xclient_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ServiceInvokeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.doraemon_action is not None:
            result['DoraemonAction'] = self.doraemon_action
        if self.mobile_extend_params_json is not None:
            result['MobileExtendParamsJson'] = self.mobile_extend_params_json
        if self.mobile_extend_params_json_sign is not None:
            result['MobileExtendParamsJsonSign'] = self.mobile_extend_params_json_sign
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.test_model is not None:
            result['TestModel'] = self.test_model
        if self.xclient_ip is not None:
            result['XClientIp'] = self.xclient_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('DoraemonAction') is not None:
            self.doraemon_action = m.get('DoraemonAction')
        if m.get('MobileExtendParamsJson') is not None:
            self.mobile_extend_params_json = m.get('MobileExtendParamsJson')
        if m.get('MobileExtendParamsJsonSign') is not None:
            self.mobile_extend_params_json_sign = m.get('MobileExtendParamsJsonSign')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('TestModel') is not None:
            self.test_model = m.get('TestModel')
        if m.get('XClientIp') is not None:
            self.xclient_ip = m.get('XClientIp')
        return self


class ServiceInvokeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ServiceInvokeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ServiceInvokeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ServiceInvokeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ServiceInvokeResponse, self).to_map()
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
            temp_model = ServiceInvokeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthenticatorAttributeRequest(TeaModel):
    def __init__(self, application_external_id=None, authenticator_name=None, authenticator_uuid=None,
                 user_id=None):
        # 应用外部Id
        self.application_external_id = application_external_id  # type: str
        # 认证器名字
        self.authenticator_name = authenticator_name  # type: str
        # 认证器uuid
        self.authenticator_uuid = authenticator_uuid  # type: str
        # 用户id
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuthenticatorAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateAuthenticatorAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuthenticatorAttributeResponseBody, self).to_map()
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


class UpdateAuthenticatorAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAuthenticatorAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAuthenticatorAttributeResponse, self).to_map()
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
            temp_model = UpdateAuthenticatorAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyUserAuthenticationRequest(TeaModel):
    def __init__(self, application_external_id=None, authentication_context=None, authenticator_type=None,
                 client_extend_params_json=None, client_extend_params_json_sign=None, log_params=None, log_tag=None,
                 require_bind_hash_base_64=None, require_challenge_base_64=None, server_extend_params_json=None, user_id=None,
                 user_source_ip=None):
        # 应用外部Id
        self.application_external_id = application_external_id  # type: str
        # 认证上下文，由AuthenticatorType决定格式
        self.authentication_context = authentication_context  # type: str
        # 认证器类型
        self.authenticator_type = authenticator_type  # type: str
        # 客户端SDK生成认证上下文
        self.client_extend_params_json = client_extend_params_json  # type: str
        # 客户端SDK生成认证上下文签名信息
        self.client_extend_params_json_sign = client_extend_params_json_sign  # type: str
        # 用户自定义记录审计日志信息
        self.log_params = log_params  # type: str
        # 用户自定义记录审计日志标签
        self.log_tag = log_tag  # type: str
        # 认证绑定的操作hash base64标识
        self.require_bind_hash_base_64 = require_bind_hash_base_64  # type: str
        # 会话绑定的challenge base64标识
        self.require_challenge_base_64 = require_challenge_base_64  # type: str
        # 服务端配置项，决定认证要求属性
        self.server_extend_params_json = server_extend_params_json  # type: str
        # 用户id
        self.user_id = user_id  # type: str
        # 用户端来源IP地址，用于审计
        self.user_source_ip = user_source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyUserAuthenticationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authentication_context is not None:
            result['AuthenticationContext'] = self.authentication_context
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.client_extend_params_json is not None:
            result['ClientExtendParamsJson'] = self.client_extend_params_json
        if self.client_extend_params_json_sign is not None:
            result['ClientExtendParamsJsonSign'] = self.client_extend_params_json_sign
        if self.log_params is not None:
            result['LogParams'] = self.log_params
        if self.log_tag is not None:
            result['LogTag'] = self.log_tag
        if self.require_bind_hash_base_64 is not None:
            result['RequireBindHashBase64'] = self.require_bind_hash_base_64
        if self.require_challenge_base_64 is not None:
            result['RequireChallengeBase64'] = self.require_challenge_base_64
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source_ip is not None:
            result['UserSourceIp'] = self.user_source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticationContext') is not None:
            self.authentication_context = m.get('AuthenticationContext')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('ClientExtendParamsJson') is not None:
            self.client_extend_params_json = m.get('ClientExtendParamsJson')
        if m.get('ClientExtendParamsJsonSign') is not None:
            self.client_extend_params_json_sign = m.get('ClientExtendParamsJsonSign')
        if m.get('LogParams') is not None:
            self.log_params = m.get('LogParams')
        if m.get('LogTag') is not None:
            self.log_tag = m.get('LogTag')
        if m.get('RequireBindHashBase64') is not None:
            self.require_bind_hash_base_64 = m.get('RequireBindHashBase64')
        if m.get('RequireChallengeBase64') is not None:
            self.require_challenge_base_64 = m.get('RequireChallengeBase64')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSourceIp') is not None:
            self.user_source_ip = m.get('UserSourceIp')
        return self


class VerifyUserAuthenticationResponseBodyAuthenticateResultInfo(TeaModel):
    def __init__(self, bind_hash_base_64=None, credential_id=None, user_id=None):
        # 这次认证绑定的操作hash
        self.bind_hash_base_64 = bind_hash_base_64  # type: str
        # 认证使用的凭据Id
        self.credential_id = credential_id  # type: str
        # 认证通过的用户Id
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyUserAuthenticationResponseBodyAuthenticateResultInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_hash_base_64 is not None:
            result['BindHashBase64'] = self.bind_hash_base_64
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindHashBase64') is not None:
            self.bind_hash_base_64 = m.get('BindHashBase64')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class VerifyUserAuthenticationResponseBody(TeaModel):
    def __init__(self, authenticate_result_info=None, request_id=None, verify_result=None):
        # 认证结果
        self.authenticate_result_info = authenticate_result_info  # type: VerifyUserAuthenticationResponseBodyAuthenticateResultInfo
        self.request_id = request_id  # type: str
        # 认证结果，true or false
        self.verify_result = verify_result  # type: bool

    def validate(self):
        if self.authenticate_result_info:
            self.authenticate_result_info.validate()

    def to_map(self):
        _map = super(VerifyUserAuthenticationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authenticate_result_info is not None:
            result['AuthenticateResultInfo'] = self.authenticate_result_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthenticateResultInfo') is not None:
            temp_model = VerifyUserAuthenticationResponseBodyAuthenticateResultInfo()
            self.authenticate_result_info = temp_model.from_map(m['AuthenticateResultInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class VerifyUserAuthenticationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifyUserAuthenticationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyUserAuthenticationResponse, self).to_map()
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
            temp_model = VerifyUserAuthenticationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


