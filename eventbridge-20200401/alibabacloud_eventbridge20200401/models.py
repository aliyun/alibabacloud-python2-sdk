# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateApiDestinationRequestHttpApiParameters(TeaModel):
    def __init__(self, endpoint=None, method=None):
        # The endpoint of the API destination. The endpoint can be up to 127 characters in length.
        self.endpoint = endpoint  # type: str
        # The HTTP request method. Valid values:
        # 
        # *   GET
        # *   POST
        # *   HEAD
        # *   DELETE
        # *   PUT
        # *   PATCH
        self.method = method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApiDestinationRequestHttpApiParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class CreateApiDestinationRequest(TeaModel):
    def __init__(self, api_destination_name=None, connection_name=None, description=None, http_api_parameters=None):
        # The name of the API destination. The name must be 2 to 127 characters in length.
        self.api_destination_name = api_destination_name  # type: str
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # > 
        # >  Before you configure this parameter, you must call the CreateConnection operation to create a connection. Then, set this parameter to the name of the connection that you created.
        self.connection_name = connection_name  # type: str
        # The description of the API destination. The description can be up to 255 characters in length.
        self.description = description  # type: str
        # The parameters that are configured for the API destination.
        self.http_api_parameters = http_api_parameters  # type: CreateApiDestinationRequestHttpApiParameters

    def validate(self):
        if self.http_api_parameters:
            self.http_api_parameters.validate()

    def to_map(self):
        _map = super(CreateApiDestinationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.http_api_parameters is not None:
            result['HttpApiParameters'] = self.http_api_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpApiParameters') is not None:
            temp_model = CreateApiDestinationRequestHttpApiParameters()
            self.http_api_parameters = temp_model.from_map(m['HttpApiParameters'])
        return self


class CreateApiDestinationShrinkRequest(TeaModel):
    def __init__(self, api_destination_name=None, connection_name=None, description=None,
                 http_api_parameters_shrink=None):
        # The name of the API destination. The name must be 2 to 127 characters in length.
        self.api_destination_name = api_destination_name  # type: str
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # > 
        # >  Before you configure this parameter, you must call the CreateConnection operation to create a connection. Then, set this parameter to the name of the connection that you created.
        self.connection_name = connection_name  # type: str
        # The description of the API destination. The description can be up to 255 characters in length.
        self.description = description  # type: str
        # The parameters that are configured for the API destination.
        self.http_api_parameters_shrink = http_api_parameters_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApiDestinationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.http_api_parameters_shrink is not None:
            result['HttpApiParameters'] = self.http_api_parameters_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpApiParameters') is not None:
            self.http_api_parameters_shrink = m.get('HttpApiParameters')
        return self


class CreateApiDestinationResponseBodyDate(TeaModel):
    def __init__(self, api_destination_name=None):
        # The name of the API destination.
        self.api_destination_name = api_destination_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApiDestinationResponseBodyDate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        return self


class CreateApiDestinationResponseBody(TeaModel):
    def __init__(self, code=None, date=None, message=None, request_id=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The data returned if the API destination is created.
        self.date = date  # type: CreateApiDestinationResponseBodyDate
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.date:
            self.date.validate()

    def to_map(self):
        _map = super(CreateApiDestinationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.date is not None:
            result['Date'] = self.date.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Date') is not None:
            temp_model = CreateApiDestinationResponseBodyDate()
            self.date = temp_model.from_map(m['Date'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApiDestinationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApiDestinationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApiDestinationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateApiDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnectionRequestAuthParametersApiKeyAuthParameters(TeaModel):
    def __init__(self, api_key_name=None, api_key_value=None):
        # The key of the API key.
        self.api_key_name = api_key_name  # type: str
        # The value of the API key.
        self.api_key_value = api_key_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionRequestAuthParametersApiKeyAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key_name is not None:
            result['ApiKeyName'] = self.api_key_name
        if self.api_key_value is not None:
            result['ApiKeyValue'] = self.api_key_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiKeyName') is not None:
            self.api_key_name = m.get('ApiKeyName')
        if m.get('ApiKeyValue') is not None:
            self.api_key_value = m.get('ApiKeyValue')
        return self


class CreateConnectionRequestAuthParametersBasicAuthParameters(TeaModel):
    def __init__(self, password=None, username=None):
        # The password for basic authentication.
        self.password = password  # type: str
        # The username for basic authentication.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionRequestAuthParametersBasicAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateConnectionRequestAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(self, client_id=None, client_secret=None):
        # The client ID.
        self.client_id = client_id  # type: str
        # The AccessKey secret of the client.
        self.client_secret = client_secret  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionRequestAuthParametersOAuthParametersClientParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientID'] = self.client_id
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientID') is not None:
            self.client_id = m.get('ClientID')
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')
        return self


class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret  # type: str
        # The key of the request body.
        self.key = key  # type: str
        # The value of the request body.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret  # type: str
        # The key of the request header.
        self.key = key  # type: str
        # The value of the request header.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret  # type: str
        # The key of the request path.
        self.key = key  # type: str
        # The value of the request path.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters(TeaModel):
    def __init__(self, body_parameters=None, header_parameters=None, query_string_parameters=None):
        # The parameters that are configured for the request body.
        self.body_parameters = body_parameters  # type: list[CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters]
        # The parameters that are configured for the request header.
        self.header_parameters = header_parameters  # type: list[CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters]
        # The parameters that are configured for the request path.
        self.query_string_parameters = query_string_parameters  # type: list[CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters]

    def validate(self):
        if self.body_parameters:
            for k in self.body_parameters:
                if k:
                    k.validate()
        if self.header_parameters:
            for k in self.header_parameters:
                if k:
                    k.validate()
        if self.query_string_parameters:
            for k in self.query_string_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyParameters'] = []
        if self.body_parameters is not None:
            for k in self.body_parameters:
                result['BodyParameters'].append(k.to_map() if k else None)
        result['HeaderParameters'] = []
        if self.header_parameters is not None:
            for k in self.header_parameters:
                result['HeaderParameters'].append(k.to_map() if k else None)
        result['QueryStringParameters'] = []
        if self.query_string_parameters is not None:
            for k in self.query_string_parameters:
                result['QueryStringParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body_parameters = []
        if m.get('BodyParameters') is not None:
            for k in m.get('BodyParameters'):
                temp_model = CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class CreateConnectionRequestAuthParametersOAuthParameters(TeaModel):
    def __init__(self, authorization_endpoint=None, client_parameters=None, http_method=None,
                 oauth_http_parameters=None):
        # The IP address of the authorized endpoint. The default value of a column can be up to 127 characters in length.
        self.authorization_endpoint = authorization_endpoint  # type: str
        # The parameters that are configured for the client.
        self.client_parameters = client_parameters  # type: CreateConnectionRequestAuthParametersOAuthParametersClientParameters
        # The HTTP request method. Valid values:
        # 
        # *   GET
        # *   POST
        # *   HEAD
        # *   DELETE
        # *   PUT
        # *   PATCH
        self.http_method = http_method  # type: str
        # The request parameters that are configured for OAuth authentication.
        self.oauth_http_parameters = oauth_http_parameters  # type: CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters

    def validate(self):
        if self.client_parameters:
            self.client_parameters.validate()
        if self.oauth_http_parameters:
            self.oauth_http_parameters.validate()

    def to_map(self):
        _map = super(CreateConnectionRequestAuthParametersOAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_endpoint is not None:
            result['AuthorizationEndpoint'] = self.authorization_endpoint
        if self.client_parameters is not None:
            result['ClientParameters'] = self.client_parameters.to_map()
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.oauth_http_parameters is not None:
            result['OAuthHttpParameters'] = self.oauth_http_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('AuthorizationEndpoint')
        if m.get('ClientParameters') is not None:
            temp_model = CreateConnectionRequestAuthParametersOAuthParametersClientParameters()
            self.client_parameters = temp_model.from_map(m['ClientParameters'])
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('OAuthHttpParameters') is not None:
            temp_model = CreateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters()
            self.oauth_http_parameters = temp_model.from_map(m['OAuthHttpParameters'])
        return self


class CreateConnectionRequestAuthParameters(TeaModel):
    def __init__(self, api_key_auth_parameters=None, authorization_type=None, basic_auth_parameters=None,
                 oauth_parameters=None):
        # The parameters that are configured for API key authentication.
        self.api_key_auth_parameters = api_key_auth_parameters  # type: CreateConnectionRequestAuthParametersApiKeyAuthParameters
        # The authentication type. Valid values:
        # 
        # BASIC_AUTH: basic authentication.
        # 
        # Introduction: Basic authentication is a simple authentication scheme built into the HTTP protocol. When you use the HTTP protocol for communications, the authentication method that the HTTP server uses to authenticate user identities on the client is defined in the protocol. The request header is in the Authorization: Basic Base64-encoded string (Username:Password) format.
        # 
        # 1.  Username and Password are required.
        # 
        # API_KEY_AUTH: API key authentication.
        # 
        # Introduction: The request header is in the Token: Token value format.
        # 
        # *   ApiKeyName and ApiKeyValue are required.
        # 
        # OAUTH_AUTH: OAuth authentication.
        # 
        # Introduction: OAuth2.0 is an authentication mechanism. In normal cases, a system that does not use OAuth2.0 can access the resources of the server from the client. To ensure access security, access tokens are used to authenticate users in OAuth 2.0. The client must use an access token to access protected resources. This way, OAuth 2.0 protects resources from being accessed from malicious clients and improves system security.
        # 
        # *   AuthorizationEndpoint, OAuthHttpParameters, and HttpMethod are required.
        self.authorization_type = authorization_type  # type: str
        # The parameters that are configured for basic authentication.
        self.basic_auth_parameters = basic_auth_parameters  # type: CreateConnectionRequestAuthParametersBasicAuthParameters
        # The parameters that are configured for OAuth authentication.
        self.oauth_parameters = oauth_parameters  # type: CreateConnectionRequestAuthParametersOAuthParameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.oauth_parameters:
            self.oauth_parameters.validate()

    def to_map(self):
        _map = super(CreateConnectionRequestAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key_auth_parameters is not None:
            result['ApiKeyAuthParameters'] = self.api_key_auth_parameters.to_map()
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.basic_auth_parameters is not None:
            result['BasicAuthParameters'] = self.basic_auth_parameters.to_map()
        if self.oauth_parameters is not None:
            result['OAuthParameters'] = self.oauth_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiKeyAuthParameters') is not None:
            temp_model = CreateConnectionRequestAuthParametersApiKeyAuthParameters()
            self.api_key_auth_parameters = temp_model.from_map(m['ApiKeyAuthParameters'])
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('BasicAuthParameters') is not None:
            temp_model = CreateConnectionRequestAuthParametersBasicAuthParameters()
            self.basic_auth_parameters = temp_model.from_map(m['BasicAuthParameters'])
        if m.get('OAuthParameters') is not None:
            temp_model = CreateConnectionRequestAuthParametersOAuthParameters()
            self.oauth_parameters = temp_model.from_map(m['OAuthParameters'])
        return self


class CreateConnectionRequestNetworkParameters(TeaModel):
    def __init__(self, network_type=None, security_group_id=None, vpc_id=None, vswitche_id=None):
        # The network type. Valid values:
        # 
        # PublicNetwork and PrivateNetwork.
        # 
        # *   Note: If you set this parameter to PrivateNetwork, you must configure VpcId, VswitcheId, and SecurityGroupId.
        self.network_type = network_type  # type: str
        # The ID of the security group.
        self.security_group_id = security_group_id  # type: str
        # The VPC. ID
        self.vpc_id = vpc_id  # type: str
        # The vSwitch ID.
        self.vswitche_id = vswitche_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionRequestNetworkParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitche_id is not None:
            result['VswitcheId'] = self.vswitche_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitcheId') is not None:
            self.vswitche_id = m.get('VswitcheId')
        return self


class CreateConnectionRequest(TeaModel):
    def __init__(self, auth_parameters=None, connection_name=None, description=None, network_parameters=None):
        # The parameters that are configured for authentication.
        self.auth_parameters = auth_parameters  # type: CreateConnectionRequestAuthParameters
        # The name of the connection. The name must be 2 to 127 characters in length.
        self.connection_name = connection_name  # type: str
        # The description of the connection. The description can be up to 255 characters in length.
        self.description = description  # type: str
        # The parameters that are configured for the network.
        self.network_parameters = network_parameters  # type: CreateConnectionRequestNetworkParameters

    def validate(self):
        if self.auth_parameters:
            self.auth_parameters.validate()
        if self.network_parameters:
            self.network_parameters.validate()

    def to_map(self):
        _map = super(CreateConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters is not None:
            result['AuthParameters'] = self.auth_parameters.to_map()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.network_parameters is not None:
            result['NetworkParameters'] = self.network_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            temp_model = CreateConnectionRequestAuthParameters()
            self.auth_parameters = temp_model.from_map(m['AuthParameters'])
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkParameters') is not None:
            temp_model = CreateConnectionRequestNetworkParameters()
            self.network_parameters = temp_model.from_map(m['NetworkParameters'])
        return self


class CreateConnectionShrinkRequest(TeaModel):
    def __init__(self, auth_parameters_shrink=None, connection_name=None, description=None,
                 network_parameters_shrink=None):
        # The parameters that are configured for authentication.
        self.auth_parameters_shrink = auth_parameters_shrink  # type: str
        # The name of the connection. The name must be 2 to 127 characters in length.
        self.connection_name = connection_name  # type: str
        # The description of the connection. The description can be up to 255 characters in length.
        self.description = description  # type: str
        # The parameters that are configured for the network.
        self.network_parameters_shrink = network_parameters_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters_shrink is not None:
            result['AuthParameters'] = self.auth_parameters_shrink
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.network_parameters_shrink is not None:
            result['NetworkParameters'] = self.network_parameters_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            self.auth_parameters_shrink = m.get('AuthParameters')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkParameters') is not None:
            self.network_parameters_shrink = m.get('NetworkParameters')
        return self


class CreateConnectionResponseBodyData(TeaModel):
    def __init__(self, connection_name=None):
        # The connection name.
        self.connection_name = connection_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        return self


class CreateConnectionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: CreateConnectionResponseBodyData
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateConnectionResponseBody, self).to_map()
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
            temp_model = CreateConnectionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventBusRequest(TeaModel):
    def __init__(self, description=None, event_bus_name=None):
        # The description of the event bus.
        self.description = description  # type: str
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventBusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class CreateEventBusResponseBodyData(TeaModel):
    def __init__(self, event_bus_arn=None):
        # The Alibaba Cloud Resource Name (ARN) of the event bus.
        self.event_bus_arn = event_bus_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventBusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')
        return self


class CreateEventBusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: CreateEventBusResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. The value true indicates that the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEventBusResponseBody, self).to_map()
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
            temp_model = CreateEventBusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventBusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEventBusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEventBusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventSourceRequestSourceHttpEventParameters(TeaModel):
    def __init__(self, ip=None, method=None, referer=None, security_config=None, type=None):
        # The CIDR block that is used for security settings. This parameter is required only if you set SecurityConfig to ip. You can enter a CIDR block or an IP address.
        self.ip = ip  # type: list[str]
        # The HTTP request method supported by the generated webhook URL. You can select multiple values. Valid values:
        # 
        # *   GET
        # *   POST
        # *   PUT
        # *   PATCH
        # *   DELETE
        # *   HEAD
        # *   OPTIONS
        # *   TRACE
        # *   CONNECT
        self.method = method  # type: list[str]
        # The security domain name. This parameter is required only if you set SecurityConfig to referer. You can enter a domain name.
        self.referer = referer  # type: list[str]
        # The type of security settings. Valid values:
        # 
        # *   none: No configuration is required.
        # *   ip: CIDR block.
        # *   referer: security domain name.
        self.security_config = security_config  # type: str
        # The protocol type that is supported by the generated webhook URL. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # *   HTTP\&HTTPS
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSourceRequestSourceHttpEventParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.method is not None:
            result['Method'] = self.method
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.security_config is not None:
            result['SecurityConfig'] = self.security_config
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SecurityConfig') is not None:
            self.security_config = m.get('SecurityConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateEventSourceRequestSourceKafkaParameters(TeaModel):
    def __init__(self, consumer_group=None, instance_id=None, maximum_tasks=None, network=None, offset_reset=None,
                 region_id=None, security_group_id=None, topic=None, v_switch_ids=None, vpc_id=None):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group  # type: str
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id  # type: str
        # The maximum number of consumers.
        self.maximum_tasks = maximum_tasks  # type: int
        # The network. Valid values: Default and PublicNetwork. Default value: Default. The value PublicNetwork indicates a self-managed network.
        self.network = network  # type: str
        # The consumer offset.
        self.offset_reset = offset_reset  # type: str
        # The ID of the region where the Message Queue for Apache Kafka instance resides.
        self.region_id = region_id  # type: str
        # The ID of the security group to which the Message Queue for Apache Kafka instance belongs. This parameter is required only if you set Network to PublicNetwork.
        self.security_group_id = security_group_id  # type: str
        # The name of the topic on the Message Queue for Apache Kafka instance.
        self.topic = topic  # type: str
        # The ID of the vSwitch with which the Message Queue for Apache Kafka instance is associated. This parameter is required only if you set Network to PublicNetwork.
        self.v_switch_ids = v_switch_ids  # type: str
        # The ID of the VPC in which the Message Queue for Apache Kafka instance resides. This parameter is required only if you set Network to PublicNetwork.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSourceRequestSourceKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateEventSourceRequestSourceMNSParameters(TeaModel):
    def __init__(self, is_base_64decode=None, queue_name=None, region_id=None):
        # Specifies whether to enable Base64 decoding. Valid values: true and false.
        self.is_base_64decode = is_base_64decode  # type: bool
        # The name of the MNS queue.
        self.queue_name = queue_name  # type: str
        # The region where the MNS queue resides. Valid values: cn-qingdao, cn-beijing, cn-zhangjiakou, cn-huhehaote, cn-wulanchabu, cn-hangzhou, cn-shanghai, cn-shenzhen, cn-guangzhou, cn-chengdu, cn-hongkong, ap-southeast-1, ap-southeast-2, ap-southeast-3, ap-southeast-5, ap-northeast-1, eu-central-1, us-west-1, us-east-1, ap-south-1, me-east-1, and cn-north-2-gov-1.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSourceRequestSourceMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateEventSourceRequestSourceRabbitMQParameters(TeaModel):
    def __init__(self, instance_id=None, queue_name=None, region_id=None, virtual_host_name=None):
        # The ID of the Message Queue for RabbitMQ instance. For more information, see Limits.
        self.instance_id = instance_id  # type: str
        # The name of the queue on the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.queue_name = queue_name  # type: str
        # The ID of the region where the Message Queue for RabbitMQ instance resides.
        self.region_id = region_id  # type: str
        # The name of the vhost of the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.virtual_host_name = virtual_host_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSourceRequestSourceRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class CreateEventSourceRequestSourceRocketMQParameters(TeaModel):
    def __init__(self, auth_type=None, group_id=None, instance_endpoint=None, instance_id=None,
                 instance_network=None, instance_password=None, instance_security_group_id=None, instance_type=None,
                 instance_username=None, instance_vswitch_ids=None, instance_vpc_id=None, offset=None, region_id=None, tag=None,
                 timestamp=None, topic=None):
        # The authentication type. You can set this parameter to ACL or leave this parameter empty.
        self.auth_type = auth_type  # type: str
        # The ID of the consumer group on the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id  # type: str
        # The endpoint that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_endpoint = instance_endpoint  # type: str
        # The ID of the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.instance_id = instance_id  # type: str
        # None.
        self.instance_network = instance_network  # type: str
        # The password that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_password = instance_password  # type: str
        # The ID of the security group to which the Message Queue for Apache RocketMQ instance belongs.
        self.instance_security_group_id = instance_security_group_id  # type: str
        # The type of the Message Queue for Apache RocketMQ instance. Valid values:
        # 
        # *   Cloud\_4: Message Queue for Apache RocketMQ 4.0 instance.
        # *   Cloud\_5: Message Queue for Apache RocketMQ 5.0 instance.
        self.instance_type = instance_type  # type: str
        # The username that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_username = instance_username  # type: str
        # The ID of the vSwitch with which the Message Queue for Apache RocketMQ instance is associated.
        self.instance_vswitch_ids = instance_vswitch_ids  # type: str
        # The ID of the virtual private cloud (VPC) in which the Message Queue for Apache RocketMQ instance resides.
        self.instance_vpc_id = instance_vpc_id  # type: str
        # The offset from which message consumption starts. Valid values: CONSUME_FROM_LAST_OFFSET: Start message consumption from the latest offset. CONSUME_FROM_FIRST_OFFSET: Start message consumption from the earliest offset. CONSUME_FROM_TIMESTAMP: Start message consumption from the offset at the specified point in time. Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset  # type: str
        # The region where the Message Queue for Apache RocketMQ instance resides.
        self.region_id = region_id  # type: str
        # The tag that is used to filter messages.
        self.tag = tag  # type: str
        # The timestamp that specifies the time from which messages are consumed. This parameter is valid only if you set Offset to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp  # type: long
        # The name of the topic on the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSourceRequestSourceRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class CreateEventSourceRequestSourceSLSParameters(TeaModel):
    def __init__(self, consume_position=None, log_store=None, project=None, role_name=None):
        # The starting consumer offset. The value begin specifies the earliest offset, and the value end specifies the latest offset. You can also specify a time in seconds to start consumption.
        self.consume_position = consume_position  # type: str
        # The Log Service Logstore.
        self.log_store = log_store  # type: str
        # The Log Service project.
        self.project = project  # type: str
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console. For information about the permission policy of this role, see Create a custom event source of the Log Service type.
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSourceRequestSourceSLSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateEventSourceRequestSourceScheduledEventParameters(TeaModel):
    def __init__(self, schedule=None, time_zone=None, user_data=None):
        # The cron expression.
        self.schedule = schedule  # type: str
        # The time zone in which the cron expression is executed.
        self.time_zone = time_zone  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSourceRequestSourceScheduledEventParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateEventSourceRequest(TeaModel):
    def __init__(self, description=None, event_bus_name=None, event_source_name=None,
                 source_http_event_parameters=None, source_kafka_parameters=None, source_mnsparameters=None, source_rabbit_mqparameters=None,
                 source_rocket_mqparameters=None, source_slsparameters=None, source_scheduled_event_parameters=None):
        # The description of the event source.
        self.description = description  # type: str
        # The name of the event bus with which the event source is associated.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event source.
        self.event_source_name = event_source_name  # type: str
        # The parameters that are configured if the event source is HTTP events.
        self.source_http_event_parameters = source_http_event_parameters  # type: CreateEventSourceRequestSourceHttpEventParameters
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters = source_kafka_parameters  # type: CreateEventSourceRequestSourceKafkaParameters
        # The parameters that are configured if the event source is Message Service (MNS). If you specify MNS as the event source, you must configure RegionId, IsBase64Decode, and QueueName.
        self.source_mnsparameters = source_mnsparameters  # type: CreateEventSourceRequestSourceMNSParameters
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters  # type: CreateEventSourceRequestSourceRabbitMQParameters
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters = source_rocket_mqparameters  # type: CreateEventSourceRequestSourceRocketMQParameters
        # The parameters that are configured if the event source is Log Service.
        self.source_slsparameters = source_slsparameters  # type: CreateEventSourceRequestSourceSLSParameters
        # The parameters that are configured if the event source is scheduled events.
        self.source_scheduled_event_parameters = source_scheduled_event_parameters  # type: CreateEventSourceRequestSourceScheduledEventParameters

    def validate(self):
        if self.source_http_event_parameters:
            self.source_http_event_parameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()
        if self.source_scheduled_event_parameters:
            self.source_scheduled_event_parameters.validate()

    def to_map(self):
        _map = super(CreateEventSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.source_http_event_parameters is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        if self.source_scheduled_event_parameters is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('SourceHttpEventParameters') is not None:
            temp_model = CreateEventSourceRequestSourceHttpEventParameters()
            self.source_http_event_parameters = temp_model.from_map(m['SourceHttpEventParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = CreateEventSourceRequestSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = CreateEventSourceRequestSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = CreateEventSourceRequestSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = CreateEventSourceRequestSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = CreateEventSourceRequestSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        if m.get('SourceScheduledEventParameters') is not None:
            temp_model = CreateEventSourceRequestSourceScheduledEventParameters()
            self.source_scheduled_event_parameters = temp_model.from_map(m['SourceScheduledEventParameters'])
        return self


class CreateEventSourceShrinkRequest(TeaModel):
    def __init__(self, description=None, event_bus_name=None, event_source_name=None,
                 source_http_event_parameters_shrink=None, source_kafka_parameters_shrink=None, source_mnsparameters_shrink=None,
                 source_rabbit_mqparameters_shrink=None, source_rocket_mqparameters_shrink=None, source_slsparameters_shrink=None,
                 source_scheduled_event_parameters_shrink=None):
        # The description of the event source.
        self.description = description  # type: str
        # The name of the event bus with which the event source is associated.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event source.
        self.event_source_name = event_source_name  # type: str
        # The parameters that are configured if the event source is HTTP events.
        self.source_http_event_parameters_shrink = source_http_event_parameters_shrink  # type: str
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters_shrink = source_kafka_parameters_shrink  # type: str
        # The parameters that are configured if the event source is Message Service (MNS). If you specify MNS as the event source, you must configure RegionId, IsBase64Decode, and QueueName.
        self.source_mnsparameters_shrink = source_mnsparameters_shrink  # type: str
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters_shrink = source_rabbit_mqparameters_shrink  # type: str
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters_shrink = source_rocket_mqparameters_shrink  # type: str
        # The parameters that are configured if the event source is Log Service.
        self.source_slsparameters_shrink = source_slsparameters_shrink  # type: str
        # The parameters that are configured if the event source is scheduled events.
        self.source_scheduled_event_parameters_shrink = source_scheduled_event_parameters_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSourceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.source_http_event_parameters_shrink is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters_shrink
        if self.source_kafka_parameters_shrink is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters_shrink
        if self.source_mnsparameters_shrink is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters_shrink
        if self.source_rabbit_mqparameters_shrink is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters_shrink
        if self.source_rocket_mqparameters_shrink is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters_shrink
        if self.source_slsparameters_shrink is not None:
            result['SourceSLSParameters'] = self.source_slsparameters_shrink
        if self.source_scheduled_event_parameters_shrink is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('SourceHttpEventParameters') is not None:
            self.source_http_event_parameters_shrink = m.get('SourceHttpEventParameters')
        if m.get('SourceKafkaParameters') is not None:
            self.source_kafka_parameters_shrink = m.get('SourceKafkaParameters')
        if m.get('SourceMNSParameters') is not None:
            self.source_mnsparameters_shrink = m.get('SourceMNSParameters')
        if m.get('SourceRabbitMQParameters') is not None:
            self.source_rabbit_mqparameters_shrink = m.get('SourceRabbitMQParameters')
        if m.get('SourceRocketMQParameters') is not None:
            self.source_rocket_mqparameters_shrink = m.get('SourceRocketMQParameters')
        if m.get('SourceSLSParameters') is not None:
            self.source_slsparameters_shrink = m.get('SourceSLSParameters')
        if m.get('SourceScheduledEventParameters') is not None:
            self.source_scheduled_event_parameters_shrink = m.get('SourceScheduledEventParameters')
        return self


class CreateEventSourceResponseBodyData(TeaModel):
    def __init__(self, event_source_arn=None):
        # The Alibaba Cloud Resource Name (ARN) of the resource.
        self.event_source_arn = event_source_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_arn is not None:
            result['EventSourceARN'] = self.event_source_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventSourceARN') is not None:
            self.event_source_arn = m.get('EventSourceARN')
        return self


class CreateEventSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned response code. Valid values:
        # 
        # *   Success: The request is successful.
        # *   Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: CreateEventSourceResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEventSourceResponseBody, self).to_map()
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
            temp_model = CreateEventSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEventSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEventSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventStreamingRequestRunOptionsBatchWindow(TeaModel):
    def __init__(self, count_based_window=None, time_based_window=None):
        # The maximum number of events that is allowed in the batch window. When this threshold is reached, data in the window is pushed to the downstream service. If multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.count_based_window = count_based_window  # type: int
        # The maximum period of time during which events are allowed in the batch window. Unit: seconds. When this threshold is reached, data in the window is pushed to the downstream service. If multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.time_based_window = time_based_window  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestRunOptionsBatchWindow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class CreateEventStreamingRequestRunOptionsDeadLetterQueue(TeaModel):
    def __init__(self, arn=None):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue.
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestRunOptionsDeadLetterQueue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class CreateEventStreamingRequestRunOptionsRetryStrategy(TeaModel):
    def __init__(self, maximum_event_age_in_seconds=None, maximum_retry_attempts=None, push_retry_strategy=None):
        # The maximum timeout period for a retry.
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds  # type: long
        # The maximum number of retries.
        self.maximum_retry_attempts = maximum_retry_attempts  # type: long
        # The retry policy. Valid values:
        # 
        # *   BACKOFF_RETRY
        # *   EXPONENTIAL_DECAY_RETRY
        self.push_retry_strategy = push_retry_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestRunOptionsRetryStrategy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class CreateEventStreamingRequestRunOptions(TeaModel):
    def __init__(self, batch_window=None, dead_letter_queue=None, errors_tolerance=None, maximum_tasks=None,
                 retry_strategy=None):
        # The batch window.
        self.batch_window = batch_window  # type: CreateEventStreamingRequestRunOptionsBatchWindow
        # Specifies whether to enable dead-letter queues. By default, dead-letter queues are disabled. Messages that fail to be pushed are discarded after the maximum number of retries that is specified by the retry policy is reached.
        self.dead_letter_queue = dead_letter_queue  # type: CreateEventStreamingRequestRunOptionsDeadLetterQueue
        # The exception tolerance policy. Valid values:
        # 
        # *   NONE: does not tolerate exceptions.
        # *   ALL: tolerates all exceptions.
        self.errors_tolerance = errors_tolerance  # type: str
        # The maximum number of concurrent threads.
        self.maximum_tasks = maximum_tasks  # type: long
        # The retry policy that you want to use if events fail to be pushed.
        self.retry_strategy = retry_strategy  # type: CreateEventStreamingRequestRunOptionsRetryStrategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestRunOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = CreateEventStreamingRequestRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = CreateEventStreamingRequestRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = CreateEventStreamingRequestRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The BLOB topic.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkDataHubParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersProject(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The name of the DataHub project.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkDataHubParametersProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersRoleName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The role name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkDataHubParametersRoleName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The name of the DataHub topic.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkDataHubParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The TUBLE topic.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParametersTopicType(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The topic type. Valid values:
        # 
        # *   TUPLE
        # *   BLOB
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkDataHubParametersTopicType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkDataHubParameters(TeaModel):
    def __init__(self, body=None, project=None, role_name=None, topic=None, topic_schema=None, topic_type=None):
        # The BLOB topic.
        self.body = body  # type: CreateEventStreamingRequestSinkSinkDataHubParametersBody
        # The name of the DataHub project.
        self.project = project  # type: CreateEventStreamingRequestSinkSinkDataHubParametersProject
        # The role name.
        self.role_name = role_name  # type: CreateEventStreamingRequestSinkSinkDataHubParametersRoleName
        # The name of the DataHub topic.
        self.topic = topic  # type: CreateEventStreamingRequestSinkSinkDataHubParametersTopic
        # The TUBLE topic.
        self.topic_schema = topic_schema  # type: CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema
        # The topic type. Valid values:
        # 
        # *   TUPLE
        # *   BLOB
        self.topic_type = topic_type  # type: CreateEventStreamingRequestSinkSinkDataHubParametersTopicType

    def validate(self):
        if self.body:
            self.body.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()
        if self.topic_schema:
            self.topic_schema.validate()
        if self.topic_type:
            self.topic_type.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkDataHubParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.topic_schema is not None:
            result['TopicSchema'] = self.topic_schema.to_map()
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Project') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('TopicSchema') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersTopicSchema()
            self.topic_schema = temp_model.from_map(m['TopicSchema'])
        if m.get('TopicType') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParametersTopicType()
            self.topic_type = temp_model.from_map(m['TopicType'])
        return self


class CreateEventStreamingRequestSinkSinkFcParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFcParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersConcurrency(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The delivery concurrency. Minimum value: 1.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFcParametersConcurrency, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The function name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFcParametersFunctionName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The invocation method. Valid values: Sync and Async.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFcParametersInvocationType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersQualifier(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The service version.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFcParametersQualifier, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParametersServiceName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The service name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFcParametersServiceName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFcParameters(TeaModel):
    def __init__(self, body=None, concurrency=None, function_name=None, invocation_type=None, qualifier=None,
                 service_name=None):
        # The message body that you want to deliver to Function Compute.
        self.body = body  # type: CreateEventStreamingRequestSinkSinkFcParametersBody
        # The delivery concurrency. Minimum value: 1.
        self.concurrency = concurrency  # type: CreateEventStreamingRequestSinkSinkFcParametersConcurrency
        # The function name.
        self.function_name = function_name  # type: CreateEventStreamingRequestSinkSinkFcParametersFunctionName
        # The invocation method. Valid values: Sync and Async.
        self.invocation_type = invocation_type  # type: CreateEventStreamingRequestSinkSinkFcParametersInvocationType
        # The service version.
        self.qualifier = qualifier  # type: CreateEventStreamingRequestSinkSinkFcParametersQualifier
        # The service name.
        self.service_name = service_name  # type: CreateEventStreamingRequestSinkSinkFcParametersServiceName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.concurrency:
            self.concurrency.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFcParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Concurrency') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m['Concurrency'])
        if m.get('FunctionName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class CreateEventStreamingRequestSinkSinkFnfParametersExecutionName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The execution name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFnfParametersExecutionName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFnfParametersFlowName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The flow name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFnfParametersFlowName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFnfParametersInput(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The input information of the execution.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFnfParametersInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFnfParametersRoleName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The role name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFnfParametersRoleName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkFnfParameters(TeaModel):
    def __init__(self, execution_name=None, flow_name=None, input=None, role_name=None):
        # The execution name.
        self.execution_name = execution_name  # type: CreateEventStreamingRequestSinkSinkFnfParametersExecutionName
        # The flow name.
        self.flow_name = flow_name  # type: CreateEventStreamingRequestSinkSinkFnfParametersFlowName
        # The input information of the execution.
        self.input = input  # type: CreateEventStreamingRequestSinkSinkFnfParametersInput
        # The role name.
        self.role_name = role_name  # type: CreateEventStreamingRequestSinkSinkFnfParametersRoleName

    def validate(self):
        if self.execution_name:
            self.execution_name.validate()
        if self.flow_name:
            self.flow_name.validate()
        if self.input:
            self.input.validate()
        if self.role_name:
            self.role_name.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkFnfParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name.to_map()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name.to_map()
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m['ExecutionName'])
        if m.get('FlowName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m['FlowName'])
        if m.get('Input') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('RoleName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The ACK mode.
        # 
        # *   If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high.
        # *   If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader.
        # *   If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkKafkaParametersAcks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The instance ID.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersKey(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The message key.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkKafkaParametersKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The topic name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkKafkaParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParametersValue(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkKafkaParametersValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkKafkaParameters(TeaModel):
    def __init__(self, acks=None, instance_id=None, key=None, topic=None, value=None):
        # The acknowledgement (ACK) mode.
        # 
        # *   If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high.
        # *   If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader.
        # *   If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
        self.acks = acks  # type: CreateEventStreamingRequestSinkSinkKafkaParametersAcks
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id  # type: CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId
        # The message key.
        self.key = key  # type: CreateEventStreamingRequestSinkSinkKafkaParametersKey
        # The topic name.
        self.topic = topic  # type: CreateEventStreamingRequestSinkSinkKafkaParametersTopic
        # The message body.
        self.value = value  # type: CreateEventStreamingRequestSinkSinkKafkaParametersValue

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class CreateEventStreamingRequestSinkSinkMNSParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkMNSParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # Specifies that Base64 encoding is enabled.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The name of the MNS queue.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkMNSParametersQueueName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkMNSParameters(TeaModel):
    def __init__(self, body=None, is_base_64encode=None, queue_name=None):
        # The message body.
        self.body = body  # type: CreateEventStreamingRequestSinkSinkMNSParametersBody
        # Specifies whether to enable Base64 encoding.
        self.is_base_64encode = is_base_64encode  # type: CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode
        # The name of the MNS queue.
        self.queue_name = queue_name  # type: CreateEventStreamingRequestSinkSinkMNSParametersQueueName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRabbitMQParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The name of the exchange on the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The ID of the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The name of the queue on the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The rule that you want to use to route messages.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The type of the resource to which you want to deliver events. Valid values:
        # 
        # *   Exchange
        # *   Queue
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The name of the vhost of the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRabbitMQParameters(TeaModel):
    def __init__(self, body=None, exchange=None, instance_id=None, message_id=None, properties=None, queue_name=None,
                 routing_key=None, target_type=None, virtual_host_name=None):
        # The message body.
        self.body = body  # type: CreateEventStreamingRequestSinkSinkRabbitMQParametersBody
        # The exchange to which you want to deliver events. This parameter is available only if you set TargetType to Exchange.
        self.exchange = exchange  # type: CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange
        # The information about the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id  # type: CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId
        # The message ID.
        self.message_id = message_id  # type: CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId
        # The properties that you want to use to filter messages.
        self.properties = properties  # type: CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties
        # The queue to which you want to deliver events. This parameter is available only if you set TargetType to Queue.
        self.queue_name = queue_name  # type: CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName
        # The rule that you want to use to route messages. This parameter is available only if you set TargetType to Exchange.
        self.routing_key = routing_key  # type: CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey
        # The type of the resource to which you want to deliver events.
        self.target_type = target_type  # type: CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType
        # The name of the vhost of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name  # type: CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The instance endpoint.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The instance password.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The instance type.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The instance username.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The network type. Valid values:
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The security group ID.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The name of the topic on the Message Queue for Apache RocketMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The vSwitch ID.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The VPC ID.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkRocketMQParameters(TeaModel):
    def __init__(self, body=None, instance_endpoint=None, instance_id=None, instance_password=None,
                 instance_type=None, instance_username=None, keys=None, network=None, properties=None, security_group_id=None,
                 tags=None, topic=None, v_switch_ids=None, vpc_id=None):
        # The message body.
        self.body = body  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersBody
        # The instance endpoint.
        self.instance_endpoint = instance_endpoint  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint
        # The parameters that are configured if you specify the event target as Message Queue for Apache RocketMQ.
        self.instance_id = instance_id  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId
        # The instance password.
        self.instance_password = instance_password  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword
        # The instance type.
        self.instance_type = instance_type  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType
        # The instance username.
        self.instance_username = instance_username  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername
        # The keys that you want to use to filter messages.
        self.keys = keys  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersKeys
        # The network type. Valid values:
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
        self.network = network  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork
        # The properties that you want to use to filter messages.
        self.properties = properties  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersProperties
        # The security group ID.
        self.security_group_id = security_group_id  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId
        # The tags that you want to use to filter messages.
        self.tags = tags  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersTags
        # The topic on the Message Queue for Apache RocketMQ instance.
        self.topic = topic  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersTopic
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds
        # The VPC ID.
        self.vpc_id = vpc_id  # type: CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_endpoint:
            self.instance_endpoint.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.instance_password:
            self.instance_password.validate()
        if self.instance_type:
            self.instance_type.validate()
        if self.instance_username:
            self.instance_username.validate()
        if self.keys:
            self.keys.validate()
        if self.network:
            self.network.validate()
        if self.properties:
            self.properties.validate()
        if self.security_group_id:
            self.security_group_id.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()
        if self.vpc_id:
            self.vpc_id.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password.to_map()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type.to_map()
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceEndpoint') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceEndpoint()
            self.instance_endpoint = temp_model.from_map(m['InstanceEndpoint'])
        if m.get('InstanceId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('InstancePassword') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstancePassword()
            self.instance_password = temp_model.from_map(m['InstancePassword'])
        if m.get('InstanceType') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceType()
            self.instance_type = temp_model.from_map(m['InstanceType'])
        if m.get('InstanceUsername') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersInstanceUsername()
            self.instance_username = temp_model.from_map(m['InstanceUsername'])
        if m.get('Keys') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Network') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('Properties') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('SecurityGroupId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersSecurityGroupId()
            self.security_group_id = temp_model.from_map(m['SecurityGroupId'])
        if m.get('Tags') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('VSwitchIds') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m['VSwitchIds'])
        if m.get('VpcId') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParametersVpcId()
            self.vpc_id = temp_model.from_map(m['VpcId'])
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events.
        self.form = form  # type: str
        # The template based on which you want to transform events.
        self.template = template  # type: str
        # The value before transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkSLSParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The Simple Log Service Logstore.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkSLSParametersLogStore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersProject(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The Simple Log Service project.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkSLSParametersProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkSLSParametersRoleName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The format into which you want to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The topic that you want to use to store logs. This parameter corresponds to the **topic** reserved field in Simple Log Service.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkSLSParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateEventStreamingRequestSinkSinkSLSParameters(TeaModel):
    def __init__(self, body=None, log_store=None, project=None, role_name=None, topic=None):
        # The message body that you want to deliver to Simple Log Service.
        self.body = body  # type: CreateEventStreamingRequestSinkSinkSLSParametersBody
        # The Simple Log Service Logstore.
        self.log_store = log_store  # type: CreateEventStreamingRequestSinkSinkSLSParametersLogStore
        # The Simple Log Service project.
        self.project = project  # type: CreateEventStreamingRequestSinkSinkSLSParametersProject
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name  # type: CreateEventStreamingRequestSinkSinkSLSParametersRoleName
        # The topic that you want to use to store logs. This parameter corresponds to the **topic** reserved field in Simple Log Service.
        self.topic = topic  # type: CreateEventStreamingRequestSinkSinkSLSParametersTopic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestSinkSinkSLSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class CreateEventStreamingRequestSink(TeaModel):
    def __init__(self, sink_data_hub_parameters=None, sink_fc_parameters=None, sink_fnf_parameters=None,
                 sink_kafka_parameters=None, sink_mnsparameters=None, sink_rabbit_mqparameters=None, sink_rocket_mqparameters=None,
                 sink_slsparameters=None):
        # The parameters that are configured if you specify the event target as DataHub.
        self.sink_data_hub_parameters = sink_data_hub_parameters  # type: CreateEventStreamingRequestSinkSinkDataHubParameters
        # The parameters that are configured if you specify the event target as Function Compute.
        self.sink_fc_parameters = sink_fc_parameters  # type: CreateEventStreamingRequestSinkSinkFcParameters
        # The parameters that are configured if you specify the event target as Serverless Workflow.
        self.sink_fnf_parameters = sink_fnf_parameters  # type: CreateEventStreamingRequestSinkSinkFnfParameters
        # The parameters that are configured if you specify the event target as Message Queue for Apache Kafka.
        self.sink_kafka_parameters = sink_kafka_parameters  # type: CreateEventStreamingRequestSinkSinkKafkaParameters
        # The parameters that are configured if you specify the event target as MNS.
        self.sink_mnsparameters = sink_mnsparameters  # type: CreateEventStreamingRequestSinkSinkMNSParameters
        # The parameters that are configured if you specify the event target as Message Queue for RabbitMQ.
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters  # type: CreateEventStreamingRequestSinkSinkRabbitMQParameters
        # The parameters that are configured if you specify the event target as Message Queue for Apache RocketMQ.
        self.sink_rocket_mqparameters = sink_rocket_mqparameters  # type: CreateEventStreamingRequestSinkSinkRocketMQParameters
        # The parameters that are configured if you specify the event target as Simple Log Service.
        self.sink_slsparameters = sink_slsparameters  # type: CreateEventStreamingRequestSinkSinkSLSParameters

    def validate(self):
        if self.sink_data_hub_parameters:
            self.sink_data_hub_parameters.validate()
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_fnf_parameters:
            self.sink_fnf_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestSink, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_data_hub_parameters is not None:
            result['SinkDataHubParameters'] = self.sink_data_hub_parameters.to_map()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_fnf_parameters is not None:
            result['SinkFnfParameters'] = self.sink_fnf_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SinkDataHubParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkDataHubParameters()
            self.sink_data_hub_parameters = temp_model.from_map(m['SinkDataHubParameters'])
        if m.get('SinkFcParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkFnfParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m['SinkFnfParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = CreateEventStreamingRequestSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class CreateEventStreamingRequestSourceSourceDTSParameters(TeaModel):
    def __init__(self, broker_url=None, init_check_point=None, password=None, sid=None, task_id=None, topic=None,
                 username=None):
        # The URL and port number of the data subscription channel.
        self.broker_url = broker_url  # type: str
        # The consumer offset. It is the timestamp that indicates when the SDK client consumes the first data record.
        self.init_check_point = init_check_point  # type: long
        # The consumer group password.
        self.password = password  # type: str
        # The consumer group ID.
        self.sid = sid  # type: str
        # The task ID.
        self.task_id = task_id  # type: str
        # The topic to which you want to subscribe by using the data subscription channel.
        self.topic = topic  # type: str
        # The consumer group username.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSourceSourceDTSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateEventStreamingRequestSourceSourceKafkaParameters(TeaModel):
    def __init__(self, consumer_group=None, instance_id=None, network=None, offset_reset=None, region_id=None,
                 security_group_id=None, topic=None, v_switch_ids=None, vpc_id=None):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The network type. Default value: Default. The value PublicNetwork specifies virtual private clouds (VPCs).
        self.network = network  # type: str
        # The offset.
        self.offset_reset = offset_reset  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The security group ID.
        self.security_group_id = security_group_id  # type: str
        # The topic name.
        self.topic = topic  # type: str
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids  # type: str
        # The VPC ID.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSourceSourceKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateEventStreamingRequestSourceSourceMNSParameters(TeaModel):
    def __init__(self, is_base_64decode=None, queue_name=None, region_id=None):
        # Specifies whether to enable Base64 encoding. Default value: true.
        self.is_base_64decode = is_base_64decode  # type: bool
        # The queue name.
        self.queue_name = queue_name  # type: str
        # The region ID.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSourceSourceMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateEventStreamingRequestSourceSourceMQTTParameters(TeaModel):
    def __init__(self, instance_id=None, region_id=None, topic=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The topic in which messages are stored.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSourceSourceMQTTParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class CreateEventStreamingRequestSourceSourceRabbitMQParameters(TeaModel):
    def __init__(self, instance_id=None, queue_name=None, region_id=None, virtual_host_name=None):
        # The ID of the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The name of the queue on the Message Queue for RabbitMQ instance.
        self.queue_name = queue_name  # type: str
        # The region ID. You can call the [describeregions](~~62010~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The name of the vhost of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSourceSourceRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class CreateEventStreamingRequestSourceSourceRocketMQParameters(TeaModel):
    def __init__(self, auth_type=None, filter_sql=None, filter_type=None, group_id=None, instance_endpoint=None,
                 instance_id=None, instance_network=None, instance_password=None, instance_security_group_id=None,
                 instance_type=None, instance_username=None, instance_vswitch_ids=None, instance_vpc_id=None, network=None,
                 offset=None, region_id=None, security_group_id=None, tag=None, timestamp=None, topic=None,
                 v_switch_ids=None, vpc_id=None):
        # The authentication method.
        self.auth_type = auth_type  # type: str
        # The SQL statement that is used to filter messages.
        self.filter_sql = filter_sql  # type: str
        # The message filter type.
        self.filter_type = filter_type  # type: str
        # The ID of the consumer group on the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id  # type: str
        # The instance endpoint.
        self.instance_endpoint = instance_endpoint  # type: str
        # The region where the Message Queue for Apache RocketMQ instance resides.
        self.instance_id = instance_id  # type: str
        # The network type of the instance. Valid values:
        # 
        # *   PublicNetwork
        # *   PrivateNetwork
        self.instance_network = instance_network  # type: str
        # The instance password.
        self.instance_password = instance_password  # type: str
        # The security group ID of the instance.
        self.instance_security_group_id = instance_security_group_id  # type: str
        # The instance type.
        self.instance_type = instance_type  # type: str
        # The instance username.
        self.instance_username = instance_username  # type: str
        # The vSwitch ID of the instance.
        self.instance_vswitch_ids = instance_vswitch_ids  # type: str
        # The VPC ID of the instance.
        self.instance_vpc_id = instance_vpc_id  # type: str
        # The network type. Valid values: PublicNetwork and PrivateNetwork.
        self.network = network  # type: str
        # The offset from which message consumption starts. Valid values:
        # 
        # *   CONSUME_FROM_LAST_OFFSET: Start message consumption from the latest offset.
        # *   CONSUME_FROM_FIRST_OFFSET: Start message consumption from the earliest offset.
        # *   CONSUME_FROM_TIMESTAMP: Start message consumption from the offset at the specified point in time.
        # 
        # Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The security group of the cross-border task.
        self.security_group_id = security_group_id  # type: str
        # The tag that is used to filter messages.
        self.tag = tag  # type: str
        # The timestamp that specifies the time from which messages are consumed. This parameter is valid only if you set Offset to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp  # type: long
        # The name of the topic on the Message Queue for Apache RocketMQ instance.
        self.topic = topic  # type: str
        # The vSwitch ID of the cross-border task.
        self.v_switch_ids = v_switch_ids  # type: str
        # The VPC ID of the cross-border task.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSourceSourceRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.filter_sql is not None:
            result['FilterSql'] = self.filter_sql
        if self.filter_type is not None:
            result['FilterType'] = self.filter_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('FilterSql') is not None:
            self.filter_sql = m.get('FilterSql')
        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateEventStreamingRequestSourceSourceSLSParameters(TeaModel):
    def __init__(self, consume_position=None, log_store=None, project=None, role_name=None):
        # The consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start message consumption.
        self.consume_position = consume_position  # type: str
        # The Simple Log Service Logstore.
        self.log_store = log_store  # type: str
        # The Simple Log Service project.
        self.project = project  # type: str
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestSourceSourceSLSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateEventStreamingRequestSource(TeaModel):
    def __init__(self, source_dtsparameters=None, source_kafka_parameters=None, source_mnsparameters=None,
                 source_mqttparameters=None, source_rabbit_mqparameters=None, source_rocket_mqparameters=None,
                 source_slsparameters=None):
        # The parameters that are configured if you specify the event source as Data Transmission Service (DTS).
        self.source_dtsparameters = source_dtsparameters  # type: CreateEventStreamingRequestSourceSourceDTSParameters
        # The parameters that are configured if you specify the event source as Message Queue for Apache Kafka.
        self.source_kafka_parameters = source_kafka_parameters  # type: CreateEventStreamingRequestSourceSourceKafkaParameters
        # The parameters that are configured if you specify the event source as Message Service (MNS).
        self.source_mnsparameters = source_mnsparameters  # type: CreateEventStreamingRequestSourceSourceMNSParameters
        # The parameters that are configured if you specify the event source as Message Queue for MQTT.
        self.source_mqttparameters = source_mqttparameters  # type: CreateEventStreamingRequestSourceSourceMQTTParameters
        # The parameters that are configured if you specify the event source as Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters  # type: CreateEventStreamingRequestSourceSourceRabbitMQParameters
        # The parameters that are configured if you specify the event source as Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters = source_rocket_mqparameters  # type: CreateEventStreamingRequestSourceSourceRocketMQParameters
        # The parameters that are configured if you specify the event source as Simple Log Service.
        self.source_slsparameters = source_slsparameters  # type: CreateEventStreamingRequestSourceSourceSLSParameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequestSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = CreateEventStreamingRequestSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class CreateEventStreamingRequestTransforms(TeaModel):
    def __init__(self, arn=None):
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingRequestTransforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class CreateEventStreamingRequest(TeaModel):
    def __init__(self, description=None, event_streaming_name=None, filter_pattern=None, run_options=None,
                 sink=None, source=None, transforms=None):
        # The description of the event stream.
        self.description = description  # type: str
        # The name of the event stream.
        self.event_streaming_name = event_streaming_name  # type: str
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern  # type: str
        # The parameters that are configured for the runtime environment.
        self.run_options = run_options  # type: CreateEventStreamingRequestRunOptions
        # The event target. You must and can specify only one event target.
        self.sink = sink  # type: CreateEventStreamingRequestSink
        # The event provider, which is also known as the event source. You must and can specify only one event source.
        self.source = source  # type: CreateEventStreamingRequestSource
        self.transforms = transforms  # type: list[CreateEventStreamingRequestTransforms]

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()
        if self.transforms:
            for k in self.transforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEventStreamingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        result['Transforms'] = []
        if self.transforms is not None:
            for k in self.transforms:
                result['Transforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = CreateEventStreamingRequestRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = CreateEventStreamingRequestSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = CreateEventStreamingRequestSource()
            self.source = temp_model.from_map(m['Source'])
        self.transforms = []
        if m.get('Transforms') is not None:
            for k in m.get('Transforms'):
                temp_model = CreateEventStreamingRequestTransforms()
                self.transforms.append(temp_model.from_map(k))
        return self


class CreateEventStreamingShrinkRequest(TeaModel):
    def __init__(self, description=None, event_streaming_name=None, filter_pattern=None, run_options_shrink=None,
                 sink_shrink=None, source_shrink=None, transforms_shrink=None):
        # The description of the event stream.
        self.description = description  # type: str
        # The name of the event stream.
        self.event_streaming_name = event_streaming_name  # type: str
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern  # type: str
        # The parameters that are configured for the runtime environment.
        self.run_options_shrink = run_options_shrink  # type: str
        # The event target. You must and can specify only one event target.
        self.sink_shrink = sink_shrink  # type: str
        # The event provider, which is also known as the event source. You must and can specify only one event source.
        self.source_shrink = source_shrink  # type: str
        self.transforms_shrink = transforms_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options_shrink is not None:
            result['RunOptions'] = self.run_options_shrink
        if self.sink_shrink is not None:
            result['Sink'] = self.sink_shrink
        if self.source_shrink is not None:
            result['Source'] = self.source_shrink
        if self.transforms_shrink is not None:
            result['Transforms'] = self.transforms_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            self.run_options_shrink = m.get('RunOptions')
        if m.get('Sink') is not None:
            self.sink_shrink = m.get('Sink')
        if m.get('Source') is not None:
            self.source_shrink = m.get('Source')
        if m.get('Transforms') is not None:
            self.transforms_shrink = m.get('Transforms')
        return self


class CreateEventStreamingResponseBodyData(TeaModel):
    def __init__(self, event_streaming_arn=None):
        # The ARN of the event stream.
        self.event_streaming_arn = event_streaming_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventStreamingResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_arn is not None:
            result['EventStreamingARN'] = self.event_streaming_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventStreamingARN') is not None:
            self.event_streaming_arn = m.get('EventStreamingARN')
        return self


class CreateEventStreamingResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The response code. Valid values:
        # 
        # *   Success: The request is successful.
        # *   Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: CreateEventStreamingResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEventStreamingResponseBody, self).to_map()
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
            temp_model = CreateEventStreamingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventStreamingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEventStreamingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEventStreamingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleRequestEventTargetsDeadLetterQueue(TeaModel):
    def __init__(self, arn=None):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue. Events that are not processed or whose maximum retries are exceeded are written to the dead-letter queue. The ARN feature is supported by the following queue types: MNS and Message Queue for Apache RocketMQ.
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRuleRequestEventTargetsDeadLetterQueue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class CreateRuleRequestEventTargetsParamList(TeaModel):
    def __init__(self, form=None, resource_key=None, template=None, value=None):
        # The format that is used by the event target parameter. For more information, see [Limits.](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.form = form  # type: str
        # The resource parameter of the event target. For more information, see [Limits](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.resource_key = resource_key  # type: str
        # The template that is used by the event target parameter.
        self.template = template  # type: str
        # The value of the event target parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRuleRequestEventTargetsParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateRuleRequestEventTargets(TeaModel):
    def __init__(self, dead_letter_queue=None, endpoint=None, errors_tolerance=None, id=None, param_list=None,
                 push_retry_strategy=None, type=None):
        # The dead-letter queue. Events that are not processed or whose maximum retries are exceeded are written to the dead-letter queue. The dead-letter queue feature is supported by the following queue types: Message Queue for Apache RocketMQ, Message Service (MNS), Message Queue for Apache Kafka, and EventBridge.
        self.dead_letter_queue = dead_letter_queue  # type: CreateRuleRequestEventTargetsDeadLetterQueue
        # The endpoint of the event target.
        self.endpoint = endpoint  # type: str
        # The fault tolerance policy. Valid values: ALL: allows fault tolerance. If an error occurs, the event processing is not blocked. If the message fails to be sent after the maximum number of retries specified by the retry policy is reached, the message is delivered to the dead-letter queue or discarded based on your configurations. NONE: does not allow fault tolerance. If an error occurs and the message fails to be sent after the maximum number of retries specified by the retry policy is reached, the event processing is blocked.
        self.errors_tolerance = errors_tolerance  # type: str
        # The ID of the custom event target.
        self.id = id  # type: str
        # The parameters that are configured for the event target.
        self.param_list = param_list  # type: list[CreateRuleRequestEventTargetsParamList]
        # The retry policy that is used to push events. Valid values: BACKOFF_RETRY: backoff retry. If an event failed to be pushed, it can be retried up to three times. The interval between two consecutive retries is a random value between 10 and 20 seconds. EXPONENTIAL_DECAY_RETRY: exponential decay retry. If an event failed to be pushed, it can be retried up to 176 times. The interval between two consecutive retries exponentially increases to 512 seconds, and the total retry time is one day. The specific retry intervals are 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 512, ..., and 512 seconds. The interval of 512 seconds is used for 167 retries.
        self.push_retry_strategy = push_retry_strategy  # type: str
        # The type of the event target. For more information, see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.type = type  # type: str

    def validate(self):
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateRuleRequestEventTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeadLetterQueue') is not None:
            temp_model = CreateRuleRequestEventTargetsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = CreateRuleRequestEventTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateRuleRequest(TeaModel):
    def __init__(self, description=None, event_bus_name=None, event_targets=None, filter_pattern=None,
                 rule_name=None, status=None):
        # The description of the event bus.
        self.description = description  # type: str
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event targets.
        self.event_targets = event_targets  # type: list[CreateRuleRequestEventTargets]
        # The event pattern, in JSON format. Valid values: stringEqual and stringExpression. You can specify up to five expressions in the map data structure in each field.
        # 
        # You can specify up to five expressions in the map data structure in each field.
        self.filter_pattern = filter_pattern  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str
        # The status of the event rule. Valid values: ENABLE: enables the event rule. It is the default status of the event rule. DISABLE: disables the event rule.
        self.status = status  # type: str

    def validate(self):
        if self.event_targets:
            for k in self.event_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        result['EventTargets'] = []
        if self.event_targets is not None:
            for k in self.event_targets:
                result['EventTargets'].append(k.to_map() if k else None)
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        self.event_targets = []
        if m.get('EventTargets') is not None:
            for k in m.get('EventTargets'):
                temp_model = CreateRuleRequestEventTargets()
                self.event_targets.append(temp_model.from_map(k))
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateRuleShrinkRequest(TeaModel):
    def __init__(self, description=None, event_bus_name=None, event_targets_shrink=None, filter_pattern=None,
                 rule_name=None, status=None):
        # The description of the event bus.
        self.description = description  # type: str
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event targets.
        self.event_targets_shrink = event_targets_shrink  # type: str
        # The event pattern, in JSON format. Valid values: stringEqual and stringExpression. You can specify up to five expressions in the map data structure in each field.
        # 
        # You can specify up to five expressions in the map data structure in each field.
        self.filter_pattern = filter_pattern  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str
        # The status of the event rule. Valid values: ENABLE: enables the event rule. It is the default status of the event rule. DISABLE: disables the event rule.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRuleShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_targets_shrink is not None:
            result['EventTargets'] = self.event_targets_shrink
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventTargets') is not None:
            self.event_targets_shrink = m.get('EventTargets')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateRuleResponseBodyData(TeaModel):
    def __init__(self, rule_arn=None):
        # The ARN of the event rule. The ARN is used for authorization.
        self.rule_arn = rule_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: CreateRuleResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateRuleResponseBody, self).to_map()
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
            temp_model = CreateRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleForProductRequest(TeaModel):
    def __init__(self, product_name=None):
        # The name of the cloud service or the name of the service-linked role with which the cloud service is associated.
        self.product_name = product_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleForProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class CreateServiceLinkedRoleForProductResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The returned message. If the request is successful, success is returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleForProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateServiceLinkedRoleForProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceLinkedRoleForProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceLinkedRoleForProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceLinkedRoleForProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiDestinationRequest(TeaModel):
    def __init__(self, api_destination_name=None):
        # The name of the API destination.
        self.api_destination_name = api_destination_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApiDestinationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        return self


class DeleteApiDestinationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApiDestinationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApiDestinationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApiDestinationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApiDestinationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteApiDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnectionRequest(TeaModel):
    def __init__(self, connection_name=None):
        # The name of the connection that you want to delete.
        self.connection_name = connection_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        return self


class DeleteConnectionResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConnectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventBusRequest(TeaModel):
    def __init__(self, event_bus_name=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventBusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class DeleteEventBusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventBusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventBusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEventBusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEventBusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventSourceRequest(TeaModel):
    def __init__(self, event_source_name=None):
        # The name of the event source.
        self.event_source_name = event_source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        return self


class DeleteEventSourceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEventSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEventSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventStreamingRequest(TeaModel):
    def __init__(self, event_streaming_name=None):
        # The name of the event stream that you want to delete.
        self.event_streaming_name = event_streaming_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventStreamingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class DeleteEventStreamingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: bool
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventStreamingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventStreamingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEventStreamingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEventStreamingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(self, event_bus_name=None, rule_name=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event rule that you want to delete.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTargetsRequest(TeaModel):
    def __init__(self, event_bus_name=None, rule_name=None, target_ids=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str
        # The IDs of the event targets that you want to delete.
        self.target_ids = target_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTargetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')
        return self


class DeleteTargetsShrinkRequest(TeaModel):
    def __init__(self, event_bus_name=None, rule_name=None, target_ids_shrink=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str
        # The IDs of the event targets that you want to delete.
        self.target_ids_shrink = target_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTargetsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.target_ids_shrink is not None:
            result['TargetIds'] = self.target_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('TargetIds') is not None:
            self.target_ids_shrink = m.get('TargetIds')
        return self


class DeleteTargetsResponseBodyDataErrorEntries(TeaModel):
    def __init__(self, entry_id=None, error_code=None, error_message=None):
        # The ID of the event body that failed to be processed.
        self.entry_id = entry_id  # type: str
        # The returned error code.
        self.error_code = error_code  # type: str
        # The returned error message.
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTargetsResponseBodyDataErrorEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DeleteTargetsResponseBodyData(TeaModel):
    def __init__(self, error_entries=None, error_entries_count=None):
        # The information about the event body that failed to be processed.
        self.error_entries = error_entries  # type: list[DeleteTargetsResponseBodyDataErrorEntries]
        # The number of event bodies that failed to be processed. Valid values: 0: No event bodies failed to be processed. An integer other than 0: the number of event bodies that failed to be processed.
        self.error_entries_count = error_entries_count  # type: int

    def validate(self):
        if self.error_entries:
            for k in self.error_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteTargetsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorEntries'] = []
        if self.error_entries is not None:
            for k in self.error_entries:
                result['ErrorEntries'].append(k.to_map() if k else None)
        if self.error_entries_count is not None:
            result['ErrorEntriesCount'] = self.error_entries_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.error_entries = []
        if m.get('ErrorEntries') is not None:
            for k in m.get('ErrorEntries'):
                temp_model = DeleteTargetsResponseBodyDataErrorEntries()
                self.error_entries.append(temp_model.from_map(k))
        if m.get('ErrorEntriesCount') is not None:
            self.error_entries_count = m.get('ErrorEntriesCount')
        return self


class DeleteTargetsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: DeleteTargetsResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteTargetsResponseBody, self).to_map()
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
            temp_model = DeleteTargetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTargetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTargetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTargetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableRuleRequest(TeaModel):
    def __init__(self, event_bus_name=None, rule_name=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DisableRuleResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The error code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRuleRequest(TeaModel):
    def __init__(self, event_bus_name=None, rule_name=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class EnableRuleResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The error code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The error message that is returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApiDestinationRequest(TeaModel):
    def __init__(self, api_destination_name=None):
        # The name of the API destination.
        self.api_destination_name = api_destination_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApiDestinationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        return self


class GetApiDestinationResponseBodyDataHttpApiParameters(TeaModel):
    def __init__(self, endpoint=None, method=None):
        # The endpoint of the API destination.
        self.endpoint = endpoint  # type: str
        # The HTTP request method. Valid values:
        # 
        # *   POST
        # *   GET
        # *   DELETE
        # *   PUT
        # *   HEAD
        # *   TRACE
        # *   PATCH
        self.method = method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApiDestinationResponseBodyDataHttpApiParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class GetApiDestinationResponseBodyData(TeaModel):
    def __init__(self, api_destination_name=None, connection_name=None, description=None, gmt_create=None,
                 http_api_parameters=None):
        # The name of the API destination.
        self.api_destination_name = api_destination_name  # type: str
        # The connection name.
        self.connection_name = connection_name  # type: str
        # The description of the API destination.
        self.description = description  # type: str
        # The time when the API destination was created.
        self.gmt_create = gmt_create  # type: long
        # The request parameters that are configured for the API destination.
        self.http_api_parameters = http_api_parameters  # type: GetApiDestinationResponseBodyDataHttpApiParameters

    def validate(self):
        if self.http_api_parameters:
            self.http_api_parameters.validate()

    def to_map(self):
        _map = super(GetApiDestinationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.http_api_parameters is not None:
            result['HttpApiParameters'] = self.http_api_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('HttpApiParameters') is not None:
            temp_model = GetApiDestinationResponseBodyDataHttpApiParameters()
            self.http_api_parameters = temp_model.from_map(m['HttpApiParameters'])
        return self


class GetApiDestinationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: GetApiDestinationResponseBodyData
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetApiDestinationResponseBody, self).to_map()
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
            temp_model = GetApiDestinationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApiDestinationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApiDestinationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApiDestinationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetApiDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionRequest(TeaModel):
    def __init__(self, connection_name=None):
        # The connection name.
        self.connection_name = connection_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters(TeaModel):
    def __init__(self, api_key_name=None, api_key_value=None):
        # The key of the API key.
        self.api_key_name = api_key_name  # type: str
        # The value of the API key.
        self.api_key_value = api_key_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key_name is not None:
            result['ApiKeyName'] = self.api_key_name
        if self.api_key_value is not None:
            result['ApiKeyValue'] = self.api_key_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiKeyName') is not None:
            self.api_key_name = m.get('ApiKeyName')
        if m.get('ApiKeyValue') is not None:
            self.api_key_value = m.get('ApiKeyValue')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersBasicAuthParameters(TeaModel):
    def __init__(self, password=None, username=None):
        # The password of basic authentication.
        self.password = password  # type: str
        # The username of basic authentication.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnectionsAuthParametersBasicAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(self, client_id=None, client_secret=None):
        # The client ID.
        self.client_id = client_id  # type: str
        # The AccessKey secret of the client.
        self.client_secret = client_secret  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientID'] = self.client_id
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientID') is not None:
            self.client_id = m.get('ClientID')
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret  # type: str
        # The key of the request body.
        self.key = key  # type: str
        # The value of the request body.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret  # type: str
        # The key of the request header.
        self.key = key  # type: str
        # The value of the request header.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret  # type: str
        # The key of the request path.
        self.key = key  # type: str
        # The value of the request path.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters(TeaModel):
    def __init__(self, body_parameters=None, header_parameters=None, query_string_parameters=None):
        # The information about the request body.
        self.body_parameters = body_parameters  # type: list[GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters]
        # The information about the request header.
        self.header_parameters = header_parameters  # type: list[GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters]
        # The information about the request path.
        self.query_string_parameters = query_string_parameters  # type: list[GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters]

    def validate(self):
        if self.body_parameters:
            for k in self.body_parameters:
                if k:
                    k.validate()
        if self.header_parameters:
            for k in self.header_parameters:
                if k:
                    k.validate()
        if self.query_string_parameters:
            for k in self.query_string_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyParameters'] = []
        if self.body_parameters is not None:
            for k in self.body_parameters:
                result['BodyParameters'].append(k.to_map() if k else None)
        result['HeaderParameters'] = []
        if self.header_parameters is not None:
            for k in self.header_parameters:
                result['HeaderParameters'].append(k.to_map() if k else None)
        result['QueryStringParameters'] = []
        if self.query_string_parameters is not None:
            for k in self.query_string_parameters:
                result['QueryStringParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body_parameters = []
        if m.get('BodyParameters') is not None:
            for k in m.get('BodyParameters'):
                temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters(TeaModel):
    def __init__(self, authorization_endpoint=None, client_parameters=None, http_method=None,
                 oauth_http_parameters=None):
        # The endpoint that is used to obtain the OAuth token.
        self.authorization_endpoint = authorization_endpoint  # type: str
        # The information about the client.
        self.client_parameters = client_parameters  # type: GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters
        # The HTTP request method. Valid values:
        # 
        # *   GET
        # *   POST
        # *   HEAD
        self.http_method = http_method  # type: str
        # The request parameters of OAuth authentication.
        self.oauth_http_parameters = oauth_http_parameters  # type: GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters

    def validate(self):
        if self.client_parameters:
            self.client_parameters.validate()
        if self.oauth_http_parameters:
            self.oauth_http_parameters.validate()

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_endpoint is not None:
            result['AuthorizationEndpoint'] = self.authorization_endpoint
        if self.client_parameters is not None:
            result['ClientParameters'] = self.client_parameters.to_map()
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.oauth_http_parameters is not None:
            result['OAuthHttpParameters'] = self.oauth_http_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('AuthorizationEndpoint')
        if m.get('ClientParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters()
            self.client_parameters = temp_model.from_map(m['ClientParameters'])
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('OAuthHttpParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters()
            self.oauth_http_parameters = temp_model.from_map(m['OAuthHttpParameters'])
        return self


class GetConnectionResponseBodyDataConnectionsAuthParameters(TeaModel):
    def __init__(self, api_key_auth_parameters=None, authorization_type=None, basic_auth_parameters=None,
                 oauth_parameters=None):
        # The information about API key authentication.
        self.api_key_auth_parameters = api_key_auth_parameters  # type: GetConnectionResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters
        # The authentication method. Valid values:
        # 
        # *   BASIC_AUTH: basic authentication.
        # *   API_KEY_AUTH: API key authentication.
        # *   OAUTH_AUTH: OAuth authentication.
        self.authorization_type = authorization_type  # type: str
        # The information about basic authentication.
        self.basic_auth_parameters = basic_auth_parameters  # type: GetConnectionResponseBodyDataConnectionsAuthParametersBasicAuthParameters
        # The information about OAuth authentication.
        self.oauth_parameters = oauth_parameters  # type: GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.oauth_parameters:
            self.oauth_parameters.validate()

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnectionsAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key_auth_parameters is not None:
            result['ApiKeyAuthParameters'] = self.api_key_auth_parameters.to_map()
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.basic_auth_parameters is not None:
            result['BasicAuthParameters'] = self.basic_auth_parameters.to_map()
        if self.oauth_parameters is not None:
            result['OAuthParameters'] = self.oauth_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiKeyAuthParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters()
            self.api_key_auth_parameters = temp_model.from_map(m['ApiKeyAuthParameters'])
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('BasicAuthParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersBasicAuthParameters()
            self.basic_auth_parameters = temp_model.from_map(m['BasicAuthParameters'])
        if m.get('OAuthParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParametersOAuthParameters()
            self.oauth_parameters = temp_model.from_map(m['OAuthParameters'])
        return self


class GetConnectionResponseBodyDataConnectionsNetworkParameters(TeaModel):
    def __init__(self, network_type=None, security_group_id=None, vpc_id=None, vswitche_id=None):
        # *   PublicNetwork: the Internet.
        # *   PrivateNetwork: virtual private cloud (VPC).
        self.network_type = network_type  # type: str
        # The security group ID.
        self.security_group_id = security_group_id  # type: str
        # The VPC ID.
        self.vpc_id = vpc_id  # type: str
        # The vSwitch ID.
        self.vswitche_id = vswitche_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnectionsNetworkParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitche_id is not None:
            result['VswitcheId'] = self.vswitche_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitcheId') is not None:
            self.vswitche_id = m.get('VswitcheId')
        return self


class GetConnectionResponseBodyDataConnections(TeaModel):
    def __init__(self, auth_parameters=None, connection_name=None, description=None, gmt_create=None, id=None,
                 network_parameters=None):
        # The authentication methods.
        self.auth_parameters = auth_parameters  # type: GetConnectionResponseBodyDataConnectionsAuthParameters
        # The connection name.
        self.connection_name = connection_name  # type: str
        # The connection description.
        self.description = description  # type: str
        # The time when the connection was created.
        self.gmt_create = gmt_create  # type: long
        # The data source ID.
        self.id = id  # type: long
        # The information about the network.
        self.network_parameters = network_parameters  # type: GetConnectionResponseBodyDataConnectionsNetworkParameters

    def validate(self):
        if self.auth_parameters:
            self.auth_parameters.validate()
        if self.network_parameters:
            self.network_parameters.validate()

    def to_map(self):
        _map = super(GetConnectionResponseBodyDataConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters is not None:
            result['AuthParameters'] = self.auth_parameters.to_map()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.network_parameters is not None:
            result['NetworkParameters'] = self.network_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsAuthParameters()
            self.auth_parameters = temp_model.from_map(m['AuthParameters'])
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NetworkParameters') is not None:
            temp_model = GetConnectionResponseBodyDataConnectionsNetworkParameters()
            self.network_parameters = temp_model.from_map(m['NetworkParameters'])
        return self


class GetConnectionResponseBodyData(TeaModel):
    def __init__(self, connections=None):
        # The queried connections.
        self.connections = connections  # type: list[GetConnectionResponseBodyDataConnections]

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetConnectionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = GetConnectionResponseBodyDataConnections()
                self.connections.append(temp_model.from_map(k))
        return self


class GetConnectionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_code=None, message=None, request_id=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: GetConnectionResponseBodyData
        # The HTTP status code.
        self.http_code = http_code  # type: int
        # The returned message.
        self.message = message  # type: str
        # The returned request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetConnectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
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
            temp_model = GetConnectionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventBusRequest(TeaModel):
    def __init__(self, event_bus_name=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventBusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class GetEventBusResponseBodyData(TeaModel):
    def __init__(self, create_timestamp=None, description=None, event_bus_arn=None, event_bus_name=None):
        # The timestamp that indicates when the event bus was created.
        self.create_timestamp = create_timestamp  # type: long
        # The description of the event bus.
        self.description = description  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the event bus.
        self.event_bus_arn = event_bus_arn  # type: str
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventBusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class GetEventBusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: GetEventBusResponseBodyData
        # The error message that is returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEventBusResponseBody, self).to_map()
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
            temp_model = GetEventBusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEventBusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEventBusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEventBusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventStreamingRequest(TeaModel):
    def __init__(self, event_streaming_name=None):
        # The name of the event stream whose details you want to query.
        self.event_streaming_name = event_streaming_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class GetEventStreamingResponseBodyDataRunOptionsBatchWindow(TeaModel):
    def __init__(self, count_based_window=None, time_based_window=None):
        # The maximum number of events that are allowed in the batch window. If this threshold is reached, data in the window is pushed downstream. When multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.count_based_window = count_based_window  # type: int
        # The maximum period of time during which events are allowed in the batch window. Unit: seconds. If this threshold is reached, data in the window is pushed downstream. When multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.time_based_window = time_based_window  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataRunOptionsBatchWindow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue(TeaModel):
    def __init__(self, arn=None):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue.
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class GetEventStreamingResponseBodyDataRunOptionsRetryStrategy(TeaModel):
    def __init__(self, maximum_event_age_in_seconds=None, maximum_retry_attempts=None, push_retry_strategy=None):
        # The maximum period of time during which retries are performed.
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds  # type: float
        # The maximum number of retries.
        self.maximum_retry_attempts = maximum_retry_attempts  # type: float
        # The retry policy. Valid values: BACKOFFRETRY and EXPONENTIALDECAY_RETRY.
        self.push_retry_strategy = push_retry_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataRunOptionsRetryStrategy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class GetEventStreamingResponseBodyDataRunOptions(TeaModel):
    def __init__(self, batch_window=None, dead_letter_queue=None, errors_tolerance=None, maximum_tasks=None,
                 retry_strategy=None):
        # The batch window.
        self.batch_window = batch_window  # type: GetEventStreamingResponseBodyDataRunOptionsBatchWindow
        # Indicates whether dead-letter queues are enabled. By default, dead-letter queues are disabled. Messages that fail to be pushed after allowed retries as specified by the retry policy are discarded.
        self.dead_letter_queue = dead_letter_queue  # type: GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue
        # The fault tolerance policy. The value NONE specifies that faults are not tolerated, and the value All specifies that all faults are tolerated.
        self.errors_tolerance = errors_tolerance  # type: str
        # The concurrency level.
        self.maximum_tasks = maximum_tasks  # type: int
        # The information about the retry policy that is used if the event fails to be pushed.
        self.retry_strategy = retry_strategy  # type: GetEventStreamingResponseBodyDataRunOptionsRetryStrategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataRunOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFcParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersConcurrency(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The delivery concurrency. Minimum value: 1.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFcParametersConcurrency, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The function name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The invocation type.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The alias of the service to which the function belongs.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The name of the service.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFcParameters(TeaModel):
    def __init__(self, body=None, concurrency=None, function_name=None, invocation_type=None, qualifier=None,
                 service_name=None):
        # The message body that is sent to the function.
        self.body = body  # type: GetEventStreamingResponseBodyDataSinkSinkFcParametersBody
        # The delivery concurrency. Minimum value: 1.
        self.concurrency = concurrency  # type: GetEventStreamingResponseBodyDataSinkSinkFcParametersConcurrency
        # The function name.
        self.function_name = function_name  # type: GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName
        # The invocation type. Valid values: Sync: synchronous Async: asynchronous
        self.invocation_type = invocation_type  # type: GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType
        # The alias of the service to which the function belongs.
        self.qualifier = qualifier  # type: GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier
        # The service name.
        self.service_name = service_name  # type: GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.concurrency:
            self.concurrency.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFcParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Concurrency') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m['Concurrency'])
        if m.get('FunctionName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkFnfParametersExecutionName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The execution name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFnfParametersExecutionName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFnfParametersFlowName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The flow name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFnfParametersFlowName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFnfParametersInput(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The execution input information.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFnfParametersInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFnfParametersRoleName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The role configuration.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFnfParametersRoleName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkFnfParameters(TeaModel):
    def __init__(self, execution_name=None, flow_name=None, input=None, role_name=None):
        # The execution name.
        self.execution_name = execution_name  # type: GetEventStreamingResponseBodyDataSinkSinkFnfParametersExecutionName
        # The flow name.
        self.flow_name = flow_name  # type: GetEventStreamingResponseBodyDataSinkSinkFnfParametersFlowName
        # The execution input information.
        self.input = input  # type: GetEventStreamingResponseBodyDataSinkSinkFnfParametersInput
        # The role name.
        self.role_name = role_name  # type: GetEventStreamingResponseBodyDataSinkSinkFnfParametersRoleName

    def validate(self):
        if self.execution_name:
            self.execution_name.validate()
        if self.flow_name:
            self.flow_name.validate()
        if self.input:
            self.input.validate()
        if self.role_name:
            self.role_name.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkFnfParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name.to_map()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name.to_map()
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m['ExecutionName'])
        if m.get('FlowName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m['FlowName'])
        if m.get('Input') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('RoleName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The acknowledgment information.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The instance ID.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The message key.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The topic name.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkKafkaParameters(TeaModel):
    def __init__(self, acks=None, instance_id=None, key=None, topic=None, value=None):
        # The acknowledgment information.
        self.acks = acks  # type: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks
        # The target service type is Message Queue for Apache Kafka.
        self.instance_id = instance_id  # type: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId
        # The message key.
        self.key = key  # type: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey
        # The topic name.
        self.topic = topic  # type: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic
        # The message content.
        self.value = value  # type: GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('Topic') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # Specifies that Base64 encoding is enabled.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The name of the MNS queue.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkMNSParameters(TeaModel):
    def __init__(self, body=None, is_base_64encode=None, queue_name=None):
        # The message content.
        self.body = body  # type: GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody
        # Indicates whether Base64 encoding is enabled.
        self.is_base_64encode = is_base_64encode  # type: GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode
        # The target service type is MNS.
        self.queue_name = queue_name  # type: GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The name of the exchange in the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The ID of the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The name of the queue in the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The routing rule for the message.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The type of the resource to which the event is delivered. Valid values: Exchange: exchanges. Queue: queues.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The vhost name of the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters(TeaModel):
    def __init__(self, body=None, exchange=None, instance_id=None, message_id=None, properties=None, queue_name=None,
                 routing_key=None, target_type=None, virtual_host_name=None):
        # The message content.
        self.body = body  # type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody
        # The exchange mode. This parameter is available only if TargetType is set to Exchange.
        self.exchange = exchange  # type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange
        # The target service type is Message Queue for RabbitMQ instance.
        self.instance_id = instance_id  # type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId
        # The message ID.
        self.message_id = message_id  # type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId
        # The tags that are used to filter messages.
        self.properties = properties  # type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties
        # The queue mode. This parameter is available only if TargetType is set to Queue.
        self.queue_name = queue_name  # type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName
        # The routing rule for the message. This parameter is available only if TargetType is set to Exchange.
        self.routing_key = routing_key  # type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey
        # The target type.
        self.target_type = target_type  # type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType
        # The name of the vhost of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name  # type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The name of the topic in the Message Queue for Apache RocketMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters(TeaModel):
    def __init__(self, body=None, instance_id=None, keys=None, properties=None, tags=None, topic=None):
        # The message content.
        self.body = body  # type: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody
        # The target service type is Message Queue for Apache RocketMQ.
        self.instance_id = instance_id  # type: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId
        # The tags that are used to filter messages.
        self.keys = keys  # type: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys
        # The tags that are used to filter messages.
        self.properties = properties  # type: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties
        # The tags that are used to filter messages.
        self.tags = tags  # type: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags
        # The name of the topic in the Message Queue for Apache RocketMQ instance.
        self.topic = topic  # type: GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.keys:
            self.keys.validate()
        if self.properties:
            self.properties.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceId') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Keys') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Properties') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Tags') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event.
        self.form = form  # type: str
        # The template based on which the event is transformed.
        self.template = template  # type: str
        # The value before the transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The Log Service Logstore.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The Log Service project.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform the event. Default value: CONSTANT.
        self.form = form  # type: str
        # The template style.
        self.template = template  # type: str
        # The name of the topic in which logs are stored. The topic corresponds to the topic reserved field in Log Service.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEventStreamingResponseBodyDataSinkSinkSLSParameters(TeaModel):
    def __init__(self, body=None, log_store=None, project=None, role_name=None, topic=None):
        # The message content.
        self.body = body  # type: GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody
        # The Simple Log Service Logstore.
        self.log_store = log_store  # type: GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore
        # The Simple Log Service project.
        self.project = project  # type: GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name  # type: GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName
        # The name of the topic in which logs are stored. The topic corresponds to the topic reserved field in Simple Log Service.
        self.topic = topic  # type: GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSinkSinkSLSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class GetEventStreamingResponseBodyDataSink(TeaModel):
    def __init__(self, sink_fc_parameters=None, sink_fnf_parameters=None, sink_kafka_parameters=None,
                 sink_mnsparameters=None, sink_rabbit_mqparameters=None, sink_rocket_mqparameters=None, sink_slsparameters=None):
        # The parameters that are returned if the event target is Function Compute.
        self.sink_fc_parameters = sink_fc_parameters  # type: GetEventStreamingResponseBodyDataSinkSinkFcParameters
        # The Sink Fnf parameters.
        self.sink_fnf_parameters = sink_fnf_parameters  # type: GetEventStreamingResponseBodyDataSinkSinkFnfParameters
        # The parameters that are returned if the event target is Message Queue for Apache Kafka.
        self.sink_kafka_parameters = sink_kafka_parameters  # type: GetEventStreamingResponseBodyDataSinkSinkKafkaParameters
        # The parameters that are returned if the event target is Message Service (MNS).
        self.sink_mnsparameters = sink_mnsparameters  # type: GetEventStreamingResponseBodyDataSinkSinkMNSParameters
        # The parameters that are returned if the event target is Message Queue for RabbitMQ.
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters  # type: GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters
        # Sink RocketMQ Parameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters  # type: GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters
        # Sink SLS Parameters
        self.sink_slsparameters = sink_slsparameters  # type: GetEventStreamingResponseBodyDataSinkSinkSLSParameters

    def validate(self):
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_fnf_parameters:
            self.sink_fnf_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSink, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_fnf_parameters is not None:
            result['SinkFnfParameters'] = self.sink_fnf_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SinkFcParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkFnfParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m['SinkFnfParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class GetEventStreamingResponseBodyDataSourceSourceDTSParameters(TeaModel):
    def __init__(self, broker_url=None, init_check_point=None, password=None, sid=None, task_id=None, topic=None,
                 username=None):
        # The URL and port number of the data subscription channel.
        self.broker_url = broker_url  # type: str
        # The consumer offset. A consumer offset is a timestamp that indicates when the SDK client consumes the first data record. The value is a UNIX timestamp.
        self.init_check_point = init_check_point  # type: str
        # The password of the consumer group.
        self.password = password  # type: str
        # The ID of the consumer group.
        self.sid = sid  # type: str
        # The task ID.
        self.task_id = task_id  # type: str
        # The topic to which you want to subscribe by using the data subscription channel.
        self.topic = topic  # type: str
        # The account of the consumer group.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSourceSourceDTSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetEventStreamingResponseBodyDataSourceSourceKafkaParameters(TeaModel):
    def __init__(self, consumer_group=None, instance_id=None, network=None, offset_reset=None, region_id=None,
                 security_group_id=None, topic=None, v_switch_ids=None, vpc_id=None):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The network. Default value: Default. The value PublicNetwork specifies a virtual private cloud (VPC).
        self.network = network  # type: str
        # The offset.
        self.offset_reset = offset_reset  # type: str
        # The region ID of the Message Queue for Apache Kafka instance.
        self.region_id = region_id  # type: str
        # The security group ID.
        self.security_group_id = security_group_id  # type: str
        # The name of the topic.
        self.topic = topic  # type: str
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids  # type: str
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSourceSourceKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetEventStreamingResponseBodyDataSourceSourceMNSParameters(TeaModel):
    def __init__(self, is_base_64decode=None, queue_name=None, region_id=None):
        # Indicates whether Base64 encoding is enabled.
        self.is_base_64decode = is_base_64decode  # type: bool
        # The name of the MNS queue.
        self.queue_name = queue_name  # type: str
        # The region ID of the MNS queue.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSourceSourceMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetEventStreamingResponseBodyDataSourceSourceMQTTParameters(TeaModel):
    def __init__(self, instance_id=None, region_id=None, topic=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The region ID of the Message Queue for MQTT instance.
        self.region_id = region_id  # type: str
        # The name of the topic in the Message Queue for MQTT instance.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSourceSourceMQTTParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters(TeaModel):
    def __init__(self, instance_id=None, queue_name=None, region_id=None, virtual_host_name=None):
        # The ID of the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The name of the queue in the Message Queue for RabbitMQ instance.
        self.queue_name = queue_name  # type: str
        # The region ID of the Message Queue for RabbitMQ instance.
        self.region_id = region_id  # type: str
        # The vhost name of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters(TeaModel):
    def __init__(self, auth_type=None, group_id=None, instance_endpoint=None, instance_id=None,
                 instance_network=None, instance_password=None, instance_security_group_id=None, instance_type=None,
                 instance_username=None, instance_vswitch_ids=None, instance_vpc_id=None, offset=None, region_id=None, tag=None,
                 timestamp=None, topic=None):
        self.auth_type = auth_type  # type: str
        # The ID of the consumer group in the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id  # type: str
        self.instance_endpoint = instance_endpoint  # type: str
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.instance_id = instance_id  # type: str
        self.instance_network = instance_network  # type: str
        self.instance_password = instance_password  # type: str
        self.instance_security_group_id = instance_security_group_id  # type: str
        self.instance_type = instance_type  # type: str
        self.instance_username = instance_username  # type: str
        self.instance_vswitch_ids = instance_vswitch_ids  # type: str
        self.instance_vpc_id = instance_vpc_id  # type: str
        # The consumer offset of messages. Valid values: CONSUME_FROM_LAST_OFFSET: Start consumption from the latest offset. CONSUME_FROM_FIRST_OFFSET: Start consumption from the earliest offset. CONSUME_FROM_TIMESTAMP: Start consumption from the offset at the specified point in time.
        self.offset = offset  # type: str
        # The region ID of the Message Queue for Apache RocketMQ instance.
        self.region_id = region_id  # type: str
        # The tags that are used to filter messages.
        self.tag = tag  # type: str
        # The timestamp of the offset from which consumption starts. This parameter is valid only if you set the Offset parameter to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp  # type: long
        # The topic to which the message belongs.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetEventStreamingResponseBodyDataSourceSourceSLSParameters(TeaModel):
    def __init__(self, consume_position=None, consumer_group=None, log_store=None, project=None, role_name=None):
        # The starting consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start consumption.
        self.consume_position = consume_position  # type: str
        # The consumer group.
        self.consumer_group = consumer_group  # type: str
        # The Log Service Logstore.
        self.log_store = log_store  # type: str
        # The Log Service project.
        self.project = project  # type: str
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSourceSourceSLSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetEventStreamingResponseBodyDataSource(TeaModel):
    def __init__(self, source_dtsparameters=None, source_kafka_parameters=None, source_mnsparameters=None,
                 source_mqttparameters=None, source_rabbit_mqparameters=None, source_rocket_mqparameters=None,
                 source_slsparameters=None):
        # The parameters that are returned if the event source is Data Transmission Service (DTS).
        self.source_dtsparameters = source_dtsparameters  # type: GetEventStreamingResponseBodyDataSourceSourceDTSParameters
        # Source Kafka Parameters
        self.source_kafka_parameters = source_kafka_parameters  # type: GetEventStreamingResponseBodyDataSourceSourceKafkaParameters
        # Source MNS Parameters
        self.source_mnsparameters = source_mnsparameters  # type: GetEventStreamingResponseBodyDataSourceSourceMNSParameters
        # The parameters that are returned if the event source is Message Queue for MQTT.
        self.source_mqttparameters = source_mqttparameters  # type: GetEventStreamingResponseBodyDataSourceSourceMQTTParameters
        # Source RabbitMQ Parameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters  # type: GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters
        # Source RocketMQ Parameters
        self.source_rocket_mqparameters = source_rocket_mqparameters  # type: GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters
        # The parameters that are returned if the event provider is Simple Log Service.
        self.source_slsparameters = source_slsparameters  # type: GetEventStreamingResponseBodyDataSourceSourceSLSParameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = GetEventStreamingResponseBodyDataSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class GetEventStreamingResponseBodyDataTransforms(TeaModel):
    def __init__(self, arn=None):
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyDataTransforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class GetEventStreamingResponseBodyData(TeaModel):
    def __init__(self, description=None, event_streaming_name=None, filter_pattern=None, run_options=None,
                 sink=None, source=None, status=None, transforms=None):
        # The description of the event stream that is returned.
        self.description = description  # type: str
        # The name of the event stream that is returned.
        self.event_streaming_name = event_streaming_name  # type: str
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern  # type: str
        # The parameters that are configured for the runtime environment.
        self.run_options = run_options  # type: GetEventStreamingResponseBodyDataRunOptions
        # The event target.
        self.sink = sink  # type: GetEventStreamingResponseBodyDataSink
        # The event provider.
        self.source = source  # type: GetEventStreamingResponseBodyDataSource
        # The status of the event stream that is returned.
        self.status = status  # type: str
        self.transforms = transforms  # type: list[GetEventStreamingResponseBodyDataTransforms]

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()
        if self.transforms:
            for k in self.transforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['Transforms'] = []
        if self.transforms is not None:
            for k in self.transforms:
                result['Transforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = GetEventStreamingResponseBodyDataRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = GetEventStreamingResponseBodyDataSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = GetEventStreamingResponseBodyDataSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.transforms = []
        if m.get('Transforms') is not None:
            for k in m.get('Transforms'):
                temp_model = GetEventStreamingResponseBodyDataTransforms()
                self.transforms.append(temp_model.from_map(k))
        return self


class GetEventStreamingResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For a list of error codes, see Error codes.
        self.code = code  # type: str
        # The response parameters.
        self.data = data  # type: GetEventStreamingResponseBodyData
        # The error message that is returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponseBody, self).to_map()
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
            temp_model = GetEventStreamingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEventStreamingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEventStreamingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEventStreamingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleRequest(TeaModel):
    def __init__(self, event_bus_name=None, rule_name=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetRuleResponseBodyDataTargetsDeadLetterQueue(TeaModel):
    def __init__(self, arn=None):
        # The Alibaba Cloud Resource Name (ARN) of the event source.
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleResponseBodyDataTargetsDeadLetterQueue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class GetRuleResponseBodyDataTargetsParamList(TeaModel):
    def __init__(self, form=None, resource_key=None, template=None, value=None):
        # The format that is used by the event target parameter. For more information, see [Limits.](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.form = form  # type: str
        # The resource parameter of the event target. For more information, see [Limits.](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.resource_key = resource_key  # type: str
        # The template that is used by the event target parameter.
        self.template = template  # type: str
        # The value of the event target parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleResponseBodyDataTargetsParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetRuleResponseBodyDataTargets(TeaModel):
    def __init__(self, dead_letter_queue=None, detail_map=None, endpoint=None, errors_tolerance=None, id=None,
                 param_list=None, push_retry_strategy=None, push_selector=None, type=None):
        # The ID of the custom event target.
        self.dead_letter_queue = dead_letter_queue  # type: GetRuleResponseBodyDataTargetsDeadLetterQueue
        # The information about the event target.
        self.detail_map = detail_map  # type: dict[str, any]
        # The endpoint of the event target.
        self.endpoint = endpoint  # type: str
        self.errors_tolerance = errors_tolerance  # type: str
        # The ID of the custom event target.
        self.id = id  # type: str
        # The parameters that are configured for the event target.
        self.param_list = param_list  # type: list[GetRuleResponseBodyDataTargetsParamList]
        # The retry policy that is used to push events. Valid values: BACKOFF_RETRY: backoff retry. If an event failed to be pushed, it can be retried up to three times. The interval between two consecutive retries is a random value from 10 to 20. Unit: seconds. EXPONENTIAL_DECAY_RETRY: exponential decay retry. If an event failed to be pushed, it can be retried up to 176 times. The interval between two consecutive retries exponentially increases to 512 seconds, and the total retry time is one day. The specific retry intervals are 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 512, ..., and 512 seconds. The interval of 512 seconds is used for 167 retries.
        self.push_retry_strategy = push_retry_strategy  # type: str
        # The transformer that is used to push events.
        self.push_selector = push_selector  # type: str
        # The type of the event target. For more information, see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.type = type  # type: str

    def validate(self):
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRuleResponseBodyDataTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.detail_map is not None:
            result['DetailMap'] = self.detail_map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        if self.push_selector is not None:
            result['PushSelector'] = self.push_selector
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeadLetterQueue') is not None:
            temp_model = GetRuleResponseBodyDataTargetsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('DetailMap') is not None:
            self.detail_map = m.get('DetailMap')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = GetRuleResponseBodyDataTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        if m.get('PushSelector') is not None:
            self.push_selector = m.get('PushSelector')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetRuleResponseBodyData(TeaModel):
    def __init__(self, created_timestamp=None, description=None, event_bus_name=None, filter_pattern=None,
                 rule_arn=None, rule_name=None, status=None, targets=None):
        # The timestamp that indicates when the event rule was created.
        self.created_timestamp = created_timestamp  # type: long
        # The description of the event rule.
        self.description = description  # type: str
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event pattern, in JSON format. Valid values: stringEqual and stringExpression. You can specify up to five expressions in the map data structure in each field.
        # 
        # You can specify up to five expressions in the map data structure in each field.
        self.filter_pattern = filter_pattern  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the event rule.
        self.rule_arn = rule_arn  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str
        # The status of the event rule. Valid values: ENABLE (default): The event rule is enabled. DISABLE: The event rule is disabled.
        self.status = status  # type: str
        # The event targets.
        self.targets = targets  # type: list[GetRuleResponseBodyDataTargets]

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = GetRuleResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class GetRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: GetRuleResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRuleResponseBody, self).to_map()
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
            temp_model = GetRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes(TeaModel):
    def __init__(self, event_source_name=None, group_name=None, name=None, short_name=None):
        # The name of the event source.
        self.event_source_name = event_source_name  # type: str
        # The name of the group to which the queried event type belongs.
        self.group_name = group_name  # type: str
        # The full name of the queried event type.
        self.name = name  # type: str
        # The short name of the queried event type.
        self.short_name = short_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.short_name is not None:
            result['ShortName'] = self.short_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')
        return self


class ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList(TeaModel):
    def __init__(self, arn=None, ctime=None, description=None, event_bus_name=None, event_types=None, full_name=None,
                 name=None, status=None, type=None):
        # The Alibaba Cloud Resource Name (ARN) of the event bus.
        self.arn = arn  # type: str
        # The time when the event source was created. Unit: milliseconds.
        self.ctime = ctime  # type: float
        # The description of the queried event source.
        self.description = description  # type: str
        # The name of the event source to which the queried event type belongs.
        self.event_bus_name = event_bus_name  # type: str
        # The queried event types.
        self.event_types = event_types  # type: list[ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes]
        self.full_name = full_name  # type: str
        # The name of the queried event source.
        self.name = name  # type: str
        # The status of the queried event source. Valid value: Activated.
        self.status = status  # type: str
        # The type of the queried event source.
        self.type = type  # type: str

    def validate(self):
        if self.event_types:
            for k in self.event_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        result['EventTypes'] = []
        if self.event_types is not None:
            for k in self.event_types:
                result['EventTypes'].append(k.to_map() if k else None)
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        self.event_types = []
        if m.get('EventTypes') is not None:
            for k in m.get('EventTypes'):
                temp_model = ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes()
                self.event_types.append(temp_model.from_map(k))
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAliyunOfficialEventSourcesResponseBodyData(TeaModel):
    def __init__(self, event_source_list=None):
        # The name of the event source to which the queried event type belongs.
        self.event_source_list = event_source_list  # type: list[ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList]

    def validate(self):
        if self.event_source_list:
            for k in self.event_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAliyunOfficialEventSourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventSourceList'] = []
        if self.event_source_list is not None:
            for k in self.event_source_list:
                result['EventSourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_source_list = []
        if m.get('EventSourceList') is not None:
            for k in m.get('EventSourceList'):
                temp_model = ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList()
                self.event_source_list.append(temp_model.from_map(k))
        return self


class ListAliyunOfficialEventSourcesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: ListAliyunOfficialEventSourcesResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAliyunOfficialEventSourcesResponseBody, self).to_map()
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
            temp_model = ListAliyunOfficialEventSourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAliyunOfficialEventSourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAliyunOfficialEventSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAliyunOfficialEventSourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAliyunOfficialEventSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApiDestinationsRequest(TeaModel):
    def __init__(self, api_destination_name_prefix=None, connection_name=None, max_results=None, next_token=None):
        # The prefix of the API destination name.
        self.api_destination_name_prefix = api_destination_name_prefix  # type: str
        # The connection name.
        self.connection_name = connection_name  # type: str
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging.
        # 
        # *   Default value: 10.
        self.max_results = max_results  # type: long
        # If you set Limit and excess return values exist, this parameter is returned.
        # 
        # *   Default value: 0.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApiDestinationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name_prefix is not None:
            result['ApiDestinationNamePrefix'] = self.api_destination_name_prefix
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationNamePrefix') is not None:
            self.api_destination_name_prefix = m.get('ApiDestinationNamePrefix')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListApiDestinationsResponseBodyDataApiDestinationsHttpApiParameters(TeaModel):
    def __init__(self, endpoint=None, method=None):
        # The endpoint of the API destination.
        self.endpoint = endpoint  # type: str
        # The HTTP request method. Valid values:
        # 
        # - POST
        # 
        # - GET
        # 
        # - DELETE
        # 
        # - PUT
        # 
        # - HEAD
        # 
        # - TRACE
        # 
        # - PATCH
        self.method = method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApiDestinationsResponseBodyDataApiDestinationsHttpApiParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class ListApiDestinationsResponseBodyDataApiDestinations(TeaModel):
    def __init__(self, api_destination_name=None, connection_name=None, description=None, gmt_create=None,
                 http_api_parameters=None):
        # The name of the API destination.
        self.api_destination_name = api_destination_name  # type: str
        # The connection name.
        self.connection_name = connection_name  # type: str
        # The description of the connection.
        self.description = description  # type: str
        # The time when the API destination was created.
        self.gmt_create = gmt_create  # type: long
        # The request parameters that are configured for the API destination.
        self.http_api_parameters = http_api_parameters  # type: ListApiDestinationsResponseBodyDataApiDestinationsHttpApiParameters

    def validate(self):
        if self.http_api_parameters:
            self.http_api_parameters.validate()

    def to_map(self):
        _map = super(ListApiDestinationsResponseBodyDataApiDestinations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.http_api_parameters is not None:
            result['HttpApiParameters'] = self.http_api_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('HttpApiParameters') is not None:
            temp_model = ListApiDestinationsResponseBodyDataApiDestinationsHttpApiParameters()
            self.http_api_parameters = temp_model.from_map(m['HttpApiParameters'])
        return self


class ListApiDestinationsResponseBodyData(TeaModel):
    def __init__(self, api_destinations=None, max_results=None, next_token=None, total=None):
        # The API destinations.
        self.api_destinations = api_destinations  # type: list[ListApiDestinationsResponseBodyDataApiDestinations]
        # The maximum number of entries returned per page.
        self.max_results = max_results  # type: float
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The total number of entries returned.
        self.total = total  # type: float

    def validate(self):
        if self.api_destinations:
            for k in self.api_destinations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApiDestinationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiDestinations'] = []
        if self.api_destinations is not None:
            for k in self.api_destinations:
                result['ApiDestinations'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_destinations = []
        if m.get('ApiDestinations') is not None:
            for k in m.get('ApiDestinations'):
                temp_model = ListApiDestinationsResponseBodyDataApiDestinations()
                self.api_destinations.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListApiDestinationsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: ListApiDestinationsResponseBodyData
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListApiDestinationsResponseBody, self).to_map()
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
            temp_model = ListApiDestinationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApiDestinationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApiDestinationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApiDestinationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListApiDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionsRequest(TeaModel):
    def __init__(self, connection_name_prefix=None, max_results=None, next_token=None):
        # The key word that you specify to query connections. Connections can be queried by prefixes.
        self.connection_name_prefix = connection_name_prefix  # type: str
        # The maximum number of entries to be returned in a single call. You can use this parameter and the NextToken parameter to implement paging.
        # 
        # *   Default value: 10.
        self.max_results = max_results  # type: long
        # If you set the Limit parameter and excess return values exist, this parameter is returned.
        # 
        # *   Default value: 0.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_name_prefix is not None:
            result['ConnectionNamePrefix'] = self.connection_name_prefix
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionNamePrefix') is not None:
            self.connection_name_prefix = m.get('ConnectionNamePrefix')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters(TeaModel):
    def __init__(self, api_key_name=None, api_key_value=None):
        # The API key.
        self.api_key_name = api_key_name  # type: str
        # The value of the API key.
        self.api_key_value = api_key_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key_name is not None:
            result['ApiKeyName'] = self.api_key_name
        if self.api_key_value is not None:
            result['ApiKeyValue'] = self.api_key_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiKeyName') is not None:
            self.api_key_name = m.get('ApiKeyName')
        if m.get('ApiKeyValue') is not None:
            self.api_key_value = m.get('ApiKeyValue')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersBasicAuthParameters(TeaModel):
    def __init__(self, password=None, username=None):
        # The password for basic authentication.
        self.password = password  # type: str
        # The username for basic authentication.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnectionsAuthParametersBasicAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(self, client_id=None, client_secret=None):
        # The client ID.
        self.client_id = client_id  # type: str
        # The client key secret of the application.
        self.client_secret = client_secret  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientID'] = self.client_id
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientID') is not None:
            self.client_id = m.get('ClientID')
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret  # type: str
        # The key in the request body.
        self.key = key  # type: str
        # The value of the key in the request body.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret  # type: str
        # The key in the request header.
        self.key = key  # type: str
        # The value of the key in the request header.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Indicates whether authentication is enabled.
        self.is_value_secret = is_value_secret  # type: str
        # The key in the request path.
        self.key = key  # type: str
        # The value of the key in the request path.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters(TeaModel):
    def __init__(self, body_parameters=None, header_parameters=None, query_string_parameters=None):
        # The parameters that are configured for the request.
        self.body_parameters = body_parameters  # type: list[ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters]
        # The parameters that are configured for the request header.
        self.header_parameters = header_parameters  # type: list[ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters]
        # The parameters that are configured for the request path.
        self.query_string_parameters = query_string_parameters  # type: list[ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters]

    def validate(self):
        if self.body_parameters:
            for k in self.body_parameters:
                if k:
                    k.validate()
        if self.header_parameters:
            for k in self.header_parameters:
                if k:
                    k.validate()
        if self.query_string_parameters:
            for k in self.query_string_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyParameters'] = []
        if self.body_parameters is not None:
            for k in self.body_parameters:
                result['BodyParameters'].append(k.to_map() if k else None)
        result['HeaderParameters'] = []
        if self.header_parameters is not None:
            for k in self.header_parameters:
                result['HeaderParameters'].append(k.to_map() if k else None)
        result['QueryStringParameters'] = []
        if self.query_string_parameters is not None:
            for k in self.query_string_parameters:
                result['QueryStringParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body_parameters = []
        if m.get('BodyParameters') is not None:
            for k in m.get('BodyParameters'):
                temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParameters(TeaModel):
    def __init__(self, authorization_endpoint=None, client_parameters=None, http_method=None,
                 oauth_http_parameters=None):
        # The endpoint that is used to obtain the OAuth token.
        self.authorization_endpoint = authorization_endpoint  # type: str
        # The parameters that are configured for the client.
        self.client_parameters = client_parameters  # type: ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters
        # The HTTP request method. Valid values:
        # 
        # - GET
        # 
        # - POST
        # 
        # - HEAD
        self.http_method = http_method  # type: str
        # The request parameters for OAuth authentication.
        self.oauth_http_parameters = oauth_http_parameters  # type: ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters

    def validate(self):
        if self.client_parameters:
            self.client_parameters.validate()
        if self.oauth_http_parameters:
            self.oauth_http_parameters.validate()

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_endpoint is not None:
            result['AuthorizationEndpoint'] = self.authorization_endpoint
        if self.client_parameters is not None:
            result['ClientParameters'] = self.client_parameters.to_map()
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.oauth_http_parameters is not None:
            result['OAuthHttpParameters'] = self.oauth_http_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('AuthorizationEndpoint')
        if m.get('ClientParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersClientParameters()
            self.client_parameters = temp_model.from_map(m['ClientParameters'])
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('OAuthHttpParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParametersOAuthHttpParameters()
            self.oauth_http_parameters = temp_model.from_map(m['OAuthHttpParameters'])
        return self


class ListConnectionsResponseBodyDataConnectionsAuthParameters(TeaModel):
    def __init__(self, api_key_auth_parameters=None, authorization_type=None, basic_auth_parameters=None,
                 oauth_parameters=None):
        # The parameters that are configured for API key authentication.
        self.api_key_auth_parameters = api_key_auth_parameters  # type: ListConnectionsResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters
        # The authentication type. Valid values:
        # 
        # - BASIC_AUTH: basic authentication.
        # 
        # - API_KEY_AUTH: API key authentication.
        # 
        # - OAUTH_AUTH: OAuth authentication.
        self.authorization_type = authorization_type  # type: str
        # The parameters that are configured for basic authentication.
        self.basic_auth_parameters = basic_auth_parameters  # type: ListConnectionsResponseBodyDataConnectionsAuthParametersBasicAuthParameters
        # The parameters that are configured for OAuth authentication.
        self.oauth_parameters = oauth_parameters  # type: ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.oauth_parameters:
            self.oauth_parameters.validate()

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnectionsAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key_auth_parameters is not None:
            result['ApiKeyAuthParameters'] = self.api_key_auth_parameters.to_map()
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.basic_auth_parameters is not None:
            result['BasicAuthParameters'] = self.basic_auth_parameters.to_map()
        if self.oauth_parameters is not None:
            result['OAuthParameters'] = self.oauth_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiKeyAuthParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersApiKeyAuthParameters()
            self.api_key_auth_parameters = temp_model.from_map(m['ApiKeyAuthParameters'])
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('BasicAuthParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersBasicAuthParameters()
            self.basic_auth_parameters = temp_model.from_map(m['BasicAuthParameters'])
        if m.get('OAuthParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParametersOAuthParameters()
            self.oauth_parameters = temp_model.from_map(m['OAuthParameters'])
        return self


class ListConnectionsResponseBodyDataConnectionsNetworkParameters(TeaModel):
    def __init__(self, network_type=None, security_group_id=None, vpc_id=None, vswitche_id=None):
        # The network type. Valid values:PublicNetwork and PrivateNetwork.
        self.network_type = network_type  # type: str
        # The security group ID.
        self.security_group_id = security_group_id  # type: str
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id  # type: str
        # The vSwitch ID.
        self.vswitche_id = vswitche_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnectionsNetworkParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitche_id is not None:
            result['VswitcheId'] = self.vswitche_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitcheId') is not None:
            self.vswitche_id = m.get('VswitcheId')
        return self


class ListConnectionsResponseBodyDataConnections(TeaModel):
    def __init__(self, auth_parameters=None, connection_name=None, description=None, gmt_create=None, id=None,
                 network_parameters=None):
        # The parameters that are configured for authentication.
        self.auth_parameters = auth_parameters  # type: ListConnectionsResponseBodyDataConnectionsAuthParameters
        # The connection name.
        self.connection_name = connection_name  # type: str
        # The connection description.
        self.description = description  # type: str
        # The time when the connection was created.
        self.gmt_create = gmt_create  # type: long
        # The connection ID.
        self.id = id  # type: long
        self.network_parameters = network_parameters  # type: ListConnectionsResponseBodyDataConnectionsNetworkParameters

    def validate(self):
        if self.auth_parameters:
            self.auth_parameters.validate()
        if self.network_parameters:
            self.network_parameters.validate()

    def to_map(self):
        _map = super(ListConnectionsResponseBodyDataConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters is not None:
            result['AuthParameters'] = self.auth_parameters.to_map()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.network_parameters is not None:
            result['NetworkParameters'] = self.network_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsAuthParameters()
            self.auth_parameters = temp_model.from_map(m['AuthParameters'])
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NetworkParameters') is not None:
            temp_model = ListConnectionsResponseBodyDataConnectionsNetworkParameters()
            self.network_parameters = temp_model.from_map(m['NetworkParameters'])
        return self


class ListConnectionsResponseBodyData(TeaModel):
    def __init__(self, connections=None, max_results=None, next_token=None, total=None):
        # The value of the key in the request path.
        self.connections = connections  # type: list[ListConnectionsResponseBodyDataConnections]
        # The number of entries returned per page.
        self.max_results = max_results  # type: float
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The total number of entries returned.
        self.total = total  # type: float

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConnectionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = ListConnectionsResponseBodyDataConnections()
                self.connections.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListConnectionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        # The HTTP status code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The information about the connections returned.
        self.data = data  # type: ListConnectionsResponseBodyData
        # The message returned.
        self.message = message  # type: str
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use the ID to troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListConnectionsResponseBody, self).to_map()
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
            temp_model = ListConnectionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConnectionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConnectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConnectionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventBusesRequest(TeaModel):
    def __init__(self, limit=None, name_prefix=None, next_token=None):
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging. Note: Up to 100 entries can be returned in a call.
        self.limit = limit  # type: int
        # The prefix of the names of the event buses that you want to query.
        self.name_prefix = name_prefix  # type: str
        # If you set Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventBusesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListEventBusesResponseBodyDataEventBuses(TeaModel):
    def __init__(self, create_timestamp=None, description=None, event_bus_arn=None, event_bus_name=None):
        # The timestamp that indicates when the event bus was created.
        self.create_timestamp = create_timestamp  # type: long
        # The description of the queried event bus.
        self.description = description  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the queried event bus.
        self.event_bus_arn = event_bus_arn  # type: str
        # The name of the queried event bus.
        self.event_bus_name = event_bus_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventBusesResponseBodyDataEventBuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_arn is not None:
            result['EventBusARN'] = self.event_bus_arn
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusARN') is not None:
            self.event_bus_arn = m.get('EventBusARN')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class ListEventBusesResponseBodyData(TeaModel):
    def __init__(self, event_buses=None, next_token=None, total=None):
        # The timestamp that indicates when the event bus was created.
        self.event_buses = event_buses  # type: list[ListEventBusesResponseBodyDataEventBuses]
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The total number of entries.
        self.total = total  # type: int

    def validate(self):
        if self.event_buses:
            for k in self.event_buses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEventBusesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventBuses'] = []
        if self.event_buses is not None:
            for k in self.event_buses:
                result['EventBuses'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_buses = []
        if m.get('EventBuses') is not None:
            for k in m.get('EventBuses'):
                temp_model = ListEventBusesResponseBodyDataEventBuses()
                self.event_buses.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEventBusesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: ListEventBusesResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the event buses are successfully queried. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEventBusesResponseBody, self).to_map()
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
            temp_model = ListEventBusesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEventBusesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEventBusesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEventBusesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEventBusesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventStreamingsRequest(TeaModel):
    def __init__(self, limit=None, name_prefix=None, next_token=None, sink_arn=None, source_arn=None):
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging. A maximum of 100 entries can be returned in a call.
        self.limit = limit  # type: int
        # The name of the event stream that you want to query.
        self.name_prefix = name_prefix  # type: str
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The ARN of the event target.
        self.sink_arn = sink_arn  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the event source.
        self.source_arn = source_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sink_arn is not None:
            result['SinkArn'] = self.sink_arn
        if self.source_arn is not None:
            result['SourceArn'] = self.source_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SinkArn') is not None:
            self.sink_arn = m.get('SinkArn')
        if m.get('SourceArn') is not None:
            self.source_arn = m.get('SourceArn')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBatchWindow(TeaModel):
    def __init__(self, count_based_window=None, time_based_window=None):
        self.count_based_window = count_based_window  # type: int
        self.time_based_window = time_based_window  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBatchWindow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue(TeaModel):
    def __init__(self, arn=None):
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsRetryStrategy(TeaModel):
    def __init__(self, maximum_event_age_in_seconds=None, maximum_retry_attempts=None, push_retry_strategy=None):
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds  # type: float
        self.maximum_retry_attempts = maximum_retry_attempts  # type: float
        self.push_retry_strategy = push_retry_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsRetryStrategy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsRunOptions(TeaModel):
    def __init__(self, batch_window=None, dead_letter_queue=None, errors_tolerance=None, maximum_tasks=None,
                 retry_strategy=None):
        self.batch_window = batch_window  # type: ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBatchWindow
        self.dead_letter_queue = dead_letter_queue  # type: ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue
        self.errors_tolerance = errors_tolerance  # type: str
        self.maximum_tasks = maximum_tasks  # type: int
        self.retry_strategy = retry_strategy  # type: ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsRetryStrategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsRunOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersConcurrency(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersConcurrency, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParameters(TeaModel):
    def __init__(self, body=None, concurrency=None, function_name=None, invocation_type=None, qualifier=None,
                 service_name=None):
        self.body = body  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersBody
        self.concurrency = concurrency  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersConcurrency
        self.function_name = function_name  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName
        self.invocation_type = invocation_type  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType
        self.qualifier = qualifier  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier
        self.service_name = service_name  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.concurrency:
            self.concurrency.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Concurrency') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m['Concurrency'])
        if m.get('FunctionName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersExecutionName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersExecutionName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersFlowName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersFlowName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersInput(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersRoleName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersRoleName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParameters(TeaModel):
    def __init__(self, execution_name=None, flow_name=None, input=None, role_name=None):
        self.execution_name = execution_name  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersExecutionName
        self.flow_name = flow_name  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersFlowName
        self.input = input  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersInput
        self.role_name = role_name  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersRoleName

    def validate(self):
        if self.execution_name:
            self.execution_name.validate()
        if self.flow_name:
            self.flow_name.validate()
        if self.input:
            self.input.validate()
        if self.role_name:
            self.role_name.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name.to_map()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name.to_map()
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m['ExecutionName'])
        if m.get('FlowName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m['FlowName'])
        if m.get('Input') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('RoleName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters(TeaModel):
    def __init__(self, acks=None, instance_id=None, key=None, topic=None, value=None):
        self.acks = acks  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks
        self.instance_id = instance_id  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId
        self.key = key  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey
        self.topic = topic  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic
        self.value = value  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('Topic') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters(TeaModel):
    def __init__(self, body=None, is_base_64encode=None, queue_name=None):
        self.body = body  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersBody
        self.is_base_64encode = is_base_64encode  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode
        self.queue_name = queue_name  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters(TeaModel):
    def __init__(self, body=None, exchange=None, instance_id=None, message_id=None, properties=None, queue_name=None,
                 routing_key=None, target_type=None, virtual_host_name=None):
        self.body = body  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody
        self.exchange = exchange  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange
        self.instance_id = instance_id  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId
        self.message_id = message_id  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId
        self.properties = properties  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties
        self.queue_name = queue_name  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName
        self.routing_key = routing_key  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey
        self.target_type = target_type  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType
        self.virtual_host_name = virtual_host_name  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters(TeaModel):
    def __init__(self, body=None, instance_id=None, keys=None, properties=None, tags=None, topic=None):
        self.body = body  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody
        self.instance_id = instance_id  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId
        self.keys = keys  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys
        self.properties = properties  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties
        self.tags = tags  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags
        self.topic = topic  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.keys:
            self.keys.validate()
        if self.properties:
            self.properties.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceId') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Keys') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Properties') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Tags') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersProject(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters(TeaModel):
    def __init__(self, body=None, log_store=None, project=None, role_name=None, topic=None):
        self.body = body  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersBody
        self.log_store = log_store  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore
        self.project = project  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersProject
        self.role_name = role_name  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName
        self.topic = topic  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSink(TeaModel):
    def __init__(self, sink_fc_parameters=None, sink_fnf_parameters=None, sink_kafka_parameters=None,
                 sink_mnsparameters=None, sink_rabbit_mqparameters=None, sink_rocket_mqparameters=None, sink_slsparameters=None):
        self.sink_fc_parameters = sink_fc_parameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParameters
        self.sink_fnf_parameters = sink_fnf_parameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParameters
        self.sink_kafka_parameters = sink_kafka_parameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters
        self.sink_mnsparameters = sink_mnsparameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters
        # Sink RocketMQ Parameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters
        # Sink SLS Parameters
        self.sink_slsparameters = sink_slsparameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters

    def validate(self):
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_fnf_parameters:
            self.sink_fnf_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSink, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_fnf_parameters is not None:
            result['SinkFnfParameters'] = self.sink_fnf_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SinkFcParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkFnfParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m['SinkFnfParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceDTSParameters(TeaModel):
    def __init__(self, broker_url=None, init_check_point=None, password=None, sid=None, task_id=None, topic=None,
                 username=None):
        self.broker_url = broker_url  # type: str
        self.init_check_point = init_check_point  # type: str
        self.password = password  # type: str
        self.sid = sid  # type: str
        self.task_id = task_id  # type: str
        self.topic = topic  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceDTSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceKafkaParameters(TeaModel):
    def __init__(self, consumer_group=None, instance_id=None, network=None, offset_reset=None, region_id=None,
                 security_group_id=None, topic=None, v_switch_ids=None, vpc_id=None):
        self.consumer_group = consumer_group  # type: str
        self.instance_id = instance_id  # type: str
        self.network = network  # type: str
        self.offset_reset = offset_reset  # type: str
        self.region_id = region_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.topic = topic  # type: str
        self.v_switch_ids = v_switch_ids  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMNSParameters(TeaModel):
    def __init__(self, is_base_64decode=None, queue_name=None, region_id=None):
        self.is_base_64decode = is_base_64decode  # type: bool
        self.queue_name = queue_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMQTTParameters(TeaModel):
    def __init__(self, instance_id=None, region_id=None, topic=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMQTTParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters(TeaModel):
    def __init__(self, instance_id=None, queue_name=None, region_id=None, virtual_host_name=None):
        self.instance_id = instance_id  # type: str
        self.queue_name = queue_name  # type: str
        self.region_id = region_id  # type: str
        self.virtual_host_name = virtual_host_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQParameters(TeaModel):
    def __init__(self, auth_type=None, group_id=None, instance_endpoint=None, instance_id=None,
                 instance_network=None, instance_password=None, instance_security_group_id=None, instance_type=None,
                 instance_username=None, instance_vswitch_ids=None, instance_vpc_id=None, offset=None, region_id=None, tag=None,
                 timestamp=None, topic=None):
        self.auth_type = auth_type  # type: str
        self.group_id = group_id  # type: str
        self.instance_endpoint = instance_endpoint  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_network = instance_network  # type: str
        self.instance_password = instance_password  # type: str
        self.instance_security_group_id = instance_security_group_id  # type: str
        self.instance_type = instance_type  # type: str
        self.instance_username = instance_username  # type: str
        self.instance_vswitch_ids = instance_vswitch_ids  # type: str
        self.instance_vpc_id = instance_vpc_id  # type: str
        self.offset = offset  # type: str
        self.region_id = region_id  # type: str
        self.tag = tag  # type: str
        self.timestamp = timestamp  # type: long
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceSLSParameters(TeaModel):
    def __init__(self, consume_position=None, consumer_group=None, log_store=None, project=None, role_name=None):
        self.consume_position = consume_position  # type: str
        self.consumer_group = consumer_group  # type: str
        self.log_store = log_store  # type: str
        self.project = project  # type: str
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceSLSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsSource(TeaModel):
    def __init__(self, source_dtsparameters=None, source_kafka_parameters=None, source_mnsparameters=None,
                 source_mqttparameters=None, source_rabbit_mqparameters=None, source_rocket_mqparameters=None,
                 source_slsparameters=None):
        self.source_dtsparameters = source_dtsparameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceDTSParameters
        # Source Kafka Parameters
        self.source_kafka_parameters = source_kafka_parameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceKafkaParameters
        # Source MNS Parameters
        self.source_mnsparameters = source_mnsparameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMNSParameters
        self.source_mqttparameters = source_mqttparameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMQTTParameters
        # Source RabbitMQ Parameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters
        # Source RocketMQ Parameters
        self.source_rocket_mqparameters = source_rocket_mqparameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQParameters
        self.source_slsparameters = source_slsparameters  # type: ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceSLSParameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class ListEventStreamingsResponseBodyDataEventStreamingsTransforms(TeaModel):
    def __init__(self, arn=None):
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamingsTransforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class ListEventStreamingsResponseBodyDataEventStreamings(TeaModel):
    def __init__(self, description=None, event_streaming_name=None, filter_pattern=None, run_options=None,
                 sink=None, source=None, status=None, transforms=None):
        self.description = description  # type: str
        self.event_streaming_name = event_streaming_name  # type: str
        self.filter_pattern = filter_pattern  # type: str
        self.run_options = run_options  # type: ListEventStreamingsResponseBodyDataEventStreamingsRunOptions
        self.sink = sink  # type: ListEventStreamingsResponseBodyDataEventStreamingsSink
        self.source = source  # type: ListEventStreamingsResponseBodyDataEventStreamingsSource
        self.status = status  # type: str
        self.transforms = transforms  # type: list[ListEventStreamingsResponseBodyDataEventStreamingsTransforms]

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()
        if self.transforms:
            for k in self.transforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyDataEventStreamings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['Transforms'] = []
        if self.transforms is not None:
            for k in self.transforms:
                result['Transforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = ListEventStreamingsResponseBodyDataEventStreamingsSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.transforms = []
        if m.get('Transforms') is not None:
            for k in m.get('Transforms'):
                temp_model = ListEventStreamingsResponseBodyDataEventStreamingsTransforms()
                self.transforms.append(temp_model.from_map(k))
        return self


class ListEventStreamingsResponseBodyData(TeaModel):
    def __init__(self, event_streamings=None, next_token=None, total=None):
        # The status of the event stream that is returned.
        self.event_streamings = event_streamings  # type: list[ListEventStreamingsResponseBodyDataEventStreamings]
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists. You must specify the pagination token in the next request.
        self.next_token = next_token  # type: str
        # The total number of records.
        self.total = total  # type: int

    def validate(self):
        if self.event_streamings:
            for k in self.event_streamings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventStreamings'] = []
        if self.event_streamings is not None:
            for k in self.event_streamings:
                result['EventStreamings'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_streamings = []
        if m.get('EventStreamings') is not None:
            for k in m.get('EventStreamings'):
                temp_model = ListEventStreamingsResponseBodyDataEventStreamings()
                self.event_streamings.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEventStreamingsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The response code. Valid values:
        # 
        # Success: The request is successful.
        # 
        # Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The information about the event streams.
        self.data = data  # type: ListEventStreamingsResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. The value true indicates that the request is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponseBody, self).to_map()
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
            temp_model = ListEventStreamingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEventStreamingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEventStreamingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEventStreamingsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEventStreamingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(self, event_bus_name=None, limit=None, next_token=None, rule_name_prefix=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The maximum number of entries to be returned in a single call. You can use this parameter and the NextToken parameter to implement paging. A maximum of 100 entries can be returned in a single call.
        self.limit = limit  # type: int
        # If you set the Limit parameter and excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The prefix of the rule name.
        self.rule_name_prefix = rule_name_prefix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.rule_name_prefix is not None:
            result['RuleNamePrefix'] = self.rule_name_prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RuleNamePrefix') is not None:
            self.rule_name_prefix = m.get('RuleNamePrefix')
        return self


class ListRulesResponseBodyDataRulesTargets(TeaModel):
    def __init__(self, endpoint=None, errors_tolerance=None, id=None, push_selector=None, type=None):
        # The endpoint of the event target.
        self.endpoint = endpoint  # type: str
        self.errors_tolerance = errors_tolerance  # type: str
        # The ID of the custom event target.
        self.id = id  # type: str
        # The transformer that is used to push events.
        self.push_selector = push_selector  # type: str
        # The type of the event target. For more information, see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRulesResponseBodyDataRulesTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.id is not None:
            result['Id'] = self.id
        if self.push_selector is not None:
            result['PushSelector'] = self.push_selector
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PushSelector') is not None:
            self.push_selector = m.get('PushSelector')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRulesResponseBodyDataRules(TeaModel):
    def __init__(self, created_timestamp=None, description=None, detail_map=None, event_bus_name=None,
                 filter_pattern=None, rule_arn=None, rule_name=None, status=None, targets=None):
        # The creation timestamp.
        self.created_timestamp = created_timestamp  # type: long
        # The rule description.
        self.description = description  # type: str
        # The details of the event rule.
        self.detail_map = detail_map  # type: dict[str, any]
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event pattern, in JSON format. Valid values: stringEqual pattern stringExpression pattern Each field can have a maximum of five expressions in the map data structure.
        # 
        # Each field can have a maximum of five expressions in the map data structure.
        self.filter_pattern = filter_pattern  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the rule.
        self.rule_arn = rule_arn  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str
        # The status of the event rule. Valid values: ENABLE: The event rule is enabled. It is the default state of the event rule. DISABLE: The event rule is disabled.
        self.status = status  # type: str
        # The event targets.
        self.targets = targets  # type: list[ListRulesResponseBodyDataRulesTargets]

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRulesResponseBodyDataRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp
        if self.description is not None:
            result['Description'] = self.description
        if self.detail_map is not None:
            result['DetailMap'] = self.detail_map
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DetailMap') is not None:
            self.detail_map = m.get('DetailMap')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = ListRulesResponseBodyDataRulesTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class ListRulesResponseBodyData(TeaModel):
    def __init__(self, next_token=None, rules=None, total=None):
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The rules.
        self.rules = rules  # type: list[ListRulesResponseBodyDataRules]
        # The total number of entries.
        self.total = total  # type: int

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListRulesResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The error code. The value Success indicates that the request is successful.
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: ListRulesResponseBodyData
        # The error message that is returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListRulesResponseBody, self).to_map()
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
            temp_model = ListRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTargetsRequest(TeaModel):
    def __init__(self, arn=None, event_bus_name=None, limit=None, next_token=None, rule_name=None):
        # The Alibaba Cloud Resource Name (ARN) of the event rule.
        self.arn = arn  # type: str
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The maximum number of entries returned per page.
        self.limit = limit  # type: int
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTargetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListTargetsResponseBodyDataTargetsParamList(TeaModel):
    def __init__(self, form=None, resource_key=None, template=None, value=None):
        self.form = form  # type: str
        self.resource_key = resource_key  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTargetsResponseBodyDataTargetsParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTargetsResponseBodyDataTargets(TeaModel):
    def __init__(self, endpoint=None, errors_tolerance=None, event_bus_name=None, id=None, param_list=None,
                 rule_name=None, type=None):
        self.endpoint = endpoint  # type: str
        self.errors_tolerance = errors_tolerance  # type: str
        self.event_bus_name = event_bus_name  # type: str
        self.id = id  # type: str
        self.param_list = param_list  # type: list[ListTargetsResponseBodyDataTargetsParamList]
        self.rule_name = rule_name  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTargetsResponseBodyDataTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = ListTargetsResponseBodyDataTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTargetsResponseBodyData(TeaModel):
    def __init__(self, next_token=None, targets=None, total=None):
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The name of the event rule.
        self.targets = targets  # type: list[ListTargetsResponseBodyDataTargets]
        # The total number of entries.
        self.total = total  # type: int

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTargetsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = ListTargetsResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListTargetsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned response code. Valid values:
        # 
        #     Success: The request is successful. 
        # 
        #     Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: ListTargetsResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        #     true: The request is successful. 
        # 
        #     false: The request failed.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListTargetsResponseBody, self).to_map()
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
            temp_model = ListTargetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTargetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTargetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTargetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDefinedEventSourcesRequest(TeaModel):
    def __init__(self, event_bus_name=None, limit=None, name_prefix=None, next_token=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging. Note: Up to 100 entries can be returned in a call.
        self.limit = limit  # type: int
        # The name of the event source.
        self.name_prefix = name_prefix  # type: str
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters(TeaModel):
    def __init__(self, ip=None, method=None, public_web_hook_url=None, referer=None, security_config=None, type=None,
                 vpc_web_hook_url=None):
        # The CIDR block that is used for security settings. This parameter is required only if SecurityConfig is set to ip. You can enter a CIDR block or an IP address.
        self.ip = ip  # type: list[str]
        # The HTTP request method that is supported by the generated webhook URL. You can select multiple values. Valid values:
        # 
        # *   GET
        # *   POST
        # *   PUT
        # *   PATCH
        # *   DELETE
        # *   HEAD
        # *   OPTIONS
        # *   TRACE
        # *   CONNECT
        self.method = method  # type: list[str]
        # The Internet request URL.
        self.public_web_hook_url = public_web_hook_url  # type: list[str]
        # The security domain name. This parameter is required only if SecurityConfig is set to referer. You can enter a domain name.
        self.referer = referer  # type: list[str]
        # The type of security settings. Valid values:
        # 
        # *   none: No configuration is required.
        # *   ip: CIDR block.
        # *   referer: security domain name.
        self.security_config = security_config  # type: str
        # The protocol type that is supported by the generated webhook URL. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # *   HTTP\&HTTPS
        self.type = type  # type: str
        # The internal request URL.
        self.vpc_web_hook_url = vpc_web_hook_url  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.method is not None:
            result['Method'] = self.method
        if self.public_web_hook_url is not None:
            result['PublicWebHookUrl'] = self.public_web_hook_url
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.security_config is not None:
            result['SecurityConfig'] = self.security_config
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_web_hook_url is not None:
            result['VpcWebHookUrl'] = self.vpc_web_hook_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('PublicWebHookUrl') is not None:
            self.public_web_hook_url = m.get('PublicWebHookUrl')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SecurityConfig') is not None:
            self.security_config = m.get('SecurityConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcWebHookUrl') is not None:
            self.vpc_web_hook_url = m.get('VpcWebHookUrl')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceKafkaParameters(TeaModel):
    def __init__(self, consumer_group=None, instance_id=None, maximum_tasks=None, network=None, offset_reset=None,
                 region_id=None, security_group_id=None, topic=None, v_switch_ids=None, vpc_id=None):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group  # type: str
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id  # type: str
        # The maximum number of consumers.
        self.maximum_tasks = maximum_tasks  # type: int
        # The network. Valid values: Default and PublicNetwork. Default value: Default. The value PublicNetwork indicates a self-managed network.
        self.network = network  # type: str
        # The consumer offset.
        self.offset_reset = offset_reset  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The security group ID.
        self.security_group_id = security_group_id  # type: str
        # The topic name.
        self.topic = topic  # type: str
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids  # type: str
        # The VPC ID.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters(TeaModel):
    def __init__(self, is_base_64decode=None, queue_name=None, region_id=None):
        # Indicates whether Base64 decoding is enabled. By default, Base64 decoding is enabled.
        self.is_base_64decode = is_base_64decode  # type: bool
        # The name of the MNS queue.
        self.queue_name = queue_name  # type: str
        # The region where the MNS queue resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters(TeaModel):
    def __init__(self, instance_id=None, queue_name=None, region_id=None, virtual_host_name=None):
        # The ID of the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.instance_id = instance_id  # type: str
        # The name of the queue on the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.queue_name = queue_name  # type: str
        # The ID of the region where the Message Queue for RabbitMQ instance resides.
        self.region_id = region_id  # type: str
        # The name of the vhost of the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.virtual_host_name = virtual_host_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters(TeaModel):
    def __init__(self, auth_type=None, group_id=None, instance_endpoint=None, instance_id=None,
                 instance_network=None, instance_password=None, instance_security_group_id=None, instance_type=None,
                 instance_username=None, instance_vswitch_ids=None, instance_vpc_id=None, offset=None, region_id=None, tag=None,
                 timestamp=None, topic=None):
        # The authentication type. This parameter can be set to ACL or left empty.
        self.auth_type = auth_type  # type: str
        # The ID of the consumer group on the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id  # type: str
        # The instance endpoint.
        self.instance_endpoint = instance_endpoint  # type: str
        # The ID of the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.instance_id = instance_id  # type: str
        # The network that is used by the Message Queue for Apache RocketMQ instance.
        self.instance_network = instance_network  # type: str
        # The instance password.
        self.instance_password = instance_password  # type: str
        # The security group ID.
        self.instance_security_group_id = instance_security_group_id  # type: str
        # The instance type. Valid values: CLOUD\_4, CLOUD\_5, and SELF_BUILT. The value CLOUD\_4 indicates that the instance is a Message Queue for Apache RocketMQ 4.0 instance. The value CLOUD\_5 indicates that the instance is a Message Queue for Apache RocketMQ 5.0 instance. The value SELF_BUILT indicates that the instance is a self-managed RocketMQ instance.
        self.instance_type = instance_type  # type: str
        # The instance username.
        self.instance_username = instance_username  # type: str
        # The vSwitch ID.
        self.instance_vswitch_ids = instance_vswitch_ids  # type: str
        # The virtual private cloud (VPC) ID.
        self.instance_vpc_id = instance_vpc_id  # type: str
        # The offset from which messages are consumed. Valid values:
        # 
        # *   CONSUME_FROM_LAST_OFFSET: Messages are consumed from the latest offset.
        # *   CONSUME_FROM_FIRST_OFFSET: Messages are consumed from the earliest offset.
        # *   CONSUME_FROM_TIMESTAMP: Messages are consumed from the offset at the specified point in time.
        # 
        # Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset  # type: str
        # The region where the Message Queue for Apache RocketMQ instance resides.
        self.region_id = region_id  # type: str
        # The tag that is used to filter messages.
        self.tag = tag  # type: str
        # The timestamp that indicates the time from which messages are consumed. This parameter is valid only if Offset is set to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp  # type: float
        # The name of the topic on the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters(TeaModel):
    def __init__(self, consume_position=None, log_store=None, project=None, role_name=None):
        # The consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start message consumption.
        self.consume_position = consume_position  # type: str
        # The Simple Log Service Logstore.
        self.log_store = log_store  # type: str
        # The Simple Log Service project.
        self.project = project  # type: str
        # The role name. If you want to authorize EventBridge to use this role to read logs in Simple Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console. For information about the permission policy of this role, see Create a custom event source of the Log Service type.
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceScheduledEventParameters(TeaModel):
    def __init__(self, schedule=None, time_zone=None, user_data=None):
        # The cron expression.
        self.schedule = schedule  # type: str
        # The time zone in which the cron expression is executed.
        self.time_zone = time_zone  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceScheduledEventParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class ListUserDefinedEventSourcesResponseBodyDataEventSourceList(TeaModel):
    def __init__(self, arn=None, ctime=None, event_bus_name=None, external_source_type=None, name=None,
                 source_http_event_parameters=None, source_kafka_parameters=None, source_mnsparameters=None, source_rabbit_mqparameters=None,
                 source_rocket_mqparameters=None, source_slsparameters=None, source_scheduled_event_parameters=None, status=None, type=None):
        # The Alibaba Cloud Resource Name (ARN) of the queried event source.
        self.arn = arn  # type: str
        # The timestamp that indicates when the event source was created.
        self.ctime = ctime  # type: float
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The type of the event source.
        self.external_source_type = external_source_type  # type: str
        # The name of the queried event source.
        self.name = name  # type: str
        # The parameters that are returned if HTTP events are specified as the event source.
        self.source_http_event_parameters = source_http_event_parameters  # type: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters
        # The parameters that are returned if Message Queue for Apache Kafka is specified as the event source.
        self.source_kafka_parameters = source_kafka_parameters  # type: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceKafkaParameters
        # The parameters that are returned if Message Service (MNS) is specified as the event source.
        self.source_mnsparameters = source_mnsparameters  # type: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters
        # The parameters that are returned if Message Queue for RabbitMQ is specified as the event source.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters  # type: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters
        # The parameters that are returned if Message Queue for Apache RocketMQ is specified as the event source.
        self.source_rocket_mqparameters = source_rocket_mqparameters  # type: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters
        # The parameters that are returned if Simple Log Service is specified as the event source.
        self.source_slsparameters = source_slsparameters  # type: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters
        # The parameters that are returned if scheduled events are specified as the event source.
        self.source_scheduled_event_parameters = source_scheduled_event_parameters  # type: ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceScheduledEventParameters
        # The status of the queried event source. The returned value Activated indicates that the event source is activated.
        self.status = status  # type: str
        # The type of the queried event source. The returned value UserDefined indicates that the event source is a custom event source.
        self.type = type  # type: str

    def validate(self):
        if self.source_http_event_parameters:
            self.source_http_event_parameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()
        if self.source_scheduled_event_parameters:
            self.source_scheduled_event_parameters.validate()

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponseBodyDataEventSourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.external_source_type is not None:
            result['ExternalSourceType'] = self.external_source_type
        if self.name is not None:
            result['Name'] = self.name
        if self.source_http_event_parameters is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        if self.source_scheduled_event_parameters is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('ExternalSourceType') is not None:
            self.external_source_type = m.get('ExternalSourceType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceHttpEventParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceHttpEventParameters()
            self.source_http_event_parameters = temp_model.from_map(m['SourceHttpEventParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        if m.get('SourceScheduledEventParameters') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceListSourceScheduledEventParameters()
            self.source_scheduled_event_parameters = temp_model.from_map(m['SourceScheduledEventParameters'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListUserDefinedEventSourcesResponseBodyData(TeaModel):
    def __init__(self, event_source_list=None):
        # The event sources.
        self.event_source_list = event_source_list  # type: list[ListUserDefinedEventSourcesResponseBodyDataEventSourceList]

    def validate(self):
        if self.event_source_list:
            for k in self.event_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventSourceList'] = []
        if self.event_source_list is not None:
            for k in self.event_source_list:
                result['EventSourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_source_list = []
        if m.get('EventSourceList') is not None:
            for k in m.get('EventSourceList'):
                temp_model = ListUserDefinedEventSourcesResponseBodyDataEventSourceList()
                self.event_source_list.append(temp_model.from_map(k))
        return self


class ListUserDefinedEventSourcesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned response code. Valid values:
        # 
        # *   Success: The request is successful.
        # *   Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The returned data.
        self.data = data  # type: ListUserDefinedEventSourcesResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponseBody, self).to_map()
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
            temp_model = ListUserDefinedEventSourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserDefinedEventSourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserDefinedEventSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserDefinedEventSourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserDefinedEventSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseEventStreamingRequest(TeaModel):
    def __init__(self, event_streaming_name=None):
        # The name of the event stream that you want to stop.
        self.event_streaming_name = event_streaming_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PauseEventStreamingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class PauseEventStreamingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code  # type: bool
        # The error message that is returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PauseEventStreamingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PauseEventStreamingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PauseEventStreamingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PauseEventStreamingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PauseEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutTargetsRequestTargetsDeadLetterQueue(TeaModel):
    def __init__(self, arn=None):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue. Events that are not processed or whose maximum retries have been exceeded are written to the dead-letter queue.
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutTargetsRequestTargetsDeadLetterQueue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class PutTargetsRequestTargetsParamList(TeaModel):
    def __init__(self, form=None, resource_key=None, template=None, value=None):
        # The method that is used to deliver events to the event target. For more information,see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.form = form  # type: str
        # The resource parameter of the event target. For more information,see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.resource_key = resource_key  # type: str
        # The template based on which events are delivered to the event target.
        self.template = template  # type: str
        # The value of the event target parameter.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutTargetsRequestTargetsParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class PutTargetsRequestTargets(TeaModel):
    def __init__(self, dead_letter_queue=None, endpoint=None, errors_tolerance=None, id=None, param_list=None,
                 push_retry_strategy=None, type=None):
        # The dead-letter queue. Events that are not processed or whose maximum retries have been exceeded are written to the dead-letter queue. The dead-letter queue feature supports the following queue types: Message Queue for Apache RocketMQ, Message Service, Message Queue for Apache Kafka, and event bus.
        self.dead_letter_queue = dead_letter_queue  # type: PutTargetsRequestTargetsDeadLetterQueue
        # The endpoint of the event target.
        self.endpoint = endpoint  # type: str
        # The fault tolerance policy. Valid values:
        # 
        # * **ALL**: ignores the error. Fault tolerance is allowed. If an error occurs, event processing is not blocked. If the message exceeds the number of retries specified by the retry policy, the message is delivered to a dead-letter queue or discarded based on your configurations.
        # 
        # * **NONE**: does not ignore the error. Fault tolerance is prohibited. If an error occurs and the message exceeds the number of retries specified by the retry policy, event processing is blocked.
        self.errors_tolerance = errors_tolerance  # type: str
        # The ID of the custom event target.
        self.id = id  # type: str
        # The parameters that are configured for the event target.
        self.param_list = param_list  # type: list[PutTargetsRequestTargetsParamList]
        # The retry policy for pushing the event. Valid values:
        # 
        # * **BACKOFF_RETRY**: backoff retry. A failed event can be retried up to three times. The interval between two consecutive retries is a random value from 10 to 20. Unit: seconds.
        # 
        # * **EXPONENTIAL_DECAY_RETRY**: exponential decay retry. The request can be retried up to 176 times. The interval between two consecutive retries exponentially increases to 512 seconds, and the total retry time is one day. The specific retry intervals are 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 512, ..., and 512 seconds. The interval of 512 seconds can be used up to one hundred and sixty-seven times in total.
        self.push_retry_strategy = push_retry_strategy  # type: str
        # The type of the event target. For more information, see [Event target parameters.](https://www.alibabacloud.com/help/en/eventbridge/latest/event-target-parameters)
        self.type = type  # type: str

    def validate(self):
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PutTargetsRequestTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.id is not None:
            result['Id'] = self.id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeadLetterQueue') is not None:
            temp_model = PutTargetsRequestTargetsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = PutTargetsRequestTargetsParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PutTargetsRequest(TeaModel):
    def __init__(self, event_bus_name=None, rule_name=None, targets=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str
        # The event targets to be created or updated. For more information, see [Limits.](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.targets = targets  # type: list[PutTargetsRequestTargets]

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PutTargetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = PutTargetsRequestTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class PutTargetsShrinkRequest(TeaModel):
    def __init__(self, event_bus_name=None, rule_name=None, targets_shrink=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str
        # The event targets to be created or updated. For more information, see [Limits.](https://www.alibabacloud.com/help/en/eventbridge/latest/limits)
        self.targets_shrink = targets_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutTargetsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        return self


class PutTargetsResponseBodyDataErrorEntries(TeaModel):
    def __init__(self, entry_id=None, error_code=None, error_message=None):
        # The ID of the failed event target.
        self.entry_id = entry_id  # type: str
        # The error code returned.
        self.error_code = error_code  # type: str
        # The error message returned.
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutTargetsResponseBodyDataErrorEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class PutTargetsResponseBodyData(TeaModel):
    def __init__(self, error_entries=None, error_entries_count=None):
        # The ID of the failed event target.
        self.error_entries = error_entries  # type: list[PutTargetsResponseBodyDataErrorEntries]
        # The number of failed event targets. Valid values:
        # 
        # *   0: All event targets succeeded.
        # *   An integer other than 0: indicates the number of failed event targets.
        self.error_entries_count = error_entries_count  # type: int

    def validate(self):
        if self.error_entries:
            for k in self.error_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PutTargetsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorEntries'] = []
        if self.error_entries is not None:
            for k in self.error_entries:
                result['ErrorEntries'].append(k.to_map() if k else None)
        if self.error_entries_count is not None:
            result['ErrorEntriesCount'] = self.error_entries_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.error_entries = []
        if m.get('ErrorEntries') is not None:
            for k in m.get('ErrorEntries'):
                temp_model = PutTargetsResponseBodyDataErrorEntries()
                self.error_entries.append(temp_model.from_map(k))
        if m.get('ErrorEntriesCount') is not None:
            self.error_entries_count = m.get('ErrorEntriesCount')
        return self


class PutTargetsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The response code. Valid values:
        # 
        # *   Success: The call succeeded.
        # *   Other codes: The call failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The returned result.
        self.data = data  # type: PutTargetsResponseBodyData
        # The error message that is returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request failed.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PutTargetsResponseBody, self).to_map()
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
            temp_model = PutTargetsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PutTargetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutTargetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutTargetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PutTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRequest(TeaModel):
    def __init__(self, event_bus_name=None, event_id=None, event_source=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event ID.
        self.event_id = event_id  # type: str
        self.event_source = event_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        return self


class QueryEventResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The status code returned. The status code 200 indicates that the request was successful.
        self.code = code  # type: str
        # The content of the event.
        self.data = data  # type: dict[str, any]
        # The error message that is returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventResponseBody, self).to_map()
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


class QueryEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEventResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventTracesRequest(TeaModel):
    def __init__(self, event_bus_name=None, event_id=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event ID.
        self.event_id = event_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventTracesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class QueryEventTracesResponseBodyData(TeaModel):
    def __init__(self, action=None, action_time=None, endpoint=None, event_bus_name=None, event_id=None,
                 event_source=None, notify_latency=None, notify_status=None, notify_time=None, received_time=None,
                 rule_matching_time=None, rule_name=None):
        # The type of the event trace. Valid values: PutEvent: a delivery event. FilterEvent: a filtering event. PushEvent: a pushing event.
        self.action = action  # type: str
        # The execution time of the event trace.
        self.action_time = action_time  # type: long
        # The endpoint of the event target. This parameter is returned if the value of the Action parameter is PushEvent.
        self.endpoint = endpoint  # type: str
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event ID.
        self.event_id = event_id  # type: str
        # The name of the event source.
        self.event_source = event_source  # type: str
        # The delivery delay of the event target. This parameter is returned if the value of the Action parameter is PushEvent.
        self.notify_latency = notify_latency  # type: str
        # The event target delivery status.
        self.notify_status = notify_status  # type: str
        # The delivery time of the event target. This parameter is returned if the value of the Action parameter is PushEvent.
        self.notify_time = notify_time  # type: long
        # The time when the event was delivered to the event bus. This parameter is returned if the value of the Action parameter is PutEvent.
        self.received_time = received_time  # type: long
        # The time when the event rule was matched. This parameter is returned if the value of the Action parameter is FilterEvent.
        self.rule_matching_time = rule_matching_time  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventTracesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_time is not None:
            result['ActionTime'] = self.action_time
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.notify_latency is not None:
            result['NotifyLatency'] = self.notify_latency
        if self.notify_status is not None:
            result['NotifyStatus'] = self.notify_status
        if self.notify_time is not None:
            result['NotifyTime'] = self.notify_time
        if self.received_time is not None:
            result['ReceivedTime'] = self.received_time
        if self.rule_matching_time is not None:
            result['RuleMatchingTime'] = self.rule_matching_time
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('NotifyLatency') is not None:
            self.notify_latency = m.get('NotifyLatency')
        if m.get('NotifyStatus') is not None:
            self.notify_status = m.get('NotifyStatus')
        if m.get('NotifyTime') is not None:
            self.notify_time = m.get('NotifyTime')
        if m.get('ReceivedTime') is not None:
            self.received_time = m.get('ReceivedTime')
        if m.get('RuleMatchingTime') is not None:
            self.rule_matching_time = m.get('RuleMatchingTime')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class QueryEventTracesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The status code returned. The status code 200 indicates that the request was successful.
        self.code = code  # type: str
        # The name of the event source.
        self.data = data  # type: list[QueryEventTracesResponseBodyData]
        # The error message that is returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryEventTracesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryEventTracesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventTracesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryEventTracesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEventTracesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryEventTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTracedEventByEventIdRequest(TeaModel):
    def __init__(self, event_bus_name=None, event_id=None, event_source=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event ID.
        self.event_id = event_id  # type: str
        # The name of the event source.
        self.event_source = event_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTracedEventByEventIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        return self


class QueryTracedEventByEventIdResponseBodyDataEvents(TeaModel):
    def __init__(self, event_bus_name=None, event_id=None, event_received_time=None, event_source=None,
                 event_type=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event ID.
        self.event_id = event_id  # type: str
        # The time when the event was delivered to the event bus.
        self.event_received_time = event_received_time  # type: long
        # The name of the event source.
        self.event_source = event_source  # type: str
        # The event type.
        self.event_type = event_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTracedEventByEventIdResponseBodyDataEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_received_time is not None:
            result['EventReceivedTime'] = self.event_received_time
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.event_type is not None:
            result['EventType'] = self.event_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventReceivedTime') is not None:
            self.event_received_time = m.get('EventReceivedTime')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        return self


class QueryTracedEventByEventIdResponseBodyData(TeaModel):
    def __init__(self, events=None, next_token=None, total=None):
        # The events.
        self.events = events  # type: list[QueryTracedEventByEventIdResponseBodyDataEvents]
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The total number of entries returned.
        self.total = total  # type: int

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTracedEventByEventIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = QueryTracedEventByEventIdResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryTracedEventByEventIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The total number of entries returned.
        self.data = data  # type: list[QueryTracedEventByEventIdResponseBodyData]
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTracedEventByEventIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTracedEventByEventIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTracedEventByEventIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTracedEventByEventIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTracedEventByEventIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTracedEventByEventIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTracedEventsRequest(TeaModel):
    def __init__(self, end_time=None, event_bus_name=None, event_source=None, event_type=None, limit=None,
                 matched_rule=None, next_token=None, start_time=None):
        # The end of the time range when event traces are queried. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event source.
        self.event_source = event_source  # type: str
        # The event type.
        self.event_type = event_type  # type: str
        # The maximum number of entries to be returned in a call. You can use this parameter and NextToken to implement paging. Up to 100 entries can be returned in a call.
        self.limit = limit  # type: int
        # The name of the event rule that is matched.
        self.matched_rule = matched_rule  # type: str
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The beginning of the time range to query event traces. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTracedEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.matched_rule is not None:
            result['MatchedRule'] = self.matched_rule
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MatchedRule') is not None:
            self.matched_rule = m.get('MatchedRule')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryTracedEventsResponseBodyDataEvents(TeaModel):
    def __init__(self, event_bus_name=None, event_id=None, event_received_time=None, event_source=None,
                 event_type=None):
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event ID.
        self.event_id = event_id  # type: str
        # The time when the event was delivered to the event bus.
        self.event_received_time = event_received_time  # type: long
        # The name of the event source.
        self.event_source = event_source  # type: str
        # The event type.
        self.event_type = event_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTracedEventsResponseBodyDataEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_received_time is not None:
            result['EventReceivedTime'] = self.event_received_time
        if self.event_source is not None:
            result['EventSource'] = self.event_source
        if self.event_type is not None:
            result['EventType'] = self.event_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventReceivedTime') is not None:
            self.event_received_time = m.get('EventReceivedTime')
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        return self


class QueryTracedEventsResponseBodyData(TeaModel):
    def __init__(self, events=None, next_token=None, total=None):
        # The event type.
        self.events = events  # type: list[QueryTracedEventsResponseBodyDataEvents]
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token  # type: str
        # The total number of entries.
        self.total = total  # type: int

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTracedEventsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = QueryTracedEventsResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryTracedEventsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned HTTP status code. The HTTP status code 200 indicates that the request is successful.
        self.code = code  # type: str
        # The data returned.
        self.data = data  # type: QueryTracedEventsResponseBodyData
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTracedEventsResponseBody, self).to_map()
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
            temp_model = QueryTracedEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTracedEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTracedEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTracedEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTracedEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartEventStreamingRequest(TeaModel):
    def __init__(self, event_streaming_name=None):
        # The name of the event stream that you want to enable.
        self.event_streaming_name = event_streaming_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartEventStreamingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        return self


class StartEventStreamingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code  # type: bool
        # The error message that is returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartEventStreamingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartEventStreamingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartEventStreamingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartEventStreamingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestEventPatternRequest(TeaModel):
    def __init__(self, event=None, event_pattern=None):
        # The event.
        self.event = event  # type: str
        # The event pattern.
        self.event_pattern = event_pattern  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestEventPatternRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['Event'] = self.event
        if self.event_pattern is not None:
            result['EventPattern'] = self.event_pattern
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('EventPattern') is not None:
            self.event_pattern = m.get('EventPattern')
        return self


class TestEventPatternResponseBodyData(TeaModel):
    def __init__(self, result=None):
        # The value true indicates that the event pattern matches the provided JSON format. The value false indicates that the event pattern does not match the provided JSON format.
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestEventPatternResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class TestEventPatternResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The returned result.
        self.data = data  # type: TestEventPatternResponseBodyData
        # The error message returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TestEventPatternResponseBody, self).to_map()
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
            temp_model = TestEventPatternResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TestEventPatternResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TestEventPatternResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TestEventPatternResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TestEventPatternResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApiDestinationRequestHttpApiParameters(TeaModel):
    def __init__(self, endpoint=None, method=None):
        # The endpoint of the API destination. The endpoint can be up to 127 characters in length.
        self.endpoint = endpoint  # type: str
        # The HTTP request method. Valid values:
        # 
        # - GET
        # - POST
        # - HEAD
        # - DELETE
        # - PUT
        # - PATCH
        self.method = method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApiDestinationRequestHttpApiParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class UpdateApiDestinationRequest(TeaModel):
    def __init__(self, api_destination_name=None, connection_name=None, description=None, http_api_parameters=None):
        # The name of the API destination. The name must be 2 to 127 characters in length.
        self.api_destination_name = api_destination_name  # type: str
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # Note: Before you configure this parameter, you must call the CreateConnection operation to create a connection. Then, set this parameter to the name of the connection that you created.
        self.connection_name = connection_name  # type: str
        # The description of the API destination. The description can be up to 255 characters in length.
        self.description = description  # type: str
        # The parameters that are configured for the API destination.
        self.http_api_parameters = http_api_parameters  # type: UpdateApiDestinationRequestHttpApiParameters

    def validate(self):
        if self.http_api_parameters:
            self.http_api_parameters.validate()

    def to_map(self):
        _map = super(UpdateApiDestinationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.http_api_parameters is not None:
            result['HttpApiParameters'] = self.http_api_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpApiParameters') is not None:
            temp_model = UpdateApiDestinationRequestHttpApiParameters()
            self.http_api_parameters = temp_model.from_map(m['HttpApiParameters'])
        return self


class UpdateApiDestinationShrinkRequest(TeaModel):
    def __init__(self, api_destination_name=None, connection_name=None, description=None,
                 http_api_parameters_shrink=None):
        # The name of the API destination. The name must be 2 to 127 characters in length.
        self.api_destination_name = api_destination_name  # type: str
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # Note: Before you configure this parameter, you must call the CreateConnection operation to create a connection. Then, set this parameter to the name of the connection that you created.
        self.connection_name = connection_name  # type: str
        # The description of the API destination. The description can be up to 255 characters in length.
        self.description = description  # type: str
        # The parameters that are configured for the API destination.
        self.http_api_parameters_shrink = http_api_parameters_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApiDestinationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.http_api_parameters_shrink is not None:
            result['HttpApiParameters'] = self.http_api_parameters_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HttpApiParameters') is not None:
            self.http_api_parameters_shrink = m.get('HttpApiParameters')
        return self


class UpdateApiDestinationResponseBody(TeaModel):
    def __init__(self, api_destination_name=None, code=None, message=None, request_id=None):
        # api-destination-name
        self.api_destination_name = api_destination_name  # type: str
        # The response code. If the request is successful, Success is returned.
        self.code = code  # type: str
        # The returned message. If the request is successful, success is returned.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApiDestinationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateApiDestinationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApiDestinationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApiDestinationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateApiDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnectionRequestAuthParametersApiKeyAuthParameters(TeaModel):
    def __init__(self, api_key_name=None, api_key_value=None):
        # The key of the API key.
        self.api_key_name = api_key_name  # type: str
        # The value of the API key.
        self.api_key_value = api_key_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionRequestAuthParametersApiKeyAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key_name is not None:
            result['ApiKeyName'] = self.api_key_name
        if self.api_key_value is not None:
            result['ApiKeyValue'] = self.api_key_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiKeyName') is not None:
            self.api_key_name = m.get('ApiKeyName')
        if m.get('ApiKeyValue') is not None:
            self.api_key_value = m.get('ApiKeyValue')
        return self


class UpdateConnectionRequestAuthParametersBasicAuthParameters(TeaModel):
    def __init__(self, password=None, username=None):
        # The password for basic authentication.
        self.password = password  # type: str
        # The username for basic authentication.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionRequestAuthParametersBasicAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateConnectionRequestAuthParametersOAuthParametersClientParameters(TeaModel):
    def __init__(self, client_id=None, client_secret=None):
        # The client ID.
        self.client_id = client_id  # type: str
        # The AccessKey secret of the client.
        self.client_secret = client_secret  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionRequestAuthParametersOAuthParametersClientParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientID'] = self.client_id
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientID') is not None:
            self.client_id = m.get('ClientID')
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')
        return self


class UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret  # type: str
        # The key of the request body.
        self.key = key  # type: str
        # The value of the request body.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret  # type: str
        # The key of the request header.
        self.key = key  # type: str
        # The value of the request header.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters(TeaModel):
    def __init__(self, is_value_secret=None, key=None, value=None):
        # Specifies whether to enable authentication.
        self.is_value_secret = is_value_secret  # type: str
        # The key of the request path.
        self.key = key  # type: str
        # The value of the request path.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_value_secret is not None:
            result['IsValueSecret'] = self.is_value_secret
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsValueSecret') is not None:
            self.is_value_secret = m.get('IsValueSecret')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters(TeaModel):
    def __init__(self, body_parameters=None, header_parameters=None, query_string_parameters=None):
        # The parameters that are configured for the request body.
        self.body_parameters = body_parameters  # type: list[UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters]
        # The value of the request header.
        self.header_parameters = header_parameters  # type: list[UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters]
        # The parameters that are configured for the request path.
        self.query_string_parameters = query_string_parameters  # type: list[UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters]

    def validate(self):
        if self.body_parameters:
            for k in self.body_parameters:
                if k:
                    k.validate()
        if self.header_parameters:
            for k in self.header_parameters:
                if k:
                    k.validate()
        if self.query_string_parameters:
            for k in self.query_string_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BodyParameters'] = []
        if self.body_parameters is not None:
            for k in self.body_parameters:
                result['BodyParameters'].append(k.to_map() if k else None)
        result['HeaderParameters'] = []
        if self.header_parameters is not None:
            for k in self.header_parameters:
                result['HeaderParameters'].append(k.to_map() if k else None)
        result['QueryStringParameters'] = []
        if self.query_string_parameters is not None:
            for k in self.query_string_parameters:
                result['QueryStringParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body_parameters = []
        if m.get('BodyParameters') is not None:
            for k in m.get('BodyParameters'):
                temp_model = UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersBodyParameters()
                self.body_parameters.append(temp_model.from_map(k))
        self.header_parameters = []
        if m.get('HeaderParameters') is not None:
            for k in m.get('HeaderParameters'):
                temp_model = UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersHeaderParameters()
                self.header_parameters.append(temp_model.from_map(k))
        self.query_string_parameters = []
        if m.get('QueryStringParameters') is not None:
            for k in m.get('QueryStringParameters'):
                temp_model = UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParametersQueryStringParameters()
                self.query_string_parameters.append(temp_model.from_map(k))
        return self


class UpdateConnectionRequestAuthParametersOAuthParameters(TeaModel):
    def __init__(self, authorization_endpoint=None, client_parameters=None, http_method=None,
                 oauth_http_parameters=None):
        # The endpoint that is used to obtain the OAuth token. The endpoint can be up to 127 characters in length.
        self.authorization_endpoint = authorization_endpoint  # type: str
        # The parameters that are configured for the client.
        self.client_parameters = client_parameters  # type: UpdateConnectionRequestAuthParametersOAuthParametersClientParameters
        # The HTTP request method. Valid values:
        # 
        # *   GET
        # *   POST
        # *   HEAD
        # *   DELETE
        # *   PUT
        # *   PATCH
        self.http_method = http_method  # type: str
        # The request parameters for OAuth authentication.
        self.oauth_http_parameters = oauth_http_parameters  # type: UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters

    def validate(self):
        if self.client_parameters:
            self.client_parameters.validate()
        if self.oauth_http_parameters:
            self.oauth_http_parameters.validate()

    def to_map(self):
        _map = super(UpdateConnectionRequestAuthParametersOAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_endpoint is not None:
            result['AuthorizationEndpoint'] = self.authorization_endpoint
        if self.client_parameters is not None:
            result['ClientParameters'] = self.client_parameters.to_map()
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.oauth_http_parameters is not None:
            result['OAuthHttpParameters'] = self.oauth_http_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('AuthorizationEndpoint')
        if m.get('ClientParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParametersOAuthParametersClientParameters()
            self.client_parameters = temp_model.from_map(m['ClientParameters'])
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('OAuthHttpParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParametersOAuthParametersOAuthHttpParameters()
            self.oauth_http_parameters = temp_model.from_map(m['OAuthHttpParameters'])
        return self


class UpdateConnectionRequestAuthParameters(TeaModel):
    def __init__(self, api_key_auth_parameters=None, authorization_type=None, basic_auth_parameters=None,
                 oauth_parameters=None):
        # The parameters for API key authentication.
        self.api_key_auth_parameters = api_key_auth_parameters  # type: UpdateConnectionRequestAuthParametersApiKeyAuthParameters
        # The authentication type. Valid values:
        # 
        # BASIC_AUTH: basic authentication.
        # 
        # Introduction: Basic authentication is a simple authentication scheme built into the HTTP protocol. When you use the HTTP protocol for communications, the authentication method that the HTTP server uses to authenticate user identities on the client is defined in the protocol. The request header is in the Authorization: Basic Base64-encoded string (Username:Password) format.
        # 
        # 1.  Username and Password are required.
        # 
        # API_KEY_AUTH: API key authentication.
        # 
        # Introduction: The request header is in the Token : Token value format.
        # 
        # *   ApiKeyName and ApiKeyValue are required.
        # 
        # OAUTH_AUTH: OAuth authentication.
        # 
        # Introduction: OAuth2.0 is an authentication mechanism. In normal cases, a system that does not use OAuth2.0 can access the resources of the server from the client. To ensure access security, access tokens are used to identify users in OAuth 2.0. The client must use an access token to access protected resources. This way, OAuth 2.0 protects resources from being accessed from malicious clients and improves system security.
        # 
        # *   AuthorizationEndpoint, OAuthHttpParameters, and HttpMethod are required.
        self.authorization_type = authorization_type  # type: str
        # The parameters that are configured for basic authentication.
        self.basic_auth_parameters = basic_auth_parameters  # type: UpdateConnectionRequestAuthParametersBasicAuthParameters
        # The parameters that are configured for OAuth authentication.
        self.oauth_parameters = oauth_parameters  # type: UpdateConnectionRequestAuthParametersOAuthParameters

    def validate(self):
        if self.api_key_auth_parameters:
            self.api_key_auth_parameters.validate()
        if self.basic_auth_parameters:
            self.basic_auth_parameters.validate()
        if self.oauth_parameters:
            self.oauth_parameters.validate()

    def to_map(self):
        _map = super(UpdateConnectionRequestAuthParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key_auth_parameters is not None:
            result['ApiKeyAuthParameters'] = self.api_key_auth_parameters.to_map()
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.basic_auth_parameters is not None:
            result['BasicAuthParameters'] = self.basic_auth_parameters.to_map()
        if self.oauth_parameters is not None:
            result['OAuthParameters'] = self.oauth_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiKeyAuthParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParametersApiKeyAuthParameters()
            self.api_key_auth_parameters = temp_model.from_map(m['ApiKeyAuthParameters'])
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('BasicAuthParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParametersBasicAuthParameters()
            self.basic_auth_parameters = temp_model.from_map(m['BasicAuthParameters'])
        if m.get('OAuthParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParametersOAuthParameters()
            self.oauth_parameters = temp_model.from_map(m['OAuthParameters'])
        return self


class UpdateConnectionRequestNetworkParameters(TeaModel):
    def __init__(self, network_type=None, security_group_id=None, vpc_id=None, vswitche_id=None):
        # PublicNetwork: the Internet.
        # 
        # PrivateNetwork: virtual private cloud (VPC).
        # 
        # Note: If you set this parameter to PrivateNetwork, you must configure VpcId, VswitcheId, and SecurityGroupId.
        self.network_type = network_type  # type: str
        # The ID of the security group.
        self.security_group_id = security_group_id  # type: str
        # The VPC ID.
        self.vpc_id = vpc_id  # type: str
        # The vSwitch ID.
        self.vswitche_id = vswitche_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionRequestNetworkParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitche_id is not None:
            result['VswitcheId'] = self.vswitche_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitcheId') is not None:
            self.vswitche_id = m.get('VswitcheId')
        return self


class UpdateConnectionRequest(TeaModel):
    def __init__(self, auth_parameters=None, connection_name=None, description=None, network_parameters=None):
        # The parameters that are configured for authentication.
        self.auth_parameters = auth_parameters  # type: UpdateConnectionRequestAuthParameters
        # The name of the connection that you want to update. The name must be 2 to 127 characters in length.
        self.connection_name = connection_name  # type: str
        # The description of the connection. The description can be up to 255 characters in length.
        self.description = description  # type: str
        # The parameters that are configured for the network.
        self.network_parameters = network_parameters  # type: UpdateConnectionRequestNetworkParameters

    def validate(self):
        if self.auth_parameters:
            self.auth_parameters.validate()
        if self.network_parameters:
            self.network_parameters.validate()

    def to_map(self):
        _map = super(UpdateConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters is not None:
            result['AuthParameters'] = self.auth_parameters.to_map()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.network_parameters is not None:
            result['NetworkParameters'] = self.network_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            temp_model = UpdateConnectionRequestAuthParameters()
            self.auth_parameters = temp_model.from_map(m['AuthParameters'])
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkParameters') is not None:
            temp_model = UpdateConnectionRequestNetworkParameters()
            self.network_parameters = temp_model.from_map(m['NetworkParameters'])
        return self


class UpdateConnectionShrinkRequest(TeaModel):
    def __init__(self, auth_parameters_shrink=None, connection_name=None, description=None,
                 network_parameters_shrink=None):
        # The parameters that are configured for authentication.
        self.auth_parameters_shrink = auth_parameters_shrink  # type: str
        # The name of the connection that you want to update. The name must be 2 to 127 characters in length.
        self.connection_name = connection_name  # type: str
        # The description of the connection. The description can be up to 255 characters in length.
        self.description = description  # type: str
        # The parameters that are configured for the network.
        self.network_parameters_shrink = network_parameters_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_parameters_shrink is not None:
            result['AuthParameters'] = self.auth_parameters_shrink
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.description is not None:
            result['Description'] = self.description
        if self.network_parameters_shrink is not None:
            result['NetworkParameters'] = self.network_parameters_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            self.auth_parameters_shrink = m.get('AuthParameters')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkParameters') is not None:
            self.network_parameters_shrink = m.get('NetworkParameters')
        return self


class UpdateConnectionResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        # The returned response code.
        self.code = code  # type: str
        # The returned message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventBusRequest(TeaModel):
    def __init__(self, description=None, event_bus_name=None):
        # The description of the event bus.
        self.description = description  # type: str
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventBusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        return self


class UpdateEventBusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The error message returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventBusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventBusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEventBusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEventBusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEventBusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventSourceRequestSourceHttpEventParameters(TeaModel):
    def __init__(self, ip=None, method=None, referer=None, security_config=None, type=None):
        # The CIDR block that is used for security settings. This parameter is required only if SecurityConfig is set to ip. You can enter a CIDR block or an IP address.
        self.ip = ip  # type: list[str]
        # The HTTP request method supported by the generated webhook URL. You can select multiple values. Valid values:
        # 
        # *   GET
        # *   POST
        # *   PUT
        # *   PATCH
        # *   DELETE
        # *   HEAD
        # *   OPTIONS
        # *   TRACE
        # *   CONNECT
        self.method = method  # type: list[str]
        # The security domain name. This parameter is required only if SecurityConfig is set to referer. You can enter a domain name.
        self.referer = referer  # type: list[str]
        # The type of security settings. Valid values:
        # 
        # *   none: No configuration is required.
        # *   ip: CIDR block.
        # *   referer: security domain name.
        self.security_config = security_config  # type: str
        # The protocol type that is supported by the generated webhook URL. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # *   HTTP\&HTTPS
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventSourceRequestSourceHttpEventParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.method is not None:
            result['Method'] = self.method
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.security_config is not None:
            result['SecurityConfig'] = self.security_config
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SecurityConfig') is not None:
            self.security_config = m.get('SecurityConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateEventSourceRequestSourceKafkaParameters(TeaModel):
    def __init__(self, consumer_group=None, instance_id=None, maximum_tasks=None, network=None, offset_reset=None,
                 region_id=None, security_group_id=None, topic=None, v_switch_ids=None, vpc_id=None):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group  # type: str
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id  # type: str
        # The maximum number of consumers.
        self.maximum_tasks = maximum_tasks  # type: int
        # The network. Valid values: Default and PublicNetwork. Default value: Default. The value PublicNetwork indicates a self-managed network.
        self.network = network  # type: str
        # The consumer offset.
        self.offset_reset = offset_reset  # type: str
        # The ID of the region where the Message Queue for Apache Kafka instance resides.
        self.region_id = region_id  # type: str
        # The ID of the security group to which the Message Queue for Apache Kafka instance belongs. This parameter is required only if you set Network to PublicNetwork.
        self.security_group_id = security_group_id  # type: str
        # The name of the topic on the Message Queue for Apache Kafka instance.
        self.topic = topic  # type: str
        # The ID of the vSwitch with which the Message Queue for Apache Kafka instance is associated. This parameter is required only if you set Network to PublicNetwork.
        self.v_switch_ids = v_switch_ids  # type: str
        # The ID of the VPC in which the Message Queue for Apache Kafka instance resides. This parameter is required only if you set Network to PublicNetwork.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventSourceRequestSourceKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateEventSourceRequestSourceMNSParameters(TeaModel):
    def __init__(self, is_base_64decode=None, queue_name=None, region_id=None):
        # Indicates whether Base64 decoding is enabled. By default, Base64 decoding is enabled.
        self.is_base_64decode = is_base_64decode  # type: bool
        # The name of the MNS queue.
        self.queue_name = queue_name  # type: str
        # The region where the MNS queue resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventSourceRequestSourceMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateEventSourceRequestSourceRabbitMQParameters(TeaModel):
    def __init__(self, instance_id=None, queue_name=None, region_id=None, virtual_host_name=None):
        # The ID of the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.instance_id = instance_id  # type: str
        # The name of the queue on the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.queue_name = queue_name  # type: str
        # The ID of the region where the Message Queue for RabbitMQ instance resides.
        self.region_id = region_id  # type: str
        # The name of the vhost of the Message Queue for RabbitMQ instance. For more information, see [Limits](~~163289~~).
        self.virtual_host_name = virtual_host_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventSourceRequestSourceRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class UpdateEventSourceRequestSourceRocketMQParameters(TeaModel):
    def __init__(self, auth_type=None, group_id=None, instance_endpoint=None, instance_id=None,
                 instance_network=None, instance_password=None, instance_security_group_id=None, instance_type=None,
                 instance_username=None, instance_vswitch_ids=None, instance_vpc_id=None, offset=None, region_id=None, tag=None,
                 timestamp=None, topic=None):
        # The authentication type. You can set this parameter to ACL or leave this parameter empty.
        self.auth_type = auth_type  # type: str
        # The ID of the consumer group on the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id  # type: str
        # The endpoint that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_endpoint = instance_endpoint  # type: str
        # The ID of the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.instance_id = instance_id  # type: str
        # None.
        self.instance_network = instance_network  # type: str
        # The password that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_password = instance_password  # type: str
        # The ID of the security group to which the Message Queue for Apache RocketMQ instance belongs.
        self.instance_security_group_id = instance_security_group_id  # type: str
        # The type of the Message Queue for Apache RocketMQ instance. Valid values:
        # 
        # *   Cloud\_4: Message Queue for Apache RocketMQ 4.0 instance.
        # *   Cloud\_5: Message Queue for Apache RocketMQ 5.0 instance.
        self.instance_type = instance_type  # type: str
        # The username that is used to access the Message Queue for Apache RocketMQ instance.
        self.instance_username = instance_username  # type: str
        # The ID of the vSwitch with which the Message Queue for Apache RocketMQ instance is associated.
        self.instance_vswitch_ids = instance_vswitch_ids  # type: str
        # The ID of the virtual private cloud (VPC) in which the Message Queue for Apache RocketMQ instance resides.
        self.instance_vpc_id = instance_vpc_id  # type: str
        # The offset from which message consumption starts. Valid values:
        # 
        # *   CONSUME_FROM_LAST_OFFSET: Start message consumption from the latest offset.
        # *   CONSUME_FROM_FIRST_OFFSET: Start message consumption from the earliest offset.
        # *   CONSUME_FROM_TIMESTAMP: Start message consumption from the offset at the specified point in time.
        # 
        # Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset  # type: str
        # The region where the Message Queue for Apache RocketMQ instance resides.
        self.region_id = region_id  # type: str
        # The tag that is used to filter messages.
        self.tag = tag  # type: str
        # The timestamp that specifies the time from which messages are consumed. This parameter is valid only if you set Offset to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp  # type: long
        # The name of the topic on the Message Queue for Apache RocketMQ instance. For more information, see [Limits](~~163289~~).
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventSourceRequestSourceRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateEventSourceRequestSourceSLSParameters(TeaModel):
    def __init__(self, consume_position=None, log_store=None, project=None, role_name=None):
        # The starting consumer offset. The value begin indicates the earliest offset, and the value end indicates the latest offset. You can also specify a time in seconds to start consumption.
        self.consume_position = consume_position  # type: str
        # The Log Service Logstore.
        self.log_store = log_store  # type: str
        # The Log Service project.
        self.project = project  # type: str
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console. For information about the permission policy of this role, see Create a custom event source of the Log Service type.
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventSourceRequestSourceSLSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_position is not None:
            result['ConsumePosition'] = self.consume_position
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumePosition') is not None:
            self.consume_position = m.get('ConsumePosition')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdateEventSourceRequestSourceScheduledEventParameters(TeaModel):
    def __init__(self, schedule=None, time_zone=None, user_data=None):
        # The cron expression.
        self.schedule = schedule  # type: str
        # The time zone in which the cron expression is executed.
        self.time_zone = time_zone  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventSourceRequestSourceScheduledEventParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class UpdateEventSourceRequest(TeaModel):
    def __init__(self, description=None, event_bus_name=None, event_source_name=None,
                 source_http_event_parameters=None, source_kafka_parameters=None, source_mnsparameters=None, source_rabbit_mqparameters=None,
                 source_rocket_mqparameters=None, source_slsparameters=None, source_scheduled_event_parameters=None):
        # The description of the event source.
        self.description = description  # type: str
        # The event bus with which the event source is associated.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event source.
        self.event_source_name = event_source_name  # type: str
        # The parameters that are configured if the event source is HTTP events.
        self.source_http_event_parameters = source_http_event_parameters  # type: UpdateEventSourceRequestSourceHttpEventParameters
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters = source_kafka_parameters  # type: UpdateEventSourceRequestSourceKafkaParameters
        # The parameters that are configured if the event source is Message Service (MNS).
        self.source_mnsparameters = source_mnsparameters  # type: UpdateEventSourceRequestSourceMNSParameters
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters  # type: UpdateEventSourceRequestSourceRabbitMQParameters
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters = source_rocket_mqparameters  # type: UpdateEventSourceRequestSourceRocketMQParameters
        # SourceSLSParameters
        self.source_slsparameters = source_slsparameters  # type: UpdateEventSourceRequestSourceSLSParameters
        # The parameters that are configured if you specify scheduled events as the event source.
        self.source_scheduled_event_parameters = source_scheduled_event_parameters  # type: UpdateEventSourceRequestSourceScheduledEventParameters

    def validate(self):
        if self.source_http_event_parameters:
            self.source_http_event_parameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()
        if self.source_scheduled_event_parameters:
            self.source_scheduled_event_parameters.validate()

    def to_map(self):
        _map = super(UpdateEventSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.source_http_event_parameters is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        if self.source_scheduled_event_parameters is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('SourceHttpEventParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceHttpEventParameters()
            self.source_http_event_parameters = temp_model.from_map(m['SourceHttpEventParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        if m.get('SourceScheduledEventParameters') is not None:
            temp_model = UpdateEventSourceRequestSourceScheduledEventParameters()
            self.source_scheduled_event_parameters = temp_model.from_map(m['SourceScheduledEventParameters'])
        return self


class UpdateEventSourceShrinkRequest(TeaModel):
    def __init__(self, description=None, event_bus_name=None, event_source_name=None,
                 source_http_event_parameters_shrink=None, source_kafka_parameters_shrink=None, source_mnsparameters_shrink=None,
                 source_rabbit_mqparameters_shrink=None, source_rocket_mqparameters_shrink=None, source_slsparameters_shrink=None,
                 source_scheduled_event_parameters_shrink=None):
        # The description of the event source.
        self.description = description  # type: str
        # The event bus with which the event source is associated.
        self.event_bus_name = event_bus_name  # type: str
        # The name of the event source.
        self.event_source_name = event_source_name  # type: str
        # The parameters that are configured if the event source is HTTP events.
        self.source_http_event_parameters_shrink = source_http_event_parameters_shrink  # type: str
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters_shrink = source_kafka_parameters_shrink  # type: str
        # The parameters that are configured if the event source is Message Service (MNS).
        self.source_mnsparameters_shrink = source_mnsparameters_shrink  # type: str
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters_shrink = source_rabbit_mqparameters_shrink  # type: str
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters_shrink = source_rocket_mqparameters_shrink  # type: str
        # SourceSLSParameters
        self.source_slsparameters_shrink = source_slsparameters_shrink  # type: str
        # The parameters that are configured if you specify scheduled events as the event source.
        self.source_scheduled_event_parameters_shrink = source_scheduled_event_parameters_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventSourceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name
        if self.source_http_event_parameters_shrink is not None:
            result['SourceHttpEventParameters'] = self.source_http_event_parameters_shrink
        if self.source_kafka_parameters_shrink is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters_shrink
        if self.source_mnsparameters_shrink is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters_shrink
        if self.source_rabbit_mqparameters_shrink is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters_shrink
        if self.source_rocket_mqparameters_shrink is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters_shrink
        if self.source_slsparameters_shrink is not None:
            result['SourceSLSParameters'] = self.source_slsparameters_shrink
        if self.source_scheduled_event_parameters_shrink is not None:
            result['SourceScheduledEventParameters'] = self.source_scheduled_event_parameters_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')
        if m.get('SourceHttpEventParameters') is not None:
            self.source_http_event_parameters_shrink = m.get('SourceHttpEventParameters')
        if m.get('SourceKafkaParameters') is not None:
            self.source_kafka_parameters_shrink = m.get('SourceKafkaParameters')
        if m.get('SourceMNSParameters') is not None:
            self.source_mnsparameters_shrink = m.get('SourceMNSParameters')
        if m.get('SourceRabbitMQParameters') is not None:
            self.source_rabbit_mqparameters_shrink = m.get('SourceRabbitMQParameters')
        if m.get('SourceRocketMQParameters') is not None:
            self.source_rocket_mqparameters_shrink = m.get('SourceRocketMQParameters')
        if m.get('SourceSLSParameters') is not None:
            self.source_slsparameters_shrink = m.get('SourceSLSParameters')
        if m.get('SourceScheduledEventParameters') is not None:
            self.source_scheduled_event_parameters_shrink = m.get('SourceScheduledEventParameters')
        return self


class UpdateEventSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The returned response code. Valid values:
        # 
        # *   Success: The request is successful.
        # *   Other codes: The request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The result of the operation.
        self.data = data  # type: bool
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. The value true indicates that the operation is successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventSourceResponseBody, self).to_map()
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


class UpdateEventSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEventSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEventSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventStreamingRequestRunOptionsBatchWindow(TeaModel):
    def __init__(self, count_based_window=None, time_based_window=None):
        # The maximum number of events that is allowed in the batch window. If the value specified by this parameter is reached, the data in the batch window is pushed to the downstream application. If multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.count_based_window = count_based_window  # type: int
        # The maximum period of time during which events are allowed in the batch window. Unit: seconds. If the value specified by this parameter is reached, the data in the batch window is pushed to the downstream application. If multiple batch windows exist, data is pushed if triggering conditions are met in one of the windows.
        self.time_based_window = time_based_window  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestRunOptionsBatchWindow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class UpdateEventStreamingRequestRunOptionsDeadLetterQueue(TeaModel):
    def __init__(self, arn=None):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue.
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestRunOptionsDeadLetterQueue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class UpdateEventStreamingRequestRunOptionsRetryStrategy(TeaModel):
    def __init__(self, maximum_event_age_in_seconds=None, maximum_retry_attempts=None, push_retry_strategy=None):
        # The maximum period of time during which retries are performed.
        self.maximum_event_age_in_seconds = maximum_event_age_in_seconds  # type: long
        # The maximum number of retries.
        self.maximum_retry_attempts = maximum_retry_attempts  # type: long
        # The retry policy that is used if an event failed to be pushed. Valid values: BACKOFF_RETRY and EXPONENTIAL_DECAY_RETRY.
        self.push_retry_strategy = push_retry_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestRunOptionsRetryStrategy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_event_age_in_seconds is not None:
            result['MaximumEventAgeInSeconds'] = self.maximum_event_age_in_seconds
        if self.maximum_retry_attempts is not None:
            result['MaximumRetryAttempts'] = self.maximum_retry_attempts
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaximumEventAgeInSeconds') is not None:
            self.maximum_event_age_in_seconds = m.get('MaximumEventAgeInSeconds')
        if m.get('MaximumRetryAttempts') is not None:
            self.maximum_retry_attempts = m.get('MaximumRetryAttempts')
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class UpdateEventStreamingRequestRunOptions(TeaModel):
    def __init__(self, batch_window=None, dead_letter_queue=None, errors_tolerance=None, maximum_tasks=None,
                 retry_strategy=None):
        # The information about the batch window.
        self.batch_window = batch_window  # type: UpdateEventStreamingRequestRunOptionsBatchWindow
        # Specifies whether to enable dead-letter queues. By default, dead-letter queues are disabled. Messages that fail to be pushed are discarded after the maximum number of retries specified by the retry policy is reached.
        self.dead_letter_queue = dead_letter_queue  # type: UpdateEventStreamingRequestRunOptionsDeadLetterQueue
        # The fault tolerance policy. The value NONE specifies that faults are not tolerated, and the value All specifies that all faults are tolerated.
        self.errors_tolerance = errors_tolerance  # type: str
        # The concurrency level.
        self.maximum_tasks = maximum_tasks  # type: long
        # The information about the retry policy that is used if the event fails to be pushed.
        self.retry_strategy = retry_strategy  # type: UpdateEventStreamingRequestRunOptionsRetryStrategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequestRunOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['BatchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance
        if self.maximum_tasks is not None:
            result['MaximumTasks'] = self.maximum_tasks
        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchWindow') is not None:
            temp_model = UpdateEventStreamingRequestRunOptionsBatchWindow()
            self.batch_window = temp_model.from_map(m['BatchWindow'])
        if m.get('DeadLetterQueue') is not None:
            temp_model = UpdateEventStreamingRequestRunOptionsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['DeadLetterQueue'])
        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')
        if m.get('MaximumTasks') is not None:
            self.maximum_tasks = m.get('MaximumTasks')
        if m.get('RetryStrategy') is not None:
            temp_model = UpdateEventStreamingRequestRunOptionsRetryStrategy()
            self.retry_strategy = temp_model.from_map(m['RetryStrategy'])
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFcParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersConcurrency(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The delivery concurrency. Minimum value: 1.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFcParametersConcurrency, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersFunctionName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The name of the Function Compute function.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFcParametersFunctionName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersInvocationType(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The invocation type. Valid values: Sync and Async.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFcParametersInvocationType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersQualifier(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The alias of the service to which the function belongs.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFcParametersQualifier, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParametersServiceName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The name of the Function Compute service.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFcParametersServiceName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFcParameters(TeaModel):
    def __init__(self, body=None, concurrency=None, function_name=None, invocation_type=None, qualifier=None,
                 service_name=None):
        # The message body that is sent to the function.
        self.body = body  # type: UpdateEventStreamingRequestSinkSinkFcParametersBody
        # The information about the delivery concurrency.
        self.concurrency = concurrency  # type: UpdateEventStreamingRequestSinkSinkFcParametersConcurrency
        # The information about the Function Compute function.
        self.function_name = function_name  # type: UpdateEventStreamingRequestSinkSinkFcParametersFunctionName
        # The information about the invocation type.
        self.invocation_type = invocation_type  # type: UpdateEventStreamingRequestSinkSinkFcParametersInvocationType
        # The information about the service to which the function belongs.
        self.qualifier = qualifier  # type: UpdateEventStreamingRequestSinkSinkFcParametersQualifier
        # The information about the Function Compute service.
        self.service_name = service_name  # type: UpdateEventStreamingRequestSinkSinkFcParametersServiceName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.concurrency:
            self.concurrency.validate()
        if self.function_name:
            self.function_name.validate()
        if self.invocation_type:
            self.invocation_type.validate()
        if self.qualifier:
            self.qualifier.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFcParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name.to_map()
        if self.invocation_type is not None:
            result['InvocationType'] = self.invocation_type.to_map()
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Concurrency') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersConcurrency()
            self.concurrency = temp_model.from_map(m['Concurrency'])
        if m.get('FunctionName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersFunctionName()
            self.function_name = temp_model.from_map(m['FunctionName'])
        if m.get('InvocationType') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersInvocationType()
            self.invocation_type = temp_model.from_map(m['InvocationType'])
        if m.get('Qualifier') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersQualifier()
            self.qualifier = temp_model.from_map(m['Qualifier'])
        if m.get('ServiceName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParametersServiceName()
            self.service_name = temp_model.from_map(m['ServiceName'])
        return self


class UpdateEventStreamingRequestSinkSinkFnfParametersExecutionName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFnfParametersExecutionName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFnfParametersFlowName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFnfParametersFlowName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFnfParametersInput(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFnfParametersInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFnfParametersRoleName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        self.form = form  # type: str
        self.template = template  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFnfParametersRoleName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkFnfParameters(TeaModel):
    def __init__(self, execution_name=None, flow_name=None, input=None, role_name=None):
        self.execution_name = execution_name  # type: UpdateEventStreamingRequestSinkSinkFnfParametersExecutionName
        self.flow_name = flow_name  # type: UpdateEventStreamingRequestSinkSinkFnfParametersFlowName
        self.input = input  # type: UpdateEventStreamingRequestSinkSinkFnfParametersInput
        self.role_name = role_name  # type: UpdateEventStreamingRequestSinkSinkFnfParametersRoleName

    def validate(self):
        if self.execution_name:
            self.execution_name.validate()
        if self.flow_name:
            self.flow_name.validate()
        if self.input:
            self.input.validate()
        if self.role_name:
            self.role_name.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkFnfParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name.to_map()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name.to_map()
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFnfParametersExecutionName()
            self.execution_name = temp_model.from_map(m['ExecutionName'])
        if m.get('FlowName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFnfParametersFlowName()
            self.flow_name = temp_model.from_map(m['FlowName'])
        if m.get('Input') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFnfParametersInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('RoleName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFnfParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersAcks(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The ACK mode. If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high. If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader. If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkKafkaParametersAcks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The ID of the Message Queue for Apache Kafka instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersKey(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The message key.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkKafkaParametersKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The name of the topic in Message Queue for Apache Kafka instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkKafkaParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParametersValue(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkKafkaParametersValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkKafkaParameters(TeaModel):
    def __init__(self, acks=None, instance_id=None, key=None, topic=None, value=None):
        # The information about the acknowledgment (ACK) mode. If you set this parameter to 0, no response is returned from the broker. In this mode, the performance is high, but the risk of data loss is also high. If you set this parameter to 1, a response is returned when data is written to the leader. In this mode, the performance and the risk of data loss are moderate. Data loss may occur if a failure occurs on the leader. If you set this parameter to all, a response is returned when data is written to the leader and synchronized to the followers. In this mode, the performance is low, but the risk of data loss is also low. Data loss occurs if the leader and the followers fail at the same time.
        self.acks = acks  # type: UpdateEventStreamingRequestSinkSinkKafkaParametersAcks
        # The information about the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id  # type: UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId
        # The information about the message key.
        self.key = key  # type: UpdateEventStreamingRequestSinkSinkKafkaParametersKey
        # The information about the topic in Message Queue for Apache Kafka instance.
        self.topic = topic  # type: UpdateEventStreamingRequestSinkSinkKafkaParametersTopic
        # The information about the message value.
        self.value = value  # type: UpdateEventStreamingRequestSinkSinkKafkaParametersValue

    def validate(self):
        if self.acks:
            self.acks.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.key:
            self.key.validate()
        if self.topic:
            self.topic.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acks is not None:
            result['Acks'] = self.acks.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.key is not None:
            result['Key'] = self.key.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acks') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersAcks()
            self.acks = temp_model.from_map(m['Acks'])
        if m.get('InstanceId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Key') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersKey()
            self.key = temp_model.from_map(m['Key'])
        if m.get('Topic') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        if m.get('Value') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParametersValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class UpdateEventStreamingRequestSinkSinkMNSParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkMNSParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # Specifies that Base64 encoding is enabled.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkMNSParametersQueueName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The name of the queue in MNS.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkMNSParametersQueueName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkMNSParameters(TeaModel):
    def __init__(self, body=None, is_base_64encode=None, queue_name=None):
        # The message content.
        self.body = body  # type: UpdateEventStreamingRequestSinkSinkMNSParametersBody
        # Specifies whether to enable Base64 encoding.
        self.is_base_64encode = is_base_64encode  # type: UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode
        # The information about the MNS queue.
        self.queue_name = queue_name  # type: UpdateEventStreamingRequestSinkSinkMNSParametersQueueName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.is_base_64encode:
            self.is_base_64encode.validate()
        if self.queue_name:
            self.queue_name.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.is_base_64encode is not None:
            result['IsBase64Encode'] = self.is_base_64encode.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('IsBase64Encode') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParametersIsBase64Encode()
            self.is_base_64encode = temp_model.from_map(m['IsBase64Encode'])
        if m.get('QueueName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The name of the exchange in the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The ID of the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The name of the queue in the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The routing rule of the message.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The type of the resource to which events are delivered. Valid values: Exchange: exchanges. Queue: queues.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The vhost name of the Message Queue for RabbitMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRabbitMQParameters(TeaModel):
    def __init__(self, body=None, exchange=None, instance_id=None, message_id=None, properties=None, queue_name=None,
                 routing_key=None, target_type=None, virtual_host_name=None):
        # The message content.
        self.body = body  # type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody
        # The information about the exchange to which events are delivered. This parameter is available only if you set TargetType to Exchange.
        self.exchange = exchange  # type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange
        # The information about the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id  # type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId
        # The message ID.
        self.message_id = message_id  # type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId
        # The properties that are used to filter messages.
        self.properties = properties  # type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties
        # The information about the queue to which events are delivered. This parameter is available only if you set TargetType to Queue.
        self.queue_name = queue_name  # type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName
        # The information about the routing rule of the message. This parameter is available only if you set TargetType to Exchange.
        self.routing_key = routing_key  # type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey
        # The information about the type of the resource to which events are delivered.
        self.target_type = target_type  # type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType
        # The information about the vhost of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name  # type: UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName

    def validate(self):
        if self.body:
            self.body.validate()
        if self.exchange:
            self.exchange.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.message_id:
            self.message_id.validate()
        if self.properties:
            self.properties.validate()
        if self.queue_name:
            self.queue_name.validate()
        if self.routing_key:
            self.routing_key.validate()
        if self.target_type:
            self.target_type.validate()
        if self.virtual_host_name:
            self.virtual_host_name.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.exchange is not None:
            result['Exchange'] = self.exchange.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.message_id is not None:
            result['MessageId'] = self.message_id.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name.to_map()
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type.to_map()
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('Exchange') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersExchange()
            self.exchange = temp_model.from_map(m['Exchange'])
        if m.get('InstanceId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('MessageId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersMessageId()
            self.message_id = temp_model.from_map(m['MessageId'])
        if m.get('Properties') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('QueueName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersQueueName()
            self.queue_name = temp_model.from_map(m['QueueName'])
        if m.get('RoutingKey') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersRoutingKey()
            self.routing_key = temp_model.from_map(m['RoutingKey'])
        if m.get('TargetType') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersTargetType()
            self.target_type = temp_model.from_map(m['TargetType'])
        if m.get('VirtualHostName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParametersVirtualHostName()
            self.virtual_host_name = temp_model.from_map(m['VirtualHostName'])
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRocketMQParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersTags(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRocketMQParametersTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The name of the topic in the Message Queue for Apache RocketMQ instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkRocketMQParameters(TeaModel):
    def __init__(self, body=None, instance_id=None, keys=None, properties=None, tags=None, topic=None):
        # The message content.
        self.body = body  # type: UpdateEventStreamingRequestSinkSinkRocketMQParametersBody
        # The parameters that are configured if the event target is Message Queue for Apache RocketMQ.
        self.instance_id = instance_id  # type: UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId
        # The properties that are used to filter messages.
        self.keys = keys  # type: UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys
        # The properties that are used to filter messages.
        self.properties = properties  # type: UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties
        # The properties that are used to filter messages.
        self.tags = tags  # type: UpdateEventStreamingRequestSinkSinkRocketMQParametersTags
        # The information about the topic in the Message Queue for Apache RocketMQ instance.
        self.topic = topic  # type: UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.instance_id:
            self.instance_id.validate()
        if self.keys:
            self.keys.validate()
        if self.properties:
            self.properties.validate()
        if self.tags:
            self.tags.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('InstanceId') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('Keys') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('Properties') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Tags') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersBody(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events.
        self.form = form  # type: str
        # The template based on which events are transformed.
        self.template = template  # type: str
        # The value before event transformation.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkSLSParametersBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersLogStore(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The Log Service Logstore.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkSLSParametersLogStore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersProject(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The Log Service project.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkSLSParametersProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersRoleName(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkSLSParametersRoleName, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParametersTopic(TeaModel):
    def __init__(self, form=None, template=None, value=None):
        # The method that is used to transform events. Default value: CONSTANT.
        self.form = form  # type: str
        # None.
        self.template = template  # type: str
        # The name of the topic in which logs are stored. The topic corresponds to the topic reserved field in Log Service.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkSLSParametersTopic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.form is not None:
            result['Form'] = self.form
        if self.template is not None:
            result['Template'] = self.template
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateEventStreamingRequestSinkSinkSLSParameters(TeaModel):
    def __init__(self, body=None, log_store=None, project=None, role_name=None, topic=None):
        # The message body that is sent to Log Service.
        self.body = body  # type: UpdateEventStreamingRequestSinkSinkSLSParametersBody
        # The information about the Log Service Logstore.
        self.log_store = log_store  # type: UpdateEventStreamingRequestSinkSinkSLSParametersLogStore
        # The information about the Log Service project.
        self.project = project  # type: UpdateEventStreamingRequestSinkSinkSLSParametersProject
        # The information about the role. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the RAM console.
        self.role_name = role_name  # type: UpdateEventStreamingRequestSinkSinkSLSParametersRoleName
        # The information about the topic in which logs are stored. The topic corresponds to the topic reserved field in Log Service.
        self.topic = topic  # type: UpdateEventStreamingRequestSinkSinkSLSParametersTopic

    def validate(self):
        if self.body:
            self.body.validate()
        if self.log_store:
            self.log_store.validate()
        if self.project:
            self.project.validate()
        if self.role_name:
            self.role_name.validate()
        if self.topic:
            self.topic.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSinkSinkSLSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        if self.log_store is not None:
            result['LogStore'] = self.log_store.to_map()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.role_name is not None:
            result['RoleName'] = self.role_name.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersBody()
            self.body = temp_model.from_map(m['Body'])
        if m.get('LogStore') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersLogStore()
            self.log_store = temp_model.from_map(m['LogStore'])
        if m.get('Project') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RoleName') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersRoleName()
            self.role_name = temp_model.from_map(m['RoleName'])
        if m.get('Topic') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParametersTopic()
            self.topic = temp_model.from_map(m['Topic'])
        return self


class UpdateEventStreamingRequestSink(TeaModel):
    def __init__(self, sink_fc_parameters=None, sink_fnf_parameters=None, sink_kafka_parameters=None,
                 sink_mnsparameters=None, sink_rabbit_mqparameters=None, sink_rocket_mqparameters=None, sink_slsparameters=None):
        # The parameters that are configured if the event target is Function Compute.
        self.sink_fc_parameters = sink_fc_parameters  # type: UpdateEventStreamingRequestSinkSinkFcParameters
        self.sink_fnf_parameters = sink_fnf_parameters  # type: UpdateEventStreamingRequestSinkSinkFnfParameters
        # The parameters that are configured if the event target is Message Queue for Apache Kafka.
        self.sink_kafka_parameters = sink_kafka_parameters  # type: UpdateEventStreamingRequestSinkSinkKafkaParameters
        # The parameters that are configured if the event target is MNS.
        self.sink_mnsparameters = sink_mnsparameters  # type: UpdateEventStreamingRequestSinkSinkMNSParameters
        # The parameters that are configured if the event target is Message Queue for RabbitMQ.
        self.sink_rabbit_mqparameters = sink_rabbit_mqparameters  # type: UpdateEventStreamingRequestSinkSinkRabbitMQParameters
        # Sink RocketMQ Parameters
        self.sink_rocket_mqparameters = sink_rocket_mqparameters  # type: UpdateEventStreamingRequestSinkSinkRocketMQParameters
        # Sink SLS Parameters
        self.sink_slsparameters = sink_slsparameters  # type: UpdateEventStreamingRequestSinkSinkSLSParameters

    def validate(self):
        if self.sink_fc_parameters:
            self.sink_fc_parameters.validate()
        if self.sink_fnf_parameters:
            self.sink_fnf_parameters.validate()
        if self.sink_kafka_parameters:
            self.sink_kafka_parameters.validate()
        if self.sink_mnsparameters:
            self.sink_mnsparameters.validate()
        if self.sink_rabbit_mqparameters:
            self.sink_rabbit_mqparameters.validate()
        if self.sink_rocket_mqparameters:
            self.sink_rocket_mqparameters.validate()
        if self.sink_slsparameters:
            self.sink_slsparameters.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSink, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sink_fc_parameters is not None:
            result['SinkFcParameters'] = self.sink_fc_parameters.to_map()
        if self.sink_fnf_parameters is not None:
            result['SinkFnfParameters'] = self.sink_fnf_parameters.to_map()
        if self.sink_kafka_parameters is not None:
            result['SinkKafkaParameters'] = self.sink_kafka_parameters.to_map()
        if self.sink_mnsparameters is not None:
            result['SinkMNSParameters'] = self.sink_mnsparameters.to_map()
        if self.sink_rabbit_mqparameters is not None:
            result['SinkRabbitMQParameters'] = self.sink_rabbit_mqparameters.to_map()
        if self.sink_rocket_mqparameters is not None:
            result['SinkRocketMQParameters'] = self.sink_rocket_mqparameters.to_map()
        if self.sink_slsparameters is not None:
            result['SinkSLSParameters'] = self.sink_slsparameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SinkFcParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFcParameters()
            self.sink_fc_parameters = temp_model.from_map(m['SinkFcParameters'])
        if m.get('SinkFnfParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkFnfParameters()
            self.sink_fnf_parameters = temp_model.from_map(m['SinkFnfParameters'])
        if m.get('SinkKafkaParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkKafkaParameters()
            self.sink_kafka_parameters = temp_model.from_map(m['SinkKafkaParameters'])
        if m.get('SinkMNSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkMNSParameters()
            self.sink_mnsparameters = temp_model.from_map(m['SinkMNSParameters'])
        if m.get('SinkRabbitMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRabbitMQParameters()
            self.sink_rabbit_mqparameters = temp_model.from_map(m['SinkRabbitMQParameters'])
        if m.get('SinkRocketMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkRocketMQParameters()
            self.sink_rocket_mqparameters = temp_model.from_map(m['SinkRocketMQParameters'])
        if m.get('SinkSLSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSinkSinkSLSParameters()
            self.sink_slsparameters = temp_model.from_map(m['SinkSLSParameters'])
        return self


class UpdateEventStreamingRequestSourceSourceDTSParameters(TeaModel):
    def __init__(self, broker_url=None, init_check_point=None, password=None, sid=None, task_id=None, topic=None,
                 username=None):
        # The URL and port number of the data subscription channel.
        self.broker_url = broker_url  # type: str
        # The consumer offset. A consumer offset is a timestamp that indicates when the SDK client consumes the first data record. The value is a UNIX timestamp.
        self.init_check_point = init_check_point  # type: long
        # The password of the consumer group.
        self.password = password  # type: str
        # The ID of the consumer group.
        self.sid = sid  # type: str
        # The task ID.
        self.task_id = task_id  # type: str
        # The topic to which you want to subscribe by using the data subscription channel.
        self.topic = topic  # type: str
        # The username of the consumer group.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSourceSourceDTSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateEventStreamingRequestSourceSourceKafkaParameters(TeaModel):
    def __init__(self, consumer_group=None, instance_id=None, network=None, offset_reset=None, region_id=None,
                 security_group_id=None, topic=None, v_switch_ids=None, vpc_id=None):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group  # type: str
        # The ID of the Message Queue for Apache Kafka instance.
        self.instance_id = instance_id  # type: str
        # The network. Default value: Default. The value PublicNetwork specifies a virtual private cloud (VPC).
        self.network = network  # type: str
        # The offset.
        self.offset_reset = offset_reset  # type: str
        # The ID of the region where the Message Queue for Apache Kafka instance resides.
        self.region_id = region_id  # type: str
        # The ID of the security group to which the Message Queue for Apache Kafka instance belongs.
        self.security_group_id = security_group_id  # type: str
        # The name of the topic in the Message Queue for Apache Kafka instance.
        self.topic = topic  # type: str
        # The ID of the vSwitch with which the Message Queue for Apache Kafka instance is associated.
        self.v_switch_ids = v_switch_ids  # type: str
        # The ID of the VPC to which the Message Queue for Apache Kafka instance belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSourceSourceKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateEventStreamingRequestSourceSourceMNSParameters(TeaModel):
    def __init__(self, is_base_64decode=None, queue_name=None, region_id=None):
        # Specifies whether to enable Base64 encoding. Default value: true.
        self.is_base_64decode = is_base_64decode  # type: bool
        # The queue name.
        self.queue_name = queue_name  # type: str
        # The ID of the region where the MNS queue resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSourceSourceMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateEventStreamingRequestSourceSourceMQTTParameters(TeaModel):
    def __init__(self, instance_id=None, region_id=None, topic=None):
        # The ID of the Message Queue for MQTT instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region where the Message Queue for MQTT resides.
        self.region_id = region_id  # type: str
        # The name of the topic in the Message Queue for MQTT instance.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSourceSourceMQTTParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateEventStreamingRequestSourceSourceRabbitMQParameters(TeaModel):
    def __init__(self, instance_id=None, queue_name=None, region_id=None, virtual_host_name=None):
        # The ID of the Message Queue for RabbitMQ instance.
        self.instance_id = instance_id  # type: str
        # The name of the queue in the Message Queue for RabbitMQ instance.
        self.queue_name = queue_name  # type: str
        # The ID of the region where the Message Queue for RabbitMQ instance resides.
        self.region_id = region_id  # type: str
        # The vhost name of the Message Queue for RabbitMQ instance.
        self.virtual_host_name = virtual_host_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSourceSourceRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class UpdateEventStreamingRequestSourceSourceRocketMQParameters(TeaModel):
    def __init__(self, auth_type=None, group_id=None, instance_endpoint=None, instance_id=None,
                 instance_network=None, instance_password=None, instance_security_group_id=None, instance_type=None,
                 instance_username=None, instance_vswitch_ids=None, instance_vpc_id=None, offset=None, region_id=None, tag=None,
                 timestamp=None, topic=None):
        self.auth_type = auth_type  # type: str
        # The ID of the consumer group in the Message Queue for Apache RocketMQ instance.
        self.group_id = group_id  # type: str
        self.instance_endpoint = instance_endpoint  # type: str
        # The ID of the Message Queue for Apache RocketMQ instance.
        self.instance_id = instance_id  # type: str
        self.instance_network = instance_network  # type: str
        self.instance_password = instance_password  # type: str
        self.instance_security_group_id = instance_security_group_id  # type: str
        self.instance_type = instance_type  # type: str
        self.instance_username = instance_username  # type: str
        self.instance_vswitch_ids = instance_vswitch_ids  # type: str
        self.instance_vpc_id = instance_vpc_id  # type: str
        # The consumer offset of the message. Valid values: CONSUME_FROM_LAST_OFFSET: consumes messages from the latest offset. CONSUME_FROM_FIRST_OFFSET: consumes messages from the earliest offset. CONSUME_FROM_TIMESTAMP: consumes messages from the offset at the specified point in time. Default value: CONSUME_FROM_LAST_OFFSET.
        self.offset = offset  # type: str
        # The ID of the region where the Message Queue for Apache RocketMQ instance resides.
        self.region_id = region_id  # type: str
        # The tags that are used to filter messages.
        self.tag = tag  # type: str
        # The timestamp that indicates the time from which messages are consumed. This parameter is valid only if you set Offset to CONSUME_FROM_TIMESTAMP.
        self.timestamp = timestamp  # type: long
        # The name of the topic in the Message Queue for Apache RocketMQ instance.
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSourceSourceRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class UpdateEventStreamingRequestSourceSourceSLSParameters(TeaModel):
    def __init__(self, role_name=None):
        # The role name. If you want to authorize EventBridge to use this role to read logs in Log Service, you must select Alibaba Cloud Service for Selected Trusted Entity and EventBridge for Select Trusted Service when you create the role in the Resource Access Management (RAM) console.
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSourceSourceSLSParameters, self).to_map()
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


class UpdateEventStreamingRequestSource(TeaModel):
    def __init__(self, source_dtsparameters=None, source_kafka_parameters=None, source_mnsparameters=None,
                 source_mqttparameters=None, source_rabbit_mqparameters=None, source_rocket_mqparameters=None,
                 source_slsparameters=None):
        # The parameters that are configured if the event source is Data Transmission Service (DTS).
        self.source_dtsparameters = source_dtsparameters  # type: UpdateEventStreamingRequestSourceSourceDTSParameters
        # The parameters that are configured if the event source is Message Queue for Apache Kafka.
        self.source_kafka_parameters = source_kafka_parameters  # type: UpdateEventStreamingRequestSourceSourceKafkaParameters
        # The parameters that are configured if the event source is Message Service (MNS).
        self.source_mnsparameters = source_mnsparameters  # type: UpdateEventStreamingRequestSourceSourceMNSParameters
        # The parameters that are configured if the event source is Message Queue for MQTT.
        self.source_mqttparameters = source_mqttparameters  # type: UpdateEventStreamingRequestSourceSourceMQTTParameters
        # The parameters that are configured if the event source is Message Queue for RabbitMQ.
        self.source_rabbit_mqparameters = source_rabbit_mqparameters  # type: UpdateEventStreamingRequestSourceSourceRabbitMQParameters
        # The parameters that are configured if the event source is Message Queue for Apache RocketMQ.
        self.source_rocket_mqparameters = source_rocket_mqparameters  # type: UpdateEventStreamingRequestSourceSourceRocketMQParameters
        # The parameters that are configured if the event source is Log Service.
        self.source_slsparameters = source_slsparameters  # type: UpdateEventStreamingRequestSourceSourceSLSParameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()
        if self.source_slsparameters:
            self.source_slsparameters.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequestSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['SourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['SourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['SourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['SourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['SourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['SourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        if self.source_slsparameters is not None:
            result['SourceSLSParameters'] = self.source_slsparameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceDTSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['SourceDTSParameters'])
        if m.get('SourceKafkaParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['SourceKafkaParameters'])
        if m.get('SourceMNSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['SourceMNSParameters'])
        if m.get('SourceMQTTParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['SourceMQTTParameters'])
        if m.get('SourceRabbitMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['SourceRabbitMQParameters'])
        if m.get('SourceRocketMQParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['SourceRocketMQParameters'])
        if m.get('SourceSLSParameters') is not None:
            temp_model = UpdateEventStreamingRequestSourceSourceSLSParameters()
            self.source_slsparameters = temp_model.from_map(m['SourceSLSParameters'])
        return self


class UpdateEventStreamingRequestTransforms(TeaModel):
    def __init__(self, arn=None):
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingRequestTransforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class UpdateEventStreamingRequest(TeaModel):
    def __init__(self, description=None, event_streaming_name=None, filter_pattern=None, run_options=None,
                 sink=None, source=None, transforms=None):
        # The description of the event stream.
        self.description = description  # type: str
        # The name of the event stream.
        self.event_streaming_name = event_streaming_name  # type: str
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern  # type: str
        # The parameters that are configured for the runtime environment.
        self.run_options = run_options  # type: UpdateEventStreamingRequestRunOptions
        # The event target. You must and can specify only one event target.
        self.sink = sink  # type: UpdateEventStreamingRequestSink
        # The event source, which is also known as the event source. You must and can specify only one event source.
        self.source = source  # type: UpdateEventStreamingRequestSource
        self.transforms = transforms  # type: list[UpdateEventStreamingRequestTransforms]

    def validate(self):
        if self.run_options:
            self.run_options.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()
        if self.transforms:
            for k in self.transforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options is not None:
            result['RunOptions'] = self.run_options.to_map()
        if self.sink is not None:
            result['Sink'] = self.sink.to_map()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        result['Transforms'] = []
        if self.transforms is not None:
            for k in self.transforms:
                result['Transforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            temp_model = UpdateEventStreamingRequestRunOptions()
            self.run_options = temp_model.from_map(m['RunOptions'])
        if m.get('Sink') is not None:
            temp_model = UpdateEventStreamingRequestSink()
            self.sink = temp_model.from_map(m['Sink'])
        if m.get('Source') is not None:
            temp_model = UpdateEventStreamingRequestSource()
            self.source = temp_model.from_map(m['Source'])
        self.transforms = []
        if m.get('Transforms') is not None:
            for k in m.get('Transforms'):
                temp_model = UpdateEventStreamingRequestTransforms()
                self.transforms.append(temp_model.from_map(k))
        return self


class UpdateEventStreamingShrinkRequest(TeaModel):
    def __init__(self, description=None, event_streaming_name=None, filter_pattern=None, run_options_shrink=None,
                 sink_shrink=None, source_shrink=None, transforms_shrink=None):
        # The description of the event stream.
        self.description = description  # type: str
        # The name of the event stream.
        self.event_streaming_name = event_streaming_name  # type: str
        # The rule that is used to filter events. If you leave this parameter empty, all events are matched.
        self.filter_pattern = filter_pattern  # type: str
        # The parameters that are configured for the runtime environment.
        self.run_options_shrink = run_options_shrink  # type: str
        # The event target. You must and can specify only one event target.
        self.sink_shrink = sink_shrink  # type: str
        # The event source, which is also known as the event source. You must and can specify only one event source.
        self.source_shrink = source_shrink  # type: str
        self.transforms_shrink = transforms_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_streaming_name is not None:
            result['EventStreamingName'] = self.event_streaming_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.run_options_shrink is not None:
            result['RunOptions'] = self.run_options_shrink
        if self.sink_shrink is not None:
            result['Sink'] = self.sink_shrink
        if self.source_shrink is not None:
            result['Source'] = self.source_shrink
        if self.transforms_shrink is not None:
            result['Transforms'] = self.transforms_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventStreamingName') is not None:
            self.event_streaming_name = m.get('EventStreamingName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RunOptions') is not None:
            self.run_options_shrink = m.get('RunOptions')
        if m.get('Sink') is not None:
            self.sink_shrink = m.get('Sink')
        if m.get('Source') is not None:
            self.source_shrink = m.get('Source')
        if m.get('Transforms') is not None:
            self.transforms_shrink = m.get('Transforms')
        return self


class UpdateEventStreamingResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code  # type: str
        # The returned error message.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventStreamingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventStreamingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEventStreamingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEventStreamingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEventStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleRequest(TeaModel):
    def __init__(self, description=None, event_bus_name=None, filter_pattern=None, rule_name=None, status=None):
        # The description of the event bus.
        self.description = description  # type: str
        # The name of the event bus.
        self.event_bus_name = event_bus_name  # type: str
        # The event pattern, in JSON format. Valid values: stringEqual stringExpression Each field can have a maximum of five expressions in the map data structure.
        # 
        # Each field can have a maximum of five expressions in the map data structure.
        self.filter_pattern = filter_pattern  # type: str
        # The name of the event rule.
        self.rule_name = rule_name  # type: str
        # The status of the event rule. Valid values: ENABLE: The event rule is enabled. It is the default state of the event rule. DISABLE: The event rule is disabled.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # The status code returned. The status code 200 indicates that the request was successful.
        self.code = code  # type: str
        # The result of the operation.
        self.data = data  # type: bool
        # The error message that is returned if the request failed.
        self.message = message  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values: true and false.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRuleResponseBody, self).to_map()
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


class UpdateRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


