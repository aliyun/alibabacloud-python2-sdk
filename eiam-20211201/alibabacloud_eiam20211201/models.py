# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddUserToOrganizationalUnitsRequest(TeaModel):
    def __init__(self, instance_id=None, organizational_unit_ids=None, user_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The organization IDs. You can add an account to a maximum of 100 organizations.
        self.organizational_unit_ids = organizational_unit_ids  # type: list[str]
        # The account ID.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToOrganizationalUnitsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddUserToOrganizationalUnitsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToOrganizationalUnitsResponseBody, self).to_map()
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


class AddUserToOrganizationalUnitsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddUserToOrganizationalUnitsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserToOrganizationalUnitsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddUserToOrganizationalUnitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUsersToGroupRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None, user_ids=None):
        # The group ID.
        self.group_id = group_id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The account IDs.
        self.user_ids = user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUsersToGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class AddUsersToGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUsersToGroupResponseBody, self).to_map()
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


class AuthorizeApplicationToGroupsRequest(TeaModel):
    def __init__(self, application_id=None, group_ids=None, instance_id=None):
        # The application ID.
        self.application_id = application_id  # type: str
        # The group IDs. You can specify up to 100 group IDs at a time.
        self.group_ids = group_ids  # type: list[str]
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeApplicationToGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AuthorizeApplicationToGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeApplicationToGroupsResponseBody, self).to_map()
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


class AuthorizeApplicationToGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuthorizeApplicationToGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthorizeApplicationToGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AuthorizeApplicationToGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeApplicationToOrganizationalUnitsRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, organizational_unit_ids=None):
        # The ID of the application on which you want to grant permissions.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The IDs of the organizations to which you want to grant permissions. You can grant permissions to a maximum of 100 organizations at a time.
        self.organizational_unit_ids = organizational_unit_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeApplicationToOrganizationalUnitsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')
        return self


class AuthorizeApplicationToOrganizationalUnitsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeApplicationToOrganizationalUnitsResponseBody, self).to_map()
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


class AuthorizeApplicationToOrganizationalUnitsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuthorizeApplicationToOrganizationalUnitsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthorizeApplicationToOrganizationalUnitsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AuthorizeApplicationToOrganizationalUnitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeApplicationToUsersRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, user_ids=None):
        # The ID of the application on which you want to grant permissions.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The IDs of the accounts to which you want to grant permissions. You can grant permissions to a maximum of 100 accounts at a time.
        self.user_ids = user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeApplicationToUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class AuthorizeApplicationToUsersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeApplicationToUsersResponseBody, self).to_map()
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


class AuthorizeApplicationToUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuthorizeApplicationToUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthorizeApplicationToUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AuthorizeApplicationToUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(self, application_name=None, application_source_type=None, application_template_id=None,
                 description=None, instance_id=None, logo_url=None, sso_type=None):
        # The name of the application.
        self.application_name = application_name  # type: str
        # The type of the application source. Valid values:
        # 
        # *   urn:alibaba:idaas:app:source:template: application template
        # *   urn:alibaba:idaas:app:source:standard: standard protocol
        self.application_source_type = application_source_type  # type: str
        # The ID of the application template. This parameter is required if you set the ApplicationSourceType parameter to urn:alibaba:idaas:app:source:template.
        self.application_template_id = application_template_id  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The URL of the application logo.
        self.logo_url = logo_url  # type: str
        # The SSO protocol. Valid values:
        # 
        # *   saml2: the SAML 2.0 protocol.
        # *   oidc: the OpenID Connect protocol.
        self.sso_type = sso_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.application_source_type is not None:
            result['ApplicationSourceType'] = self.application_source_type
        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        if self.sso_type is not None:
            result['SsoType'] = self.sso_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ApplicationSourceType') is not None:
            self.application_source_type = m.get('ApplicationSourceType')
        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(self, application_id=None, request_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
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


class CreateApplicationClientSecretRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application for which you want to create a client key.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationClientSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateApplicationClientSecretResponseBodyApplicationClientSecret(TeaModel):
    def __init__(self, client_id=None, client_secret=None, secret_id=None):
        # The client ID of the application.
        self.client_id = client_id  # type: str
        # The client key secret of the application.
        self.client_secret = client_secret  # type: str
        # The client key ID of the application.
        self.secret_id = secret_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationClientSecretResponseBodyApplicationClientSecret, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class CreateApplicationClientSecretResponseBody(TeaModel):
    def __init__(self, application_client_secret=None, request_id=None):
        # The information about the client key.
        self.application_client_secret = application_client_secret  # type: CreateApplicationClientSecretResponseBodyApplicationClientSecret
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application_client_secret:
            self.application_client_secret.validate()

    def to_map(self):
        _map = super(CreateApplicationClientSecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_client_secret is not None:
            result['ApplicationClientSecret'] = self.application_client_secret.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationClientSecret') is not None:
            temp_model = CreateApplicationClientSecretResponseBodyApplicationClientSecret()
            self.application_client_secret = temp_model.from_map(m['ApplicationClientSecret'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationClientSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApplicationClientSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationClientSecretResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateApplicationClientSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequestFiling(TeaModel):
    def __init__(self, icp_number=None):
        # 域名关联的备案号，长度最大限制64。
        self.icp_number = icp_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainRequestFiling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icp_number is not None:
            result['IcpNumber'] = self.icp_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IcpNumber') is not None:
            self.icp_number = m.get('IcpNumber')
        return self


class CreateDomainRequest(TeaModel):
    def __init__(self, domain=None, filing=None, instance_id=None):
        # 域名。最大长度限制255，格式由数字、字母、横线（-）点（.）组成;
        self.domain = domain  # type: str
        # 备案信息参数。
        self.filing = filing  # type: CreateDomainRequestFiling
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        if self.filing:
            self.filing.validate()

    def to_map(self):
        _map = super(CreateDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.filing is not None:
            result['Filing'] = self.filing.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Filing') is not None:
            temp_model = CreateDomainRequestFiling()
            self.filing = temp_model.from_map(m['Filing'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(self, domain_id=None, request_id=None):
        self.domain_id = domain_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainProxyTokenRequest(TeaModel):
    def __init__(self, domain_id=None, instance_id=None):
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainProxyTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDomainProxyTokenResponseBody(TeaModel):
    def __init__(self, domain_proxy_token_id=None, request_id=None):
        self.domain_proxy_token_id = domain_proxy_token_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainProxyTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_proxy_token_id is not None:
            result['DomainProxyTokenId'] = self.domain_proxy_token_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainProxyTokenId') is not None:
            self.domain_proxy_token_id = m.get('DomainProxyTokenId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDomainProxyTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDomainProxyTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDomainProxyTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDomainProxyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(self, description=None, group_external_id=None, group_name=None, instance_id=None):
        # The description of the group. The value can be up to 256 characters in length.
        self.description = description  # type: str
        # The external ID of the group, which can be used to associate the group with an external system. By default, the external ID is the group ID. The value can be up to 64 characters in length.
        self.group_external_id = group_external_id  # type: str
        # The name of the group. The name can be up to 64 characters in length.
        self.group_name = group_name  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_external_id is not None:
            result['GroupExternalId'] = self.group_external_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupExternalId') is not None:
            self.group_external_id = m.get('GroupExternalId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(self, group_id=None, request_id=None):
        # The group ID.
        self.group_id = group_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
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


class CreateInstanceRequest(TeaModel):
    def __init__(self, description=None):
        # The description of the instance. The description can be up to 128 characters in length.
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # The ID of the instance that is created.
        self.instance_id = instance_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
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


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkAccessEndpointRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, network_access_endpoint_name=None, v_switch_ids=None,
                 vpc_id=None, vpc_region_id=None):
        # 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。
        self.client_token = client_token  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str
        # 专属网络端点名称。
        self.network_access_endpoint_name = network_access_endpoint_name  # type: str
        # 专属网络端点连接的指定vSwitch。
        self.v_switch_ids = v_switch_ids  # type: list[str]
        # 专属网络端点连接的VpcID。
        self.vpc_id = vpc_id  # type: str
        # 专属网络端点连接的VpcID所属地域，该地域取值必须在ListNetworkAccessEndpointAvailableRegions接口中返回。
        self.vpc_region_id = vpc_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNetworkAccessEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_access_endpoint_name is not None:
            result['NetworkAccessEndpointName'] = self.network_access_endpoint_name
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkAccessEndpointName') is not None:
            self.network_access_endpoint_name = m.get('NetworkAccessEndpointName')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        return self


class CreateNetworkAccessEndpointResponseBody(TeaModel):
    def __init__(self, network_access_endpoint_id=None, request_id=None):
        self.network_access_endpoint_id = network_access_endpoint_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNetworkAccessEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNetworkAccessEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNetworkAccessEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNetworkAccessEndpointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateNetworkAccessEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrganizationalUnitRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, organizational_unit_external_id=None,
                 organizational_unit_name=None, parent_id=None):
        # The description of the organization. The value can be up to 256 characters in length.
        self.description = description  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The external ID of the organization, which can be used to associate the organization with an external system. By default, the external ID is the organization ID. The value can be up to 64 characters in length.
        self.organizational_unit_external_id = organizational_unit_external_id  # type: str
        # The name of the organization. The name can be up to 64 characters in length.
        self.organizational_unit_name = organizational_unit_name  # type: str
        # The parent organization ID.
        self.parent_id = parent_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrganizationalUnitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_external_id is not None:
            result['OrganizationalUnitExternalId'] = self.organizational_unit_external_id
        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('OrganizationalUnitExternalId')
        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class CreateOrganizationalUnitResponseBody(TeaModel):
    def __init__(self, organizational_unit_id=None, request_id=None):
        # The organization ID.
        self.organizational_unit_id = organizational_unit_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrganizationalUnitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrganizationalUnitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOrganizationalUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrganizationalUnitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateOrganizationalUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequestCustomFields(TeaModel):
    def __init__(self, field_name=None, field_value=None):
        # The name of the extended field. You must create the extended field in advance. To create an extended field, log on to the IDaaS console. In the left-side navigation pane, choose Accounts > Extended Fields, and then click Create Field on the Extended Fields page.
        self.field_name = field_name  # type: str
        # The value of the extended field. The value follows the limits on the properties of the extended field.
        self.field_value = field_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserRequestCustomFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        return self


class CreateUserRequestPasswordInitializationConfig(TeaModel):
    def __init__(self, password_forced_update_status=None, password_initialization_policy_priority=None,
                 password_initialization_type=None, user_notification_channels=None):
        # Specifies whether to forcibly change the password status. Default value: disabled. Valid values:
        # 
        # *   enabled: forcibly changes the password status.
        # *   disabled: does not forcibly change the password status.
        self.password_forced_update_status = password_forced_update_status  # type: str
        # The priority of the password initialization policy. By default, this parameter does not take effect. Valid values:
        # 
        # *   global: The password initialization policy globally takes effect.
        # *   custom: The password initialization policy takes effect based on custom settings.
        self.password_initialization_policy_priority = password_initialization_policy_priority  # type: str
        # The password initialization method. Set the value to random,
        # 
        # *   which indicates that the password is randomly generated.
        self.password_initialization_type = password_initialization_type  # type: str
        # The password notification methods.
        self.user_notification_channels = user_notification_channels  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserRequestPasswordInitializationConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_forced_update_status is not None:
            result['PasswordForcedUpdateStatus'] = self.password_forced_update_status
        if self.password_initialization_policy_priority is not None:
            result['PasswordInitializationPolicyPriority'] = self.password_initialization_policy_priority
        if self.password_initialization_type is not None:
            result['PasswordInitializationType'] = self.password_initialization_type
        if self.user_notification_channels is not None:
            result['UserNotificationChannels'] = self.user_notification_channels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordForcedUpdateStatus') is not None:
            self.password_forced_update_status = m.get('PasswordForcedUpdateStatus')
        if m.get('PasswordInitializationPolicyPriority') is not None:
            self.password_initialization_policy_priority = m.get('PasswordInitializationPolicyPriority')
        if m.get('PasswordInitializationType') is not None:
            self.password_initialization_type = m.get('PasswordInitializationType')
        if m.get('UserNotificationChannels') is not None:
            self.user_notification_channels = m.get('UserNotificationChannels')
        return self


class CreateUserRequest(TeaModel):
    def __init__(self, custom_fields=None, description=None, display_name=None, email=None, email_verified=None,
                 instance_id=None, organizational_unit_ids=None, password=None, password_initialization_config=None,
                 phone_number=None, phone_number_verified=None, phone_region=None, primary_organizational_unit_id=None,
                 user_external_id=None, username=None):
        # The extended fields.
        self.custom_fields = custom_fields  # type: list[CreateUserRequestCustomFields]
        # The description of the organizational unit. The description can be up to 256 characters in length.
        self.description = description  # type: str
        # The display name of the account. The display name can be up to 64 characters in length.
        self.display_name = display_name  # type: str
        # The email address of the user who owns the account. The email address prefix can contain letters, digits, underscores (\_), periods (.), and hyphens (-).
        self.email = email  # type: str
        # Specifies whether the email address is a trusted email address. This parameter is required if the Email parameter is specified. If you have no special business requirements, set this parameter to true.
        self.email_verified = email_verified  # type: bool
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The IDs of organizational units to which the account belongs. An account can belong to multiple organizational units.
        self.organizational_unit_ids = organizational_unit_ids  # type: list[str]
        # The password of the account. For more information, view the password policy of the instance in the IDaaS console.
        self.password = password  # type: str
        # The configurations for password initialization.
        self.password_initialization_config = password_initialization_config  # type: CreateUserRequestPasswordInitializationConfig
        # The mobile phone number, which contains 6 to 15 digits.
        self.phone_number = phone_number  # type: str
        # Specifies whether the mobile phone number is a trusted mobile phone number. This parameter is required if the PhoneNumber parameter is specified. If you have no special business requirements, set this parameter to true.
        self.phone_number_verified = phone_number_verified  # type: bool
        # The country code of the mobile phone number. The country code contains only digits and does not contain a plus sign (+).
        self.phone_region = phone_region  # type: str
        # The ID of the primary organizational unit to which the account belongs.
        self.primary_organizational_unit_id = primary_organizational_unit_id  # type: str
        # The external ID of the account. The external ID can be used to associate the account with an external system. The external ID can be up to 64 characters in length. If you do not specify an external ID for the account, the ID of the account is used as the external ID by default.
        self.user_external_id = user_external_id  # type: str
        # The name of the account. The name can be up to 64 characters in length and can contain letters, digits, underscores (\_), periods (.), at signs (@), and hyphens (-).
        self.username = username  # type: str

    def validate(self):
        if self.custom_fields:
            for k in self.custom_fields:
                if k:
                    k.validate()
        if self.password_initialization_config:
            self.password_initialization_config.validate()

    def to_map(self):
        _map = super(CreateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomFields'] = []
        if self.custom_fields is not None:
            for k in self.custom_fields:
                result['CustomFields'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verified is not None:
            result['EmailVerified'] = self.email_verified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids
        if self.password is not None:
            result['Password'] = self.password
        if self.password_initialization_config is not None:
            result['PasswordInitializationConfig'] = self.password_initialization_config.to_map()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_number_verified is not None:
            result['PhoneNumberVerified'] = self.phone_number_verified
        if self.phone_region is not None:
            result['PhoneRegion'] = self.phone_region
        if self.primary_organizational_unit_id is not None:
            result['PrimaryOrganizationalUnitId'] = self.primary_organizational_unit_id
        if self.user_external_id is not None:
            result['UserExternalId'] = self.user_external_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_fields = []
        if m.get('CustomFields') is not None:
            for k in m.get('CustomFields'):
                temp_model = CreateUserRequestCustomFields()
                self.custom_fields.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerified') is not None:
            self.email_verified = m.get('EmailVerified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordInitializationConfig') is not None:
            temp_model = CreateUserRequestPasswordInitializationConfig()
            self.password_initialization_config = temp_model.from_map(m['PasswordInitializationConfig'])
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneNumberVerified') is not None:
            self.phone_number_verified = m.get('PhoneNumberVerified')
        if m.get('PhoneRegion') is not None:
            self.phone_region = m.get('PhoneRegion')
        if m.get('PrimaryOrganizationalUnitId') is not None:
            self.primary_organizational_unit_id = m.get('PrimaryOrganizationalUnitId')
        if m.get('UserExternalId') is not None:
            self.user_external_id = m.get('UserExternalId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the account.
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


class DeleteApplicationRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application that you want to delete.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


class DeleteApplicationClientSecretRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, secret_id=None):
        # The ID of the application for which you want to delete a client key.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the client key that you want to delete for the application.
        self.secret_id = secret_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationClientSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class DeleteApplicationClientSecretResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationClientSecretResponseBody, self).to_map()
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


class DeleteApplicationClientSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApplicationClientSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApplicationClientSecretResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteApplicationClientSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(self, domain_id=None, instance_id=None):
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainResponseBody, self).to_map()
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


class DeleteDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainProxyTokenRequest(TeaModel):
    def __init__(self, domain_id=None, domain_proxy_token_id=None, instance_id=None):
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # 域名代理Token ID。
        self.domain_proxy_token_id = domain_proxy_token_id  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainProxyTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_proxy_token_id is not None:
            result['DomainProxyTokenId'] = self.domain_proxy_token_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainProxyTokenId') is not None:
            self.domain_proxy_token_id = m.get('DomainProxyTokenId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDomainProxyTokenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainProxyTokenResponseBody, self).to_map()
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


class DeleteDomainProxyTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDomainProxyTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDomainProxyTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDomainProxyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None):
        # The group ID.
        self.group_id = group_id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
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


class DeleteInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the instance to be deleted.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
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


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkAccessEndpointRequest(TeaModel):
    def __init__(self, instance_id=None, network_access_endpoint_id=None):
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str
        # 专属网络端点ID。
        self.network_access_endpoint_id = network_access_endpoint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNetworkAccessEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')
        return self


class DeleteNetworkAccessEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNetworkAccessEndpointResponseBody, self).to_map()
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


class DeleteNetworkAccessEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNetworkAccessEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNetworkAccessEndpointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNetworkAccessEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOrganizationalUnitRequest(TeaModel):
    def __init__(self, instance_id=None, organizational_unit_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The organization ID.
        self.organizational_unit_id = organizational_unit_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOrganizationalUnitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        return self


class DeleteOrganizationalUnitResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOrganizationalUnitResponseBody, self).to_map()
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


class DeleteOrganizationalUnitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteOrganizationalUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteOrganizationalUnitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteOrganizationalUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, instance_id=None, user_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The account ID.
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
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
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


class DisableApplicationRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application that you want to disable.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableApplicationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationResponseBody, self).to_map()
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


class DisableApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableApplicationApiInvokeRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationApiInvokeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableApplicationApiInvokeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationApiInvokeResponseBody, self).to_map()
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


class DisableApplicationApiInvokeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableApplicationApiInvokeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableApplicationApiInvokeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableApplicationApiInvokeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableApplicationClientSecretRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, secret_id=None):
        # The ID of the application for which you want to disable a client key.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The client key ID of the application.
        self.secret_id = secret_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationClientSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class DisableApplicationClientSecretResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationClientSecretResponseBody, self).to_map()
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


class DisableApplicationClientSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableApplicationClientSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableApplicationClientSecretResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableApplicationClientSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableApplicationProvisioningRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationProvisioningRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableApplicationProvisioningResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationProvisioningResponseBody, self).to_map()
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


class DisableApplicationProvisioningResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableApplicationProvisioningResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableApplicationProvisioningResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableApplicationProvisioningResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableApplicationSsoRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # IDaaS的应用主键id
        self.application_id = application_id  # type: str
        # IDaaS EIAM的实例id
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationSsoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableApplicationSsoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationSsoResponseBody, self).to_map()
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


class DisableApplicationSsoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableApplicationSsoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableApplicationSsoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableApplicationSsoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDomainProxyTokenRequest(TeaModel):
    def __init__(self, domain_id=None, domain_proxy_token_id=None, instance_id=None):
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # 域名代理Token ID。
        self.domain_proxy_token_id = domain_proxy_token_id  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableDomainProxyTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_proxy_token_id is not None:
            result['DomainProxyTokenId'] = self.domain_proxy_token_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainProxyTokenId') is not None:
            self.domain_proxy_token_id = m.get('DomainProxyTokenId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableDomainProxyTokenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableDomainProxyTokenResponseBody, self).to_map()
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


class DisableDomainProxyTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableDomainProxyTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableDomainProxyTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableDomainProxyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableInitDomainAutoRedirectRequest(TeaModel):
    def __init__(self, instance_id=None):
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableInitDomainAutoRedirectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableInitDomainAutoRedirectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableInitDomainAutoRedirectResponseBody, self).to_map()
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


class DisableInitDomainAutoRedirectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableInitDomainAutoRedirectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableInitDomainAutoRedirectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableInitDomainAutoRedirectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableUserRequest(TeaModel):
    def __init__(self, instance_id=None, user_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The ID of the account.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DisableUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableUserResponseBody, self).to_map()
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


class DisableUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableApplicationRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application that you want to enable.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnableApplicationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationResponseBody, self).to_map()
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


class EnableApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableApplicationApiInvokeRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationApiInvokeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnableApplicationApiInvokeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationApiInvokeResponseBody, self).to_map()
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


class EnableApplicationApiInvokeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableApplicationApiInvokeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableApplicationApiInvokeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableApplicationApiInvokeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableApplicationClientSecretRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, secret_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The client key ID of the application.
        self.secret_id = secret_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationClientSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class EnableApplicationClientSecretResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationClientSecretResponseBody, self).to_map()
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


class EnableApplicationClientSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableApplicationClientSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableApplicationClientSecretResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableApplicationClientSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableApplicationProvisioningRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationProvisioningRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnableApplicationProvisioningResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationProvisioningResponseBody, self).to_map()
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


class EnableApplicationProvisioningResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableApplicationProvisioningResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableApplicationProvisioningResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableApplicationProvisioningResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableApplicationSsoRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # IDaaS的应用主键id
        self.application_id = application_id  # type: str
        # IDaaS EIAM的实例id
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationSsoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnableApplicationSsoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationSsoResponseBody, self).to_map()
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


class EnableApplicationSsoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableApplicationSsoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableApplicationSsoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableApplicationSsoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableDomainProxyTokenRequest(TeaModel):
    def __init__(self, domain_id=None, domain_proxy_token_id=None, instance_id=None):
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # 域名代理Token ID。
        self.domain_proxy_token_id = domain_proxy_token_id  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableDomainProxyTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_proxy_token_id is not None:
            result['DomainProxyTokenId'] = self.domain_proxy_token_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainProxyTokenId') is not None:
            self.domain_proxy_token_id = m.get('DomainProxyTokenId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnableDomainProxyTokenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableDomainProxyTokenResponseBody, self).to_map()
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


class EnableDomainProxyTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableDomainProxyTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableDomainProxyTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableDomainProxyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableInitDomainAutoRedirectRequest(TeaModel):
    def __init__(self, instance_id=None):
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableInitDomainAutoRedirectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnableInitDomainAutoRedirectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableInitDomainAutoRedirectResponseBody, self).to_map()
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


class EnableInitDomainAutoRedirectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableInitDomainAutoRedirectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableInitDomainAutoRedirectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableInitDomainAutoRedirectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableUserRequest(TeaModel):
    def __init__(self, instance_id=None, user_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The account ID.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class EnableUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableUserResponseBody, self).to_map()
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


class EnableUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application that you want to query.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetApplicationResponseBodyApplication(TeaModel):
    def __init__(self, api_invoke_status=None, application_id=None, application_name=None,
                 application_source_type=None, application_template_id=None, authorization_type=None, client_id=None, create_time=None,
                 description=None, features=None, instance_id=None, logo_url=None, managed_service_code=None,
                 service_managed=None, sso_type=None, status=None, update_time=None):
        # The status of the Developer API feature. Valid values:
        # 
        # *   Enabled: The Developer API feature is enabled.
        # *   Disabled: The Developer API feature is disabled.
        self.api_invoke_status = api_invoke_status  # type: str
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The name of the application.
        self.application_name = application_name  # type: str
        # The origin of the application. Valid values:
        # 
        # *   urn:alibaba:idaas:app:source:template: The application is created based on a template.
        # *   urn:alibaba:idaas: The application is created based on the standard protocol.
        self.application_source_type = application_source_type  # type: str
        # The ID of the template based on which the application is created. This parameter is returned only if the application is created based on a template.
        self.application_template_id = application_template_id  # type: str
        # The authorization type of the EIAM application. Valid values:
        # 
        # *   authorize_required: Only the user with explicit authorization can access the application.
        # *   default_all: By default, all users can access the application.
        self.authorization_type = authorization_type  # type: str
        # The client ID of the application.
        self.client_id = client_id  # type: str
        # The time when the application was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The description of the application.
        self.description = description  # type: str
        # The features that are supported by the application. The value is a JSON array. Valid values:
        # 
        # *   sso: The application supports SSO.
        # *   provision: The application supports account synchronization.
        # *   api_invoke: The application supports custom APIs.
        self.features = features  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The URL of the application icon.
        self.logo_url = logo_url  # type: str
        # The service code of the cloud service that manages the application template.
        self.managed_service_code = managed_service_code  # type: str
        # Indicates whether the application template is managed by a cloud service.
        self.service_managed = service_managed  # type: bool
        # The type of the single sign-on (SSO) protocol. Valid values:
        # 
        # *   saml2: the Security Assertion Markup Language (SAML) 2.0 protocol.
        # *   oidc: the OpenID Connect (OIDC) protocol.
        self.sso_type = sso_type  # type: str
        # The status of the application. Valid values:
        # 
        # *   Enabled: The application is enabled.
        # *   Disabled: The application is disabled.
        self.status = status  # type: str
        # The time when the application was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationResponseBodyApplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_invoke_status is not None:
            result['ApiInvokeStatus'] = self.api_invoke_status
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.application_source_type is not None:
            result['ApplicationSourceType'] = self.application_source_type
        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.features is not None:
            result['Features'] = self.features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        if self.managed_service_code is not None:
            result['ManagedServiceCode'] = self.managed_service_code
        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed
        if self.sso_type is not None:
            result['SsoType'] = self.sso_type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiInvokeStatus') is not None:
            self.api_invoke_status = m.get('ApiInvokeStatus')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ApplicationSourceType') is not None:
            self.application_source_type = m.get('ApplicationSourceType')
        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        if m.get('ManagedServiceCode') is not None:
            self.managed_service_code = m.get('ManagedServiceCode')
        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')
        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(self, application=None, request_id=None):
        # The details of the application.
        self.application = application  # type: GetApplicationResponseBodyApplication
        # The ID of the request.
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


class GetApplicationGrantScopeRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationGrantScopeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetApplicationGrantScopeResponseBodyApplicationGrantScope(TeaModel):
    def __init__(self, grant_scopes=None):
        # The permissions of the Developer API feature.
        self.grant_scopes = grant_scopes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationGrantScopeResponseBodyApplicationGrantScope, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_scopes is not None:
            result['GrantScopes'] = self.grant_scopes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GrantScopes') is not None:
            self.grant_scopes = m.get('GrantScopes')
        return self


class GetApplicationGrantScopeResponseBody(TeaModel):
    def __init__(self, application_grant_scope=None, request_id=None):
        # The permissions of the Developer API feature.
        self.application_grant_scope = application_grant_scope  # type: GetApplicationGrantScopeResponseBodyApplicationGrantScope
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application_grant_scope:
            self.application_grant_scope.validate()

    def to_map(self):
        _map = super(GetApplicationGrantScopeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_grant_scope is not None:
            result['ApplicationGrantScope'] = self.application_grant_scope.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationGrantScope') is not None:
            temp_model = GetApplicationGrantScopeResponseBodyApplicationGrantScope()
            self.application_grant_scope = temp_model.from_map(m['ApplicationGrantScope'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationGrantScopeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApplicationGrantScopeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApplicationGrantScopeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetApplicationGrantScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationProvisioningConfigRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationProvisioningConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigCallbackProvisioningConfig(TeaModel):
    def __init__(self, callback_url=None, encrypt_key=None, encrypt_required=None, listen_event_scopes=None):
        # The URL that the application uses to receive IDaaS event callbacks.
        self.callback_url = callback_url  # type: str
        # The symmetric key for IDaaS event callbacks. The key is an AES-256 encryption key in the HEX format.
        self.encrypt_key = encrypt_key  # type: str
        # Indicates whether IDaaS event callback messages are encrypted. Valid values:
        # 
        # *   true: The messages are encrypted.
        # *   false: The messages are transmitted in plaintext.
        self.encrypt_required = encrypt_required  # type: bool
        # The list of types of IDaaS event callback messages that are supported by the listener.
        self.listen_event_scopes = listen_event_scopes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigCallbackProvisioningConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.encrypt_key is not None:
            result['EncryptKey'] = self.encrypt_key
        if self.encrypt_required is not None:
            result['EncryptRequired'] = self.encrypt_required
        if self.listen_event_scopes is not None:
            result['ListenEventScopes'] = self.listen_event_scopes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('EncryptKey') is not None:
            self.encrypt_key = m.get('EncryptKey')
        if m.get('EncryptRequired') is not None:
            self.encrypt_required = m.get('EncryptRequired')
        if m.get('ListenEventScopes') is not None:
            self.listen_event_scopes = m.get('ListenEventScopes')
        return self


class GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfigurationAuthnParam(TeaModel):
    def __init__(self, access_token=None, authn_method=None, client_id=None, client_secret=None,
                 token_endpoint=None):
        # The access token. This parameter is returned when the GrantType parameter is set to bearer_token.
        self.access_token = access_token  # type: str
        # The authentication mode of the SCIM protocol. Valid values:
        # 
        # *   client_secret_basic: The client secret is passed in the request header.
        # *   client_secret_post: The client secret is passed in the request body.
        self.authn_method = authn_method  # type: str
        # The client ID of the application.
        self.client_id = client_id  # type: str
        # The client secret of the application.
        self.client_secret = client_secret  # type: str
        # The token endpoint.
        self.token_endpoint = token_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfigurationAuthnParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.authn_method is not None:
            result['AuthnMethod'] = self.authn_method
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret
        if self.token_endpoint is not None:
            result['TokenEndpoint'] = self.token_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AuthnMethod') is not None:
            self.authn_method = m.get('AuthnMethod')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')
        if m.get('TokenEndpoint') is not None:
            self.token_endpoint = m.get('TokenEndpoint')
        return self


class GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfiguration(TeaModel):
    def __init__(self, authn_mode=None, authn_param=None, grant_type=None):
        # The authentication mode of the SCIM protocol. Valid value:
        # 
        # *   oauth2: OAuth2.0 mode.
        self.authn_mode = authn_mode  # type: str
        # The configuration parameters related to authorization.
        # 
        # *   If the GrantType parameter is set to client_credentials, the configuration parameters ClientId, ClientSecret, and AuthnMethod are returned.
        # *   If the GrantType parameter is set to bearer_token, the configuration parameter AccessToken is returned.
        self.authn_param = authn_param  # type: GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfigurationAuthnParam
        # The grant type of the SCIM protocol. Valid values:
        # 
        # *   client_credentials: client mode.
        # *   bearer_token: key mode.
        self.grant_type = grant_type  # type: str

    def validate(self):
        if self.authn_param:
            self.authn_param.validate()

    def to_map(self):
        _map = super(GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authn_mode is not None:
            result['AuthnMode'] = self.authn_mode
        if self.authn_param is not None:
            result['AuthnParam'] = self.authn_param.to_map()
        if self.grant_type is not None:
            result['GrantType'] = self.grant_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthnMode') is not None:
            self.authn_mode = m.get('AuthnMode')
        if m.get('AuthnParam') is not None:
            temp_model = GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfigurationAuthnParam()
            self.authn_param = temp_model.from_map(m['AuthnParam'])
        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')
        return self


class GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfig(TeaModel):
    def __init__(self, authn_configuration=None, full_push_scopes=None, provisioning_actions=None,
                 scim_base_url=None):
        # The configuration parameters related to SCIM-based synchronization.
        self.authn_configuration = authn_configuration  # type: GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfiguration
        # The full synchronization scope of the SCIM protocol. Valid value:
        # 
        # *   urn:alibaba:idaas:app:scim:User:PUSH: full account data synchronization.
        self.full_push_scopes = full_push_scopes  # type: list[str]
        # The resource operations of the SCIM protocol. Valid values:
        # 
        # *   urn:alibaba:idaas:app:scim:User:CREATE: account creation.
        # *   urn:alibaba:idaas:app:scim:User:UPDATE: account update.
        # *   urn:alibaba:idaas:app:scim:User:DELETE: account deletion.
        self.provisioning_actions = provisioning_actions  # type: list[str]
        # The base URL that the application uses to receive the SCIM protocol for IDaaS synchronization.
        self.scim_base_url = scim_base_url  # type: str

    def validate(self):
        if self.authn_configuration:
            self.authn_configuration.validate()

    def to_map(self):
        _map = super(GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authn_configuration is not None:
            result['AuthnConfiguration'] = self.authn_configuration.to_map()
        if self.full_push_scopes is not None:
            result['FullPushScopes'] = self.full_push_scopes
        if self.provisioning_actions is not None:
            result['ProvisioningActions'] = self.provisioning_actions
        if self.scim_base_url is not None:
            result['ScimBaseUrl'] = self.scim_base_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthnConfiguration') is not None:
            temp_model = GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfiguration()
            self.authn_configuration = temp_model.from_map(m['AuthnConfiguration'])
        if m.get('FullPushScopes') is not None:
            self.full_push_scopes = m.get('FullPushScopes')
        if m.get('ProvisioningActions') is not None:
            self.provisioning_actions = m.get('ProvisioningActions')
        if m.get('ScimBaseUrl') is not None:
            self.scim_base_url = m.get('ScimBaseUrl')
        return self


class GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfig(TeaModel):
    def __init__(self, application_id=None, callback_provisioning_config=None, config_operate_mode=None,
                 instance_id=None, provision_jwks_endpoint=None, provision_password=None, provision_protocol_type=None,
                 scim_provisioning_config=None, status=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The configuration of the custom event callback protocol of IDaaS.
        self.callback_provisioning_config = callback_provisioning_config  # type: GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigCallbackProvisioningConfig
        # Client-side rendering, Valid values: 
        # - standard：standard mode.
        # - template：template mode.
        self.config_operate_mode = config_operate_mode  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The public key endpoint for signature verification of the synchronization callback information.
        self.provision_jwks_endpoint = provision_jwks_endpoint  # type: str
        # Indicates whether the password is synchronized in IDaaS user event callbacks. Valid values:
        # 
        # *   true: The password is synchronized.
        # *   false: The password is not synchronized.
        self.provision_password = provision_password  # type: bool
        # The synchronization protocol type of the application. Valid values:
        # 
        # *   idaas_callback: custom event callback protocol of IDaaS.
        # *   scim2: System for Cross-domain Identity Management (SCIM) protocol.
        self.provision_protocol_type = provision_protocol_type  # type: str
        # The configuration of SCIM-based IDaaS synchronization.
        self.scim_provisioning_config = scim_provisioning_config  # type: GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfig
        # The status of the IDaaS account synchronization feature. Valid values:
        # 
        # *   enabled: The feature is enabled.
        # *   disabled: The feature is disabled.
        self.status = status  # type: str

    def validate(self):
        if self.callback_provisioning_config:
            self.callback_provisioning_config.validate()
        if self.scim_provisioning_config:
            self.scim_provisioning_config.validate()

    def to_map(self):
        _map = super(GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.callback_provisioning_config is not None:
            result['CallbackProvisioningConfig'] = self.callback_provisioning_config.to_map()
        if self.config_operate_mode is not None:
            result['ConfigOperateMode'] = self.config_operate_mode
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.provision_jwks_endpoint is not None:
            result['ProvisionJwksEndpoint'] = self.provision_jwks_endpoint
        if self.provision_password is not None:
            result['ProvisionPassword'] = self.provision_password
        if self.provision_protocol_type is not None:
            result['ProvisionProtocolType'] = self.provision_protocol_type
        if self.scim_provisioning_config is not None:
            result['ScimProvisioningConfig'] = self.scim_provisioning_config.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CallbackProvisioningConfig') is not None:
            temp_model = GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigCallbackProvisioningConfig()
            self.callback_provisioning_config = temp_model.from_map(m['CallbackProvisioningConfig'])
        if m.get('ConfigOperateMode') is not None:
            self.config_operate_mode = m.get('ConfigOperateMode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProvisionJwksEndpoint') is not None:
            self.provision_jwks_endpoint = m.get('ProvisionJwksEndpoint')
        if m.get('ProvisionPassword') is not None:
            self.provision_password = m.get('ProvisionPassword')
        if m.get('ProvisionProtocolType') is not None:
            self.provision_protocol_type = m.get('ProvisionProtocolType')
        if m.get('ScimProvisioningConfig') is not None:
            temp_model = GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfig()
            self.scim_provisioning_config = temp_model.from_map(m['ScimProvisioningConfig'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetApplicationProvisioningConfigResponseBody(TeaModel):
    def __init__(self, application_provisioning_config=None, request_id=None):
        # The configuration of the account synchronization feature for the application.
        self.application_provisioning_config = application_provisioning_config  # type: GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfig
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application_provisioning_config:
            self.application_provisioning_config.validate()

    def to_map(self):
        _map = super(GetApplicationProvisioningConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_provisioning_config is not None:
            result['ApplicationProvisioningConfig'] = self.application_provisioning_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationProvisioningConfig') is not None:
            temp_model = GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfig()
            self.application_provisioning_config = temp_model.from_map(m['ApplicationProvisioningConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationProvisioningConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApplicationProvisioningConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApplicationProvisioningConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetApplicationProvisioningConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationProvisioningScopeRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationProvisioningScopeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetApplicationProvisioningScopeResponseBodyApplicationProvisioningScope(TeaModel):
    def __init__(self, organizational_unit_ids=None):
        # The list of organizational units that are authorized for account synchronization.
        self.organizational_unit_ids = organizational_unit_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationProvisioningScopeResponseBodyApplicationProvisioningScope, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')
        return self


class GetApplicationProvisioningScopeResponseBody(TeaModel):
    def __init__(self, application_provisioning_scope=None, request_id=None):
        # The scope of account synchronization.
        self.application_provisioning_scope = application_provisioning_scope  # type: GetApplicationProvisioningScopeResponseBodyApplicationProvisioningScope
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application_provisioning_scope:
            self.application_provisioning_scope.validate()

    def to_map(self):
        _map = super(GetApplicationProvisioningScopeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_provisioning_scope is not None:
            result['ApplicationProvisioningScope'] = self.application_provisioning_scope.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationProvisioningScope') is not None:
            temp_model = GetApplicationProvisioningScopeResponseBodyApplicationProvisioningScope()
            self.application_provisioning_scope = temp_model.from_map(m['ApplicationProvisioningScope'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationProvisioningScopeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApplicationProvisioningScopeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApplicationProvisioningScopeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetApplicationProvisioningScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationSsoConfigRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationSsoConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfigCustomClaims(TeaModel):
    def __init__(self, claim_name=None, claim_value_expression=None):
        # The claim name.
        self.claim_name = claim_name  # type: str
        # The expression that is used to generate the value of the claim.
        self.claim_value_expression = claim_value_expression  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfigCustomClaims, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_name is not None:
            result['ClaimName'] = self.claim_name
        if self.claim_value_expression is not None:
            result['ClaimValueExpression'] = self.claim_value_expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClaimName') is not None:
            self.claim_name = m.get('ClaimName')
        if m.get('ClaimValueExpression') is not None:
            self.claim_value_expression = m.get('ClaimValueExpression')
        return self


class GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfig(TeaModel):
    def __init__(self, access_token_effective_time=None, code_effective_time=None, custom_claims=None,
                 grant_scopes=None, grant_types=None, id_token_effective_time=None, password_authentication_source_id=None,
                 password_totp_mfa_required=None, pkce_challenge_methods=None, pkce_required=None, post_logout_redirect_uris=None,
                 redirect_uris=None, refresh_token_effective=None, response_types=None, subject_id_expression=None):
        # The validity period of the issued access token. Unit: seconds. Default value: 1200.
        self.access_token_effective_time = access_token_effective_time  # type: long
        # The validity period of the issued code. Unit: seconds. Default value: 60.
        self.code_effective_time = code_effective_time  # type: long
        # The custom claims that are returned for the ID token.
        self.custom_claims = custom_claims  # type: list[GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfigCustomClaims]
        # The scopes of user attributes that can be returned for the UserInfo endpoint or ID token.
        self.grant_scopes = grant_scopes  # type: list[str]
        # The list of grant types that are supported for OIDC protocols.
        self.grant_types = grant_types  # type: list[str]
        # The validity period of the issued ID token. Unit: seconds. Default value: 300.
        self.id_token_effective_time = id_token_effective_time  # type: long
        # The ID of the identity authentication source in password mode. This parameter is returned only when the value of the GrantTypes parameter includes the password mode.
        self.password_authentication_source_id = password_authentication_source_id  # type: str
        # Indicates whether time-based one-time password (TOTP) authentication is required in password mode. This parameter is returned only when the value of the GrantTypes parameter includes the password mode.
        self.password_totp_mfa_required = password_totp_mfa_required  # type: bool
        # The algorithms that are used to calculate the code challenge for PKCE.
        self.pkce_challenge_methods = pkce_challenge_methods  # type: list[str]
        # Indicates whether the SSO of the application requires Proof Key for Code Exchange (PKCE) (RFC 7636).
        self.pkce_required = pkce_required  # type: bool
        # The list of logout redirect URIs that are supported by the application.
        self.post_logout_redirect_uris = post_logout_redirect_uris  # type: list[str]
        # The list of redirect URIs that are supported by the application.
        self.redirect_uris = redirect_uris  # type: list[str]
        # The validity period of the issued refresh token. Unit: seconds. Default value: 86400.
        self.refresh_token_effective = refresh_token_effective  # type: long
        # The response types that are supported by the application. This parameter is returned when the value of the GrantTypes parameter includes the implicit mode.
        self.response_types = response_types  # type: list[str]
        # The custom expression that is used to generate the subject ID returned for the ID token.
        self.subject_id_expression = subject_id_expression  # type: str

    def validate(self):
        if self.custom_claims:
            for k in self.custom_claims:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_effective_time is not None:
            result['AccessTokenEffectiveTime'] = self.access_token_effective_time
        if self.code_effective_time is not None:
            result['CodeEffectiveTime'] = self.code_effective_time
        result['CustomClaims'] = []
        if self.custom_claims is not None:
            for k in self.custom_claims:
                result['CustomClaims'].append(k.to_map() if k else None)
        if self.grant_scopes is not None:
            result['GrantScopes'] = self.grant_scopes
        if self.grant_types is not None:
            result['GrantTypes'] = self.grant_types
        if self.id_token_effective_time is not None:
            result['IdTokenEffectiveTime'] = self.id_token_effective_time
        if self.password_authentication_source_id is not None:
            result['PasswordAuthenticationSourceId'] = self.password_authentication_source_id
        if self.password_totp_mfa_required is not None:
            result['PasswordTotpMfaRequired'] = self.password_totp_mfa_required
        if self.pkce_challenge_methods is not None:
            result['PkceChallengeMethods'] = self.pkce_challenge_methods
        if self.pkce_required is not None:
            result['PkceRequired'] = self.pkce_required
        if self.post_logout_redirect_uris is not None:
            result['PostLogoutRedirectUris'] = self.post_logout_redirect_uris
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris
        if self.refresh_token_effective is not None:
            result['RefreshTokenEffective'] = self.refresh_token_effective
        if self.response_types is not None:
            result['ResponseTypes'] = self.response_types
        if self.subject_id_expression is not None:
            result['SubjectIdExpression'] = self.subject_id_expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenEffectiveTime') is not None:
            self.access_token_effective_time = m.get('AccessTokenEffectiveTime')
        if m.get('CodeEffectiveTime') is not None:
            self.code_effective_time = m.get('CodeEffectiveTime')
        self.custom_claims = []
        if m.get('CustomClaims') is not None:
            for k in m.get('CustomClaims'):
                temp_model = GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfigCustomClaims()
                self.custom_claims.append(temp_model.from_map(k))
        if m.get('GrantScopes') is not None:
            self.grant_scopes = m.get('GrantScopes')
        if m.get('GrantTypes') is not None:
            self.grant_types = m.get('GrantTypes')
        if m.get('IdTokenEffectiveTime') is not None:
            self.id_token_effective_time = m.get('IdTokenEffectiveTime')
        if m.get('PasswordAuthenticationSourceId') is not None:
            self.password_authentication_source_id = m.get('PasswordAuthenticationSourceId')
        if m.get('PasswordTotpMfaRequired') is not None:
            self.password_totp_mfa_required = m.get('PasswordTotpMfaRequired')
        if m.get('PkceChallengeMethods') is not None:
            self.pkce_challenge_methods = m.get('PkceChallengeMethods')
        if m.get('PkceRequired') is not None:
            self.pkce_required = m.get('PkceRequired')
        if m.get('PostLogoutRedirectUris') is not None:
            self.post_logout_redirect_uris = m.get('PostLogoutRedirectUris')
        if m.get('RedirectUris') is not None:
            self.redirect_uris = m.get('RedirectUris')
        if m.get('RefreshTokenEffective') is not None:
            self.refresh_token_effective = m.get('RefreshTokenEffective')
        if m.get('ResponseTypes') is not None:
            self.response_types = m.get('ResponseTypes')
        if m.get('SubjectIdExpression') is not None:
            self.subject_id_expression = m.get('SubjectIdExpression')
        return self


class GetApplicationSsoConfigResponseBodyApplicationSsoConfigProtocolEndpointDomain(TeaModel):
    def __init__(self, oauth_2authorization_endpoint=None, oauth_2device_authorization_endpoint=None,
                 oauth_2revoke_endpoint=None, oauth_2token_endpoint=None, oauth_2userinfo_endpoint=None, oidc_issuer=None,
                 oidc_jwks_endpoint=None, oidc_logout_endpoint=None, saml_meta_endpoint=None, saml_sso_endpoint=None):
        # The OAuth2.0 authorization endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol.
        self.oauth_2authorization_endpoint = oauth_2authorization_endpoint  # type: str
        # The OAuth2.0 device authorization endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol.
        self.oauth_2device_authorization_endpoint = oauth_2device_authorization_endpoint  # type: str
        # The OAuth2.0 token revocation endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol.
        self.oauth_2revoke_endpoint = oauth_2revoke_endpoint  # type: str
        # The OAuth2.0 token endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol.
        self.oauth_2token_endpoint = oauth_2token_endpoint  # type: str
        # The OIDC UserInfo endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol.
        self.oauth_2userinfo_endpoint = oauth_2userinfo_endpoint  # type: str
        # The information about the OIDC issuer. This parameter is returned only when the SSO protocol of the application is an OIDC protocol.
        self.oidc_issuer = oidc_issuer  # type: str
        # The JSON Web Key Set (JWKS) URL of the OIDC issuer. This parameter is returned only when the SSO protocol of the application is an OIDC protocol.
        self.oidc_jwks_endpoint = oidc_jwks_endpoint  # type: str
        # The OIDC relying party (RP)-initiated logout endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol.
        self.oidc_logout_endpoint = oidc_logout_endpoint  # type: str
        # The metadata URL of the SAML protocol. This parameter is returned only when the SSO protocol of the application is SAML 2.0.
        self.saml_meta_endpoint = saml_meta_endpoint  # type: str
        # The request receiving URL of the SAML protocol. This parameter is returned only when the SSO protocol of the application is SAML 2.0.
        self.saml_sso_endpoint = saml_sso_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationSsoConfigResponseBodyApplicationSsoConfigProtocolEndpointDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oauth_2authorization_endpoint is not None:
            result['Oauth2AuthorizationEndpoint'] = self.oauth_2authorization_endpoint
        if self.oauth_2device_authorization_endpoint is not None:
            result['Oauth2DeviceAuthorizationEndpoint'] = self.oauth_2device_authorization_endpoint
        if self.oauth_2revoke_endpoint is not None:
            result['Oauth2RevokeEndpoint'] = self.oauth_2revoke_endpoint
        if self.oauth_2token_endpoint is not None:
            result['Oauth2TokenEndpoint'] = self.oauth_2token_endpoint
        if self.oauth_2userinfo_endpoint is not None:
            result['Oauth2UserinfoEndpoint'] = self.oauth_2userinfo_endpoint
        if self.oidc_issuer is not None:
            result['OidcIssuer'] = self.oidc_issuer
        if self.oidc_jwks_endpoint is not None:
            result['OidcJwksEndpoint'] = self.oidc_jwks_endpoint
        if self.oidc_logout_endpoint is not None:
            result['OidcLogoutEndpoint'] = self.oidc_logout_endpoint
        if self.saml_meta_endpoint is not None:
            result['SamlMetaEndpoint'] = self.saml_meta_endpoint
        if self.saml_sso_endpoint is not None:
            result['SamlSsoEndpoint'] = self.saml_sso_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Oauth2AuthorizationEndpoint') is not None:
            self.oauth_2authorization_endpoint = m.get('Oauth2AuthorizationEndpoint')
        if m.get('Oauth2DeviceAuthorizationEndpoint') is not None:
            self.oauth_2device_authorization_endpoint = m.get('Oauth2DeviceAuthorizationEndpoint')
        if m.get('Oauth2RevokeEndpoint') is not None:
            self.oauth_2revoke_endpoint = m.get('Oauth2RevokeEndpoint')
        if m.get('Oauth2TokenEndpoint') is not None:
            self.oauth_2token_endpoint = m.get('Oauth2TokenEndpoint')
        if m.get('Oauth2UserinfoEndpoint') is not None:
            self.oauth_2userinfo_endpoint = m.get('Oauth2UserinfoEndpoint')
        if m.get('OidcIssuer') is not None:
            self.oidc_issuer = m.get('OidcIssuer')
        if m.get('OidcJwksEndpoint') is not None:
            self.oidc_jwks_endpoint = m.get('OidcJwksEndpoint')
        if m.get('OidcLogoutEndpoint') is not None:
            self.oidc_logout_endpoint = m.get('OidcLogoutEndpoint')
        if m.get('SamlMetaEndpoint') is not None:
            self.saml_meta_endpoint = m.get('SamlMetaEndpoint')
        if m.get('SamlSsoEndpoint') is not None:
            self.saml_sso_endpoint = m.get('SamlSsoEndpoint')
        return self


class GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfigAttributeStatements(TeaModel):
    def __init__(self, attribute_name=None, attribute_value_expression=None):
        # The attribute name.
        self.attribute_name = attribute_name  # type: str
        # The expression that is used to generate the value of the attribute.
        self.attribute_value_expression = attribute_value_expression  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfigAttributeStatements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value_expression is not None:
            result['AttributeValueExpression'] = self.attribute_value_expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValueExpression') is not None:
            self.attribute_value_expression = m.get('AttributeValueExpression')
        return self


class GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfig(TeaModel):
    def __init__(self, assertion_signed=None, attribute_statements=None, default_relay_state=None,
                 name_id_format=None, name_id_value_expression=None, response_signed=None, signature_algorithm=None,
                 sp_entity_id=None, sp_sso_acs_url=None):
        # assertion是否签名
        self.assertion_signed = assertion_signed  # type: bool
        # The additional user attributes in the SAML assertion.
        self.attribute_statements = attribute_statements  # type: list[GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfigAttributeStatements]
        # The default value of the RelayState attribute. If the SSO request is initiated in EIAM, the RelayState attribute in the SAML response is set to this default value.
        self.default_relay_state = default_relay_state  # type: str
        # The Format attribute of the NameID element in the SAML assertion. Valid values:
        # 
        # *   urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified: No format is specified. How to resolve the NameID element depends on the application.
        # *   urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress: The NameID element must be an email address.
        # *   urn:oasis:names:tc:SAML:2.0:nameid-format:persistent: The NameID element must be persistent.
        # *   urn:oasis:names:tc:SAML:2.0:nameid-format:transient: The NameID element must be transient.
        self.name_id_format = name_id_format  # type: str
        # The expression that is used to generate the value of NameID in the SAML assertion.
        self.name_id_value_expression = name_id_value_expression  # type: str
        # response是否签名
        self.response_signed = response_signed  # type: bool
        # The algorithm that is used to calculate the signature for the SAML assertion.
        self.signature_algorithm = signature_algorithm  # type: str
        # The entity ID of the application in SAML. The application assumes the role of service provider.
        self.sp_entity_id = sp_entity_id  # type: str
        # The Assertion Consumer Service (ACS) URL of the application in SAML. The application assumes the role of service provider.
        self.sp_sso_acs_url = sp_sso_acs_url  # type: str

    def validate(self):
        if self.attribute_statements:
            for k in self.attribute_statements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assertion_signed is not None:
            result['AssertionSigned'] = self.assertion_signed
        result['AttributeStatements'] = []
        if self.attribute_statements is not None:
            for k in self.attribute_statements:
                result['AttributeStatements'].append(k.to_map() if k else None)
        if self.default_relay_state is not None:
            result['DefaultRelayState'] = self.default_relay_state
        if self.name_id_format is not None:
            result['NameIdFormat'] = self.name_id_format
        if self.name_id_value_expression is not None:
            result['NameIdValueExpression'] = self.name_id_value_expression
        if self.response_signed is not None:
            result['ResponseSigned'] = self.response_signed
        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm
        if self.sp_entity_id is not None:
            result['SpEntityId'] = self.sp_entity_id
        if self.sp_sso_acs_url is not None:
            result['SpSsoAcsUrl'] = self.sp_sso_acs_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssertionSigned') is not None:
            self.assertion_signed = m.get('AssertionSigned')
        self.attribute_statements = []
        if m.get('AttributeStatements') is not None:
            for k in m.get('AttributeStatements'):
                temp_model = GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfigAttributeStatements()
                self.attribute_statements.append(temp_model.from_map(k))
        if m.get('DefaultRelayState') is not None:
            self.default_relay_state = m.get('DefaultRelayState')
        if m.get('NameIdFormat') is not None:
            self.name_id_format = m.get('NameIdFormat')
        if m.get('NameIdValueExpression') is not None:
            self.name_id_value_expression = m.get('NameIdValueExpression')
        if m.get('ResponseSigned') is not None:
            self.response_signed = m.get('ResponseSigned')
        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')
        if m.get('SpEntityId') is not None:
            self.sp_entity_id = m.get('SpEntityId')
        if m.get('SpSsoAcsUrl') is not None:
            self.sp_sso_acs_url = m.get('SpSsoAcsUrl')
        return self


class GetApplicationSsoConfigResponseBodyApplicationSsoConfig(TeaModel):
    def __init__(self, init_login_type=None, init_login_url=None, oidc_sso_config=None,
                 protocol_endpoint_domain=None, saml_sso_config=None, sso_status=None):
        # The initial SSO method. Valid values:
        # 
        # *   only_app_init_sso: Only application-initiated SSO is allowed. This method is selected by default when the SSO protocol of the application is an OIDC protocol. If this method is selected when the SSO protocol of the application is SAML, the InitLoginUrl parameter is required.
        # *   idaas_or_app_init_sso: IDaaS-initiated SSO and application-initiated SSO are allowed. This method is selected by default when the SSO protocol of the application is SAML. If this method is selected when the SSO protocol of the application is an OIDC protocol, the InitLoginUrl parameter is required.
        self.init_login_type = init_login_type  # type: str
        # The initial webhook URL of SSO. This parameter is required when the SSO protocol of the application is an OIDC protocol and the InitLoginType parameters is set to idaas_or_app_init_sso or when the SSO protocol of the application is SAML and the InitLoginType parameter is set to only_app_init_sso.
        self.init_login_url = init_login_url  # type: str
        # The Open ID Connect (OIDC)-based SSO configuration attributes of the application. This parameter is returned only when the SSO protocol of the application is an OIDC protocol.
        self.oidc_sso_config = oidc_sso_config  # type: GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfig
        # The configuration of the metadata endpoint provided by the application.
        self.protocol_endpoint_domain = protocol_endpoint_domain  # type: GetApplicationSsoConfigResponseBodyApplicationSsoConfigProtocolEndpointDomain
        # The Security Assertion Markup Language (SAML)-based SSO configuration attributes of the application. This parameter is returned only when the SSO protocol of the application is SAML 2.0.
        self.saml_sso_config = saml_sso_config  # type: GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfig
        # The SSO feature status of the application. Valid values:
        # 
        # *   enabled: The feature is enabled.
        # *   disabled: The feature is disabled.
        self.sso_status = sso_status  # type: str

    def validate(self):
        if self.oidc_sso_config:
            self.oidc_sso_config.validate()
        if self.protocol_endpoint_domain:
            self.protocol_endpoint_domain.validate()
        if self.saml_sso_config:
            self.saml_sso_config.validate()

    def to_map(self):
        _map = super(GetApplicationSsoConfigResponseBodyApplicationSsoConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.init_login_type is not None:
            result['InitLoginType'] = self.init_login_type
        if self.init_login_url is not None:
            result['InitLoginUrl'] = self.init_login_url
        if self.oidc_sso_config is not None:
            result['OidcSsoConfig'] = self.oidc_sso_config.to_map()
        if self.protocol_endpoint_domain is not None:
            result['ProtocolEndpointDomain'] = self.protocol_endpoint_domain.to_map()
        if self.saml_sso_config is not None:
            result['SamlSsoConfig'] = self.saml_sso_config.to_map()
        if self.sso_status is not None:
            result['SsoStatus'] = self.sso_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InitLoginType') is not None:
            self.init_login_type = m.get('InitLoginType')
        if m.get('InitLoginUrl') is not None:
            self.init_login_url = m.get('InitLoginUrl')
        if m.get('OidcSsoConfig') is not None:
            temp_model = GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfig()
            self.oidc_sso_config = temp_model.from_map(m['OidcSsoConfig'])
        if m.get('ProtocolEndpointDomain') is not None:
            temp_model = GetApplicationSsoConfigResponseBodyApplicationSsoConfigProtocolEndpointDomain()
            self.protocol_endpoint_domain = temp_model.from_map(m['ProtocolEndpointDomain'])
        if m.get('SamlSsoConfig') is not None:
            temp_model = GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfig()
            self.saml_sso_config = temp_model.from_map(m['SamlSsoConfig'])
        if m.get('SsoStatus') is not None:
            self.sso_status = m.get('SsoStatus')
        return self


class GetApplicationSsoConfigResponseBody(TeaModel):
    def __init__(self, application_sso_config=None, request_id=None):
        # The SSO configuration information of the application.
        self.application_sso_config = application_sso_config  # type: GetApplicationSsoConfigResponseBodyApplicationSsoConfig
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application_sso_config:
            self.application_sso_config.validate()

    def to_map(self):
        _map = super(GetApplicationSsoConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_sso_config is not None:
            result['ApplicationSsoConfig'] = self.application_sso_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationSsoConfig') is not None:
            temp_model = GetApplicationSsoConfigResponseBodyApplicationSsoConfig()
            self.application_sso_config = temp_model.from_map(m['ApplicationSsoConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationSsoConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApplicationSsoConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApplicationSsoConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetApplicationSsoConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainRequest(TeaModel):
    def __init__(self, domain_id=None, instance_id=None):
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDomainResponseBodyDomainFiling(TeaModel):
    def __init__(self, icp_number=None):
        # 域名关联的备案号, 长度最大限制64。
        self.icp_number = icp_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainResponseBodyDomainFiling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icp_number is not None:
            result['IcpNumber'] = self.icp_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IcpNumber') is not None:
            self.icp_number = m.get('IcpNumber')
        return self


class GetDomainResponseBodyDomain(TeaModel):
    def __init__(self, create_time=None, default_domain=None, domain=None, domain_id=None, domain_type=None,
                 filing=None, instance_id=None, lock_mode=None, update_time=None):
        # 域名创建时间，Unix时间戳格式，单位为毫秒。
        self.create_time = create_time  # type: long
        # 是否默认域名。true表示实例默认域名，false表示非默认域名
        self.default_domain = default_domain  # type: bool
        # 域名。
        self.domain = domain  # type: str
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # 域名类型。枚举取值:system_init(系统初始化)、user_custom(用户自定义)。
        self.domain_type = domain_type  # type: str
        # 域名备案信息。
        self.filing = filing  # type: GetDomainResponseBodyDomainFiling
        # 实例ID。
        self.instance_id = instance_id  # type: str
        # 域名锁定状态。枚举取值:unlock(正常)、lockByLicense(因License限制不可用)。
        self.lock_mode = lock_mode  # type: str
        # 域名最近更新时间，Unix时间戳格式，单位为毫秒。
        self.update_time = update_time  # type: long

    def validate(self):
        if self.filing:
            self.filing.validate()

    def to_map(self):
        _map = super(GetDomainResponseBodyDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.filing is not None:
            result['Filing'] = self.filing.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('Filing') is not None:
            temp_model = GetDomainResponseBodyDomainFiling()
            self.filing = temp_model.from_map(m['Filing'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetDomainResponseBody(TeaModel):
    def __init__(self, domain=None, request_id=None):
        self.domain = domain  # type: GetDomainResponseBodyDomain
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain:
            self.domain.validate()

    def to_map(self):
        _map = super(GetDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            temp_model = GetDomainResponseBodyDomain()
            self.domain = temp_model.from_map(m['Domain'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainDnsChallengeRequest(TeaModel):
    def __init__(self, domain=None, instance_id=None):
        # 域名。
        self.domain = domain  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainDnsChallengeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDomainDnsChallengeResponseBodyDomainDnsChallenge(TeaModel):
    def __init__(self, dns_challenge_name=None, dns_challenge_value=None, dns_type=None):
        # DNS challenge名称。
        self.dns_challenge_name = dns_challenge_name  # type: str
        # DNS challenge值。
        self.dns_challenge_value = dns_challenge_value  # type: str
        # DNS记录类型。
        self.dns_type = dns_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainDnsChallengeResponseBodyDomainDnsChallenge, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_challenge_name is not None:
            result['DnsChallengeName'] = self.dns_challenge_name
        if self.dns_challenge_value is not None:
            result['DnsChallengeValue'] = self.dns_challenge_value
        if self.dns_type is not None:
            result['DnsType'] = self.dns_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsChallengeName') is not None:
            self.dns_challenge_name = m.get('DnsChallengeName')
        if m.get('DnsChallengeValue') is not None:
            self.dns_challenge_value = m.get('DnsChallengeValue')
        if m.get('DnsType') is not None:
            self.dns_type = m.get('DnsType')
        return self


class GetDomainDnsChallengeResponseBody(TeaModel):
    def __init__(self, domain_dns_challenge=None, request_id=None):
        self.domain_dns_challenge = domain_dns_challenge  # type: GetDomainDnsChallengeResponseBodyDomainDnsChallenge
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_dns_challenge:
            self.domain_dns_challenge.validate()

    def to_map(self):
        _map = super(GetDomainDnsChallengeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_dns_challenge is not None:
            result['DomainDnsChallenge'] = self.domain_dns_challenge.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainDnsChallenge') is not None:
            temp_model = GetDomainDnsChallengeResponseBodyDomainDnsChallenge()
            self.domain_dns_challenge = temp_model.from_map(m['DomainDnsChallenge'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainDnsChallengeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDomainDnsChallengeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDomainDnsChallengeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDomainDnsChallengeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetForgetPasswordConfigurationRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetForgetPasswordConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetForgetPasswordConfigurationResponseBodyOpenForgetPasswordConfiguration(TeaModel):
    def __init__(self, authentication_channels=None, enable=None, enable_email=None, enable_sms=None,
                 forget_password_status=None):
        # 表示忘记密码认证渠道。枚举取值:email(邮件)、sms(短信)
        self.authentication_channels = authentication_channels  # type: list[str]
        # Indicates whether the forgot password feature is enabled.
        self.enable = enable  # type: bool
        # Indicates whether email authentication is enabled for the forgot password feature.
        self.enable_email = enable_email  # type: bool
        # Indicates whether Short Message Service (SMS) authentication is enabled for the forgot password feature.
        self.enable_sms = enable_sms  # type: bool
        # 表示忘记密码配置状态。枚举取值:enabled(开启)、disabled(禁用)
        self.forget_password_status = forget_password_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetForgetPasswordConfigurationResponseBodyOpenForgetPasswordConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_channels is not None:
            result['AuthenticationChannels'] = self.authentication_channels
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.enable_email is not None:
            result['EnableEmail'] = self.enable_email
        if self.enable_sms is not None:
            result['EnableSms'] = self.enable_sms
        if self.forget_password_status is not None:
            result['ForgetPasswordStatus'] = self.forget_password_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthenticationChannels') is not None:
            self.authentication_channels = m.get('AuthenticationChannels')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EnableEmail') is not None:
            self.enable_email = m.get('EnableEmail')
        if m.get('EnableSms') is not None:
            self.enable_sms = m.get('EnableSms')
        if m.get('ForgetPasswordStatus') is not None:
            self.forget_password_status = m.get('ForgetPasswordStatus')
        return self


class GetForgetPasswordConfigurationResponseBody(TeaModel):
    def __init__(self, open_forget_password_configuration=None, request_id=None):
        # The forgot password configurations.
        self.open_forget_password_configuration = open_forget_password_configuration  # type: GetForgetPasswordConfigurationResponseBodyOpenForgetPasswordConfiguration
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.open_forget_password_configuration:
            self.open_forget_password_configuration.validate()

    def to_map(self):
        _map = super(GetForgetPasswordConfigurationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_forget_password_configuration is not None:
            result['OpenForgetPasswordConfiguration'] = self.open_forget_password_configuration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenForgetPasswordConfiguration') is not None:
            temp_model = GetForgetPasswordConfigurationResponseBodyOpenForgetPasswordConfiguration()
            self.open_forget_password_configuration = temp_model.from_map(m['OpenForgetPasswordConfiguration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetForgetPasswordConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetForgetPasswordConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetForgetPasswordConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetForgetPasswordConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None):
        # The group ID.
        self.group_id = group_id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetGroupResponseBodyGroup(TeaModel):
    def __init__(self, create_time=None, description=None, group_external_id=None, group_id=None, group_name=None,
                 group_source_id=None, group_source_type=None, instance_id=None, update_time=None):
        # The time at which the group was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time  # type: long
        # The description of the group.
        self.description = description  # type: str
        # The external ID of the group, which can be used to associate the group with an external system. By default, the external ID is the group ID.
        self.group_external_id = group_external_id  # type: str
        # The group ID.
        self.group_id = group_id  # type: str
        # The name of the group.
        self.group_name = group_name  # type: str
        # The source ID of the group. By default, the source ID is the instance ID.
        self.group_source_id = group_source_id  # type: str
        # The source type of the group. Only build_in may be returned, which indicates that the group was created in IDaaS.
        # 
        # *\
        self.group_source_type = group_source_type  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The time at which the group was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupResponseBodyGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_external_id is not None:
            result['GroupExternalId'] = self.group_external_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_source_id is not None:
            result['GroupSourceId'] = self.group_source_id
        if self.group_source_type is not None:
            result['GroupSourceType'] = self.group_source_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupExternalId') is not None:
            self.group_external_id = m.get('GroupExternalId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupSourceId') is not None:
            self.group_source_id = m.get('GroupSourceId')
        if m.get('GroupSourceType') is not None:
            self.group_source_type = m.get('GroupSourceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetGroupResponseBody(TeaModel):
    def __init__(self, group=None, request_id=None):
        # The information about the account group.
        self.group = group  # type: GetGroupResponseBodyGroup
        # The request ID.
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


class GetInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstanceResponseBodyInstanceDefaultEndpoint(TeaModel):
    def __init__(self, endpoint=None, status=None):
        # The endpoint of the instance.
        self.endpoint = endpoint  # type: str
        # The status of the endpoint. Valid values:
        # 
        # *   resolved
        # *   unresolved
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstanceDefaultEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceResponseBodyInstanceDomainConfig(TeaModel):
    def __init__(self, default_domain=None, init_domain=None, init_domain_auto_redirect_status=None):
        # The default domain of the instance.
        self.default_domain = default_domain  # type: str
        # The init domain of the instance.
        self.init_domain = init_domain  # type: str
        # Valid values:
        # 
        # *   true
        # *   false
        self.init_domain_auto_redirect_status = init_domain_auto_redirect_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstanceDomainConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.init_domain is not None:
            result['InitDomain'] = self.init_domain
        if self.init_domain_auto_redirect_status is not None:
            result['InitDomainAutoRedirectStatus'] = self.init_domain_auto_redirect_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('InitDomain') is not None:
            self.init_domain = m.get('InitDomain')
        if m.get('InitDomainAutoRedirectStatus') is not None:
            self.init_domain_auto_redirect_status = m.get('InitDomainAutoRedirectStatus')
        return self


class GetInstanceResponseBodyInstance(TeaModel):
    def __init__(self, create_time=None, default_endpoint=None, description=None, domain_config=None,
                 egress_addresses=None, instance_id=None, status=None):
        # The time when the instance was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time  # type: long
        # The default endpoint of the instance.
        self.default_endpoint = default_endpoint  # type: GetInstanceResponseBodyInstanceDefaultEndpoint
        # The description of the instance.
        self.description = description  # type: str
        # The default domain of the instance.
        self.domain_config = domain_config  # type: GetInstanceResponseBodyInstanceDomainConfig
        # The outbound public CIDR blocks of the instance. For example, when you synchronize Active Directory (AD) accounts, the IDaaS EIAM instance accesses your AD service by using the outbound public CIDR blocks.
        self.egress_addresses = egress_addresses  # type: list[str]
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The status of the instance. Valid values:
        # 
        # *   creating
        # *   running
        self.status = status  # type: str

    def validate(self):
        if self.default_endpoint:
            self.default_endpoint.validate()
        if self.domain_config:
            self.domain_config.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_config is not None:
            result['DomainConfig'] = self.domain_config.to_map()
        if self.egress_addresses is not None:
            result['EgressAddresses'] = self.egress_addresses
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultEndpoint') is not None:
            temp_model = GetInstanceResponseBodyInstanceDefaultEndpoint()
            self.default_endpoint = temp_model.from_map(m['DefaultEndpoint'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainConfig') is not None:
            temp_model = GetInstanceResponseBodyInstanceDomainConfig()
            self.domain_config = temp_model.from_map(m['DomainConfig'])
        if m.get('EgressAddresses') is not None:
            self.egress_addresses = m.get('EgressAddresses')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, instance=None, request_id=None):
        # The details of the instance.
        self.instance = instance  # type: GetInstanceResponseBodyInstance
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = GetInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNetworkAccessEndpointRequest(TeaModel):
    def __init__(self, instance_id=None, network_access_endpoint_id=None):
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str
        # 专属网络端点ID。
        self.network_access_endpoint_id = network_access_endpoint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNetworkAccessEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')
        return self


class GetNetworkAccessEndpointResponseBodyNetworkAccessEndpoint(TeaModel):
    def __init__(self, create_time=None, egress_private_ip_addresses=None, egress_public_ip_addresses=None,
                 instance_id=None, network_access_endpoint_id=None, network_access_endpoint_name=None,
                 network_access_endpoint_type=None, security_group_id=None, status=None, update_time=None, v_switch_ids=None, vpc_id=None,
                 vpc_region_id=None):
        # 专属网络端点创建时间，Unix时间戳格式，单位为毫秒。
        self.create_time = create_time  # type: long
        # 网络访问端私网出口IP地址列表。
        self.egress_private_ip_addresses = egress_private_ip_addresses  # type: list[str]
        # 网络访问端点公网出口IP地址段
        self.egress_public_ip_addresses = egress_public_ip_addresses  # type: list[str]
        # 实例ID。
        self.instance_id = instance_id  # type: str
        # 专属网络端点ID。
        self.network_access_endpoint_id = network_access_endpoint_id  # type: str
        # 专属网络端点名称。
        self.network_access_endpoint_name = network_access_endpoint_name  # type: str
        # 专属网络端点连接的类型。
        self.network_access_endpoint_type = network_access_endpoint_type  # type: str
        # 专属网络端点使用的安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 专属网络端点状态。
        self.status = status  # type: str
        # 专属网络端点最近更新时间，Unix时间戳格式，单位为毫秒。
        self.update_time = update_time  # type: long
        # 专属网络端点连接的指定vSwitch列表。
        self.v_switch_ids = v_switch_ids  # type: list[str]
        # 专属网络端点连接的VpcID。
        self.vpc_id = vpc_id  # type: str
        # 专属网络端点连接的Vpc所属地域。
        self.vpc_region_id = vpc_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNetworkAccessEndpointResponseBodyNetworkAccessEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.egress_private_ip_addresses is not None:
            result['EgressPrivateIpAddresses'] = self.egress_private_ip_addresses
        if self.egress_public_ip_addresses is not None:
            result['EgressPublicIpAddresses'] = self.egress_public_ip_addresses
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id
        if self.network_access_endpoint_name is not None:
            result['NetworkAccessEndpointName'] = self.network_access_endpoint_name
        if self.network_access_endpoint_type is not None:
            result['NetworkAccessEndpointType'] = self.network_access_endpoint_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EgressPrivateIpAddresses') is not None:
            self.egress_private_ip_addresses = m.get('EgressPrivateIpAddresses')
        if m.get('EgressPublicIpAddresses') is not None:
            self.egress_public_ip_addresses = m.get('EgressPublicIpAddresses')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')
        if m.get('NetworkAccessEndpointName') is not None:
            self.network_access_endpoint_name = m.get('NetworkAccessEndpointName')
        if m.get('NetworkAccessEndpointType') is not None:
            self.network_access_endpoint_type = m.get('NetworkAccessEndpointType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        return self


class GetNetworkAccessEndpointResponseBody(TeaModel):
    def __init__(self, network_access_endpoint=None, request_id=None):
        self.network_access_endpoint = network_access_endpoint  # type: GetNetworkAccessEndpointResponseBodyNetworkAccessEndpoint
        self.request_id = request_id  # type: str

    def validate(self):
        if self.network_access_endpoint:
            self.network_access_endpoint.validate()

    def to_map(self):
        _map = super(GetNetworkAccessEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_access_endpoint is not None:
            result['NetworkAccessEndpoint'] = self.network_access_endpoint.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkAccessEndpoint') is not None:
            temp_model = GetNetworkAccessEndpointResponseBodyNetworkAccessEndpoint()
            self.network_access_endpoint = temp_model.from_map(m['NetworkAccessEndpoint'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNetworkAccessEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNetworkAccessEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNetworkAccessEndpointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNetworkAccessEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrganizationalUnitRequest(TeaModel):
    def __init__(self, instance_id=None, organizational_unit_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrganizationalUnitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        return self


class GetOrganizationalUnitResponseBodyOrganizationalUnit(TeaModel):
    def __init__(self, create_time=None, description=None, instance_id=None, leaf=None,
                 organizational_unit_external_id=None, organizational_unit_id=None, organizational_unit_name=None,
                 organizational_unit_source_id=None, organizational_unit_source_type=None, parent_id=None, update_time=None):
        # The time when the organizational unit was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The description of the organizational unit.
        self.description = description  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether the node is a leaf node.
        self.leaf = leaf  # type: bool
        # The external ID of the organizational unit. The external ID can be used by external data to map the data of the organizational unit in IDaaS EIAM. By default, the external ID is the organizational unit ID.
        # 
        # For organizational units with the same source type and source ID, each organizational unit has a unique external ID.
        self.organizational_unit_external_id = organizational_unit_external_id  # type: str
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id  # type: str
        # 组织名称。
        self.organizational_unit_name = organizational_unit_name  # type: str
        # The source ID of the organizational unit.
        # 
        # If the organizational unit was created in IDaaS, its source ID is the ID of the IDaaS instance. If the organizational unit was imported, its source ID is the enterprise ID in the source. For example, if the organizational unit was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk.
        self.organizational_unit_source_id = organizational_unit_source_id  # type: str
        # The source type of the organizational unit. Valid values:
        # 
        # *   build_in: The organizational unit was created in IDaaS.
        # *   ding_talk: The organizational unit was imported from DingTalk.
        # *   ad: The organizational unit was imported from Microsoft Active Directory (AD).
        # *   ldap: The organizational unit was imported from a Lightweight Directory Access Protocol (LDAP) service.
        self.organizational_unit_source_type = organizational_unit_source_type  # type: str
        # The ID of the parent organizational unit.
        self.parent_id = parent_id  # type: str
        # The time when the organizational unit was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrganizationalUnitResponseBodyOrganizationalUnit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.leaf is not None:
            result['Leaf'] = self.leaf
        if self.organizational_unit_external_id is not None:
            result['OrganizationalUnitExternalId'] = self.organizational_unit_external_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name
        if self.organizational_unit_source_id is not None:
            result['OrganizationalUnitSourceId'] = self.organizational_unit_source_id
        if self.organizational_unit_source_type is not None:
            result['OrganizationalUnitSourceType'] = self.organizational_unit_source_type
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Leaf') is not None:
            self.leaf = m.get('Leaf')
        if m.get('OrganizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('OrganizationalUnitExternalId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')
        if m.get('OrganizationalUnitSourceId') is not None:
            self.organizational_unit_source_id = m.get('OrganizationalUnitSourceId')
        if m.get('OrganizationalUnitSourceType') is not None:
            self.organizational_unit_source_type = m.get('OrganizationalUnitSourceType')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetOrganizationalUnitResponseBody(TeaModel):
    def __init__(self, organizational_unit=None, request_id=None):
        # The data object of the organizational unit.
        self.organizational_unit = organizational_unit  # type: GetOrganizationalUnitResponseBodyOrganizationalUnit
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.organizational_unit:
            self.organizational_unit.validate()

    def to_map(self):
        _map = super(GetOrganizationalUnitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit is not None:
            result['OrganizationalUnit'] = self.organizational_unit.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationalUnit') is not None:
            temp_model = GetOrganizationalUnitResponseBodyOrganizationalUnit()
            self.organizational_unit = temp_model.from_map(m['OrganizationalUnit'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOrganizationalUnitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOrganizationalUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrganizationalUnitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOrganizationalUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPasswordComplexityConfigurationRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPasswordComplexityConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfigurationPasswordComplexityRules(TeaModel):
    def __init__(self, password_check_type=None):
        # The type of the password check. Valid values:
        # 
        # *   inclusion_upper_case: The password must contain uppercase letters.
        # *   inclusion_lower_case: The password must contain lowercase letters.
        # *   inclusion_special_case: The password must contain one or more of the following special characters: @ % + \ / \" ! # $ ^ ? : , ( ) { } \[ ] ~ - \_ .
        # *   inclusion_number: The password must contain digits.
        # *   exclusion_username: The password cannot contain a username.
        # *   exclusion_email: The password cannot contain an email prefix.
        # *   exclusion_phone_number: The password cannot contain a mobile number.
        # *   exclusion_display_name: The password cannot contain a display name.
        self.password_check_type = password_check_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfigurationPasswordComplexityRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_check_type is not None:
            result['PasswordCheckType'] = self.password_check_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordCheckType') is not None:
            self.password_check_type = m.get('PasswordCheckType')
        return self


class GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfiguration(TeaModel):
    def __init__(self, password_complexity_rules=None, password_min_length=None):
        # The password complexity rules.
        self.password_complexity_rules = password_complexity_rules  # type: list[GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfigurationPasswordComplexityRules]
        # The minimum number of characters in a password.
        self.password_min_length = password_min_length  # type: int

    def validate(self):
        if self.password_complexity_rules:
            for k in self.password_complexity_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PasswordComplexityRules'] = []
        if self.password_complexity_rules is not None:
            for k in self.password_complexity_rules:
                result['PasswordComplexityRules'].append(k.to_map() if k else None)
        if self.password_min_length is not None:
            result['PasswordMinLength'] = self.password_min_length
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.password_complexity_rules = []
        if m.get('PasswordComplexityRules') is not None:
            for k in m.get('PasswordComplexityRules'):
                temp_model = GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfigurationPasswordComplexityRules()
                self.password_complexity_rules.append(temp_model.from_map(k))
        if m.get('PasswordMinLength') is not None:
            self.password_min_length = m.get('PasswordMinLength')
        return self


class GetPasswordComplexityConfigurationResponseBody(TeaModel):
    def __init__(self, password_complexity_configuration=None, request_id=None):
        # The password complexity configurations.
        self.password_complexity_configuration = password_complexity_configuration  # type: GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfiguration
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.password_complexity_configuration:
            self.password_complexity_configuration.validate()

    def to_map(self):
        _map = super(GetPasswordComplexityConfigurationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_complexity_configuration is not None:
            result['PasswordComplexityConfiguration'] = self.password_complexity_configuration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordComplexityConfiguration') is not None:
            temp_model = GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfiguration()
            self.password_complexity_configuration = temp_model.from_map(m['PasswordComplexityConfiguration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPasswordComplexityConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPasswordComplexityConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPasswordComplexityConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPasswordComplexityConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPasswordExpirationConfigurationRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPasswordExpirationConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetPasswordExpirationConfigurationResponseBodyPasswordExpirationConfiguration(TeaModel):
    def __init__(self, password_expiration_action=None, password_expiration_notification_channels=None,
                 password_expiration_notification_duration=None, password_expiration_notification_status=None, password_expiration_status=None,
                 password_forced_update_duration=None, password_valid_max_day=None):
        # The action to take when a password expires. Valid values:
        # 
        # *   forbid_login: Prohibit the user from using the password to log on to IDaaS.
        # *   force_update_password: Force the user to change the password.
        # *   remind_update_password: Remind the user to change the password.
        self.password_expiration_action = password_expiration_action  # type: str
        # The methods for receiving password expiration notifications.
        self.password_expiration_notification_channels = password_expiration_notification_channels  # type: list[str]
        # The number of days before the expiration date during which password expiration notifications are sent. Unit: day.
        self.password_expiration_notification_duration = password_expiration_notification_duration  # type: int
        # Indicates whether the password expiration notification feature is enabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_expiration_notification_status = password_expiration_notification_status  # type: str
        # Indicates whether the password expiration feature is enabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_expiration_status = password_expiration_status  # type: str
        # The number of days before which users must change the password to prevent password expiration. Unit: day.
        self.password_forced_update_duration = password_forced_update_duration  # type: int
        # The validity period of a password. Unit: day.
        self.password_valid_max_day = password_valid_max_day  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPasswordExpirationConfigurationResponseBodyPasswordExpirationConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_expiration_action is not None:
            result['PasswordExpirationAction'] = self.password_expiration_action
        if self.password_expiration_notification_channels is not None:
            result['PasswordExpirationNotificationChannels'] = self.password_expiration_notification_channels
        if self.password_expiration_notification_duration is not None:
            result['PasswordExpirationNotificationDuration'] = self.password_expiration_notification_duration
        if self.password_expiration_notification_status is not None:
            result['PasswordExpirationNotificationStatus'] = self.password_expiration_notification_status
        if self.password_expiration_status is not None:
            result['PasswordExpirationStatus'] = self.password_expiration_status
        if self.password_forced_update_duration is not None:
            result['PasswordForcedUpdateDuration'] = self.password_forced_update_duration
        if self.password_valid_max_day is not None:
            result['PasswordValidMaxDay'] = self.password_valid_max_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordExpirationAction') is not None:
            self.password_expiration_action = m.get('PasswordExpirationAction')
        if m.get('PasswordExpirationNotificationChannels') is not None:
            self.password_expiration_notification_channels = m.get('PasswordExpirationNotificationChannels')
        if m.get('PasswordExpirationNotificationDuration') is not None:
            self.password_expiration_notification_duration = m.get('PasswordExpirationNotificationDuration')
        if m.get('PasswordExpirationNotificationStatus') is not None:
            self.password_expiration_notification_status = m.get('PasswordExpirationNotificationStatus')
        if m.get('PasswordExpirationStatus') is not None:
            self.password_expiration_status = m.get('PasswordExpirationStatus')
        if m.get('PasswordForcedUpdateDuration') is not None:
            self.password_forced_update_duration = m.get('PasswordForcedUpdateDuration')
        if m.get('PasswordValidMaxDay') is not None:
            self.password_valid_max_day = m.get('PasswordValidMaxDay')
        return self


class GetPasswordExpirationConfigurationResponseBody(TeaModel):
    def __init__(self, password_expiration_configuration=None, request_id=None):
        # The password expiration configurations.
        self.password_expiration_configuration = password_expiration_configuration  # type: GetPasswordExpirationConfigurationResponseBodyPasswordExpirationConfiguration
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.password_expiration_configuration:
            self.password_expiration_configuration.validate()

    def to_map(self):
        _map = super(GetPasswordExpirationConfigurationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_expiration_configuration is not None:
            result['PasswordExpirationConfiguration'] = self.password_expiration_configuration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordExpirationConfiguration') is not None:
            temp_model = GetPasswordExpirationConfigurationResponseBodyPasswordExpirationConfiguration()
            self.password_expiration_configuration = temp_model.from_map(m['PasswordExpirationConfiguration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPasswordExpirationConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPasswordExpirationConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPasswordExpirationConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPasswordExpirationConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPasswordHistoryConfigurationRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPasswordHistoryConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetPasswordHistoryConfigurationResponseBodyPasswordHistoryConfiguration(TeaModel):
    def __init__(self, password_history_max_retention=None, password_history_status=None):
        # The maximum number of recent passwords that are retained.
        self.password_history_max_retention = password_history_max_retention  # type: int
        # Indicates whether the password history feature is enabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_history_status = password_history_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPasswordHistoryConfigurationResponseBodyPasswordHistoryConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_history_max_retention is not None:
            result['PasswordHistoryMaxRetention'] = self.password_history_max_retention
        if self.password_history_status is not None:
            result['PasswordHistoryStatus'] = self.password_history_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordHistoryMaxRetention') is not None:
            self.password_history_max_retention = m.get('PasswordHistoryMaxRetention')
        if m.get('PasswordHistoryStatus') is not None:
            self.password_history_status = m.get('PasswordHistoryStatus')
        return self


class GetPasswordHistoryConfigurationResponseBody(TeaModel):
    def __init__(self, password_history_configuration=None, request_id=None):
        # The password history configurations.
        self.password_history_configuration = password_history_configuration  # type: GetPasswordHistoryConfigurationResponseBodyPasswordHistoryConfiguration
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.password_history_configuration:
            self.password_history_configuration.validate()

    def to_map(self):
        _map = super(GetPasswordHistoryConfigurationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_history_configuration is not None:
            result['PasswordHistoryConfiguration'] = self.password_history_configuration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordHistoryConfiguration') is not None:
            temp_model = GetPasswordHistoryConfigurationResponseBodyPasswordHistoryConfiguration()
            self.password_history_configuration = temp_model.from_map(m['PasswordHistoryConfiguration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPasswordHistoryConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPasswordHistoryConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPasswordHistoryConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPasswordHistoryConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPasswordInitializationConfigurationRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPasswordInitializationConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetPasswordInitializationConfigurationResponseBodyPasswordInitializationConfiguration(TeaModel):
    def __init__(self, password_forced_update_status=None, password_initialization_notification_channels=None,
                 password_initialization_status=None, password_initialization_type=None):
        # Indicates whether forcible password change upon first logon is enabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_forced_update_status = password_forced_update_status  # type: str
        # The methods for receiving password initialization notifications.
        self.password_initialization_notification_channels = password_initialization_notification_channels  # type: list[str]
        # Indicates whether the password initialization feature is enabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_initialization_status = password_initialization_status  # type: str
        # The password initialization method. Set the value to random.
        # 
        # *   random: A randomly generated password is used.
        self.password_initialization_type = password_initialization_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPasswordInitializationConfigurationResponseBodyPasswordInitializationConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_forced_update_status is not None:
            result['PasswordForcedUpdateStatus'] = self.password_forced_update_status
        if self.password_initialization_notification_channels is not None:
            result['PasswordInitializationNotificationChannels'] = self.password_initialization_notification_channels
        if self.password_initialization_status is not None:
            result['PasswordInitializationStatus'] = self.password_initialization_status
        if self.password_initialization_type is not None:
            result['PasswordInitializationType'] = self.password_initialization_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordForcedUpdateStatus') is not None:
            self.password_forced_update_status = m.get('PasswordForcedUpdateStatus')
        if m.get('PasswordInitializationNotificationChannels') is not None:
            self.password_initialization_notification_channels = m.get('PasswordInitializationNotificationChannels')
        if m.get('PasswordInitializationStatus') is not None:
            self.password_initialization_status = m.get('PasswordInitializationStatus')
        if m.get('PasswordInitializationType') is not None:
            self.password_initialization_type = m.get('PasswordInitializationType')
        return self


class GetPasswordInitializationConfigurationResponseBody(TeaModel):
    def __init__(self, password_initialization_configuration=None, request_id=None):
        # The password initialization configurations.
        self.password_initialization_configuration = password_initialization_configuration  # type: GetPasswordInitializationConfigurationResponseBodyPasswordInitializationConfiguration
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.password_initialization_configuration:
            self.password_initialization_configuration.validate()

    def to_map(self):
        _map = super(GetPasswordInitializationConfigurationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_initialization_configuration is not None:
            result['PasswordInitializationConfiguration'] = self.password_initialization_configuration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordInitializationConfiguration') is not None:
            temp_model = GetPasswordInitializationConfigurationResponseBodyPasswordInitializationConfiguration()
            self.password_initialization_configuration = temp_model.from_map(m['PasswordInitializationConfiguration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPasswordInitializationConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPasswordInitializationConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPasswordInitializationConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPasswordInitializationConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRootOrganizationalUnitRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRootOrganizationalUnitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetRootOrganizationalUnitResponseBodyOrganizationalUnit(TeaModel):
    def __init__(self, create_time=None, description=None, instance_id=None, organizational_unit_id=None,
                 organizational_unit_name=None, update_time=None):
        # The time when the organizational unit was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The description of the organizational unit.
        self.description = description  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id  # type: str
        # The name of the organization.
        self.organizational_unit_name = organizational_unit_name  # type: str
        # The time when the organizational unit was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRootOrganizationalUnitResponseBodyOrganizationalUnit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetRootOrganizationalUnitResponseBody(TeaModel):
    def __init__(self, organizational_unit=None, request_id=None):
        # The data object of the organizational unit.
        self.organizational_unit = organizational_unit  # type: GetRootOrganizationalUnitResponseBodyOrganizationalUnit
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.organizational_unit:
            self.organizational_unit.validate()

    def to_map(self):
        _map = super(GetRootOrganizationalUnitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit is not None:
            result['OrganizationalUnit'] = self.organizational_unit.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationalUnit') is not None:
            temp_model = GetRootOrganizationalUnitResponseBodyOrganizationalUnit()
            self.organizational_unit = temp_model.from_map(m['OrganizationalUnit'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRootOrganizationalUnitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRootOrganizationalUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRootOrganizationalUnitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRootOrganizationalUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(self, instance_id=None, user_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the account.
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
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserResponseBodyUserCustomFields(TeaModel):
    def __init__(self, field_name=None, field_value=None):
        # The identifier of the custom field.
        self.field_name = field_name  # type: str
        # The value of the custom field.
        self.field_value = field_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyUserCustomFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        return self


class GetUserResponseBodyUserGroups(TeaModel):
    def __init__(self, description=None, group_id=None, group_name=None):
        # The description of the organizational unit.
        self.description = description  # type: str
        # The ID of the organizational unit.
        self.group_id = group_id  # type: str
        # The name of the organizational unit.
        self.group_name = group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyUserGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetUserResponseBodyUserOrganizationalUnits(TeaModel):
    def __init__(self, organizational_unit_id=None, organizational_unit_name=None, primary=None):
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id  # type: str
        # The name of the organizational unit.
        self.organizational_unit_name = organizational_unit_name  # type: str
        # Indicates whether the organization is the primary organization.
        self.primary = primary  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyUserOrganizationalUnits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name
        if self.primary is not None:
            result['Primary'] = self.primary
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')
        if m.get('Primary') is not None:
            self.primary = m.get('Primary')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(self, account_expire_time=None, create_time=None, custom_fields=None, description=None,
                 display_name=None, email=None, email_verified=None, groups=None, instance_id=None, lock_expire_time=None,
                 organizational_units=None, password_expire_time=None, password_set=None, phone_number=None, phone_number_verified=None,
                 phone_region=None, primary_organizational_unit_id=None, register_time=None, status=None, update_time=None,
                 user_external_id=None, user_id=None, user_source_id=None, user_source_type=None, username=None):
        # The time when the account expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.account_expire_time = account_expire_time  # type: long
        # The time when the account was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The list of custom fields that describe the account.
        self.custom_fields = custom_fields  # type: list[GetUserResponseBodyUserCustomFields]
        # The description of the account.
        self.description = description  # type: str
        # The display name of the account.
        self.display_name = display_name  # type: str
        # The email address of the user who owns the account.
        self.email = email  # type: str
        # Indicates whether the email address has been verified. A value of true indicates that the email address has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the email address has not been verified.
        self.email_verified = email_verified  # type: bool
        # The organizational units to which the account belongs.
        self.groups = groups  # type: list[GetUserResponseBodyUserGroups]
        # The ID of the instance
        self.instance_id = instance_id  # type: str
        # The time when the account lock expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.lock_expire_time = lock_expire_time  # type: long
        # The organizational units to which the account belongs.
        self.organizational_units = organizational_units  # type: list[GetUserResponseBodyUserOrganizationalUnits]
        # The time when the password of the account expires. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # *   If the value -1 is returned, the password does not expire.
        # *   If no value is returned, the password does not expire.
        # *   If a UNIX timestamp is returned, the password expires at the indicated point of time.
        self.password_expire_time = password_expire_time  # type: long
        # Indicates whether a password is set.
        self.password_set = password_set  # type: bool
        # The mobile number of the user who owns the account.
        self.phone_number = phone_number  # type: str
        # Indicates whether the mobile number has been verified. A value of true indicates that the mobile number has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the mobile number has not been verified.
        self.phone_number_verified = phone_number_verified  # type: bool
        # The country code of the mobile number. For example, the country code of China is 86 without 00 or +.
        self.phone_region = phone_region  # type: str
        # The ID of the primary organizational unit to which the account belongs.
        self.primary_organizational_unit_id = primary_organizational_unit_id  # type: str
        # The time when the account was registered. This value is a UNIX timestamp. Unit: milliseconds.
        self.register_time = register_time  # type: long
        # The status of the account. Valid values:
        # 
        # *   enabled: The account is enabled.
        # *   disabled: The account is disabled.
        self.status = status  # type: str
        # The time when the account was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time  # type: long
        # The external ID of the account. The external ID can be used by external data to map the data of the account in IDaaS EIAM. By default, the external ID is the account ID.
        # 
        # For accounts with the same source type and source ID, each account has a unique external ID.
        self.user_external_id = user_external_id  # type: str
        # The ID of the account.
        self.user_id = user_id  # type: str
        # The source ID of the account.
        # 
        # If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk.
        self.user_source_id = user_source_id  # type: str
        # The source type of the account. Valid values:
        # 
        # *   build_in: The account was created in IDaaS.
        # *   ding_talk: The account was imported from DingTalk.
        # *   ad: The account was imported from Microsoft Active Directory (AD).
        # *   ldap: The account was imported from a Lightweight Directory Access Protocol (LDAP) service.
        self.user_source_type = user_source_type  # type: str
        # The username of the account.
        self.username = username  # type: str

    def validate(self):
        if self.custom_fields:
            for k in self.custom_fields:
                if k:
                    k.validate()
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()
        if self.organizational_units:
            for k in self.organizational_units:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserResponseBodyUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_expire_time is not None:
            result['AccountExpireTime'] = self.account_expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CustomFields'] = []
        if self.custom_fields is not None:
            for k in self.custom_fields:
                result['CustomFields'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verified is not None:
            result['EmailVerified'] = self.email_verified
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lock_expire_time is not None:
            result['LockExpireTime'] = self.lock_expire_time
        result['OrganizationalUnits'] = []
        if self.organizational_units is not None:
            for k in self.organizational_units:
                result['OrganizationalUnits'].append(k.to_map() if k else None)
        if self.password_expire_time is not None:
            result['PasswordExpireTime'] = self.password_expire_time
        if self.password_set is not None:
            result['PasswordSet'] = self.password_set
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_number_verified is not None:
            result['PhoneNumberVerified'] = self.phone_number_verified
        if self.phone_region is not None:
            result['PhoneRegion'] = self.phone_region
        if self.primary_organizational_unit_id is not None:
            result['PrimaryOrganizationalUnitId'] = self.primary_organizational_unit_id
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_external_id is not None:
            result['UserExternalId'] = self.user_external_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source_id is not None:
            result['UserSourceId'] = self.user_source_id
        if self.user_source_type is not None:
            result['UserSourceType'] = self.user_source_type
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountExpireTime') is not None:
            self.account_expire_time = m.get('AccountExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.custom_fields = []
        if m.get('CustomFields') is not None:
            for k in m.get('CustomFields'):
                temp_model = GetUserResponseBodyUserCustomFields()
                self.custom_fields.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerified') is not None:
            self.email_verified = m.get('EmailVerified')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = GetUserResponseBodyUserGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LockExpireTime') is not None:
            self.lock_expire_time = m.get('LockExpireTime')
        self.organizational_units = []
        if m.get('OrganizationalUnits') is not None:
            for k in m.get('OrganizationalUnits'):
                temp_model = GetUserResponseBodyUserOrganizationalUnits()
                self.organizational_units.append(temp_model.from_map(k))
        if m.get('PasswordExpireTime') is not None:
            self.password_expire_time = m.get('PasswordExpireTime')
        if m.get('PasswordSet') is not None:
            self.password_set = m.get('PasswordSet')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneNumberVerified') is not None:
            self.phone_number_verified = m.get('PhoneNumberVerified')
        if m.get('PhoneRegion') is not None:
            self.phone_region = m.get('PhoneRegion')
        if m.get('PrimaryOrganizationalUnitId') is not None:
            self.primary_organizational_unit_id = m.get('PrimaryOrganizationalUnitId')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserExternalId') is not None:
            self.user_external_id = m.get('UserExternalId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSourceId') is not None:
            self.user_source_id = m.get('UserSourceId')
        if m.get('UserSourceType') is not None:
            self.user_source_type = m.get('UserSourceType')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The data object of the account.
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


class ListApplicationClientSecretsRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None):
        # The ID of the application that you want to query.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationClientSecretsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListApplicationClientSecretsResponseBodyApplicationClientSecrets(TeaModel):
    def __init__(self, application_id=None, client_id=None, client_secret=None, instance_id=None,
                 last_used_time=None, secret_id=None, status=None):
        # The ID of the application that you want to query.
        self.application_id = application_id  # type: str
        # The client ID of the application.
        self.client_id = client_id  # type: str
        # The client key secret of the application. The value is not masked.
        self.client_secret = client_secret  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The time when the client key was last used. The value is a UNIX timestamp. Unit: milliseconds.
        self.last_used_time = last_used_time  # type: long
        # The client key ID of the application.
        self.secret_id = secret_id  # type: str
        # The status of the client key. Valid values:
        # 
        # *   Enabled: The client key is enabled.
        # *   Disabled: The client key is disabled.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationClientSecretsResponseBodyApplicationClientSecrets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationClientSecretsResponseBody(TeaModel):
    def __init__(self, application_client_secrets=None, request_id=None, total_count=None):
        # The information about the client keys.
        self.application_client_secrets = application_client_secrets  # type: list[ListApplicationClientSecretsResponseBodyApplicationClientSecrets]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.application_client_secrets:
            for k in self.application_client_secrets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationClientSecretsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationClientSecrets'] = []
        if self.application_client_secrets is not None:
            for k in self.application_client_secrets:
                result['ApplicationClientSecrets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application_client_secrets = []
        if m.get('ApplicationClientSecrets') is not None:
            for k in m.get('ApplicationClientSecrets'):
                temp_model = ListApplicationClientSecretsResponseBodyApplicationClientSecrets()
                self.application_client_secrets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationClientSecretsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationClientSecretsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationClientSecretsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListApplicationClientSecretsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(self, application_ids=None, application_name=None, authorization_type=None, instance_id=None,
                 page_number=None, page_size=None, status=None):
        # The IDs of the applications.
        self.application_ids = application_ids  # type: list[str]
        # The name of the application. Only fuzzy match from the leftmost character is supported.
        self.application_name = application_name  # type: str
        # The authorization of the application. Valid values:
        # 
        # *   authorize_required: Only the user with explicit authorization can access the application.
        # *   default_all: By default, all users can access the application.
        self.authorization_type = authorization_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: long
        # The status of the application. Valid values:
        # 
        # *   Enabled: The application is enabled.
        # *   Disabled: The application is disabled.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationsResponseBodyApplications(TeaModel):
    def __init__(self, application_id=None, application_name=None, application_source_type=None, client_id=None,
                 create_time=None, description=None, features=None, instance_id=None, logo_url=None, managed_service_code=None,
                 service_managed=None, sso_type=None, status=None, update_time=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The name of the application.
        self.application_name = application_name  # type: str
        # The origin of the application. Valid values:
        # 
        # *   urn:alibaba:idaas:app:source:template: The application is created based on a template.
        # *   urn:alibaba:idaas: The application is created based on the standard protocol.
        self.application_source_type = application_source_type  # type: str
        # The client ID of the application.
        self.client_id = client_id  # type: str
        # The time when the application was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The description of the application.
        self.description = description  # type: str
        # The features that are supported by the application. The value is a JSON array. Valid values:
        # 
        # *   sso: The application supports SSO.
        # *   provision: The application supports account synchronization.
        # *   api_invoke: The application supports custom APIs.
        self.features = features  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The URL of the application icon.
        self.logo_url = logo_url  # type: str
        # The service code of the cloud service that manages the application template.
        self.managed_service_code = managed_service_code  # type: str
        # Indicates whether the application template is managed by a cloud service.
        self.service_managed = service_managed  # type: bool
        # The type of the single sign-on (SSO) protocol. Valid values:
        # 
        # *   saml2: the Security Assertion Markup Language (SAML) 2.0 protocol.
        # *   oidc: the OpenID Connect (OIDC) protocol.
        self.sso_type = sso_type  # type: str
        # The status of the application. Valid values:
        # 
        # *   Enabled: The application is enabled.
        # *   Disabled: The application is disabled.
        self.status = status  # type: str
        # The time when the application was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsResponseBodyApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.application_source_type is not None:
            result['ApplicationSourceType'] = self.application_source_type
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.features is not None:
            result['Features'] = self.features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        if self.managed_service_code is not None:
            result['ManagedServiceCode'] = self.managed_service_code
        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed
        if self.sso_type is not None:
            result['SsoType'] = self.sso_type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ApplicationSourceType') is not None:
            self.application_source_type = m.get('ApplicationSourceType')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        if m.get('ManagedServiceCode') is not None:
            self.managed_service_code = m.get('ManagedServiceCode')
        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')
        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(self, applications=None, request_id=None, total_count=None):
        # The details of the applications.
        self.applications = applications  # type: list[ListApplicationsResponseBodyApplications]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of the returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListApplicationsForOrganizationalUnitRequest(TeaModel):
    def __init__(self, application_ids=None, instance_id=None, organizational_unit_id=None, page_number=None,
                 page_size=None):
        # The IDs of the applications that the EIAM organization can access. You can query a maximum of 100 application IDs at a time.
        self.application_ids = application_ids  # type: list[str]
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the EIAM organization.
        self.organizational_unit_id = organizational_unit_id  # type: str
        # The number of the page to return.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsForOrganizationalUnitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListApplicationsForOrganizationalUnitResponseBodyApplications(TeaModel):
    def __init__(self, application_id=None):
        # The ID of the application that the EIAM organization can access.
        self.application_id = application_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsForOrganizationalUnitResponseBodyApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class ListApplicationsForOrganizationalUnitResponseBody(TeaModel):
    def __init__(self, applications=None, request_id=None, total_count=None):
        # The applications that the EIAM organization can access.
        self.applications = applications  # type: list[ListApplicationsForOrganizationalUnitResponseBodyApplications]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of the returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsForOrganizationalUnitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsForOrganizationalUnitResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationsForOrganizationalUnitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationsForOrganizationalUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationsForOrganizationalUnitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListApplicationsForOrganizationalUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsForUserRequest(TeaModel):
    def __init__(self, application_ids=None, instance_id=None, page_number=None, page_size=None, query_mode=None,
                 user_id=None):
        # The IDs of the applications that the EIAM account can access. You can query a maximum of 100 application IDs at a time.
        self.application_ids = application_ids  # type: list[str]
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: long
        # The query mode. Default value: **OnlyDirect**. Valid values:
        # 
        # *   OnlyDirect: Only the direct permissions are queried. Direct permissions are the permissions that are directly granted to the account.
        # *   IncludeInherit: Both the permissions that are directly granted to the account and the inherited permissions are queried. Inherited permissions are the permissions that an account inherits from the parent organization or the group to which the account belongs.
        self.query_mode = query_mode  # type: str
        # The ID of the EIAM account.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsForUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListApplicationsForUserResponseBodyApplications(TeaModel):
    def __init__(self, application_id=None, has_direct_authorization=None, has_inherit_authorization=None):
        # The ID of the application that the EIAM account can access.
        self.application_id = application_id  # type: str
        # Indicates whether the EIAM account has direct permissions on the application. Valid values:
        # 
        # *   true: The EIAM account has direct permissions on the application.
        # *   false: The EIAM account does not have direct permissions on the application.
        self.has_direct_authorization = has_direct_authorization  # type: bool
        # Indicates whether the EIAM account has inherited permissions on the application. Valid values:
        # 
        # *   true: A parent organization or an organization to which the EIAM account belongs has direct permissions on the application.
        # *   false: A parent organization or an organization to which the EIAM account belongs does not have direct permissions on the application.
        self.has_inherit_authorization = has_inherit_authorization  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsForUserResponseBodyApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.has_direct_authorization is not None:
            result['HasDirectAuthorization'] = self.has_direct_authorization
        if self.has_inherit_authorization is not None:
            result['HasInheritAuthorization'] = self.has_inherit_authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('HasDirectAuthorization') is not None:
            self.has_direct_authorization = m.get('HasDirectAuthorization')
        if m.get('HasInheritAuthorization') is not None:
            self.has_inherit_authorization = m.get('HasInheritAuthorization')
        return self


class ListApplicationsForUserResponseBody(TeaModel):
    def __init__(self, applications=None, request_id=None, total_count=None):
        # The applications that the EIAM account can access.
        self.applications = applications  # type: list[ListApplicationsForUserResponseBodyApplications]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of the returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsForUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsForUserResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationsForUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationsForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationsForUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListApplicationsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainProxyTokensRequest(TeaModel):
    def __init__(self, domain_id=None, instance_id=None):
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainProxyTokensRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListDomainProxyTokensResponseBodyDomainProxyTokens(TeaModel):
    def __init__(self, create_time=None, domain_id=None, domain_proxy_token=None, domain_proxy_token_id=None,
                 instance_id=None, last_used_time=None, status=None, update_time=None):
        # 域名代理Token创建时间，Unix时间戳格式，单位为毫秒。
        self.create_time = create_time  # type: long
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # 域名代理Token。
        self.domain_proxy_token = domain_proxy_token  # type: str
        # 域名代理Token ID。
        self.domain_proxy_token_id = domain_proxy_token_id  # type: str
        # 实例ID。
        self.instance_id = instance_id  # type: str
        # 域名代理Token最近使用时间，Unix时间戳格式，单位为毫秒。
        self.last_used_time = last_used_time  # type: long
        # token状态，枚举类型：(enabled）启用,（disabled）禁用。
        self.status = status  # type: str
        # 域名代理Token最近更新时间，Unix时间戳格式，单位为毫秒。
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainProxyTokensResponseBodyDomainProxyTokens, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_proxy_token is not None:
            result['DomainProxyToken'] = self.domain_proxy_token
        if self.domain_proxy_token_id is not None:
            result['DomainProxyTokenId'] = self.domain_proxy_token_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainProxyToken') is not None:
            self.domain_proxy_token = m.get('DomainProxyToken')
        if m.get('DomainProxyTokenId') is not None:
            self.domain_proxy_token_id = m.get('DomainProxyTokenId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDomainProxyTokensResponseBody(TeaModel):
    def __init__(self, domain_proxy_tokens=None, request_id=None):
        self.domain_proxy_tokens = domain_proxy_tokens  # type: list[ListDomainProxyTokensResponseBodyDomainProxyTokens]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_proxy_tokens:
            for k in self.domain_proxy_tokens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDomainProxyTokensResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainProxyTokens'] = []
        if self.domain_proxy_tokens is not None:
            for k in self.domain_proxy_tokens:
                result['DomainProxyTokens'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_proxy_tokens = []
        if m.get('DomainProxyTokens') is not None:
            for k in m.get('DomainProxyTokens'):
                temp_model = ListDomainProxyTokensResponseBodyDomainProxyTokens()
                self.domain_proxy_tokens.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDomainProxyTokensResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDomainProxyTokensResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDomainProxyTokensResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDomainProxyTokensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(self, instance_id=None):
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListDomainsResponseBodyDomainsFiling(TeaModel):
    def __init__(self, icp_number=None):
        # 域名关联的备案号, 长度最大限制64。
        self.icp_number = icp_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainsResponseBodyDomainsFiling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icp_number is not None:
            result['IcpNumber'] = self.icp_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IcpNumber') is not None:
            self.icp_number = m.get('IcpNumber')
        return self


class ListDomainsResponseBodyDomains(TeaModel):
    def __init__(self, create_time=None, default_domain=None, domain=None, domain_id=None, domain_type=None,
                 filing=None, instance_id=None, lock_mode=None, update_time=None):
        # 域名创建时间，Unix时间戳格式，单位为毫秒。
        self.create_time = create_time  # type: long
        # 是否默认域名。true表示实例默认域名，false表示非默认域名
        self.default_domain = default_domain  # type: bool
        # 域名。
        self.domain = domain  # type: str
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # 域名类型。枚举取值:system_init(系统初始化)、user_custom(用户自定义)。
        self.domain_type = domain_type  # type: str
        # 域名备案信息。
        self.filing = filing  # type: ListDomainsResponseBodyDomainsFiling
        # 实例ID。
        self.instance_id = instance_id  # type: str
        # 域名锁定状态。枚举取值:unlock(正常)、lockByLicense(因License限制不可用)。
        self.lock_mode = lock_mode  # type: str
        # 域名最近更新时间，Unix时间戳格式，单位为毫秒。
        self.update_time = update_time  # type: long

    def validate(self):
        if self.filing:
            self.filing.validate()

    def to_map(self):
        _map = super(ListDomainsResponseBodyDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.filing is not None:
            result['Filing'] = self.filing.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('Filing') is not None:
            temp_model = ListDomainsResponseBodyDomainsFiling()
            self.filing = temp_model.from_map(m['Filing'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, request_id=None):
        self.domains = domains  # type: list[ListDomainsResponseBodyDomains]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = ListDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDomainsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEiamInstancesRequest(TeaModel):
    def __init__(self, instance_ids=None, instance_region_id=None):
        # 实例ID列表，支持0到100个
        self.instance_ids = instance_ids  # type: list[str]
        # 实例所属Region
        self.instance_region_id = instance_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEiamInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        return self


class ListEiamInstancesResponseBodyInstances(TeaModel):
    def __init__(self, description=None, developer_apiprivate_domain=None, developer_apipublic_domain=None,
                 instance_id=None, instance_status=None, instance_version=None, open_apiprivate_domain=None,
                 open_apipublic_domain=None, ssodomain=None, start_time=None):
        # 实例描述信息
        self.description = description  # type: str
        # 实例developer私网域名地址
        self.developer_apiprivate_domain = developer_apiprivate_domain  # type: str
        # 实例developer公网域名地址
        self.developer_apipublic_domain = developer_apipublic_domain  # type: str
        # 实例id
        self.instance_id = instance_id  # type: str
        # 实例状态，Pending(初始状态)、Creating(创建中)、Running(运行中)、Disabled(禁用)、CreateFailed(创建失败)
        self.instance_status = instance_status  # type: str
        # 实例版本，EIAM2.0/ EIAM1.0
        self.instance_version = instance_version  # type: str
        # 实例openApi私网域名地址
        self.open_apiprivate_domain = open_apiprivate_domain  # type: str
        # 实例openApi公网域名地址
        self.open_apipublic_domain = open_apipublic_domain  # type: str
        # 实例域名地址
        self.ssodomain = ssodomain  # type: str
        # 实例的创建时间
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEiamInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.developer_apiprivate_domain is not None:
            result['DeveloperAPIPrivateDomain'] = self.developer_apiprivate_domain
        if self.developer_apipublic_domain is not None:
            result['DeveloperAPIPublicDomain'] = self.developer_apipublic_domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_version is not None:
            result['InstanceVersion'] = self.instance_version
        if self.open_apiprivate_domain is not None:
            result['OpenAPIPrivateDomain'] = self.open_apiprivate_domain
        if self.open_apipublic_domain is not None:
            result['OpenAPIPublicDomain'] = self.open_apipublic_domain
        if self.ssodomain is not None:
            result['SSODomain'] = self.ssodomain
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeveloperAPIPrivateDomain') is not None:
            self.developer_apiprivate_domain = m.get('DeveloperAPIPrivateDomain')
        if m.get('DeveloperAPIPublicDomain') is not None:
            self.developer_apipublic_domain = m.get('DeveloperAPIPublicDomain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceVersion') is not None:
            self.instance_version = m.get('InstanceVersion')
        if m.get('OpenAPIPrivateDomain') is not None:
            self.open_apiprivate_domain = m.get('OpenAPIPrivateDomain')
        if m.get('OpenAPIPublicDomain') is not None:
            self.open_apipublic_domain = m.get('OpenAPIPublicDomain')
        if m.get('SSODomain') is not None:
            self.ssodomain = m.get('SSODomain')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListEiamInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None):
        self.instances = instances  # type: list[ListEiamInstancesResponseBodyInstances]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEiamInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListEiamInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEiamInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEiamInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEiamInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEiamInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEiamRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        # 地域名称
        self.local_name = local_name  # type: str
        # 地域ID
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEiamRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEiamRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: list[ListEiamRegionsResponseBodyRegions]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEiamRegionsResponseBody, self).to_map()
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
                temp_model = ListEiamRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEiamRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEiamRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEiamRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEiamRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(self, group_external_id=None, group_ids=None, group_name=None, group_name_starts_with=None,
                 instance_id=None, page_number=None, page_size=None):
        # The external ID of the group.
        self.group_external_id = group_external_id  # type: str
        # The group IDs.
        self.group_ids = group_ids  # type: list[str]
        # The name of the group. If you specify this parameter, the query is based on an exact match.
        self.group_name = group_name  # type: str
        # The prefix of the group name. If you specify this parameter, the query follows the leftmost matching principle.
        self.group_name_starts_with = group_name_starts_with  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_external_id is not None:
            result['GroupExternalId'] = self.group_external_id
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_name_starts_with is not None:
            result['GroupNameStartsWith'] = self.group_name_starts_with
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupExternalId') is not None:
            self.group_external_id = m.get('GroupExternalId')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupNameStartsWith') is not None:
            self.group_name_starts_with = m.get('GroupNameStartsWith')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGroupsResponseBodyGroups(TeaModel):
    def __init__(self, create_time=None, description=None, group_external_id=None, group_id=None, group_name=None,
                 group_source_id=None, group_source_type=None, instance_id=None, update_time=None):
        # The time at which the group was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time  # type: long
        # The description of the group.
        self.description = description  # type: str
        # The external ID of the group, which can be used to associate the group with an external system. By default, the external ID is the group ID.
        self.group_external_id = group_external_id  # type: str
        # The group ID.
        self.group_id = group_id  # type: str
        # The name of the group.
        self.group_name = group_name  # type: str
        # The source ID of the group. If the group was imported from other services, this value indicates the external source ID. By default, the source ID is the instance ID.
        self.group_source_id = group_source_id  # type: str
        # The source type of the group. Only build_in may be returned, which indicates that the group was created in IDaaS.
        # 
        # *\
        self.group_source_type = group_source_type  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The time at which the group was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_external_id is not None:
            result['GroupExternalId'] = self.group_external_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_source_id is not None:
            result['GroupSourceId'] = self.group_source_id
        if self.group_source_type is not None:
            result['GroupSourceType'] = self.group_source_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupExternalId') is not None:
            self.group_external_id = m.get('GroupExternalId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupSourceId') is not None:
            self.group_source_id = m.get('GroupSourceId')
        if m.get('GroupSourceType') is not None:
            self.group_source_type = m.get('GroupSourceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(self, groups=None, request_id=None, total_count=None):
        # The queried account groups.
        self.groups = groups  # type: list[ListGroupsResponseBodyGroups]
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned. The maximum number of entries returned at a time depends on the value of PageSize.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = ListGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListGroupsForApplicationRequest(TeaModel):
    def __init__(self, application_id=None, group_ids=None, instance_id=None, page_number=None, page_size=None):
        # The application ID.
        self.application_id = application_id  # type: str
        # The group IDs. You can specify up to 100 group IDs at a time.
        self.group_ids = group_ids  # type: list[str]
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The page number.
        self.page_number = page_number  # type: long
        # The number of entries per page.
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsForApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGroupsForApplicationResponseBodyGroups(TeaModel):
    def __init__(self, group_id=None):
        # The group ID.
        self.group_id = group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsForApplicationResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class ListGroupsForApplicationResponseBody(TeaModel):
    def __init__(self, groups=None, request_id=None, total_count=None):
        # The group IDs.
        self.groups = groups  # type: list[ListGroupsForApplicationResponseBodyGroups]
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupsForApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = ListGroupsForApplicationResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGroupsForApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupsForApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupsForApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGroupsForApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsForUserRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, user_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The number of the page to return.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: long
        # The account ID.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsForUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListGroupsForUserResponseBodyGroups(TeaModel):
    def __init__(self, group_id=None):
        # The group ID.
        self.group_id = group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupsForUserResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class ListGroupsForUserResponseBody(TeaModel):
    def __init__(self, groups=None, request_id=None, total_count=None):
        # The queried account groups.
        self.groups = groups  # type: list[ListGroupsForUserResponseBodyGroups]
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned. The maximum number of entries returned at a time depends on the value of PageSize.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupsForUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = ListGroupsForUserResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListInstancesRequest(TeaModel):
    def __init__(self, instance_ids=None, page_number=None, page_size=None, status=None):
        # The list of instance IDs.
        self.instance_ids = instance_ids  # type: list[str]
        # The number of the page to return.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: long
        # The status of the instance. Valid values:
        # 
        # *   creating
        # *   running
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstancesDefaultEndpoint(TeaModel):
    def __init__(self, endpoint=None, status=None):
        # The endpoint of the instance.
        self.endpoint = endpoint  # type: str
        # The status of the endpoint. Valid values:
        # 
        # *   resolved
        # *   unresolved
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesDefaultEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(self, create_time=None, default_endpoint=None, description=None, instance_id=None, status=None):
        # The time when the instance was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time  # type: long
        # The default endpoint of the instance.
        self.default_endpoint = default_endpoint  # type: ListInstancesResponseBodyInstancesDefaultEndpoint
        # The description of the instance.
        self.description = description  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The status of the instance. Valid values:
        # 
        # *   creating
        # *   running
        self.status = status  # type: str

    def validate(self):
        if self.default_endpoint:
            self.default_endpoint.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultEndpoint') is not None:
            temp_model = ListInstancesResponseBodyInstancesDefaultEndpoint()
            self.default_endpoint = temp_model.from_map(m['DefaultEndpoint'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None, total_count=None):
        # The information of instances.
        self.instances = instances  # type: list[ListInstancesResponseBodyInstances]
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBody, self).to_map()
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
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworkAccessEndpointAvailableRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        # 地域名称。
        self.local_name = local_name  # type: str
        # 地域ID。
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkAccessEndpointAvailableRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListNetworkAccessEndpointAvailableRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: list[ListNetworkAccessEndpointAvailableRegionsResponseBodyRegions]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNetworkAccessEndpointAvailableRegionsResponseBody, self).to_map()
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
                temp_model = ListNetworkAccessEndpointAvailableRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNetworkAccessEndpointAvailableRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNetworkAccessEndpointAvailableRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNetworkAccessEndpointAvailableRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNetworkAccessEndpointAvailableRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworkAccessEndpointAvailableZonesRequest(TeaModel):
    def __init__(self, nae_region_id=None):
        # 专属网络端点支持的地域
        self.nae_region_id = nae_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkAccessEndpointAvailableZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nae_region_id is not None:
            result['NaeRegionId'] = self.nae_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NaeRegionId') is not None:
            self.nae_region_id = m.get('NaeRegionId')
        return self


class ListNetworkAccessEndpointAvailableZonesResponseBodyZones(TeaModel):
    def __init__(self, local_name=None, zone_id=None):
        # 可用区名称。
        self.local_name = local_name  # type: str
        # 可用区ID。
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkAccessEndpointAvailableZonesResponseBodyZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListNetworkAccessEndpointAvailableZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, zones=None):
        self.request_id = request_id  # type: str
        self.zones = zones  # type: list[ListNetworkAccessEndpointAvailableZonesResponseBodyZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNetworkAccessEndpointAvailableZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = ListNetworkAccessEndpointAvailableZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class ListNetworkAccessEndpointAvailableZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNetworkAccessEndpointAvailableZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNetworkAccessEndpointAvailableZonesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNetworkAccessEndpointAvailableZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworkAccessEndpointsRequest(TeaModel):
    def __init__(self, instance_id=None, max_results=None, network_access_endpoint_status=None,
                 network_access_endpoint_type=None, next_token=None, vpc_id=None, vpc_region_id=None):
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str
        # 分页查询时每页行数。默认值为20，最大值为100。
        self.max_results = max_results  # type: long
        # 专属网络端点连接的状态。NetworkAccessEndpointType取值为shared时不生效。
        self.network_access_endpoint_status = network_access_endpoint_status  # type: str
        # 专属网络端点连接的类型。取值可选范围：1. private - 专属网络端点；2. shared - 共享网络端点
        self.network_access_endpoint_type = network_access_endpoint_type  # type: str
        # 查询凭证（Token），取值为上一次API调用返回的NextToken参数值。
        self.next_token = next_token  # type: str
        # 专属网络端点连接的Vpc ID。NetworkAccessEndpointType取值为shared时不生效。
        self.vpc_id = vpc_id  # type: str
        # 专属网络端点连接的Vpc所属地域，该地域取值必须在ListNetworkAccessEndpointAvailableRegions接口中返回。NetworkAccessEndpointType取值为shared时不生效。
        self.vpc_region_id = vpc_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkAccessEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.network_access_endpoint_status is not None:
            result['NetworkAccessEndpointStatus'] = self.network_access_endpoint_status
        if self.network_access_endpoint_type is not None:
            result['NetworkAccessEndpointType'] = self.network_access_endpoint_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NetworkAccessEndpointStatus') is not None:
            self.network_access_endpoint_status = m.get('NetworkAccessEndpointStatus')
        if m.get('NetworkAccessEndpointType') is not None:
            self.network_access_endpoint_type = m.get('NetworkAccessEndpointType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        return self


class ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpoints(TeaModel):
    def __init__(self, create_time=None, instance_id=None, network_access_endpoint_id=None,
                 network_access_endpoint_name=None, network_access_endpoint_type=None, security_group_id=None, status=None, update_time=None,
                 v_switch_ids=None, vpc_id=None, vpc_region_id=None):
        # 专属网络端点创建时间，Unix时间戳格式，单位为毫秒。
        self.create_time = create_time  # type: long
        # 实例ID。
        self.instance_id = instance_id  # type: str
        # 专属网络端点ID。
        self.network_access_endpoint_id = network_access_endpoint_id  # type: str
        # 专属网络端点名称。
        self.network_access_endpoint_name = network_access_endpoint_name  # type: str
        # 专属网络端点连接的类型。
        self.network_access_endpoint_type = network_access_endpoint_type  # type: str
        # 专属网络端点使用的安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 专属网络端点状态。
        self.status = status  # type: str
        # 专属网络端点最近更新时间，Unix时间戳格式，单位为毫秒。
        self.update_time = update_time  # type: long
        # 专属网络端点连接的指定vSwitch列表。
        self.v_switch_ids = v_switch_ids  # type: list[str]
        # 专属网络端点连接的VpcID。
        self.vpc_id = vpc_id  # type: str
        # 专属网络端点连接的Vpc所属地域。
        self.vpc_region_id = vpc_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id
        if self.network_access_endpoint_name is not None:
            result['NetworkAccessEndpointName'] = self.network_access_endpoint_name
        if self.network_access_endpoint_type is not None:
            result['NetworkAccessEndpointType'] = self.network_access_endpoint_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')
        if m.get('NetworkAccessEndpointName') is not None:
            self.network_access_endpoint_name = m.get('NetworkAccessEndpointName')
        if m.get('NetworkAccessEndpointType') is not None:
            self.network_access_endpoint_type = m.get('NetworkAccessEndpointType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        return self


class ListNetworkAccessEndpointsResponseBody(TeaModel):
    def __init__(self, network_access_endpoints=None, next_token=None, request_id=None, total_count=None):
        self.network_access_endpoints = network_access_endpoints  # type: list[ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpoints]
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.network_access_endpoints:
            for k in self.network_access_endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNetworkAccessEndpointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetworkAccessEndpoints'] = []
        if self.network_access_endpoints is not None:
            for k in self.network_access_endpoints:
                result['NetworkAccessEndpoints'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.network_access_endpoints = []
        if m.get('NetworkAccessEndpoints') is not None:
            for k in m.get('NetworkAccessEndpoints'):
                temp_model = ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpoints()
                self.network_access_endpoints.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNetworkAccessEndpointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNetworkAccessEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNetworkAccessEndpointsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNetworkAccessEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworkAccessPathsRequest(TeaModel):
    def __init__(self, instance_id=None, network_access_endpoint_id=None):
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str
        # 专属网络端点ID。
        self.network_access_endpoint_id = network_access_endpoint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkAccessPathsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')
        return self


class ListNetworkAccessPathsResponseBodyNetworkAccessPaths(TeaModel):
    def __init__(self, create_time=None, instance_id=None, network_access_endpoint_id=None,
                 network_access_path_id=None, network_interface_id=None, private_ip_address=None, status=None, update_time=None,
                 v_switch_id=None):
        # 专属网络端点访问路径创建时间，Unix时间戳格式，单位为毫秒。
        self.create_time = create_time  # type: long
        # 实例ID。
        self.instance_id = instance_id  # type: str
        # 专属网络端点ID。
        self.network_access_endpoint_id = network_access_endpoint_id  # type: str
        # 专属网络端点访问路径ID。
        self.network_access_path_id = network_access_path_id  # type: str
        # 专属网络端点访问路径使用的ENI ID。
        self.network_interface_id = network_interface_id  # type: str
        # 专属网络端点访问路径使用的ENI私网地址。
        self.private_ip_address = private_ip_address  # type: str
        # 专属网络端点访问路径状态。
        self.status = status  # type: str
        # 专属网络端点访问路径最近更新时间，Unix时间戳格式，单位为毫秒。
        self.update_time = update_time  # type: long
        # 专属网络端点访问路径的ENI归属的交换机ID。
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkAccessPathsResponseBodyNetworkAccessPaths, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id
        if self.network_access_path_id is not None:
            result['NetworkAccessPathId'] = self.network_access_path_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')
        if m.get('NetworkAccessPathId') is not None:
            self.network_access_path_id = m.get('NetworkAccessPathId')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class ListNetworkAccessPathsResponseBody(TeaModel):
    def __init__(self, network_access_paths=None, request_id=None):
        self.network_access_paths = network_access_paths  # type: list[ListNetworkAccessPathsResponseBodyNetworkAccessPaths]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.network_access_paths:
            for k in self.network_access_paths:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNetworkAccessPathsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetworkAccessPaths'] = []
        if self.network_access_paths is not None:
            for k in self.network_access_paths:
                result['NetworkAccessPaths'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.network_access_paths = []
        if m.get('NetworkAccessPaths') is not None:
            for k in m.get('NetworkAccessPaths'):
                temp_model = ListNetworkAccessPathsResponseBodyNetworkAccessPaths()
                self.network_access_paths.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNetworkAccessPathsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNetworkAccessPathsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNetworkAccessPathsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNetworkAccessPathsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationalUnitParentsRequest(TeaModel):
    def __init__(self, instance_id=None, organizational_unit_id=None):
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str
        # 组织ID。
        self.organizational_unit_id = organizational_unit_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationalUnitParentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        return self


class ListOrganizationalUnitParentsResponseBodyParents(TeaModel):
    def __init__(self, organizational_unit_id=None, parent_id=None):
        # 组织ID
        self.organizational_unit_id = organizational_unit_id  # type: str
        # 父组织ID
        self.parent_id = parent_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationalUnitParentsResponseBodyParents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class ListOrganizationalUnitParentsResponseBody(TeaModel):
    def __init__(self, parents=None, request_id=None):
        self.parents = parents  # type: list[ListOrganizationalUnitParentsResponseBodyParents]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.parents:
            for k in self.parents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOrganizationalUnitParentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parents'] = []
        if self.parents is not None:
            for k in self.parents:
                result['Parents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parents = []
        if m.get('Parents') is not None:
            for k in m.get('Parents'):
                temp_model = ListOrganizationalUnitParentsResponseBodyParents()
                self.parents.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOrganizationalUnitParentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOrganizationalUnitParentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOrganizationalUnitParentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOrganizationalUnitParentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationalUnitsRequest(TeaModel):
    def __init__(self, instance_id=None, organizational_unit_ids=None, organizational_unit_name=None,
                 organizational_unit_name_starts_with=None, page_number=None, page_size=None, parent_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # 组织ID列表。size限制最大100。
        self.organizational_unit_ids = organizational_unit_ids  # type: list[str]
        # The name of the organizational unit.
        self.organizational_unit_name = organizational_unit_name  # type: str
        # 组织名称，左匹配
        self.organizational_unit_name_starts_with = organizational_unit_name_starts_with  # type: str
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size  # type: long
        # The ID of the parent organizational unit.
        self.parent_id = parent_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationalUnitsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids
        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name
        if self.organizational_unit_name_starts_with is not None:
            result['OrganizationalUnitNameStartsWith'] = self.organizational_unit_name_starts_with
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')
        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')
        if m.get('OrganizationalUnitNameStartsWith') is not None:
            self.organizational_unit_name_starts_with = m.get('OrganizationalUnitNameStartsWith')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class ListOrganizationalUnitsResponseBodyOrganizationalUnits(TeaModel):
    def __init__(self, create_time=None, description=None, instance_id=None, leaf=None,
                 organizational_unit_external_id=None, organizational_unit_id=None, organizational_unit_name=None,
                 organizational_unit_source_id=None, organizational_unit_source_type=None, parent_id=None, update_time=None):
        # The time when the organizational unit was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The description of the organizational unit.
        self.description = description  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether the node is a leaf node.
        self.leaf = leaf  # type: bool
        # The external ID of the organizational unit. The external ID can be used by external data to map the data of the organizational unit in IDaaS EIAM. By default, the external ID is the organizational unit ID.
        # 
        # For organizational units with the same source type and source ID, each organizational unit has a unique external ID.
        self.organizational_unit_external_id = organizational_unit_external_id  # type: str
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id  # type: str
        # 组织名称。
        self.organizational_unit_name = organizational_unit_name  # type: str
        # The source ID of the organizational unit.
        self.organizational_unit_source_id = organizational_unit_source_id  # type: str
        # The source type of the organizational unit. Valid values:
        # 
        # *   build_in: The organizational unit was created in IDaaS.
        # *   ding_talk: The organizational unit was imported from DingTalk.
        # *   ad: The organizational unit was imported from Microsoft Active Directory (AD).
        # *   ldap: The organizational unit was imported from a Lightweight Directory Access Protocol (LDAP) service.
        self.organizational_unit_source_type = organizational_unit_source_type  # type: str
        # The ID of the parent organizational unit.
        self.parent_id = parent_id  # type: str
        # The time when the organizational unit was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationalUnitsResponseBodyOrganizationalUnits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.leaf is not None:
            result['Leaf'] = self.leaf
        if self.organizational_unit_external_id is not None:
            result['OrganizationalUnitExternalId'] = self.organizational_unit_external_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name
        if self.organizational_unit_source_id is not None:
            result['OrganizationalUnitSourceId'] = self.organizational_unit_source_id
        if self.organizational_unit_source_type is not None:
            result['OrganizationalUnitSourceType'] = self.organizational_unit_source_type
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Leaf') is not None:
            self.leaf = m.get('Leaf')
        if m.get('OrganizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('OrganizationalUnitExternalId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')
        if m.get('OrganizationalUnitSourceId') is not None:
            self.organizational_unit_source_id = m.get('OrganizationalUnitSourceId')
        if m.get('OrganizationalUnitSourceType') is not None:
            self.organizational_unit_source_type = m.get('OrganizationalUnitSourceType')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListOrganizationalUnitsResponseBody(TeaModel):
    def __init__(self, organizational_units=None, request_id=None, total_count=None):
        # The list of data objects of organizational units.
        self.organizational_units = organizational_units  # type: list[ListOrganizationalUnitsResponseBodyOrganizationalUnits]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of entries in the list.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.organizational_units:
            for k in self.organizational_units:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOrganizationalUnitsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrganizationalUnits'] = []
        if self.organizational_units is not None:
            for k in self.organizational_units:
                result['OrganizationalUnits'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.organizational_units = []
        if m.get('OrganizationalUnits') is not None:
            for k in m.get('OrganizationalUnits'):
                temp_model = ListOrganizationalUnitsResponseBodyOrganizationalUnits()
                self.organizational_units.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOrganizationalUnitsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOrganizationalUnitsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOrganizationalUnitsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOrganizationalUnitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationalUnitsForApplicationRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, organizational_unit_ids=None, page_number=None,
                 page_size=None):
        # The ID of the application that you want to query.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The IDs of the organizations that are allowed to access the application. You can query a maximum of 100 organization IDs at a time.
        self.organizational_unit_ids = organizational_unit_ids  # type: list[str]
        # The number of the page to return.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationalUnitsForApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOrganizationalUnitsForApplicationResponseBodyOrganizationalUnits(TeaModel):
    def __init__(self, organizational_unit_id=None):
        # The ID of the organization that is allowed to access the application.
        self.organizational_unit_id = organizational_unit_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationalUnitsForApplicationResponseBodyOrganizationalUnits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        return self


class ListOrganizationalUnitsForApplicationResponseBody(TeaModel):
    def __init__(self, organizational_units=None, request_id=None, total_count=None):
        # The IDs of the organizations that are allowed to access the application.
        self.organizational_units = organizational_units  # type: list[ListOrganizationalUnitsForApplicationResponseBodyOrganizationalUnits]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of the returned entries.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.organizational_units:
            for k in self.organizational_units:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOrganizationalUnitsForApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrganizationalUnits'] = []
        if self.organizational_units is not None:
            for k in self.organizational_units:
                result['OrganizationalUnits'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.organizational_units = []
        if m.get('OrganizationalUnits') is not None:
            for k in m.get('OrganizationalUnits'):
                temp_model = ListOrganizationalUnitsForApplicationResponseBodyOrganizationalUnits()
                self.organizational_units.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOrganizationalUnitsForApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOrganizationalUnitsForApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOrganizationalUnitsForApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOrganizationalUnitsForApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The endpoint of the region.
        self.region_endpoint = region_endpoint  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsResponseBodyRegions, self).to_map()
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


class ListRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # The supported regions.
        self.regions = regions  # type: list[ListRegionsResponseBodyRegions]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
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
                temp_model = ListRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, display_name_starts_with=None, email=None, instance_id=None, organizational_unit_id=None,
                 page_number=None, page_size=None, phone_number=None, phone_region=None, status=None, user_external_id=None,
                 user_ids=None, user_source_id=None, user_source_type=None, username_starts_with=None):
        # 账户展示名，模糊匹配
        self.display_name_starts_with = display_name_starts_with  # type: str
        # The email address of the user who owns the account.
        self.email = email  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id  # type: str
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size  # type: long
        # The mobile number of the user who owns the account.
        self.phone_number = phone_number  # type: str
        # The country code of the mobile number. For example, the country code of China is 86 without 00 or +.
        self.phone_region = phone_region  # type: str
        # The status of the account. Valid values:
        # 
        # *   enabled: The account is enabled.
        # *   disabled: The account is disabled.
        self.status = status  # type: str
        # The external ID of the account. The external ID can be used by external data to map the data of the account in IDaaS EIAM.
        # 
        # For accounts with the same source type and source ID, each account has a unique external ID.
        self.user_external_id = user_external_id  # type: str
        # 账户的ID集合
        self.user_ids = user_ids  # type: list[str]
        # The source ID of the account.
        # 
        # If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk.
        self.user_source_id = user_source_id  # type: str
        # The source type of the account. Valid values:
        # 
        # *   build_in: The account was created in IDaaS.
        # *   ding_talk: The account was imported from DingTalk.
        # *   ad: The account was imported from Microsoft Active Directory (AD).
        # *   ldap: The account was imported from a Lightweight Directory Access Protocol (LDAP) service.
        self.user_source_type = user_source_type  # type: str
        # 账户名，左模糊匹配
        self.username_starts_with = username_starts_with  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name_starts_with is not None:
            result['DisplayNameStartsWith'] = self.display_name_starts_with
        if self.email is not None:
            result['Email'] = self.email
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_region is not None:
            result['PhoneRegion'] = self.phone_region
        if self.status is not None:
            result['Status'] = self.status
        if self.user_external_id is not None:
            result['UserExternalId'] = self.user_external_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        if self.user_source_id is not None:
            result['UserSourceId'] = self.user_source_id
        if self.user_source_type is not None:
            result['UserSourceType'] = self.user_source_type
        if self.username_starts_with is not None:
            result['UsernameStartsWith'] = self.username_starts_with
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayNameStartsWith') is not None:
            self.display_name_starts_with = m.get('DisplayNameStartsWith')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneRegion') is not None:
            self.phone_region = m.get('PhoneRegion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserExternalId') is not None:
            self.user_external_id = m.get('UserExternalId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        if m.get('UserSourceId') is not None:
            self.user_source_id = m.get('UserSourceId')
        if m.get('UserSourceType') is not None:
            self.user_source_type = m.get('UserSourceType')
        if m.get('UsernameStartsWith') is not None:
            self.username_starts_with = m.get('UsernameStartsWith')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(self, account_expire_time=None, create_time=None, description=None, display_name=None, email=None,
                 email_verified=None, instance_id=None, lock_expire_time=None, password_expire_time=None, password_set=None,
                 phone_number=None, phone_number_verified=None, phone_region=None, register_time=None, status=None,
                 update_time=None, user_external_id=None, user_id=None, user_source_id=None, user_source_type=None,
                 username=None):
        # The time when the account expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.account_expire_time = account_expire_time  # type: long
        # The time when the account was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The description of the account.
        self.description = description  # type: str
        # The display name of the account.
        self.display_name = display_name  # type: str
        # The email address of the user who owns the account.
        self.email = email  # type: str
        # Indicates whether the email address has been verified. A value of true indicates that the email address has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the email address has not been verified.
        self.email_verified = email_verified  # type: bool
        # The ID of the instance
        self.instance_id = instance_id  # type: str
        # The time when the account lock expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.lock_expire_time = lock_expire_time  # type: long
        # Time When Password Expires
        self.password_expire_time = password_expire_time  # type: long
        # Indicates whether a password is set.
        self.password_set = password_set  # type: bool
        # The mobile number of the user who owns the account.
        self.phone_number = phone_number  # type: str
        # Indicates whether the mobile number has been verified. A value of true indicates that the mobile number has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the mobile number has not been verified.
        self.phone_number_verified = phone_number_verified  # type: bool
        # The country code of the mobile number. For example, the country code of China is 86 without 00 or +.
        self.phone_region = phone_region  # type: str
        # The time when the account was registered. This value is a UNIX timestamp. Unit: milliseconds.
        self.register_time = register_time  # type: long
        # The status of the account. Valid values:
        # 
        # *   enabled: The account is enabled.
        # *   disabled: The account is disabled.
        self.status = status  # type: str
        # The time when the account was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time  # type: long
        # The external ID of the account. The external ID can be used by external data to map the data of the account in IDaaS EIAM. By default, the external ID is the account ID.
        # 
        # For accounts with the same source type and source ID, each account has a unique external ID.
        self.user_external_id = user_external_id  # type: str
        # The ID of the account.
        self.user_id = user_id  # type: str
        # The source ID of the account.
        # 
        # If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk.
        self.user_source_id = user_source_id  # type: str
        # The source type of the account. Valid values:
        # 
        # *   build_in: The account was created in IDaaS.
        # *   ding_talk: The account was imported from DingTalk.
        # *   ad: The account was imported from Microsoft Active Directory (AD).
        # *   ldap: The account was imported from a Lightweight Directory Access Protocol (LDAP) service.
        self.user_source_type = user_source_type  # type: str
        # The username of the account.
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_expire_time is not None:
            result['AccountExpireTime'] = self.account_expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verified is not None:
            result['EmailVerified'] = self.email_verified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lock_expire_time is not None:
            result['LockExpireTime'] = self.lock_expire_time
        if self.password_expire_time is not None:
            result['PasswordExpireTime'] = self.password_expire_time
        if self.password_set is not None:
            result['PasswordSet'] = self.password_set
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_number_verified is not None:
            result['PhoneNumberVerified'] = self.phone_number_verified
        if self.phone_region is not None:
            result['PhoneRegion'] = self.phone_region
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_external_id is not None:
            result['UserExternalId'] = self.user_external_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source_id is not None:
            result['UserSourceId'] = self.user_source_id
        if self.user_source_type is not None:
            result['UserSourceType'] = self.user_source_type
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountExpireTime') is not None:
            self.account_expire_time = m.get('AccountExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerified') is not None:
            self.email_verified = m.get('EmailVerified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LockExpireTime') is not None:
            self.lock_expire_time = m.get('LockExpireTime')
        if m.get('PasswordExpireTime') is not None:
            self.password_expire_time = m.get('PasswordExpireTime')
        if m.get('PasswordSet') is not None:
            self.password_set = m.get('PasswordSet')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneNumberVerified') is not None:
            self.phone_number_verified = m.get('PhoneNumberVerified')
        if m.get('PhoneRegion') is not None:
            self.phone_region = m.get('PhoneRegion')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserExternalId') is not None:
            self.user_external_id = m.get('UserExternalId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSourceId') is not None:
            self.user_source_id = m.get('UserSourceId')
        if m.get('UserSourceType') is not None:
            self.user_source_type = m.get('UserSourceType')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, users=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of entries in the list.
        self.total_count = total_count  # type: long
        # The list of data objects of accounts.
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


class ListUsersForApplicationRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, page_number=None, page_size=None, user_ids=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return
        self.page_number = page_number  # type: long
        # The number of entries to return on each page.
        self.page_size = page_size  # type: long
        # The IDs of the accounts. You can query a maximum of 100 accounts at a time.
        self.user_ids = user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersForApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class ListUsersForApplicationResponseBodyUsers(TeaModel):
    def __init__(self, user_id=None):
        # The ID of the account.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersForApplicationResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUsersForApplicationResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, users=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned entries.
        self.total_count = total_count  # type: long
        # The IDs of the accounts.
        self.users = users  # type: list[ListUsersForApplicationResponseBodyUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersForApplicationResponseBody, self).to_map()
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
                temp_model = ListUsersForApplicationResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersForApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUsersForApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersForApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersForApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersForGroupRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None, page_number=None, page_size=None, user_ids=None):
        # The group ID.
        self.group_id = group_id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: long
        # The number of entries to return on each page. Default value: 20. Maximum value: 100.
        self.page_size = page_size  # type: long
        # The account IDs. A maximum of 100 accounts can be queried.
        self.user_ids = user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersForGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class ListUsersForGroupResponseBodyUsers(TeaModel):
    def __init__(self, user_id=None):
        # The account ID.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersForGroupResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUsersForGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, users=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned. The maximum number of entries that can be returned per page is specified by PageSize.
        self.total_count = total_count  # type: long
        # The information about accounts.
        self.users = users  # type: list[ListUsersForGroupResponseBodyUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersForGroupResponseBody, self).to_map()
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
                temp_model = ListUsersForGroupResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
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


class ObtainApplicationClientSecretRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, secret_id=None):
        # The ID of the application whose client key you want to query.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The client key ID of the application.
        self.secret_id = secret_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ObtainApplicationClientSecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        return self


class ObtainApplicationClientSecretResponseBodyApplicationClientSecret(TeaModel):
    def __init__(self, application_id=None, client_id=None, client_secret=None, instance_id=None,
                 last_used_time=None, secret_id=None, status=None):
        # The ID of the application whose client key you want to query.
        self.application_id = application_id  # type: str
        # The client ID of the application.
        self.client_id = client_id  # type: str
        # The client key secret of the application.
        self.client_secret = client_secret  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The time when the client key was last used. The value is a UNIX timestamp. Unit: milliseconds.
        self.last_used_time = last_used_time  # type: long
        # The client key ID of the application.
        self.secret_id = secret_id  # type: str
        # The status of the client key. Valid values:
        # 
        # *   Enabled: The client key is enabled.
        # *   Disabled: The client key is disabled.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ObtainApplicationClientSecretResponseBodyApplicationClientSecret, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ObtainApplicationClientSecretResponseBody(TeaModel):
    def __init__(self, application_client_secret=None, request_id=None):
        # The information about the client key.
        self.application_client_secret = application_client_secret  # type: ObtainApplicationClientSecretResponseBodyApplicationClientSecret
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application_client_secret:
            self.application_client_secret.validate()

    def to_map(self):
        _map = super(ObtainApplicationClientSecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_client_secret is not None:
            result['ApplicationClientSecret'] = self.application_client_secret.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationClientSecret') is not None:
            temp_model = ObtainApplicationClientSecretResponseBodyApplicationClientSecret()
            self.application_client_secret = temp_model.from_map(m['ApplicationClientSecret'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ObtainApplicationClientSecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ObtainApplicationClientSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ObtainApplicationClientSecretResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ObtainApplicationClientSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ObtainDomainProxyTokenRequest(TeaModel):
    def __init__(self, domain_id=None, domain_proxy_token_id=None, instance_id=None):
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # 域名代理Token ID。
        self.domain_proxy_token_id = domain_proxy_token_id  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ObtainDomainProxyTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_proxy_token_id is not None:
            result['DomainProxyTokenId'] = self.domain_proxy_token_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainProxyTokenId') is not None:
            self.domain_proxy_token_id = m.get('DomainProxyTokenId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ObtainDomainProxyTokenResponseBodyDomainProxyToken(TeaModel):
    def __init__(self, create_time=None, domain_id=None, domain_proxy_token=None, domain_proxy_token_id=None,
                 instance_id=None, last_used_time=None, status=None, update_time=None):
        # 域名代理Token创建时间，Unix时间戳格式，单位为毫秒。
        self.create_time = create_time  # type: long
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # 域名代理Token。
        self.domain_proxy_token = domain_proxy_token  # type: str
        # 域名代理Token ID。
        self.domain_proxy_token_id = domain_proxy_token_id  # type: str
        # 实例ID。
        self.instance_id = instance_id  # type: str
        # 域名代理Token最近使用时间，Unix时间戳格式，单位为毫秒。
        self.last_used_time = last_used_time  # type: long
        # token状态，枚举类型：(enabled）启用,（disabled）禁用。
        self.status = status  # type: str
        # 域名代理Token最近更新时间，Unix时间戳格式，单位为毫秒。
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ObtainDomainProxyTokenResponseBodyDomainProxyToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_proxy_token is not None:
            result['DomainProxyToken'] = self.domain_proxy_token
        if self.domain_proxy_token_id is not None:
            result['DomainProxyTokenId'] = self.domain_proxy_token_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainProxyToken') is not None:
            self.domain_proxy_token = m.get('DomainProxyToken')
        if m.get('DomainProxyTokenId') is not None:
            self.domain_proxy_token_id = m.get('DomainProxyTokenId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ObtainDomainProxyTokenResponseBody(TeaModel):
    def __init__(self, domain_proxy_token=None, request_id=None):
        self.domain_proxy_token = domain_proxy_token  # type: ObtainDomainProxyTokenResponseBodyDomainProxyToken
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_proxy_token:
            self.domain_proxy_token.validate()

    def to_map(self):
        _map = super(ObtainDomainProxyTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_proxy_token is not None:
            result['DomainProxyToken'] = self.domain_proxy_token.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainProxyToken') is not None:
            temp_model = ObtainDomainProxyTokenResponseBodyDomainProxyToken()
            self.domain_proxy_token = temp_model.from_map(m['DomainProxyToken'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ObtainDomainProxyTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ObtainDomainProxyTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ObtainDomainProxyTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ObtainDomainProxyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromOrganizationalUnitsRequest(TeaModel):
    def __init__(self, instance_id=None, organizational_unit_ids=None, user_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The organization IDs. You can remove an account from a maximum of 100 organizations.
        self.organizational_unit_ids = organizational_unit_ids  # type: list[str]
        # The account ID.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserFromOrganizationalUnitsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RemoveUserFromOrganizationalUnitsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserFromOrganizationalUnitsResponseBody, self).to_map()
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


class RemoveUserFromOrganizationalUnitsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveUserFromOrganizationalUnitsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveUserFromOrganizationalUnitsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveUserFromOrganizationalUnitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUsersFromGroupRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None, user_ids=None):
        # The group ID.
        self.group_id = group_id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The account IDs. A maximum of 100 accounts can be removed from a group.
        self.user_ids = user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUsersFromGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class RemoveUsersFromGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUsersFromGroupResponseBody, self).to_map()
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


class RevokeApplicationFromGroupsRequest(TeaModel):
    def __init__(self, application_id=None, group_ids=None, instance_id=None):
        # The application ID.
        self.application_id = application_id  # type: str
        # The group IDs. You can specify up to 100 group IDs at a time.
        self.group_ids = group_ids  # type: list[str]
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeApplicationFromGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RevokeApplicationFromGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeApplicationFromGroupsResponseBody, self).to_map()
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


class RevokeApplicationFromGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RevokeApplicationFromGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeApplicationFromGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevokeApplicationFromGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeApplicationFromOrganizationalUnitsRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, organizational_unit_ids=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The IDs of the organizations. You can revoke the access permissions from a maximum of 100 organizations at a time.
        self.organizational_unit_ids = organizational_unit_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeApplicationFromOrganizationalUnitsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')
        return self


class RevokeApplicationFromOrganizationalUnitsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeApplicationFromOrganizationalUnitsResponseBody, self).to_map()
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


class RevokeApplicationFromOrganizationalUnitsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RevokeApplicationFromOrganizationalUnitsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeApplicationFromOrganizationalUnitsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevokeApplicationFromOrganizationalUnitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeApplicationFromUsersRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, user_ids=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The IDs of the accounts. You can revoke the access permissions from a maximum of 100 accounts at a time.
        self.user_ids = user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeApplicationFromUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class RevokeApplicationFromUsersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeApplicationFromUsersResponseBody, self).to_map()
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


class RevokeApplicationFromUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RevokeApplicationFromUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeApplicationFromUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevokeApplicationFromUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApplicationGrantScopeRequest(TeaModel):
    def __init__(self, application_id=None, grant_scopes=None, instance_id=None):
        # The ID of the application that you want to configure.
        self.application_id = application_id  # type: str
        # The permissions of the Developer API feature.
        self.grant_scopes = grant_scopes  # type: list[str]
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApplicationGrantScopeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.grant_scopes is not None:
            result['GrantScopes'] = self.grant_scopes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('GrantScopes') is not None:
            self.grant_scopes = m.get('GrantScopes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SetApplicationGrantScopeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApplicationGrantScopeResponseBody, self).to_map()
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


class SetApplicationGrantScopeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetApplicationGrantScopeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetApplicationGrantScopeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetApplicationGrantScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApplicationProvisioningConfigRequestCallbackProvisioningConfig(TeaModel):
    def __init__(self, callback_url=None, encrypt_key=None, encrypt_required=None, listen_event_scopes=None):
        # The URL that the application uses to receive IDaaS event callbacks.
        self.callback_url = callback_url  # type: str
        # The symmetric key for IDaaS event callbacks. The key is an AES-256 encryption key in the HEX format.
        self.encrypt_key = encrypt_key  # type: str
        # Specifies whether to encrypt IDaaS event callback messages. Valid values:
        # 
        # *   true: encrypt the messages.
        # *   false: transmit the messages in plaintext.
        self.encrypt_required = encrypt_required  # type: bool
        # The list of types of IDaaS event callback messages that are supported by the listener.
        self.listen_event_scopes = listen_event_scopes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApplicationProvisioningConfigRequestCallbackProvisioningConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.encrypt_key is not None:
            result['EncryptKey'] = self.encrypt_key
        if self.encrypt_required is not None:
            result['EncryptRequired'] = self.encrypt_required
        if self.listen_event_scopes is not None:
            result['ListenEventScopes'] = self.listen_event_scopes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('EncryptKey') is not None:
            self.encrypt_key = m.get('EncryptKey')
        if m.get('EncryptRequired') is not None:
            self.encrypt_required = m.get('EncryptRequired')
        if m.get('ListenEventScopes') is not None:
            self.listen_event_scopes = m.get('ListenEventScopes')
        return self


class SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfigurationAuthnParam(TeaModel):
    def __init__(self, access_token=None, authn_method=None, client_id=None, client_secret=None,
                 token_endpoint=None):
        # The access token. If the GrantType parameter is set to bearer_token, you can set this parameter.
        self.access_token = access_token  # type: str
        # The authentication mode of the SCIM protocol. Valid values:
        # 
        # *   client_secret_basic: The client secret is passed in the request header.
        # *   client_secret_post: The client secret is passed in the request body.
        self.authn_method = authn_method  # type: str
        # The client ID of the application.
        self.client_id = client_id  # type: str
        # The client secret of the application.
        self.client_secret = client_secret  # type: str
        # The token endpoint.
        self.token_endpoint = token_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfigurationAuthnParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.authn_method is not None:
            result['AuthnMethod'] = self.authn_method
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret
        if self.token_endpoint is not None:
            result['TokenEndpoint'] = self.token_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AuthnMethod') is not None:
            self.authn_method = m.get('AuthnMethod')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')
        if m.get('TokenEndpoint') is not None:
            self.token_endpoint = m.get('TokenEndpoint')
        return self


class SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfiguration(TeaModel):
    def __init__(self, authn_mode=None, authn_param=None, grant_type=None):
        # The authentication mode of the SCIM protocol. Valid value:
        # 
        # *   oauth2: OAuth2.0 mode.
        self.authn_mode = authn_mode  # type: str
        # The configuration parameters related to authorization.
        # 
        # *   If the GrantType parameter is set to client_credentials, you can set the configuration parameters ClientId, ClientSecret, and AuthnMethod.
        # *   If the GrantType parameter is set to bearer_token, you can set the configuration parameter AccessToken.
        self.authn_param = authn_param  # type: SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfigurationAuthnParam
        # The grant type of the SCIM protocol. Valid values:
        # 
        # *   client_credentials: client mode.
        # *   bearer_token: key mode.
        self.grant_type = grant_type  # type: str

    def validate(self):
        if self.authn_param:
            self.authn_param.validate()

    def to_map(self):
        _map = super(SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authn_mode is not None:
            result['AuthnMode'] = self.authn_mode
        if self.authn_param is not None:
            result['AuthnParam'] = self.authn_param.to_map()
        if self.grant_type is not None:
            result['GrantType'] = self.grant_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthnMode') is not None:
            self.authn_mode = m.get('AuthnMode')
        if m.get('AuthnParam') is not None:
            temp_model = SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfigurationAuthnParam()
            self.authn_param = temp_model.from_map(m['AuthnParam'])
        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')
        return self


class SetApplicationProvisioningConfigRequestScimProvisioningConfig(TeaModel):
    def __init__(self, authn_configuration=None, full_push_scopes=None, provisioning_actions=None,
                 scim_base_url=None):
        # The configuration parameters related to SCIM-based synchronization.
        self.authn_configuration = authn_configuration  # type: SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfiguration
        # The full synchronization scope of the SCIM protocol. Valid value:
        # 
        # *   urn:alibaba:idaas:app:scim:User:PUSH: full account data synchronization.
        self.full_push_scopes = full_push_scopes  # type: list[str]
        # The resource operations of the SCIM protocol. Valid values:
        # 
        # *   urn:alibaba:idaas:app:scim:User:CREATE: account creation.
        # *   urn:alibaba:idaas:app:scim:User:UPDATE: account update.
        # *   urn:alibaba:idaas:app:scim:User:DELETE: account deletion.
        self.provisioning_actions = provisioning_actions  # type: list[str]
        # The base URL that the application uses to receive the SCIM protocol for IDaaS synchronization.
        self.scim_base_url = scim_base_url  # type: str

    def validate(self):
        if self.authn_configuration:
            self.authn_configuration.validate()

    def to_map(self):
        _map = super(SetApplicationProvisioningConfigRequestScimProvisioningConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authn_configuration is not None:
            result['AuthnConfiguration'] = self.authn_configuration.to_map()
        if self.full_push_scopes is not None:
            result['FullPushScopes'] = self.full_push_scopes
        if self.provisioning_actions is not None:
            result['ProvisioningActions'] = self.provisioning_actions
        if self.scim_base_url is not None:
            result['ScimBaseUrl'] = self.scim_base_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthnConfiguration') is not None:
            temp_model = SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfiguration()
            self.authn_configuration = temp_model.from_map(m['AuthnConfiguration'])
        if m.get('FullPushScopes') is not None:
            self.full_push_scopes = m.get('FullPushScopes')
        if m.get('ProvisioningActions') is not None:
            self.provisioning_actions = m.get('ProvisioningActions')
        if m.get('ScimBaseUrl') is not None:
            self.scim_base_url = m.get('ScimBaseUrl')
        return self


class SetApplicationProvisioningConfigRequest(TeaModel):
    def __init__(self, application_id=None, callback_provisioning_config=None, instance_id=None,
                 provision_password=None, provision_protocol_type=None, scim_provisioning_config=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The configuration of event callback synchronization. This parameter is required when the ProvisionProtocolType parameter is set to idaas_callback.
        self.callback_provisioning_config = callback_provisioning_config  # type: SetApplicationProvisioningConfigRequestCallbackProvisioningConfig
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Specifies whether to synchronize the password in IDaaS user event callbacks. Valid values:
        # 
        # *   true: synchronize the password.
        # *   false: do not synchronize the password.
        self.provision_password = provision_password  # type: bool
        # The synchronization protocol type of the application. Valid values:
        # 
        # *   idaas_callback: custom event callback protocol of IDaaS.
        # *   scim2: System for Cross-domain Identity Management (SCIM) protocol.
        self.provision_protocol_type = provision_protocol_type  # type: str
        # The configuration of SCIM-based IDaaS synchronization. This parameter is required when the ProvisionProtocolType parameter is set to scim2.
        self.scim_provisioning_config = scim_provisioning_config  # type: SetApplicationProvisioningConfigRequestScimProvisioningConfig

    def validate(self):
        if self.callback_provisioning_config:
            self.callback_provisioning_config.validate()
        if self.scim_provisioning_config:
            self.scim_provisioning_config.validate()

    def to_map(self):
        _map = super(SetApplicationProvisioningConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.callback_provisioning_config is not None:
            result['CallbackProvisioningConfig'] = self.callback_provisioning_config.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.provision_password is not None:
            result['ProvisionPassword'] = self.provision_password
        if self.provision_protocol_type is not None:
            result['ProvisionProtocolType'] = self.provision_protocol_type
        if self.scim_provisioning_config is not None:
            result['ScimProvisioningConfig'] = self.scim_provisioning_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CallbackProvisioningConfig') is not None:
            temp_model = SetApplicationProvisioningConfigRequestCallbackProvisioningConfig()
            self.callback_provisioning_config = temp_model.from_map(m['CallbackProvisioningConfig'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProvisionPassword') is not None:
            self.provision_password = m.get('ProvisionPassword')
        if m.get('ProvisionProtocolType') is not None:
            self.provision_protocol_type = m.get('ProvisionProtocolType')
        if m.get('ScimProvisioningConfig') is not None:
            temp_model = SetApplicationProvisioningConfigRequestScimProvisioningConfig()
            self.scim_provisioning_config = temp_model.from_map(m['ScimProvisioningConfig'])
        return self


class SetApplicationProvisioningConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApplicationProvisioningConfigResponseBody, self).to_map()
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


class SetApplicationProvisioningConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetApplicationProvisioningConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetApplicationProvisioningConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetApplicationProvisioningConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApplicationProvisioningScopeRequest(TeaModel):
    def __init__(self, application_id=None, instance_id=None, organizational_unit_ids=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The list of organizational units that are authorized for account synchronization.
        self.organizational_unit_ids = organizational_unit_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApplicationProvisioningScopeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')
        return self


class SetApplicationProvisioningScopeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApplicationProvisioningScopeResponseBody, self).to_map()
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


class SetApplicationProvisioningScopeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetApplicationProvisioningScopeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetApplicationProvisioningScopeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetApplicationProvisioningScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApplicationSsoConfigRequestOidcSsoConfigCustomClaims(TeaModel):
    def __init__(self, claim_name=None, claim_value_expression=None):
        # The claim name.
        self.claim_name = claim_name  # type: str
        # The expression that is used to generate the value of the claim.
        self.claim_value_expression = claim_value_expression  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApplicationSsoConfigRequestOidcSsoConfigCustomClaims, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_name is not None:
            result['ClaimName'] = self.claim_name
        if self.claim_value_expression is not None:
            result['ClaimValueExpression'] = self.claim_value_expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClaimName') is not None:
            self.claim_name = m.get('ClaimName')
        if m.get('ClaimValueExpression') is not None:
            self.claim_value_expression = m.get('ClaimValueExpression')
        return self


class SetApplicationSsoConfigRequestOidcSsoConfig(TeaModel):
    def __init__(self, access_token_effective_time=None, code_effective_time=None, custom_claims=None,
                 grant_scopes=None, grant_types=None, id_token_effective_time=None, password_authentication_source_id=None,
                 password_totp_mfa_required=None, pkce_challenge_methods=None, pkce_required=None, post_logout_redirect_uris=None,
                 redirect_uris=None, refresh_token_effective=None, response_types=None, subject_id_expression=None):
        # The validity period of the issued access token. Unit: seconds. Default value: 1200.
        self.access_token_effective_time = access_token_effective_time  # type: long
        # The validity period of the issued code. Unit: seconds. Default value: 60.
        self.code_effective_time = code_effective_time  # type: long
        # The custom claims that are returned for the ID token.
        self.custom_claims = custom_claims  # type: list[SetApplicationSsoConfigRequestOidcSsoConfigCustomClaims]
        # The scopes of user attributes that can be returned for the UserInfo endpoint or ID token.
        self.grant_scopes = grant_scopes  # type: list[str]
        # The list of grant types that are supported for OIDC protocols.
        self.grant_types = grant_types  # type: list[str]
        # The validity period of the issued ID token. Unit: seconds. Default value: 300.
        self.id_token_effective_time = id_token_effective_time  # type: long
        # The ID of the identity authentication source in password mode. Specify this parameter only when the value of the GrantTypes parameter includes the password mode.
        self.password_authentication_source_id = password_authentication_source_id  # type: str
        # Specifies whether time-based one-time password (TOTP) authentication is required in password mode. Specify this parameter only when the value of the GrantTypes parameter includes the password mode.
        self.password_totp_mfa_required = password_totp_mfa_required  # type: bool
        # The algorithms that are used to calculate the code challenge for PKCE.
        self.pkce_challenge_methods = pkce_challenge_methods  # type: list[str]
        # Specifies whether the SSO of the application requires Proof Key for Code Exchange (PKCE) (RFC 7636).
        self.pkce_required = pkce_required  # type: bool
        # The list of logout redirect URIs that are supported by the application.
        self.post_logout_redirect_uris = post_logout_redirect_uris  # type: list[str]
        # The list of redirect URIs that are supported by the application.
        self.redirect_uris = redirect_uris  # type: list[str]
        # The validity period of the issued refresh token. Unit: seconds. Default value: 86400.
        self.refresh_token_effective = refresh_token_effective  # type: long
        # The response types that are supported by the application. Specify this parameter when the value of the GrantTypes parameter includes the implicit mode.
        self.response_types = response_types  # type: list[str]
        # The custom expression that is used to generate the subject ID returned for the ID token.
        self.subject_id_expression = subject_id_expression  # type: str

    def validate(self):
        if self.custom_claims:
            for k in self.custom_claims:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SetApplicationSsoConfigRequestOidcSsoConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_effective_time is not None:
            result['AccessTokenEffectiveTime'] = self.access_token_effective_time
        if self.code_effective_time is not None:
            result['CodeEffectiveTime'] = self.code_effective_time
        result['CustomClaims'] = []
        if self.custom_claims is not None:
            for k in self.custom_claims:
                result['CustomClaims'].append(k.to_map() if k else None)
        if self.grant_scopes is not None:
            result['GrantScopes'] = self.grant_scopes
        if self.grant_types is not None:
            result['GrantTypes'] = self.grant_types
        if self.id_token_effective_time is not None:
            result['IdTokenEffectiveTime'] = self.id_token_effective_time
        if self.password_authentication_source_id is not None:
            result['PasswordAuthenticationSourceId'] = self.password_authentication_source_id
        if self.password_totp_mfa_required is not None:
            result['PasswordTotpMfaRequired'] = self.password_totp_mfa_required
        if self.pkce_challenge_methods is not None:
            result['PkceChallengeMethods'] = self.pkce_challenge_methods
        if self.pkce_required is not None:
            result['PkceRequired'] = self.pkce_required
        if self.post_logout_redirect_uris is not None:
            result['PostLogoutRedirectUris'] = self.post_logout_redirect_uris
        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris
        if self.refresh_token_effective is not None:
            result['RefreshTokenEffective'] = self.refresh_token_effective
        if self.response_types is not None:
            result['ResponseTypes'] = self.response_types
        if self.subject_id_expression is not None:
            result['SubjectIdExpression'] = self.subject_id_expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessTokenEffectiveTime') is not None:
            self.access_token_effective_time = m.get('AccessTokenEffectiveTime')
        if m.get('CodeEffectiveTime') is not None:
            self.code_effective_time = m.get('CodeEffectiveTime')
        self.custom_claims = []
        if m.get('CustomClaims') is not None:
            for k in m.get('CustomClaims'):
                temp_model = SetApplicationSsoConfigRequestOidcSsoConfigCustomClaims()
                self.custom_claims.append(temp_model.from_map(k))
        if m.get('GrantScopes') is not None:
            self.grant_scopes = m.get('GrantScopes')
        if m.get('GrantTypes') is not None:
            self.grant_types = m.get('GrantTypes')
        if m.get('IdTokenEffectiveTime') is not None:
            self.id_token_effective_time = m.get('IdTokenEffectiveTime')
        if m.get('PasswordAuthenticationSourceId') is not None:
            self.password_authentication_source_id = m.get('PasswordAuthenticationSourceId')
        if m.get('PasswordTotpMfaRequired') is not None:
            self.password_totp_mfa_required = m.get('PasswordTotpMfaRequired')
        if m.get('PkceChallengeMethods') is not None:
            self.pkce_challenge_methods = m.get('PkceChallengeMethods')
        if m.get('PkceRequired') is not None:
            self.pkce_required = m.get('PkceRequired')
        if m.get('PostLogoutRedirectUris') is not None:
            self.post_logout_redirect_uris = m.get('PostLogoutRedirectUris')
        if m.get('RedirectUris') is not None:
            self.redirect_uris = m.get('RedirectUris')
        if m.get('RefreshTokenEffective') is not None:
            self.refresh_token_effective = m.get('RefreshTokenEffective')
        if m.get('ResponseTypes') is not None:
            self.response_types = m.get('ResponseTypes')
        if m.get('SubjectIdExpression') is not None:
            self.subject_id_expression = m.get('SubjectIdExpression')
        return self


class SetApplicationSsoConfigRequestSamlSsoConfigAttributeStatements(TeaModel):
    def __init__(self, attribute_name=None, attribute_value_expression=None):
        # The attribute name.
        self.attribute_name = attribute_name  # type: str
        # The expression that is used to generate the value of the attribute.
        self.attribute_value_expression = attribute_value_expression  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApplicationSsoConfigRequestSamlSsoConfigAttributeStatements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value_expression is not None:
            result['AttributeValueExpression'] = self.attribute_value_expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValueExpression') is not None:
            self.attribute_value_expression = m.get('AttributeValueExpression')
        return self


class SetApplicationSsoConfigRequestSamlSsoConfig(TeaModel):
    def __init__(self, assertion_signed=None, attribute_statements=None, default_relay_state=None,
                 name_id_format=None, name_id_value_expression=None, response_signed=None, signature_algorithm=None,
                 sp_entity_id=None, sp_sso_acs_url=None):
        # assertion是否签名
        self.assertion_signed = assertion_signed  # type: bool
        # The additional user attributes in the SAML assertion.
        self.attribute_statements = attribute_statements  # type: list[SetApplicationSsoConfigRequestSamlSsoConfigAttributeStatements]
        # The default value of the RelayState attribute. If the SSO request is initiated in EIAM, the RelayState attribute in the SAML response is set to this default value.
        self.default_relay_state = default_relay_state  # type: str
        # The Format attribute of the NameID element in the SAML assertion. Valid values:
        # 
        # *   urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified: No format is specified. How to resolve the NameID element depends on the application.
        # *   urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress: The NameID element must be an email address.
        # *   urn:oasis:names:tc:SAML:2.0:nameid-format:persistent: The NameID element must be persistent.
        # *   urn:oasis:names:tc:SAML:2.0:nameid-format:transient: The NameID element must be transient.
        self.name_id_format = name_id_format  # type: str
        # The expression that is used to generate the value of NameID in the SAML assertion.
        self.name_id_value_expression = name_id_value_expression  # type: str
        # response是否签名
        self.response_signed = response_signed  # type: bool
        # The algorithm that is used to calculate the signature for the SAML assertion.
        self.signature_algorithm = signature_algorithm  # type: str
        # The entity ID of the application in SAML. The application assumes the role of service provider.
        self.sp_entity_id = sp_entity_id  # type: str
        # The Assertion Consumer Service (ACS) URL of the application in SAML. The application assumes the role of service provider.
        self.sp_sso_acs_url = sp_sso_acs_url  # type: str

    def validate(self):
        if self.attribute_statements:
            for k in self.attribute_statements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SetApplicationSsoConfigRequestSamlSsoConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assertion_signed is not None:
            result['AssertionSigned'] = self.assertion_signed
        result['AttributeStatements'] = []
        if self.attribute_statements is not None:
            for k in self.attribute_statements:
                result['AttributeStatements'].append(k.to_map() if k else None)
        if self.default_relay_state is not None:
            result['DefaultRelayState'] = self.default_relay_state
        if self.name_id_format is not None:
            result['NameIdFormat'] = self.name_id_format
        if self.name_id_value_expression is not None:
            result['NameIdValueExpression'] = self.name_id_value_expression
        if self.response_signed is not None:
            result['ResponseSigned'] = self.response_signed
        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm
        if self.sp_entity_id is not None:
            result['SpEntityId'] = self.sp_entity_id
        if self.sp_sso_acs_url is not None:
            result['SpSsoAcsUrl'] = self.sp_sso_acs_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssertionSigned') is not None:
            self.assertion_signed = m.get('AssertionSigned')
        self.attribute_statements = []
        if m.get('AttributeStatements') is not None:
            for k in m.get('AttributeStatements'):
                temp_model = SetApplicationSsoConfigRequestSamlSsoConfigAttributeStatements()
                self.attribute_statements.append(temp_model.from_map(k))
        if m.get('DefaultRelayState') is not None:
            self.default_relay_state = m.get('DefaultRelayState')
        if m.get('NameIdFormat') is not None:
            self.name_id_format = m.get('NameIdFormat')
        if m.get('NameIdValueExpression') is not None:
            self.name_id_value_expression = m.get('NameIdValueExpression')
        if m.get('ResponseSigned') is not None:
            self.response_signed = m.get('ResponseSigned')
        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')
        if m.get('SpEntityId') is not None:
            self.sp_entity_id = m.get('SpEntityId')
        if m.get('SpSsoAcsUrl') is not None:
            self.sp_sso_acs_url = m.get('SpSsoAcsUrl')
        return self


class SetApplicationSsoConfigRequest(TeaModel):
    def __init__(self, application_id=None, init_login_type=None, init_login_url=None, instance_id=None,
                 oidc_sso_config=None, saml_sso_config=None):
        # The ID of the application.
        self.application_id = application_id  # type: str
        # The initial SSO method. Valid values:
        # 
        # *   only_app_init_sso: Only application-initiated SSO is allowed. This method is selected by default when the SSO protocol of the application is an OIDC protocol. If this method is selected when the SSO protocol of the application is SAML, the InitLoginUrl parameter is required.
        # *   idaas_or_app_init_sso: IDaaS-initiated SSO and application-initiated SSO are allowed. This method is selected by default when the SSO protocol of the application is SAML. If this method is selected when the SSO protocol of the application is an OIDC protocol, the InitLoginUrl parameter is required.
        self.init_login_type = init_login_type  # type: str
        # The initial webhook URL of SSO. This parameter is required when the SSO protocol of the application is an OIDC protocol and the InitLoginType parameters is set to idaas_or_app_init_sso or when the SSO protocol of the application is SAML and the InitLoginType parameter is set to only_app_init_sso.
        self.init_login_url = init_login_url  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The Open ID Connect (OIDC)-based SSO configuration attributes of the application.
        self.oidc_sso_config = oidc_sso_config  # type: SetApplicationSsoConfigRequestOidcSsoConfig
        # The Security Assertion Markup Language (SAML)-based SSO configuration attributes of the application.
        self.saml_sso_config = saml_sso_config  # type: SetApplicationSsoConfigRequestSamlSsoConfig

    def validate(self):
        if self.oidc_sso_config:
            self.oidc_sso_config.validate()
        if self.saml_sso_config:
            self.saml_sso_config.validate()

    def to_map(self):
        _map = super(SetApplicationSsoConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.init_login_type is not None:
            result['InitLoginType'] = self.init_login_type
        if self.init_login_url is not None:
            result['InitLoginUrl'] = self.init_login_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.oidc_sso_config is not None:
            result['OidcSsoConfig'] = self.oidc_sso_config.to_map()
        if self.saml_sso_config is not None:
            result['SamlSsoConfig'] = self.saml_sso_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InitLoginType') is not None:
            self.init_login_type = m.get('InitLoginType')
        if m.get('InitLoginUrl') is not None:
            self.init_login_url = m.get('InitLoginUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OidcSsoConfig') is not None:
            temp_model = SetApplicationSsoConfigRequestOidcSsoConfig()
            self.oidc_sso_config = temp_model.from_map(m['OidcSsoConfig'])
        if m.get('SamlSsoConfig') is not None:
            temp_model = SetApplicationSsoConfigRequestSamlSsoConfig()
            self.saml_sso_config = temp_model.from_map(m['SamlSsoConfig'])
        return self


class SetApplicationSsoConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApplicationSsoConfigResponseBody, self).to_map()
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


class SetApplicationSsoConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetApplicationSsoConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetApplicationSsoConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetApplicationSsoConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultDomainRequest(TeaModel):
    def __init__(self, domain_id=None, instance_id=None):
        # 域名ID。
        self.domain_id = domain_id  # type: str
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SetDefaultDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultDomainResponseBody, self).to_map()
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


class SetForgetPasswordConfigurationRequest(TeaModel):
    def __init__(self, authentication_channels=None, forget_password_status=None, instance_id=None):
        # 身份认证渠道。枚举取值:email(邮件)、sms(短信)
        self.authentication_channels = authentication_channels  # type: list[str]
        # 忘记密码配置状态。枚举取值:enabled(开启)、disabled(禁用)
        self.forget_password_status = forget_password_status  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetForgetPasswordConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_channels is not None:
            result['AuthenticationChannels'] = self.authentication_channels
        if self.forget_password_status is not None:
            result['ForgetPasswordStatus'] = self.forget_password_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthenticationChannels') is not None:
            self.authentication_channels = m.get('AuthenticationChannels')
        if m.get('ForgetPasswordStatus') is not None:
            self.forget_password_status = m.get('ForgetPasswordStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SetForgetPasswordConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetForgetPasswordConfigurationResponseBody, self).to_map()
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


class SetForgetPasswordConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetForgetPasswordConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetForgetPasswordConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetForgetPasswordConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPasswordComplexityConfigurationRequestPasswordComplexityRules(TeaModel):
    def __init__(self, password_check_type=None):
        # The type of the password check. Valid values:
        # 
        # *   inclusion_upper_case: The password must contain uppercase letters.
        # *   inclusion_lower_case: The password must contain lowercase letters.
        # *   inclusion_special_case: The password must contain one or more of the following special characters: @ % + \ / \" ! # $ ^ ? : , ( ) { } \[ ] ~ - \_ .
        # *   inclusion_number: The password must contain digits.
        # *   exclusion_username: The password cannot contain a username.
        # *   exclusion_email: The password cannot contain an email prefix.
        # *   exclusion_phone_number: The password cannot contain a mobile number.
        # *   exclusion_display_name: The password cannot contain a display name.
        self.password_check_type = password_check_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPasswordComplexityConfigurationRequestPasswordComplexityRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password_check_type is not None:
            result['PasswordCheckType'] = self.password_check_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordCheckType') is not None:
            self.password_check_type = m.get('PasswordCheckType')
        return self


class SetPasswordComplexityConfigurationRequest(TeaModel):
    def __init__(self, instance_id=None, password_complexity_rules=None, password_min_length=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The password complexity rules.
        self.password_complexity_rules = password_complexity_rules  # type: list[SetPasswordComplexityConfigurationRequestPasswordComplexityRules]
        # The minimum number of characters in a password.
        self.password_min_length = password_min_length  # type: int

    def validate(self):
        if self.password_complexity_rules:
            for k in self.password_complexity_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SetPasswordComplexityConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['PasswordComplexityRules'] = []
        if self.password_complexity_rules is not None:
            for k in self.password_complexity_rules:
                result['PasswordComplexityRules'].append(k.to_map() if k else None)
        if self.password_min_length is not None:
            result['PasswordMinLength'] = self.password_min_length
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.password_complexity_rules = []
        if m.get('PasswordComplexityRules') is not None:
            for k in m.get('PasswordComplexityRules'):
                temp_model = SetPasswordComplexityConfigurationRequestPasswordComplexityRules()
                self.password_complexity_rules.append(temp_model.from_map(k))
        if m.get('PasswordMinLength') is not None:
            self.password_min_length = m.get('PasswordMinLength')
        return self


class SetPasswordComplexityConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPasswordComplexityConfigurationResponseBody, self).to_map()
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


class SetPasswordComplexityConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetPasswordComplexityConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetPasswordComplexityConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetPasswordComplexityConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPasswordExpirationConfigurationRequest(TeaModel):
    def __init__(self, instance_id=None, password_expiration_action=None,
                 password_expiration_notification_channels=None, password_expiration_notification_duration=None,
                 password_expiration_notification_status=None, password_expiration_status=None, password_forced_update_duration=None,
                 password_valid_max_day=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The action to take upon password expiration. This parameter must be specified when PasswordExpirationStatus is set to enabled. Valid values:
        # 
        # *   forbid_login: Users cannot log on to IDaaS.
        # *   force_update_password: Users must change the password.
        # *   remind_update_password: IDaaS reminds users to change the password upon each logon.
        self.password_expiration_action = password_expiration_action  # type: str
        # The methods for receiving password expiration notifications. This parameter must be specified when PasswordExpirationNotificationStatus is set to enabled.
        self.password_expiration_notification_channels = password_expiration_notification_channels  # type: list[str]
        # The number of days before the expiration date during which password expiration notifications are sent. Unit: day. This parameter must be specified when PasswordExpirationNotificationStatus is set to enabled.
        self.password_expiration_notification_duration = password_expiration_notification_duration  # type: int
        # Specifies whether to enable the password expiration notification feature. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_expiration_notification_status = password_expiration_notification_status  # type: str
        # Specifies whether to enable the password expiration feature. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_expiration_status = password_expiration_status  # type: str
        # The number of days before which users must change the password to prevent password expiration. Unit: day. You must set this parameter to a value greater than the value of PasswordExpirationNotificationDuration.
        self.password_forced_update_duration = password_forced_update_duration  # type: int
        # The validity period of a password. Unit: day. This parameter must be specified when PasswordExpirationStatus is set to enabled.
        self.password_valid_max_day = password_valid_max_day  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPasswordExpirationConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password_expiration_action is not None:
            result['PasswordExpirationAction'] = self.password_expiration_action
        if self.password_expiration_notification_channels is not None:
            result['PasswordExpirationNotificationChannels'] = self.password_expiration_notification_channels
        if self.password_expiration_notification_duration is not None:
            result['PasswordExpirationNotificationDuration'] = self.password_expiration_notification_duration
        if self.password_expiration_notification_status is not None:
            result['PasswordExpirationNotificationStatus'] = self.password_expiration_notification_status
        if self.password_expiration_status is not None:
            result['PasswordExpirationStatus'] = self.password_expiration_status
        if self.password_forced_update_duration is not None:
            result['PasswordForcedUpdateDuration'] = self.password_forced_update_duration
        if self.password_valid_max_day is not None:
            result['PasswordValidMaxDay'] = self.password_valid_max_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PasswordExpirationAction') is not None:
            self.password_expiration_action = m.get('PasswordExpirationAction')
        if m.get('PasswordExpirationNotificationChannels') is not None:
            self.password_expiration_notification_channels = m.get('PasswordExpirationNotificationChannels')
        if m.get('PasswordExpirationNotificationDuration') is not None:
            self.password_expiration_notification_duration = m.get('PasswordExpirationNotificationDuration')
        if m.get('PasswordExpirationNotificationStatus') is not None:
            self.password_expiration_notification_status = m.get('PasswordExpirationNotificationStatus')
        if m.get('PasswordExpirationStatus') is not None:
            self.password_expiration_status = m.get('PasswordExpirationStatus')
        if m.get('PasswordForcedUpdateDuration') is not None:
            self.password_forced_update_duration = m.get('PasswordForcedUpdateDuration')
        if m.get('PasswordValidMaxDay') is not None:
            self.password_valid_max_day = m.get('PasswordValidMaxDay')
        return self


class SetPasswordExpirationConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPasswordExpirationConfigurationResponseBody, self).to_map()
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


class SetPasswordExpirationConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetPasswordExpirationConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetPasswordExpirationConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetPasswordExpirationConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPasswordHistoryConfigurationRequest(TeaModel):
    def __init__(self, instance_id=None, password_history_max_retention=None, password_history_status=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The maximum number of recent passwords that can be retained. This parameter must be specified when PasswordHistoryStatus is set to enabled.
        self.password_history_max_retention = password_history_max_retention  # type: int
        # Specifies whether to enable the password history feature. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_history_status = password_history_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPasswordHistoryConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password_history_max_retention is not None:
            result['PasswordHistoryMaxRetention'] = self.password_history_max_retention
        if self.password_history_status is not None:
            result['PasswordHistoryStatus'] = self.password_history_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PasswordHistoryMaxRetention') is not None:
            self.password_history_max_retention = m.get('PasswordHistoryMaxRetention')
        if m.get('PasswordHistoryStatus') is not None:
            self.password_history_status = m.get('PasswordHistoryStatus')
        return self


class SetPasswordHistoryConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPasswordHistoryConfigurationResponseBody, self).to_map()
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


class SetPasswordHistoryConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetPasswordHistoryConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetPasswordHistoryConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetPasswordHistoryConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPasswordInitializationConfigurationRequest(TeaModel):
    def __init__(self, instance_id=None, password_forced_update_status=None,
                 password_initialization_notification_channels=None, password_initialization_status=None, password_initialization_type=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Specifies whether to enable forcible password change upon first logon. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_forced_update_status = password_forced_update_status  # type: str
        # The methods for receiving password initialization notifications.
        self.password_initialization_notification_channels = password_initialization_notification_channels  # type: list[str]
        # Specifies whether to enable password initialization. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_initialization_status = password_initialization_status  # type: str
        # The password initialization method. This parameter is required when PasswordInitializationStatus is set to enabled. Set the value to random.
        # 
        # *   random: A randomly generated password is used.
        self.password_initialization_type = password_initialization_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPasswordInitializationConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password_forced_update_status is not None:
            result['PasswordForcedUpdateStatus'] = self.password_forced_update_status
        if self.password_initialization_notification_channels is not None:
            result['PasswordInitializationNotificationChannels'] = self.password_initialization_notification_channels
        if self.password_initialization_status is not None:
            result['PasswordInitializationStatus'] = self.password_initialization_status
        if self.password_initialization_type is not None:
            result['PasswordInitializationType'] = self.password_initialization_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PasswordForcedUpdateStatus') is not None:
            self.password_forced_update_status = m.get('PasswordForcedUpdateStatus')
        if m.get('PasswordInitializationNotificationChannels') is not None:
            self.password_initialization_notification_channels = m.get('PasswordInitializationNotificationChannels')
        if m.get('PasswordInitializationStatus') is not None:
            self.password_initialization_status = m.get('PasswordInitializationStatus')
        if m.get('PasswordInitializationType') is not None:
            self.password_initialization_type = m.get('PasswordInitializationType')
        return self


class SetPasswordInitializationConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPasswordInitializationConfigurationResponseBody, self).to_map()
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


class SetPasswordInitializationConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetPasswordInitializationConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetPasswordInitializationConfigurationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetPasswordInitializationConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserPrimaryOrganizationalUnitRequest(TeaModel):
    def __init__(self, instance_id=None, organizational_unit_id=None, user_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The ID of the new primary organizational unit.
        self.organizational_unit_id = organizational_unit_id  # type: str
        # The ID of the account.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserPrimaryOrganizationalUnitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SetUserPrimaryOrganizationalUnitResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserPrimaryOrganizationalUnitResponseBody, self).to_map()
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


class SetUserPrimaryOrganizationalUnitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetUserPrimaryOrganizationalUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetUserPrimaryOrganizationalUnitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetUserPrimaryOrganizationalUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockUserRequest(TeaModel):
    def __init__(self, instance_id=None, user_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The account ID.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UnlockUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockUserResponseBody, self).to_map()
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


class UnlockUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnlockUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnlockUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnlockUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationAuthorizationTypeRequest(TeaModel):
    def __init__(self, application_id=None, authorization_type=None, instance_id=None):
        # The ID of the application that you want to modify.
        self.application_id = application_id  # type: str
        # The authorization type of the application. Valid values:
        # 
        # *   authorize_required: Only the user with explicit authorization can access the application.
        # *   default_all: By default, all users can access the application.
        self.authorization_type = authorization_type  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationAuthorizationTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateApplicationAuthorizationTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationAuthorizationTypeResponseBody, self).to_map()
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


class UpdateApplicationAuthorizationTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicationAuthorizationTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationAuthorizationTypeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateApplicationAuthorizationTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationDescriptionRequest(TeaModel):
    def __init__(self, application_id=None, description=None, instance_id=None):
        # The ID of the application that you want to modify.
        self.application_id = application_id  # type: str
        # The description of the application.
        self.description = description  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateApplicationDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationDescriptionResponseBody, self).to_map()
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


class UpdateApplicationDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicationDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationDescriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateApplicationDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(self, group_external_id=None, group_id=None, group_name=None, instance_id=None):
        # The external ID of the group.
        self.group_external_id = group_external_id  # type: str
        # The group ID.
        self.group_id = group_id  # type: str
        # The name of the group.
        self.group_name = group_name  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_external_id is not None:
            result['GroupExternalId'] = self.group_external_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupExternalId') is not None:
            self.group_external_id = m.get('GroupExternalId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupResponseBody, self).to_map()
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


class UpdateGroupDescriptionRequest(TeaModel):
    def __init__(self, description=None, group_id=None, instance_id=None):
        # The description of the account group. The value can be up to 256 characters in length.
        self.description = description  # type: str
        # The ID of the account group.
        self.group_id = group_id  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateGroupDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupDescriptionResponseBody, self).to_map()
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


class UpdateGroupDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateGroupDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupDescriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGroupDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceDescriptionRequest(TeaModel):
    def __init__(self, description=None, instance_id=None):
        # The new description of the instance.
        self.description = description  # type: str
        # The ID of the instance whose description you want to modify.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateInstanceDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceDescriptionResponseBody, self).to_map()
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


class UpdateInstanceDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceDescriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateInstanceDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNetworkAccessEndpointNameRequest(TeaModel):
    def __init__(self, instance_id=None, network_access_endpoint_id=None, network_access_endpoint_name=None):
        # IDaaS EIAM实例的ID。
        self.instance_id = instance_id  # type: str
        # 专属网络端点ID。
        self.network_access_endpoint_id = network_access_endpoint_id  # type: str
        # 专属网络端点名称。
        self.network_access_endpoint_name = network_access_endpoint_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNetworkAccessEndpointNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id
        if self.network_access_endpoint_name is not None:
            result['NetworkAccessEndpointName'] = self.network_access_endpoint_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')
        if m.get('NetworkAccessEndpointName') is not None:
            self.network_access_endpoint_name = m.get('NetworkAccessEndpointName')
        return self


class UpdateNetworkAccessEndpointNameResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNetworkAccessEndpointNameResponseBody, self).to_map()
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


class UpdateNetworkAccessEndpointNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateNetworkAccessEndpointNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNetworkAccessEndpointNameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateNetworkAccessEndpointNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOrganizationalUnitRequest(TeaModel):
    def __init__(self, instance_id=None, organizational_unit_id=None, organizational_unit_name=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The organization ID.
        self.organizational_unit_id = organizational_unit_id  # type: str
        # The name of the organization. The name can be up to 64 characters in length and must be unique in the same parent organization.
        self.organizational_unit_name = organizational_unit_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOrganizationalUnitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.organizational_unit_name is not None:
            result['OrganizationalUnitName'] = self.organizational_unit_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('OrganizationalUnitName') is not None:
            self.organizational_unit_name = m.get('OrganizationalUnitName')
        return self


class UpdateOrganizationalUnitResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOrganizationalUnitResponseBody, self).to_map()
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


class UpdateOrganizationalUnitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateOrganizationalUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateOrganizationalUnitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateOrganizationalUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOrganizationalUnitDescriptionRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, organizational_unit_id=None):
        # The description of the organization. The value can be up to 256 characters in length.
        self.description = description  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The organization ID.
        self.organizational_unit_id = organizational_unit_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOrganizationalUnitDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        return self


class UpdateOrganizationalUnitDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOrganizationalUnitDescriptionResponseBody, self).to_map()
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


class UpdateOrganizationalUnitDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateOrganizationalUnitDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateOrganizationalUnitDescriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateOrganizationalUnitDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOrganizationalUnitParentIdRequest(TeaModel):
    def __init__(self, instance_id=None, organizational_unit_id=None, parent_id=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The organization ID.
        self.organizational_unit_id = organizational_unit_id  # type: str
        # The parent organization ID.
        self.parent_id = parent_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOrganizationalUnitParentIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class UpdateOrganizationalUnitParentIdResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOrganizationalUnitParentIdResponseBody, self).to_map()
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


class UpdateOrganizationalUnitParentIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateOrganizationalUnitParentIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateOrganizationalUnitParentIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateOrganizationalUnitParentIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequestCustomFields(TeaModel):
    def __init__(self, field_name=None, field_value=None, operation=None):
        # The name of the extended field. You must create an extended field before you specify this parameter. To create an extended field, go to the Extended Fields page of the specified EIAM instance in the IDaaS console.
        self.field_name = field_name  # type: str
        # The value of the extended field. The value follows the limits on the properties of the extended field.
        self.field_value = field_value  # type: str
        # The operation type of the extended field. Valid values:
        # 
        # *   add: adds a value to the extended field of the account.
        # *   replace: replaces the existing value of the extended field of the account. If the existing value to be replaced does not exist, this operation changes to the add operation.
        # *   remove: removes a value from the extended field of the account.
        self.operation = operation  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserRequestCustomFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class UpdateUserRequest(TeaModel):
    def __init__(self, custom_fields=None, display_name=None, email=None, email_verified=None, instance_id=None,
                 phone_number=None, phone_number_verified=None, phone_region=None, user_id=None, username=None):
        # The custom extended fields.
        self.custom_fields = custom_fields  # type: list[UpdateUserRequestCustomFields]
        # The display name of the account. The display name can be up to 64 characters in length.
        self.display_name = display_name  # type: str
        # The email address. The prefix of the email address can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        self.email = email  # type: str
        # Specifies whether the email address is verified. This parameter must be specified if you specify Email. You can set this parameter to true if you have no special business requirements.
        self.email_verified = email_verified  # type: bool
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The mobile number. The mobile number must be 6 to 15 digits in length.
        self.phone_number = phone_number  # type: str
        # Specifies whether the mobile number is verified. This parameter must be specified if you specify PhoneNumber. You can set this parameter to true if you have no special business requirements.
        self.phone_number_verified = phone_number_verified  # type: bool
        # The area code of the mobile number. For example, the area code of a mobile number in the Chinese mainland is 86 without 00 or the plus sign (+). This parameter must be specified if you specify PhoneNumber.
        self.phone_region = phone_region  # type: str
        # The account ID.
        self.user_id = user_id  # type: str
        # The name of the account. The name can be up to 64 characters in length. It can contain letters, digits, and the following special characters: \_ . @ -\
        self.username = username  # type: str

    def validate(self):
        if self.custom_fields:
            for k in self.custom_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomFields'] = []
        if self.custom_fields is not None:
            for k in self.custom_fields:
                result['CustomFields'].append(k.to_map() if k else None)
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verified is not None:
            result['EmailVerified'] = self.email_verified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_number_verified is not None:
            result['PhoneNumberVerified'] = self.phone_number_verified
        if self.phone_region is not None:
            result['PhoneRegion'] = self.phone_region
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_fields = []
        if m.get('CustomFields') is not None:
            for k in m.get('CustomFields'):
                temp_model = UpdateUserRequestCustomFields()
                self.custom_fields.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerified') is not None:
            self.email_verified = m.get('EmailVerified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneNumberVerified') is not None:
            self.phone_number_verified = m.get('PhoneNumberVerified')
        if m.get('PhoneRegion') is not None:
            self.phone_region = m.get('PhoneRegion')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserResponseBody, self).to_map()
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


class UpdateUserDescriptionRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, user_id=None):
        # The description of the account. The value can be up to 256 characters in length.
        self.description = description  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The ID of the account.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateUserDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserDescriptionResponseBody, self).to_map()
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


class UpdateUserDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUserDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserDescriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserPasswordRequest(TeaModel):
    def __init__(self, instance_id=None, password=None, password_forced_update_status=None, user_id=None,
                 user_notification_channels=None):
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The new password of the account. For more information about the password format, see the "Password Policies" topic.
        self.password = password  # type: str
        # Specifies whether to enable forcible password change upon first logon. Default value: disabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_forced_update_status = password_forced_update_status  # type: str
        # The account ID.
        self.user_id = user_id  # type: str
        # The methods for receiving password notifications.
        self.user_notification_channels = user_notification_channels  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.password_forced_update_status is not None:
            result['PasswordForcedUpdateStatus'] = self.password_forced_update_status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_notification_channels is not None:
            result['UserNotificationChannels'] = self.user_notification_channels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordForcedUpdateStatus') is not None:
            self.password_forced_update_status = m.get('PasswordForcedUpdateStatus')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNotificationChannels') is not None:
            self.user_notification_channels = m.get('UserNotificationChannels')
        return self


class UpdateUserPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserPasswordResponseBody, self).to_map()
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


class UpdateUserPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUserPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserPasswordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


