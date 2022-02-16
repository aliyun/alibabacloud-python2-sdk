# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddCidrToConnectionPoolRequest(TeaModel):
    def __init__(self, cidrs=None, client_token=None, connection_pool_id=None, dry_run=None,
                 io_tcloud_connector_id=None, region_id=None):
        self.cidrs = cidrs  # type: list[str]
        self.client_token = client_token  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCidrToConnectionPoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddCidrToConnectionPoolResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCidrToConnectionPoolResponseBody, self).to_map()
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


class AddCidrToConnectionPoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddCidrToConnectionPoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddCidrToConnectionPoolResponse, self).to_map()
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
            temp_model = AddCidrToConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddIoTCloudConnectorToGroupRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_group_id=None,
                 io_tcloud_connector_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIoTCloudConnectorToGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddIoTCloudConnectorToGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIoTCloudConnectorToGroupResponseBody, self).to_map()
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


class AddIoTCloudConnectorToGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddIoTCloudConnectorToGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddIoTCloudConnectorToGroupResponse, self).to_map()
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
            temp_model = AddIoTCloudConnectorToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateIpWithConnectionPoolRequest(TeaModel):
    def __init__(self, client_token=None, connection_pool_id=None, dry_run=None, io_tcloud_connector_id=None,
                 ips=None, ips_file_path=None, region_id=None):
        self.client_token = client_token  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.ips = ips  # type: list[str]
        self.ips_file_path = ips_file_path  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateIpWithConnectionPoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.ips_file_path is not None:
            result['IpsFilePath'] = self.ips_file_path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('IpsFilePath') is not None:
            self.ips_file_path = m.get('IpsFilePath')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateIpWithConnectionPoolResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateIpWithConnectionPoolResponseBody, self).to_map()
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


class AssociateIpWithConnectionPoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssociateIpWithConnectionPoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateIpWithConnectionPoolResponse, self).to_map()
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
            temp_model = AssociateIpWithConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateVSwitchWithIoTCloudConnectorRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None,
                 v_switch_list=None, vpc_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str
        self.v_switch_list = v_switch_list  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateVSwitchWithIoTCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_list is not None:
            result['VSwitchList'] = self.v_switch_list
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchList') is not None:
            self.v_switch_list = m.get('VSwitchList')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class AssociateVSwitchWithIoTCloudConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateVSwitchWithIoTCloudConnectorResponseBody, self).to_map()
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


class AssociateVSwitchWithIoTCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssociateVSwitchWithIoTCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateVSwitchWithIoTCloudConnectorResponse, self).to_map()
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
            temp_model = AssociateVSwitchWithIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthorizationRuleRequest(TeaModel):
    def __init__(self, authorization_rule_description=None, authorization_rule_name=None, client_token=None,
                 destination=None, destination_type=None, dry_run=None, io_tcloud_connector_id=None, policy=None,
                 region_id=None, source_cidrs=None):
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.client_token = client_token  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.policy = policy  # type: str
        self.region_id = region_id  # type: str
        self.source_cidrs = source_cidrs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthorizationRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class CreateAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, authorization_rule_id=None, request_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthorizationRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAuthorizationRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAuthorizationRuleResponse, self).to_map()
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
            temp_model = CreateAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnectionPoolRequest(TeaModel):
    def __init__(self, cidrs=None, client_token=None, connection_pool_description=None, connection_pool_name=None,
                 count=None, dry_run=None, io_tcloud_connector_id=None, region_id=None):
        self.cidrs = cidrs  # type: list[str]
        self.client_token = client_token  # type: str
        self.connection_pool_description = connection_pool_description  # type: str
        self.connection_pool_name = connection_pool_name  # type: str
        self.count = count  # type: long
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionPoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.count is not None:
            result['Count'] = self.count
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateConnectionPoolResponseBody(TeaModel):
    def __init__(self, connection_pool_id=None, request_id=None):
        self.connection_pool_id = connection_pool_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionPoolResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConnectionPoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateConnectionPoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConnectionPoolResponse, self).to_map()
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
            temp_model = CreateConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDNSServiceRuleRequest(TeaModel):
    def __init__(self, authorization_rule_description=None, authorization_rule_name=None, client_token=None,
                 destination=None, dry_run=None, io_tcloud_connector_id=None, region_id=None, service_type=None, source=None):
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.client_token = client_token  # type: str
        self.destination = destination  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDNSServiceRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateDNSServiceRuleResponseBody(TeaModel):
    def __init__(self, dnsservice_rule_id=None, request_id=None):
        self.dnsservice_rule_id = dnsservice_rule_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDNSServiceRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDNSServiceRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDNSServiceRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDNSServiceRuleResponse, self).to_map()
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
            temp_model = CreateDNSServiceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupAuthorizationRuleRequest(TeaModel):
    def __init__(self, authorization_rule_description=None, authorization_rule_name=None, client_token=None,
                 destination=None, destination_type=None, dry_run=None, io_tcloud_connector_group_id=None, policy=None,
                 region_id=None, source_cidrs=None):
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.client_token = client_token  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.policy = policy  # type: str
        self.region_id = region_id  # type: str
        self.source_cidrs = source_cidrs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupAuthorizationRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class CreateGroupAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, authorization_rule_id=None, io_tcloud_connector_group_id=None, request_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupAuthorizationRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupAuthorizationRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGroupAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupAuthorizationRuleResponse, self).to_map()
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
            temp_model = CreateGroupAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupDNSServiceRuleRequest(TeaModel):
    def __init__(self, client_token=None, dnsservice_rule_description=None, dnsservice_rule_name=None,
                 destination=None, dry_run=None, io_tcloud_connector_group_id=None, region_id=None, service_type=None,
                 source=None):
        self.client_token = client_token  # type: str
        self.dnsservice_rule_description = dnsservice_rule_description  # type: str
        self.dnsservice_rule_name = dnsservice_rule_name  # type: str
        self.destination = destination  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.region_id = region_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupDNSServiceRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dnsservice_rule_description is not None:
            result['DNSServiceRuleDescription'] = self.dnsservice_rule_description
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DNSServiceRuleDescription') is not None:
            self.dnsservice_rule_description = m.get('DNSServiceRuleDescription')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateGroupDNSServiceRuleResponseBody(TeaModel):
    def __init__(self, dnsservice_rule_id=None, io_tcloud_connector_group_id=None, request_id=None):
        self.dnsservice_rule_id = dnsservice_rule_id  # type: str
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupDNSServiceRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupDNSServiceRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGroupDNSServiceRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupDNSServiceRuleResponse, self).to_map()
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
            temp_model = CreateGroupDNSServiceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIoTCloudConnectorRequest(TeaModel):
    def __init__(self, apn=None, client_token=None, dry_run=None, isp=None, io_tcloud_connector_description=None,
                 io_tcloud_connector_name=None, region_id=None, resource_uid=None, wildcard_domain_enabled=None):
        self.apn = apn  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.isp = isp  # type: str
        self.io_tcloud_connector_description = io_tcloud_connector_description  # type: str
        self.io_tcloud_connector_name = io_tcloud_connector_name  # type: str
        self.region_id = region_id  # type: str
        self.resource_uid = resource_uid  # type: long
        self.wildcard_domain_enabled = wildcard_domain_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIoTCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        return self


class CreateIoTCloudConnectorResponseBody(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, request_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIoTCloudConnectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIoTCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIoTCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIoTCloudConnectorResponse, self).to_map()
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
            temp_model = CreateIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIoTCloudConnectorGroupRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, name=None, region_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIoTCloudConnectorGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateIoTCloudConnectorGroupResponseBody(TeaModel):
    def __init__(self, io_tcloud_connector_group_id=None, request_id=None):
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIoTCloudConnectorGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIoTCloudConnectorGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIoTCloudConnectorGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIoTCloudConnectorGroupResponse, self).to_map()
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
            temp_model = CreateIoTCloudConnectorGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None,
                 service_description=None, service_name=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str
        self.service_description = service_description  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(self, request_id=None, service_id=None):
        self.request_id = request_id  # type: str
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceResponse, self).to_map()
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceEntryRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None,
                 service_entry_description=None, service_entry_name=None, service_id=None, target=None, target_type=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str
        self.service_entry_description = service_entry_description  # type: str
        self.service_entry_name = service_entry_name  # type: str
        self.service_id = service_id  # type: str
        self.target = target  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceEntryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateServiceEntryResponseBody(TeaModel):
    def __init__(self, request_id=None, service_entry_id=None):
        self.request_id = request_id  # type: str
        self.service_entry_id = service_entry_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceEntryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        return self


class CreateServiceEntryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceEntryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceEntryResponse, self).to_map()
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
            temp_model = CreateServiceEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthorizationRuleRequest(TeaModel):
    def __init__(self, authorization_rule_id=None, client_token=None, dry_run=None, io_tcloud_connector_id=None,
                 region_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAuthorizationRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAuthorizationRuleResponseBody, self).to_map()
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


class DeleteAuthorizationRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAuthorizationRuleResponse, self).to_map()
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
            temp_model = DeleteAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnectionPoolRequest(TeaModel):
    def __init__(self, client_token=None, connection_pool_id=None, dry_run=None, io_tcloud_connector_id=None,
                 region_id=None):
        self.client_token = client_token  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConnectionPoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteConnectionPoolResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConnectionPoolResponseBody, self).to_map()
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


class DeleteConnectionPoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteConnectionPoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteConnectionPoolResponse, self).to_map()
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
            temp_model = DeleteConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDNSServiceRuleRequest(TeaModel):
    def __init__(self, client_token=None, dnsservice_rule_id=None, dry_run=None, io_tcloud_connector_id=None,
                 region_id=None):
        self.client_token = client_token  # type: str
        self.dnsservice_rule_id = dnsservice_rule_id  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDNSServiceRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDNSServiceRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDNSServiceRuleResponseBody, self).to_map()
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


class DeleteDNSServiceRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDNSServiceRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDNSServiceRuleResponse, self).to_map()
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
            temp_model = DeleteDNSServiceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupAuthorizationRuleRequest(TeaModel):
    def __init__(self, authorization_rule_id=None, client_token=None, dry_run=None,
                 io_tcloud_connector_group_id=None, region_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupAuthorizationRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteGroupAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupAuthorizationRuleResponseBody, self).to_map()
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


class DeleteGroupAuthorizationRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGroupAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGroupAuthorizationRuleResponse, self).to_map()
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
            temp_model = DeleteGroupAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupDNSServiceRuleRequest(TeaModel):
    def __init__(self, client_token=None, dnsservice_rule_id=None, dry_run=None, io_tcloud_connector_group_id=None,
                 region_id=None):
        self.client_token = client_token  # type: str
        self.dnsservice_rule_id = dnsservice_rule_id  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupDNSServiceRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteGroupDNSServiceRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupDNSServiceRuleResponseBody, self).to_map()
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


class DeleteGroupDNSServiceRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGroupDNSServiceRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGroupDNSServiceRuleResponse, self).to_map()
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
            temp_model = DeleteGroupDNSServiceRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIoTCloudConnectorRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIoTCloudConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorResponseBody, self).to_map()
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


class DeleteIoTCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteIoTCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorResponse, self).to_map()
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
            temp_model = DeleteIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIoTCloudConnectorGroupRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_group_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIoTCloudConnectorGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorGroupResponseBody, self).to_map()
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


class DeleteIoTCloudConnectorGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteIoTCloudConnectorGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorGroupResponse, self).to_map()
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
            temp_model = DeleteIoTCloudConnectorGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None,
                 service_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceResponseBody, self).to_map()
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


class DeleteServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceResponse, self).to_map()
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
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceEntryRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None,
                 service_entry_id=None, service_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str
        self.service_entry_id = service_entry_id  # type: str
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceEntryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceEntryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceEntryResponseBody, self).to_map()
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


class DeleteServiceEntryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceEntryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceEntryResponse, self).to_map()
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
            temp_model = DeleteServiceEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableIoTCloudConnectorAccessLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableIoTCloudConnectorAccessLogResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableIoTCloudConnectorAccessLogResponseBody, self).to_map()
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


class DisableIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableIoTCloudConnectorAccessLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableIoTCloudConnectorAccessLogResponse, self).to_map()
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
            temp_model = DisableIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateIpFromConnectionPoolRequest(TeaModel):
    def __init__(self, client_token=None, connection_pool_id=None, dry_run=None, io_tcloud_connector_id=None,
                 ips=None, ips_file_path=None, region_id=None):
        self.client_token = client_token  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.ips = ips  # type: list[str]
        self.ips_file_path = ips_file_path  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateIpFromConnectionPoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.ips_file_path is not None:
            result['IpsFilePath'] = self.ips_file_path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('IpsFilePath') is not None:
            self.ips_file_path = m.get('IpsFilePath')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateIpFromConnectionPoolResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateIpFromConnectionPoolResponseBody, self).to_map()
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


class DissociateIpFromConnectionPoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DissociateIpFromConnectionPoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateIpFromConnectionPoolResponse, self).to_map()
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
            temp_model = DissociateIpFromConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateVSwitchFromIoTCloudConnectorRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateVSwitchFromIoTCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateVSwitchFromIoTCloudConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateVSwitchFromIoTCloudConnectorResponseBody, self).to_map()
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


class DissociateVSwitchFromIoTCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DissociateVSwitchFromIoTCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateVSwitchFromIoTCloudConnectorResponse, self).to_map()
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
            temp_model = DissociateVSwitchFromIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(self, access_log_sls_log_store=None, access_log_sls_project=None, client_token=None, dry_run=None,
                 io_tcloud_connector_id=None, region_id=None):
        self.access_log_sls_log_store = access_log_sls_log_store  # type: str
        self.access_log_sls_project = access_log_sls_project  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableIoTCloudConnectorAccessLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_sls_log_store is not None:
            result['AccessLogSlsLogStore'] = self.access_log_sls_log_store
        if self.access_log_sls_project is not None:
            result['AccessLogSlsProject'] = self.access_log_sls_project
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLogSlsLogStore') is not None:
            self.access_log_sls_log_store = m.get('AccessLogSlsLogStore')
        if m.get('AccessLogSlsProject') is not None:
            self.access_log_sls_project = m.get('AccessLogSlsProject')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableIoTCloudConnectorAccessLogResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableIoTCloudConnectorAccessLogResponseBody, self).to_map()
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


class EnableIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableIoTCloudConnectorAccessLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableIoTCloudConnectorAccessLogResponse, self).to_map()
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
            temp_model = EnableIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionPoolIpOperationResultRequest(TeaModel):
    def __init__(self, connection_pool_id=None, io_tcloud_connector_id=None, query_request_id=None, region_id=None):
        self.connection_pool_id = connection_pool_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.query_request_id = query_request_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionPoolIpOperationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.query_request_id is not None:
            result['QueryRequestId'] = self.query_request_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('QueryRequestId') is not None:
            self.query_request_id = m.get('QueryRequestId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetConnectionPoolIpOperationResultResponseBody(TeaModel):
    def __init__(self, request_id=None, result_file_paths=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # OssPath
        self.result_file_paths = result_file_paths  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionPoolIpOperationResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_file_paths is not None:
            result['ResultFilePaths'] = self.result_file_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultFilePaths') is not None:
            self.result_file_paths = m.get('ResultFilePaths')
        return self


class GetConnectionPoolIpOperationResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetConnectionPoolIpOperationResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConnectionPoolIpOperationResultResponse, self).to_map()
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
            temp_model = GetConnectionPoolIpOperationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiagnoseResultForSingleCardRequest(TeaModel):
    def __init__(self, diagnose_task_id=None, region_id=None):
        self.diagnose_task_id = diagnose_task_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDiagnoseResultForSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnose_task_id is not None:
            result['DiagnoseTaskId'] = self.diagnose_task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiagnoseTaskId') is not None:
            self.diagnose_task_id = m.get('DiagnoseTaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetDiagnoseResultForSingleCardResponseBodyDiagnoseItem(TeaModel):
    def __init__(self, part=None, status=None):
        self.part = part  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDiagnoseResultForSingleCardResponseBodyDiagnoseItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.part is not None:
            result['Part'] = self.part
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Part') is not None:
            self.part = m.get('Part')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDiagnoseResultForSingleCardResponseBodyErrorResult(TeaModel):
    def __init__(self, error_desc=None, error_level=None, error_part=None, error_suggestion=None):
        self.error_desc = error_desc  # type: str
        self.error_level = error_level  # type: str
        self.error_part = error_part  # type: str
        self.error_suggestion = error_suggestion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDiagnoseResultForSingleCardResponseBodyErrorResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_desc is not None:
            result['ErrorDesc'] = self.error_desc
        if self.error_level is not None:
            result['ErrorLevel'] = self.error_level
        if self.error_part is not None:
            result['ErrorPart'] = self.error_part
        if self.error_suggestion is not None:
            result['ErrorSuggestion'] = self.error_suggestion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorDesc') is not None:
            self.error_desc = m.get('ErrorDesc')
        if m.get('ErrorLevel') is not None:
            self.error_level = m.get('ErrorLevel')
        if m.get('ErrorPart') is not None:
            self.error_part = m.get('ErrorPart')
        if m.get('ErrorSuggestion') is not None:
            self.error_suggestion = m.get('ErrorSuggestion')
        return self


class GetDiagnoseResultForSingleCardResponseBody(TeaModel):
    def __init__(self, begin_time=None, card_ip=None, destination=None, diagnose_item=None, end_time=None,
                 error_result=None, icc_id=None, io_tcloud_connector_id=None, request_id=None, status=None):
        self.begin_time = begin_time  # type: long
        self.card_ip = card_ip  # type: str
        self.destination = destination  # type: str
        self.diagnose_item = diagnose_item  # type: list[GetDiagnoseResultForSingleCardResponseBodyDiagnoseItem]
        self.end_time = end_time  # type: long
        self.error_result = error_result  # type: list[GetDiagnoseResultForSingleCardResponseBodyErrorResult]
        self.icc_id = icc_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.diagnose_item:
            for k in self.diagnose_item:
                if k:
                    k.validate()
        if self.error_result:
            for k in self.error_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDiagnoseResultForSingleCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.card_ip is not None:
            result['CardIp'] = self.card_ip
        if self.destination is not None:
            result['Destination'] = self.destination
        result['DiagnoseItem'] = []
        if self.diagnose_item is not None:
            for k in self.diagnose_item:
                result['DiagnoseItem'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['ErrorResult'] = []
        if self.error_result is not None:
            for k in self.error_result:
                result['ErrorResult'].append(k.to_map() if k else None)
        if self.icc_id is not None:
            result['IccId'] = self.icc_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CardIp') is not None:
            self.card_ip = m.get('CardIp')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        self.diagnose_item = []
        if m.get('DiagnoseItem') is not None:
            for k in m.get('DiagnoseItem'):
                temp_model = GetDiagnoseResultForSingleCardResponseBodyDiagnoseItem()
                self.diagnose_item.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.error_result = []
        if m.get('ErrorResult') is not None:
            for k in m.get('ErrorResult'):
                temp_model = GetDiagnoseResultForSingleCardResponseBodyErrorResult()
                self.error_result.append(temp_model.from_map(k))
        if m.get('IccId') is not None:
            self.icc_id = m.get('IccId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDiagnoseResultForSingleCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDiagnoseResultForSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDiagnoseResultForSingleCardResponse, self).to_map()
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
            temp_model = GetDiagnoseResultForSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIoTCloudConnectorAccessLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIoTCloudConnectorAccessLogResponseBody(TeaModel):
    def __init__(self, access_log_sls_log_store=None, access_log_sls_project=None, access_log_status=None,
                 request_id=None):
        self.access_log_sls_log_store = access_log_sls_log_store  # type: str
        self.access_log_sls_project = access_log_sls_project  # type: str
        self.access_log_status = access_log_status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIoTCloudConnectorAccessLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_sls_log_store is not None:
            result['AccessLogSlsLogStore'] = self.access_log_sls_log_store
        if self.access_log_sls_project is not None:
            result['AccessLogSlsProject'] = self.access_log_sls_project
        if self.access_log_status is not None:
            result['AccessLogStatus'] = self.access_log_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLogSlsLogStore') is not None:
            self.access_log_sls_log_store = m.get('AccessLogSlsLogStore')
        if m.get('AccessLogSlsProject') is not None:
            self.access_log_sls_project = m.get('AccessLogSlsProject')
        if m.get('AccessLogStatus') is not None:
            self.access_log_status = m.get('AccessLogStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetIoTCloudConnectorAccessLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIoTCloudConnectorAccessLogResponse, self).to_map()
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
            temp_model = GetIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStsInfoAndOssPathRequest(TeaModel):
    def __init__(self, client_token=None, connection_pool_id=None, dry_run=None, file_name=None,
                 io_tcloud_connector_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.dry_run = dry_run  # type: bool
        self.file_name = file_name  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStsInfoAndOssPathRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetStsInfoAndOssPathResponseBody(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, expiration=None, oss_path=None, request_id=None,
                 security_token=None):
        # Sts info of accessKeyId
        self.access_key_id = access_key_id  # type: str
        # Sts info of accessKeySecret
        self.access_key_secret = access_key_secret  # type: str
        # Sts info expiration time
        self.expiration = expiration  # type: str
        # OssPath
        self.oss_path = oss_path  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # Sts info of securityToken
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStsInfoAndOssPathResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetStsInfoAndOssPathResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetStsInfoAndOssPathResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStsInfoAndOssPathResponse, self).to_map()
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
            temp_model = GetStsInfoAndOssPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantVirtualBorderRouterRequest(TeaModel):
    def __init__(self, region_id=None, virtual_border_router_id=None):
        self.region_id = region_id  # type: str
        self.virtual_border_router_id = virtual_border_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantVirtualBorderRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_border_router_id is not None:
            result['VirtualBorderRouterId'] = self.virtual_border_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualBorderRouterId') is not None:
            self.virtual_border_router_id = m.get('VirtualBorderRouterId')
        return self


class GrantVirtualBorderRouterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantVirtualBorderRouterResponseBody, self).to_map()
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


class GrantVirtualBorderRouterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GrantVirtualBorderRouterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantVirtualBorderRouterResponse, self).to_map()
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
            temp_model = GrantVirtualBorderRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAPNsRequest(TeaModel):
    def __init__(self, apn=None, isp=None, max_results=None, next_token=None, region_id=None):
        self.apn = apn  # type: str
        self.isp = isp  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAPNsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAPNsResponseBodyAPNs(TeaModel):
    def __init__(self, apn=None, description=None, feature_list=None, isp=None, name=None, zone_list=None):
        self.apn = apn  # type: str
        self.description = description  # type: str
        self.feature_list = feature_list  # type: list[str]
        self.isp = isp  # type: str
        self.name = name  # type: str
        self.zone_list = zone_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAPNsResponseBodyAPNs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.description is not None:
            result['Description'] = self.description
        if self.feature_list is not None:
            result['FeatureList'] = self.feature_list
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.zone_list is not None:
            result['ZoneList'] = self.zone_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FeatureList') is not None:
            self.feature_list = m.get('FeatureList')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ZoneList') is not None:
            self.zone_list = m.get('ZoneList')
        return self


class ListAPNsResponseBody(TeaModel):
    def __init__(self, apns=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.apns = apns  # type: list[ListAPNsResponseBodyAPNs]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.apns:
            for k in self.apns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAPNsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['APNs'] = []
        if self.apns is not None:
            for k in self.apns:
                result['APNs'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apns = []
        if m.get('APNs') is not None:
            for k in m.get('APNs'):
                temp_model = ListAPNsResponseBodyAPNs()
                self.apns.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAPNsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAPNsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAPNsResponse, self).to_map()
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
            temp_model = ListAPNsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizationRulesRequest(TeaModel):
    def __init__(self, authorization_rule_ids=None, authorization_rule_name=None, authorization_rule_status=None,
                 destination=None, destination_type=None, io_tcloud_connector_id=None, max_results=None, next_token=None,
                 policy=None, region_id=None):
        self.authorization_rule_ids = authorization_rule_ids  # type: list[str]
        self.authorization_rule_name = authorization_rule_name  # type: list[str]
        self.authorization_rule_status = authorization_rule_status  # type: list[str]
        self.destination = destination  # type: list[str]
        self.destination_type = destination_type  # type: list[str]
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.policy = policy  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthorizationRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_ids is not None:
            result['AuthorizationRuleIds'] = self.authorization_rule_ids
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleIds') is not None:
            self.authorization_rule_ids = m.get('AuthorizationRuleIds')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAuthorizationRulesResponseBodyAuthorizationRules(TeaModel):
    def __init__(self, authorization_rule_description=None, authorization_rule_id=None,
                 authorization_rule_name=None, authorization_rule_status=None, destination=None, destination_type=None,
                 io_tcloud_connector_id=None, policy=None, source_cidrs=None):
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.authorization_rule_status = authorization_rule_status  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.policy = policy  # type: str
        self.source_cidrs = source_cidrs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthorizationRulesResponseBodyAuthorizationRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class ListAuthorizationRulesResponseBody(TeaModel):
    def __init__(self, authorization_rules=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.authorization_rules = authorization_rules  # type: list[ListAuthorizationRulesResponseBodyAuthorizationRules]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.authorization_rules:
            for k in self.authorization_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAuthorizationRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthorizationRules'] = []
        if self.authorization_rules is not None:
            for k in self.authorization_rules:
                result['AuthorizationRules'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.authorization_rules = []
        if m.get('AuthorizationRules') is not None:
            for k in m.get('AuthorizationRules'):
                temp_model = ListAuthorizationRulesResponseBodyAuthorizationRules()
                self.authorization_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAuthorizationRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAuthorizationRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAuthorizationRulesResponse, self).to_map()
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
            temp_model = ListAuthorizationRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionPoolAllIpsRequest(TeaModel):
    def __init__(self, connection_pool_id=None, io_tcloud_connector_id=None, ip=None, max_results=None,
                 next_token=None, region_id=None, type=None):
        self.connection_pool_id = connection_pool_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.ip = ip  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionPoolAllIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListConnectionPoolAllIpsResponseBodyConnectionPoolIps(TeaModel):
    def __init__(self, connection_pool_id=None, ip=None, ip_num=None, status=None, type=None):
        self.connection_pool_id = connection_pool_id  # type: str
        self.ip = ip  # type: str
        self.ip_num = ip_num  # type: long
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionPoolAllIpsResponseBodyConnectionPoolIps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_num is not None:
            result['IpNum'] = self.ip_num
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpNum') is not None:
            self.ip_num = m.get('IpNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListConnectionPoolAllIpsResponseBody(TeaModel):
    def __init__(self, connection_pool_ips=None, max_results=None, next_token=None, request_id=None,
                 total_ips_count=None):
        self.connection_pool_ips = connection_pool_ips  # type: list[ListConnectionPoolAllIpsResponseBodyConnectionPoolIps]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_ips_count = total_ips_count  # type: int

    def validate(self):
        if self.connection_pool_ips:
            for k in self.connection_pool_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConnectionPoolAllIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionPoolIps'] = []
        if self.connection_pool_ips is not None:
            for k in self.connection_pool_ips:
                result['ConnectionPoolIps'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_ips_count is not None:
            result['TotalIpsCount'] = self.total_ips_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connection_pool_ips = []
        if m.get('ConnectionPoolIps') is not None:
            for k in m.get('ConnectionPoolIps'):
                temp_model = ListConnectionPoolAllIpsResponseBodyConnectionPoolIps()
                self.connection_pool_ips.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalIpsCount') is not None:
            self.total_ips_count = m.get('TotalIpsCount')
        return self


class ListConnectionPoolAllIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListConnectionPoolAllIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConnectionPoolAllIpsResponse, self).to_map()
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
            temp_model = ListConnectionPoolAllIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionPoolIpsRequest(TeaModel):
    def __init__(self, connection_pool_id=None, io_tcloud_connector_id=None, ip=None, max_results=None,
                 next_token=None, region_id=None):
        self.connection_pool_id = connection_pool_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.ip = ip  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionPoolIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListConnectionPoolIpsResponseBodyConnectionPoolIps(TeaModel):
    def __init__(self, connection_pool_id=None, ip=None, status=None):
        self.connection_pool_id = connection_pool_id  # type: str
        self.ip = ip  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionPoolIpsResponseBodyConnectionPoolIps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListConnectionPoolIpsResponseBody(TeaModel):
    def __init__(self, connection_pool_ips=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.connection_pool_ips = connection_pool_ips  # type: list[ListConnectionPoolIpsResponseBodyConnectionPoolIps]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.connection_pool_ips:
            for k in self.connection_pool_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConnectionPoolIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionPoolIps'] = []
        if self.connection_pool_ips is not None:
            for k in self.connection_pool_ips:
                result['ConnectionPoolIps'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connection_pool_ips = []
        if m.get('ConnectionPoolIps') is not None:
            for k in m.get('ConnectionPoolIps'):
                temp_model = ListConnectionPoolIpsResponseBodyConnectionPoolIps()
                self.connection_pool_ips.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListConnectionPoolIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListConnectionPoolIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConnectionPoolIpsResponse, self).to_map()
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
            temp_model = ListConnectionPoolIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionPoolsRequest(TeaModel):
    def __init__(self, connection_pool_ids=None, connection_pool_name=None, connection_pool_status=None,
                 io_tcloud_connector_id=None, max_results=None, next_token=None, region_id=None):
        self.connection_pool_ids = connection_pool_ids  # type: list[str]
        self.connection_pool_name = connection_pool_name  # type: list[str]
        self.connection_pool_status = connection_pool_status  # type: list[str]
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionPoolsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_ids is not None:
            result['ConnectionPoolIds'] = self.connection_pool_ids
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_status is not None:
            result['ConnectionPoolStatus'] = self.connection_pool_status
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionPoolIds') is not None:
            self.connection_pool_ids = m.get('ConnectionPoolIds')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolStatus') is not None:
            self.connection_pool_status = m.get('ConnectionPoolStatus')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListConnectionPoolsResponseBodyConnectionPools(TeaModel):
    def __init__(self, cidrs=None, connection_pool_description=None, connection_pool_id=None,
                 connection_pool_name=None, connection_pool_status=None, operate_result_request_id=None):
        self.cidrs = cidrs  # type: list[str]
        self.connection_pool_description = connection_pool_description  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.connection_pool_name = connection_pool_name  # type: str
        self.connection_pool_status = connection_pool_status  # type: str
        self.operate_result_request_id = operate_result_request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionPoolsResponseBodyConnectionPools, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_status is not None:
            result['ConnectionPoolStatus'] = self.connection_pool_status
        if self.operate_result_request_id is not None:
            result['OperateResultRequestID'] = self.operate_result_request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolStatus') is not None:
            self.connection_pool_status = m.get('ConnectionPoolStatus')
        if m.get('OperateResultRequestID') is not None:
            self.operate_result_request_id = m.get('OperateResultRequestID')
        return self


class ListConnectionPoolsResponseBody(TeaModel):
    def __init__(self, connection_pools=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.connection_pools = connection_pools  # type: list[ListConnectionPoolsResponseBodyConnectionPools]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.connection_pools:
            for k in self.connection_pools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConnectionPoolsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionPools'] = []
        if self.connection_pools is not None:
            for k in self.connection_pools:
                result['ConnectionPools'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connection_pools = []
        if m.get('ConnectionPools') is not None:
            for k in m.get('ConnectionPools'):
                temp_model = ListConnectionPoolsResponseBodyConnectionPools()
                self.connection_pools.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListConnectionPoolsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListConnectionPoolsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConnectionPoolsResponse, self).to_map()
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
            temp_model = ListConnectionPoolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDNSServiceRulesRequest(TeaModel):
    def __init__(self, dnsservice_rule_ids=None, dnsservice_rule_name=None, dnsservice_rule_status=None,
                 destination=None, io_tcloud_connector_id=None, max_results=None, next_token=None, region_id=None,
                 service_type=None, source=None):
        self.dnsservice_rule_ids = dnsservice_rule_ids  # type: list[str]
        self.dnsservice_rule_name = dnsservice_rule_name  # type: list[str]
        self.dnsservice_rule_status = dnsservice_rule_status  # type: list[str]
        self.destination = destination  # type: list[str]
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDNSServiceRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_ids is not None:
            result['DNSServiceRuleIds'] = self.dnsservice_rule_ids
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.dnsservice_rule_status is not None:
            result['DNSServiceRuleStatus'] = self.dnsservice_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DNSServiceRuleIds') is not None:
            self.dnsservice_rule_ids = m.get('DNSServiceRuleIds')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('DNSServiceRuleStatus') is not None:
            self.dnsservice_rule_status = m.get('DNSServiceRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListDNSServiceRulesResponseBodyDNSServiceRules(TeaModel):
    def __init__(self, dnsservice_rule_description=None, dnsservice_rule_id=None, dnsservice_rule_name=None,
                 dnsservice_rule_status=None, destination=None, io_tcloud_connector_id=None, service_type=None, source=None):
        self.dnsservice_rule_description = dnsservice_rule_description  # type: str
        self.dnsservice_rule_id = dnsservice_rule_id  # type: str
        self.dnsservice_rule_name = dnsservice_rule_name  # type: str
        self.dnsservice_rule_status = dnsservice_rule_status  # type: str
        self.destination = destination  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDNSServiceRulesResponseBodyDNSServiceRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_description is not None:
            result['DNSServiceRuleDescription'] = self.dnsservice_rule_description
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.dnsservice_rule_status is not None:
            result['DNSServiceRuleStatus'] = self.dnsservice_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DNSServiceRuleDescription') is not None:
            self.dnsservice_rule_description = m.get('DNSServiceRuleDescription')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('DNSServiceRuleStatus') is not None:
            self.dnsservice_rule_status = m.get('DNSServiceRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListDNSServiceRulesResponseBody(TeaModel):
    def __init__(self, dnsservice_rules=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.dnsservice_rules = dnsservice_rules  # type: list[ListDNSServiceRulesResponseBodyDNSServiceRules]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.dnsservice_rules:
            for k in self.dnsservice_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDNSServiceRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DNSServiceRules'] = []
        if self.dnsservice_rules is not None:
            for k in self.dnsservice_rules:
                result['DNSServiceRules'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dnsservice_rules = []
        if m.get('DNSServiceRules') is not None:
            for k in m.get('DNSServiceRules'):
                temp_model = ListDNSServiceRulesResponseBodyDNSServiceRules()
                self.dnsservice_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDNSServiceRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDNSServiceRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDNSServiceRulesResponse, self).to_map()
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
            temp_model = ListDNSServiceRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiagnoseInfoForSingleCardRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, max_results=None, next_token=None, region_id=None, source=None,
                 source_type=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.source = source  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDiagnoseInfoForSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ListDiagnoseInfoForSingleCardResponseBodyDiagnoseInfo(TeaModel):
    def __init__(self, begin_time=None, card_ip=None, destination=None, destination_type=None, diagnose_time=None,
                 end_time=None, icc_id=None, io_tcloud_connector_id=None, source=None, source_type=None, status=None,
                 task_id=None):
        self.begin_time = begin_time  # type: long
        self.card_ip = card_ip  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.diagnose_time = diagnose_time  # type: long
        self.end_time = end_time  # type: long
        self.icc_id = icc_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.source = source  # type: str
        self.source_type = source_type  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDiagnoseInfoForSingleCardResponseBodyDiagnoseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.card_ip is not None:
            result['CardIp'] = self.card_ip
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.diagnose_time is not None:
            result['DiagnoseTime'] = self.diagnose_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.icc_id is not None:
            result['IccId'] = self.icc_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CardIp') is not None:
            self.card_ip = m.get('CardIp')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DiagnoseTime') is not None:
            self.diagnose_time = m.get('DiagnoseTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IccId') is not None:
            self.icc_id = m.get('IccId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListDiagnoseInfoForSingleCardResponseBody(TeaModel):
    def __init__(self, diagnose_info=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.diagnose_info = diagnose_info  # type: list[ListDiagnoseInfoForSingleCardResponseBodyDiagnoseInfo]
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.diagnose_info:
            for k in self.diagnose_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDiagnoseInfoForSingleCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiagnoseInfo'] = []
        if self.diagnose_info is not None:
            for k in self.diagnose_info:
                result['DiagnoseInfo'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.diagnose_info = []
        if m.get('DiagnoseInfo') is not None:
            for k in m.get('DiagnoseInfo'):
                temp_model = ListDiagnoseInfoForSingleCardResponseBodyDiagnoseInfo()
                self.diagnose_info.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDiagnoseInfoForSingleCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDiagnoseInfoForSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDiagnoseInfoForSingleCardResponse, self).to_map()
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
            temp_model = ListDiagnoseInfoForSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupAuthorizationRulesRequest(TeaModel):
    def __init__(self, authorization_rule_ids=None, authorization_rule_name=None, authorization_rule_status=None,
                 destination=None, destination_type=None, io_tcloud_connector_group_id=None, max_results=None, next_token=None,
                 policy=None, region_id=None):
        self.authorization_rule_ids = authorization_rule_ids  # type: list[str]
        self.authorization_rule_name = authorization_rule_name  # type: list[str]
        self.authorization_rule_status = authorization_rule_status  # type: list[str]
        self.destination = destination  # type: list[str]
        self.destination_type = destination_type  # type: list[str]
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.policy = policy  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupAuthorizationRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_ids is not None:
            result['AuthorizationRuleIds'] = self.authorization_rule_ids
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleIds') is not None:
            self.authorization_rule_ids = m.get('AuthorizationRuleIds')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListGroupAuthorizationRulesResponseBodyGroupAuthorizationRules(TeaModel):
    def __init__(self, authorization_rule_description=None, authorization_rule_id=None,
                 authorization_rule_name=None, authorization_rule_status=None, destination=None, destination_type=None,
                 io_tcloud_connector_group_id=None, policy=None, source_cidrs=None):
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.authorization_rule_status = authorization_rule_status  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.policy = policy  # type: str
        self.source_cidrs = source_cidrs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupAuthorizationRulesResponseBodyGroupAuthorizationRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class ListGroupAuthorizationRulesResponseBody(TeaModel):
    def __init__(self, group_authorization_rules=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.group_authorization_rules = group_authorization_rules  # type: list[ListGroupAuthorizationRulesResponseBodyGroupAuthorizationRules]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.group_authorization_rules:
            for k in self.group_authorization_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupAuthorizationRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GroupAuthorizationRules'] = []
        if self.group_authorization_rules is not None:
            for k in self.group_authorization_rules:
                result['GroupAuthorizationRules'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.group_authorization_rules = []
        if m.get('GroupAuthorizationRules') is not None:
            for k in m.get('GroupAuthorizationRules'):
                temp_model = ListGroupAuthorizationRulesResponseBodyGroupAuthorizationRules()
                self.group_authorization_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGroupAuthorizationRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGroupAuthorizationRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupAuthorizationRulesResponse, self).to_map()
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
            temp_model = ListGroupAuthorizationRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupDNSServiceRulesRequest(TeaModel):
    def __init__(self, dnsservice_rule_ids=None, dnsservice_rule_name=None, dnsservice_rule_status=None,
                 destination=None, io_tcloud_connector_group_id=None, max_results=None, next_token=None, region_id=None,
                 service_type=None, source=None):
        self.dnsservice_rule_ids = dnsservice_rule_ids  # type: list[str]
        self.dnsservice_rule_name = dnsservice_rule_name  # type: list[str]
        self.dnsservice_rule_status = dnsservice_rule_status  # type: list[str]
        self.destination = destination  # type: list[str]
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupDNSServiceRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_ids is not None:
            result['DNSServiceRuleIds'] = self.dnsservice_rule_ids
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.dnsservice_rule_status is not None:
            result['DNSServiceRuleStatus'] = self.dnsservice_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DNSServiceRuleIds') is not None:
            self.dnsservice_rule_ids = m.get('DNSServiceRuleIds')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('DNSServiceRuleStatus') is not None:
            self.dnsservice_rule_status = m.get('DNSServiceRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListGroupDNSServiceRulesResponseBodyDNSServiceRules(TeaModel):
    def __init__(self, dnsservice_rule_description=None, dnsservice_rule_id=None, dnsservice_rule_name=None,
                 dnsservice_rule_status=None, destination=None, io_tcloud_connector_group_id=None, service_type=None, source=None):
        self.dnsservice_rule_description = dnsservice_rule_description  # type: str
        self.dnsservice_rule_id = dnsservice_rule_id  # type: str
        self.dnsservice_rule_name = dnsservice_rule_name  # type: str
        self.dnsservice_rule_status = dnsservice_rule_status  # type: str
        self.destination = destination  # type: str
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupDNSServiceRulesResponseBodyDNSServiceRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnsservice_rule_description is not None:
            result['DNSServiceRuleDescription'] = self.dnsservice_rule_description
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.dnsservice_rule_status is not None:
            result['DNSServiceRuleStatus'] = self.dnsservice_rule_status
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DNSServiceRuleDescription') is not None:
            self.dnsservice_rule_description = m.get('DNSServiceRuleDescription')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('DNSServiceRuleStatus') is not None:
            self.dnsservice_rule_status = m.get('DNSServiceRuleStatus')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListGroupDNSServiceRulesResponseBody(TeaModel):
    def __init__(self, dnsservice_rules=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.dnsservice_rules = dnsservice_rules  # type: list[ListGroupDNSServiceRulesResponseBodyDNSServiceRules]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.dnsservice_rules:
            for k in self.dnsservice_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupDNSServiceRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DNSServiceRules'] = []
        if self.dnsservice_rules is not None:
            for k in self.dnsservice_rules:
                result['DNSServiceRules'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dnsservice_rules = []
        if m.get('DNSServiceRules') is not None:
            for k in m.get('DNSServiceRules'):
                temp_model = ListGroupDNSServiceRulesResponseBodyDNSServiceRules()
                self.dnsservice_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGroupDNSServiceRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGroupDNSServiceRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupDNSServiceRulesResponse, self).to_map()
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
            temp_model = ListGroupDNSServiceRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorAvailableZonesRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorAvailableZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIoTCloudConnectorAvailableZonesResponseBody(TeaModel):
    def __init__(self, available_zone_list=None, io_tcloud_connector_id=None, request_id=None):
        self.available_zone_list = available_zone_list  # type: list[str]
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorAvailableZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zone_list is not None:
            result['AvailableZoneList'] = self.available_zone_list
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableZoneList') is not None:
            self.available_zone_list = m.get('AvailableZoneList')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListIoTCloudConnectorAvailableZonesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIoTCloudConnectorAvailableZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorAvailableZonesResponse, self).to_map()
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
            temp_model = ListIoTCloudConnectorAvailableZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorGroupsRequest(TeaModel):
    def __init__(self, io_tcloud_connector_group_ids=None, io_tcloud_connector_group_name=None,
                 io_tcloud_connector_group_status=None, max_results=None, next_token=None, region_id=None):
        self.io_tcloud_connector_group_ids = io_tcloud_connector_group_ids  # type: list[str]
        self.io_tcloud_connector_group_name = io_tcloud_connector_group_name  # type: list[str]
        self.io_tcloud_connector_group_status = io_tcloud_connector_group_status  # type: list[str]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_group_ids is not None:
            result['IoTCloudConnectorGroupIds'] = self.io_tcloud_connector_group_ids
        if self.io_tcloud_connector_group_name is not None:
            result['IoTCloudConnectorGroupName'] = self.io_tcloud_connector_group_name
        if self.io_tcloud_connector_group_status is not None:
            result['IoTCloudConnectorGroupStatus'] = self.io_tcloud_connector_group_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorGroupIds') is not None:
            self.io_tcloud_connector_group_ids = m.get('IoTCloudConnectorGroupIds')
        if m.get('IoTCloudConnectorGroupName') is not None:
            self.io_tcloud_connector_group_name = m.get('IoTCloudConnectorGroupName')
        if m.get('IoTCloudConnectorGroupStatus') is not None:
            self.io_tcloud_connector_group_status = m.get('IoTCloudConnectorGroupStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroupsIoTCloudConnectors(TeaModel):
    def __init__(self, apn=None, create_time=None, isp=None, io_tcloud_connector_description=None,
                 io_tcloud_connector_id=None, io_tcloud_connector_name=None, io_tcloud_connector_status=None):
        self.apn = apn  # type: str
        self.create_time = create_time  # type: long
        self.isp = isp  # type: str
        self.io_tcloud_connector_description = io_tcloud_connector_description  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.io_tcloud_connector_name = io_tcloud_connector_name  # type: str
        self.io_tcloud_connector_status = io_tcloud_connector_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroupsIoTCloudConnectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_status is not None:
            result['IoTCloudConnectorStatus'] = self.io_tcloud_connector_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorStatus') is not None:
            self.io_tcloud_connector_status = m.get('IoTCloudConnectorStatus')
        return self


class ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroups(TeaModel):
    def __init__(self, create_time=None, description=None, io_tcloud_connector_group_id=None,
                 io_tcloud_connector_group_status=None, io_tcloud_connectors=None, name=None):
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.io_tcloud_connector_group_status = io_tcloud_connector_group_status  # type: str
        self.io_tcloud_connectors = io_tcloud_connectors  # type: list[ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroupsIoTCloudConnectors]
        self.name = name  # type: str

    def validate(self):
        if self.io_tcloud_connectors:
            for k in self.io_tcloud_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.io_tcloud_connector_group_status is not None:
            result['IoTCloudConnectorGroupStatus'] = self.io_tcloud_connector_group_status
        result['IoTCloudConnectors'] = []
        if self.io_tcloud_connectors is not None:
            for k in self.io_tcloud_connectors:
                result['IoTCloudConnectors'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('IoTCloudConnectorGroupStatus') is not None:
            self.io_tcloud_connector_group_status = m.get('IoTCloudConnectorGroupStatus')
        self.io_tcloud_connectors = []
        if m.get('IoTCloudConnectors') is not None:
            for k in m.get('IoTCloudConnectors'):
                temp_model = ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroupsIoTCloudConnectors()
                self.io_tcloud_connectors.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListIoTCloudConnectorGroupsResponseBody(TeaModel):
    def __init__(self, io_tcloud_connector_groups=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.io_tcloud_connector_groups = io_tcloud_connector_groups  # type: list[ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroups]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.io_tcloud_connector_groups:
            for k in self.io_tcloud_connector_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IoTCloudConnectorGroups'] = []
        if self.io_tcloud_connector_groups is not None:
            for k in self.io_tcloud_connector_groups:
                result['IoTCloudConnectorGroups'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.io_tcloud_connector_groups = []
        if m.get('IoTCloudConnectorGroups') is not None:
            for k in m.get('IoTCloudConnectorGroups'):
                temp_model = ListIoTCloudConnectorGroupsResponseBodyIoTCloudConnectorGroups()
                self.io_tcloud_connector_groups.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIoTCloudConnectorGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIoTCloudConnectorGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorGroupsResponse, self).to_map()
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
            temp_model = ListIoTCloudConnectorGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorsRequest(TeaModel):
    def __init__(self, apn=None, isp=None, io_tcloud_connector_group_id=None, io_tcloud_connector_ids=None,
                 io_tcloud_connector_name=None, io_tcloud_connector_status=None, is_in_group=None, max_results=None, next_token=None,
                 region_id=None, vpc_id=None):
        self.apn = apn  # type: list[str]
        self.isp = isp  # type: list[str]
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.io_tcloud_connector_ids = io_tcloud_connector_ids  # type: list[str]
        self.io_tcloud_connector_name = io_tcloud_connector_name  # type: list[str]
        self.io_tcloud_connector_status = io_tcloud_connector_status  # type: list[str]
        self.is_in_group = is_in_group  # type: bool
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.io_tcloud_connector_ids is not None:
            result['IoTCloudConnectorIds'] = self.io_tcloud_connector_ids
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_status is not None:
            result['IoTCloudConnectorStatus'] = self.io_tcloud_connector_status
        if self.is_in_group is not None:
            result['IsInGroup'] = self.is_in_group
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('IoTCloudConnectorIds') is not None:
            self.io_tcloud_connector_ids = m.get('IoTCloudConnectorIds')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorStatus') is not None:
            self.io_tcloud_connector_status = m.get('IoTCloudConnectorStatus')
        if m.get('IsInGroup') is not None:
            self.is_in_group = m.get('IsInGroup')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListIoTCloudConnectorsResponseBodyIoTCloudConnectors(TeaModel):
    def __init__(self, apn=None, create_time=None, isp=None, io_tcloud_connector_business_status=None,
                 io_tcloud_connector_description=None, io_tcloud_connector_group_id=None, io_tcloud_connector_id=None,
                 io_tcloud_connector_name=None, io_tcloud_connector_status=None, modify_time=None, rate_limit=None, v_switch_list=None,
                 vpc_id=None, wildcard_domain_enabled=None):
        self.apn = apn  # type: str
        self.create_time = create_time  # type: long
        self.isp = isp  # type: str
        self.io_tcloud_connector_business_status = io_tcloud_connector_business_status  # type: str
        self.io_tcloud_connector_description = io_tcloud_connector_description  # type: str
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.io_tcloud_connector_name = io_tcloud_connector_name  # type: str
        self.io_tcloud_connector_status = io_tcloud_connector_status  # type: str
        self.modify_time = modify_time  # type: long
        self.rate_limit = rate_limit  # type: long
        self.v_switch_list = v_switch_list  # type: list[str]
        self.vpc_id = vpc_id  # type: str
        self.wildcard_domain_enabled = wildcard_domain_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorsResponseBodyIoTCloudConnectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.io_tcloud_connector_business_status is not None:
            result['IoTCloudConnectorBusinessStatus'] = self.io_tcloud_connector_business_status
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_status is not None:
            result['IoTCloudConnectorStatus'] = self.io_tcloud_connector_status
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.rate_limit is not None:
            result['RateLimit'] = self.rate_limit
        if self.v_switch_list is not None:
            result['VSwitchList'] = self.v_switch_list
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('IoTCloudConnectorBusinessStatus') is not None:
            self.io_tcloud_connector_business_status = m.get('IoTCloudConnectorBusinessStatus')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorStatus') is not None:
            self.io_tcloud_connector_status = m.get('IoTCloudConnectorStatus')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RateLimit') is not None:
            self.rate_limit = m.get('RateLimit')
        if m.get('VSwitchList') is not None:
            self.v_switch_list = m.get('VSwitchList')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        return self


class ListIoTCloudConnectorsResponseBody(TeaModel):
    def __init__(self, io_tcloud_connectors=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.io_tcloud_connectors = io_tcloud_connectors  # type: list[ListIoTCloudConnectorsResponseBodyIoTCloudConnectors]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.io_tcloud_connectors:
            for k in self.io_tcloud_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IoTCloudConnectors'] = []
        if self.io_tcloud_connectors is not None:
            for k in self.io_tcloud_connectors:
                result['IoTCloudConnectors'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.io_tcloud_connectors = []
        if m.get('IoTCloudConnectors') is not None:
            for k in m.get('IoTCloudConnectors'):
                temp_model = ListIoTCloudConnectorsResponseBodyIoTCloudConnectors()
                self.io_tcloud_connectors.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIoTCloudConnectorsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIoTCloudConnectorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorsResponse, self).to_map()
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
            temp_model = ListIoTCloudConnectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, region_id=None):
        self.accept_language = accept_language  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
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
        self.regions = regions  # type: list[ListRegionsResponseBodyRegions]
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, max_results=None, next_token=None, region_id=None,
                 resource_statuses=None, service_ids=None, service_names=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_statuses = resource_statuses  # type: list[str]
        self.service_ids = service_ids  # type: list[str]
        self.service_names = service_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_statuses is not None:
            result['ResourceStatuses'] = self.resource_statuses
        if self.service_ids is not None:
            result['ServiceIds'] = self.service_ids
        if self.service_names is not None:
            result['ServiceNames'] = self.service_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceStatuses') is not None:
            self.resource_statuses = m.get('ResourceStatuses')
        if m.get('ServiceIds') is not None:
            self.service_ids = m.get('ServiceIds')
        if m.get('ServiceNames') is not None:
            self.service_names = m.get('ServiceNames')
        return self


class ListServiceResponseBodyServices(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, service_description=None, service_id=None, service_name=None,
                 service_status=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.service_description = service_description  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.service_status = service_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceResponseBodyServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class ListServiceResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, services=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.services = services  # type: list[ListServiceResponseBodyServices]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListServiceResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceResponse, self).to_map()
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
            temp_model = ListServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceEntriesRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, max_results=None, next_token=None, region_id=None,
                 service_entry_ids=None, service_entry_name=None, service_entry_status=None, service_id=None, target=None,
                 target_type=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.service_entry_ids = service_entry_ids  # type: list[str]
        self.service_entry_name = service_entry_name  # type: list[str]
        self.service_entry_status = service_entry_status  # type: list[str]
        self.service_id = service_id  # type: str
        self.target = target  # type: list[str]
        self.target_type = target_type  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_entry_ids is not None:
            result['ServiceEntryIds'] = self.service_entry_ids
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_entry_status is not None:
            result['ServiceEntryStatus'] = self.service_entry_status
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceEntryIds') is not None:
            self.service_entry_ids = m.get('ServiceEntryIds')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceEntryStatus') is not None:
            self.service_entry_status = m.get('ServiceEntryStatus')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListServiceEntriesResponseBodyServiceEntries(TeaModel):
    def __init__(self, service_entry_description=None, service_entry_id=None, service_entry_name=None,
                 service_entry_status=None, service_id=None, target=None, target_type=None):
        self.service_entry_description = service_entry_description  # type: str
        self.service_entry_id = service_entry_id  # type: str
        self.service_entry_name = service_entry_name  # type: str
        self.service_entry_status = service_entry_status  # type: str
        self.service_id = service_id  # type: str
        self.target = target  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceEntriesResponseBodyServiceEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_entry_status is not None:
            result['ServiceEntryStatus'] = self.service_entry_status
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceEntryStatus') is not None:
            self.service_entry_status = m.get('ServiceEntryStatus')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListServiceEntriesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, service_entries=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.service_entries = service_entries  # type: list[ListServiceEntriesResponseBodyServiceEntries]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.service_entries:
            for k in self.service_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceEntries'] = []
        if self.service_entries is not None:
            for k in self.service_entries:
                result['ServiceEntries'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_entries = []
        if m.get('ServiceEntries') is not None:
            for k in m.get('ServiceEntries'):
                temp_model = ListServiceEntriesResponseBodyServiceEntries()
                self.service_entries.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceEntriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceEntriesResponse, self).to_map()
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
            temp_model = ListServiceEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveAuthorizationRuleToDNSServiceRequest(TeaModel):
    def __init__(self, authorization_rule_id=None, client_token=None, dry_run=None, io_tcloud_connector_id=None,
                 region_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveAuthorizationRuleToDNSServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveAuthorizationRuleToDNSServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveAuthorizationRuleToDNSServiceResponseBody, self).to_map()
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


class MoveAuthorizationRuleToDNSServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MoveAuthorizationRuleToDNSServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveAuthorizationRuleToDNSServiceResponse, self).to_map()
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
            temp_model = MoveAuthorizationRuleToDNSServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveGroupAuthorizationRuleToDNSServiceRequest(TeaModel):
    def __init__(self, authorization_rule_id=None, client_token=None, dry_run=None,
                 io_tcloud_connector_group_id=None, region_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveGroupAuthorizationRuleToDNSServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveGroupAuthorizationRuleToDNSServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveGroupAuthorizationRuleToDNSServiceResponseBody, self).to_map()
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


class MoveGroupAuthorizationRuleToDNSServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MoveGroupAuthorizationRuleToDNSServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveGroupAuthorizationRuleToDNSServiceResponse, self).to_map()
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
            temp_model = MoveGroupAuthorizationRuleToDNSServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenIoTCloudConnectorServiceRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenIoTCloudConnectorServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenIoTCloudConnectorServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenIoTCloudConnectorServiceResponseBody, self).to_map()
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


class OpenIoTCloudConnectorServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenIoTCloudConnectorServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenIoTCloudConnectorServiceResponse, self).to_map()
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
            temp_model = OpenIoTCloudConnectorServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveIoTCloudConnectorFromGroupRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_group_id=None,
                 io_tcloud_connector_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveIoTCloudConnectorFromGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveIoTCloudConnectorFromGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveIoTCloudConnectorFromGroupResponseBody, self).to_map()
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


class RemoveIoTCloudConnectorFromGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveIoTCloudConnectorFromGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveIoTCloudConnectorFromGroupResponse, self).to_map()
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
            temp_model = RemoveIoTCloudConnectorFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDiagnoseTaskForSingleCardRequest(TeaModel):
    def __init__(self, begin_time=None, destination=None, destination_type=None, end_time=None,
                 io_tcloud_connector_id=None, region_id=None, resource_uid=None, source=None, source_type=None):
        self.begin_time = begin_time  # type: long
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.end_time = end_time  # type: long
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_uid = resource_uid  # type: long
        self.source = source  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDiagnoseTaskForSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SubmitDiagnoseTaskForSingleCardResponseBody(TeaModel):
    def __init__(self, diagnose_task_id=None, request_id=None):
        self.diagnose_task_id = diagnose_task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDiagnoseTaskForSingleCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnose_task_id is not None:
            result['DiagnoseTaskId'] = self.diagnose_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiagnoseTaskId') is not None:
            self.diagnose_task_id = m.get('DiagnoseTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitDiagnoseTaskForSingleCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitDiagnoseTaskForSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitDiagnoseTaskForSingleCardResponse, self).to_map()
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
            temp_model = SubmitDiagnoseTaskForSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthorizationRuleAttributeRequest(TeaModel):
    def __init__(self, authorization_rule_description=None, authorization_rule_id=None,
                 authorization_rule_name=None, client_token=None, destination=None, destination_type=None, dry_run=None,
                 io_tcloud_connector_id=None, policy=None, region_id=None, source_cidrs=None):
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.client_token = client_token  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.policy = policy  # type: str
        self.region_id = region_id  # type: str
        self.source_cidrs = source_cidrs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuthorizationRuleAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class UpdateAuthorizationRuleAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuthorizationRuleAttributeResponseBody, self).to_map()
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


class UpdateAuthorizationRuleAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAuthorizationRuleAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAuthorizationRuleAttributeResponse, self).to_map()
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
            temp_model = UpdateAuthorizationRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnectionPoolAttributeRequest(TeaModel):
    def __init__(self, cidrs=None, client_token=None, connection_pool_description=None, connection_pool_id=None,
                 connection_pool_name=None, count=None, dry_run=None, io_tcloud_connector_id=None, region_id=None):
        self.cidrs = cidrs  # type: list[str]
        self.client_token = client_token  # type: str
        self.connection_pool_description = connection_pool_description  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.connection_pool_name = connection_pool_name  # type: str
        self.count = count  # type: long
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionPoolAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.count is not None:
            result['Count'] = self.count
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateConnectionPoolAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionPoolAttributeResponseBody, self).to_map()
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


class UpdateConnectionPoolAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateConnectionPoolAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConnectionPoolAttributeResponse, self).to_map()
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
            temp_model = UpdateConnectionPoolAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDNSServiceRuleAttributeRequest(TeaModel):
    def __init__(self, authorization_rule_description=None, authorization_rule_name=None, client_token=None,
                 dnsservice_rule_id=None, destination=None, dry_run=None, io_tcloud_connector_id=None, region_id=None,
                 service_type=None, source=None):
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.client_token = client_token  # type: str
        self.dnsservice_rule_id = dnsservice_rule_id  # type: str
        self.destination = destination  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDNSServiceRuleAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateDNSServiceRuleAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDNSServiceRuleAttributeResponseBody, self).to_map()
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


class UpdateDNSServiceRuleAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDNSServiceRuleAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDNSServiceRuleAttributeResponse, self).to_map()
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
            temp_model = UpdateDNSServiceRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupAuthorizationRuleAttributeRequest(TeaModel):
    def __init__(self, authorization_rule_description=None, authorization_rule_id=None,
                 authorization_rule_name=None, client_token=None, destination=None, destination_type=None, dry_run=None,
                 io_tcloud_connector_group_id=None, policy=None, region_id=None, source_cidrs=None):
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.client_token = client_token  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.policy = policy  # type: str
        self.region_id = region_id  # type: str
        self.source_cidrs = source_cidrs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupAuthorizationRuleAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        return self


class UpdateGroupAuthorizationRuleAttributeResponseBody(TeaModel):
    def __init__(self, authorization_rule_id=None, io_tcloud_connector_group_id=None, request_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupAuthorizationRuleAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGroupAuthorizationRuleAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGroupAuthorizationRuleAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupAuthorizationRuleAttributeResponse, self).to_map()
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
            temp_model = UpdateGroupAuthorizationRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupDNSServiceRuleAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dnsservice_rule_description=None, dnsservice_rule_id=None,
                 dnsservice_rule_name=None, destination=None, dry_run=None, io_tcloud_connector_group_id=None, region_id=None,
                 service_type=None, source=None):
        self.client_token = client_token  # type: str
        self.dnsservice_rule_description = dnsservice_rule_description  # type: str
        self.dnsservice_rule_id = dnsservice_rule_id  # type: str
        self.dnsservice_rule_name = dnsservice_rule_name  # type: str
        self.destination = destination  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.region_id = region_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupDNSServiceRuleAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dnsservice_rule_description is not None:
            result['DNSServiceRuleDescription'] = self.dnsservice_rule_description
        if self.dnsservice_rule_id is not None:
            result['DNSServiceRuleId'] = self.dnsservice_rule_id
        if self.dnsservice_rule_name is not None:
            result['DNSServiceRuleName'] = self.dnsservice_rule_name
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DNSServiceRuleDescription') is not None:
            self.dnsservice_rule_description = m.get('DNSServiceRuleDescription')
        if m.get('DNSServiceRuleId') is not None:
            self.dnsservice_rule_id = m.get('DNSServiceRuleId')
        if m.get('DNSServiceRuleName') is not None:
            self.dnsservice_rule_name = m.get('DNSServiceRuleName')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class UpdateGroupDNSServiceRuleAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupDNSServiceRuleAttributeResponseBody, self).to_map()
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


class UpdateGroupDNSServiceRuleAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGroupDNSServiceRuleAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupDNSServiceRuleAttributeResponse, self).to_map()
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
            temp_model = UpdateGroupDNSServiceRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIoTCloudConnectorAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_description=None,
                 io_tcloud_connector_id=None, io_tcloud_connector_name=None, region_id=None, wildcard_domain_enabled=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_description = io_tcloud_connector_description  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.io_tcloud_connector_name = io_tcloud_connector_name  # type: str
        self.region_id = region_id  # type: str
        self.wildcard_domain_enabled = wildcard_domain_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIoTCloudConnectorAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        return self


class UpdateIoTCloudConnectorAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_id=None):
        self.request_id = request_id  # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIoTCloudConnectorAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class UpdateIoTCloudConnectorAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateIoTCloudConnectorAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIoTCloudConnectorAttributeResponse, self).to_map()
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
            temp_model = UpdateIoTCloudConnectorAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIoTCloudConnectorGroupAttributeRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, io_tcloud_connector_group_id=None,
                 name=None, region_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_group_id = io_tcloud_connector_group_id  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIoTCloudConnectorGroupAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_group_id is not None:
            result['IoTCloudConnectorGroupId'] = self.io_tcloud_connector_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorGroupId') is not None:
            self.io_tcloud_connector_group_id = m.get('IoTCloudConnectorGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateIoTCloudConnectorGroupAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIoTCloudConnectorGroupAttributeResponseBody, self).to_map()
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


class UpdateIoTCloudConnectorGroupAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateIoTCloudConnectorGroupAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIoTCloudConnectorGroupAttributeResponse, self).to_map()
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
            temp_model = UpdateIoTCloudConnectorGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None,
                 service_description=None, service_id=None, service_name=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str
        self.service_description = service_description  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class UpdateServiceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceAttributeResponseBody, self).to_map()
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


class UpdateServiceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceAttributeResponse, self).to_map()
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
            temp_model = UpdateServiceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceEntryAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, io_tcloud_connector_id=None, region_id=None,
                 service_entry_description=None, service_entry_id=None, service_entry_name=None, service_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.region_id = region_id  # type: str
        self.service_entry_description = service_entry_description  # type: str
        self.service_entry_id = service_entry_id  # type: str
        self.service_entry_name = service_entry_name  # type: str
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceEntryAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class UpdateServiceEntryAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceEntryAttributeResponseBody, self).to_map()
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


class UpdateServiceEntryAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceEntryAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceEntryAttributeResponse, self).to_map()
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
            temp_model = UpdateServiceEntryAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


