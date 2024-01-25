# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AttachApplication2ConnectorRequest(TeaModel):
    def __init__(self, application_ids=None, connector_id=None):
        self.application_ids = application_ids  # type: list[str]
        # ConnectorID。
        self.connector_id = connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachApplication2ConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        return self


class AttachApplication2ConnectorShrinkRequest(TeaModel):
    def __init__(self, application_ids_shrink=None, connector_id=None):
        self.application_ids_shrink = application_ids_shrink  # type: str
        # ConnectorID。
        self.connector_id = connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachApplication2ConnectorShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids_shrink is not None:
            result['ApplicationIds'] = self.application_ids_shrink
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids_shrink = m.get('ApplicationIds')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        return self


class AttachApplication2ConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachApplication2ConnectorResponseBody, self).to_map()
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


class AttachApplication2ConnectorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachApplication2ConnectorResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachApplication2ConnectorResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachApplication2ConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDynamicRouteRequest(TeaModel):
    def __init__(self, application_ids=None, application_type=None, description=None, dynamic_route_type=None,
                 name=None, next_hop=None, priority=None, region_ids=None, status=None, tag_ids=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.description = description  # type: str
        self.dynamic_route_type = dynamic_route_type  # type: str
        self.name = name  # type: str
        self.next_hop = next_hop  # type: str
        self.priority = priority  # type: int
        self.region_ids = region_ids  # type: list[str]
        self.status = status  # type: str
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDynamicRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_route_type is not None:
            result['DynamicRouteType'] = self.dynamic_route_type
        if self.name is not None:
            result['Name'] = self.name
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicRouteType') is not None:
            self.dynamic_route_type = m.get('DynamicRouteType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class CreateDynamicRouteResponseBody(TeaModel):
    def __init__(self, dynamic_route_id=None, request_id=None):
        self.dynamic_route_id = dynamic_route_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDynamicRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDynamicRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDynamicRouteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDynamicRouteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrivateAccessApplicationRequestPortRanges(TeaModel):
    def __init__(self, begin=None, end=None):
        self.begin = begin  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrivateAccessApplicationRequestPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class CreatePrivateAccessApplicationRequest(TeaModel):
    def __init__(self, addresses=None, description=None, name=None, port_ranges=None, protocol=None, status=None,
                 tag_ids=None):
        self.addresses = addresses  # type: list[str]
        self.description = description  # type: str
        self.name = name  # type: str
        self.port_ranges = port_ranges  # type: list[CreatePrivateAccessApplicationRequestPortRanges]
        self.protocol = protocol  # type: str
        self.status = status  # type: str
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePrivateAccessApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreatePrivateAccessApplicationRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class CreatePrivateAccessApplicationResponseBody(TeaModel):
    def __init__(self, application_id=None, request_id=None):
        self.application_id = application_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrivateAccessApplicationResponseBody, self).to_map()
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


class CreatePrivateAccessApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePrivateAccessApplicationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePrivateAccessApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrivateAccessPolicyRequestCustomUserAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrivateAccessPolicyRequestCustomUserAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePrivateAccessPolicyRequest(TeaModel):
    def __init__(self, application_ids=None, application_type=None, custom_user_attributes=None, description=None,
                 device_attribute_id=None, name=None, policy_action=None, priority=None, status=None, tag_ids=None, user_group_ids=None,
                 user_group_mode=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.custom_user_attributes = custom_user_attributes  # type: list[CreatePrivateAccessPolicyRequestCustomUserAttributes]
        self.description = description  # type: str
        self.device_attribute_id = device_attribute_id  # type: str
        self.name = name  # type: str
        self.policy_action = policy_action  # type: str
        self.priority = priority  # type: int
        self.status = status  # type: str
        # 内网访问标签ID集合。最多可输入100个内网访问标签ID。当**ApplicationType**为**Tag时**，必填。和**ApplicationIds**互斥。
        self.tag_ids = tag_ids  # type: list[str]
        self.user_group_ids = user_group_ids  # type: list[str]
        # 内网访问策略的用户组类型。取值：
        # - **Normal**：普通用户组。
        # - **Custom**：自定义用户组。
        self.user_group_mode = user_group_mode  # type: str

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePrivateAccessPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.device_attribute_id is not None:
            result['DeviceAttributeId'] = self.device_attribute_id
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = CreatePrivateAccessPolicyRequestCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceAttributeId') is not None:
            self.device_attribute_id = m.get('DeviceAttributeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')
        return self


class CreatePrivateAccessPolicyResponseBody(TeaModel):
    def __init__(self, policy_id=None, request_id=None):
        self.policy_id = policy_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrivateAccessPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePrivateAccessPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePrivateAccessPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePrivateAccessPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrivateAccessTagRequest(TeaModel):
    def __init__(self, description=None, name=None):
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrivateAccessTagRequest, self).to_map()
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


class CreatePrivateAccessTagResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_id=None):
        self.request_id = request_id  # type: str
        self.tag_id = tag_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrivateAccessTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class CreatePrivateAccessTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePrivateAccessTagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePrivateAccessTagResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePrivateAccessTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRegistrationPolicyRequestCompanyLimitCount(TeaModel):
    def __init__(self, all=None, mobile=None, pc=None):
        self.all = all  # type: int
        self.mobile = mobile  # type: int
        self.pc = pc  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRegistrationPolicyRequestCompanyLimitCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class CreateRegistrationPolicyRequestPersonalLimitCount(TeaModel):
    def __init__(self, all=None, mobile=None, pc=None):
        self.all = all  # type: int
        self.mobile = mobile  # type: int
        self.pc = pc  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRegistrationPolicyRequestPersonalLimitCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class CreateRegistrationPolicyRequest(TeaModel):
    def __init__(self, company_limit_count=None, company_limit_type=None, description=None, match_mode=None,
                 name=None, personal_limit_count=None, personal_limit_type=None, priority=None, status=None,
                 user_group_ids=None, whitelist=None):
        self.company_limit_count = company_limit_count  # type: CreateRegistrationPolicyRequestCompanyLimitCount
        self.company_limit_type = company_limit_type  # type: str
        self.description = description  # type: str
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.personal_limit_count = personal_limit_count  # type: CreateRegistrationPolicyRequestPersonalLimitCount
        self.personal_limit_type = personal_limit_type  # type: str
        self.priority = priority  # type: long
        self.status = status  # type: str
        self.user_group_ids = user_group_ids  # type: list[str]
        self.whitelist = whitelist  # type: list[str]

    def validate(self):
        if self.company_limit_count:
            self.company_limit_count.validate()
        if self.personal_limit_count:
            self.personal_limit_count.validate()

    def to_map(self):
        _map = super(CreateRegistrationPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_limit_count is not None:
            result['CompanyLimitCount'] = self.company_limit_count.to_map()
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type
        if self.description is not None:
            result['Description'] = self.description
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.personal_limit_count is not None:
            result['PersonalLimitCount'] = self.personal_limit_count.to_map()
        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompanyLimitCount') is not None:
            temp_model = CreateRegistrationPolicyRequestCompanyLimitCount()
            self.company_limit_count = temp_model.from_map(m['CompanyLimitCount'])
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonalLimitCount') is not None:
            temp_model = CreateRegistrationPolicyRequestPersonalLimitCount()
            self.personal_limit_count = temp_model.from_map(m['PersonalLimitCount'])
        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class CreateRegistrationPolicyShrinkRequest(TeaModel):
    def __init__(self, company_limit_count_shrink=None, company_limit_type=None, description=None, match_mode=None,
                 name=None, personal_limit_count_shrink=None, personal_limit_type=None, priority=None, status=None,
                 user_group_ids=None, whitelist=None):
        self.company_limit_count_shrink = company_limit_count_shrink  # type: str
        self.company_limit_type = company_limit_type  # type: str
        self.description = description  # type: str
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.personal_limit_count_shrink = personal_limit_count_shrink  # type: str
        self.personal_limit_type = personal_limit_type  # type: str
        self.priority = priority  # type: long
        self.status = status  # type: str
        self.user_group_ids = user_group_ids  # type: list[str]
        self.whitelist = whitelist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRegistrationPolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_limit_count_shrink is not None:
            result['CompanyLimitCount'] = self.company_limit_count_shrink
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type
        if self.description is not None:
            result['Description'] = self.description
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.personal_limit_count_shrink is not None:
            result['PersonalLimitCount'] = self.personal_limit_count_shrink
        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompanyLimitCount') is not None:
            self.company_limit_count_shrink = m.get('CompanyLimitCount')
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonalLimitCount') is not None:
            self.personal_limit_count_shrink = m.get('PersonalLimitCount')
        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class CreateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount(TeaModel):
    def __init__(self, all=None, mobile=None, pc=None):
        self.all = all  # type: int
        self.mobile = mobile  # type: int
        self.pc = pc  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class CreateRegistrationPolicyResponseBodyPolicyLimitDetail(TeaModel):
    def __init__(self, device_belong=None, limit_count=None, limit_type=None):
        self.device_belong = device_belong  # type: str
        self.limit_count = limit_count  # type: CreateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount
        self.limit_type = limit_type  # type: str

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        _map = super(CreateRegistrationPolicyResponseBodyPolicyLimitDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('LimitCount') is not None:
            temp_model = CreateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m['LimitCount'])
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class CreateRegistrationPolicyResponseBodyPolicy(TeaModel):
    def __init__(self, create_time=None, description=None, limit_detail=None, match_mode=None, name=None,
                 policy_id=None, priority=None, status=None, user_group_ids=None, whitelist=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.limit_detail = limit_detail  # type: list[CreateRegistrationPolicyResponseBodyPolicyLimitDetail]
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: str
        self.status = status  # type: str
        self.user_group_ids = user_group_ids  # type: list[str]
        self.whitelist = whitelist  # type: list[str]

    def validate(self):
        if self.limit_detail:
            for k in self.limit_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateRegistrationPolicyResponseBodyPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k in self.limit_detail:
                result['LimitDetail'].append(k.to_map() if k else None)
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k in m.get('LimitDetail'):
                temp_model = CreateRegistrationPolicyResponseBodyPolicyLimitDetail()
                self.limit_detail.append(temp_model.from_map(k))
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class CreateRegistrationPolicyResponseBody(TeaModel):
    def __init__(self, policy=None, request_id=None):
        self.policy = policy  # type: CreateRegistrationPolicyResponseBodyPolicy
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(CreateRegistrationPolicyResponseBody, self).to_map()
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
            temp_model = CreateRegistrationPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRegistrationPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRegistrationPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRegistrationPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRegistrationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupRequestAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserGroupRequestAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(self, attributes=None, description=None, name=None):
        self.attributes = attributes  # type: list[CreateUserGroupRequestAttributes]
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = CreateUserGroupRequestAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDynamicRouteRequest(TeaModel):
    def __init__(self, dynamic_route_id=None):
        self.dynamic_route_id = dynamic_route_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDynamicRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        return self


class DeleteDynamicRouteResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDynamicRouteResponseBody, self).to_map()
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


class DeleteDynamicRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDynamicRouteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDynamicRouteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrivateAccessApplicationRequest(TeaModel):
    def __init__(self, application_id=None):
        self.application_id = application_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrivateAccessApplicationRequest, self).to_map()
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


class DeletePrivateAccessApplicationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrivateAccessApplicationResponseBody, self).to_map()
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


class DeletePrivateAccessApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePrivateAccessApplicationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePrivateAccessApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrivateAccessPolicyRequest(TeaModel):
    def __init__(self, policy_id=None):
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrivateAccessPolicyRequest, self).to_map()
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


class DeletePrivateAccessPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrivateAccessPolicyResponseBody, self).to_map()
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


class DeletePrivateAccessPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePrivateAccessPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePrivateAccessPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrivateAccessTagRequest(TeaModel):
    def __init__(self, tag_id=None):
        self.tag_id = tag_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrivateAccessTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class DeletePrivateAccessTagResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrivateAccessTagResponseBody, self).to_map()
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


class DeletePrivateAccessTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePrivateAccessTagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePrivateAccessTagResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePrivateAccessTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRegistrationPoliciesRequest(TeaModel):
    def __init__(self, policy_ids=None):
        self.policy_ids = policy_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRegistrationPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        return self


class DeleteRegistrationPoliciesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRegistrationPoliciesResponseBody, self).to_map()
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


class DeleteRegistrationPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRegistrationPoliciesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRegistrationPoliciesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRegistrationPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(self, user_group_id=None):
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachApplication2ConnectorRequest(TeaModel):
    def __init__(self, application_ids=None, connector_id=None):
        self.application_ids = application_ids  # type: list[str]
        # ConnectorID。
        self.connector_id = connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachApplication2ConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        return self


class DetachApplication2ConnectorShrinkRequest(TeaModel):
    def __init__(self, application_ids_shrink=None, connector_id=None):
        self.application_ids_shrink = application_ids_shrink  # type: str
        # ConnectorID。
        self.connector_id = connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachApplication2ConnectorShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids_shrink is not None:
            result['ApplicationIds'] = self.application_ids_shrink
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids_shrink = m.get('ApplicationIds')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        return self


class DetachApplication2ConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachApplication2ConnectorResponseBody, self).to_map()
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


class DetachApplication2ConnectorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachApplication2ConnectorResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachApplication2ConnectorResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachApplication2ConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDynamicRouteRequest(TeaModel):
    def __init__(self, dynamic_route_id=None):
        self.dynamic_route_id = dynamic_route_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDynamicRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        return self


class GetDynamicRouteResponseBodyDynamicRoute(TeaModel):
    def __init__(self, application_ids=None, application_type=None, create_time=None, description=None,
                 dynamic_route_id=None, dynamic_route_type=None, name=None, next_hop=None, priority=None, region_ids=None,
                 status=None, tag_ids=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.dynamic_route_id = dynamic_route_id  # type: str
        self.dynamic_route_type = dynamic_route_type  # type: str
        self.name = name  # type: str
        self.next_hop = next_hop  # type: str
        self.priority = priority  # type: int
        self.region_ids = region_ids  # type: list[str]
        self.status = status  # type: str
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDynamicRouteResponseBodyDynamicRoute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        if self.dynamic_route_type is not None:
            result['DynamicRouteType'] = self.dynamic_route_type
        if self.name is not None:
            result['Name'] = self.name
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        if m.get('DynamicRouteType') is not None:
            self.dynamic_route_type = m.get('DynamicRouteType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class GetDynamicRouteResponseBody(TeaModel):
    def __init__(self, dynamic_route=None, request_id=None):
        self.dynamic_route = dynamic_route  # type: GetDynamicRouteResponseBodyDynamicRoute
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dynamic_route:
            self.dynamic_route.validate()

    def to_map(self):
        _map = super(GetDynamicRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route is not None:
            result['DynamicRoute'] = self.dynamic_route.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicRoute') is not None:
            temp_model = GetDynamicRouteResponseBodyDynamicRoute()
            self.dynamic_route = temp_model.from_map(m['DynamicRoute'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDynamicRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDynamicRouteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDynamicRouteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrivateAccessApplicationRequest(TeaModel):
    def __init__(self, application_id=None):
        self.application_id = application_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrivateAccessApplicationRequest, self).to_map()
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


class GetPrivateAccessApplicationResponseBodyApplicationPortRanges(TeaModel):
    def __init__(self, begin=None, end=None):
        self.begin = begin  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrivateAccessApplicationResponseBodyApplicationPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class GetPrivateAccessApplicationResponseBodyApplication(TeaModel):
    def __init__(self, addresses=None, application_id=None, connector_ids=None, create_time=None, description=None,
                 name=None, policy_ids=None, port_ranges=None, protocol=None, status=None, tag_ids=None):
        self.addresses = addresses  # type: list[str]
        self.application_id = application_id  # type: str
        self.connector_ids = connector_ids  # type: list[str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.policy_ids = policy_ids  # type: list[str]
        self.port_ranges = port_ranges  # type: list[GetPrivateAccessApplicationResponseBodyApplicationPortRanges]
        self.protocol = protocol  # type: str
        self.status = status  # type: str
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPrivateAccessApplicationResponseBodyApplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.connector_ids is not None:
            result['ConnectorIds'] = self.connector_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ConnectorIds') is not None:
            self.connector_ids = m.get('ConnectorIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = GetPrivateAccessApplicationResponseBodyApplicationPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class GetPrivateAccessApplicationResponseBody(TeaModel):
    def __init__(self, application=None, request_id=None):
        self.application = application  # type: GetPrivateAccessApplicationResponseBodyApplication
        self.request_id = request_id  # type: str

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super(GetPrivateAccessApplicationResponseBody, self).to_map()
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
            temp_model = GetPrivateAccessApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPrivateAccessApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPrivateAccessApplicationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPrivateAccessApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrivateAccessPolicyRequest(TeaModel):
    def __init__(self, policy_id=None):
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrivateAccessPolicyRequest, self).to_map()
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


class GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetPrivateAccessPolicyResponseBodyPolicy(TeaModel):
    def __init__(self, application_ids=None, application_type=None, create_time=None, custom_user_attributes=None,
                 description=None, device_attribute_id=None, name=None, policy_action=None, policy_id=None, priority=None,
                 status=None, tag_ids=None, user_group_ids=None, user_group_mode=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.create_time = create_time  # type: str
        self.custom_user_attributes = custom_user_attributes  # type: list[GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes]
        self.description = description  # type: str
        self.device_attribute_id = device_attribute_id  # type: str
        self.name = name  # type: str
        self.policy_action = policy_action  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: int
        self.status = status  # type: str
        self.tag_ids = tag_ids  # type: list[str]
        self.user_group_ids = user_group_ids  # type: list[str]
        self.user_group_mode = user_group_mode  # type: str

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPrivateAccessPolicyResponseBodyPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.device_attribute_id is not None:
            result['DeviceAttributeId'] = self.device_attribute_id
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceAttributeId') is not None:
            self.device_attribute_id = m.get('DeviceAttributeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')
        return self


class GetPrivateAccessPolicyResponseBody(TeaModel):
    def __init__(self, policy=None, request_id=None):
        self.policy = policy  # type: GetPrivateAccessPolicyResponseBodyPolicy
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(GetPrivateAccessPolicyResponseBody, self).to_map()
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
            temp_model = GetPrivateAccessPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPrivateAccessPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPrivateAccessPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPrivateAccessPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegistrationPolicyRequest(TeaModel):
    def __init__(self, policy_id=None):
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegistrationPolicyRequest, self).to_map()
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


class GetRegistrationPolicyResponseBodyLimitDetailLimitCount(TeaModel):
    def __init__(self, all=None, mobile=None, pc=None):
        self.all = all  # type: int
        self.mobile = mobile  # type: int
        self.pc = pc  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegistrationPolicyResponseBodyLimitDetailLimitCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class GetRegistrationPolicyResponseBodyLimitDetail(TeaModel):
    def __init__(self, device_belong=None, limit_count=None, limit_type=None):
        self.device_belong = device_belong  # type: str
        self.limit_count = limit_count  # type: GetRegistrationPolicyResponseBodyLimitDetailLimitCount
        self.limit_type = limit_type  # type: str

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        _map = super(GetRegistrationPolicyResponseBodyLimitDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('LimitCount') is not None:
            temp_model = GetRegistrationPolicyResponseBodyLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m['LimitCount'])
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class GetRegistrationPolicyResponseBody(TeaModel):
    def __init__(self, create_time=None, description=None, limit_detail=None, match_mode=None, name=None,
                 policy_id=None, priority=None, request_id=None, status=None, user_group_ids=None, whitelist=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.limit_detail = limit_detail  # type: list[GetRegistrationPolicyResponseBodyLimitDetail]
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: long
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.user_group_ids = user_group_ids  # type: list[str]
        self.whitelist = whitelist  # type: list[str]

    def validate(self):
        if self.limit_detail:
            for k in self.limit_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRegistrationPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k in self.limit_detail:
                result['LimitDetail'].append(k.to_map() if k else None)
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k in m.get('LimitDetail'):
                temp_model = GetRegistrationPolicyResponseBodyLimitDetail()
                self.limit_detail.append(temp_model.from_map(k))
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class GetRegistrationPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRegistrationPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRegistrationPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRegistrationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserDeviceRequest(TeaModel):
    def __init__(self, device_tag=None):
        self.device_tag = device_tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        return self


class GetUserDeviceResponseBodyDeviceHistoryUsers(TeaModel):
    def __init__(self, sase_user_id=None, username=None):
        self.sase_user_id = sase_user_id  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserDeviceResponseBodyDeviceHistoryUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetUserDeviceResponseBodyDevice(TeaModel):
    def __init__(self, app_status=None, app_version=None, cpu=None, create_time=None, department=None,
                 device_belong=None, device_model=None, device_status=None, device_tag=None, device_type=None,
                 device_version=None, disk=None, dlp_status=None, history_users=None, hostname=None, ia_status=None, inner_ip=None,
                 mac=None, memory=None, nac_status=None, pa_status=None, sase_user_id=None, sharing_status=None,
                 src_ip=None, update_time=None, username=None):
        self.app_status = app_status  # type: str
        self.app_version = app_version  # type: str
        self.cpu = cpu  # type: str
        self.create_time = create_time  # type: str
        self.department = department  # type: str
        self.device_belong = device_belong  # type: str
        self.device_model = device_model  # type: str
        self.device_status = device_status  # type: str
        self.device_tag = device_tag  # type: str
        self.device_type = device_type  # type: str
        self.device_version = device_version  # type: str
        self.disk = disk  # type: str
        self.dlp_status = dlp_status  # type: str
        self.history_users = history_users  # type: list[GetUserDeviceResponseBodyDeviceHistoryUsers]
        self.hostname = hostname  # type: str
        self.ia_status = ia_status  # type: str
        self.inner_ip = inner_ip  # type: str
        self.mac = mac  # type: str
        self.memory = memory  # type: str
        self.nac_status = nac_status  # type: str
        self.pa_status = pa_status  # type: str
        self.sase_user_id = sase_user_id  # type: str
        self.sharing_status = sharing_status  # type: bool
        self.src_ip = src_ip  # type: str
        self.update_time = update_time  # type: str
        self.username = username  # type: str

    def validate(self):
        if self.history_users:
            for k in self.history_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserDeviceResponseBodyDevice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_version is not None:
            result['DeviceVersion'] = self.device_version
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status
        result['HistoryUsers'] = []
        if self.history_users is not None:
            for k in self.history_users:
                result['HistoryUsers'].append(k.to_map() if k else None)
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_status is not None:
            result['IaStatus'] = self.ia_status
        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.nac_status is not None:
            result['NacStatus'] = self.nac_status
        if self.pa_status is not None:
            result['PaStatus'] = self.pa_status
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceVersion') is not None:
            self.device_version = m.get('DeviceVersion')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')
        self.history_users = []
        if m.get('HistoryUsers') is not None:
            for k in m.get('HistoryUsers'):
                temp_model = GetUserDeviceResponseBodyDeviceHistoryUsers()
                self.history_users.append(temp_model.from_map(k))
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatus') is not None:
            self.ia_status = m.get('IaStatus')
        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')
        if m.get('PaStatus') is not None:
            self.pa_status = m.get('PaStatus')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetUserDeviceResponseBody(TeaModel):
    def __init__(self, device=None, request_id=None):
        self.device = device  # type: GetUserDeviceResponseBodyDevice
        self.request_id = request_id  # type: str

    def validate(self):
        if self.device:
            self.device.validate()

    def to_map(self):
        _map = super(GetUserDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device is not None:
            result['Device'] = self.device.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Device') is not None:
            temp_model = GetUserDeviceResponseBodyDevice()
            self.device = temp_model.from_map(m['Device'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserDeviceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGroupRequest(TeaModel):
    def __init__(self, user_group_id=None):
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class GetUserGroupResponseBodyUserGroupAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserGroupResponseBodyUserGroupAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetUserGroupResponseBodyUserGroup(TeaModel):
    def __init__(self, attributes=None, create_time=None, description=None, name=None, user_group_id=None):
        self.attributes = attributes  # type: list[GetUserGroupResponseBodyUserGroupAttributes]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserGroupResponseBodyUserGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = GetUserGroupResponseBodyUserGroupAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsForPrivateAccessPolicyRequest(TeaModel):
    def __init__(self, policy_ids=None):
        self.policy_ids = policy_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        return self


class ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplicationsPortRanges(TeaModel):
    def __init__(self, begin=None, end=None):
        self.begin = begin  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplicationsPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplications(TeaModel):
    def __init__(self, addresses=None, application_id=None, create_time=None, description=None, name=None,
                 port_ranges=None, protocol=None, status=None):
        self.addresses = addresses  # type: list[str]
        self.application_id = application_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.port_ranges = port_ranges  # type: list[ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplicationsPortRanges]
        self.protocol = protocol  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplicationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationsForPrivateAccessPolicyResponseBodyPolices(TeaModel):
    def __init__(self, applications=None, policy_id=None):
        self.applications = applications  # type: list[ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplications]
        self.policy_id = policy_id  # type: str

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessPolicyResponseBodyPolices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsForPrivateAccessPolicyResponseBodyPolicesApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class ListApplicationsForPrivateAccessPolicyResponseBody(TeaModel):
    def __init__(self, polices=None, request_id=None):
        self.polices = polices  # type: list[ListApplicationsForPrivateAccessPolicyResponseBodyPolices]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListApplicationsForPrivateAccessPolicyResponseBodyPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApplicationsForPrivateAccessPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationsForPrivateAccessPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListApplicationsForPrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsForPrivateAccessTagRequest(TeaModel):
    def __init__(self, tag_ids=None):
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListApplicationsForPrivateAccessTagResponseBodyTagsApplicationsPortRanges(TeaModel):
    def __init__(self, begin=None, end=None):
        self.begin = begin  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessTagResponseBodyTagsApplicationsPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class ListApplicationsForPrivateAccessTagResponseBodyTagsApplications(TeaModel):
    def __init__(self, addresses=None, application_id=None, create_time=None, description=None, name=None,
                 port_ranges=None, protocol=None, status=None):
        self.addresses = addresses  # type: list[str]
        self.application_id = application_id  # type: str
        # 内网访问应用创建时间。
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.port_ranges = port_ranges  # type: list[ListApplicationsForPrivateAccessTagResponseBodyTagsApplicationsPortRanges]
        self.protocol = protocol  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessTagResponseBodyTagsApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListApplicationsForPrivateAccessTagResponseBodyTagsApplicationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationsForPrivateAccessTagResponseBodyTags(TeaModel):
    def __init__(self, applications=None, tag_id=None):
        self.applications = applications  # type: list[ListApplicationsForPrivateAccessTagResponseBodyTagsApplications]
        self.tag_id = tag_id  # type: str

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessTagResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsForPrivateAccessTagResponseBodyTagsApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListApplicationsForPrivateAccessTagResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None):
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[ListApplicationsForPrivateAccessTagResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListApplicationsForPrivateAccessTagResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListApplicationsForPrivateAccessTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationsForPrivateAccessTagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationsForPrivateAccessTagResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListApplicationsForPrivateAccessTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectorsRequest(TeaModel):
    def __init__(self, connector_ids=None, current_page=None, name=None, page_size=None, status=None,
                 switch_status=None):
        self.connector_ids = connector_ids  # type: list[str]
        self.current_page = current_page  # type: int
        self.name = name  # type: str
        self.page_size = page_size  # type: int
        self.status = status  # type: str
        self.switch_status = switch_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connector_ids is not None:
            result['ConnectorIds'] = self.connector_ids
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectorIds') is not None:
            self.connector_ids = m.get('ConnectorIds')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        return self


class ListConnectorsResponseBodyConnectorsApplications(TeaModel):
    def __init__(self, application_id=None, application_name=None):
        self.application_id = application_id  # type: str
        self.application_name = application_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectorsResponseBodyConnectorsApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        return self


class ListConnectorsResponseBodyConnectorsConnectorClients(TeaModel):
    def __init__(self, connection_status=None, dev_tag=None, hostname=None, public_ip=None):
        self.connection_status = connection_status  # type: str
        self.dev_tag = dev_tag  # type: str
        self.hostname = hostname  # type: str
        self.public_ip = public_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectorsResponseBodyConnectorsConnectorClients, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        return self


class ListConnectorsResponseBodyConnectorsUpgradeTime(TeaModel):
    def __init__(self, end=None, start=None):
        self.end = end  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectorsResponseBodyConnectorsUpgradeTime, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class ListConnectorsResponseBodyConnectors(TeaModel):
    def __init__(self, applications=None, connector_clients=None, connector_id=None, create_time=None, name=None,
                 region_id=None, status=None, switch_status=None, upgrade_time=None):
        self.applications = applications  # type: list[ListConnectorsResponseBodyConnectorsApplications]
        self.connector_clients = connector_clients  # type: list[ListConnectorsResponseBodyConnectorsConnectorClients]
        # ConnectorID。
        self.connector_id = connector_id  # type: str
        self.create_time = create_time  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.switch_status = switch_status  # type: str
        self.upgrade_time = upgrade_time  # type: ListConnectorsResponseBodyConnectorsUpgradeTime

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()
        if self.connector_clients:
            for k in self.connector_clients:
                if k:
                    k.validate()
        if self.upgrade_time:
            self.upgrade_time.validate()

    def to_map(self):
        _map = super(ListConnectorsResponseBodyConnectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        result['ConnectorClients'] = []
        if self.connector_clients is not None:
            for k in self.connector_clients:
                result['ConnectorClients'].append(k.to_map() if k else None)
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        if self.upgrade_time is not None:
            result['UpgradeTime'] = self.upgrade_time.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListConnectorsResponseBodyConnectorsApplications()
                self.applications.append(temp_model.from_map(k))
        self.connector_clients = []
        if m.get('ConnectorClients') is not None:
            for k in m.get('ConnectorClients'):
                temp_model = ListConnectorsResponseBodyConnectorsConnectorClients()
                self.connector_clients.append(temp_model.from_map(k))
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        if m.get('UpgradeTime') is not None:
            temp_model = ListConnectorsResponseBodyConnectorsUpgradeTime()
            self.upgrade_time = temp_model.from_map(m['UpgradeTime'])
        return self


class ListConnectorsResponseBody(TeaModel):
    def __init__(self, connectors=None, request_id=None, total_num=None):
        self.connectors = connectors  # type: list[ListConnectorsResponseBodyConnectors]
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int

    def validate(self):
        if self.connectors:
            for k in self.connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConnectorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Connectors'] = []
        if self.connectors is not None:
            for k in self.connectors:
                result['Connectors'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connectors = []
        if m.get('Connectors') is not None:
            for k in m.get('Connectors'):
                temp_model = ListConnectorsResponseBodyConnectors()
                self.connectors.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListConnectorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConnectorsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConnectorsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConnectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDynamicRouteRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None, total_num=None):
        self.regions = regions  # type: list[str]
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDynamicRouteRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListDynamicRouteRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDynamicRouteRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDynamicRouteRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDynamicRouteRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDynamicRoutesRequest(TeaModel):
    def __init__(self, application_id=None, current_page=None, dynamic_route_ids=None, name=None, next_hop=None,
                 page_size=None, region_ids=None, status=None, tag_id=None):
        self.application_id = application_id  # type: str
        self.current_page = current_page  # type: int
        self.dynamic_route_ids = dynamic_route_ids  # type: list[str]
        self.name = name  # type: str
        self.next_hop = next_hop  # type: str
        self.page_size = page_size  # type: int
        self.region_ids = region_ids  # type: list[str]
        self.status = status  # type: str
        self.tag_id = tag_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDynamicRoutesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dynamic_route_ids is not None:
            result['DynamicRouteIds'] = self.dynamic_route_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DynamicRouteIds') is not None:
            self.dynamic_route_ids = m.get('DynamicRouteIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListDynamicRoutesResponseBodyDynamicRoutes(TeaModel):
    def __init__(self, application_ids=None, application_type=None, create_time=None, description=None,
                 dynamic_route_id=None, dynamic_route_type=None, name=None, next_hop=None, priority=None, region_ids=None,
                 status=None, tag_ids=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.dynamic_route_id = dynamic_route_id  # type: str
        self.dynamic_route_type = dynamic_route_type  # type: str
        self.name = name  # type: str
        self.next_hop = next_hop  # type: str
        self.priority = priority  # type: int
        self.region_ids = region_ids  # type: list[str]
        self.status = status  # type: str
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDynamicRoutesResponseBodyDynamicRoutes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        if self.dynamic_route_type is not None:
            result['DynamicRouteType'] = self.dynamic_route_type
        if self.name is not None:
            result['Name'] = self.name
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        if m.get('DynamicRouteType') is not None:
            self.dynamic_route_type = m.get('DynamicRouteType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListDynamicRoutesResponseBody(TeaModel):
    def __init__(self, dynamic_routes=None, request_id=None, total_num=None):
        self.dynamic_routes = dynamic_routes  # type: list[ListDynamicRoutesResponseBodyDynamicRoutes]
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int

    def validate(self):
        if self.dynamic_routes:
            for k in self.dynamic_routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDynamicRoutesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DynamicRoutes'] = []
        if self.dynamic_routes is not None:
            for k in self.dynamic_routes:
                result['DynamicRoutes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dynamic_routes = []
        if m.get('DynamicRoutes') is not None:
            for k in m.get('DynamicRoutes'):
                temp_model = ListDynamicRoutesResponseBodyDynamicRoutes()
                self.dynamic_routes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListDynamicRoutesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDynamicRoutesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDynamicRoutesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDynamicRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExcessiveDeviceRegistrationApplicationsRequest(TeaModel):
    def __init__(self, application_ids=None, current_page=None, department=None, device_tag=None, hostname=None,
                 mac=None, page_size=None, sase_user_id=None, statuses=None, username=None):
        self.application_ids = application_ids  # type: list[str]
        self.current_page = current_page  # type: long
        self.department = department  # type: str
        self.device_tag = device_tag  # type: str
        self.hostname = hostname  # type: str
        self.mac = mac  # type: str
        self.page_size = page_size  # type: long
        self.sase_user_id = sase_user_id  # type: str
        self.statuses = statuses  # type: list[str]
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExcessiveDeviceRegistrationApplicationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.department is not None:
            result['Department'] = self.department
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListExcessiveDeviceRegistrationApplicationsResponseBodyApplications(TeaModel):
    def __init__(self, application_id=None, create_time=None, department=None, description=None, device_tag=None,
                 device_type=None, hostname=None, is_used=None, mac=None, sase_user_id=None, status=None, username=None):
        self.application_id = application_id  # type: str
        self.create_time = create_time  # type: str
        self.department = department  # type: str
        self.description = description  # type: str
        self.device_tag = device_tag  # type: str
        self.device_type = device_type  # type: str
        self.hostname = hostname  # type: str
        self.is_used = is_used  # type: bool
        self.mac = mac  # type: str
        self.sase_user_id = sase_user_id  # type: str
        self.status = status  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExcessiveDeviceRegistrationApplicationsResponseBodyApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.description is not None:
            result['Description'] = self.description
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.is_used is not None:
            result['IsUsed'] = self.is_used
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.status is not None:
            result['Status'] = self.status
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IsUsed') is not None:
            self.is_used = m.get('IsUsed')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListExcessiveDeviceRegistrationApplicationsResponseBody(TeaModel):
    def __init__(self, applications=None, request_id=None, total_num=None):
        self.applications = applications  # type: list[ListExcessiveDeviceRegistrationApplicationsResponseBodyApplications]
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: long

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExcessiveDeviceRegistrationApplicationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListExcessiveDeviceRegistrationApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListExcessiveDeviceRegistrationApplicationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExcessiveDeviceRegistrationApplicationsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExcessiveDeviceRegistrationApplicationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExcessiveDeviceRegistrationApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicesForPrivateAccessApplicationRequest(TeaModel):
    def __init__(self, application_ids=None):
        self.application_ids = application_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        return self


class ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPoliciesCustomUserAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPoliciesCustomUserAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPolicies(TeaModel):
    def __init__(self, application_type=None, create_time=None, custom_user_attributes=None, description=None,
                 name=None, policy_action=None, policy_id=None, priority=None, status=None, user_group_type=None):
        self.application_type = application_type  # type: str
        self.create_time = create_time  # type: str
        self.custom_user_attributes = custom_user_attributes  # type: list[ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPoliciesCustomUserAttributes]
        self.description = description  # type: str
        self.name = name  # type: str
        self.policy_action = policy_action  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: int
        self.status = status  # type: str
        self.user_group_type = user_group_type  # type: str

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPoliciesCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        return self


class ListPolicesForPrivateAccessApplicationResponseBodyApplications(TeaModel):
    def __init__(self, application_id=None, policies=None):
        self.application_id = application_id  # type: str
        self.policies = policies  # type: list[ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPolicies]

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessApplicationResponseBodyApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPolicies()
                self.policies.append(temp_model.from_map(k))
        return self


class ListPolicesForPrivateAccessApplicationResponseBody(TeaModel):
    def __init__(self, applications=None, request_id=None):
        self.applications = applications  # type: list[ListPolicesForPrivateAccessApplicationResponseBodyApplications]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListPolicesForPrivateAccessApplicationResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPolicesForPrivateAccessApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPolicesForPrivateAccessApplicationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPolicesForPrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicesForPrivateAccessTagRequest(TeaModel):
    def __init__(self, tag_ids=None):
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListPolicesForPrivateAccessTagResponseBodyTagsPolicesCustomUserAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        # 用户组的身份源ID。当自定义用户组类型为**department**时，存在该值。
        self.idp_id = idp_id  # type: int
        # 用户组的关系。取值：
        # - **Equal**：等于。
        # - **Unequal**：不等于。
        self.relation = relation  # type: str
        # 用户组的类型。取值：
        # - **username**：用户名。
        # - **department**：部门。
        # - **email**：邮箱。
        # - **telephone**：手机。
        self.user_group_type = user_group_type  # type: str
        # 用户组属性的值。
        # - 当用户组类型为**username**时，表示用户名的值。长度为1~128个字符，支持中文和大小写英文字母，可包含数字、半角句号（.）、下划线（_）和短划线（-）。
        # - 当用户组类型为**department**时，表示部门的值。如：OU=部门1,OU=SASE钉钉。
        # - 当用户组类型为**email**时，表示邮箱的值。如：username@example.com。
        # - 当用户组类型为**telephone**时，表示手机的值。如：13900001234。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessTagResponseBodyTagsPolicesCustomUserAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPolicesForPrivateAccessTagResponseBodyTagsPolices(TeaModel):
    def __init__(self, application_type=None, create_time=None, custom_user_attributes=None, description=None,
                 name=None, policy_action=None, policy_id=None, priority=None, status=None, user_group_type=None):
        self.application_type = application_type  # type: str
        # 内网访问策略创建时间。
        self.create_time = create_time  # type: str
        # 自定义用户组属性集合。多个自定义用户组属性之间是或的关系，按照合集生效。
        self.custom_user_attributes = custom_user_attributes  # type: list[ListPolicesForPrivateAccessTagResponseBodyTagsPolicesCustomUserAttributes]
        self.description = description  # type: str
        self.name = name  # type: str
        self.policy_action = policy_action  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: int
        self.status = status  # type: str
        self.user_group_type = user_group_type  # type: str

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessTagResponseBodyTagsPolices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = ListPolicesForPrivateAccessTagResponseBodyTagsPolicesCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        return self


class ListPolicesForPrivateAccessTagResponseBodyTags(TeaModel):
    def __init__(self, polices=None, tag_id=None):
        self.polices = polices  # type: list[ListPolicesForPrivateAccessTagResponseBodyTagsPolices]
        self.tag_id = tag_id  # type: str

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessTagResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListPolicesForPrivateAccessTagResponseBodyTagsPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListPolicesForPrivateAccessTagResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None):
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[ListPolicesForPrivateAccessTagResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPolicesForPrivateAccessTagResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListPolicesForPrivateAccessTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPolicesForPrivateAccessTagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPolicesForPrivateAccessTagResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPolicesForPrivateAccessTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicesForUserGroupRequest(TeaModel):
    def __init__(self, user_group_ids=None):
        self.user_group_ids = user_group_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPolicesForUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        return self


class ListPolicesForUserGroupResponseBodyUserGroupsPolices(TeaModel):
    def __init__(self, name=None, policy_id=None, policy_type=None):
        self.name = name  # type: str
        self.policy_id = policy_id  # type: str
        self.policy_type = policy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPolicesForUserGroupResponseBodyUserGroupsPolices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPolicesForUserGroupResponseBodyUserGroups(TeaModel):
    def __init__(self, polices=None, user_group_id=None):
        self.polices = polices  # type: list[ListPolicesForUserGroupResponseBodyUserGroupsPolices]
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPolicesForUserGroupResponseBodyUserGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListPolicesForUserGroupResponseBodyUserGroupsPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListPolicesForUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, user_groups=None):
        self.request_id = request_id  # type: str
        self.user_groups = user_groups  # type: list[ListPolicesForUserGroupResponseBodyUserGroups]

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPolicesForUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListPolicesForUserGroupResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListPolicesForUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPolicesForUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPolicesForUserGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPolicesForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPopTrafficStatisticsRequest(TeaModel):
    def __init__(self, end_time=None, region=None, start_time=None):
        self.end_time = end_time  # type: str
        self.region = region  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPopTrafficStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region is not None:
            result['Region'] = self.region
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListPopTrafficStatisticsResponseBodyTrafficDataDatapoints(TeaModel):
    def __init__(self, average=None, date_time=None):
        self.average = average  # type: float
        self.date_time = date_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPopTrafficStatisticsResponseBodyTrafficDataDatapoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.date_time is not None:
            result['DateTime'] = self.date_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')
        return self


class ListPopTrafficStatisticsResponseBodyTrafficData(TeaModel):
    def __init__(self, datapoints=None, metric_name=None):
        self.datapoints = datapoints  # type: list[ListPopTrafficStatisticsResponseBodyTrafficDataDatapoints]
        self.metric_name = metric_name  # type: str

    def validate(self):
        if self.datapoints:
            for k in self.datapoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPopTrafficStatisticsResponseBodyTrafficData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datapoints'] = []
        if self.datapoints is not None:
            for k in self.datapoints:
                result['Datapoints'].append(k.to_map() if k else None)
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.datapoints = []
        if m.get('Datapoints') is not None:
            for k in m.get('Datapoints'):
                temp_model = ListPopTrafficStatisticsResponseBodyTrafficDataDatapoints()
                self.datapoints.append(temp_model.from_map(k))
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        return self


class ListPopTrafficStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, traffic_data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.traffic_data = traffic_data  # type: list[ListPopTrafficStatisticsResponseBodyTrafficData]

    def validate(self):
        if self.traffic_data:
            for k in self.traffic_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPopTrafficStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TrafficData'] = []
        if self.traffic_data is not None:
            for k in self.traffic_data:
                result['TrafficData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.traffic_data = []
        if m.get('TrafficData') is not None:
            for k in m.get('TrafficData'):
                temp_model = ListPopTrafficStatisticsResponseBodyTrafficData()
                self.traffic_data.append(temp_model.from_map(k))
        return self


class ListPopTrafficStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPopTrafficStatisticsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPopTrafficStatisticsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPopTrafficStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateAccessApplicationsRequest(TeaModel):
    def __init__(self, address=None, application_ids=None, connector_id=None, current_page=None, name=None,
                 page_size=None, policy_id=None, status=None, tag_id=None):
        self.address = address  # type: str
        self.application_ids = application_ids  # type: list[str]
        self.connector_id = connector_id  # type: str
        self.current_page = current_page  # type: int
        self.name = name  # type: str
        self.page_size = page_size  # type: int
        self.policy_id = policy_id  # type: str
        self.status = status  # type: str
        self.tag_id = tag_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListPrivateAccessApplicationsResponseBodyApplicationsPortRanges(TeaModel):
    def __init__(self, begin=None, end=None):
        self.begin = begin  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsResponseBodyApplicationsPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class ListPrivateAccessApplicationsResponseBodyApplications(TeaModel):
    def __init__(self, addresses=None, application_id=None, connector_ids=None, create_time=None, description=None,
                 name=None, policy_ids=None, port_ranges=None, protocol=None, status=None, tag_ids=None):
        self.addresses = addresses  # type: list[str]
        self.application_id = application_id  # type: str
        self.connector_ids = connector_ids  # type: list[str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.policy_ids = policy_ids  # type: list[str]
        self.port_ranges = port_ranges  # type: list[ListPrivateAccessApplicationsResponseBodyApplicationsPortRanges]
        self.protocol = protocol  # type: str
        self.status = status  # type: str
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsResponseBodyApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.connector_ids is not None:
            result['ConnectorIds'] = self.connector_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ConnectorIds') is not None:
            self.connector_ids = m.get('ConnectorIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListPrivateAccessApplicationsResponseBodyApplicationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListPrivateAccessApplicationsResponseBody(TeaModel):
    def __init__(self, applications=None, request_id=None, total_num=None):
        self.applications = applications  # type: list[ListPrivateAccessApplicationsResponseBodyApplications]
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListPrivateAccessApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListPrivateAccessApplicationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrivateAccessApplicationsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPrivateAccessApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateAccessApplicationsForDynamicRouteRequest(TeaModel):
    def __init__(self, dynamic_route_ids=None):
        self.dynamic_route_ids = dynamic_route_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsForDynamicRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_ids is not None:
            result['DynamicRouteIds'] = self.dynamic_route_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicRouteIds') is not None:
            self.dynamic_route_ids = m.get('DynamicRouteIds')
        return self


class ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplicationsPortRanges(TeaModel):
    def __init__(self, begin=None, end=None):
        self.begin = begin  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplicationsPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplications(TeaModel):
    def __init__(self, addresses=None, application_id=None, create_time=None, description=None, name=None,
                 port_ranges=None, protocol=None, status=None):
        self.addresses = addresses  # type: list[str]
        self.application_id = application_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.port_ranges = port_ranges  # type: list[ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplicationsPortRanges]
        self.protocol = protocol  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplicationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutes(TeaModel):
    def __init__(self, applications=None, dynamic_route_id=None):
        self.applications = applications  # type: list[ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplications]
        self.dynamic_route_id = dynamic_route_id  # type: str

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutesApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        return self


class ListPrivateAccessApplicationsForDynamicRouteResponseBody(TeaModel):
    def __init__(self, dynamic_routes=None, request_id=None):
        self.dynamic_routes = dynamic_routes  # type: list[ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutes]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dynamic_routes:
            for k in self.dynamic_routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsForDynamicRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DynamicRoutes'] = []
        if self.dynamic_routes is not None:
            for k in self.dynamic_routes:
                result['DynamicRoutes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dynamic_routes = []
        if m.get('DynamicRoutes') is not None:
            for k in m.get('DynamicRoutes'):
                temp_model = ListPrivateAccessApplicationsForDynamicRouteResponseBodyDynamicRoutes()
                self.dynamic_routes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrivateAccessApplicationsForDynamicRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrivateAccessApplicationsForDynamicRouteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrivateAccessApplicationsForDynamicRouteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPrivateAccessApplicationsForDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateAccessPolicesRequest(TeaModel):
    def __init__(self, application_id=None, application_name=None, current_page=None, name=None, page_size=None,
                 policy_action=None, policy_ids=None, status=None, tag_id=None, tag_name=None, user_group_id=None):
        self.application_id = application_id  # type: str
        self.application_name = application_name  # type: str
        self.current_page = current_page  # type: int
        self.name = name  # type: str
        self.page_size = page_size  # type: int
        self.policy_action = policy_action  # type: str
        self.policy_ids = policy_ids  # type: list[str]
        self.status = status  # type: str
        self.tag_id = tag_id  # type: str
        self.tag_name = tag_name  # type: str
        # 用户组ID。取值来源：
        # - [ListUserGroups](~~ListUserGroups~~)：批量查询用户组。
        # - [CreateUserGroup](~~CreateUserGroup~~)：创建用户组。
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrivateAccessPolicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrivateAccessPolicesResponseBodyPolices(TeaModel):
    def __init__(self, application_ids=None, application_type=None, create_time=None, custom_user_attributes=None,
                 description=None, device_attribute_id=None, name=None, policy_action=None, policy_id=None, priority=None,
                 status=None, tag_ids=None, user_group_ids=None, user_group_mode=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.create_time = create_time  # type: str
        self.custom_user_attributes = custom_user_attributes  # type: list[ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes]
        self.description = description  # type: str
        self.device_attribute_id = device_attribute_id  # type: str
        self.name = name  # type: str
        self.policy_action = policy_action  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: int
        self.status = status  # type: str
        self.tag_ids = tag_ids  # type: list[str]
        self.user_group_ids = user_group_ids  # type: list[str]
        self.user_group_mode = user_group_mode  # type: str

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrivateAccessPolicesResponseBodyPolices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.device_attribute_id is not None:
            result['DeviceAttributeId'] = self.device_attribute_id
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceAttributeId') is not None:
            self.device_attribute_id = m.get('DeviceAttributeId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')
        return self


class ListPrivateAccessPolicesResponseBody(TeaModel):
    def __init__(self, polices=None, request_id=None, total_num=None):
        self.polices = polices  # type: list[ListPrivateAccessPolicesResponseBodyPolices]
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrivateAccessPolicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListPrivateAccessPolicesResponseBodyPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListPrivateAccessPolicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrivateAccessPolicesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrivateAccessPolicesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPrivateAccessPolicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateAccessTagsRequest(TeaModel):
    def __init__(self, application_id=None, current_page=None, name=None, page_size=None, policy_id=None,
                 simple_mode=None, tag_ids=None):
        # The ID of the internal access application. You can obtain the application ID by calling the following operations:
        # 
        # *   [ListPrivateAccessApplications](~~ListPrivateAccessApplications~~): queries all internal access applications.
        # *   [CreatePrivateAccessApplication](~~CreatePrivateAccessApplication~~): creates an internal access application.
        self.application_id = application_id  # type: str
        # The page number. Valid values: 1 to 10000.
        self.current_page = current_page  # type: int
        # The name of the internal access tag. The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        self.name = name  # type: str
        # The number of entries per page. Valid values: 1 to 1000.
        self.page_size = page_size  # type: int
        # The ID of the internal access policy. You can obtain the policy ID by calling the following operations:
        # 
        # *   [ListPrivateAccessPolices](~~ListPrivateAccessPolices~~): queries all internal access policies.
        # *   [CreatePrivateAccessPolicy](~~CreatePrivateAccessPolicy~~): creates an internal access policy.
        self.policy_id = policy_id  # type: str
        # Specifies whether to enable the simple query mode. A value of true specifies that policy IDs are not queried.
        self.simple_mode = simple_mode  # type: bool
        # The IDs of internal access tags. You can specify up to 100 tag IDs.
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrivateAccessTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.simple_mode is not None:
            result['SimpleMode'] = self.simple_mode
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SimpleMode') is not None:
            self.simple_mode = m.get('SimpleMode')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListPrivateAccessTagsResponseBodyTags(TeaModel):
    def __init__(self, application_ids=None, create_time=None, description=None, name=None, policy_ids=None,
                 tag_id=None, tag_type=None):
        # The IDs of the internal access applications.
        self.application_ids = application_ids  # type: list[str]
        # The time when the internal access tag was created.
        self.create_time = create_time  # type: str
        # The description of the internal access tag.
        self.description = description  # type: str
        # The name of the internal access tag.
        self.name = name  # type: str
        # The IDs of the internal access policies.
        self.policy_ids = policy_ids  # type: list[str]
        # The ID of the internal access tag.
        self.tag_id = tag_id  # type: str
        # The type of the internal access tag. Valid values:
        # 
        # *   **Default**\
        # *   **Custom**\
        self.tag_type = tag_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrivateAccessTagsResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_type is not None:
            result['TagType'] = self.tag_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')
        return self


class ListPrivateAccessTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None, total_num=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The internal access tags.
        self.tags = tags  # type: list[ListPrivateAccessTagsResponseBodyTags]
        # The total number of internal access tags.
        self.total_num = total_num  # type: int

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrivateAccessTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPrivateAccessTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListPrivateAccessTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrivateAccessTagsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrivateAccessTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPrivateAccessTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateAccessTagsForDynamicRouteRequest(TeaModel):
    def __init__(self, dynamic_route_ids=None):
        self.dynamic_route_ids = dynamic_route_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrivateAccessTagsForDynamicRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_ids is not None:
            result['DynamicRouteIds'] = self.dynamic_route_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicRouteIds') is not None:
            self.dynamic_route_ids = m.get('DynamicRouteIds')
        return self


class ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutesTags(TeaModel):
    def __init__(self, create_time=None, description=None, name=None, tag_id=None, tag_type=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.tag_id = tag_id  # type: str
        self.tag_type = tag_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_type is not None:
            result['TagType'] = self.tag_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')
        return self


class ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutes(TeaModel):
    def __init__(self, dynamic_route_id=None, tags=None):
        self.dynamic_route_id = dynamic_route_id  # type: str
        self.tags = tags  # type: list[ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutesTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListPrivateAccessTagsForDynamicRouteResponseBody(TeaModel):
    def __init__(self, dynamic_routes=None, request_id=None):
        self.dynamic_routes = dynamic_routes  # type: list[ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutes]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dynamic_routes:
            for k in self.dynamic_routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrivateAccessTagsForDynamicRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DynamicRoutes'] = []
        if self.dynamic_routes is not None:
            for k in self.dynamic_routes:
                result['DynamicRoutes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dynamic_routes = []
        if m.get('DynamicRoutes') is not None:
            for k in m.get('DynamicRoutes'):
                temp_model = ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutes()
                self.dynamic_routes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrivateAccessTagsForDynamicRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrivateAccessTagsForDynamicRouteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrivateAccessTagsForDynamicRouteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPrivateAccessTagsForDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegistrationPoliciesRequest(TeaModel):
    def __init__(self, company_limit_type=None, current_page=None, match_mode=None, name=None, page_size=None,
                 personal_limit_type=None, policy_ids=None, status=None, user_group_id=None):
        self.company_limit_type = company_limit_type  # type: str
        self.current_page = current_page  # type: long
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.page_size = page_size  # type: long
        self.personal_limit_type = personal_limit_type  # type: str
        self.policy_ids = policy_ids  # type: list[str]
        self.status = status  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegistrationPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListRegistrationPoliciesResponseBodyPoliciesLimitDetailLimitCount(TeaModel):
    def __init__(self, all=None, mobile=None, pc=None):
        self.all = all  # type: int
        self.mobile = mobile  # type: int
        self.pc = pc  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegistrationPoliciesResponseBodyPoliciesLimitDetailLimitCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class ListRegistrationPoliciesResponseBodyPoliciesLimitDetail(TeaModel):
    def __init__(self, device_belong=None, limit_count=None, limit_type=None):
        self.device_belong = device_belong  # type: str
        self.limit_count = limit_count  # type: ListRegistrationPoliciesResponseBodyPoliciesLimitDetailLimitCount
        self.limit_type = limit_type  # type: str

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        _map = super(ListRegistrationPoliciesResponseBodyPoliciesLimitDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('LimitCount') is not None:
            temp_model = ListRegistrationPoliciesResponseBodyPoliciesLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m['LimitCount'])
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class ListRegistrationPoliciesResponseBodyPolicies(TeaModel):
    def __init__(self, create_time=None, description=None, limit_detail=None, match_mode=None, name=None,
                 policy_id=None, priority=None, status=None, user_group_ids=None, whitelist=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.limit_detail = limit_detail  # type: list[ListRegistrationPoliciesResponseBodyPoliciesLimitDetail]
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: long
        self.status = status  # type: str
        self.user_group_ids = user_group_ids  # type: list[str]
        self.whitelist = whitelist  # type: list[str]

    def validate(self):
        if self.limit_detail:
            for k in self.limit_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegistrationPoliciesResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k in self.limit_detail:
                result['LimitDetail'].append(k.to_map() if k else None)
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k in m.get('LimitDetail'):
                temp_model = ListRegistrationPoliciesResponseBodyPoliciesLimitDetail()
                self.limit_detail.append(temp_model.from_map(k))
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class ListRegistrationPoliciesResponseBody(TeaModel):
    def __init__(self, policies=None, request_id=None, total_num=None):
        self.policies = policies  # type: list[ListRegistrationPoliciesResponseBodyPolicies]
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: str

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegistrationPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListRegistrationPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListRegistrationPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegistrationPoliciesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegistrationPoliciesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegistrationPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegistrationPoliciesForUserGroupRequest(TeaModel):
    def __init__(self, user_group_ids=None):
        self.user_group_ids = user_group_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegistrationPoliciesForUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        return self


class ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetailLimitCount(TeaModel):
    def __init__(self, all=None, mobile=None, pc=None):
        self.all = all  # type: str
        self.mobile = mobile  # type: str
        self.pc = pc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetailLimitCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetail(TeaModel):
    def __init__(self, device_belong=None, limit_count=None, limit_type=None):
        self.device_belong = device_belong  # type: str
        self.limit_count = limit_count  # type: ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetailLimitCount
        self.limit_type = limit_type  # type: str

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        _map = super(ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('LimitCount') is not None:
            temp_model = ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m['LimitCount'])
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPolicies(TeaModel):
    def __init__(self, create_time=None, description=None, limit_detail=None, match_mode=None, name=None,
                 policy_id=None, priority=None, status=None, whitelist=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.limit_detail = limit_detail  # type: list[ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetail]
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: long
        self.status = status  # type: str
        self.whitelist = whitelist  # type: list[str]

    def validate(self):
        if self.limit_detail:
            for k in self.limit_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k in self.limit_detail:
                result['LimitDetail'].append(k.to_map() if k else None)
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k in m.get('LimitDetail'):
                temp_model = ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetail()
                self.limit_detail.append(temp_model.from_map(k))
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class ListRegistrationPoliciesForUserGroupResponseBodyUserGroups(TeaModel):
    def __init__(self, policies=None, user_group_id=None):
        self.policies = policies  # type: list[ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPolicies]
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegistrationPoliciesForUserGroupResponseBodyUserGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListRegistrationPoliciesForUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, user_groups=None):
        self.request_id = request_id  # type: str
        self.user_groups = user_groups  # type: list[ListRegistrationPoliciesForUserGroupResponseBodyUserGroups]

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegistrationPoliciesForUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListRegistrationPoliciesForUserGroupResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListRegistrationPoliciesForUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegistrationPoliciesForUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegistrationPoliciesForUserGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegistrationPoliciesForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSoftwareForUserDeviceRequest(TeaModel):
    def __init__(self, current_page=None, device_tag=None, page_size=None):
        self.current_page = current_page  # type: long
        self.device_tag = device_tag  # type: str
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSoftwareForUserDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSoftwareForUserDeviceResponseBodySoftware(TeaModel):
    def __init__(self, inc=None, install_time=None, name=None, versions=None):
        self.inc = inc  # type: str
        self.install_time = install_time  # type: str
        self.name = name  # type: str
        self.versions = versions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSoftwareForUserDeviceResponseBodySoftware, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inc is not None:
            result['Inc'] = self.inc
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.name is not None:
            result['Name'] = self.name
        if self.versions is not None:
            result['Versions'] = self.versions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Inc') is not None:
            self.inc = m.get('Inc')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Versions') is not None:
            self.versions = m.get('Versions')
        return self


class ListSoftwareForUserDeviceResponseBody(TeaModel):
    def __init__(self, request_id=None, software=None, total_num=None):
        self.request_id = request_id  # type: str
        self.software = software  # type: list[ListSoftwareForUserDeviceResponseBodySoftware]
        self.total_num = total_num  # type: long

    def validate(self):
        if self.software:
            for k in self.software:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSoftwareForUserDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Software'] = []
        if self.software is not None:
            for k in self.software:
                result['Software'].append(k.to_map() if k else None)
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.software = []
        if m.get('Software') is not None:
            for k in m.get('Software'):
                temp_model = ListSoftwareForUserDeviceResponseBodySoftware()
                self.software.append(temp_model.from_map(k))
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListSoftwareForUserDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSoftwareForUserDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSoftwareForUserDeviceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSoftwareForUserDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsForPrivateAccessApplicationRequest(TeaModel):
    def __init__(self, application_ids=None):
        self.application_ids = application_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsForPrivateAccessApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        return self


class ListTagsForPrivateAccessApplicationResponseBodyApplicationsTags(TeaModel):
    def __init__(self, create_time=None, description=None, name=None, tag_id=None, tag_type=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.tag_id = tag_id  # type: str
        self.tag_type = tag_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsForPrivateAccessApplicationResponseBodyApplicationsTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_type is not None:
            result['TagType'] = self.tag_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')
        return self


class ListTagsForPrivateAccessApplicationResponseBodyApplications(TeaModel):
    def __init__(self, application_id=None, tags=None):
        self.application_id = application_id  # type: str
        self.tags = tags  # type: list[ListTagsForPrivateAccessApplicationResponseBodyApplicationsTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsForPrivateAccessApplicationResponseBodyApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagsForPrivateAccessApplicationResponseBodyApplicationsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagsForPrivateAccessApplicationResponseBody(TeaModel):
    def __init__(self, applications=None, request_id=None):
        self.applications = applications  # type: list[ListTagsForPrivateAccessApplicationResponseBodyApplications]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsForPrivateAccessApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListTagsForPrivateAccessApplicationResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagsForPrivateAccessApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagsForPrivateAccessApplicationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagsForPrivateAccessApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagsForPrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsForPrivateAccessPolicyRequest(TeaModel):
    def __init__(self, policy_ids=None):
        self.policy_ids = policy_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsForPrivateAccessPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        return self


class ListTagsForPrivateAccessPolicyResponseBodyPolicesTags(TeaModel):
    def __init__(self, create_time=None, description=None, name=None, tag_id=None, tag_type=None):
        # 内网访问标签创建时间。
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.tag_id = tag_id  # type: str
        self.tag_type = tag_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsForPrivateAccessPolicyResponseBodyPolicesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_type is not None:
            result['TagType'] = self.tag_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')
        return self


class ListTagsForPrivateAccessPolicyResponseBodyPolices(TeaModel):
    def __init__(self, policy_id=None, tags=None):
        self.policy_id = policy_id  # type: str
        self.tags = tags  # type: list[ListTagsForPrivateAccessPolicyResponseBodyPolicesTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsForPrivateAccessPolicyResponseBodyPolices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagsForPrivateAccessPolicyResponseBodyPolicesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagsForPrivateAccessPolicyResponseBody(TeaModel):
    def __init__(self, polices=None, request_id=None):
        self.polices = polices  # type: list[ListTagsForPrivateAccessPolicyResponseBodyPolices]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsForPrivateAccessPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListTagsForPrivateAccessPolicyResponseBodyPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagsForPrivateAccessPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagsForPrivateAccessPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagsForPrivateAccessPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagsForPrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserDevicesRequest(TeaModel):
    def __init__(self, app_statuses=None, current_page=None, department=None, device_belong=None,
                 device_statuses=None, device_tags=None, device_types=None, dlp_statuses=None, hostname=None, ia_statuses=None,
                 mac=None, nac_statuses=None, pa_statuses=None, page_size=None, sase_user_id=None, sharing_status=None,
                 sort_by=None, username=None):
        self.app_statuses = app_statuses  # type: list[str]
        self.current_page = current_page  # type: long
        self.department = department  # type: str
        self.device_belong = device_belong  # type: str
        self.device_statuses = device_statuses  # type: list[str]
        self.device_tags = device_tags  # type: list[str]
        self.device_types = device_types  # type: list[str]
        self.dlp_statuses = dlp_statuses  # type: list[str]
        self.hostname = hostname  # type: str
        self.ia_statuses = ia_statuses  # type: list[str]
        self.mac = mac  # type: str
        self.nac_statuses = nac_statuses  # type: list[str]
        self.pa_statuses = pa_statuses  # type: list[str]
        self.page_size = page_size  # type: long
        self.sase_user_id = sase_user_id  # type: str
        self.sharing_status = sharing_status  # type: bool
        self.sort_by = sort_by  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_statuses is not None:
            result['AppStatuses'] = self.app_statuses
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_statuses is not None:
            result['DeviceStatuses'] = self.device_statuses
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags
        if self.device_types is not None:
            result['DeviceTypes'] = self.device_types
        if self.dlp_statuses is not None:
            result['DlpStatuses'] = self.dlp_statuses
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_statuses is not None:
            result['IaStatuses'] = self.ia_statuses
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.nac_statuses is not None:
            result['NacStatuses'] = self.nac_statuses
        if self.pa_statuses is not None:
            result['PaStatuses'] = self.pa_statuses
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppStatuses') is not None:
            self.app_statuses = m.get('AppStatuses')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceStatuses') is not None:
            self.device_statuses = m.get('DeviceStatuses')
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')
        if m.get('DeviceTypes') is not None:
            self.device_types = m.get('DeviceTypes')
        if m.get('DlpStatuses') is not None:
            self.dlp_statuses = m.get('DlpStatuses')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatuses') is not None:
            self.ia_statuses = m.get('IaStatuses')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('NacStatuses') is not None:
            self.nac_statuses = m.get('NacStatuses')
        if m.get('PaStatuses') is not None:
            self.pa_statuses = m.get('PaStatuses')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListUserDevicesResponseBodyDevices(TeaModel):
    def __init__(self, app_status=None, app_version=None, cpu=None, create_time=None, department=None,
                 device_belong=None, device_model=None, device_status=None, device_tag=None, device_type=None,
                 device_version=None, disk=None, dlp_status=None, hostname=None, ia_status=None, inner_ip=None, mac=None,
                 memory=None, nac_status=None, pa_status=None, sase_user_id=None, sharing_status=None, src_ip=None,
                 update_time=None, username=None):
        self.app_status = app_status  # type: str
        self.app_version = app_version  # type: str
        self.cpu = cpu  # type: str
        self.create_time = create_time  # type: str
        self.department = department  # type: str
        self.device_belong = device_belong  # type: str
        self.device_model = device_model  # type: str
        self.device_status = device_status  # type: str
        self.device_tag = device_tag  # type: str
        self.device_type = device_type  # type: str
        self.device_version = device_version  # type: str
        self.disk = disk  # type: str
        self.dlp_status = dlp_status  # type: str
        self.hostname = hostname  # type: str
        self.ia_status = ia_status  # type: str
        self.inner_ip = inner_ip  # type: str
        self.mac = mac  # type: str
        self.memory = memory  # type: str
        self.nac_status = nac_status  # type: str
        self.pa_status = pa_status  # type: str
        self.sase_user_id = sase_user_id  # type: str
        self.sharing_status = sharing_status  # type: bool
        self.src_ip = src_ip  # type: str
        self.update_time = update_time  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserDevicesResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_version is not None:
            result['DeviceVersion'] = self.device_version
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_status is not None:
            result['IaStatus'] = self.ia_status
        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.nac_status is not None:
            result['NacStatus'] = self.nac_status
        if self.pa_status is not None:
            result['PaStatus'] = self.pa_status
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceVersion') is not None:
            self.device_version = m.get('DeviceVersion')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatus') is not None:
            self.ia_status = m.get('IaStatus')
        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')
        if m.get('PaStatus') is not None:
            self.pa_status = m.get('PaStatus')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListUserDevicesResponseBody(TeaModel):
    def __init__(self, devices=None, request_id=None, total_num=None):
        self.devices = devices  # type: list[ListUserDevicesResponseBodyDevices]
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: long

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = ListUserDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListUserDevicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserDevicesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserDevicesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsRequest(TeaModel):
    def __init__(self, attribute_value=None, current_page=None, name=None, papolicy_id=None, page_size=None,
                 user_group_ids=None):
        self.attribute_value = attribute_value  # type: str
        self.current_page = current_page  # type: int
        # 用户组名称。长度为1~128个字符，支持中文和大小写英文字母，可包含数字、半角句号（.）、下划线（_）和短划线（-）。
        self.name = name  # type: str
        self.papolicy_id = papolicy_id  # type: str
        self.page_size = page_size  # type: int
        self.user_group_ids = user_group_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.name is not None:
            result['Name'] = self.name
        if self.papolicy_id is not None:
            result['PAPolicyId'] = self.papolicy_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PAPolicyId') is not None:
            self.papolicy_id = m.get('PAPolicyId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        return self


class ListUserGroupsResponseBodyUserGroupsAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsResponseBodyUserGroupsAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListUserGroupsResponseBodyUserGroups(TeaModel):
    def __init__(self, attributes=None, create_time=None, description=None, name=None, user_group_id=None):
        self.attributes = attributes  # type: list[ListUserGroupsResponseBodyUserGroupsAttributes]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserGroupsResponseBodyUserGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = ListUserGroupsResponseBodyUserGroupsAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListUserGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, total_num=None, user_groups=None):
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int
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
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListUserGroupsResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListUserGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserGroupsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsForPrivateAccessPolicyRequest(TeaModel):
    def __init__(self, policy_ids=None):
        self.policy_ids = policy_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsForPrivateAccessPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        return self


class ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroupsAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroupsAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroups(TeaModel):
    def __init__(self, attributes=None, create_time=None, description=None, name=None, user_group_id=None):
        self.attributes = attributes  # type: list[ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroupsAttributes]
        # 用户组创建时间。
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroupsAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListUserGroupsForPrivateAccessPolicyResponseBodyPolices(TeaModel):
    def __init__(self, policy_id=None, user_groups=None):
        self.policy_id = policy_id  # type: str
        self.user_groups = user_groups  # type: list[ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroups]

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserGroupsForPrivateAccessPolicyResponseBodyPolices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListUserGroupsForPrivateAccessPolicyResponseBodyPolicesUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListUserGroupsForPrivateAccessPolicyResponseBody(TeaModel):
    def __init__(self, polices=None, request_id=None):
        self.polices = polices  # type: list[ListUserGroupsForPrivateAccessPolicyResponseBodyPolices]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.polices:
            for k in self.polices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserGroupsForPrivateAccessPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Polices'] = []
        if self.polices is not None:
            for k in self.polices:
                result['Polices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k in m.get('Polices'):
                temp_model = ListUserGroupsForPrivateAccessPolicyResponseBodyPolices()
                self.polices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserGroupsForPrivateAccessPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserGroupsForPrivateAccessPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserGroupsForPrivateAccessPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserGroupsForPrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsForRegistrationPolicyRequest(TeaModel):
    def __init__(self, policy_ids=None):
        self.policy_ids = policy_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsForRegistrationPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        return self


class ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroupsAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroupsAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroups(TeaModel):
    def __init__(self, attributes=None, create_time=None, description=None, name=None, user_group_id=None):
        self.attributes = attributes  # type: list[ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroupsAttributes]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroupsAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListUserGroupsForRegistrationPolicyResponseBodyPolicies(TeaModel):
    def __init__(self, policy_id=None, user_groups=None):
        self.policy_id = policy_id  # type: str
        self.user_groups = user_groups  # type: list[ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroups]

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserGroupsForRegistrationPolicyResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListUserGroupsForRegistrationPolicyResponseBody(TeaModel):
    def __init__(self, policies=None, request_id=None):
        self.policies = policies  # type: list[ListUserGroupsForRegistrationPolicyResponseBodyPolicies]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserGroupsForRegistrationPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListUserGroupsForRegistrationPolicyResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserGroupsForRegistrationPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserGroupsForRegistrationPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserGroupsForRegistrationPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserGroupsForRegistrationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDynamicRouteRequest(TeaModel):
    def __init__(self, application_ids=None, application_type=None, description=None, dynamic_route_id=None,
                 dynamic_route_type=None, modify_type=None, name=None, next_hop=None, priority=None, region_ids=None, status=None,
                 tag_ids=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.description = description  # type: str
        self.dynamic_route_id = dynamic_route_id  # type: str
        self.dynamic_route_type = dynamic_route_type  # type: str
        self.modify_type = modify_type  # type: str
        self.name = name  # type: str
        self.next_hop = next_hop  # type: str
        self.priority = priority  # type: int
        self.region_ids = region_ids  # type: list[str]
        self.status = status  # type: str
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDynamicRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id
        if self.dynamic_route_type is not None:
            result['DynamicRouteType'] = self.dynamic_route_type
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.name is not None:
            result['Name'] = self.name
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')
        if m.get('DynamicRouteType') is not None:
            self.dynamic_route_type = m.get('DynamicRouteType')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class UpdateDynamicRouteResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDynamicRouteResponseBody, self).to_map()
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


class UpdateDynamicRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDynamicRouteResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDynamicRouteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDynamicRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExcessiveDeviceRegistrationApplicationsStatusRequest(TeaModel):
    def __init__(self, application_ids=None, status=None):
        self.application_ids = application_ids  # type: list[str]
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExcessiveDeviceRegistrationApplicationsStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBodyApplications(TeaModel):
    def __init__(self, application_id=None, create_time=None, department=None, description=None, device_tag=None,
                 device_type=None, hostname=None, is_used=None, mac=None, sase_user_id=None, status=None, username=None):
        self.application_id = application_id  # type: str
        self.create_time = create_time  # type: str
        self.department = department  # type: str
        self.description = description  # type: str
        self.device_tag = device_tag  # type: str
        self.device_type = device_type  # type: str
        self.hostname = hostname  # type: str
        self.is_used = is_used  # type: bool
        self.mac = mac  # type: str
        self.sase_user_id = sase_user_id  # type: str
        self.status = status  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBodyApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.description is not None:
            result['Description'] = self.description
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.is_used is not None:
            result['IsUsed'] = self.is_used
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.status is not None:
            result['Status'] = self.status
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IsUsed') is not None:
            self.is_used = m.get('IsUsed')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBody(TeaModel):
    def __init__(self, applications=None, request_id=None):
        self.applications = applications  # type: list[UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBodyApplications]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateExcessiveDeviceRegistrationApplicationsStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateExcessiveDeviceRegistrationApplicationsStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrivateAccessApplicationRequestPortRanges(TeaModel):
    def __init__(self, begin=None, end=None):
        self.begin = begin  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrivateAccessApplicationRequestPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class UpdatePrivateAccessApplicationRequest(TeaModel):
    def __init__(self, addresses=None, application_id=None, description=None, modify_type=None, port_ranges=None,
                 protocol=None, status=None, tag_ids=None):
        self.addresses = addresses  # type: list[str]
        self.application_id = application_id  # type: str
        self.description = description  # type: str
        self.modify_type = modify_type  # type: str
        self.port_ranges = port_ranges  # type: list[UpdatePrivateAccessApplicationRequestPortRanges]
        self.protocol = protocol  # type: str
        self.status = status  # type: str
        self.tag_ids = tag_ids  # type: list[str]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdatePrivateAccessApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses is not None:
            result['Addresses'] = self.addresses
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.description is not None:
            result['Description'] = self.description
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = UpdatePrivateAccessApplicationRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class UpdatePrivateAccessApplicationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrivateAccessApplicationResponseBody, self).to_map()
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


class UpdatePrivateAccessApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePrivateAccessApplicationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePrivateAccessApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePrivateAccessApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrivateAccessPolicyRequestCustomUserAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrivateAccessPolicyRequestCustomUserAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdatePrivateAccessPolicyRequest(TeaModel):
    def __init__(self, application_ids=None, application_type=None, custom_user_attributes=None, description=None,
                 device_attribute_id=None, modify_type=None, policy_action=None, policy_id=None, priority=None, status=None,
                 tag_ids=None, user_group_ids=None, user_group_mode=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.custom_user_attributes = custom_user_attributes  # type: list[UpdatePrivateAccessPolicyRequestCustomUserAttributes]
        self.description = description  # type: str
        self.device_attribute_id = device_attribute_id  # type: str
        self.modify_type = modify_type  # type: str
        self.policy_action = policy_action  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: int
        self.status = status  # type: str
        # 内网访问标签ID集合。一条策略最多支持100个内网访问标签ID。
        self.tag_ids = tag_ids  # type: list[str]
        self.user_group_ids = user_group_ids  # type: list[str]
        # 内网访问策略的用户组类型。取值：
        # - **Normal**：普通用户组。
        # - **Custom**：自定义用户组。
        self.user_group_mode = user_group_mode  # type: str

    def validate(self):
        if self.custom_user_attributes:
            for k in self.custom_user_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdatePrivateAccessPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.device_attribute_id is not None:
            result['DeviceAttributeId'] = self.device_attribute_id
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k in m.get('CustomUserAttributes'):
                temp_model = UpdatePrivateAccessPolicyRequestCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceAttributeId') is not None:
            self.device_attribute_id = m.get('DeviceAttributeId')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')
        return self


class UpdatePrivateAccessPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrivateAccessPolicyResponseBody, self).to_map()
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


class UpdatePrivateAccessPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePrivateAccessPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePrivateAccessPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePrivateAccessPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRegistrationPolicyRequestCompanyLimitCount(TeaModel):
    def __init__(self, all=None, mobile=None, pc=None):
        self.all = all  # type: int
        self.mobile = mobile  # type: int
        self.pc = pc  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRegistrationPolicyRequestCompanyLimitCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class UpdateRegistrationPolicyRequestPersonalLimitCount(TeaModel):
    def __init__(self, all=None, mobile=None, pc=None):
        self.all = all  # type: int
        self.mobile = mobile  # type: int
        self.pc = pc  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRegistrationPolicyRequestPersonalLimitCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class UpdateRegistrationPolicyRequest(TeaModel):
    def __init__(self, company_limit_count=None, company_limit_type=None, description=None, match_mode=None,
                 name=None, personal_limit_count=None, personal_limit_type=None, policy_id=None, priority=None,
                 status=None, user_group_ids=None, whitelist=None):
        self.company_limit_count = company_limit_count  # type: UpdateRegistrationPolicyRequestCompanyLimitCount
        self.company_limit_type = company_limit_type  # type: str
        self.description = description  # type: str
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.personal_limit_count = personal_limit_count  # type: UpdateRegistrationPolicyRequestPersonalLimitCount
        self.personal_limit_type = personal_limit_type  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: long
        self.status = status  # type: str
        self.user_group_ids = user_group_ids  # type: list[str]
        self.whitelist = whitelist  # type: list[str]

    def validate(self):
        if self.company_limit_count:
            self.company_limit_count.validate()
        if self.personal_limit_count:
            self.personal_limit_count.validate()

    def to_map(self):
        _map = super(UpdateRegistrationPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_limit_count is not None:
            result['CompanyLimitCount'] = self.company_limit_count.to_map()
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type
        if self.description is not None:
            result['Description'] = self.description
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.personal_limit_count is not None:
            result['PersonalLimitCount'] = self.personal_limit_count.to_map()
        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompanyLimitCount') is not None:
            temp_model = UpdateRegistrationPolicyRequestCompanyLimitCount()
            self.company_limit_count = temp_model.from_map(m['CompanyLimitCount'])
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonalLimitCount') is not None:
            temp_model = UpdateRegistrationPolicyRequestPersonalLimitCount()
            self.personal_limit_count = temp_model.from_map(m['PersonalLimitCount'])
        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class UpdateRegistrationPolicyShrinkRequest(TeaModel):
    def __init__(self, company_limit_count_shrink=None, company_limit_type=None, description=None, match_mode=None,
                 name=None, personal_limit_count_shrink=None, personal_limit_type=None, policy_id=None, priority=None,
                 status=None, user_group_ids=None, whitelist=None):
        self.company_limit_count_shrink = company_limit_count_shrink  # type: str
        self.company_limit_type = company_limit_type  # type: str
        self.description = description  # type: str
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.personal_limit_count_shrink = personal_limit_count_shrink  # type: str
        self.personal_limit_type = personal_limit_type  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: long
        self.status = status  # type: str
        self.user_group_ids = user_group_ids  # type: list[str]
        self.whitelist = whitelist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRegistrationPolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_limit_count_shrink is not None:
            result['CompanyLimitCount'] = self.company_limit_count_shrink
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type
        if self.description is not None:
            result['Description'] = self.description
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.personal_limit_count_shrink is not None:
            result['PersonalLimitCount'] = self.personal_limit_count_shrink
        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompanyLimitCount') is not None:
            self.company_limit_count_shrink = m.get('CompanyLimitCount')
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PersonalLimitCount') is not None:
            self.personal_limit_count_shrink = m.get('PersonalLimitCount')
        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class UpdateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount(TeaModel):
    def __init__(self, all=None, mobile=None, pc=None):
        self.all = all  # type: int
        self.mobile = mobile  # type: int
        self.pc = pc  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.pc is not None:
            result['PC'] = self.pc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PC') is not None:
            self.pc = m.get('PC')
        return self


class UpdateRegistrationPolicyResponseBodyPolicyLimitDetail(TeaModel):
    def __init__(self, device_belong=None, limit_count=None, limit_type=None):
        self.device_belong = device_belong  # type: str
        self.limit_count = limit_count  # type: UpdateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount
        self.limit_type = limit_type  # type: str

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        _map = super(UpdateRegistrationPolicyResponseBodyPolicyLimitDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('LimitCount') is not None:
            temp_model = UpdateRegistrationPolicyResponseBodyPolicyLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m['LimitCount'])
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class UpdateRegistrationPolicyResponseBodyPolicy(TeaModel):
    def __init__(self, create_time=None, description=None, limit_detail=None, match_mode=None, name=None,
                 policy_id=None, priority=None, status=None, user_group_ids=None, whitelist=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.limit_detail = limit_detail  # type: list[UpdateRegistrationPolicyResponseBodyPolicyLimitDetail]
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: str
        self.status = status  # type: str
        self.user_group_ids = user_group_ids  # type: list[str]
        self.whitelist = whitelist  # type: list[str]

    def validate(self):
        if self.limit_detail:
            for k in self.limit_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateRegistrationPolicyResponseBodyPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k in self.limit_detail:
                result['LimitDetail'].append(k.to_map() if k else None)
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k in m.get('LimitDetail'):
                temp_model = UpdateRegistrationPolicyResponseBodyPolicyLimitDetail()
                self.limit_detail.append(temp_model.from_map(k))
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class UpdateRegistrationPolicyResponseBody(TeaModel):
    def __init__(self, policy=None, request_id=None):
        self.policy = policy  # type: UpdateRegistrationPolicyResponseBodyPolicy
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(UpdateRegistrationPolicyResponseBody, self).to_map()
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
            temp_model = UpdateRegistrationPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRegistrationPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRegistrationPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRegistrationPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRegistrationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserDevicesSharingStatusRequest(TeaModel):
    def __init__(self, device_tags=None, sharing_status=None):
        self.device_tags = device_tags  # type: list[str]
        self.sharing_status = sharing_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserDevicesSharingStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        return self


class UpdateUserDevicesSharingStatusResponseBodyDevices(TeaModel):
    def __init__(self, app_status=None, app_version=None, cpu=None, create_time=None, department=None,
                 device_belong=None, device_model=None, device_status=None, device_tag=None, device_type=None,
                 device_version=None, disk=None, dlp_status=None, hostname=None, ia_status=None, inner_ip=None, mac=None,
                 memory=None, nac_status=None, pa_status=None, sase_user_id=None, sharing_status=None, src_ip=None,
                 update_time=None, username=None):
        self.app_status = app_status  # type: str
        self.app_version = app_version  # type: str
        self.cpu = cpu  # type: str
        self.create_time = create_time  # type: str
        self.department = department  # type: str
        self.device_belong = device_belong  # type: str
        self.device_model = device_model  # type: str
        self.device_status = device_status  # type: str
        self.device_tag = device_tag  # type: str
        self.device_type = device_type  # type: str
        self.device_version = device_version  # type: str
        self.disk = disk  # type: str
        self.dlp_status = dlp_status  # type: str
        self.hostname = hostname  # type: str
        self.ia_status = ia_status  # type: str
        self.inner_ip = inner_ip  # type: str
        self.mac = mac  # type: str
        self.memory = memory  # type: str
        self.nac_status = nac_status  # type: str
        self.pa_status = pa_status  # type: str
        self.sase_user_id = sase_user_id  # type: str
        self.sharing_status = sharing_status  # type: bool
        self.src_ip = src_ip  # type: str
        self.update_time = update_time  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserDevicesSharingStatusResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_version is not None:
            result['DeviceVersion'] = self.device_version
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_status is not None:
            result['IaStatus'] = self.ia_status
        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.nac_status is not None:
            result['NacStatus'] = self.nac_status
        if self.pa_status is not None:
            result['PaStatus'] = self.pa_status
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceVersion') is not None:
            self.device_version = m.get('DeviceVersion')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatus') is not None:
            self.ia_status = m.get('IaStatus')
        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')
        if m.get('PaStatus') is not None:
            self.pa_status = m.get('PaStatus')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateUserDevicesSharingStatusResponseBody(TeaModel):
    def __init__(self, devices=None, request_id=None):
        self.devices = devices  # type: list[UpdateUserDevicesSharingStatusResponseBodyDevices]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateUserDevicesSharingStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = UpdateUserDevicesSharingStatusResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUserDevicesSharingStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUserDevicesSharingStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserDevicesSharingStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserDevicesSharingStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserDevicesStatusRequest(TeaModel):
    def __init__(self, device_action=None, device_tags=None):
        self.device_action = device_action  # type: str
        self.device_tags = device_tags  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserDevicesStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_action is not None:
            result['DeviceAction'] = self.device_action
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceAction') is not None:
            self.device_action = m.get('DeviceAction')
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')
        return self


class UpdateUserDevicesStatusResponseBodyDevices(TeaModel):
    def __init__(self, app_status=None, app_version=None, cpu=None, create_time=None, department=None,
                 device_belong=None, device_model=None, device_status=None, device_tag=None, device_type=None,
                 device_version=None, disk=None, dlp_status=None, hostname=None, ia_status=None, inner_ip=None, mac=None,
                 memory=None, nac_status=None, pa_status=None, sase_user_id=None, sharing_status=None, src_ip=None,
                 update_time=None, username=None):
        self.app_status = app_status  # type: str
        self.app_version = app_version  # type: str
        self.cpu = cpu  # type: str
        self.create_time = create_time  # type: str
        self.department = department  # type: str
        self.device_belong = device_belong  # type: str
        self.device_model = device_model  # type: str
        self.device_status = device_status  # type: str
        self.device_tag = device_tag  # type: str
        self.device_type = device_type  # type: str
        self.device_version = device_version  # type: str
        self.disk = disk  # type: str
        self.dlp_status = dlp_status  # type: str
        self.hostname = hostname  # type: str
        self.ia_status = ia_status  # type: str
        self.inner_ip = inner_ip  # type: str
        self.mac = mac  # type: str
        self.memory = memory  # type: str
        self.nac_status = nac_status  # type: str
        self.pa_status = pa_status  # type: str
        self.sase_user_id = sase_user_id  # type: str
        self.sharing_status = sharing_status  # type: bool
        self.src_ip = src_ip  # type: str
        self.update_time = update_time  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserDevicesStatusResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.department is not None:
            result['Department'] = self.department
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_version is not None:
            result['DeviceVersion'] = self.device_version
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.dlp_status is not None:
            result['DlpStatus'] = self.dlp_status
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ia_status is not None:
            result['IaStatus'] = self.ia_status
        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.nac_status is not None:
            result['NacStatus'] = self.nac_status
        if self.pa_status is not None:
            result['PaStatus'] = self.pa_status
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id
        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Department') is not None:
            self.department = m.get('Department')
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceVersion') is not None:
            self.device_version = m.get('DeviceVersion')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DlpStatus') is not None:
            self.dlp_status = m.get('DlpStatus')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IaStatus') is not None:
            self.ia_status = m.get('IaStatus')
        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NacStatus') is not None:
            self.nac_status = m.get('NacStatus')
        if m.get('PaStatus') is not None:
            self.pa_status = m.get('PaStatus')
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')
        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateUserDevicesStatusResponseBody(TeaModel):
    def __init__(self, devices=None, request_id=None):
        self.devices = devices  # type: list[UpdateUserDevicesStatusResponseBodyDevices]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateUserDevicesStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = UpdateUserDevicesStatusResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateUserDevicesStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUserDevicesStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserDevicesStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserDevicesStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserGroupRequestAttributes(TeaModel):
    def __init__(self, idp_id=None, relation=None, user_group_type=None, value=None):
        self.idp_id = idp_id  # type: int
        self.relation = relation  # type: str
        self.user_group_type = user_group_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserGroupRequestAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateUserGroupRequest(TeaModel):
    def __init__(self, attributes=None, description=None, modify_type=None, user_group_id=None):
        self.attributes = attributes  # type: list[UpdateUserGroupRequestAttributes]
        self.description = description  # type: str
        self.modify_type = modify_type  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = UpdateUserGroupRequestAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class UpdateUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserGroupResponseBody, self).to_map()
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


class UpdateUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


