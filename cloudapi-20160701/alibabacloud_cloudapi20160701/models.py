# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AbolishApiRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbolishApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class AbolishApiResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbolishApiResponseBody, self).to_map()
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


class AbolishApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AbolishApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AbolishApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AbolishApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddBlackListRequest(TeaModel):
    def __init__(self, black_content=None, black_type=None, description=None, security_token=None):
        self.black_content = black_content  # type: str
        self.black_type = black_type  # type: str
        self.description = description  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBlackListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_content is not None:
            result['BlackContent'] = self.black_content
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.description is not None:
            result['Description'] = self.description
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackContent') is not None:
            self.black_content = m.get('BlackContent')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class AddBlackListResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBlackListResponseBody, self).to_map()
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


class AddBlackListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddBlackListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddBlackListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddIpControlPolicyItemRequest(TeaModel):
    def __init__(self, app_id=None, cidr_ip=None, ip_control_id=None, security_token=None):
        self.app_id = app_id  # type: str
        self.cidr_ip = cidr_ip  # type: str
        self.ip_control_id = ip_control_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIpControlPolicyItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class AddIpControlPolicyItemResponseBody(TeaModel):
    def __init__(self, policy_item_id=None, request_id=None):
        self.policy_item_id = policy_item_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIpControlPolicyItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddIpControlPolicyItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddIpControlPolicyItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddIpControlPolicyItemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddIpControlPolicyItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTrafficSpecialControlRequest(TeaModel):
    def __init__(self, security_token=None, special_key=None, special_type=None, traffic_control_id=None,
                 traffic_value=None):
        self.security_token = security_token  # type: str
        self.special_key = special_key  # type: str
        self.special_type = special_type  # type: str
        self.traffic_control_id = traffic_control_id  # type: str
        self.traffic_value = traffic_value  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTrafficSpecialControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.special_key is not None:
            result['SpecialKey'] = self.special_key
        if self.special_type is not None:
            result['SpecialType'] = self.special_type
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SpecialKey') is not None:
            self.special_key = m.get('SpecialKey')
        if m.get('SpecialType') is not None:
            self.special_type = m.get('SpecialType')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        return self


class AddTrafficSpecialControlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTrafficSpecialControlResponseBody, self).to_map()
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


class AddTrafficSpecialControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddTrafficSpecialControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddTrafficSpecialControlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddTrafficSpecialControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiRequest(TeaModel):
    def __init__(self, allow_signature_method=None, api_name=None, app_code_auth_type=None, auth_type=None,
                 description=None, disable_internet=None, error_code_samples=None, fail_result_sample=None,
                 force_nonce_check=None, group_id=None, open_id_connect_config=None, request_config=None, request_paramters=None,
                 result_body_model=None, result_descriptions=None, result_sample=None, result_type=None, security_token=None,
                 service_config=None, service_parameters=None, service_parameters_map=None, visibility=None,
                 web_socket_api_type=None):
        self.allow_signature_method = allow_signature_method  # type: str
        self.api_name = api_name  # type: str
        self.app_code_auth_type = app_code_auth_type  # type: str
        self.auth_type = auth_type  # type: str
        self.description = description  # type: str
        self.disable_internet = disable_internet  # type: bool
        self.error_code_samples = error_code_samples  # type: str
        self.fail_result_sample = fail_result_sample  # type: str
        self.force_nonce_check = force_nonce_check  # type: bool
        self.group_id = group_id  # type: str
        self.open_id_connect_config = open_id_connect_config  # type: str
        self.request_config = request_config  # type: str
        self.request_paramters = request_paramters  # type: str
        self.result_body_model = result_body_model  # type: str
        self.result_descriptions = result_descriptions  # type: str
        self.result_sample = result_sample  # type: str
        self.result_type = result_type  # type: str
        self.security_token = security_token  # type: str
        self.service_config = service_config  # type: str
        self.service_parameters = service_parameters  # type: str
        self.service_parameters_map = service_parameters_map  # type: str
        self.visibility = visibility  # type: str
        self.web_socket_api_type = web_socket_api_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_signature_method is not None:
            result['AllowSignatureMethod'] = self.allow_signature_method
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.app_code_auth_type is not None:
            result['AppCodeAuthType'] = self.app_code_auth_type
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.open_id_connect_config is not None:
            result['OpenIdConnectConfig'] = self.open_id_connect_config
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config
        if self.request_paramters is not None:
            result['RequestParamters'] = self.request_paramters
        if self.result_body_model is not None:
            result['ResultBodyModel'] = self.result_body_model
        if self.result_descriptions is not None:
            result['ResultDescriptions'] = self.result_descriptions
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        if self.service_parameters_map is not None:
            result['ServiceParametersMap'] = self.service_parameters_map
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.web_socket_api_type is not None:
            result['WebSocketApiType'] = self.web_socket_api_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowSignatureMethod') is not None:
            self.allow_signature_method = m.get('AllowSignatureMethod')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AppCodeAuthType') is not None:
            self.app_code_auth_type = m.get('AppCodeAuthType')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            self.error_code_samples = m.get('ErrorCodeSamples')
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OpenIdConnectConfig') is not None:
            self.open_id_connect_config = m.get('OpenIdConnectConfig')
        if m.get('RequestConfig') is not None:
            self.request_config = m.get('RequestConfig')
        if m.get('RequestParamters') is not None:
            self.request_paramters = m.get('RequestParamters')
        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')
        if m.get('ResultDescriptions') is not None:
            self.result_descriptions = m.get('ResultDescriptions')
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        if m.get('ServiceParametersMap') is not None:
            self.service_parameters_map = m.get('ServiceParametersMap')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('WebSocketApiType') is not None:
            self.web_socket_api_type = m.get('WebSocketApiType')
        return self


class CreateApiResponseBody(TeaModel):
    def __init__(self, api_id=None, request_id=None):
        self.api_id = api_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiGroupRequest(TeaModel):
    def __init__(self, description=None, group_name=None, instance_id=None, security_token=None):
        self.description = description  # type: str
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApiGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateApiGroupResponseBody(TeaModel):
    def __init__(self, description=None, group_id=None, group_name=None, instance_id=None, instance_type=None,
                 request_id=None, sub_domain=None):
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.request_id = request_id  # type: str
        self.sub_domain = sub_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApiGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class CreateApiGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApiGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApiGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiStageVariableRequest(TeaModel):
    def __init__(self, group_id=None, security_token=None, stage_id=None, stage_route_model=None,
                 support_route=None, variable_name=None, variable_value=None):
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_id = stage_id  # type: str
        self.stage_route_model = stage_route_model  # type: str
        self.support_route = support_route  # type: bool
        self.variable_name = variable_name  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApiStageVariableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_route_model is not None:
            result['StageRouteModel'] = self.stage_route_model
        if self.support_route is not None:
            result['SupportRoute'] = self.support_route
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageRouteModel') is not None:
            self.stage_route_model = m.get('StageRouteModel')
        if m.get('SupportRoute') is not None:
            self.support_route = m.get('SupportRoute')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class CreateApiStageVariableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApiStageVariableResponseBody, self).to_map()
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


class CreateApiStageVariableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApiStageVariableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApiStageVariableResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateApiStageVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(self, app_name=None, description=None, security_token=None):
        self.app_name = app_name  # type: str
        self.description = description  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(self, app_id=None, request_id=None):
        self.app_id = app_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomizedInfoRequest(TeaModel):
    def __init__(self, api_id=None, api_name=None, csharp_demo=None, curl_demo=None, group_id=None, java_demo=None,
                 objectc_demo=None, php_demo=None, python_demo=None, security_token=None, stage_id=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.csharp_demo = csharp_demo  # type: str
        self.curl_demo = curl_demo  # type: str
        self.group_id = group_id  # type: str
        self.java_demo = java_demo  # type: str
        self.objectc_demo = objectc_demo  # type: str
        self.php_demo = php_demo  # type: str
        self.python_demo = python_demo  # type: str
        self.security_token = security_token  # type: str
        self.stage_id = stage_id  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomizedInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.csharp_demo is not None:
            result['CsharpDemo'] = self.csharp_demo
        if self.curl_demo is not None:
            result['CurlDemo'] = self.curl_demo
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.java_demo is not None:
            result['JavaDemo'] = self.java_demo
        if self.objectc_demo is not None:
            result['ObjectcDemo'] = self.objectc_demo
        if self.php_demo is not None:
            result['PhpDemo'] = self.php_demo
        if self.python_demo is not None:
            result['PythonDemo'] = self.python_demo
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CsharpDemo') is not None:
            self.csharp_demo = m.get('CsharpDemo')
        if m.get('CurlDemo') is not None:
            self.curl_demo = m.get('CurlDemo')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JavaDemo') is not None:
            self.java_demo = m.get('JavaDemo')
        if m.get('ObjectcDemo') is not None:
            self.objectc_demo = m.get('ObjectcDemo')
        if m.get('PhpDemo') is not None:
            self.php_demo = m.get('PhpDemo')
        if m.get('PythonDemo') is not None:
            self.python_demo = m.get('PythonDemo')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class CreateCustomizedInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomizedInfoResponseBody, self).to_map()
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


class CreateCustomizedInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCustomizedInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCustomizedInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomizedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, account_quantity=None, expired_on=None, security_token=None, sku_id=None, token=None):
        self.account_quantity = account_quantity  # type: int
        self.expired_on = expired_on  # type: str
        self.security_token = security_token  # type: str
        self.sku_id = sku_id  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_quantity is not None:
            result['AccountQuantity'] = self.account_quantity
        if self.expired_on is not None:
            result['ExpiredOn'] = self.expired_on
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountQuantity') is not None:
            self.account_quantity = m.get('AccountQuantity')
        if m.get('ExpiredOn') is not None:
            self.expired_on = m.get('ExpiredOn')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        self.instance_id = instance_id  # type: str
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


class CreateIntranetDomainRequest(TeaModel):
    def __init__(self, group_id=None, security_token=None):
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntranetDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateIntranetDomainResponseBody(TeaModel):
    def __init__(self, domain_name=None, request_id=None):
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntranetDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIntranetDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIntranetDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIntranetDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateIntranetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpControlRequestIpControlPolicys(TeaModel):
    def __init__(self, app_id=None, ip=None):
        self.app_id = app_id  # type: str
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIpControlRequestIpControlPolicys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ip is not None:
            result['IP'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        return self


class CreateIpControlRequest(TeaModel):
    def __init__(self, description=None, ip_control_name=None, ip_control_policys=None, ip_control_type=None,
                 security_token=None):
        self.description = description  # type: str
        self.ip_control_name = ip_control_name  # type: str
        self.ip_control_policys = ip_control_policys  # type: list[CreateIpControlRequestIpControlPolicys]
        self.ip_control_type = ip_control_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        if self.ip_control_policys:
            for k in self.ip_control_policys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateIpControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name
        result['IpControlPolicys'] = []
        if self.ip_control_policys is not None:
            for k in self.ip_control_policys:
                result['IpControlPolicys'].append(k.to_map() if k else None)
        if self.ip_control_type is not None:
            result['IpControlType'] = self.ip_control_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')
        self.ip_control_policys = []
        if m.get('IpControlPolicys') is not None:
            for k in m.get('IpControlPolicys'):
                temp_model = CreateIpControlRequestIpControlPolicys()
                self.ip_control_policys.append(temp_model.from_map(k))
        if m.get('IpControlType') is not None:
            self.ip_control_type = m.get('IpControlType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateIpControlResponseBody(TeaModel):
    def __init__(self, ip_control_id=None, request_id=None):
        self.ip_control_id = ip_control_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIpControlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIpControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIpControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIpControlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateIpControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogConfigRequest(TeaModel):
    def __init__(self, log_type=None, security_token=None, sls_log_store=None, sls_project=None):
        self.log_type = log_type  # type: str
        self.security_token = security_token  # type: str
        self.sls_log_store = sls_log_store  # type: str
        self.sls_project = sls_project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        return self


class CreateLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogConfigResponseBody, self).to_map()
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


class CreateLogConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRaceWorkForInnerRequest(TeaModel):
    def __init__(self, commodity_code=None, group_id=None, keywords=None, logo_url=None, security_token=None,
                 short_description=None, work_name=None):
        self.commodity_code = commodity_code  # type: str
        self.group_id = group_id  # type: str
        self.keywords = keywords  # type: str
        self.logo_url = logo_url  # type: str
        self.security_token = security_token  # type: str
        self.short_description = short_description  # type: str
        self.work_name = work_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRaceWorkForInnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        return self


class CreateRaceWorkForInnerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRaceWorkForInnerResponseBody, self).to_map()
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


class CreateRaceWorkForInnerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRaceWorkForInnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRaceWorkForInnerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRaceWorkForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecretKeyRequest(TeaModel):
    def __init__(self, secret_key=None, secret_key_name=None, secret_value=None, security_token=None):
        self.secret_key = secret_key  # type: str
        self.secret_key_name = secret_key_name  # type: str
        self.secret_value = secret_value  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecretKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        if self.secret_value is not None:
            result['SecretValue'] = self.secret_value
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        if m.get('SecretValue') is not None:
            self.secret_value = m.get('SecretValue')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateSecretKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, secret_key_id=None, secret_key_name=None):
        self.request_id = request_id  # type: str
        self.secret_key_id = secret_key_id  # type: str
        self.secret_key_name = secret_key_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecretKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        return self


class CreateSecretKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSecretKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSecretKeyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSecretKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrafficControlRequest(TeaModel):
    def __init__(self, api_default=None, app_default=None, description=None, security_token=None,
                 traffic_control_name=None, traffic_control_unit=None, user_default=None):
        self.api_default = api_default  # type: int
        self.app_default = app_default  # type: int
        self.description = description  # type: str
        self.security_token = security_token  # type: str
        self.traffic_control_name = traffic_control_name  # type: str
        self.traffic_control_unit = traffic_control_unit  # type: str
        self.user_default = user_default  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrafficControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_default is not None:
            result['ApiDefault'] = self.api_default
        if self.app_default is not None:
            result['AppDefault'] = self.app_default
        if self.description is not None:
            result['Description'] = self.description
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name
        if self.traffic_control_unit is not None:
            result['TrafficControlUnit'] = self.traffic_control_unit
        if self.user_default is not None:
            result['UserDefault'] = self.user_default
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDefault') is not None:
            self.api_default = m.get('ApiDefault')
        if m.get('AppDefault') is not None:
            self.app_default = m.get('AppDefault')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')
        if m.get('TrafficControlUnit') is not None:
            self.traffic_control_unit = m.get('TrafficControlUnit')
        if m.get('UserDefault') is not None:
            self.user_default = m.get('UserDefault')
        return self


class CreateTrafficControlResponseBody(TeaModel):
    def __init__(self, request_id=None, traffic_control_id=None):
        self.request_id = request_id  # type: str
        self.traffic_control_id = traffic_control_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrafficControlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class CreateTrafficControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTrafficControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTrafficControlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTrafficControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAllTrafficSpecialControlRequest(TeaModel):
    def __init__(self, security_token=None, traffic_control_id=None):
        self.security_token = security_token  # type: str
        self.traffic_control_id = traffic_control_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAllTrafficSpecialControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class DeleteAllTrafficSpecialControlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAllTrafficSpecialControlResponseBody, self).to_map()
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


class DeleteAllTrafficSpecialControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAllTrafficSpecialControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAllTrafficSpecialControlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAllTrafficSpecialControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, security_token=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteApiResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApiResponseBody, self).to_map()
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


class DeleteApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiGroupRequest(TeaModel):
    def __init__(self, group_id=None, security_token=None):
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApiGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteApiGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApiGroupResponseBody, self).to_map()
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


class DeleteApiGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApiGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApiGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiStageVariableRequest(TeaModel):
    def __init__(self, group_id=None, security_token=None, stage_id=None, variable_name=None):
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_id = stage_id  # type: str
        self.variable_name = variable_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApiStageVariableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        return self


class DeleteApiStageVariableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApiStageVariableResponseBody, self).to_map()
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


class DeleteApiStageVariableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApiStageVariableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApiStageVariableResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteApiStageVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(self, app_id=None, security_token=None):
        self.app_id = app_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppResponseBody, self).to_map()
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


class DeleteAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(self, domain_name=None, group_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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


class DeleteDomainCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None, domain_name=None, group_id=None, security_token=None):
        self.certificate_id = certificate_id  # type: str
        self.domain_name = domain_name  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteDomainCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainCertificateResponseBody, self).to_map()
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


class DeleteDomainCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDomainCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDomainCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpControlRequest(TeaModel):
    def __init__(self, ip_control_id=None, security_token=None):
        self.ip_control_id = ip_control_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteIpControlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpControlResponseBody, self).to_map()
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


class DeleteIpControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIpControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIpControlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIpControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLogConfigRequest(TeaModel):
    def __init__(self, log_type=None, security_token=None):
        self.log_type = log_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLogConfigResponseBody, self).to_map()
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


class DeleteLogConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretKeyRequest(TeaModel):
    def __init__(self, secret_key_id=None, security_token=None):
        self.secret_key_id = secret_key_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecretKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteSecretKeyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecretKeyResponseBody, self).to_map()
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


class DeleteSecretKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSecretKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSecretKeyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSecretKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrafficControlRequest(TeaModel):
    def __init__(self, security_token=None, traffic_control_id=None):
        self.security_token = security_token  # type: str
        self.traffic_control_id = traffic_control_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrafficControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class DeleteTrafficControlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrafficControlResponseBody, self).to_map()
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


class DeleteTrafficControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTrafficControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTrafficControlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTrafficControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrafficSpecialControlRequest(TeaModel):
    def __init__(self, security_token=None, special_key=None, special_type=None, traffic_control_id=None):
        self.security_token = security_token  # type: str
        self.special_key = special_key  # type: str
        self.special_type = special_type  # type: str
        self.traffic_control_id = traffic_control_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrafficSpecialControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.special_key is not None:
            result['SpecialKey'] = self.special_key
        if self.special_type is not None:
            result['SpecialType'] = self.special_type
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SpecialKey') is not None:
            self.special_key = m.get('SpecialKey')
        if m.get('SpecialType') is not None:
            self.special_type = m.get('SpecialType')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class DeleteTrafficSpecialControlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrafficSpecialControlResponseBody, self).to_map()
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


class DeleteTrafficSpecialControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTrafficSpecialControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTrafficSpecialControlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTrafficSpecialControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApiRequest(TeaModel):
    def __init__(self, api_id=None, description=None, group_id=None, security_token=None, stage_name=None,
                 support_mock=None):
        self.api_id = api_id  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str
        self.support_mock = support_mock  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.support_mock is not None:
            result['SupportMock'] = self.support_mock
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('SupportMock') is not None:
            self.support_mock = m.get('SupportMock')
        return self


class DeployApiResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployApiResponseBody, self).to_map()
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


class DeployApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeployApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeployApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeployApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, security_token=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeApiResponseBodyConstantParametersConstantParameter(TeaModel):
    def __init__(self, constant_value=None, description=None, location=None, service_parameter_name=None):
        self.constant_value = constant_value  # type: str
        self.description = description  # type: str
        self.location = location  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyConstantParametersConstantParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constant_value is not None:
            result['ConstantValue'] = self.constant_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConstantValue') is not None:
            self.constant_value = m.get('ConstantValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiResponseBodyConstantParameters(TeaModel):
    def __init__(self, constant_parameter=None):
        self.constant_parameter = constant_parameter  # type: list[DescribeApiResponseBodyConstantParametersConstantParameter]

    def validate(self):
        if self.constant_parameter:
            for k in self.constant_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBodyConstantParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConstantParameter'] = []
        if self.constant_parameter is not None:
            for k in self.constant_parameter:
                result['ConstantParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.constant_parameter = []
        if m.get('ConstantParameter') is not None:
            for k in m.get('ConstantParameter'):
                temp_model = DescribeApiResponseBodyConstantParametersConstantParameter()
                self.constant_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyCustomSystemParametersCustomSystemParameter(TeaModel):
    def __init__(self, demo_value=None, description=None, location=None, parameter_name=None,
                 service_parameter_name=None):
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.location = location  # type: str
        self.parameter_name = parameter_name  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyCustomSystemParametersCustomSystemParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiResponseBodyCustomSystemParameters(TeaModel):
    def __init__(self, custom_system_parameter=None):
        self.custom_system_parameter = custom_system_parameter  # type: list[DescribeApiResponseBodyCustomSystemParametersCustomSystemParameter]

    def validate(self):
        if self.custom_system_parameter:
            for k in self.custom_system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBodyCustomSystemParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomSystemParameter'] = []
        if self.custom_system_parameter is not None:
            for k in self.custom_system_parameter:
                result['CustomSystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_system_parameter = []
        if m.get('CustomSystemParameter') is not None:
            for k in m.get('CustomSystemParameter'):
                temp_model = DescribeApiResponseBodyCustomSystemParametersCustomSystemParameter()
                self.custom_system_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyDeployedInfosDeployedInfo(TeaModel):
    def __init__(self, deployed_status=None, effective_version=None, stage_name=None):
        self.deployed_status = deployed_status  # type: str
        self.effective_version = effective_version  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyDeployedInfosDeployedInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployed_status is not None:
            result['DeployedStatus'] = self.deployed_status
        if self.effective_version is not None:
            result['EffectiveVersion'] = self.effective_version
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployedStatus') is not None:
            self.deployed_status = m.get('DeployedStatus')
        if m.get('EffectiveVersion') is not None:
            self.effective_version = m.get('EffectiveVersion')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiResponseBodyDeployedInfos(TeaModel):
    def __init__(self, deployed_info=None):
        self.deployed_info = deployed_info  # type: list[DescribeApiResponseBodyDeployedInfosDeployedInfo]

    def validate(self):
        if self.deployed_info:
            for k in self.deployed_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBodyDeployedInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeployedInfo'] = []
        if self.deployed_info is not None:
            for k in self.deployed_info:
                result['DeployedInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.deployed_info = []
        if m.get('DeployedInfo') is not None:
            for k in m.get('DeployedInfo'):
                temp_model = DescribeApiResponseBodyDeployedInfosDeployedInfo()
                self.deployed_info.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyErrorCodeSamplesErrorCodeSample(TeaModel):
    def __init__(self, code=None, description=None, message=None, model=None):
        self.code = code  # type: str
        self.description = description  # type: str
        self.message = message  # type: str
        self.model = model  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyErrorCodeSamplesErrorCodeSample, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        return self


class DescribeApiResponseBodyErrorCodeSamples(TeaModel):
    def __init__(self, error_code_sample=None):
        self.error_code_sample = error_code_sample  # type: list[DescribeApiResponseBodyErrorCodeSamplesErrorCodeSample]

    def validate(self):
        if self.error_code_sample:
            for k in self.error_code_sample:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBodyErrorCodeSamples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorCodeSample'] = []
        if self.error_code_sample is not None:
            for k in self.error_code_sample:
                result['ErrorCodeSample'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.error_code_sample = []
        if m.get('ErrorCodeSample') is not None:
            for k in m.get('ErrorCodeSample'):
                temp_model = DescribeApiResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyOpenIdConnectConfig(TeaModel):
    def __init__(self, id_token_param_name=None, open_id_api_type=None, public_key=None, public_key_id=None):
        self.id_token_param_name = id_token_param_name  # type: str
        self.open_id_api_type = open_id_api_type  # type: str
        self.public_key = public_key  # type: str
        self.public_key_id = public_key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyOpenIdConnectConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_token_param_name is not None:
            result['IdTokenParamName'] = self.id_token_param_name
        if self.open_id_api_type is not None:
            result['OpenIdApiType'] = self.open_id_api_type
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdTokenParamName') is not None:
            self.id_token_param_name = m.get('IdTokenParamName')
        if m.get('OpenIdApiType') is not None:
            self.open_id_api_type = m.get('OpenIdApiType')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')
        return self


class DescribeApiResponseBodyParametersMapObjectServiceParameterMap(TeaModel):
    def __init__(self, request_parameter_name=None, service_parameter_name=None):
        self.request_parameter_name = request_parameter_name  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyParametersMapObjectServiceParameterMap, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_parameter_name is not None:
            result['RequestParameterName'] = self.request_parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestParameterName') is not None:
            self.request_parameter_name = m.get('RequestParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiResponseBodyParametersMapObject(TeaModel):
    def __init__(self, service_parameter_map=None):
        self.service_parameter_map = service_parameter_map  # type: list[DescribeApiResponseBodyParametersMapObjectServiceParameterMap]

    def validate(self):
        if self.service_parameter_map:
            for k in self.service_parameter_map:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBodyParametersMapObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServiceParameterMap'] = []
        if self.service_parameter_map is not None:
            for k in self.service_parameter_map:
                result['ServiceParameterMap'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.service_parameter_map = []
        if m.get('ServiceParameterMap') is not None:
            for k in m.get('ServiceParameterMap'):
                temp_model = DescribeApiResponseBodyParametersMapObjectServiceParameterMap()
                self.service_parameter_map.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyRequestConfig(TeaModel):
    def __init__(self, body_format=None, body_model=None, post_body_description=None, request_http_method=None,
                 request_mode=None, request_path=None, request_protocol=None):
        self.body_format = body_format  # type: str
        self.body_model = body_model  # type: str
        self.post_body_description = post_body_description  # type: str
        self.request_http_method = request_http_method  # type: str
        self.request_mode = request_mode  # type: str
        self.request_path = request_path  # type: str
        self.request_protocol = request_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyRequestConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.body_model is not None:
            result['BodyModel'] = self.body_model
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.request_http_method is not None:
            result['RequestHttpMethod'] = self.request_http_method
        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode
        if self.request_path is not None:
            result['RequestPath'] = self.request_path
        if self.request_protocol is not None:
            result['RequestProtocol'] = self.request_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('BodyModel') is not None:
            self.body_model = m.get('BodyModel')
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('RequestHttpMethod') is not None:
            self.request_http_method = m.get('RequestHttpMethod')
        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')
        if m.get('RequestPath') is not None:
            self.request_path = m.get('RequestPath')
        if m.get('RequestProtocol') is not None:
            self.request_protocol = m.get('RequestProtocol')
        return self


class DescribeApiResponseBodyRequestParametersObjectRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, array_items_type=None, default_value=None, demo_value=None,
                 description=None, doc_order=None, doc_show=None, enum_value=None, json_scheme=None, location=None,
                 max_length=None, max_value=None, min_length=None, min_value=None, parameter_type=None,
                 regular_expression=None, required=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.array_items_type = array_items_type  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.doc_order = doc_order  # type: str
        self.doc_show = doc_show  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.location = location  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyRequestParametersObjectRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.location is not None:
            result['Location'] = self.location
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribeApiResponseBodyRequestParametersObject(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribeApiResponseBodyRequestParametersObjectRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBodyRequestParametersObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeApiResponseBodyRequestParametersObjectRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyServiceConfigFunctionComputeConfig(TeaModel):
    def __init__(self, fc_region_id=None, function_name=None, qualifier=None, role_arn=None, service_name=None):
        self.fc_region_id = fc_region_id  # type: str
        self.function_name = function_name  # type: str
        self.qualifier = qualifier  # type: str
        self.role_arn = role_arn  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyServiceConfigFunctionComputeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fc_region_id is not None:
            result['FcRegionId'] = self.fc_region_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FcRegionId') is not None:
            self.fc_region_id = m.get('FcRegionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeApiResponseBodyServiceConfigMockHeadersMockHeader(TeaModel):
    def __init__(self, header_name=None, header_value=None):
        self.header_name = header_name  # type: str
        self.header_value = header_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyServiceConfigMockHeadersMockHeader, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_name is not None:
            result['HeaderName'] = self.header_name
        if self.header_value is not None:
            result['HeaderValue'] = self.header_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')
        if m.get('HeaderValue') is not None:
            self.header_value = m.get('HeaderValue')
        return self


class DescribeApiResponseBodyServiceConfigMockHeaders(TeaModel):
    def __init__(self, mock_header=None):
        self.mock_header = mock_header  # type: list[DescribeApiResponseBodyServiceConfigMockHeadersMockHeader]

    def validate(self):
        if self.mock_header:
            for k in self.mock_header:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBodyServiceConfigMockHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MockHeader'] = []
        if self.mock_header is not None:
            for k in self.mock_header:
                result['MockHeader'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mock_header = []
        if m.get('MockHeader') is not None:
            for k in m.get('MockHeader'):
                temp_model = DescribeApiResponseBodyServiceConfigMockHeadersMockHeader()
                self.mock_header.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyServiceConfigVpcConfig(TeaModel):
    def __init__(self, id=None, instance_id=None, name=None, port=None, vpc_id=None, vpc_scheme=None):
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.port = port  # type: int
        self.vpc_id = vpc_id  # type: str
        self.vpc_scheme = vpc_scheme  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyServiceConfigVpcConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_scheme is not None:
            result['VpcScheme'] = self.vpc_scheme
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcScheme') is not None:
            self.vpc_scheme = m.get('VpcScheme')
        return self


class DescribeApiResponseBodyServiceConfig(TeaModel):
    def __init__(self, aone_app_name=None, content_type_catagory=None, content_type_value=None,
                 function_compute_config=None, inner_service_info=None, inner_service_type=None, mock=None, mock_headers=None,
                 mock_result=None, mock_status_code=None, service_address=None, service_http_method=None, service_path=None,
                 service_protocol=None, service_timeout=None, service_vpc_enable=None, vpc_config=None):
        self.aone_app_name = aone_app_name  # type: str
        self.content_type_catagory = content_type_catagory  # type: str
        self.content_type_value = content_type_value  # type: str
        self.function_compute_config = function_compute_config  # type: DescribeApiResponseBodyServiceConfigFunctionComputeConfig
        self.inner_service_info = inner_service_info  # type: str
        self.inner_service_type = inner_service_type  # type: str
        self.mock = mock  # type: str
        self.mock_headers = mock_headers  # type: DescribeApiResponseBodyServiceConfigMockHeaders
        self.mock_result = mock_result  # type: str
        self.mock_status_code = mock_status_code  # type: int
        self.service_address = service_address  # type: str
        self.service_http_method = service_http_method  # type: str
        self.service_path = service_path  # type: str
        self.service_protocol = service_protocol  # type: str
        self.service_timeout = service_timeout  # type: str
        self.service_vpc_enable = service_vpc_enable  # type: str
        self.vpc_config = vpc_config  # type: DescribeApiResponseBodyServiceConfigVpcConfig

    def validate(self):
        if self.function_compute_config:
            self.function_compute_config.validate()
        if self.mock_headers:
            self.mock_headers.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBodyServiceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aone_app_name is not None:
            result['AoneAppName'] = self.aone_app_name
        if self.content_type_catagory is not None:
            result['ContentTypeCatagory'] = self.content_type_catagory
        if self.content_type_value is not None:
            result['ContentTypeValue'] = self.content_type_value
        if self.function_compute_config is not None:
            result['FunctionComputeConfig'] = self.function_compute_config.to_map()
        if self.inner_service_info is not None:
            result['InnerServiceInfo'] = self.inner_service_info
        if self.inner_service_type is not None:
            result['InnerServiceType'] = self.inner_service_type
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_headers is not None:
            result['MockHeaders'] = self.mock_headers.to_map()
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.mock_status_code is not None:
            result['MockStatusCode'] = self.mock_status_code
        if self.service_address is not None:
            result['ServiceAddress'] = self.service_address
        if self.service_http_method is not None:
            result['ServiceHttpMethod'] = self.service_http_method
        if self.service_path is not None:
            result['ServicePath'] = self.service_path
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.service_vpc_enable is not None:
            result['ServiceVpcEnable'] = self.service_vpc_enable
        if self.vpc_config is not None:
            result['VpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AoneAppName') is not None:
            self.aone_app_name = m.get('AoneAppName')
        if m.get('ContentTypeCatagory') is not None:
            self.content_type_catagory = m.get('ContentTypeCatagory')
        if m.get('ContentTypeValue') is not None:
            self.content_type_value = m.get('ContentTypeValue')
        if m.get('FunctionComputeConfig') is not None:
            temp_model = DescribeApiResponseBodyServiceConfigFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m['FunctionComputeConfig'])
        if m.get('InnerServiceInfo') is not None:
            self.inner_service_info = m.get('InnerServiceInfo')
        if m.get('InnerServiceType') is not None:
            self.inner_service_type = m.get('InnerServiceType')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockHeaders') is not None:
            temp_model = DescribeApiResponseBodyServiceConfigMockHeaders()
            self.mock_headers = temp_model.from_map(m['MockHeaders'])
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('MockStatusCode') is not None:
            self.mock_status_code = m.get('MockStatusCode')
        if m.get('ServiceAddress') is not None:
            self.service_address = m.get('ServiceAddress')
        if m.get('ServiceHttpMethod') is not None:
            self.service_http_method = m.get('ServiceHttpMethod')
        if m.get('ServicePath') is not None:
            self.service_path = m.get('ServicePath')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('ServiceVpcEnable') is not None:
            self.service_vpc_enable = m.get('ServiceVpcEnable')
        if m.get('VpcConfig') is not None:
            temp_model = DescribeApiResponseBodyServiceConfigVpcConfig()
            self.vpc_config = temp_model.from_map(m['VpcConfig'])
        return self


class DescribeApiResponseBodyServiceParametersObjectServiceParam(TeaModel):
    def __init__(self, location=None, service_parameter_name=None, type=None):
        self.location = location  # type: str
        self.service_parameter_name = service_parameter_name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodyServiceParametersObjectServiceParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeApiResponseBodyServiceParametersObject(TeaModel):
    def __init__(self, service_param=None):
        self.service_param = service_param  # type: list[DescribeApiResponseBodyServiceParametersObjectServiceParam]

    def validate(self):
        if self.service_param:
            for k in self.service_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBodyServiceParametersObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServiceParam'] = []
        if self.service_param is not None:
            for k in self.service_param:
                result['ServiceParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.service_param = []
        if m.get('ServiceParam') is not None:
            for k in m.get('ServiceParam'):
                temp_model = DescribeApiResponseBodyServiceParametersObjectServiceParam()
                self.service_param.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodySystemParametersSystemParameter(TeaModel):
    def __init__(self, demo_value=None, description=None, location=None, parameter_name=None,
                 service_parameter_name=None):
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.location = location  # type: str
        self.parameter_name = parameter_name  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiResponseBodySystemParametersSystemParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiResponseBodySystemParameters(TeaModel):
    def __init__(self, system_parameter=None):
        self.system_parameter = system_parameter  # type: list[DescribeApiResponseBodySystemParametersSystemParameter]

    def validate(self):
        if self.system_parameter:
            for k in self.system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBodySystemParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParameter'] = []
        if self.system_parameter is not None:
            for k in self.system_parameter:
                result['SystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.system_parameter = []
        if m.get('SystemParameter') is not None:
            for k in m.get('SystemParameter'):
                temp_model = DescribeApiResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBody(TeaModel):
    def __init__(self, allow_signature_method=None, api_id=None, api_name=None, app_code_auth_type=None,
                 auth_type=None, constant_parameters=None, created_time=None, custom_system_parameters=None,
                 deployed_infos=None, description=None, disable_internet=None, error_code_samples=None, fail_result_sample=None,
                 force_nonce_check=None, group_id=None, group_name=None, mock=None, mock_result=None, modified_time=None,
                 open_id_connect_config=None, origin_result_description=None, parameters_map_object=None, region_id=None,
                 request_config=None, request_id=None, request_parameters_object=None, result_body_model=None, result_sample=None,
                 result_type=None, service_config=None, service_parameters_object=None, system_parameters=None,
                 visibility=None, web_socket_api_type=None):
        self.allow_signature_method = allow_signature_method  # type: str
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.app_code_auth_type = app_code_auth_type  # type: str
        self.auth_type = auth_type  # type: str
        self.constant_parameters = constant_parameters  # type: DescribeApiResponseBodyConstantParameters
        self.created_time = created_time  # type: str
        self.custom_system_parameters = custom_system_parameters  # type: DescribeApiResponseBodyCustomSystemParameters
        self.deployed_infos = deployed_infos  # type: DescribeApiResponseBodyDeployedInfos
        self.description = description  # type: str
        self.disable_internet = disable_internet  # type: bool
        self.error_code_samples = error_code_samples  # type: DescribeApiResponseBodyErrorCodeSamples
        self.fail_result_sample = fail_result_sample  # type: str
        self.force_nonce_check = force_nonce_check  # type: bool
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.mock = mock  # type: str
        self.mock_result = mock_result  # type: str
        self.modified_time = modified_time  # type: str
        self.open_id_connect_config = open_id_connect_config  # type: DescribeApiResponseBodyOpenIdConnectConfig
        self.origin_result_description = origin_result_description  # type: str
        self.parameters_map_object = parameters_map_object  # type: DescribeApiResponseBodyParametersMapObject
        self.region_id = region_id  # type: str
        self.request_config = request_config  # type: DescribeApiResponseBodyRequestConfig
        self.request_id = request_id  # type: str
        self.request_parameters_object = request_parameters_object  # type: DescribeApiResponseBodyRequestParametersObject
        self.result_body_model = result_body_model  # type: str
        self.result_sample = result_sample  # type: str
        self.result_type = result_type  # type: str
        self.service_config = service_config  # type: DescribeApiResponseBodyServiceConfig
        self.service_parameters_object = service_parameters_object  # type: DescribeApiResponseBodyServiceParametersObject
        self.system_parameters = system_parameters  # type: DescribeApiResponseBodySystemParameters
        self.visibility = visibility  # type: str
        self.web_socket_api_type = web_socket_api_type  # type: str

    def validate(self):
        if self.constant_parameters:
            self.constant_parameters.validate()
        if self.custom_system_parameters:
            self.custom_system_parameters.validate()
        if self.deployed_infos:
            self.deployed_infos.validate()
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.open_id_connect_config:
            self.open_id_connect_config.validate()
        if self.parameters_map_object:
            self.parameters_map_object.validate()
        if self.request_config:
            self.request_config.validate()
        if self.request_parameters_object:
            self.request_parameters_object.validate()
        if self.service_config:
            self.service_config.validate()
        if self.service_parameters_object:
            self.service_parameters_object.validate()
        if self.system_parameters:
            self.system_parameters.validate()

    def to_map(self):
        _map = super(DescribeApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_signature_method is not None:
            result['AllowSignatureMethod'] = self.allow_signature_method
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.app_code_auth_type is not None:
            result['AppCodeAuthType'] = self.app_code_auth_type
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters.to_map()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.custom_system_parameters is not None:
            result['CustomSystemParameters'] = self.custom_system_parameters.to_map()
        if self.deployed_infos is not None:
            result['DeployedInfos'] = self.deployed_infos.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.open_id_connect_config is not None:
            result['OpenIdConnectConfig'] = self.open_id_connect_config.to_map()
        if self.origin_result_description is not None:
            result['OriginResultDescription'] = self.origin_result_description
        if self.parameters_map_object is not None:
            result['ParametersMapObject'] = self.parameters_map_object.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_parameters_object is not None:
            result['RequestParametersObject'] = self.request_parameters_object.to_map()
        if self.result_body_model is not None:
            result['ResultBodyModel'] = self.result_body_model
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config.to_map()
        if self.service_parameters_object is not None:
            result['ServiceParametersObject'] = self.service_parameters_object.to_map()
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters.to_map()
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.web_socket_api_type is not None:
            result['WebSocketApiType'] = self.web_socket_api_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowSignatureMethod') is not None:
            self.allow_signature_method = m.get('AllowSignatureMethod')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AppCodeAuthType') is not None:
            self.app_code_auth_type = m.get('AppCodeAuthType')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('ConstantParameters') is not None:
            temp_model = DescribeApiResponseBodyConstantParameters()
            self.constant_parameters = temp_model.from_map(m['ConstantParameters'])
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CustomSystemParameters') is not None:
            temp_model = DescribeApiResponseBodyCustomSystemParameters()
            self.custom_system_parameters = temp_model.from_map(m['CustomSystemParameters'])
        if m.get('DeployedInfos') is not None:
            temp_model = DescribeApiResponseBodyDeployedInfos()
            self.deployed_infos = temp_model.from_map(m['DeployedInfos'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OpenIdConnectConfig') is not None:
            temp_model = DescribeApiResponseBodyOpenIdConnectConfig()
            self.open_id_connect_config = temp_model.from_map(m['OpenIdConnectConfig'])
        if m.get('OriginResultDescription') is not None:
            self.origin_result_description = m.get('OriginResultDescription')
        if m.get('ParametersMapObject') is not None:
            temp_model = DescribeApiResponseBodyParametersMapObject()
            self.parameters_map_object = temp_model.from_map(m['ParametersMapObject'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestConfig') is not None:
            temp_model = DescribeApiResponseBodyRequestConfig()
            self.request_config = temp_model.from_map(m['RequestConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestParametersObject') is not None:
            temp_model = DescribeApiResponseBodyRequestParametersObject()
            self.request_parameters_object = temp_model.from_map(m['RequestParametersObject'])
        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceConfig') is not None:
            temp_model = DescribeApiResponseBodyServiceConfig()
            self.service_config = temp_model.from_map(m['ServiceConfig'])
        if m.get('ServiceParametersObject') is not None:
            temp_model = DescribeApiResponseBodyServiceParametersObject()
            self.service_parameters_object = temp_model.from_map(m['ServiceParametersObject'])
        if m.get('SystemParameters') is not None:
            temp_model = DescribeApiResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m['SystemParameters'])
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('WebSocketApiType') is not None:
            self.web_socket_api_type = m.get('WebSocketApiType')
        return self


class DescribeApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiDocRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiDocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiDocResponseBodyErrorCodeSamplesErrorCodeSample(TeaModel):
    def __init__(self, code=None, description=None, message=None):
        self.code = code  # type: str
        self.description = description  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiDocResponseBodyErrorCodeSamplesErrorCodeSample, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeApiDocResponseBodyErrorCodeSamples(TeaModel):
    def __init__(self, error_code_sample=None):
        self.error_code_sample = error_code_sample  # type: list[DescribeApiDocResponseBodyErrorCodeSamplesErrorCodeSample]

    def validate(self):
        if self.error_code_sample:
            for k in self.error_code_sample:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiDocResponseBodyErrorCodeSamples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorCodeSample'] = []
        if self.error_code_sample is not None:
            for k in self.error_code_sample:
                result['ErrorCodeSample'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.error_code_sample = []
        if m.get('ErrorCodeSample') is not None:
            for k in m.get('ErrorCodeSample'):
                temp_model = DescribeApiDocResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBodyPathParametersPathParameter(TeaModel):
    def __init__(self, api_parameter_name=None, demo_value=None, description=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiDocResponseBodyPathParametersPathParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class DescribeApiDocResponseBodyPathParameters(TeaModel):
    def __init__(self, path_parameter=None):
        self.path_parameter = path_parameter  # type: list[DescribeApiDocResponseBodyPathParametersPathParameter]

    def validate(self):
        if self.path_parameter:
            for k in self.path_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiDocResponseBodyPathParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PathParameter'] = []
        if self.path_parameter is not None:
            for k in self.path_parameter:
                result['PathParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.path_parameter = []
        if m.get('PathParameter') is not None:
            for k in m.get('PathParameter'):
                temp_model = DescribeApiDocResponseBodyPathParametersPathParameter()
                self.path_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBodyRequestBodyRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, array_items_type=None, default_value=None, demo_value=None,
                 description=None, enum_value=None, json_scheme=None, max_length=None, max_value=None, min_length=None,
                 min_value=None, parameter_type=None, regular_expression=None, required=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.array_items_type = array_items_type  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiDocResponseBodyRequestBodyRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribeApiDocResponseBodyRequestBody(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribeApiDocResponseBodyRequestBodyRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiDocResponseBodyRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeApiDocResponseBodyRequestBodyRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBodyRequestHeadersRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, array_items_type=None, default_value=None, demo_value=None,
                 description=None, enum_value=None, json_scheme=None, max_length=None, max_value=None, min_length=None,
                 min_value=None, parameter_type=None, regular_expression=None, required=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.array_items_type = array_items_type  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiDocResponseBodyRequestHeadersRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribeApiDocResponseBodyRequestHeaders(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribeApiDocResponseBodyRequestHeadersRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiDocResponseBodyRequestHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeApiDocResponseBodyRequestHeadersRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBodyRequestQueriesRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, array_items_type=None, default_value=None, demo_value=None,
                 description=None, enum_value=None, json_scheme=None, max_length=None, max_value=None, min_length=None,
                 min_value=None, parameter_type=None, regular_expression=None, required=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.array_items_type = array_items_type  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiDocResponseBodyRequestQueriesRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribeApiDocResponseBodyRequestQueries(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribeApiDocResponseBodyRequestQueriesRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiDocResponseBodyRequestQueries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeApiDocResponseBodyRequestQueriesRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBody(TeaModel):
    def __init__(self, api_id=None, api_name=None, body_format=None, deployed_time=None, description=None,
                 disable_internet=None, error_code_samples=None, fail_result_sample=None, force_nonce_check=None, group_id=None,
                 group_name=None, http_method=None, http_protocol=None, mock=None, mock_result=None,
                 origin_result_description=None, path=None, path_parameters=None, post_body_description=None, post_body_type=None,
                 region_id=None, request_body=None, request_headers=None, request_id=None, request_mode=None,
                 request_queries=None, result_sample=None, result_type=None, service_timeout=None, service_vpc_enable=None,
                 stage_name=None, vpc_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.body_format = body_format  # type: str
        self.deployed_time = deployed_time  # type: str
        self.description = description  # type: str
        self.disable_internet = disable_internet  # type: bool
        self.error_code_samples = error_code_samples  # type: DescribeApiDocResponseBodyErrorCodeSamples
        self.fail_result_sample = fail_result_sample  # type: str
        self.force_nonce_check = force_nonce_check  # type: bool
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.http_method = http_method  # type: str
        self.http_protocol = http_protocol  # type: str
        self.mock = mock  # type: str
        self.mock_result = mock_result  # type: str
        self.origin_result_description = origin_result_description  # type: str
        self.path = path  # type: str
        self.path_parameters = path_parameters  # type: DescribeApiDocResponseBodyPathParameters
        self.post_body_description = post_body_description  # type: str
        self.post_body_type = post_body_type  # type: str
        self.region_id = region_id  # type: str
        self.request_body = request_body  # type: DescribeApiDocResponseBodyRequestBody
        self.request_headers = request_headers  # type: DescribeApiDocResponseBodyRequestHeaders
        self.request_id = request_id  # type: str
        self.request_mode = request_mode  # type: str
        self.request_queries = request_queries  # type: DescribeApiDocResponseBodyRequestQueries
        self.result_sample = result_sample  # type: str
        self.result_type = result_type  # type: str
        self.service_timeout = service_timeout  # type: int
        self.service_vpc_enable = service_vpc_enable  # type: str
        self.stage_name = stage_name  # type: str
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.path_parameters:
            self.path_parameters.validate()
        if self.request_body:
            self.request_body.validate()
        if self.request_headers:
            self.request_headers.validate()
        if self.request_queries:
            self.request_queries.validate()

    def to_map(self):
        _map = super(DescribeApiDocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.http_protocol is not None:
            result['HttpProtocol'] = self.http_protocol
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.origin_result_description is not None:
            result['OriginResultDescription'] = self.origin_result_description
        if self.path is not None:
            result['Path'] = self.path
        if self.path_parameters is not None:
            result['PathParameters'] = self.path_parameters.to_map()
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.post_body_type is not None:
            result['PostBodyType'] = self.post_body_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_body is not None:
            result['RequestBody'] = self.request_body.to_map()
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.service_vpc_enable is not None:
            result['ServiceVpcEnable'] = self.service_vpc_enable
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeApiDocResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('HttpProtocol') is not None:
            self.http_protocol = m.get('HttpProtocol')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('OriginResultDescription') is not None:
            self.origin_result_description = m.get('OriginResultDescription')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathParameters') is not None:
            temp_model = DescribeApiDocResponseBodyPathParameters()
            self.path_parameters = temp_model.from_map(m['PathParameters'])
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('PostBodyType') is not None:
            self.post_body_type = m.get('PostBodyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestBody') is not None:
            temp_model = DescribeApiDocResponseBodyRequestBody()
            self.request_body = temp_model.from_map(m['RequestBody'])
        if m.get('RequestHeaders') is not None:
            temp_model = DescribeApiDocResponseBodyRequestHeaders()
            self.request_headers = temp_model.from_map(m['RequestHeaders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')
        if m.get('RequestQueries') is not None:
            temp_model = DescribeApiDocResponseBodyRequestQueries()
            self.request_queries = temp_model.from_map(m['RequestQueries'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('ServiceVpcEnable') is not None:
            self.service_vpc_enable = m.get('ServiceVpcEnable')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeApiDocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiDocResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiDocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiDocsRequest(TeaModel):
    def __init__(self, api_id=None, api_name=None, group_id=None, page_number=None, page_size=None,
                 security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiDocsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiDocsResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(self, api_id=None, api_name=None, deployed_time=None, description=None, group_description=None,
                 group_id=None, group_name=None, region_id=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.deployed_time = deployed_time  # type: str
        self.description = description  # type: str
        self.group_description = group_description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.region_id = region_id  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiDocsResponseBodyApiInfosApiInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_description is not None:
            result['GroupDescription'] = self.group_description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupDescription') is not None:
            self.group_description = m.get('GroupDescription')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiDocsResponseBodyApiInfos(TeaModel):
    def __init__(self, api_info=None):
        self.api_info = api_info  # type: list[DescribeApiDocsResponseBodyApiInfosApiInfo]

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiDocsResponseBodyApiInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeApiDocsResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApiDocsResponseBody(TeaModel):
    def __init__(self, api_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.api_infos = api_infos  # type: DescribeApiDocsResponseBodyApiInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super(DescribeApiDocsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
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
        if m.get('ApiInfos') is not None:
            temp_model = DescribeApiDocsResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiDocsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiDocsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiDocsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiDocsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiErrorRequest(TeaModel):
    def __init__(self, api_id=None, end_time=None, group_id=None, security_token=None, start_time=None):
        self.api_id = api_id  # type: str
        self.end_time = end_time  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiErrorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiErrorResponseBodyClientErrorsClientError(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiErrorResponseBodyClientErrorsClientError, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiErrorResponseBodyClientErrors(TeaModel):
    def __init__(self, client_error=None):
        self.client_error = client_error  # type: list[DescribeApiErrorResponseBodyClientErrorsClientError]

    def validate(self):
        if self.client_error:
            for k in self.client_error:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiErrorResponseBodyClientErrors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientError'] = []
        if self.client_error is not None:
            for k in self.client_error:
                result['ClientError'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.client_error = []
        if m.get('ClientError') is not None:
            for k in m.get('ClientError'):
                temp_model = DescribeApiErrorResponseBodyClientErrorsClientError()
                self.client_error.append(temp_model.from_map(k))
        return self


class DescribeApiErrorResponseBodyServerErrorsServerError(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiErrorResponseBodyServerErrorsServerError, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiErrorResponseBodyServerErrors(TeaModel):
    def __init__(self, server_error=None):
        self.server_error = server_error  # type: list[DescribeApiErrorResponseBodyServerErrorsServerError]

    def validate(self):
        if self.server_error:
            for k in self.server_error:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiErrorResponseBodyServerErrors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerError'] = []
        if self.server_error is not None:
            for k in self.server_error:
                result['ServerError'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.server_error = []
        if m.get('ServerError') is not None:
            for k in m.get('ServerError'):
                temp_model = DescribeApiErrorResponseBodyServerErrorsServerError()
                self.server_error.append(temp_model.from_map(k))
        return self


class DescribeApiErrorResponseBody(TeaModel):
    def __init__(self, client_errors=None, request_id=None, server_errors=None):
        self.client_errors = client_errors  # type: DescribeApiErrorResponseBodyClientErrors
        self.request_id = request_id  # type: str
        self.server_errors = server_errors  # type: DescribeApiErrorResponseBodyServerErrors

    def validate(self):
        if self.client_errors:
            self.client_errors.validate()
        if self.server_errors:
            self.server_errors.validate()

    def to_map(self):
        _map = super(DescribeApiErrorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_errors is not None:
            result['ClientErrors'] = self.client_errors.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_errors is not None:
            result['ServerErrors'] = self.server_errors.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientErrors') is not None:
            temp_model = DescribeApiErrorResponseBodyClientErrors()
            self.client_errors = temp_model.from_map(m['ClientErrors'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerErrors') is not None:
            temp_model = DescribeApiErrorResponseBodyServerErrors()
            self.server_errors = temp_model.from_map(m['ServerErrors'])
        return self


class DescribeApiErrorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiErrorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiErrorResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiErrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGroupDetailRequest(TeaModel):
    def __init__(self, group_id=None, security_token=None):
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiGroupDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeApiGroupDetailResponseBodyDomainItemsDomainItem(TeaModel):
    def __init__(self, bind_stage_name=None, certificate_id=None, certificate_name=None,
                 domain_binding_status=None, domain_legal_status=None, domain_name=None, domain_name_resolution=None, domain_remark=None,
                 domain_web_socket_status=None, wildcard_domain_patterns=None):
        self.bind_stage_name = bind_stage_name  # type: str
        self.certificate_id = certificate_id  # type: str
        self.certificate_name = certificate_name  # type: str
        self.domain_binding_status = domain_binding_status  # type: str
        self.domain_legal_status = domain_legal_status  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_name_resolution = domain_name_resolution  # type: str
        self.domain_remark = domain_remark  # type: str
        self.domain_web_socket_status = domain_web_socket_status  # type: str
        self.wildcard_domain_patterns = wildcard_domain_patterns  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiGroupDetailResponseBodyDomainItemsDomainItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_stage_name is not None:
            result['BindStageName'] = self.bind_stage_name
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_binding_status is not None:
            result['DomainBindingStatus'] = self.domain_binding_status
        if self.domain_legal_status is not None:
            result['DomainLegalStatus'] = self.domain_legal_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        if self.domain_remark is not None:
            result['DomainRemark'] = self.domain_remark
        if self.domain_web_socket_status is not None:
            result['DomainWebSocketStatus'] = self.domain_web_socket_status
        if self.wildcard_domain_patterns is not None:
            result['WildcardDomainPatterns'] = self.wildcard_domain_patterns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindStageName') is not None:
            self.bind_stage_name = m.get('BindStageName')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainBindingStatus') is not None:
            self.domain_binding_status = m.get('DomainBindingStatus')
        if m.get('DomainLegalStatus') is not None:
            self.domain_legal_status = m.get('DomainLegalStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        if m.get('DomainRemark') is not None:
            self.domain_remark = m.get('DomainRemark')
        if m.get('DomainWebSocketStatus') is not None:
            self.domain_web_socket_status = m.get('DomainWebSocketStatus')
        if m.get('WildcardDomainPatterns') is not None:
            self.wildcard_domain_patterns = m.get('WildcardDomainPatterns')
        return self


class DescribeApiGroupDetailResponseBodyDomainItems(TeaModel):
    def __init__(self, domain_item=None):
        self.domain_item = domain_item  # type: list[DescribeApiGroupDetailResponseBodyDomainItemsDomainItem]

    def validate(self):
        if self.domain_item:
            for k in self.domain_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiGroupDetailResponseBodyDomainItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainItem'] = []
        if self.domain_item is not None:
            for k in self.domain_item:
                result['DomainItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_item = []
        if m.get('DomainItem') is not None:
            for k in m.get('DomainItem'):
                temp_model = DescribeApiGroupDetailResponseBodyDomainItemsDomainItem()
                self.domain_item.append(temp_model.from_map(k))
        return self


class DescribeApiGroupDetailResponseBodyStageItemsStageInfo(TeaModel):
    def __init__(self, description=None, stage_id=None, stage_name=None):
        self.description = description  # type: str
        self.stage_id = stage_id  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiGroupDetailResponseBodyStageItemsStageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiGroupDetailResponseBodyStageItems(TeaModel):
    def __init__(self, stage_info=None):
        self.stage_info = stage_info  # type: list[DescribeApiGroupDetailResponseBodyStageItemsStageInfo]

    def validate(self):
        if self.stage_info:
            for k in self.stage_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiGroupDetailResponseBodyStageItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StageInfo'] = []
        if self.stage_info is not None:
            for k in self.stage_info:
                result['StageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.stage_info = []
        if m.get('StageInfo') is not None:
            for k in m.get('StageInfo'):
                temp_model = DescribeApiGroupDetailResponseBodyStageItemsStageInfo()
                self.stage_info.append(temp_model.from_map(k))
        return self


class DescribeApiGroupDetailResponseBody(TeaModel):
    def __init__(self, billing_status=None, classic_vpc_sub_domain=None, compatible_flags=None, created_time=None,
                 custom_trace_config=None, default_domain=None, description=None, domain_items=None, group_id=None, group_name=None,
                 https_policy=None, illegal_status=None, instance_id=None, instance_name=None, instance_type=None,
                 instance_vip_list=None, ipv_6status=None, modified_time=None, passthrough_headers=None, region_id=None,
                 request_id=None, rpc_pattern=None, stage_items=None, status=None, sub_domain=None, traffic_limit=None,
                 user_log_config=None, vpc_domain=None):
        self.billing_status = billing_status  # type: str
        self.classic_vpc_sub_domain = classic_vpc_sub_domain  # type: str
        self.compatible_flags = compatible_flags  # type: str
        self.created_time = created_time  # type: str
        self.custom_trace_config = custom_trace_config  # type: str
        self.default_domain = default_domain  # type: str
        self.description = description  # type: str
        self.domain_items = domain_items  # type: DescribeApiGroupDetailResponseBodyDomainItems
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.https_policy = https_policy  # type: str
        self.illegal_status = illegal_status  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_type = instance_type  # type: str
        self.instance_vip_list = instance_vip_list  # type: str
        self.ipv_6status = ipv_6status  # type: str
        self.modified_time = modified_time  # type: str
        self.passthrough_headers = passthrough_headers  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.rpc_pattern = rpc_pattern  # type: str
        self.stage_items = stage_items  # type: DescribeApiGroupDetailResponseBodyStageItems
        self.status = status  # type: str
        self.sub_domain = sub_domain  # type: str
        self.traffic_limit = traffic_limit  # type: int
        self.user_log_config = user_log_config  # type: str
        self.vpc_domain = vpc_domain  # type: str

    def validate(self):
        if self.domain_items:
            self.domain_items.validate()
        if self.stage_items:
            self.stage_items.validate()

    def to_map(self):
        _map = super(DescribeApiGroupDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_status is not None:
            result['BillingStatus'] = self.billing_status
        if self.classic_vpc_sub_domain is not None:
            result['ClassicVpcSubDomain'] = self.classic_vpc_sub_domain
        if self.compatible_flags is not None:
            result['CompatibleFlags'] = self.compatible_flags
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.custom_trace_config is not None:
            result['CustomTraceConfig'] = self.custom_trace_config
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_items is not None:
            result['DomainItems'] = self.domain_items.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.https_policy is not None:
            result['HttpsPolicy'] = self.https_policy
        if self.illegal_status is not None:
            result['IllegalStatus'] = self.illegal_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_vip_list is not None:
            result['InstanceVipList'] = self.instance_vip_list
        if self.ipv_6status is not None:
            result['Ipv6Status'] = self.ipv_6status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.passthrough_headers is not None:
            result['PassthroughHeaders'] = self.passthrough_headers
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rpc_pattern is not None:
            result['RpcPattern'] = self.rpc_pattern
        if self.stage_items is not None:
            result['StageItems'] = self.stage_items.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.traffic_limit is not None:
            result['TrafficLimit'] = self.traffic_limit
        if self.user_log_config is not None:
            result['UserLogConfig'] = self.user_log_config
        if self.vpc_domain is not None:
            result['VpcDomain'] = self.vpc_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingStatus') is not None:
            self.billing_status = m.get('BillingStatus')
        if m.get('ClassicVpcSubDomain') is not None:
            self.classic_vpc_sub_domain = m.get('ClassicVpcSubDomain')
        if m.get('CompatibleFlags') is not None:
            self.compatible_flags = m.get('CompatibleFlags')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CustomTraceConfig') is not None:
            self.custom_trace_config = m.get('CustomTraceConfig')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainItems') is not None:
            temp_model = DescribeApiGroupDetailResponseBodyDomainItems()
            self.domain_items = temp_model.from_map(m['DomainItems'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HttpsPolicy') is not None:
            self.https_policy = m.get('HttpsPolicy')
        if m.get('IllegalStatus') is not None:
            self.illegal_status = m.get('IllegalStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceVipList') is not None:
            self.instance_vip_list = m.get('InstanceVipList')
        if m.get('Ipv6Status') is not None:
            self.ipv_6status = m.get('Ipv6Status')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PassthroughHeaders') is not None:
            self.passthrough_headers = m.get('PassthroughHeaders')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RpcPattern') is not None:
            self.rpc_pattern = m.get('RpcPattern')
        if m.get('StageItems') is not None:
            temp_model = DescribeApiGroupDetailResponseBodyStageItems()
            self.stage_items = temp_model.from_map(m['StageItems'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('TrafficLimit') is not None:
            self.traffic_limit = m.get('TrafficLimit')
        if m.get('UserLogConfig') is not None:
            self.user_log_config = m.get('UserLogConfig')
        if m.get('VpcDomain') is not None:
            self.vpc_domain = m.get('VpcDomain')
        return self


class DescribeApiGroupDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiGroupDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiGroupDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGroupDetailForConsumerRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiGroupDetailForConsumerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiGroupDetailForConsumerResponseBodyDomainItemsDomainItem(TeaModel):
    def __init__(self, certificate_id=None, certificate_name=None, domain_name=None, domain_name_resolution=None,
                 domain_status=None):
        self.certificate_id = certificate_id  # type: str
        self.certificate_name = certificate_name  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_name_resolution = domain_name_resolution  # type: str
        self.domain_status = domain_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiGroupDetailForConsumerResponseBodyDomainItemsDomainItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        return self


class DescribeApiGroupDetailForConsumerResponseBodyDomainItems(TeaModel):
    def __init__(self, domain_item=None):
        self.domain_item = domain_item  # type: list[DescribeApiGroupDetailForConsumerResponseBodyDomainItemsDomainItem]

    def validate(self):
        if self.domain_item:
            for k in self.domain_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiGroupDetailForConsumerResponseBodyDomainItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainItem'] = []
        if self.domain_item is not None:
            for k in self.domain_item:
                result['DomainItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_item = []
        if m.get('DomainItem') is not None:
            for k in m.get('DomainItem'):
                temp_model = DescribeApiGroupDetailForConsumerResponseBodyDomainItemsDomainItem()
                self.domain_item.append(temp_model.from_map(k))
        return self


class DescribeApiGroupDetailForConsumerResponseBody(TeaModel):
    def __init__(self, billing_status=None, created_time=None, description=None, domain_items=None, group_id=None,
                 group_name=None, illegal_status=None, modified_time=None, purchased=None, region_id=None, request_id=None,
                 status=None, sub_domain=None, traffic_limit=None):
        self.billing_status = billing_status  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.domain_items = domain_items  # type: DescribeApiGroupDetailForConsumerResponseBodyDomainItems
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.illegal_status = illegal_status  # type: str
        self.modified_time = modified_time  # type: str
        self.purchased = purchased  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.sub_domain = sub_domain  # type: str
        self.traffic_limit = traffic_limit  # type: int

    def validate(self):
        if self.domain_items:
            self.domain_items.validate()

    def to_map(self):
        _map = super(DescribeApiGroupDetailForConsumerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_status is not None:
            result['BillingStatus'] = self.billing_status
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_items is not None:
            result['DomainItems'] = self.domain_items.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.illegal_status is not None:
            result['IllegalStatus'] = self.illegal_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.purchased is not None:
            result['Purchased'] = self.purchased
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.traffic_limit is not None:
            result['TrafficLimit'] = self.traffic_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingStatus') is not None:
            self.billing_status = m.get('BillingStatus')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainItems') is not None:
            temp_model = DescribeApiGroupDetailForConsumerResponseBodyDomainItems()
            self.domain_items = temp_model.from_map(m['DomainItems'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IllegalStatus') is not None:
            self.illegal_status = m.get('IllegalStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Purchased') is not None:
            self.purchased = m.get('Purchased')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('TrafficLimit') is not None:
            self.traffic_limit = m.get('TrafficLimit')
        return self


class DescribeApiGroupDetailForConsumerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiGroupDetailForConsumerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiGroupDetailForConsumerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiGroupDetailForConsumerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGroupsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiGroupsRequestTag, self).to_map()
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


class DescribeApiGroupsRequest(TeaModel):
    def __init__(self, enable_tag_auth=None, group_id=None, group_name=None, instance_id=None, not_classic=None,
                 page_number=None, page_size=None, security_token=None, tag=None):
        self.enable_tag_auth = enable_tag_auth  # type: bool
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.not_classic = not_classic  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.tag = tag  # type: list[DescribeApiGroupsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tag_auth is not None:
            result['EnableTagAuth'] = self.enable_tag_auth
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.not_classic is not None:
            result['NotClassic'] = self.not_classic
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableTagAuth') is not None:
            self.enable_tag_auth = m.get('EnableTagAuth')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NotClassic') is not None:
            self.not_classic = m.get('NotClassic')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeApiGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttribute(TeaModel):
    def __init__(self, billing_status=None, created_time=None, description=None, group_id=None, group_name=None,
                 https_policy=None, illegal_status=None, instance_id=None, instance_type=None, modified_time=None,
                 region_id=None, sub_domain=None, traffic_limit=None):
        self.billing_status = billing_status  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.https_policy = https_policy  # type: str
        self.illegal_status = illegal_status  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.modified_time = modified_time  # type: str
        self.region_id = region_id  # type: str
        self.sub_domain = sub_domain  # type: str
        self.traffic_limit = traffic_limit  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_status is not None:
            result['BillingStatus'] = self.billing_status
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.https_policy is not None:
            result['HttpsPolicy'] = self.https_policy
        if self.illegal_status is not None:
            result['IllegalStatus'] = self.illegal_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.traffic_limit is not None:
            result['TrafficLimit'] = self.traffic_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingStatus') is not None:
            self.billing_status = m.get('BillingStatus')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HttpsPolicy') is not None:
            self.https_policy = m.get('HttpsPolicy')
        if m.get('IllegalStatus') is not None:
            self.illegal_status = m.get('IllegalStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('TrafficLimit') is not None:
            self.traffic_limit = m.get('TrafficLimit')
        return self


class DescribeApiGroupsResponseBodyApiGroupAttributes(TeaModel):
    def __init__(self, api_group_attribute=None):
        self.api_group_attribute = api_group_attribute  # type: list[DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttribute]

    def validate(self):
        if self.api_group_attribute:
            for k in self.api_group_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiGroupsResponseBodyApiGroupAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiGroupAttribute'] = []
        if self.api_group_attribute is not None:
            for k in self.api_group_attribute:
                result['ApiGroupAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_group_attribute = []
        if m.get('ApiGroupAttribute') is not None:
            for k in m.get('ApiGroupAttribute'):
                temp_model = DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttribute()
                self.api_group_attribute.append(temp_model.from_map(k))
        return self


class DescribeApiGroupsResponseBody(TeaModel):
    def __init__(self, api_group_attributes=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.api_group_attributes = api_group_attributes  # type: DescribeApiGroupsResponseBodyApiGroupAttributes
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_group_attributes:
            self.api_group_attributes.validate()

    def to_map(self):
        _map = super(DescribeApiGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_group_attributes is not None:
            result['ApiGroupAttributes'] = self.api_group_attributes.to_map()
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
        if m.get('ApiGroupAttributes') is not None:
            temp_model = DescribeApiGroupsResponseBodyApiGroupAttributes()
            self.api_group_attributes = temp_model.from_map(m['ApiGroupAttributes'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiIpControlsRequest(TeaModel):
    def __init__(self, api_ids=None, group_id=None, page_number=None, page_size=None, security_token=None,
                 stage_name=None):
        self.api_ids = api_ids  # type: str
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiIpControlsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiIpControlsResponseBodyApiIpControlsApiIpControlItem(TeaModel):
    def __init__(self, api_id=None, api_name=None, bound_time=None, ip_control_id=None, ip_control_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.bound_time = bound_time  # type: str
        self.ip_control_id = ip_control_id  # type: str
        self.ip_control_name = ip_control_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiIpControlsResponseBodyApiIpControlsApiIpControlItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')
        return self


class DescribeApiIpControlsResponseBodyApiIpControls(TeaModel):
    def __init__(self, api_ip_control_item=None):
        self.api_ip_control_item = api_ip_control_item  # type: list[DescribeApiIpControlsResponseBodyApiIpControlsApiIpControlItem]

    def validate(self):
        if self.api_ip_control_item:
            for k in self.api_ip_control_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiIpControlsResponseBodyApiIpControls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiIpControlItem'] = []
        if self.api_ip_control_item is not None:
            for k in self.api_ip_control_item:
                result['ApiIpControlItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_ip_control_item = []
        if m.get('ApiIpControlItem') is not None:
            for k in m.get('ApiIpControlItem'):
                temp_model = DescribeApiIpControlsResponseBodyApiIpControlsApiIpControlItem()
                self.api_ip_control_item.append(temp_model.from_map(k))
        return self


class DescribeApiIpControlsResponseBody(TeaModel):
    def __init__(self, api_ip_controls=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.api_ip_controls = api_ip_controls  # type: DescribeApiIpControlsResponseBodyApiIpControls
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_ip_controls:
            self.api_ip_controls.validate()

    def to_map(self):
        _map = super(DescribeApiIpControlsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ip_controls is not None:
            result['ApiIpControls'] = self.api_ip_controls.to_map()
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
        if m.get('ApiIpControls') is not None:
            temp_model = DescribeApiIpControlsResponseBodyApiIpControls()
            self.api_ip_controls = temp_model.from_map(m['ApiIpControls'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiIpControlsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiIpControlsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiIpControlsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiIpControlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiLatencyRequest(TeaModel):
    def __init__(self, api_id=None, end_time=None, group_id=None, security_token=None, start_time=None):
        self.api_id = api_id  # type: str
        self.end_time = end_time  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiLatencyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiLatencyResponseBodyLatencysLatency(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiLatencyResponseBodyLatencysLatency, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiLatencyResponseBodyLatencys(TeaModel):
    def __init__(self, latency=None):
        self.latency = latency  # type: list[DescribeApiLatencyResponseBodyLatencysLatency]

    def validate(self):
        if self.latency:
            for k in self.latency:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiLatencyResponseBodyLatencys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Latency'] = []
        if self.latency is not None:
            for k in self.latency:
                result['Latency'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.latency = []
        if m.get('Latency') is not None:
            for k in m.get('Latency'):
                temp_model = DescribeApiLatencyResponseBodyLatencysLatency()
                self.latency.append(temp_model.from_map(k))
        return self


class DescribeApiLatencyResponseBody(TeaModel):
    def __init__(self, latencys=None, request_id=None):
        self.latencys = latencys  # type: DescribeApiLatencyResponseBodyLatencys
        self.request_id = request_id  # type: str

    def validate(self):
        if self.latencys:
            self.latencys.validate()

    def to_map(self):
        _map = super(DescribeApiLatencyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latencys is not None:
            result['Latencys'] = self.latencys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Latencys') is not None:
            temp_model = DescribeApiLatencyResponseBodyLatencys()
            self.latencys = temp_model.from_map(m['Latencys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApiLatencyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiLatencyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiLatencyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiLatencyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiQpsRequest(TeaModel):
    def __init__(self, api_id=None, end_time=None, group_id=None, security_token=None, start_time=None):
        self.api_id = api_id  # type: str
        self.end_time = end_time  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiQpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiQpsResponseBodyFailsFail(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiQpsResponseBodyFailsFail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiQpsResponseBodyFails(TeaModel):
    def __init__(self, fail=None):
        self.fail = fail  # type: list[DescribeApiQpsResponseBodyFailsFail]

    def validate(self):
        if self.fail:
            for k in self.fail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiQpsResponseBodyFails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fail'] = []
        if self.fail is not None:
            for k in self.fail:
                result['Fail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fail = []
        if m.get('Fail') is not None:
            for k in m.get('Fail'):
                temp_model = DescribeApiQpsResponseBodyFailsFail()
                self.fail.append(temp_model.from_map(k))
        return self


class DescribeApiQpsResponseBodySuccessesSuccess(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiQpsResponseBodySuccessesSuccess, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiQpsResponseBodySuccesses(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: list[DescribeApiQpsResponseBodySuccessesSuccess]

    def validate(self):
        if self.success:
            for k in self.success:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiQpsResponseBodySuccesses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Success'] = []
        if self.success is not None:
            for k in self.success:
                result['Success'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.success = []
        if m.get('Success') is not None:
            for k in m.get('Success'):
                temp_model = DescribeApiQpsResponseBodySuccessesSuccess()
                self.success.append(temp_model.from_map(k))
        return self


class DescribeApiQpsResponseBody(TeaModel):
    def __init__(self, fails=None, request_id=None, successes=None):
        self.fails = fails  # type: DescribeApiQpsResponseBodyFails
        self.request_id = request_id  # type: str
        self.successes = successes  # type: DescribeApiQpsResponseBodySuccesses

    def validate(self):
        if self.fails:
            self.fails.validate()
        if self.successes:
            self.successes.validate()

    def to_map(self):
        _map = super(DescribeApiQpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fails is not None:
            result['Fails'] = self.fails.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successes is not None:
            result['Successes'] = self.successes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fails') is not None:
            temp_model = DescribeApiQpsResponseBodyFails()
            self.fails = temp_model.from_map(m['Fails'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successes') is not None:
            temp_model = DescribeApiQpsResponseBodySuccesses()
            self.successes = temp_model.from_map(m['Successes'])
        return self


class DescribeApiQpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiQpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiQpsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiQpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiRulesRequest(TeaModel):
    def __init__(self, api_ids=None, api_name=None, group_id=None, page_number=None, page_size=None, rule_type=None,
                 security_token=None, stage_name=None):
        self.api_ids = api_ids  # type: str
        self.api_name = api_name  # type: str
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.rule_type = rule_type  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiRulesResponseBodyApiRulesApiRule(TeaModel):
    def __init__(self, api_id=None, api_name=None, created_time=None, rule_id=None, rule_name=None, rule_type=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.created_time = created_time  # type: str
        self.rule_id = rule_id  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiRulesResponseBodyApiRulesApiRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DescribeApiRulesResponseBodyApiRules(TeaModel):
    def __init__(self, api_rule=None):
        self.api_rule = api_rule  # type: list[DescribeApiRulesResponseBodyApiRulesApiRule]

    def validate(self):
        if self.api_rule:
            for k in self.api_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiRulesResponseBodyApiRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiRule'] = []
        if self.api_rule is not None:
            for k in self.api_rule:
                result['ApiRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_rule = []
        if m.get('ApiRule') is not None:
            for k in m.get('ApiRule'):
                temp_model = DescribeApiRulesResponseBodyApiRulesApiRule()
                self.api_rule.append(temp_model.from_map(k))
        return self


class DescribeApiRulesResponseBody(TeaModel):
    def __init__(self, api_rules=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.api_rules = api_rules  # type: DescribeApiRulesResponseBodyApiRules
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_rules:
            self.api_rules.validate()

    def to_map(self):
        _map = super(DescribeApiRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_rules is not None:
            result['ApiRules'] = self.api_rules.to_map()
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
        if m.get('ApiRules') is not None:
            temp_model = DescribeApiRulesResponseBodyApiRules()
            self.api_rules = temp_model.from_map(m['ApiRules'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiStageDetailRequest(TeaModel):
    def __init__(self, group_id=None, security_token=None, stage_id=None):
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_id = stage_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiStageDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        return self


class DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRulesRouteRuleItem(TeaModel):
    def __init__(self, condition_value=None, max_value=None, min_value=None, result_value=None):
        self.condition_value = condition_value  # type: str
        self.max_value = max_value  # type: long
        self.min_value = min_value  # type: long
        self.result_value = result_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRulesRouteRuleItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_value is not None:
            result['ConditionValue'] = self.condition_value
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.result_value is not None:
            result['ResultValue'] = self.result_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConditionValue') is not None:
            self.condition_value = m.get('ConditionValue')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ResultValue') is not None:
            self.result_value = m.get('ResultValue')
        return self


class DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRules(TeaModel):
    def __init__(self, route_rule_item=None):
        self.route_rule_item = route_rule_item  # type: list[DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRulesRouteRuleItem]

    def validate(self):
        if self.route_rule_item:
            for k in self.route_rule_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteRuleItem'] = []
        if self.route_rule_item is not None:
            for k in self.route_rule_item:
                result['RouteRuleItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.route_rule_item = []
        if m.get('RouteRuleItem') is not None:
            for k in m.get('RouteRuleItem'):
                temp_model = DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRulesRouteRuleItem()
                self.route_rule_item.append(temp_model.from_map(k))
        return self


class DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModel(TeaModel):
    def __init__(self, location=None, parameter_catalog=None, parameter_type=None, route_match_symbol=None,
                 route_rules=None, service_parameter_name=None):
        self.location = location  # type: str
        self.parameter_catalog = parameter_catalog  # type: str
        self.parameter_type = parameter_type  # type: str
        self.route_match_symbol = route_match_symbol  # type: str
        self.route_rules = route_rules  # type: DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRules
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        if self.route_rules:
            self.route_rules.validate()

    def to_map(self):
        _map = super(DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_catalog is not None:
            result['ParameterCatalog'] = self.parameter_catalog
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.route_match_symbol is not None:
            result['RouteMatchSymbol'] = self.route_match_symbol
        if self.route_rules is not None:
            result['RouteRules'] = self.route_rules.to_map()
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterCatalog') is not None:
            self.parameter_catalog = m.get('ParameterCatalog')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RouteMatchSymbol') is not None:
            self.route_match_symbol = m.get('RouteMatchSymbol')
        if m.get('RouteRules') is not None:
            temp_model = DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRules()
            self.route_rules = temp_model.from_map(m['RouteRules'])
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiStageDetailResponseBodyVariablesVariableItem(TeaModel):
    def __init__(self, stage_route_model=None, support_route=None, variable_name=None, variable_value=None):
        self.stage_route_model = stage_route_model  # type: DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModel
        self.support_route = support_route  # type: bool
        self.variable_name = variable_name  # type: str
        self.variable_value = variable_value  # type: str

    def validate(self):
        if self.stage_route_model:
            self.stage_route_model.validate()

    def to_map(self):
        _map = super(DescribeApiStageDetailResponseBodyVariablesVariableItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stage_route_model is not None:
            result['StageRouteModel'] = self.stage_route_model.to_map()
        if self.support_route is not None:
            result['SupportRoute'] = self.support_route
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StageRouteModel') is not None:
            temp_model = DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModel()
            self.stage_route_model = temp_model.from_map(m['StageRouteModel'])
        if m.get('SupportRoute') is not None:
            self.support_route = m.get('SupportRoute')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class DescribeApiStageDetailResponseBodyVariables(TeaModel):
    def __init__(self, variable_item=None):
        self.variable_item = variable_item  # type: list[DescribeApiStageDetailResponseBodyVariablesVariableItem]

    def validate(self):
        if self.variable_item:
            for k in self.variable_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiStageDetailResponseBodyVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VariableItem'] = []
        if self.variable_item is not None:
            for k in self.variable_item:
                result['VariableItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.variable_item = []
        if m.get('VariableItem') is not None:
            for k in m.get('VariableItem'):
                temp_model = DescribeApiStageDetailResponseBodyVariablesVariableItem()
                self.variable_item.append(temp_model.from_map(k))
        return self


class DescribeApiStageDetailResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, group_id=None, modified_time=None, request_id=None,
                 stage_id=None, stage_name=None, variables=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.modified_time = modified_time  # type: str
        self.request_id = request_id  # type: str
        self.stage_id = stage_id  # type: str
        self.stage_name = stage_name  # type: str
        self.variables = variables  # type: DescribeApiStageDetailResponseBodyVariables

    def validate(self):
        if self.variables:
            self.variables.validate()

    def to_map(self):
        _map = super(DescribeApiStageDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.variables is not None:
            result['Variables'] = self.variables.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Variables') is not None:
            temp_model = DescribeApiStageDetailResponseBodyVariables()
            self.variables = temp_model.from_map(m['Variables'])
        return self


class DescribeApiStageDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiStageDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiStageDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiStageDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiTrafficRequest(TeaModel):
    def __init__(self, api_id=None, end_time=None, group_id=None, security_token=None, start_time=None):
        self.api_id = api_id  # type: str
        self.end_time = end_time  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiTrafficRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiTrafficResponseBodyDownloadsDownload(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiTrafficResponseBodyDownloadsDownload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiTrafficResponseBodyDownloads(TeaModel):
    def __init__(self, download=None):
        self.download = download  # type: list[DescribeApiTrafficResponseBodyDownloadsDownload]

    def validate(self):
        if self.download:
            for k in self.download:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiTrafficResponseBodyDownloads, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Download'] = []
        if self.download is not None:
            for k in self.download:
                result['Download'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.download = []
        if m.get('Download') is not None:
            for k in m.get('Download'):
                temp_model = DescribeApiTrafficResponseBodyDownloadsDownload()
                self.download.append(temp_model.from_map(k))
        return self


class DescribeApiTrafficResponseBodyUploadsUpload(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApiTrafficResponseBodyUploadsUpload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiTrafficResponseBodyUploads(TeaModel):
    def __init__(self, upload=None):
        self.upload = upload  # type: list[DescribeApiTrafficResponseBodyUploadsUpload]

    def validate(self):
        if self.upload:
            for k in self.upload:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApiTrafficResponseBodyUploads, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Upload'] = []
        if self.upload is not None:
            for k in self.upload:
                result['Upload'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.upload = []
        if m.get('Upload') is not None:
            for k in m.get('Upload'):
                temp_model = DescribeApiTrafficResponseBodyUploadsUpload()
                self.upload.append(temp_model.from_map(k))
        return self


class DescribeApiTrafficResponseBody(TeaModel):
    def __init__(self, downloads=None, request_id=None, uploads=None):
        self.downloads = downloads  # type: DescribeApiTrafficResponseBodyDownloads
        self.request_id = request_id  # type: str
        self.uploads = uploads  # type: DescribeApiTrafficResponseBodyUploads

    def validate(self):
        if self.downloads:
            self.downloads.validate()
        if self.uploads:
            self.uploads.validate()

    def to_map(self):
        _map = super(DescribeApiTrafficResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.downloads is not None:
            result['Downloads'] = self.downloads.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uploads is not None:
            result['Uploads'] = self.uploads.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Downloads') is not None:
            temp_model = DescribeApiTrafficResponseBodyDownloads()
            self.downloads = temp_model.from_map(m['Downloads'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Uploads') is not None:
            temp_model = DescribeApiTrafficResponseBodyUploads()
            self.uploads = temp_model.from_map(m['Uploads'])
        return self


class DescribeApiTrafficResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApiTrafficResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApiTrafficResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApiTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisRequest(TeaModel):
    def __init__(self, api_id=None, api_name=None, group_id=None, page_number=None, page_size=None,
                 security_token=None, visibility=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(self, api_id=None, api_name=None, created_time=None, description=None, group_id=None,
                 group_name=None, modified_time=None, region_id=None, visibility=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.modified_time = modified_time  # type: str
        self.region_id = region_id  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApisResponseBodyApiInfosApiInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisResponseBodyApiInfos(TeaModel):
    def __init__(self, api_info=None):
        self.api_info = api_info  # type: list[DescribeApisResponseBodyApiInfosApiInfo]

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApisResponseBodyApiInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeApisResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApisResponseBody(TeaModel):
    def __init__(self, api_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.api_infos = api_infos  # type: DescribeApisResponseBodyApiInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super(DescribeApisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
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
        if m.get('ApiInfos') is not None:
            temp_model = DescribeApisResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisByAppRequest(TeaModel):
    def __init__(self, app_id=None, page_number=None, page_size=None, security_token=None):
        self.app_id = app_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApisByAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo(TeaModel):
    def __init__(self, api_id=None, api_name=None, auth_vaild_time=None, authorization_source=None,
                 created_time=None, description=None, group_id=None, group_name=None, operator=None, region_id=None,
                 stage_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.auth_vaild_time = auth_vaild_time  # type: str
        self.authorization_source = authorization_source  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.operator = operator  # type: str
        self.region_id = region_id  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.auth_vaild_time is not None:
            result['AuthVaildTime'] = self.auth_vaild_time
        if self.authorization_source is not None:
            result['AuthorizationSource'] = self.authorization_source
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthVaildTime') is not None:
            self.auth_vaild_time = m.get('AuthVaildTime')
        if m.get('AuthorizationSource') is not None:
            self.authorization_source = m.get('AuthorizationSource')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApisByAppResponseBodyAppApiRelationInfos(TeaModel):
    def __init__(self, app_api_relation_info=None):
        self.app_api_relation_info = app_api_relation_info  # type: list[DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo]

    def validate(self):
        if self.app_api_relation_info:
            for k in self.app_api_relation_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApisByAppResponseBodyAppApiRelationInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppApiRelationInfo'] = []
        if self.app_api_relation_info is not None:
            for k in self.app_api_relation_info:
                result['AppApiRelationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_api_relation_info = []
        if m.get('AppApiRelationInfo') is not None:
            for k in m.get('AppApiRelationInfo'):
                temp_model = DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo()
                self.app_api_relation_info.append(temp_model.from_map(k))
        return self


class DescribeApisByAppResponseBody(TeaModel):
    def __init__(self, app_api_relation_infos=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.app_api_relation_infos = app_api_relation_infos  # type: DescribeApisByAppResponseBodyAppApiRelationInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.app_api_relation_infos:
            self.app_api_relation_infos.validate()

    def to_map(self):
        _map = super(DescribeApisByAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_api_relation_infos is not None:
            result['AppApiRelationInfos'] = self.app_api_relation_infos.to_map()
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
        if m.get('AppApiRelationInfos') is not None:
            temp_model = DescribeApisByAppResponseBodyAppApiRelationInfos()
            self.app_api_relation_infos = temp_model.from_map(m['AppApiRelationInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApisByAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApisByAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApisByAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApisByAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisByIpControlRequest(TeaModel):
    def __init__(self, ip_control_id=None, page_number=None, page_size=None, security_token=None):
        self.ip_control_id = ip_control_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApisByIpControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeApisByIpControlResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(self, api_id=None, api_name=None, bound_time=None, description=None, group_id=None, group_name=None,
                 region_id=None, stage_name=None, visibility=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.bound_time = bound_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.region_id = region_id  # type: str
        self.stage_name = stage_name  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApisByIpControlResponseBodyApiInfosApiInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisByIpControlResponseBodyApiInfos(TeaModel):
    def __init__(self, api_info=None):
        self.api_info = api_info  # type: list[DescribeApisByIpControlResponseBodyApiInfosApiInfo]

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApisByIpControlResponseBodyApiInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeApisByIpControlResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApisByIpControlResponseBody(TeaModel):
    def __init__(self, api_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.api_infos = api_infos  # type: DescribeApisByIpControlResponseBodyApiInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super(DescribeApisByIpControlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
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
        if m.get('ApiInfos') is not None:
            temp_model = DescribeApisByIpControlResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApisByIpControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApisByIpControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApisByIpControlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApisByIpControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisByRuleRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, rule_id=None, rule_type=None, security_token=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.rule_id = rule_id  # type: str
        self.rule_type = rule_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApisByRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeApisByRuleResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(self, api_id=None, api_name=None, created_time=None, description=None, group_id=None,
                 group_name=None, modified_time=None, region_id=None, stage_name=None, visibility=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.modified_time = modified_time  # type: str
        self.region_id = region_id  # type: str
        self.stage_name = stage_name  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApisByRuleResponseBodyApiInfosApiInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisByRuleResponseBodyApiInfos(TeaModel):
    def __init__(self, api_info=None):
        self.api_info = api_info  # type: list[DescribeApisByRuleResponseBodyApiInfosApiInfo]

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApisByRuleResponseBodyApiInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeApisByRuleResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApisByRuleResponseBody(TeaModel):
    def __init__(self, api_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.api_infos = api_infos  # type: DescribeApisByRuleResponseBodyApiInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super(DescribeApisByRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
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
        if m.get('ApiInfos') is not None:
            temp_model = DescribeApisByRuleResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApisByRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApisByRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApisByRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApisByRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisForConsoleRequest(TeaModel):
    def __init__(self, api_id=None, api_name=None, group_id=None, page_number=None, page_size=None,
                 security_token=None, stage_name=None, visibility=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApisForConsoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfosDeployedInfo(TeaModel):
    def __init__(self, deployed_status=None, effective_version=None, stage_name=None):
        self.deployed_status = deployed_status  # type: str
        self.effective_version = effective_version  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfosDeployedInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployed_status is not None:
            result['DeployedStatus'] = self.deployed_status
        if self.effective_version is not None:
            result['EffectiveVersion'] = self.effective_version
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployedStatus') is not None:
            self.deployed_status = m.get('DeployedStatus')
        if m.get('EffectiveVersion') is not None:
            self.effective_version = m.get('EffectiveVersion')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfos(TeaModel):
    def __init__(self, deployed_info=None):
        self.deployed_info = deployed_info  # type: list[DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfosDeployedInfo]

    def validate(self):
        if self.deployed_info:
            for k in self.deployed_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeployedInfo'] = []
        if self.deployed_info is not None:
            for k in self.deployed_info:
                result['DeployedInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.deployed_info = []
        if m.get('DeployedInfo') is not None:
            for k in m.get('DeployedInfo'):
                temp_model = DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfosDeployedInfo()
                self.deployed_info.append(temp_model.from_map(k))
        return self


class DescribeApisForConsoleResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(self, api_id=None, api_name=None, created_time=None, deployed_infos=None, description=None,
                 group_id=None, group_name=None, modified_time=None, region_id=None, visibility=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.created_time = created_time  # type: str
        self.deployed_infos = deployed_infos  # type: DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfos
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.modified_time = modified_time  # type: str
        self.region_id = region_id  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        if self.deployed_infos:
            self.deployed_infos.validate()

    def to_map(self):
        _map = super(DescribeApisForConsoleResponseBodyApiInfosApiInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.deployed_infos is not None:
            result['DeployedInfos'] = self.deployed_infos.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DeployedInfos') is not None:
            temp_model = DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfos()
            self.deployed_infos = temp_model.from_map(m['DeployedInfos'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisForConsoleResponseBodyApiInfos(TeaModel):
    def __init__(self, api_info=None):
        self.api_info = api_info  # type: list[DescribeApisForConsoleResponseBodyApiInfosApiInfo]

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApisForConsoleResponseBodyApiInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeApisForConsoleResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApisForConsoleResponseBody(TeaModel):
    def __init__(self, api_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.api_infos = api_infos  # type: DescribeApisForConsoleResponseBodyApiInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super(DescribeApisForConsoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
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
        if m.get('ApiInfos') is not None:
            temp_model = DescribeApisForConsoleResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApisForConsoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApisForConsoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApisForConsoleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApisForConsoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppRequest(TeaModel):
    def __init__(self, app_id=None, security_token=None):
        self.app_id = app_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAppResponseBody(TeaModel):
    def __init__(self, app_id=None, app_name=None, created_time=None, description=None, modified_time=None,
                 request_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppSecuritiesRequest(TeaModel):
    def __init__(self, app_id=None, security_token=None):
        self.app_id = app_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppSecuritiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAppSecuritiesResponseBodyAppSecuritysAppSecurity(TeaModel):
    def __init__(self, app_code=None, app_key=None, app_secret=None, created_time=None, modified_time=None):
        self.app_code = app_code  # type: str
        self.app_key = app_key  # type: str
        self.app_secret = app_secret  # type: str
        self.created_time = created_time  # type: str
        self.modified_time = modified_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppSecuritiesResponseBodyAppSecuritysAppSecurity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class DescribeAppSecuritiesResponseBodyAppSecuritys(TeaModel):
    def __init__(self, app_security=None):
        self.app_security = app_security  # type: list[DescribeAppSecuritiesResponseBodyAppSecuritysAppSecurity]

    def validate(self):
        if self.app_security:
            for k in self.app_security:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppSecuritiesResponseBodyAppSecuritys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppSecurity'] = []
        if self.app_security is not None:
            for k in self.app_security:
                result['AppSecurity'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_security = []
        if m.get('AppSecurity') is not None:
            for k in m.get('AppSecurity'):
                temp_model = DescribeAppSecuritiesResponseBodyAppSecuritysAppSecurity()
                self.app_security.append(temp_model.from_map(k))
        return self


class DescribeAppSecuritiesResponseBody(TeaModel):
    def __init__(self, app_securitys=None, request_id=None):
        self.app_securitys = app_securitys  # type: DescribeAppSecuritiesResponseBodyAppSecuritys
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_securitys:
            self.app_securitys.validate()

    def to_map(self):
        _map = super(DescribeAppSecuritiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_securitys is not None:
            result['AppSecuritys'] = self.app_securitys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppSecuritys') is not None:
            temp_model = DescribeAppSecuritiesResponseBodyAppSecuritys()
            self.app_securitys = temp_model.from_map(m['AppSecuritys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppSecuritiesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppSecuritiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppSecuritiesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppSecuritiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppSecurityRequest(TeaModel):
    def __init__(self, app_key=None, security_token=None):
        self.app_key = app_key  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppSecurityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAppSecurityResponseBody(TeaModel):
    def __init__(self, app_code=None, app_key=None, app_secret=None, created_time=None, modified_time=None,
                 request_id=None):
        self.app_code = app_code  # type: str
        self.app_key = app_key  # type: str
        self.app_secret = app_secret  # type: str
        self.created_time = created_time  # type: str
        self.modified_time = modified_time  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppSecurityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppSecurityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppSecurityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppSecurityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppSecurityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsRequestTag, self).to_map()
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


class DescribeAppsRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None, enable_tag_auth=None, page_number=None, page_size=None,
                 security_token=None, tag=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.enable_tag_auth = enable_tag_auth  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.tag = tag  # type: list[DescribeAppsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.enable_tag_auth is not None:
            result['EnableTagAuth'] = self.enable_tag_auth
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('EnableTagAuth') is not None:
            self.enable_tag_auth = m.get('EnableTagAuth')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeAppsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeAppsResponseBodyAppsApp(TeaModel):
    def __init__(self, app_id=None, app_name=None, created_time=None, description=None, modified_time=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsResponseBodyAppsApp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class DescribeAppsResponseBodyApps(TeaModel):
    def __init__(self, app=None):
        self.app = app  # type: list[DescribeAppsResponseBodyAppsApp]

    def validate(self):
        if self.app:
            for k in self.app:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppsResponseBodyApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['App'] = []
        if self.app is not None:
            for k in self.app:
                result['App'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app = []
        if m.get('App') is not None:
            for k in m.get('App'):
                temp_model = DescribeAppsResponseBodyAppsApp()
                self.app.append(temp_model.from_map(k))
        return self


class DescribeAppsResponseBody(TeaModel):
    def __init__(self, apps=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.apps = apps  # type: DescribeAppsResponseBodyApps
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.apps:
            self.apps.validate()

    def to_map(self):
        _map = super(DescribeAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apps is not None:
            result['Apps'] = self.apps.to_map()
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
        if m.get('Apps') is not None:
            temp_model = DescribeAppsResponseBodyApps()
            self.apps = temp_model.from_map(m['Apps'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsByApiRequest(TeaModel):
    def __init__(self, api_id=None, app_id=None, app_name=None, app_owner_id=None, group_id=None, page_number=None,
                 page_size=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.app_owner_id = app_owner_id  # type: long
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsByApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_owner_id is not None:
            result['AppOwnerId'] = self.app_owner_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppOwnerId') is not None:
            self.app_owner_id = m.get('AppOwnerId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeAppsByApiResponseBodyAppApiRelationInfosAppApiRelationInfo(TeaModel):
    def __init__(self, app_id=None, app_name=None, auth_vaild_time=None, authorization_source=None,
                 created_time=None, description=None, operator=None, stage_name=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.auth_vaild_time = auth_vaild_time  # type: str
        self.authorization_source = authorization_source  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.operator = operator  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsByApiResponseBodyAppApiRelationInfosAppApiRelationInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_vaild_time is not None:
            result['AuthVaildTime'] = self.auth_vaild_time
        if self.authorization_source is not None:
            result['AuthorizationSource'] = self.authorization_source
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthVaildTime') is not None:
            self.auth_vaild_time = m.get('AuthVaildTime')
        if m.get('AuthorizationSource') is not None:
            self.authorization_source = m.get('AuthorizationSource')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeAppsByApiResponseBodyAppApiRelationInfos(TeaModel):
    def __init__(self, app_api_relation_info=None):
        self.app_api_relation_info = app_api_relation_info  # type: list[DescribeAppsByApiResponseBodyAppApiRelationInfosAppApiRelationInfo]

    def validate(self):
        if self.app_api_relation_info:
            for k in self.app_api_relation_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppsByApiResponseBodyAppApiRelationInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppApiRelationInfo'] = []
        if self.app_api_relation_info is not None:
            for k in self.app_api_relation_info:
                result['AppApiRelationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_api_relation_info = []
        if m.get('AppApiRelationInfo') is not None:
            for k in m.get('AppApiRelationInfo'):
                temp_model = DescribeAppsByApiResponseBodyAppApiRelationInfosAppApiRelationInfo()
                self.app_api_relation_info.append(temp_model.from_map(k))
        return self


class DescribeAppsByApiResponseBody(TeaModel):
    def __init__(self, app_api_relation_infos=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.app_api_relation_infos = app_api_relation_infos  # type: DescribeAppsByApiResponseBodyAppApiRelationInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.app_api_relation_infos:
            self.app_api_relation_infos.validate()

    def to_map(self):
        _map = super(DescribeAppsByApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_api_relation_infos is not None:
            result['AppApiRelationInfos'] = self.app_api_relation_infos.to_map()
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
        if m.get('AppApiRelationInfos') is not None:
            temp_model = DescribeAppsByApiResponseBodyAppApiRelationInfos()
            self.app_api_relation_infos = temp_model.from_map(m['AppApiRelationInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppsByApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppsByApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppsByApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppsByApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsForProviderRequest(TeaModel):
    def __init__(self, app_id=None, app_owner_id=None, page_number=None, page_size=None, security_token=None):
        self.app_id = app_id  # type: long
        self.app_owner_id = app_owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsForProviderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_owner_id is not None:
            result['AppOwnerId'] = self.app_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppOwnerId') is not None:
            self.app_owner_id = m.get('AppOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAppsForProviderResponseBodyAppsApp(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, description=None, modified_time=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsForProviderResponseBodyAppsApp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class DescribeAppsForProviderResponseBodyApps(TeaModel):
    def __init__(self, app=None):
        self.app = app  # type: list[DescribeAppsForProviderResponseBodyAppsApp]

    def validate(self):
        if self.app:
            for k in self.app:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppsForProviderResponseBodyApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['App'] = []
        if self.app is not None:
            for k in self.app:
                result['App'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app = []
        if m.get('App') is not None:
            for k in m.get('App'):
                temp_model = DescribeAppsForProviderResponseBodyAppsApp()
                self.app.append(temp_model.from_map(k))
        return self


class DescribeAppsForProviderResponseBody(TeaModel):
    def __init__(self, apps=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.apps = apps  # type: DescribeAppsForProviderResponseBodyApps
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.apps:
            self.apps.validate()

    def to_map(self):
        _map = super(DescribeAppsForProviderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apps is not None:
            result['Apps'] = self.apps.to_map()
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
        if m.get('Apps') is not None:
            temp_model = DescribeAppsForProviderResponseBodyApps()
            self.apps = temp_model.from_map(m['Apps'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppsForProviderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppsForProviderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppsForProviderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppsForProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlackListsRequest(TeaModel):
    def __init__(self, black_type=None, page_number=None, page_size=None, security_token=None):
        self.black_type = black_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBlackListsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeBlackListsResponseBodyBlackListsBlackList(TeaModel):
    def __init__(self, black_content=None, black_type=None, create_time=None, description=None, modified_time=None):
        self.black_content = black_content  # type: str
        self.black_type = black_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBlackListsResponseBodyBlackListsBlackList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_content is not None:
            result['BlackContent'] = self.black_content
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackContent') is not None:
            self.black_content = m.get('BlackContent')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class DescribeBlackListsResponseBodyBlackLists(TeaModel):
    def __init__(self, black_list=None):
        self.black_list = black_list  # type: list[DescribeBlackListsResponseBodyBlackListsBlackList]

    def validate(self):
        if self.black_list:
            for k in self.black_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBlackListsResponseBodyBlackLists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlackList'] = []
        if self.black_list is not None:
            for k in self.black_list:
                result['BlackList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.black_list = []
        if m.get('BlackList') is not None:
            for k in m.get('BlackList'):
                temp_model = DescribeBlackListsResponseBodyBlackListsBlackList()
                self.black_list.append(temp_model.from_map(k))
        return self


class DescribeBlackListsResponseBody(TeaModel):
    def __init__(self, black_lists=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.black_lists = black_lists  # type: DescribeBlackListsResponseBodyBlackLists
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.black_lists:
            self.black_lists.validate()

    def to_map(self):
        _map = super(DescribeBlackListsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_lists is not None:
            result['BlackLists'] = self.black_lists.to_map()
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
        if m.get('BlackLists') is not None:
            temp_model = DescribeBlackListsResponseBodyBlackLists()
            self.black_lists = temp_model.from_map(m['BlackLists'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBlackListsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBlackListsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBlackListsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBlackListsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeployedApiRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeDeployedApiResponseBodyConstantParametersConstantParameter(TeaModel):
    def __init__(self, constant_value=None, description=None, location=None, service_parameter_name=None):
        self.constant_value = constant_value  # type: str
        self.description = description  # type: str
        self.location = location  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyConstantParametersConstantParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constant_value is not None:
            result['ConstantValue'] = self.constant_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConstantValue') is not None:
            self.constant_value = m.get('ConstantValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyConstantParameters(TeaModel):
    def __init__(self, constant_parameter=None):
        self.constant_parameter = constant_parameter  # type: list[DescribeDeployedApiResponseBodyConstantParametersConstantParameter]

    def validate(self):
        if self.constant_parameter:
            for k in self.constant_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyConstantParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConstantParameter'] = []
        if self.constant_parameter is not None:
            for k in self.constant_parameter:
                result['ConstantParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.constant_parameter = []
        if m.get('ConstantParameter') is not None:
            for k in m.get('ConstantParameter'):
                temp_model = DescribeDeployedApiResponseBodyConstantParametersConstantParameter()
                self.constant_parameter.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyErrorCodeSamplesErrorCodeSample(TeaModel):
    def __init__(self, code=None, description=None, message=None):
        self.code = code  # type: str
        self.description = description  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyErrorCodeSamplesErrorCodeSample, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeDeployedApiResponseBodyErrorCodeSamples(TeaModel):
    def __init__(self, error_code_sample=None):
        self.error_code_sample = error_code_sample  # type: list[DescribeDeployedApiResponseBodyErrorCodeSamplesErrorCodeSample]

    def validate(self):
        if self.error_code_sample:
            for k in self.error_code_sample:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyErrorCodeSamples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorCodeSample'] = []
        if self.error_code_sample is not None:
            for k in self.error_code_sample:
                result['ErrorCodeSample'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.error_code_sample = []
        if m.get('ErrorCodeSample') is not None:
            for k in m.get('ErrorCodeSample'):
                temp_model = DescribeDeployedApiResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyFunctionComputeConfig(TeaModel):
    def __init__(self, fc_region_id=None, function_name=None, role_arn=None, service_name=None):
        self.fc_region_id = fc_region_id  # type: str
        self.function_name = function_name  # type: str
        self.role_arn = role_arn  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyFunctionComputeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fc_region_id is not None:
            result['FcRegionId'] = self.fc_region_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FcRegionId') is not None:
            self.fc_region_id = m.get('FcRegionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeDeployedApiResponseBodyPathParametersPathParameter(TeaModel):
    def __init__(self, api_parameter_name=None, demo_value=None, description=None, service_parameter_name=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyPathParametersPathParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyPathParameters(TeaModel):
    def __init__(self, path_parameter=None):
        self.path_parameter = path_parameter  # type: list[DescribeDeployedApiResponseBodyPathParametersPathParameter]

    def validate(self):
        if self.path_parameter:
            for k in self.path_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyPathParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PathParameter'] = []
        if self.path_parameter is not None:
            for k in self.path_parameter:
                result['PathParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.path_parameter = []
        if m.get('PathParameter') is not None:
            for k in m.get('PathParameter'):
                temp_model = DescribeDeployedApiResponseBodyPathParametersPathParameter()
                self.path_parameter.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyRequestBodyRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, array_items_type=None, default_value=None, demo_value=None,
                 description=None, doc_order=None, doc_show=None, enum_value=None, json_scheme=None, max_length=None,
                 max_value=None, min_length=None, min_value=None, parameter_type=None, regular_expression=None, required=None,
                 service_parameter_name=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.array_items_type = array_items_type  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.doc_order = doc_order  # type: str
        self.doc_show = doc_show  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyRequestBodyRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyRequestBody(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribeDeployedApiResponseBodyRequestBodyRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeDeployedApiResponseBodyRequestBodyRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyRequestHeadersRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, array_items_type=None, default_value=None, demo_value=None,
                 description=None, doc_order=None, doc_show=None, enum_value=None, json_scheme=None, max_length=None,
                 max_value=None, min_length=None, min_value=None, parameter_type=None, regular_expression=None, required=None,
                 service_parameter_name=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.array_items_type = array_items_type  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.doc_order = doc_order  # type: str
        self.doc_show = doc_show  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyRequestHeadersRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyRequestHeaders(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribeDeployedApiResponseBodyRequestHeadersRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyRequestHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeDeployedApiResponseBodyRequestHeadersRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyRequestQueriesRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, array_items_type=None, default_value=None, demo_value=None,
                 description=None, doc_order=None, doc_show=None, enum_value=None, json_scheme=None, max_length=None,
                 max_value=None, min_length=None, min_value=None, parameter_type=None, regular_expression=None, required=None,
                 service_parameter_name=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.array_items_type = array_items_type  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.doc_order = doc_order  # type: str
        self.doc_show = doc_show  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyRequestQueriesRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyRequestQueries(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribeDeployedApiResponseBodyRequestQueriesRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodyRequestQueries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeDeployedApiResponseBodyRequestQueriesRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodySystemParametersSystemParameter(TeaModel):
    def __init__(self, demo_value=None, description=None, location=None, parameter_name=None,
                 service_parameter_name=None):
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.location = location  # type: str
        self.parameter_name = parameter_name  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodySystemParametersSystemParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodySystemParameters(TeaModel):
    def __init__(self, system_parameter=None):
        self.system_parameter = system_parameter  # type: list[DescribeDeployedApiResponseBodySystemParametersSystemParameter]

    def validate(self):
        if self.system_parameter:
            for k in self.system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBodySystemParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParameter'] = []
        if self.system_parameter is not None:
            for k in self.system_parameter:
                result['SystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.system_parameter = []
        if m.get('SystemParameter') is not None:
            for k in m.get('SystemParameter'):
                temp_model = DescribeDeployedApiResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBody(TeaModel):
    def __init__(self, api_id=None, api_name=None, auth_type=None, body_format=None, constant_parameters=None,
                 deployed_time=None, disable_internet=None, error_code_samples=None, fail_result_sample=None,
                 force_nonce_check=None, function_compute_config=None, group_id=None, group_name=None, http_method=None,
                 http_protocol=None, path=None, path_parameters=None, post_body_description=None, post_body_type=None,
                 region_id=None, request_body=None, request_headers=None, request_id=None, request_mode=None,
                 request_queries=None, result_sample=None, result_type=None, service_address=None, service_fcenable=None,
                 service_protocol=None, service_timeout=None, service_vpc_enable=None, stage_name=None, system_parameters=None,
                 visibility=None, vpc_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.auth_type = auth_type  # type: str
        self.body_format = body_format  # type: str
        self.constant_parameters = constant_parameters  # type: DescribeDeployedApiResponseBodyConstantParameters
        self.deployed_time = deployed_time  # type: str
        self.disable_internet = disable_internet  # type: bool
        self.error_code_samples = error_code_samples  # type: DescribeDeployedApiResponseBodyErrorCodeSamples
        self.fail_result_sample = fail_result_sample  # type: str
        self.force_nonce_check = force_nonce_check  # type: bool
        self.function_compute_config = function_compute_config  # type: DescribeDeployedApiResponseBodyFunctionComputeConfig
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.http_method = http_method  # type: str
        self.http_protocol = http_protocol  # type: str
        self.path = path  # type: str
        self.path_parameters = path_parameters  # type: DescribeDeployedApiResponseBodyPathParameters
        self.post_body_description = post_body_description  # type: str
        self.post_body_type = post_body_type  # type: str
        self.region_id = region_id  # type: str
        self.request_body = request_body  # type: DescribeDeployedApiResponseBodyRequestBody
        self.request_headers = request_headers  # type: DescribeDeployedApiResponseBodyRequestHeaders
        self.request_id = request_id  # type: str
        self.request_mode = request_mode  # type: str
        self.request_queries = request_queries  # type: DescribeDeployedApiResponseBodyRequestQueries
        self.result_sample = result_sample  # type: str
        self.result_type = result_type  # type: str
        self.service_address = service_address  # type: str
        self.service_fcenable = service_fcenable  # type: str
        self.service_protocol = service_protocol  # type: str
        self.service_timeout = service_timeout  # type: int
        self.service_vpc_enable = service_vpc_enable  # type: str
        self.stage_name = stage_name  # type: str
        self.system_parameters = system_parameters  # type: DescribeDeployedApiResponseBodySystemParameters
        self.visibility = visibility  # type: str
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.constant_parameters:
            self.constant_parameters.validate()
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.function_compute_config:
            self.function_compute_config.validate()
        if self.path_parameters:
            self.path_parameters.validate()
        if self.request_body:
            self.request_body.validate()
        if self.request_headers:
            self.request_headers.validate()
        if self.request_queries:
            self.request_queries.validate()
        if self.system_parameters:
            self.system_parameters.validate()

    def to_map(self):
        _map = super(DescribeDeployedApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters.to_map()
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check
        if self.function_compute_config is not None:
            result['FunctionComputeConfig'] = self.function_compute_config.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.http_protocol is not None:
            result['HttpProtocol'] = self.http_protocol
        if self.path is not None:
            result['Path'] = self.path
        if self.path_parameters is not None:
            result['PathParameters'] = self.path_parameters.to_map()
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.post_body_type is not None:
            result['PostBodyType'] = self.post_body_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_body is not None:
            result['RequestBody'] = self.request_body.to_map()
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_address is not None:
            result['ServiceAddress'] = self.service_address
        if self.service_fcenable is not None:
            result['ServiceFCEnable'] = self.service_fcenable
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.service_vpc_enable is not None:
            result['ServiceVpcEnable'] = self.service_vpc_enable
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters.to_map()
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('ConstantParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodyConstantParameters()
            self.constant_parameters = temp_model.from_map(m['ConstantParameters'])
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeDeployedApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
        if m.get('FunctionComputeConfig') is not None:
            temp_model = DescribeDeployedApiResponseBodyFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m['FunctionComputeConfig'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('HttpProtocol') is not None:
            self.http_protocol = m.get('HttpProtocol')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodyPathParameters()
            self.path_parameters = temp_model.from_map(m['PathParameters'])
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('PostBodyType') is not None:
            self.post_body_type = m.get('PostBodyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestBody') is not None:
            temp_model = DescribeDeployedApiResponseBodyRequestBody()
            self.request_body = temp_model.from_map(m['RequestBody'])
        if m.get('RequestHeaders') is not None:
            temp_model = DescribeDeployedApiResponseBodyRequestHeaders()
            self.request_headers = temp_model.from_map(m['RequestHeaders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')
        if m.get('RequestQueries') is not None:
            temp_model = DescribeDeployedApiResponseBodyRequestQueries()
            self.request_queries = temp_model.from_map(m['RequestQueries'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceAddress') is not None:
            self.service_address = m.get('ServiceAddress')
        if m.get('ServiceFCEnable') is not None:
            self.service_fcenable = m.get('ServiceFCEnable')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('ServiceVpcEnable') is not None:
            self.service_vpc_enable = m.get('ServiceVpcEnable')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('SystemParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m['SystemParameters'])
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeDeployedApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDeployedApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeployedApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDeployedApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeployedApisRequest(TeaModel):
    def __init__(self, api_id=None, api_name=None, group_id=None, page_number=None, page_size=None,
                 security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeDeployedApisResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(self, api_id=None, api_name=None, deployed_time=None, description=None, group_id=None,
                 group_name=None, region_id=None, stage_name=None, visibility=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.deployed_time = deployed_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.region_id = region_id  # type: str
        self.stage_name = stage_name  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployedApisResponseBodyApiInfosApiInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeDeployedApisResponseBodyApiInfos(TeaModel):
    def __init__(self, api_info=None):
        self.api_info = api_info  # type: list[DescribeDeployedApisResponseBodyApiInfosApiInfo]

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeployedApisResponseBodyApiInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeDeployedApisResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeDeployedApisResponseBody(TeaModel):
    def __init__(self, api_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.api_infos = api_infos  # type: DescribeDeployedApisResponseBodyApiInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super(DescribeDeployedApisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
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
        if m.get('ApiInfos') is not None:
            temp_model = DescribeDeployedApisResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDeployedApisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDeployedApisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeployedApisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDeployedApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRequest(TeaModel):
    def __init__(self, domain_name=None, group_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDomainResponseBody(TeaModel):
    def __init__(self, certificate_body=None, certificate_id=None, certificate_name=None,
                 domain_binding_status=None, domain_legal_status=None, domain_name=None, domain_name_resolution=None, domain_remark=None,
                 domain_web_socket_status=None, group_id=None, private_key=None, request_id=None, sub_domain=None):
        self.certificate_body = certificate_body  # type: str
        self.certificate_id = certificate_id  # type: str
        self.certificate_name = certificate_name  # type: str
        self.domain_binding_status = domain_binding_status  # type: str
        self.domain_legal_status = domain_legal_status  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_name_resolution = domain_name_resolution  # type: str
        self.domain_remark = domain_remark  # type: str
        self.domain_web_socket_status = domain_web_socket_status  # type: str
        self.group_id = group_id  # type: str
        self.private_key = private_key  # type: str
        self.request_id = request_id  # type: str
        self.sub_domain = sub_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_body is not None:
            result['CertificateBody'] = self.certificate_body
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_binding_status is not None:
            result['DomainBindingStatus'] = self.domain_binding_status
        if self.domain_legal_status is not None:
            result['DomainLegalStatus'] = self.domain_legal_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        if self.domain_remark is not None:
            result['DomainRemark'] = self.domain_remark
        if self.domain_web_socket_status is not None:
            result['DomainWebSocketStatus'] = self.domain_web_socket_status
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateBody') is not None:
            self.certificate_body = m.get('CertificateBody')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainBindingStatus') is not None:
            self.domain_binding_status = m.get('DomainBindingStatus')
        if m.get('DomainLegalStatus') is not None:
            self.domain_legal_status = m.get('DomainLegalStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        if m.get('DomainRemark') is not None:
            self.domain_remark = m.get('DomainRemark')
        if m.get('DomainWebSocketStatus') is not None:
            self.domain_web_socket_status = m.get('DomainWebSocketStatus')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class DescribeDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainResolutionRequest(TeaModel):
    def __init__(self, domain_names=None, group_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainResolutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDomainResolutionResponseBodyDomainResolutionsDomainResolution(TeaModel):
    def __init__(self, domain_name=None, domain_name_resolution=None):
        self.domain_name = domain_name  # type: str
        self.domain_name_resolution = domain_name_resolution  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainResolutionResponseBodyDomainResolutionsDomainResolution, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        return self


class DescribeDomainResolutionResponseBodyDomainResolutions(TeaModel):
    def __init__(self, domain_resolution=None):
        self.domain_resolution = domain_resolution  # type: list[DescribeDomainResolutionResponseBodyDomainResolutionsDomainResolution]

    def validate(self):
        if self.domain_resolution:
            for k in self.domain_resolution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainResolutionResponseBodyDomainResolutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainResolution'] = []
        if self.domain_resolution is not None:
            for k in self.domain_resolution:
                result['DomainResolution'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_resolution = []
        if m.get('DomainResolution') is not None:
            for k in m.get('DomainResolution'):
                temp_model = DescribeDomainResolutionResponseBodyDomainResolutionsDomainResolution()
                self.domain_resolution.append(temp_model.from_map(k))
        return self


class DescribeDomainResolutionResponseBody(TeaModel):
    def __init__(self, domain_resolutions=None, group_id=None, request_id=None):
        self.domain_resolutions = domain_resolutions  # type: DescribeDomainResolutionResponseBodyDomainResolutions
        self.group_id = group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_resolutions:
            self.domain_resolutions.validate()

    def to_map(self):
        _map = super(DescribeDomainResolutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_resolutions is not None:
            result['DomainResolutions'] = self.domain_resolutions.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainResolutions') is not None:
            temp_model = DescribeDomainResolutionResponseBodyDomainResolutions()
            self.domain_resolutions = temp_model.from_map(m['DomainResolutions'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainResolutionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainResolutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainResolutionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDomainResolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHistoryApiRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, history_version=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.history_version = history_version  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeHistoryApiResponseBodyConstantParametersConstantParameter(TeaModel):
    def __init__(self, constant_value=None, description=None, location=None, service_parameter_name=None):
        self.constant_value = constant_value  # type: str
        self.description = description  # type: str
        self.location = location  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyConstantParametersConstantParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constant_value is not None:
            result['ConstantValue'] = self.constant_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConstantValue') is not None:
            self.constant_value = m.get('ConstantValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyConstantParameters(TeaModel):
    def __init__(self, constant_parameter=None):
        self.constant_parameter = constant_parameter  # type: list[DescribeHistoryApiResponseBodyConstantParametersConstantParameter]

    def validate(self):
        if self.constant_parameter:
            for k in self.constant_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyConstantParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConstantParameter'] = []
        if self.constant_parameter is not None:
            for k in self.constant_parameter:
                result['ConstantParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.constant_parameter = []
        if m.get('ConstantParameter') is not None:
            for k in m.get('ConstantParameter'):
                temp_model = DescribeHistoryApiResponseBodyConstantParametersConstantParameter()
                self.constant_parameter.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyCustomSystemParametersCustomSystemParameter(TeaModel):
    def __init__(self, demo_value=None, description=None, location=None, parameter_name=None,
                 service_parameter_name=None):
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.location = location  # type: str
        self.parameter_name = parameter_name  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyCustomSystemParametersCustomSystemParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyCustomSystemParameters(TeaModel):
    def __init__(self, custom_system_parameter=None):
        self.custom_system_parameter = custom_system_parameter  # type: list[DescribeHistoryApiResponseBodyCustomSystemParametersCustomSystemParameter]

    def validate(self):
        if self.custom_system_parameter:
            for k in self.custom_system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyCustomSystemParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomSystemParameter'] = []
        if self.custom_system_parameter is not None:
            for k in self.custom_system_parameter:
                result['CustomSystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_system_parameter = []
        if m.get('CustomSystemParameter') is not None:
            for k in m.get('CustomSystemParameter'):
                temp_model = DescribeHistoryApiResponseBodyCustomSystemParametersCustomSystemParameter()
                self.custom_system_parameter.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyErrorCodeSamplesErrorCodeSample(TeaModel):
    def __init__(self, code=None, description=None, message=None):
        self.code = code  # type: str
        self.description = description  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyErrorCodeSamplesErrorCodeSample, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeHistoryApiResponseBodyErrorCodeSamples(TeaModel):
    def __init__(self, error_code_sample=None):
        self.error_code_sample = error_code_sample  # type: list[DescribeHistoryApiResponseBodyErrorCodeSamplesErrorCodeSample]

    def validate(self):
        if self.error_code_sample:
            for k in self.error_code_sample:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyErrorCodeSamples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorCodeSample'] = []
        if self.error_code_sample is not None:
            for k in self.error_code_sample:
                result['ErrorCodeSample'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.error_code_sample = []
        if m.get('ErrorCodeSample') is not None:
            for k in m.get('ErrorCodeSample'):
                temp_model = DescribeHistoryApiResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyFunctionComputeConfig(TeaModel):
    def __init__(self, fc_region_id=None, function_name=None, role_arn=None, service_name=None):
        self.fc_region_id = fc_region_id  # type: str
        self.function_name = function_name  # type: str
        self.role_arn = role_arn  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyFunctionComputeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fc_region_id is not None:
            result['FcRegionId'] = self.fc_region_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FcRegionId') is not None:
            self.fc_region_id = m.get('FcRegionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeHistoryApiResponseBodyOpenIdConnectConfig(TeaModel):
    def __init__(self, id_token_param_name=None, open_id_api_type=None, public_key=None, public_key_id=None):
        self.id_token_param_name = id_token_param_name  # type: str
        self.open_id_api_type = open_id_api_type  # type: str
        self.public_key = public_key  # type: str
        self.public_key_id = public_key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyOpenIdConnectConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_token_param_name is not None:
            result['IdTokenParamName'] = self.id_token_param_name
        if self.open_id_api_type is not None:
            result['OpenIdApiType'] = self.open_id_api_type
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdTokenParamName') is not None:
            self.id_token_param_name = m.get('IdTokenParamName')
        if m.get('OpenIdApiType') is not None:
            self.open_id_api_type = m.get('OpenIdApiType')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')
        return self


class DescribeHistoryApiResponseBodyPathParametersPathParameter(TeaModel):
    def __init__(self, api_parameter_name=None, demo_value=None, description=None, service_parameter_name=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyPathParametersPathParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyPathParameters(TeaModel):
    def __init__(self, path_parameter=None):
        self.path_parameter = path_parameter  # type: list[DescribeHistoryApiResponseBodyPathParametersPathParameter]

    def validate(self):
        if self.path_parameter:
            for k in self.path_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyPathParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PathParameter'] = []
        if self.path_parameter is not None:
            for k in self.path_parameter:
                result['PathParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.path_parameter = []
        if m.get('PathParameter') is not None:
            for k in m.get('PathParameter'):
                temp_model = DescribeHistoryApiResponseBodyPathParametersPathParameter()
                self.path_parameter.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyRequestBodyRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, array_items_type=None, default_value=None, demo_value=None,
                 description=None, doc_order=None, doc_show=None, enum_value=None, json_scheme=None, max_length=None,
                 max_value=None, min_length=None, min_value=None, parameter_type=None, regular_expression=None, required=None,
                 service_parameter_name=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.array_items_type = array_items_type  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.doc_order = doc_order  # type: str
        self.doc_show = doc_show  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyRequestBodyRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyRequestBody(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribeHistoryApiResponseBodyRequestBodyRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeHistoryApiResponseBodyRequestBodyRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyRequestHeadersRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, array_items_type=None, default_value=None, demo_value=None,
                 description=None, doc_order=None, doc_show=None, enum_value=None, json_scheme=None, max_length=None,
                 max_value=None, min_length=None, min_value=None, parameter_type=None, regular_expression=None, required=None,
                 service_parameter_name=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.array_items_type = array_items_type  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.doc_order = doc_order  # type: str
        self.doc_show = doc_show  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyRequestHeadersRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyRequestHeaders(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribeHistoryApiResponseBodyRequestHeadersRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyRequestHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeHistoryApiResponseBodyRequestHeadersRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyRequestQueriesRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, array_items_type=None, default_value=None, demo_value=None,
                 description=None, doc_order=None, doc_show=None, enum_value=None, json_scheme=None, max_length=None,
                 max_value=None, min_length=None, min_value=None, parameter_type=None, regular_expression=None, required=None,
                 service_parameter_name=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.array_items_type = array_items_type  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.doc_order = doc_order  # type: str
        self.doc_show = doc_show  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyRequestQueriesRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyRequestQueries(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribeHistoryApiResponseBodyRequestQueriesRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodyRequestQueries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeHistoryApiResponseBodyRequestQueriesRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodySystemParametersSystemParameter(TeaModel):
    def __init__(self, demo_value=None, description=None, location=None, parameter_name=None,
                 service_parameter_name=None):
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.location = location  # type: str
        self.parameter_name = parameter_name  # type: str
        self.service_parameter_name = service_parameter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodySystemParametersSystemParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodySystemParameters(TeaModel):
    def __init__(self, system_parameter=None):
        self.system_parameter = system_parameter  # type: list[DescribeHistoryApiResponseBodySystemParametersSystemParameter]

    def validate(self):
        if self.system_parameter:
            for k in self.system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBodySystemParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParameter'] = []
        if self.system_parameter is not None:
            for k in self.system_parameter:
                result['SystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.system_parameter = []
        if m.get('SystemParameter') is not None:
            for k in m.get('SystemParameter'):
                temp_model = DescribeHistoryApiResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBody(TeaModel):
    def __init__(self, allow_signature_method=None, api_id=None, api_name=None, auth_type=None, body_format=None,
                 constant_parameters=None, custom_system_parameters=None, deployed_time=None, description=None,
                 error_code_samples=None, fail_result_sample=None, function_compute_config=None, group_id=None, group_name=None,
                 history_version=None, http_method=None, http_protocol=None, mock=None, mock_result=None,
                 open_id_connect_config=None, origin_result_description=None, path=None, path_parameters=None, post_body_description=None,
                 post_body_type=None, region_id=None, request_body=None, request_headers=None, request_id=None, request_mode=None,
                 request_queries=None, result_sample=None, result_type=None, service_address=None, service_fcenable=None,
                 service_protocol=None, service_timeout=None, service_vpc_enable=None, status=None, system_parameters=None,
                 visibility=None, vpc_name=None):
        self.allow_signature_method = allow_signature_method  # type: str
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.auth_type = auth_type  # type: str
        self.body_format = body_format  # type: str
        self.constant_parameters = constant_parameters  # type: DescribeHistoryApiResponseBodyConstantParameters
        self.custom_system_parameters = custom_system_parameters  # type: DescribeHistoryApiResponseBodyCustomSystemParameters
        self.deployed_time = deployed_time  # type: str
        self.description = description  # type: str
        self.error_code_samples = error_code_samples  # type: DescribeHistoryApiResponseBodyErrorCodeSamples
        self.fail_result_sample = fail_result_sample  # type: str
        self.function_compute_config = function_compute_config  # type: DescribeHistoryApiResponseBodyFunctionComputeConfig
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.history_version = history_version  # type: str
        self.http_method = http_method  # type: str
        self.http_protocol = http_protocol  # type: str
        self.mock = mock  # type: str
        self.mock_result = mock_result  # type: str
        self.open_id_connect_config = open_id_connect_config  # type: DescribeHistoryApiResponseBodyOpenIdConnectConfig
        self.origin_result_description = origin_result_description  # type: str
        self.path = path  # type: str
        self.path_parameters = path_parameters  # type: DescribeHistoryApiResponseBodyPathParameters
        self.post_body_description = post_body_description  # type: str
        self.post_body_type = post_body_type  # type: str
        self.region_id = region_id  # type: str
        self.request_body = request_body  # type: DescribeHistoryApiResponseBodyRequestBody
        self.request_headers = request_headers  # type: DescribeHistoryApiResponseBodyRequestHeaders
        self.request_id = request_id  # type: str
        self.request_mode = request_mode  # type: str
        self.request_queries = request_queries  # type: DescribeHistoryApiResponseBodyRequestQueries
        self.result_sample = result_sample  # type: str
        self.result_type = result_type  # type: str
        self.service_address = service_address  # type: str
        self.service_fcenable = service_fcenable  # type: str
        self.service_protocol = service_protocol  # type: str
        self.service_timeout = service_timeout  # type: int
        self.service_vpc_enable = service_vpc_enable  # type: str
        self.status = status  # type: str
        self.system_parameters = system_parameters  # type: DescribeHistoryApiResponseBodySystemParameters
        self.visibility = visibility  # type: str
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.constant_parameters:
            self.constant_parameters.validate()
        if self.custom_system_parameters:
            self.custom_system_parameters.validate()
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.function_compute_config:
            self.function_compute_config.validate()
        if self.open_id_connect_config:
            self.open_id_connect_config.validate()
        if self.path_parameters:
            self.path_parameters.validate()
        if self.request_body:
            self.request_body.validate()
        if self.request_headers:
            self.request_headers.validate()
        if self.request_queries:
            self.request_queries.validate()
        if self.system_parameters:
            self.system_parameters.validate()

    def to_map(self):
        _map = super(DescribeHistoryApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_signature_method is not None:
            result['AllowSignatureMethod'] = self.allow_signature_method
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters.to_map()
        if self.custom_system_parameters is not None:
            result['CustomSystemParameters'] = self.custom_system_parameters.to_map()
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.function_compute_config is not None:
            result['FunctionComputeConfig'] = self.function_compute_config.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.http_protocol is not None:
            result['HttpProtocol'] = self.http_protocol
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.open_id_connect_config is not None:
            result['OpenIdConnectConfig'] = self.open_id_connect_config.to_map()
        if self.origin_result_description is not None:
            result['OriginResultDescription'] = self.origin_result_description
        if self.path is not None:
            result['Path'] = self.path
        if self.path_parameters is not None:
            result['PathParameters'] = self.path_parameters.to_map()
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.post_body_type is not None:
            result['PostBodyType'] = self.post_body_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_body is not None:
            result['RequestBody'] = self.request_body.to_map()
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_address is not None:
            result['ServiceAddress'] = self.service_address
        if self.service_fcenable is not None:
            result['ServiceFCEnable'] = self.service_fcenable
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.service_vpc_enable is not None:
            result['ServiceVpcEnable'] = self.service_vpc_enable
        if self.status is not None:
            result['Status'] = self.status
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters.to_map()
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowSignatureMethod') is not None:
            self.allow_signature_method = m.get('AllowSignatureMethod')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('ConstantParameters') is not None:
            temp_model = DescribeHistoryApiResponseBodyConstantParameters()
            self.constant_parameters = temp_model.from_map(m['ConstantParameters'])
        if m.get('CustomSystemParameters') is not None:
            temp_model = DescribeHistoryApiResponseBodyCustomSystemParameters()
            self.custom_system_parameters = temp_model.from_map(m['CustomSystemParameters'])
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeHistoryApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('FunctionComputeConfig') is not None:
            temp_model = DescribeHistoryApiResponseBodyFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m['FunctionComputeConfig'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('HttpProtocol') is not None:
            self.http_protocol = m.get('HttpProtocol')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('OpenIdConnectConfig') is not None:
            temp_model = DescribeHistoryApiResponseBodyOpenIdConnectConfig()
            self.open_id_connect_config = temp_model.from_map(m['OpenIdConnectConfig'])
        if m.get('OriginResultDescription') is not None:
            self.origin_result_description = m.get('OriginResultDescription')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathParameters') is not None:
            temp_model = DescribeHistoryApiResponseBodyPathParameters()
            self.path_parameters = temp_model.from_map(m['PathParameters'])
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('PostBodyType') is not None:
            self.post_body_type = m.get('PostBodyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestBody') is not None:
            temp_model = DescribeHistoryApiResponseBodyRequestBody()
            self.request_body = temp_model.from_map(m['RequestBody'])
        if m.get('RequestHeaders') is not None:
            temp_model = DescribeHistoryApiResponseBodyRequestHeaders()
            self.request_headers = temp_model.from_map(m['RequestHeaders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')
        if m.get('RequestQueries') is not None:
            temp_model = DescribeHistoryApiResponseBodyRequestQueries()
            self.request_queries = temp_model.from_map(m['RequestQueries'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceAddress') is not None:
            self.service_address = m.get('ServiceAddress')
        if m.get('ServiceFCEnable') is not None:
            self.service_fcenable = m.get('ServiceFCEnable')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('ServiceVpcEnable') is not None:
            self.service_vpc_enable = m.get('ServiceVpcEnable')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemParameters') is not None:
            temp_model = DescribeHistoryApiResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m['SystemParameters'])
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeHistoryApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHistoryApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHistoryApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHistoryApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHistoryApisRequest(TeaModel):
    def __init__(self, api_id=None, api_name=None, group_id=None, page_number=None, page_size=None,
                 security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeHistoryApisResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(self, api_id=None, api_name=None, deployed_time=None, description=None, group_id=None,
                 group_name=None, history_version=None, region_id=None, stage_name=None, status=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.deployed_time = deployed_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.history_version = history_version  # type: str
        self.region_id = region_id  # type: str
        self.stage_name = stage_name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHistoryApisResponseBodyApiInfosApiInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeHistoryApisResponseBodyApiInfos(TeaModel):
    def __init__(self, api_info=None):
        self.api_info = api_info  # type: list[DescribeHistoryApisResponseBodyApiInfosApiInfo]

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHistoryApisResponseBodyApiInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeHistoryApisResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeHistoryApisResponseBody(TeaModel):
    def __init__(self, api_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.api_infos = api_infos  # type: DescribeHistoryApisResponseBodyApiInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super(DescribeHistoryApisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
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
        if m.get('ApiInfos') is not None:
            temp_model = DescribeHistoryApisResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHistoryApisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHistoryApisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHistoryApisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHistoryApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpControlPolicyItemsRequest(TeaModel):
    def __init__(self, ip_control_id=None, page_number=None, page_size=None, policy_item_id=None,
                 security_token=None):
        self.ip_control_id = ip_control_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policy_item_id = policy_item_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpControlPolicyItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItemsIpControlPolicyItem(TeaModel):
    def __init__(self, app_id=None, cidr_ip=None, create_time=None, modified_time=None, policy_item_id=None):
        self.app_id = app_id  # type: str
        self.cidr_ip = cidr_ip  # type: str
        self.create_time = create_time  # type: str
        self.modified_time = modified_time  # type: str
        self.policy_item_id = policy_item_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItemsIpControlPolicyItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')
        return self


class DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItems(TeaModel):
    def __init__(self, ip_control_policy_item=None):
        self.ip_control_policy_item = ip_control_policy_item  # type: list[DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItemsIpControlPolicyItem]

    def validate(self):
        if self.ip_control_policy_item:
            for k in self.ip_control_policy_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpControlPolicyItem'] = []
        if self.ip_control_policy_item is not None:
            for k in self.ip_control_policy_item:
                result['IpControlPolicyItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ip_control_policy_item = []
        if m.get('IpControlPolicyItem') is not None:
            for k in m.get('IpControlPolicyItem'):
                temp_model = DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItemsIpControlPolicyItem()
                self.ip_control_policy_item.append(temp_model.from_map(k))
        return self


class DescribeIpControlPolicyItemsResponseBody(TeaModel):
    def __init__(self, ip_control_policy_items=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.ip_control_policy_items = ip_control_policy_items  # type: DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItems
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.ip_control_policy_items:
            self.ip_control_policy_items.validate()

    def to_map(self):
        _map = super(DescribeIpControlPolicyItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_policy_items is not None:
            result['IpControlPolicyItems'] = self.ip_control_policy_items.to_map()
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
        if m.get('IpControlPolicyItems') is not None:
            temp_model = DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItems()
            self.ip_control_policy_items = temp_model.from_map(m['IpControlPolicyItems'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeIpControlPolicyItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIpControlPolicyItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpControlPolicyItemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIpControlPolicyItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpControlsRequest(TeaModel):
    def __init__(self, ip_control_id=None, ip_control_name=None, ip_control_type=None, page_number=None,
                 page_size=None, security_token=None):
        self.ip_control_id = ip_control_id  # type: str
        self.ip_control_name = ip_control_name  # type: str
        self.ip_control_type = ip_control_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpControlsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name
        if self.ip_control_type is not None:
            result['IpControlType'] = self.ip_control_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')
        if m.get('IpControlType') is not None:
            self.ip_control_type = m.get('IpControlType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeIpControlsResponseBodyIpControlInfosIpControlInfo(TeaModel):
    def __init__(self, create_time=None, description=None, ip_control_id=None, ip_control_name=None,
                 ip_control_type=None, modified_time=None, region_id=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.ip_control_id = ip_control_id  # type: str
        self.ip_control_name = ip_control_name  # type: str
        self.ip_control_type = ip_control_type  # type: str
        self.modified_time = modified_time  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpControlsResponseBodyIpControlInfosIpControlInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name
        if self.ip_control_type is not None:
            result['IpControlType'] = self.ip_control_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')
        if m.get('IpControlType') is not None:
            self.ip_control_type = m.get('IpControlType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeIpControlsResponseBodyIpControlInfos(TeaModel):
    def __init__(self, ip_control_info=None):
        self.ip_control_info = ip_control_info  # type: list[DescribeIpControlsResponseBodyIpControlInfosIpControlInfo]

    def validate(self):
        if self.ip_control_info:
            for k in self.ip_control_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIpControlsResponseBodyIpControlInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpControlInfo'] = []
        if self.ip_control_info is not None:
            for k in self.ip_control_info:
                result['IpControlInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ip_control_info = []
        if m.get('IpControlInfo') is not None:
            for k in m.get('IpControlInfo'):
                temp_model = DescribeIpControlsResponseBodyIpControlInfosIpControlInfo()
                self.ip_control_info.append(temp_model.from_map(k))
        return self


class DescribeIpControlsResponseBody(TeaModel):
    def __init__(self, ip_control_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.ip_control_infos = ip_control_infos  # type: DescribeIpControlsResponseBodyIpControlInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.ip_control_infos:
            self.ip_control_infos.validate()

    def to_map(self):
        _map = super(DescribeIpControlsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_infos is not None:
            result['IpControlInfos'] = self.ip_control_infos.to_map()
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
        if m.get('IpControlInfos') is not None:
            temp_model = DescribeIpControlsResponseBodyIpControlInfos()
            self.ip_control_infos = temp_model.from_map(m['IpControlInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeIpControlsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIpControlsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpControlsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIpControlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogConfigRequest(TeaModel):
    def __init__(self, log_type=None, security_token=None):
        self.log_type = log_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeLogConfigResponseBodyLogInfosLogInfo(TeaModel):
    def __init__(self, log_type=None, region_id=None, sls_log_store=None, sls_project=None):
        self.log_type = log_type  # type: str
        self.region_id = region_id  # type: str
        self.sls_log_store = sls_log_store  # type: str
        self.sls_project = sls_project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogConfigResponseBodyLogInfosLogInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        return self


class DescribeLogConfigResponseBodyLogInfos(TeaModel):
    def __init__(self, log_info=None):
        self.log_info = log_info  # type: list[DescribeLogConfigResponseBodyLogInfosLogInfo]

    def validate(self):
        if self.log_info:
            for k in self.log_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogConfigResponseBodyLogInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogInfo'] = []
        if self.log_info is not None:
            for k in self.log_info:
                result['LogInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_info = []
        if m.get('LogInfo') is not None:
            for k in m.get('LogInfo'):
                temp_model = DescribeLogConfigResponseBodyLogInfosLogInfo()
                self.log_info.append(temp_model.from_map(k))
        return self


class DescribeLogConfigResponseBody(TeaModel):
    def __init__(self, log_infos=None, request_id=None):
        self.log_infos = log_infos  # type: DescribeLogConfigResponseBodyLogInfos
        self.request_id = request_id  # type: str

    def validate(self):
        if self.log_infos:
            self.log_infos.validate()

    def to_map(self):
        _map = super(DescribeLogConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogInfos') is not None:
            temp_model = DescribeLogConfigResponseBodyLogInfos()
            self.log_infos = temp_model.from_map(m['LogInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLogConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApiRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, security_token=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribePurchasedApiResponseBodyPathParametersPathParameter(TeaModel):
    def __init__(self, api_parameter_name=None, demo_value=None, description=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApiResponseBodyPathParametersPathParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class DescribePurchasedApiResponseBodyPathParameters(TeaModel):
    def __init__(self, path_parameter=None):
        self.path_parameter = path_parameter  # type: list[DescribePurchasedApiResponseBodyPathParametersPathParameter]

    def validate(self):
        if self.path_parameter:
            for k in self.path_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiResponseBodyPathParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PathParameter'] = []
        if self.path_parameter is not None:
            for k in self.path_parameter:
                result['PathParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.path_parameter = []
        if m.get('PathParameter') is not None:
            for k in m.get('PathParameter'):
                temp_model = DescribePurchasedApiResponseBodyPathParametersPathParameter()
                self.path_parameter.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiResponseBodyRequestBodyRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, default_value=None, demo_value=None, description=None,
                 doc_order=None, doc_show=None, enum_value=None, json_scheme=None, max_length=None, max_value=None,
                 min_length=None, min_value=None, parameter_type=None, regular_expression=None, required=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.doc_order = doc_order  # type: str
        self.doc_show = doc_show  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: str
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: str
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApiResponseBodyRequestBodyRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribePurchasedApiResponseBodyRequestBody(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribePurchasedApiResponseBodyRequestBodyRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiResponseBodyRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribePurchasedApiResponseBodyRequestBodyRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiResponseBodyRequestHeadersRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, default_value=None, demo_value=None, description=None,
                 doc_order=None, doc_show=None, enum_value=None, json_scheme=None, max_length=None, max_value=None,
                 min_length=None, min_value=None, parameter_type=None, regular_expression=None, required=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.doc_order = doc_order  # type: str
        self.doc_show = doc_show  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: long
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: long
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApiResponseBodyRequestHeadersRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribePurchasedApiResponseBodyRequestHeaders(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribePurchasedApiResponseBodyRequestHeadersRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiResponseBodyRequestHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribePurchasedApiResponseBodyRequestHeadersRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiResponseBodyRequestQueriesRequestParam(TeaModel):
    def __init__(self, api_parameter_name=None, default_value=None, demo_value=None, description=None,
                 doc_order=None, doc_show=None, enum_value=None, json_scheme=None, max_length=None, max_value=None,
                 min_length=None, min_value=None, parameter_type=None, regular_expression=None, required=None):
        self.api_parameter_name = api_parameter_name  # type: str
        self.default_value = default_value  # type: str
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.doc_order = doc_order  # type: str
        self.doc_show = doc_show  # type: str
        self.enum_value = enum_value  # type: str
        self.json_scheme = json_scheme  # type: str
        self.max_length = max_length  # type: long
        self.max_value = max_value  # type: str
        self.min_length = min_length  # type: long
        self.min_value = min_value  # type: str
        self.parameter_type = parameter_type  # type: str
        self.regular_expression = regular_expression  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApiResponseBodyRequestQueriesRequestParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribePurchasedApiResponseBodyRequestQueries(TeaModel):
    def __init__(self, request_param=None):
        self.request_param = request_param  # type: list[DescribePurchasedApiResponseBodyRequestQueriesRequestParam]

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiResponseBodyRequestQueries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribePurchasedApiResponseBodyRequestQueriesRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiResponseBody(TeaModel):
    def __init__(self, api_id=None, api_name=None, body_format=None, created_time=None, description=None,
                 group_id=None, group_name=None, http_method=None, http_protocol=None, mock=None, mock_result=None,
                 modified_time=None, path=None, path_parameters=None, post_body_description=None, post_body_type=None,
                 region_id=None, request_body=None, request_headers=None, request_id=None, request_queries=None,
                 result_sample=None, result_type=None, visibility=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.body_format = body_format  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.http_method = http_method  # type: str
        self.http_protocol = http_protocol  # type: str
        self.mock = mock  # type: str
        self.mock_result = mock_result  # type: str
        self.modified_time = modified_time  # type: str
        self.path = path  # type: str
        self.path_parameters = path_parameters  # type: DescribePurchasedApiResponseBodyPathParameters
        self.post_body_description = post_body_description  # type: str
        self.post_body_type = post_body_type  # type: str
        self.region_id = region_id  # type: str
        self.request_body = request_body  # type: DescribePurchasedApiResponseBodyRequestBody
        self.request_headers = request_headers  # type: DescribePurchasedApiResponseBodyRequestHeaders
        self.request_id = request_id  # type: str
        self.request_queries = request_queries  # type: DescribePurchasedApiResponseBodyRequestQueries
        self.result_sample = result_sample  # type: str
        self.result_type = result_type  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        if self.path_parameters:
            self.path_parameters.validate()
        if self.request_body:
            self.request_body.validate()
        if self.request_headers:
            self.request_headers.validate()
        if self.request_queries:
            self.request_queries.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.http_protocol is not None:
            result['HttpProtocol'] = self.http_protocol
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.path is not None:
            result['Path'] = self.path
        if self.path_parameters is not None:
            result['PathParameters'] = self.path_parameters.to_map()
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.post_body_type is not None:
            result['PostBodyType'] = self.post_body_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_body is not None:
            result['RequestBody'] = self.request_body.to_map()
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('HttpProtocol') is not None:
            self.http_protocol = m.get('HttpProtocol')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathParameters') is not None:
            temp_model = DescribePurchasedApiResponseBodyPathParameters()
            self.path_parameters = temp_model.from_map(m['PathParameters'])
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('PostBodyType') is not None:
            self.post_body_type = m.get('PostBodyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestBody') is not None:
            temp_model = DescribePurchasedApiResponseBodyRequestBody()
            self.request_body = temp_model.from_map(m['RequestBody'])
        if m.get('RequestHeaders') is not None:
            temp_model = DescribePurchasedApiResponseBodyRequestHeaders()
            self.request_headers = temp_model.from_map(m['RequestHeaders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestQueries') is not None:
            temp_model = DescribePurchasedApiResponseBodyRequestQueries()
            self.request_queries = temp_model.from_map(m['RequestQueries'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribePurchasedApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePurchasedApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePurchasedApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApiGroupDetailRequest(TeaModel):
    def __init__(self, group_id=None, security_token=None):
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApiGroupDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribePurchasedApiGroupDetailResponseBodyDomainItemsDomainItem(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApiGroupDetailResponseBodyDomainItemsDomainItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribePurchasedApiGroupDetailResponseBodyDomainItems(TeaModel):
    def __init__(self, domain_item=None):
        self.domain_item = domain_item  # type: list[DescribePurchasedApiGroupDetailResponseBodyDomainItemsDomainItem]

    def validate(self):
        if self.domain_item:
            for k in self.domain_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiGroupDetailResponseBodyDomainItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainItem'] = []
        if self.domain_item is not None:
            for k in self.domain_item:
                result['DomainItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_item = []
        if m.get('DomainItem') is not None:
            for k in m.get('DomainItem'):
                temp_model = DescribePurchasedApiGroupDetailResponseBodyDomainItemsDomainItem()
                self.domain_item.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiGroupDetailResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, domain_items=None, group_id=None, group_name=None,
                 modified_time=None, region_id=None, request_id=None, status=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.domain_items = domain_items  # type: DescribePurchasedApiGroupDetailResponseBodyDomainItems
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.modified_time = modified_time  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.domain_items:
            self.domain_items.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiGroupDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_items is not None:
            result['DomainItems'] = self.domain_items.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainItems') is not None:
            temp_model = DescribePurchasedApiGroupDetailResponseBodyDomainItems()
            self.domain_items = temp_model.from_map(m['DomainItems'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePurchasedApiGroupDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePurchasedApiGroupDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiGroupDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePurchasedApiGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApiGroupsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, security_token=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApiGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributesPurchasedApiGroupAttribute(TeaModel):
    def __init__(self, billing_type=None, created_time=None, expire_time=None, group_description=None,
                 group_id=None, group_name=None, invoke_times_max=None, invoke_times_now=None, modified_time=None,
                 region_id=None):
        self.billing_type = billing_type  # type: str
        self.created_time = created_time  # type: str
        self.expire_time = expire_time  # type: str
        self.group_description = group_description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.invoke_times_max = invoke_times_max  # type: long
        self.invoke_times_now = invoke_times_now  # type: long
        self.modified_time = modified_time  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributesPurchasedApiGroupAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.group_description is not None:
            result['GroupDescription'] = self.group_description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.invoke_times_max is not None:
            result['InvokeTimesMax'] = self.invoke_times_max
        if self.invoke_times_now is not None:
            result['InvokeTimesNow'] = self.invoke_times_now
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GroupDescription') is not None:
            self.group_description = m.get('GroupDescription')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InvokeTimesMax') is not None:
            self.invoke_times_max = m.get('InvokeTimesMax')
        if m.get('InvokeTimesNow') is not None:
            self.invoke_times_now = m.get('InvokeTimesNow')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributes(TeaModel):
    def __init__(self, purchased_api_group_attribute=None):
        self.purchased_api_group_attribute = purchased_api_group_attribute  # type: list[DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributesPurchasedApiGroupAttribute]

    def validate(self):
        if self.purchased_api_group_attribute:
            for k in self.purchased_api_group_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PurchasedApiGroupAttribute'] = []
        if self.purchased_api_group_attribute is not None:
            for k in self.purchased_api_group_attribute:
                result['PurchasedApiGroupAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.purchased_api_group_attribute = []
        if m.get('PurchasedApiGroupAttribute') is not None:
            for k in m.get('PurchasedApiGroupAttribute'):
                temp_model = DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributesPurchasedApiGroupAttribute()
                self.purchased_api_group_attribute.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiGroupsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, purchased_api_group_attributes=None, request_id=None,
                 total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.purchased_api_group_attributes = purchased_api_group_attributes  # type: DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributes
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.purchased_api_group_attributes:
            self.purchased_api_group_attributes.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.purchased_api_group_attributes is not None:
            result['PurchasedApiGroupAttributes'] = self.purchased_api_group_attributes.to_map()
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
        if m.get('PurchasedApiGroupAttributes') is not None:
            temp_model = DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributes()
            self.purchased_api_group_attributes = temp_model.from_map(m['PurchasedApiGroupAttributes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePurchasedApiGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePurchasedApiGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePurchasedApiGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePurchasedApiGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApisRequest(TeaModel):
    def __init__(self, api_id=None, api_name=None, group_id=None, page_number=None, page_size=None,
                 security_token=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribePurchasedApisResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(self, api_id=None, api_name=None, deployed_time=None, description=None, group_id=None,
                 group_name=None, modified_time=None, region_id=None, stage_name=None, visibility=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.deployed_time = deployed_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.modified_time = modified_time  # type: str
        self.region_id = region_id  # type: str
        self.stage_name = stage_name  # type: str
        self.visibility = visibility  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedApisResponseBodyApiInfosApiInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribePurchasedApisResponseBodyApiInfos(TeaModel):
    def __init__(self, api_info=None):
        self.api_info = api_info  # type: list[DescribePurchasedApisResponseBodyApiInfosApiInfo]

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePurchasedApisResponseBodyApiInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribePurchasedApisResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribePurchasedApisResponseBody(TeaModel):
    def __init__(self, api_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.api_infos = api_infos  # type: DescribePurchasedApisResponseBodyApiInfos
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super(DescribePurchasedApisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
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
        if m.get('ApiInfos') is not None:
            temp_model = DescribePurchasedApisResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePurchasedApisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePurchasedApisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePurchasedApisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePurchasedApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRaceWorkForInnerRequest(TeaModel):
    def __init__(self, group_id=None, security_token=None):
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRaceWorkForInnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRaceWorkForInnerResponseBody(TeaModel):
    def __init__(self, commodity_code=None, create_time=None, group_id=None, keywords=None, logo_url=None,
                 modified_time=None, request_id=None, short_description=None, work_name=None):
        self.commodity_code = commodity_code  # type: str
        self.create_time = create_time  # type: str
        self.group_id = group_id  # type: str
        self.keywords = keywords  # type: str
        self.logo_url = logo_url  # type: str
        self.modified_time = modified_time  # type: str
        self.request_id = request_id  # type: str
        self.short_description = short_description  # type: str
        self.work_name = work_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRaceWorkForInnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        return self


class DescribeRaceWorkForInnerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRaceWorkForInnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRaceWorkForInnerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRaceWorkForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, language=None, security_token=None):
        self.language = language  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
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


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
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


class DescribeRulesByApiRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRulesByApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeRulesByApiResponseBodyRulesRule(TeaModel):
    def __init__(self, created_time=None, rule_id=None, rule_name=None, rule_type=None):
        self.created_time = created_time  # type: int
        self.rule_id = rule_id  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRulesByApiResponseBodyRulesRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DescribeRulesByApiResponseBodyRules(TeaModel):
    def __init__(self, rule=None):
        self.rule = rule  # type: list[DescribeRulesByApiResponseBodyRulesRule]

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRulesByApiResponseBodyRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeRulesByApiResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeRulesByApiResponseBody(TeaModel):
    def __init__(self, request_id=None, rules=None):
        self.request_id = request_id  # type: str
        self.rules = rules  # type: DescribeRulesByApiResponseBodyRules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        _map = super(DescribeRulesByApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rules') is not None:
            temp_model = DescribeRulesByApiResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class DescribeRulesByApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRulesByApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRulesByApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRulesByApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecretKeysRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, secret_key_id=None, secret_key_name=None,
                 security_token=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.secret_key_id = secret_key_id  # type: str
        self.secret_key_name = secret_key_name  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecretKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSecretKeysResponseBodySecretKeysSecretKey(TeaModel):
    def __init__(self, created_time=None, modified_time=None, region_id=None, secret_key=None, secret_key_id=None,
                 secret_key_name=None, secret_key_value=None):
        self.created_time = created_time  # type: str
        self.modified_time = modified_time  # type: str
        self.region_id = region_id  # type: str
        self.secret_key = secret_key  # type: str
        self.secret_key_id = secret_key_id  # type: str
        self.secret_key_name = secret_key_name  # type: str
        self.secret_key_value = secret_key_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecretKeysResponseBodySecretKeysSecretKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        if self.secret_key_value is not None:
            result['SecretKeyValue'] = self.secret_key_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        if m.get('SecretKeyValue') is not None:
            self.secret_key_value = m.get('SecretKeyValue')
        return self


class DescribeSecretKeysResponseBodySecretKeys(TeaModel):
    def __init__(self, secret_key=None):
        self.secret_key = secret_key  # type: list[DescribeSecretKeysResponseBodySecretKeysSecretKey]

    def validate(self):
        if self.secret_key:
            for k in self.secret_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSecretKeysResponseBodySecretKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecretKey'] = []
        if self.secret_key is not None:
            for k in self.secret_key:
                result['SecretKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.secret_key = []
        if m.get('SecretKey') is not None:
            for k in m.get('SecretKey'):
                temp_model = DescribeSecretKeysResponseBodySecretKeysSecretKey()
                self.secret_key.append(temp_model.from_map(k))
        return self


class DescribeSecretKeysResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, secret_keys=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.secret_keys = secret_keys  # type: DescribeSecretKeysResponseBodySecretKeys
        self.total_count = total_count  # type: int

    def validate(self):
        if self.secret_keys:
            self.secret_keys.validate()

    def to_map(self):
        _map = super(DescribeSecretKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_keys is not None:
            result['SecretKeys'] = self.secret_keys.to_map()
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
        if m.get('SecretKeys') is not None:
            temp_model = DescribeSecretKeysResponseBodySecretKeys()
            self.secret_keys = temp_model.from_map(m['SecretKeys'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSecretKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSecretKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecretKeysResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSecretKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSystemParametersRequest(TeaModel):
    def __init__(self, security_token=None):
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSystemParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSystemParametersResponseBodySystemParametersSystemParameter(TeaModel):
    def __init__(self, demo_value=None, description=None, param_name=None, param_type=None):
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.param_name = param_name  # type: str
        self.param_type = param_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSystemParametersResponseBodySystemParametersSystemParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        return self


class DescribeSystemParametersResponseBodySystemParameters(TeaModel):
    def __init__(self, system_parameter=None):
        self.system_parameter = system_parameter  # type: list[DescribeSystemParametersResponseBodySystemParametersSystemParameter]

    def validate(self):
        if self.system_parameter:
            for k in self.system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSystemParametersResponseBodySystemParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParameter'] = []
        if self.system_parameter is not None:
            for k in self.system_parameter:
                result['SystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.system_parameter = []
        if m.get('SystemParameter') is not None:
            for k in m.get('SystemParameter'):
                temp_model = DescribeSystemParametersResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k))
        return self


class DescribeSystemParametersResponseBody(TeaModel):
    def __init__(self, request_id=None, system_parameters=None):
        self.request_id = request_id  # type: str
        self.system_parameters = system_parameters  # type: DescribeSystemParametersResponseBodySystemParameters

    def validate(self):
        if self.system_parameters:
            self.system_parameters.validate()

    def to_map(self):
        _map = super(DescribeSystemParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemParameters') is not None:
            temp_model = DescribeSystemParametersResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m['SystemParameters'])
        return self


class DescribeSystemParametersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSystemParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSystemParametersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSystemParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSystemParamsRequest(TeaModel):
    def __init__(self, security_token=None):
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSystemParamsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSystemParamsResponseBodySystemParamsSystemParam(TeaModel):
    def __init__(self, demo_value=None, description=None, param_name=None, param_type=None):
        self.demo_value = demo_value  # type: str
        self.description = description  # type: str
        self.param_name = param_name  # type: str
        self.param_type = param_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSystemParamsResponseBodySystemParamsSystemParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        return self


class DescribeSystemParamsResponseBodySystemParams(TeaModel):
    def __init__(self, system_param=None):
        self.system_param = system_param  # type: list[DescribeSystemParamsResponseBodySystemParamsSystemParam]

    def validate(self):
        if self.system_param:
            for k in self.system_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSystemParamsResponseBodySystemParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParam'] = []
        if self.system_param is not None:
            for k in self.system_param:
                result['SystemParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.system_param = []
        if m.get('SystemParam') is not None:
            for k in m.get('SystemParam'):
                temp_model = DescribeSystemParamsResponseBodySystemParamsSystemParam()
                self.system_param.append(temp_model.from_map(k))
        return self


class DescribeSystemParamsResponseBody(TeaModel):
    def __init__(self, request_id=None, system_params=None):
        self.request_id = request_id  # type: str
        self.system_params = system_params  # type: DescribeSystemParamsResponseBodySystemParams

    def validate(self):
        if self.system_params:
            self.system_params.validate()

    def to_map(self):
        _map = super(DescribeSystemParamsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_params is not None:
            result['SystemParams'] = self.system_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemParams') is not None:
            temp_model = DescribeSystemParamsResponseBodySystemParams()
            self.system_params = temp_model.from_map(m['SystemParams'])
        return self


class DescribeSystemParamsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSystemParamsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSystemParamsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSystemParamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrafficControlsRequest(TeaModel):
    def __init__(self, api_uid=None, group_id=None, page_number=None, page_size=None, security_token=None,
                 stage_name=None, traffic_control_id=None, traffic_control_name=None):
        self.api_uid = api_uid  # type: str
        self.group_id = group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str
        self.traffic_control_id = traffic_control_id  # type: str
        self.traffic_control_name = traffic_control_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrafficControlsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')
        return self


class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecialsSpecial(TeaModel):
    def __init__(self, special_key=None, traffic_value=None):
        self.special_key = special_key  # type: str
        self.traffic_value = traffic_value  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecialsSpecial, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.special_key is not None:
            result['SpecialKey'] = self.special_key
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpecialKey') is not None:
            self.special_key = m.get('SpecialKey')
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        return self


class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecials(TeaModel):
    def __init__(self, special=None):
        self.special = special  # type: list[DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecialsSpecial]

    def validate(self):
        if self.special:
            for k in self.special:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecials, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Special'] = []
        if self.special is not None:
            for k in self.special:
                result['Special'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.special = []
        if m.get('Special') is not None:
            for k in m.get('Special'):
                temp_model = DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecialsSpecial()
                self.special.append(temp_model.from_map(k))
        return self


class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicy(TeaModel):
    def __init__(self, special_type=None, specials=None):
        self.special_type = special_type  # type: str
        self.specials = specials  # type: DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecials

    def validate(self):
        if self.specials:
            self.specials.validate()

    def to_map(self):
        _map = super(DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.special_type is not None:
            result['SpecialType'] = self.special_type
        if self.specials is not None:
            result['Specials'] = self.specials.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpecialType') is not None:
            self.special_type = m.get('SpecialType')
        if m.get('Specials') is not None:
            temp_model = DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecials()
            self.specials = temp_model.from_map(m['Specials'])
        return self


class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPolicies(TeaModel):
    def __init__(self, special_policy=None):
        self.special_policy = special_policy  # type: list[DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicy]

    def validate(self):
        if self.special_policy:
            for k in self.special_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SpecialPolicy'] = []
        if self.special_policy is not None:
            for k in self.special_policy:
                result['SpecialPolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.special_policy = []
        if m.get('SpecialPolicy') is not None:
            for k in m.get('SpecialPolicy'):
                temp_model = DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicy()
                self.special_policy.append(temp_model.from_map(k))
        return self


class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControl(TeaModel):
    def __init__(self, api_default=None, app_default=None, created_time=None, description=None, modified_time=None,
                 special_policies=None, traffic_control_id=None, traffic_control_name=None, traffic_control_unit=None,
                 user_default=None):
        self.api_default = api_default  # type: int
        self.app_default = app_default  # type: int
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.special_policies = special_policies  # type: DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPolicies
        self.traffic_control_id = traffic_control_id  # type: str
        self.traffic_control_name = traffic_control_name  # type: str
        self.traffic_control_unit = traffic_control_unit  # type: str
        self.user_default = user_default  # type: int

    def validate(self):
        if self.special_policies:
            self.special_policies.validate()

    def to_map(self):
        _map = super(DescribeTrafficControlsResponseBodyTrafficControlsTrafficControl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_default is not None:
            result['ApiDefault'] = self.api_default
        if self.app_default is not None:
            result['AppDefault'] = self.app_default
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.special_policies is not None:
            result['SpecialPolicies'] = self.special_policies.to_map()
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name
        if self.traffic_control_unit is not None:
            result['TrafficControlUnit'] = self.traffic_control_unit
        if self.user_default is not None:
            result['UserDefault'] = self.user_default
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDefault') is not None:
            self.api_default = m.get('ApiDefault')
        if m.get('AppDefault') is not None:
            self.app_default = m.get('AppDefault')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SpecialPolicies') is not None:
            temp_model = DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPolicies()
            self.special_policies = temp_model.from_map(m['SpecialPolicies'])
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')
        if m.get('TrafficControlUnit') is not None:
            self.traffic_control_unit = m.get('TrafficControlUnit')
        if m.get('UserDefault') is not None:
            self.user_default = m.get('UserDefault')
        return self


class DescribeTrafficControlsResponseBodyTrafficControls(TeaModel):
    def __init__(self, traffic_control=None):
        self.traffic_control = traffic_control  # type: list[DescribeTrafficControlsResponseBodyTrafficControlsTrafficControl]

    def validate(self):
        if self.traffic_control:
            for k in self.traffic_control:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTrafficControlsResponseBodyTrafficControls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrafficControl'] = []
        if self.traffic_control is not None:
            for k in self.traffic_control:
                result['TrafficControl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.traffic_control = []
        if m.get('TrafficControl') is not None:
            for k in m.get('TrafficControl'):
                temp_model = DescribeTrafficControlsResponseBodyTrafficControlsTrafficControl()
                self.traffic_control.append(temp_model.from_map(k))
        return self


class DescribeTrafficControlsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, traffic_controls=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.traffic_controls = traffic_controls  # type: DescribeTrafficControlsResponseBodyTrafficControls

    def validate(self):
        if self.traffic_controls:
            self.traffic_controls.validate()

    def to_map(self):
        _map = super(DescribeTrafficControlsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.traffic_controls is not None:
            result['TrafficControls'] = self.traffic_controls.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TrafficControls') is not None:
            temp_model = DescribeTrafficControlsResponseBodyTrafficControls()
            self.traffic_controls = temp_model.from_map(m['TrafficControls'])
        return self


class DescribeTrafficControlsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTrafficControlsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTrafficControlsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTrafficControlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportSwaggerRequest(TeaModel):
    def __init__(self, api_uid=None, data_format=None, security_token=None):
        self.api_uid = api_uid  # type: str
        self.data_format = data_format  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportSwaggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ExportSwaggerResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportSwaggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportSwaggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportSwaggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportSwaggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExportSwaggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApiMethodsRequest(TeaModel):
    def __init__(self, api_path=None, group_id=None, security_token=None, stage_name=None):
        self.api_path = api_path  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApiMethodsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_path is not None:
            result['ApiPath'] = self.api_path
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiPath') is not None:
            self.api_path = m.get('ApiPath')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class GetApiMethodsResponseBody(TeaModel):
    def __init__(self, methods=None, request_id=None):
        self.methods = methods  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApiMethodsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.methods is not None:
            result['Methods'] = self.methods
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Methods') is not None:
            self.methods = m.get('Methods')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApiMethodsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApiMethodsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApiMethodsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetApiMethodsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomizedInfoRequest(TeaModel):
    def __init__(self, api_id=None, api_name=None, group_id=None, security_token=None, stage_id=None,
                 stage_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_id = stage_id  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomizedInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class GetCustomizedInfoResponseBodySdkDemosSdkDemo(TeaModel):
    def __init__(self, call_demo=None, ide_key=None):
        self.call_demo = call_demo  # type: str
        self.ide_key = ide_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomizedInfoResponseBodySdkDemosSdkDemo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_demo is not None:
            result['CallDemo'] = self.call_demo
        if self.ide_key is not None:
            result['IdeKey'] = self.ide_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallDemo') is not None:
            self.call_demo = m.get('CallDemo')
        if m.get('IdeKey') is not None:
            self.ide_key = m.get('IdeKey')
        return self


class GetCustomizedInfoResponseBodySdkDemos(TeaModel):
    def __init__(self, sdk_demo=None):
        self.sdk_demo = sdk_demo  # type: list[GetCustomizedInfoResponseBodySdkDemosSdkDemo]

    def validate(self):
        if self.sdk_demo:
            for k in self.sdk_demo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCustomizedInfoResponseBodySdkDemos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SdkDemo'] = []
        if self.sdk_demo is not None:
            for k in self.sdk_demo:
                result['SdkDemo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sdk_demo = []
        if m.get('SdkDemo') is not None:
            for k in m.get('SdkDemo'):
                temp_model = GetCustomizedInfoResponseBodySdkDemosSdkDemo()
                self.sdk_demo.append(temp_model.from_map(k))
        return self


class GetCustomizedInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, sdk_demos=None):
        self.request_id = request_id  # type: str
        self.sdk_demos = sdk_demos  # type: GetCustomizedInfoResponseBodySdkDemos

    def validate(self):
        if self.sdk_demos:
            self.sdk_demos.validate()

    def to_map(self):
        _map = super(GetCustomizedInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_demos is not None:
            result['SdkDemos'] = self.sdk_demos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkDemos') is not None:
            temp_model = GetCustomizedInfoResponseBodySdkDemos()
            self.sdk_demos = temp_model.from_map(m['SdkDemos'])
        return self


class GetCustomizedInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCustomizedInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCustomizedInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCustomizedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportSwaggerRequest(TeaModel):
    def __init__(self, data=None, data_format=None, dry_run=None, group_id=None, overwrite=None):
        self.data = data  # type: str
        self.data_format = data_format  # type: str
        self.dry_run = dry_run  # type: bool
        self.group_id = group_id  # type: str
        self.overwrite = overwrite  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportSwaggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        return self


class ImportSwaggerResponseBodyFailedApiImportSwaggerFailed(TeaModel):
    def __init__(self, error_msg=None, http_method=None, path=None):
        self.error_msg = error_msg  # type: str
        self.http_method = http_method  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportSwaggerResponseBodyFailedApiImportSwaggerFailed, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ImportSwaggerResponseBodyFailed(TeaModel):
    def __init__(self, api_import_swagger_failed=None):
        self.api_import_swagger_failed = api_import_swagger_failed  # type: list[ImportSwaggerResponseBodyFailedApiImportSwaggerFailed]

    def validate(self):
        if self.api_import_swagger_failed:
            for k in self.api_import_swagger_failed:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportSwaggerResponseBodyFailed, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiImportSwaggerFailed'] = []
        if self.api_import_swagger_failed is not None:
            for k in self.api_import_swagger_failed:
                result['ApiImportSwaggerFailed'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_import_swagger_failed = []
        if m.get('ApiImportSwaggerFailed') is not None:
            for k in m.get('ApiImportSwaggerFailed'):
                temp_model = ImportSwaggerResponseBodyFailedApiImportSwaggerFailed()
                self.api_import_swagger_failed.append(temp_model.from_map(k))
        return self


class ImportSwaggerResponseBodyModelFailedApiImportModelFailed(TeaModel):
    def __init__(self, error_msg=None, group_id=None, model_name=None):
        self.error_msg = error_msg  # type: str
        self.group_id = group_id  # type: str
        self.model_name = model_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportSwaggerResponseBodyModelFailedApiImportModelFailed, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class ImportSwaggerResponseBodyModelFailed(TeaModel):
    def __init__(self, api_import_model_failed=None):
        self.api_import_model_failed = api_import_model_failed  # type: list[ImportSwaggerResponseBodyModelFailedApiImportModelFailed]

    def validate(self):
        if self.api_import_model_failed:
            for k in self.api_import_model_failed:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportSwaggerResponseBodyModelFailed, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiImportModelFailed'] = []
        if self.api_import_model_failed is not None:
            for k in self.api_import_model_failed:
                result['ApiImportModelFailed'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_import_model_failed = []
        if m.get('ApiImportModelFailed') is not None:
            for k in m.get('ApiImportModelFailed'):
                temp_model = ImportSwaggerResponseBodyModelFailedApiImportModelFailed()
                self.api_import_model_failed.append(temp_model.from_map(k))
        return self


class ImportSwaggerResponseBodyModelSuccessApiImportModelSuccess(TeaModel):
    def __init__(self, group_id=None, model_name=None, model_operation=None, model_uid=None):
        self.group_id = group_id  # type: str
        self.model_name = model_name  # type: str
        self.model_operation = model_operation  # type: str
        self.model_uid = model_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportSwaggerResponseBodyModelSuccessApiImportModelSuccess, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_operation is not None:
            result['ModelOperation'] = self.model_operation
        if self.model_uid is not None:
            result['ModelUid'] = self.model_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelOperation') is not None:
            self.model_operation = m.get('ModelOperation')
        if m.get('ModelUid') is not None:
            self.model_uid = m.get('ModelUid')
        return self


class ImportSwaggerResponseBodyModelSuccess(TeaModel):
    def __init__(self, api_import_model_success=None):
        self.api_import_model_success = api_import_model_success  # type: list[ImportSwaggerResponseBodyModelSuccessApiImportModelSuccess]

    def validate(self):
        if self.api_import_model_success:
            for k in self.api_import_model_success:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportSwaggerResponseBodyModelSuccess, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiImportModelSuccess'] = []
        if self.api_import_model_success is not None:
            for k in self.api_import_model_success:
                result['ApiImportModelSuccess'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_import_model_success = []
        if m.get('ApiImportModelSuccess') is not None:
            for k in m.get('ApiImportModelSuccess'):
                temp_model = ImportSwaggerResponseBodyModelSuccessApiImportModelSuccess()
                self.api_import_model_success.append(temp_model.from_map(k))
        return self


class ImportSwaggerResponseBodySuccessApiImportSwaggerSuccess(TeaModel):
    def __init__(self, api_operation=None, api_uid=None, http_method=None, path=None):
        self.api_operation = api_operation  # type: str
        self.api_uid = api_uid  # type: str
        self.http_method = http_method  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportSwaggerResponseBodySuccessApiImportSwaggerSuccess, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_operation is not None:
            result['ApiOperation'] = self.api_operation
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiOperation') is not None:
            self.api_operation = m.get('ApiOperation')
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ImportSwaggerResponseBodySuccess(TeaModel):
    def __init__(self, api_import_swagger_success=None):
        self.api_import_swagger_success = api_import_swagger_success  # type: list[ImportSwaggerResponseBodySuccessApiImportSwaggerSuccess]

    def validate(self):
        if self.api_import_swagger_success:
            for k in self.api_import_swagger_success:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportSwaggerResponseBodySuccess, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiImportSwaggerSuccess'] = []
        if self.api_import_swagger_success is not None:
            for k in self.api_import_swagger_success:
                result['ApiImportSwaggerSuccess'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.api_import_swagger_success = []
        if m.get('ApiImportSwaggerSuccess') is not None:
            for k in m.get('ApiImportSwaggerSuccess'):
                temp_model = ImportSwaggerResponseBodySuccessApiImportSwaggerSuccess()
                self.api_import_swagger_success.append(temp_model.from_map(k))
        return self


class ImportSwaggerResponseBody(TeaModel):
    def __init__(self, failed=None, model_failed=None, model_success=None, request_id=None, success=None):
        self.failed = failed  # type: ImportSwaggerResponseBodyFailed
        self.model_failed = model_failed  # type: ImportSwaggerResponseBodyModelFailed
        self.model_success = model_success  # type: ImportSwaggerResponseBodyModelSuccess
        self.request_id = request_id  # type: str
        self.success = success  # type: ImportSwaggerResponseBodySuccess

    def validate(self):
        if self.failed:
            self.failed.validate()
        if self.model_failed:
            self.model_failed.validate()
        if self.model_success:
            self.model_success.validate()
        if self.success:
            self.success.validate()

    def to_map(self):
        _map = super(ImportSwaggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed is not None:
            result['Failed'] = self.failed.to_map()
        if self.model_failed is not None:
            result['ModelFailed'] = self.model_failed.to_map()
        if self.model_success is not None:
            result['ModelSuccess'] = self.model_success.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Failed') is not None:
            temp_model = ImportSwaggerResponseBodyFailed()
            self.failed = temp_model.from_map(m['Failed'])
        if m.get('ModelFailed') is not None:
            temp_model = ImportSwaggerResponseBodyModelFailed()
            self.model_failed = temp_model.from_map(m['ModelFailed'])
        if m.get('ModelSuccess') is not None:
            temp_model = ImportSwaggerResponseBodyModelSuccess()
            self.model_success = temp_model.from_map(m['ModelSuccess'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            temp_model = ImportSwaggerResponseBodySuccess()
            self.success = temp_model.from_map(m['Success'])
        return self


class ImportSwaggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportSwaggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportSwaggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ImportSwaggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiRequest(TeaModel):
    def __init__(self, allow_signature_method=None, api_id=None, api_name=None, app_code_auth_type=None,
                 auth_type=None, description=None, disable_internet=None, error_code_samples=None, fail_result_sample=None,
                 force_nonce_check=None, group_id=None, open_id_connect_config=None, request_config=None, request_paramters=None,
                 result_body_model=None, result_descriptions=None, result_sample=None, result_type=None, security_token=None,
                 service_config=None, service_parameters=None, service_parameters_map=None, visibility=None,
                 web_socket_api_type=None):
        self.allow_signature_method = allow_signature_method  # type: str
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.app_code_auth_type = app_code_auth_type  # type: str
        self.auth_type = auth_type  # type: str
        self.description = description  # type: str
        self.disable_internet = disable_internet  # type: bool
        self.error_code_samples = error_code_samples  # type: str
        self.fail_result_sample = fail_result_sample  # type: str
        self.force_nonce_check = force_nonce_check  # type: bool
        self.group_id = group_id  # type: str
        self.open_id_connect_config = open_id_connect_config  # type: str
        self.request_config = request_config  # type: str
        self.request_paramters = request_paramters  # type: str
        self.result_body_model = result_body_model  # type: str
        self.result_descriptions = result_descriptions  # type: str
        self.result_sample = result_sample  # type: str
        self.result_type = result_type  # type: str
        self.security_token = security_token  # type: str
        self.service_config = service_config  # type: str
        self.service_parameters = service_parameters  # type: str
        self.service_parameters_map = service_parameters_map  # type: str
        self.visibility = visibility  # type: str
        self.web_socket_api_type = web_socket_api_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_signature_method is not None:
            result['AllowSignatureMethod'] = self.allow_signature_method
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.app_code_auth_type is not None:
            result['AppCodeAuthType'] = self.app_code_auth_type
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.open_id_connect_config is not None:
            result['OpenIdConnectConfig'] = self.open_id_connect_config
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config
        if self.request_paramters is not None:
            result['RequestParamters'] = self.request_paramters
        if self.result_body_model is not None:
            result['ResultBodyModel'] = self.result_body_model
        if self.result_descriptions is not None:
            result['ResultDescriptions'] = self.result_descriptions
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        if self.service_parameters_map is not None:
            result['ServiceParametersMap'] = self.service_parameters_map
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.web_socket_api_type is not None:
            result['WebSocketApiType'] = self.web_socket_api_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowSignatureMethod') is not None:
            self.allow_signature_method = m.get('AllowSignatureMethod')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AppCodeAuthType') is not None:
            self.app_code_auth_type = m.get('AppCodeAuthType')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            self.error_code_samples = m.get('ErrorCodeSamples')
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OpenIdConnectConfig') is not None:
            self.open_id_connect_config = m.get('OpenIdConnectConfig')
        if m.get('RequestConfig') is not None:
            self.request_config = m.get('RequestConfig')
        if m.get('RequestParamters') is not None:
            self.request_paramters = m.get('RequestParamters')
        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')
        if m.get('ResultDescriptions') is not None:
            self.result_descriptions = m.get('ResultDescriptions')
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        if m.get('ServiceParametersMap') is not None:
            self.service_parameters_map = m.get('ServiceParametersMap')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('WebSocketApiType') is not None:
            self.web_socket_api_type = m.get('WebSocketApiType')
        return self


class ModifyApiResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyApiResponseBody, self).to_map()
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


class ModifyApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiGroupRequest(TeaModel):
    def __init__(self, compatible_flags=None, custom_trace_config=None, default_domain=None, description=None,
                 group_id=None, group_name=None, passthrough_headers=None, rpc_pattern=None, security_token=None,
                 user_log_config=None):
        self.compatible_flags = compatible_flags  # type: str
        self.custom_trace_config = custom_trace_config  # type: str
        self.default_domain = default_domain  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.passthrough_headers = passthrough_headers  # type: str
        self.rpc_pattern = rpc_pattern  # type: str
        self.security_token = security_token  # type: str
        self.user_log_config = user_log_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyApiGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_flags is not None:
            result['CompatibleFlags'] = self.compatible_flags
        if self.custom_trace_config is not None:
            result['CustomTraceConfig'] = self.custom_trace_config
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.passthrough_headers is not None:
            result['PassthroughHeaders'] = self.passthrough_headers
        if self.rpc_pattern is not None:
            result['RpcPattern'] = self.rpc_pattern
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.user_log_config is not None:
            result['UserLogConfig'] = self.user_log_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompatibleFlags') is not None:
            self.compatible_flags = m.get('CompatibleFlags')
        if m.get('CustomTraceConfig') is not None:
            self.custom_trace_config = m.get('CustomTraceConfig')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('PassthroughHeaders') is not None:
            self.passthrough_headers = m.get('PassthroughHeaders')
        if m.get('RpcPattern') is not None:
            self.rpc_pattern = m.get('RpcPattern')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('UserLogConfig') is not None:
            self.user_log_config = m.get('UserLogConfig')
        return self


class ModifyApiGroupResponseBody(TeaModel):
    def __init__(self, description=None, group_id=None, group_name=None, request_id=None, sub_domain=None):
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.request_id = request_id  # type: str
        self.sub_domain = sub_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyApiGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class ModifyApiGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyApiGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyApiGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None, description=None, security_token=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.description = description  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyAppResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppResponseBody, self).to_map()
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


class ModifyAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(self, https_policy=None, instance_id=None, instance_name=None, token=None):
        self.https_policy = https_policy  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_policy is not None:
            result['HttpsPolicy'] = self.https_policy
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpsPolicy') is not None:
            self.https_policy = m.get('HttpsPolicy')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
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


class ModifyInstanceVpcAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, token=None, vpc_id=None):
        self.instance_id = instance_id  # type: str
        self.token = token  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceVpcAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.token is not None:
            result['Token'] = self.token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ModifyInstanceVpcAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceVpcAttributeResponseBody, self).to_map()
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


class ModifyInstanceVpcAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceVpcAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceVpcAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceVpcAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpControlRequest(TeaModel):
    def __init__(self, description=None, ip_control_id=None, ip_control_name=None, security_token=None):
        self.description = description  # type: str
        self.ip_control_id = ip_control_id  # type: str
        self.ip_control_name = ip_control_name  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyIpControlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpControlResponseBody, self).to_map()
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


class ModifyIpControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyIpControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyIpControlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyIpControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpControlPolicyItemRequest(TeaModel):
    def __init__(self, app_id=None, cidr_ip=None, ip_control_id=None, policy_item_id=None, security_token=None):
        self.app_id = app_id  # type: str
        self.cidr_ip = cidr_ip  # type: str
        self.ip_control_id = ip_control_id  # type: str
        self.policy_item_id = policy_item_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpControlPolicyItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyIpControlPolicyItemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpControlPolicyItemResponseBody, self).to_map()
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


class ModifyIpControlPolicyItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyIpControlPolicyItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyIpControlPolicyItemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyIpControlPolicyItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogConfigRequest(TeaModel):
    def __init__(self, log_type=None, security_token=None, sls_log_store=None, sls_project=None):
        self.log_type = log_type  # type: str
        self.security_token = security_token  # type: str
        self.sls_log_store = sls_log_store  # type: str
        self.sls_project = sls_project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        return self


class ModifyLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLogConfigResponseBody, self).to_map()
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


class ModifyLogConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecretKeyRequest(TeaModel):
    def __init__(self, secret_key=None, secret_key_id=None, secret_key_name=None, secret_value=None,
                 security_token=None):
        self.secret_key = secret_key  # type: str
        self.secret_key_id = secret_key_id  # type: str
        self.secret_key_name = secret_key_name  # type: str
        self.secret_value = secret_value  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecretKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        if self.secret_value is not None:
            result['SecretValue'] = self.secret_value
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        if m.get('SecretValue') is not None:
            self.secret_value = m.get('SecretValue')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifySecretKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, secret_key_id=None, secret_key_name=None):
        self.request_id = request_id  # type: str
        self.secret_key_id = secret_key_id  # type: str
        self.secret_key_name = secret_key_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecretKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        return self


class ModifySecretKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySecretKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySecretKeyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifySecretKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTrafficControlRequest(TeaModel):
    def __init__(self, api_default=None, app_default=None, description=None, security_token=None,
                 traffic_control_id=None, traffic_control_name=None, traffic_control_unit=None, user_default=None):
        self.api_default = api_default  # type: int
        self.app_default = app_default  # type: int
        self.description = description  # type: str
        self.security_token = security_token  # type: str
        self.traffic_control_id = traffic_control_id  # type: str
        self.traffic_control_name = traffic_control_name  # type: str
        self.traffic_control_unit = traffic_control_unit  # type: str
        self.user_default = user_default  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTrafficControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_default is not None:
            result['ApiDefault'] = self.api_default
        if self.app_default is not None:
            result['AppDefault'] = self.app_default
        if self.description is not None:
            result['Description'] = self.description
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name
        if self.traffic_control_unit is not None:
            result['TrafficControlUnit'] = self.traffic_control_unit
        if self.user_default is not None:
            result['UserDefault'] = self.user_default
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiDefault') is not None:
            self.api_default = m.get('ApiDefault')
        if m.get('AppDefault') is not None:
            self.app_default = m.get('AppDefault')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')
        if m.get('TrafficControlUnit') is not None:
            self.traffic_control_unit = m.get('TrafficControlUnit')
        if m.get('UserDefault') is not None:
            self.user_default = m.get('UserDefault')
        return self


class ModifyTrafficControlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTrafficControlResponseBody, self).to_map()
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


class ModifyTrafficControlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTrafficControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTrafficControlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTrafficControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReactivateDomainRequest(TeaModel):
    def __init__(self, domain_name=None, group_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReactivateDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ReactivateDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReactivateDomainResponseBody, self).to_map()
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


class ReactivateDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReactivateDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReactivateDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReactivateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverApiFromHistoricalRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, history_version=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.history_version = history_version  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoverApiFromHistoricalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RecoverApiFromHistoricalResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoverApiFromHistoricalResponseBody, self).to_map()
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


class RecoverApiFromHistoricalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecoverApiFromHistoricalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecoverApiFromHistoricalResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecoverApiFromHistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoveryApiDefineFromHistoricalRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, history_version=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.history_version = history_version  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoveryApiDefineFromHistoricalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RecoveryApiDefineFromHistoricalResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoveryApiDefineFromHistoricalResponseBody, self).to_map()
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


class RecoveryApiDefineFromHistoricalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecoveryApiDefineFromHistoricalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecoveryApiDefineFromHistoricalResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecoveryApiDefineFromHistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoveryApiFromHistoricalRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, history_version=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.history_version = history_version  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoveryApiFromHistoricalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RecoveryApiFromHistoricalResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoveryApiFromHistoricalResponseBody, self).to_map()
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


class RecoveryApiFromHistoricalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecoveryApiFromHistoricalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecoveryApiFromHistoricalResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RecoveryApiFromHistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshDomainRequest(TeaModel):
    def __init__(self, domain_name=None, group_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RefreshDomainResponseBody(TeaModel):
    def __init__(self, certificate_id=None, certificate_name=None, domain_name=None, domain_name_resolution=None,
                 domain_status=None, group_id=None, request_id=None, sub_domain=None):
        self.certificate_id = certificate_id  # type: str
        self.certificate_name = certificate_name  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_name_resolution = domain_name_resolution  # type: str
        self.domain_status = domain_status  # type: str
        self.group_id = group_id  # type: str
        self.request_id = request_id  # type: str
        self.sub_domain = sub_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class RefreshDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RefreshDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAccessPermissionByApisRequest(TeaModel):
    def __init__(self, api_ids=None, app_id=None, description=None, group_id=None, security_token=None,
                 stage_name=None):
        self.api_ids = api_ids  # type: str
        self.app_id = app_id  # type: long
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveAccessPermissionByApisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveAccessPermissionByApisResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveAccessPermissionByApisResponseBody, self).to_map()
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


class RemoveAccessPermissionByApisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveAccessPermissionByApisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveAccessPermissionByApisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveAccessPermissionByApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAccessPermissionByAppsRequest(TeaModel):
    def __init__(self, api_id=None, app_ids=None, group_id=None, security_token=None, stage_name=None):
        self.api_id = api_id  # type: str
        self.app_ids = app_ids  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveAccessPermissionByAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveAccessPermissionByAppsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveAccessPermissionByAppsResponseBody, self).to_map()
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


class RemoveAccessPermissionByAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveAccessPermissionByAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveAccessPermissionByAppsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveAccessPermissionByAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAllBlackListRequest(TeaModel):
    def __init__(self, black_type=None, security_token=None):
        self.black_type = black_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveAllBlackListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RemoveAllBlackListResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveAllBlackListResponseBody, self).to_map()
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


class RemoveAllBlackListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveAllBlackListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveAllBlackListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveAllBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveApiRuleRequest(TeaModel):
    def __init__(self, api_ids=None, group_id=None, rule_id=None, rule_type=None, security_token=None,
                 stage_name=None):
        self.api_ids = api_ids  # type: str
        self.group_id = group_id  # type: str
        self.rule_id = rule_id  # type: str
        self.rule_type = rule_type  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveApiRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveApiRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveApiRuleResponseBody, self).to_map()
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


class RemoveApiRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveApiRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveApiRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveApiRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveBlackListRequest(TeaModel):
    def __init__(self, black_content=None, black_type=None, security_token=None):
        self.black_content = black_content  # type: str
        self.black_type = black_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveBlackListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_content is not None:
            result['BlackContent'] = self.black_content
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackContent') is not None:
            self.black_content = m.get('BlackContent')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RemoveBlackListResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveBlackListResponseBody, self).to_map()
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


class RemoveBlackListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveBlackListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveBlackListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveIpControlApisRequest(TeaModel):
    def __init__(self, api_ids=None, group_id=None, ip_control_id=None, security_token=None, stage_name=None):
        self.api_ids = api_ids  # type: str
        self.group_id = group_id  # type: str
        self.ip_control_id = ip_control_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveIpControlApisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveIpControlApisResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveIpControlApisResponseBody, self).to_map()
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


class RemoveIpControlApisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveIpControlApisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveIpControlApisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveIpControlApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveIpControlPolicyItemRequest(TeaModel):
    def __init__(self, ip_control_id=None, policy_item_ids=None, security_token=None):
        self.ip_control_id = ip_control_id  # type: str
        self.policy_item_ids = policy_item_ids  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveIpControlPolicyItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.policy_item_ids is not None:
            result['PolicyItemIds'] = self.policy_item_ids
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('PolicyItemIds') is not None:
            self.policy_item_ids = m.get('PolicyItemIds')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RemoveIpControlPolicyItemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveIpControlPolicyItemResponseBody, self).to_map()
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


class RemoveIpControlPolicyItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveIpControlPolicyItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveIpControlPolicyItemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveIpControlPolicyItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAppKeySecretRequest(TeaModel):
    def __init__(self, app_key=None, security_token=None):
        self.app_key = app_key  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAppKeySecretRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ResetAppKeySecretResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAppKeySecretResponseBody, self).to_map()
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


class ResetAppKeySecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetAppKeySecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetAppKeySecretResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetAppKeySecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetCustomizedRequest(TeaModel):
    def __init__(self, api_id=None, api_name=None, group_id=None, security_token=None, stage_id=None,
                 stage_name=None):
        self.api_id = api_id  # type: str
        self.api_name = api_name  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_id = stage_id  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetCustomizedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class ResetCustomizedResponseBodySdkDemosSdkDemo(TeaModel):
    def __init__(self, call_demo=None, ide_key=None):
        self.call_demo = call_demo  # type: str
        self.ide_key = ide_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetCustomizedResponseBodySdkDemosSdkDemo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_demo is not None:
            result['CallDemo'] = self.call_demo
        if self.ide_key is not None:
            result['IdeKey'] = self.ide_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallDemo') is not None:
            self.call_demo = m.get('CallDemo')
        if m.get('IdeKey') is not None:
            self.ide_key = m.get('IdeKey')
        return self


class ResetCustomizedResponseBodySdkDemos(TeaModel):
    def __init__(self, sdk_demo=None):
        self.sdk_demo = sdk_demo  # type: list[ResetCustomizedResponseBodySdkDemosSdkDemo]

    def validate(self):
        if self.sdk_demo:
            for k in self.sdk_demo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ResetCustomizedResponseBodySdkDemos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SdkDemo'] = []
        if self.sdk_demo is not None:
            for k in self.sdk_demo:
                result['SdkDemo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sdk_demo = []
        if m.get('SdkDemo') is not None:
            for k in m.get('SdkDemo'):
                temp_model = ResetCustomizedResponseBodySdkDemosSdkDemo()
                self.sdk_demo.append(temp_model.from_map(k))
        return self


class ResetCustomizedResponseBody(TeaModel):
    def __init__(self, request_id=None, sdk_demos=None):
        self.request_id = request_id  # type: str
        self.sdk_demos = sdk_demos  # type: ResetCustomizedResponseBodySdkDemos

    def validate(self):
        if self.sdk_demos:
            self.sdk_demos.validate()

    def to_map(self):
        _map = super(ResetCustomizedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_demos is not None:
            result['SdkDemos'] = self.sdk_demos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkDemos') is not None:
            temp_model = ResetCustomizedResponseBodySdkDemos()
            self.sdk_demos = temp_model.from_map(m['SdkDemos'])
        return self


class ResetCustomizedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetCustomizedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetCustomizedResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetCustomizedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SdkGenerateRequest(TeaModel):
    def __init__(self, app_id=None, group_id=None, language=None, security_token=None):
        self.app_id = app_id  # type: long
        self.group_id = group_id  # type: str
        self.language = language  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SdkGenerateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.language is not None:
            result['Language'] = self.language
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SdkGenerateResponseBody(TeaModel):
    def __init__(self, download_link=None, request_id=None):
        self.download_link = download_link  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SdkGenerateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SdkGenerateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SdkGenerateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SdkGenerateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SdkGenerateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SdkGenerateByAppRequest(TeaModel):
    def __init__(self, app_id=None, language=None, security_token=None):
        self.app_id = app_id  # type: long
        self.language = language  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SdkGenerateByAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.language is not None:
            result['Language'] = self.language
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SdkGenerateByAppResponseBody(TeaModel):
    def __init__(self, download_link=None, request_id=None):
        self.download_link = download_link  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SdkGenerateByAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SdkGenerateByAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SdkGenerateByAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SdkGenerateByAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SdkGenerateByAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SdkGenerateByGroupRequest(TeaModel):
    def __init__(self, group_id=None, language=None, security_token=None):
        self.group_id = group_id  # type: str
        self.language = language  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SdkGenerateByGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.language is not None:
            result['Language'] = self.language
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SdkGenerateByGroupResponseBody(TeaModel):
    def __init__(self, download_link=None, request_id=None):
        self.download_link = download_link  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SdkGenerateByGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SdkGenerateByGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SdkGenerateByGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SdkGenerateByGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SdkGenerateByGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccessPermissionByApisRequest(TeaModel):
    def __init__(self, api_ids=None, app_id=None, auth_valid_time=None, description=None, group_id=None,
                 security_token=None, stage_name=None):
        self.api_ids = api_ids  # type: str
        self.app_id = app_id  # type: long
        self.auth_valid_time = auth_valid_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAccessPermissionByApisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auth_valid_time is not None:
            result['AuthValidTime'] = self.auth_valid_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuthValidTime') is not None:
            self.auth_valid_time = m.get('AuthValidTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SetAccessPermissionByApisResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAccessPermissionByApisResponseBody, self).to_map()
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


class SetAccessPermissionByApisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetAccessPermissionByApisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetAccessPermissionByApisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetAccessPermissionByApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccessPermissionsRequest(TeaModel):
    def __init__(self, api_id=None, app_ids=None, description=None, group_id=None, security_token=None,
                 stage_name=None):
        self.api_id = api_id  # type: str
        self.app_ids = app_ids  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAccessPermissionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SetAccessPermissionsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAccessPermissionsResponseBody, self).to_map()
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


class SetAccessPermissionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetAccessPermissionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetAccessPermissionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetAccessPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApiRuleRequest(TeaModel):
    def __init__(self, api_ids=None, group_id=None, rule_id=None, rule_type=None, security_token=None,
                 stage_name=None):
        self.api_ids = api_ids  # type: str
        self.group_id = group_id  # type: str
        self.rule_id = rule_id  # type: str
        self.rule_type = rule_type  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApiRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SetApiRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApiRuleResponseBody, self).to_map()
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


class SetApiRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetApiRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetApiRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetApiRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainRequest(TeaModel):
    def __init__(self, bind_stage_name=None, certificate_body=None, certificate_name=None, domain_name=None,
                 group_id=None, is_force=None, private_key=None, security_token=None):
        self.bind_stage_name = bind_stage_name  # type: str
        self.certificate_body = certificate_body  # type: str
        self.certificate_name = certificate_name  # type: str
        self.domain_name = domain_name  # type: str
        self.group_id = group_id  # type: str
        self.is_force = is_force  # type: bool
        self.private_key = private_key  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_stage_name is not None:
            result['BindStageName'] = self.bind_stage_name
        if self.certificate_body is not None:
            result['CertificateBody'] = self.certificate_body
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.is_force is not None:
            result['IsForce'] = self.is_force
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindStageName') is not None:
            self.bind_stage_name = m.get('BindStageName')
        if m.get('CertificateBody') is not None:
            self.certificate_body = m.get('CertificateBody')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IsForce') is not None:
            self.is_force = m.get('IsForce')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetDomainResponseBody(TeaModel):
    def __init__(self, domain_binding_status=None, domain_legal_status=None, domain_name=None, domain_remark=None,
                 domain_web_socket_status=None, group_id=None, request_id=None, sub_domain=None):
        self.domain_binding_status = domain_binding_status  # type: str
        self.domain_legal_status = domain_legal_status  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_remark = domain_remark  # type: str
        self.domain_web_socket_status = domain_web_socket_status  # type: str
        self.group_id = group_id  # type: str
        self.request_id = request_id  # type: str
        self.sub_domain = sub_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_binding_status is not None:
            result['DomainBindingStatus'] = self.domain_binding_status
        if self.domain_legal_status is not None:
            result['DomainLegalStatus'] = self.domain_legal_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_remark is not None:
            result['DomainRemark'] = self.domain_remark
        if self.domain_web_socket_status is not None:
            result['DomainWebSocketStatus'] = self.domain_web_socket_status
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainBindingStatus') is not None:
            self.domain_binding_status = m.get('DomainBindingStatus')
        if m.get('DomainLegalStatus') is not None:
            self.domain_legal_status = m.get('DomainLegalStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainRemark') is not None:
            self.domain_remark = m.get('DomainRemark')
        if m.get('DomainWebSocketStatus') is not None:
            self.domain_web_socket_status = m.get('DomainWebSocketStatus')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class SetDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainCertificateRequest(TeaModel):
    def __init__(self, ca_certificate_body=None, certificate_body=None, certificate_name=None, domain_name=None,
                 group_id=None, private_key=None, security_token=None):
        self.ca_certificate_body = ca_certificate_body  # type: str
        self.certificate_body = certificate_body  # type: str
        self.certificate_name = certificate_name  # type: str
        self.domain_name = domain_name  # type: str
        self.group_id = group_id  # type: str
        self.private_key = private_key  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_certificate_body is not None:
            result['CaCertificateBody'] = self.ca_certificate_body
        if self.certificate_body is not None:
            result['CertificateBody'] = self.certificate_body
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaCertificateBody') is not None:
            self.ca_certificate_body = m.get('CaCertificateBody')
        if m.get('CertificateBody') is not None:
            self.certificate_body = m.get('CertificateBody')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetDomainCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainCertificateResponseBody, self).to_map()
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


class SetDomainCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDomainCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDomainCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainWebSocketStatusRequest(TeaModel):
    def __init__(self, action_value=None, domain_name=None, group_id=None, security_token=None):
        self.action_value = action_value  # type: str
        self.domain_name = domain_name  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainWebSocketStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_value is not None:
            result['ActionValue'] = self.action_value
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionValue') is not None:
            self.action_value = m.get('ActionValue')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetDomainWebSocketStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainWebSocketStatusResponseBody, self).to_map()
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


class SetDomainWebSocketStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDomainWebSocketStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDomainWebSocketStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetDomainWebSocketStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIpControlApisRequest(TeaModel):
    def __init__(self, api_ids=None, group_id=None, ip_control_id=None, security_token=None, stage_name=None):
        self.api_ids = api_ids  # type: str
        self.group_id = group_id  # type: str
        self.ip_control_id = ip_control_id  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetIpControlApisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SetIpControlApisResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetIpControlApisResponseBody, self).to_map()
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


class SetIpControlApisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetIpControlApisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetIpControlApisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetIpControlApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMockIntegrationRequest(TeaModel):
    def __init__(self, api_id=None, group_id=None, mock=None, mock_result=None, security_token=None):
        self.api_id = api_id  # type: str
        self.group_id = group_id  # type: str
        self.mock = mock  # type: str
        self.mock_result = mock_result  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMockIntegrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetMockIntegrationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMockIntegrationResponseBody, self).to_map()
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


class SetMockIntegrationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetMockIntegrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetMockIntegrationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetMockIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetWildcardDomainPatternsRequest(TeaModel):
    def __init__(self, domain_name=None, group_id=None, security_token=None, wildcard_domain_patterns=None):
        self.domain_name = domain_name  # type: str
        self.group_id = group_id  # type: str
        self.security_token = security_token  # type: str
        self.wildcard_domain_patterns = wildcard_domain_patterns  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetWildcardDomainPatternsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.wildcard_domain_patterns is not None:
            result['WildcardDomainPatterns'] = self.wildcard_domain_patterns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('WildcardDomainPatterns') is not None:
            self.wildcard_domain_patterns = m.get('WildcardDomainPatterns')
        return self


class SetWildcardDomainPatternsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetWildcardDomainPatternsResponseBody, self).to_map()
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


class SetWildcardDomainPatternsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetWildcardDomainPatternsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetWildcardDomainPatternsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetWildcardDomainPatternsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchApiRequest(TeaModel):
    def __init__(self, api_id=None, description=None, group_id=None, history_version=None, security_token=None,
                 stage_name=None):
        self.api_id = api_id  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.history_version = history_version  # type: str
        self.security_token = security_token  # type: str
        self.stage_name = stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SwitchApiResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchApiResponseBody, self).to_map()
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


class SwitchApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SwitchApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcDescribeAccessesRequest(TeaModel):
    def __init__(self, instance_id=None, instance_port=None, name=None, page_number=None, page_size=None,
                 security_token=None, vpc_id=None):
        self.instance_id = instance_id  # type: str
        self.instance_port = instance_port  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VpcDescribeAccessesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcDescribeAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute(TeaModel):
    def __init__(self, created_time=None, id=None, instance_id=None, modified_time=None, name=None, port=None,
                 region_id=None, status=None, user_id=None, vpc_id=None):
        self.created_time = created_time  # type: str
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.port = port  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.user_id = user_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VpcDescribeAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcDescribeAccessesResponseBodyVpcAccessAttributes(TeaModel):
    def __init__(self, vpc_access_attribute=None):
        self.vpc_access_attribute = vpc_access_attribute  # type: list[VpcDescribeAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute]

    def validate(self):
        if self.vpc_access_attribute:
            for k in self.vpc_access_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VpcDescribeAccessesResponseBodyVpcAccessAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VpcAccessAttribute'] = []
        if self.vpc_access_attribute is not None:
            for k in self.vpc_access_attribute:
                result['VpcAccessAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vpc_access_attribute = []
        if m.get('VpcAccessAttribute') is not None:
            for k in m.get('VpcAccessAttribute'):
                temp_model = VpcDescribeAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute()
                self.vpc_access_attribute.append(temp_model.from_map(k))
        return self


class VpcDescribeAccessesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None,
                 vpc_access_attributes=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.vpc_access_attributes = vpc_access_attributes  # type: VpcDescribeAccessesResponseBodyVpcAccessAttributes

    def validate(self):
        if self.vpc_access_attributes:
            self.vpc_access_attributes.validate()

    def to_map(self):
        _map = super(VpcDescribeAccessesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vpc_access_attributes is not None:
            result['VpcAccessAttributes'] = self.vpc_access_attributes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VpcAccessAttributes') is not None:
            temp_model = VpcDescribeAccessesResponseBodyVpcAccessAttributes()
            self.vpc_access_attributes = temp_model.from_map(m['VpcAccessAttributes'])
        return self


class VpcDescribeAccessesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VpcDescribeAccessesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VpcDescribeAccessesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VpcDescribeAccessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcGrantAccessRequest(TeaModel):
    def __init__(self, instance_id=None, instance_port=None, name=None, security_token=None, token=None, vpc_id=None):
        self.instance_id = instance_id  # type: str
        self.instance_port = instance_port  # type: str
        self.name = name  # type: str
        self.security_token = security_token  # type: str
        self.token = token  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VpcGrantAccessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.name is not None:
            result['Name'] = self.name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.token is not None:
            result['Token'] = self.token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcGrantAccessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VpcGrantAccessResponseBody, self).to_map()
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


class VpcGrantAccessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VpcGrantAccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VpcGrantAccessResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VpcGrantAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcModifyAccessRequest(TeaModel):
    def __init__(self, instance_id=None, instance_port=None, security_token=None, token=None, vpc_id=None):
        self.instance_id = instance_id  # type: str
        self.instance_port = instance_port  # type: str
        self.security_token = security_token  # type: str
        self.token = token  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VpcModifyAccessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.token is not None:
            result['Token'] = self.token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcModifyAccessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VpcModifyAccessResponseBody, self).to_map()
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


class VpcModifyAccessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VpcModifyAccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VpcModifyAccessResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VpcModifyAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcRevokeAccessRequest(TeaModel):
    def __init__(self, instance_id=None, instance_port=None, security_token=None, token=None, vpc_id=None):
        self.instance_id = instance_id  # type: str
        self.instance_port = instance_port  # type: str
        self.security_token = security_token  # type: str
        self.token = token  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VpcRevokeAccessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.token is not None:
            result['Token'] = self.token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcRevokeAccessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VpcRevokeAccessResponseBody, self).to_map()
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


class VpcRevokeAccessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VpcRevokeAccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VpcRevokeAccessResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VpcRevokeAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


