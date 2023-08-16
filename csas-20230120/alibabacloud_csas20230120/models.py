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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class CreatePrivateAccessApplicationShrinkRequest(TeaModel):
    def __init__(self, addresses_shrink=None, description=None, name=None, port_ranges_shrink=None, protocol=None,
                 status=None, tag_ids_shrink=None):
        self.addresses_shrink = addresses_shrink  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.port_ranges_shrink = port_ranges_shrink  # type: str
        self.protocol = protocol  # type: str
        self.status = status  # type: str
        self.tag_ids_shrink = tag_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrivateAccessApplicationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses_shrink is not None:
            result['Addresses'] = self.addresses_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.port_ranges_shrink is not None:
            result['PortRanges'] = self.port_ranges_shrink
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids_shrink is not None:
            result['TagIds'] = self.tag_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses_shrink = m.get('Addresses')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PortRanges') is not None:
            self.port_ranges_shrink = m.get('PortRanges')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids_shrink = m.get('TagIds')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
                 name=None, policy_action=None, priority=None, status=None, tag_ids=None, user_group_ids=None,
                 user_group_mode=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.custom_user_attributes = custom_user_attributes  # type: list[CreatePrivateAccessPolicyRequestCustomUserAttributes]
        self.description = description  # type: str
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


class CreatePrivateAccessPolicyShrinkRequest(TeaModel):
    def __init__(self, application_ids_shrink=None, application_type=None, custom_user_attributes_shrink=None,
                 description=None, name=None, policy_action=None, priority=None, status=None, tag_ids_shrink=None,
                 user_group_ids_shrink=None, user_group_mode=None):
        self.application_ids_shrink = application_ids_shrink  # type: str
        self.application_type = application_type  # type: str
        self.custom_user_attributes_shrink = custom_user_attributes_shrink  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.policy_action = policy_action  # type: str
        self.priority = priority  # type: int
        self.status = status  # type: str
        # 内网访问标签ID集合。最多可输入100个内网访问标签ID。当**ApplicationType**为**Tag时**，必填。和**ApplicationIds**互斥。
        self.tag_ids_shrink = tag_ids_shrink  # type: str
        self.user_group_ids_shrink = user_group_ids_shrink  # type: str
        # 内网访问策略的用户组类型。取值：
        # - **Normal**：普通用户组。
        # - **Custom**：自定义用户组。
        self.user_group_mode = user_group_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrivateAccessPolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids_shrink is not None:
            result['ApplicationIds'] = self.application_ids_shrink
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.custom_user_attributes_shrink is not None:
            result['CustomUserAttributes'] = self.custom_user_attributes_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids_shrink is not None:
            result['TagIds'] = self.tag_ids_shrink
        if self.user_group_ids_shrink is not None:
            result['UserGroupIds'] = self.user_group_ids_shrink
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids_shrink = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CustomUserAttributes') is not None:
            self.custom_user_attributes_shrink = m.get('CustomUserAttributes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids_shrink = m.get('TagIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids_shrink = m.get('UserGroupIds')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
    def __init__(self, addresses=None, application_id=None, create_time=None, description=None, name=None,
                 policy_ids=None, port_ranges=None, protocol=None, status=None, tag_ids=None):
        self.addresses = addresses  # type: list[str]
        self.application_id = application_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
                 description=None, name=None, policy_action=None, policy_id=None, priority=None, status=None, tag_ids=None,
                 user_group_ids=None, user_group_mode=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.create_time = create_time  # type: str
        self.custom_user_attributes = custom_user_attributes  # type: list[GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes]
        self.description = description  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
    def __init__(self, applications=None, connector_id=None, create_time=None, name=None, region_id=None,
                 status=None, switch_status=None, upgrade_time=None):
        self.applications = applications  # type: list[ListConnectorsResponseBodyConnectorsApplications]
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListPrivateAccessApplicationsRequest(TeaModel):
    def __init__(self, address=None, application_ids=None, current_page=None, name=None, page_size=None,
                 policy_id=None, status=None, tag_id=None):
        self.address = address  # type: str
        self.application_ids = application_ids  # type: list[str]
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
    def __init__(self, addresses=None, application_id=None, create_time=None, description=None, name=None,
                 policy_ids=None, port_ranges=None, protocol=None, status=None, tag_ids=None):
        self.addresses = addresses  # type: list[str]
        self.application_id = application_id  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
    def __init__(self, application_id=None, current_page=None, name=None, page_size=None, policy_action=None,
                 policy_ids=None, status=None, tag_id=None, user_group_id=None):
        self.application_id = application_id  # type: str
        self.current_page = current_page  # type: int
        self.name = name  # type: str
        self.page_size = page_size  # type: int
        self.policy_action = policy_action  # type: str
        self.policy_ids = policy_ids  # type: list[str]
        self.status = status  # type: str
        self.tag_id = tag_id  # type: str
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
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
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
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
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
                 description=None, name=None, policy_action=None, policy_id=None, priority=None, status=None, tag_ids=None,
                 user_group_ids=None, user_group_mode=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.create_time = create_time  # type: str
        self.custom_user_attributes = custom_user_attributes  # type: list[ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes]
        self.description = description  # type: str
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
                 tag_ids=None):
        self.application_id = application_id  # type: str
        self.current_page = current_page  # type: int
        self.name = name  # type: str
        self.page_size = page_size  # type: int
        self.policy_id = policy_id  # type: str
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
        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')
        return self


class ListPrivateAccessTagsResponseBodyTags(TeaModel):
    def __init__(self, application_ids=None, create_time=None, description=None, name=None, policy_ids=None,
                 tag_id=None, tag_type=None):
        self.application_ids = application_ids  # type: list[str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.policy_ids = policy_ids  # type: list[str]
        self.tag_id = tag_id  # type: str
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
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[ListPrivateAccessTagsResponseBodyTags]
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class UpdatePrivateAccessApplicationShrinkRequest(TeaModel):
    def __init__(self, addresses_shrink=None, application_id=None, description=None, modify_type=None,
                 port_ranges_shrink=None, protocol=None, status=None, tag_ids_shrink=None):
        self.addresses_shrink = addresses_shrink  # type: str
        self.application_id = application_id  # type: str
        self.description = description  # type: str
        self.modify_type = modify_type  # type: str
        self.port_ranges_shrink = port_ranges_shrink  # type: str
        self.protocol = protocol  # type: str
        self.status = status  # type: str
        self.tag_ids_shrink = tag_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrivateAccessApplicationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addresses_shrink is not None:
            result['Addresses'] = self.addresses_shrink
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.description is not None:
            result['Description'] = self.description
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.port_ranges_shrink is not None:
            result['PortRanges'] = self.port_ranges_shrink
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_ids_shrink is not None:
            result['TagIds'] = self.tag_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses_shrink = m.get('Addresses')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('PortRanges') is not None:
            self.port_ranges_shrink = m.get('PortRanges')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagIds') is not None:
            self.tag_ids_shrink = m.get('TagIds')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
                 modify_type=None, policy_action=None, policy_id=None, priority=None, status=None, tag_ids=None,
                 user_group_ids=None, user_group_mode=None):
        self.application_ids = application_ids  # type: list[str]
        self.application_type = application_type  # type: str
        self.custom_user_attributes = custom_user_attributes  # type: list[UpdatePrivateAccessPolicyRequestCustomUserAttributes]
        self.description = description  # type: str
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


class UpdatePrivateAccessPolicyShrinkRequest(TeaModel):
    def __init__(self, application_ids_shrink=None, application_type=None, custom_user_attributes_shrink=None,
                 description=None, modify_type=None, policy_action=None, policy_id=None, priority=None, status=None,
                 tag_ids_shrink=None, user_group_ids_shrink=None, user_group_mode=None):
        self.application_ids_shrink = application_ids_shrink  # type: str
        self.application_type = application_type  # type: str
        self.custom_user_attributes_shrink = custom_user_attributes_shrink  # type: str
        self.description = description  # type: str
        self.modify_type = modify_type  # type: str
        self.policy_action = policy_action  # type: str
        self.policy_id = policy_id  # type: str
        self.priority = priority  # type: int
        self.status = status  # type: str
        # 内网访问标签ID集合。一条策略最多支持100个内网访问标签ID。
        self.tag_ids_shrink = tag_ids_shrink  # type: str
        self.user_group_ids_shrink = user_group_ids_shrink  # type: str
        # 内网访问策略的用户组类型。取值：
        # - **Normal**：普通用户组。
        # - **Custom**：自定义用户组。
        self.user_group_mode = user_group_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrivateAccessPolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_ids_shrink is not None:
            result['ApplicationIds'] = self.application_ids_shrink
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.custom_user_attributes_shrink is not None:
            result['CustomUserAttributes'] = self.custom_user_attributes_shrink
        if self.description is not None:
            result['Description'] = self.description
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
        if self.tag_ids_shrink is not None:
            result['TagIds'] = self.tag_ids_shrink
        if self.user_group_ids_shrink is not None:
            result['UserGroupIds'] = self.user_group_ids_shrink
        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids_shrink = m.get('ApplicationIds')
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CustomUserAttributes') is not None:
            self.custom_user_attributes_shrink = m.get('CustomUserAttributes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
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
            self.tag_ids_shrink = m.get('TagIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids_shrink = m.get('UserGroupIds')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


