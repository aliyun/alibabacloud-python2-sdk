# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddDNSAuthorizationRuleRequest(TeaModel):
    def __init__(self, client_token=None, description=None, destination_ip=None, dry_run=None, name=None,
                 source_dnsip=None, wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.destination_ip = destination_ip  # type: str
        self.dry_run = dry_run  # type: bool
        self.name = name  # type: str
        self.source_dnsip = source_dnsip  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDNSAuthorizationRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.source_dnsip is not None:
            result['SourceDNSIp'] = self.source_dnsip
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceDNSIp') is not None:
            self.source_dnsip = m.get('SourceDNSIp')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class AddDNSAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, authorization_rule_id=None, request_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDNSAuthorizationRuleResponseBody, self).to_map()
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


class AddDNSAuthorizationRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddDNSAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDNSAuthorizationRuleResponse, self).to_map()
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
            temp_model = AddDNSAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachVpcToNetLinkRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, net_link_id=None, region_id=None, v_switches=None,
                 vpc_id=None, wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.net_link_id = net_link_id  # type: str
        self.region_id = region_id  # type: str
        self.v_switches = v_switches  # type: list[str]
        self.vpc_id = vpc_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachVpcToNetLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.net_link_id is not None:
            result['NetLinkId'] = self.net_link_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('NetLinkId') is not None:
            self.net_link_id = m.get('NetLinkId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class AttachVpcToNetLinkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachVpcToNetLinkResponseBody, self).to_map()
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


class AttachVpcToNetLinkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachVpcToNetLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachVpcToNetLinkResponse, self).to_map()
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
            temp_model = AttachVpcToNetLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthorizationRuleRequest(TeaModel):
    def __init__(self, client_token=None, description=None, destination=None, destination_type=None, dry_run=None,
                 name=None, policy=None, source_cidr=None, wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.dry_run = dry_run  # type: bool
        self.name = name  # type: str
        self.policy = policy  # type: str
        self.source_cidr = source_cidr  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthorizationRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class CreateAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, authorization_rule_id=None, request_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        # Id of the request
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


class CreateWirelessCloudConnectorRequestNetLinks(TeaModel):
    def __init__(self, apn=None, region_id=None, v_switchs=None, vpc_id=None):
        self.apn = apn  # type: str
        self.region_id = region_id  # type: str
        self.v_switchs = v_switchs  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWirelessCloudConnectorRequestNetLinks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switchs is not None:
            result['VSwitchs'] = self.v_switchs
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchs') is not None:
            self.v_switchs = m.get('VSwitchs')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateWirelessCloudConnectorRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, isp=None, name=None, net_links=None,
                 region_id=None, use_case=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.isp = isp  # type: str
        self.name = name  # type: str
        self.net_links = net_links  # type: list[CreateWirelessCloudConnectorRequestNetLinks]
        self.region_id = region_id  # type: str
        self.use_case = use_case  # type: str

    def validate(self):
        if self.net_links:
            for k in self.net_links:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateWirelessCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        result['NetLinks'] = []
        if self.net_links is not None:
            for k in self.net_links:
                result['NetLinks'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.use_case is not None:
            result['UseCase'] = self.use_case
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.net_links = []
        if m.get('NetLinks') is not None:
            for k in m.get('NetLinks'):
                temp_model = CreateWirelessCloudConnectorRequestNetLinks()
                self.net_links.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UseCase') is not None:
            self.use_case = m.get('UseCase')
        return self


class CreateWirelessCloudConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None, wireless_cloud_connector_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWirelessCloudConnectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class CreateWirelessCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateWirelessCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWirelessCloudConnectorResponse, self).to_map()
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
            temp_model = CreateWirelessCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthorizationRuleRequest(TeaModel):
    def __init__(self, authorization_rule_id=None, client_token=None, dry_run=None,
                 wireless_cloud_connector_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

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
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class DeleteAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
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


class DeleteWirelessCloudConnectorRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWirelessCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class DeleteWirelessCloudConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWirelessCloudConnectorResponseBody, self).to_map()
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


class DeleteWirelessCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteWirelessCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWirelessCloudConnectorResponse, self).to_map()
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
            temp_model = DeleteWirelessCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachVpcFromNetLinkRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, net_link_id=None, wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.net_link_id = net_link_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachVpcFromNetLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.net_link_id is not None:
            result['NetLinkId'] = self.net_link_id
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('NetLinkId') is not None:
            self.net_link_id = m.get('NetLinkId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class DetachVpcFromNetLinkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachVpcFromNetLinkResponseBody, self).to_map()
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


class DetachVpcFromNetLinkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachVpcFromNetLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachVpcFromNetLinkResponse, self).to_map()
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
            temp_model = DetachVpcFromNetLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWirelessCloudConnectorRequest(TeaModel):
    def __init__(self, region_id=None, wireless_cloud_connector_id=None):
        self.region_id = region_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWirelessCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class GetWirelessCloudConnectorResponseBodyNetLinks(TeaModel):
    def __init__(self, apn=None, create_time=None, description=None, isp=None, name=None, net_link_id=None,
                 region_id=None, status=None, v_switchs=None, vpc_id=None):
        self.apn = apn  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.isp = isp  # type: str
        # 创建时间
        self.name = name  # type: str
        # 资源名称
        self.net_link_id = net_link_id  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.v_switchs = v_switchs  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWirelessCloudConnectorResponseBodyNetLinks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.net_link_id is not None:
            result['NetLinkId'] = self.net_link_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switchs is not None:
            result['VSwitchs'] = self.v_switchs
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetLinkId') is not None:
            self.net_link_id = m.get('NetLinkId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchs') is not None:
            self.v_switchs = m.get('VSwitchs')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetWirelessCloudConnectorResponseBody(TeaModel):
    def __init__(self, card_count=None, create_time=None, data_package_id=None, data_package_type=None,
                 description=None, name=None, net_links=None, region_id=None, request_id=None, status=None, use_case=None,
                 wireless_cloud_connector_id=None):
        self.card_count = card_count  # type: str
        self.create_time = create_time  # type: str
        self.data_package_id = data_package_id  # type: str
        self.data_package_type = data_package_type  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        # 数组，返回示例目录。
        self.net_links = net_links  # type: list[GetWirelessCloudConnectorResponseBodyNetLinks]
        self.region_id = region_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.use_case = use_case  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        if self.net_links:
            for k in self.net_links:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetWirelessCloudConnectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_count is not None:
            result['CardCount'] = self.card_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_package_id is not None:
            result['DataPackageId'] = self.data_package_id
        if self.data_package_type is not None:
            result['DataPackageType'] = self.data_package_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['NetLinks'] = []
        if self.net_links is not None:
            for k in self.net_links:
                result['NetLinks'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.use_case is not None:
            result['UseCase'] = self.use_case
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardCount') is not None:
            self.card_count = m.get('CardCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataPackageId') is not None:
            self.data_package_id = m.get('DataPackageId')
        if m.get('DataPackageType') is not None:
            self.data_package_type = m.get('DataPackageType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.net_links = []
        if m.get('NetLinks') is not None:
            for k in m.get('NetLinks'):
                temp_model = GetWirelessCloudConnectorResponseBodyNetLinks()
                self.net_links.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UseCase') is not None:
            self.use_case = m.get('UseCase')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class GetWirelessCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetWirelessCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWirelessCloudConnectorResponse, self).to_map()
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
            temp_model = GetWirelessCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizationRulesRequest(TeaModel):
    def __init__(self, authorization_rule_ids=None, destination=None, destination_type=None, dns=None,
                 max_results=None, names=None, next_token=None, policy=None, statuses=None, type=None,
                 wireless_cloud_connector_id=None):
        self.authorization_rule_ids = authorization_rule_ids  # type: list[str]
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.dns = dns  # type: bool
        self.max_results = max_results  # type: long
        self.names = names  # type: list[str]
        self.next_token = next_token  # type: str
        self.policy = policy  # type: str
        self.statuses = statuses  # type: list[str]
        self.type = type  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthorizationRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_ids is not None:
            result['AuthorizationRuleIds'] = self.authorization_rule_ids
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dns is not None:
            result['Dns'] = self.dns
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.names is not None:
            result['Names'] = self.names
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        if self.type is not None:
            result['Type'] = self.type
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleIds') is not None:
            self.authorization_rule_ids = m.get('AuthorizationRuleIds')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Dns') is not None:
            self.dns = m.get('Dns')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListAuthorizationRulesResponseBodyAuthorizationRules(TeaModel):
    def __init__(self, authorization_rule_id=None, create_time=None, description=None, destination=None,
                 destination_type=None, dns=None, name=None, policy=None, source_cidr=None, status=None, type=None):
        # 资源一级ID
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.dns = dns  # type: str
        # 创建时间
        self.name = name  # type: str
        self.policy = policy  # type: str
        self.source_cidr = source_cidr  # type: str
        # 资源名称
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthorizationRulesResponseBodyAuthorizationRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dns is not None:
            result['Dns'] = self.dns
        if self.name is not None:
            result['Name'] = self.name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Dns') is not None:
            self.dns = m.get('Dns')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAuthorizationRulesResponseBody(TeaModel):
    def __init__(self, authorization_rules=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        # 数组，返回示例目录。
        self.authorization_rules = authorization_rules  # type: list[ListAuthorizationRulesResponseBodyAuthorizationRules]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

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


class ListCardsRequest(TeaModel):
    def __init__(self, apn=None, destination_type=None, iccids=None, ip_address=None, lock=None, max_results=None,
                 net_link_id=None, next_token=None, online=None, statuses=None, vpc_id=None, wireless_cloud_connector_id=None):
        self.apn = apn  # type: str
        self.destination_type = destination_type  # type: str
        self.iccids = iccids  # type: list[str]
        self.ip_address = ip_address  # type: str
        self.lock = lock  # type: bool
        self.max_results = max_results  # type: long
        self.net_link_id = net_link_id  # type: str
        self.next_token = next_token  # type: str
        self.online = online  # type: bool
        self.statuses = statuses  # type: list[str]
        self.vpc_id = vpc_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.iccids is not None:
            result['Iccids'] = self.iccids
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.lock is not None:
            result['Lock'] = self.lock
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.net_link_id is not None:
            result['NetLinkId'] = self.net_link_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.online is not None:
            result['Online'] = self.online
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Iccids') is not None:
            self.iccids = m.get('Iccids')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Lock') is not None:
            self.lock = m.get('Lock')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NetLinkId') is not None:
            self.net_link_id = m.get('NetLinkId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListCardsResponseBodyCards(TeaModel):
    def __init__(self, apn=None, activated_time=None, description=None, isp=None, iccid=None, imei=None, imsi=None,
                 ip_address=None, lock=None, name=None, net_type=None, order_id=None, spec=None, status=None,
                 usage_data_month=None):
        # 创建时间
        self.apn = apn  # type: str
        self.activated_time = activated_time  # type: str
        self.description = description  # type: str
        self.isp = isp  # type: str
        # 资源一级ID
        self.iccid = iccid  # type: str
        self.imei = imei  # type: str
        self.imsi = imsi  # type: str
        self.ip_address = ip_address  # type: str
        self.lock = lock  # type: bool
        self.name = name  # type: str
        # 资源名称
        self.net_type = net_type  # type: str
        self.order_id = order_id  # type: str
        self.spec = spec  # type: str
        self.status = status  # type: str
        self.usage_data_month = usage_data_month  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCardsResponseBodyCards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.activated_time is not None:
            result['ActivatedTime'] = self.activated_time
        if self.description is not None:
            result['Description'] = self.description
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imei is not None:
            result['Imei'] = self.imei
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.lock is not None:
            result['Lock'] = self.lock
        if self.name is not None:
            result['Name'] = self.name
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        if self.usage_data_month is not None:
            result['UsageDataMonth'] = self.usage_data_month
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('ActivatedTime') is not None:
            self.activated_time = m.get('ActivatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imei') is not None:
            self.imei = m.get('Imei')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Lock') is not None:
            self.lock = m.get('Lock')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UsageDataMonth') is not None:
            self.usage_data_month = m.get('UsageDataMonth')
        return self


class ListCardsResponseBody(TeaModel):
    def __init__(self, cards=None, max_results=None, next_token=None, request_id=None, total_count=None):
        # 数组，返回示例目录。
        self.cards = cards  # type: list[ListCardsResponseBodyCards]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.cards:
            for k in self.cards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCardsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cards'] = []
        if self.cards is not None:
            for k in self.cards:
                result['Cards'].append(k.to_map() if k else None)
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
        self.cards = []
        if m.get('Cards') is not None:
            for k in m.get('Cards'):
                temp_model = ListCardsResponseBodyCards()
                self.cards.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCardsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCardsResponse, self).to_map()
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
            temp_model = ListCardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataPackagesRequest(TeaModel):
    def __init__(self, data_package_ids=None, max_results=None, names=None, next_token=None, statuses=None,
                 wireless_cloud_connector_id=None):
        self.data_package_ids = data_package_ids  # type: list[str]
        self.max_results = max_results  # type: long
        self.names = names  # type: list[str]
        self.next_token = next_token  # type: str
        self.statuses = statuses  # type: list[str]
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataPackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_package_ids is not None:
            result['DataPackageIds'] = self.data_package_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.names is not None:
            result['Names'] = self.names
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataPackageIds') is not None:
            self.data_package_ids = m.get('DataPackageIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListDataPackagesResponseBodyDataPackages(TeaModel):
    def __init__(self, card_count=None, create_time=None, data_package_id=None, expired_time=None, isp=None,
                 name=None, size=None, status=None):
        self.card_count = card_count  # type: str
        self.create_time = create_time  # type: str
        self.data_package_id = data_package_id  # type: str
        self.expired_time = expired_time  # type: str
        self.isp = isp  # type: str
        # 创建时间
        self.name = name  # type: str
        self.size = size  # type: str
        # 资源名称
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataPackagesResponseBodyDataPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_count is not None:
            result['CardCount'] = self.card_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_package_id is not None:
            result['DataPackageId'] = self.data_package_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardCount') is not None:
            self.card_count = m.get('CardCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataPackageId') is not None:
            self.data_package_id = m.get('DataPackageId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDataPackagesResponseBody(TeaModel):
    def __init__(self, data_packages=None, max_results=None, next_token=None, request_id=None, total_count=None):
        # 数组，返回示例目录。
        self.data_packages = data_packages  # type: list[ListDataPackagesResponseBodyDataPackages]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.data_packages:
            for k in self.data_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataPackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataPackages'] = []
        if self.data_packages is not None:
            for k in self.data_packages:
                result['DataPackages'].append(k.to_map() if k else None)
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
        self.data_packages = []
        if m.get('DataPackages') is not None:
            for k in m.get('DataPackages'):
                temp_model = ListDataPackagesResponseBodyDataPackages()
                self.data_packages.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDataPackagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataPackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataPackagesResponse, self).to_map()
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
            temp_model = ListDataPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrdersRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, order_action=None, order_ids=None, statuses=None,
                 wireless_cloud_connector_id=None):
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.order_action = order_action  # type: str
        self.order_ids = order_ids  # type: list[str]
        self.statuses = statuses  # type: list[str]
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrdersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_action is not None:
            result['OrderAction'] = self.order_action
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderAction') is not None:
            self.order_action = m.get('OrderAction')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListOrdersResponseBodyOrders(TeaModel):
    def __init__(self, action=None, card_count=None, card_net_type=None, card_type=None, contact_name=None,
                 contact_phone=None, create_time=None, description=None, logistics_id=None, logistics_status=None,
                 logistics_type=None, logistics_update_time=None, order_id=None, pay_time=None, post_address=None, region_id=None,
                 status=None):
        # 创建时间
        self.action = action  # type: str
        self.card_count = card_count  # type: str
        self.card_net_type = card_net_type  # type: str
        self.card_type = card_type  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_phone = contact_phone  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.logistics_id = logistics_id  # type: str
        self.logistics_status = logistics_status  # type: str
        self.logistics_type = logistics_type  # type: str
        self.logistics_update_time = logistics_update_time  # type: str
        self.order_id = order_id  # type: str
        self.pay_time = pay_time  # type: str
        self.post_address = post_address  # type: str
        self.region_id = region_id  # type: str
        # 资源名称
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrdersResponseBodyOrders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.card_count is not None:
            result['CardCount'] = self.card_count
        if self.card_net_type is not None:
            result['CardNetType'] = self.card_net_type
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone is not None:
            result['ContactPhone'] = self.contact_phone
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.logistics_id is not None:
            result['LogisticsId'] = self.logistics_id
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.logistics_type is not None:
            result['LogisticsType'] = self.logistics_type
        if self.logistics_update_time is not None:
            result['LogisticsUpdateTime'] = self.logistics_update_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pay_time is not None:
            result['PayTime'] = self.pay_time
        if self.post_address is not None:
            result['PostAddress'] = self.post_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('CardCount') is not None:
            self.card_count = m.get('CardCount')
        if m.get('CardNetType') is not None:
            self.card_net_type = m.get('CardNetType')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhone') is not None:
            self.contact_phone = m.get('ContactPhone')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LogisticsId') is not None:
            self.logistics_id = m.get('LogisticsId')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('LogisticsType') is not None:
            self.logistics_type = m.get('LogisticsType')
        if m.get('LogisticsUpdateTime') is not None:
            self.logistics_update_time = m.get('LogisticsUpdateTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')
        if m.get('PostAddress') is not None:
            self.post_address = m.get('PostAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListOrdersResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, orders=None, request_id=None, total_count=None):
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        # 数组，返回示例目录。
        self.orders = orders  # type: list[ListOrdersResponseBodyOrders]
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.orders:
            for k in self.orders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOrdersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Orders'] = []
        if self.orders is not None:
            for k in self.orders:
                result['Orders'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.orders = []
        if m.get('Orders') is not None:
            for k in m.get('Orders'):
                temp_model = ListOrdersResponseBodyOrders()
                self.orders.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOrdersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOrdersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOrdersResponse, self).to_map()
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
            temp_model = ListOrdersResponseBody()
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
        # 资源名称
        self.local_name = local_name  # type: str
        # 创建时间
        self.region_endpoint = region_endpoint  # type: str
        # 资源一级ID
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
        # 数组，返回示例目录。
        self.regions = regions  # type: list[ListRegionsResponseBodyRegions]
        # Id of the request
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


class ListWirelessCloudConnectorsRequest(TeaModel):
    def __init__(self, max_results=None, names=None, next_token=None, region_id=None, statuses=None,
                 wireless_cloud_connector_ids=None):
        self.max_results = max_results  # type: long
        self.names = names  # type: list[str]
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.statuses = statuses  # type: list[str]
        self.wireless_cloud_connector_ids = wireless_cloud_connector_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWirelessCloudConnectorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.names is not None:
            result['Names'] = self.names
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        if self.wireless_cloud_connector_ids is not None:
            result['WirelessCloudConnectorIds'] = self.wireless_cloud_connector_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        if m.get('WirelessCloudConnectorIds') is not None:
            self.wireless_cloud_connector_ids = m.get('WirelessCloudConnectorIds')
        return self


class ListWirelessCloudConnectorsResponseBodyWirelessCloudConnectors(TeaModel):
    def __init__(self, card_count=None, create_time=None, data_package_id=None, data_package_type=None,
                 description=None, name=None, region_id=None, status=None, use_case=None, wireless_cloud_connector_id=None):
        self.card_count = card_count  # type: str
        self.create_time = create_time  # type: str
        self.data_package_id = data_package_id  # type: str
        self.data_package_type = data_package_type  # type: str
        self.description = description  # type: str
        # 创建时间
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        # 资源名称
        self.status = status  # type: str
        self.use_case = use_case  # type: str
        # 资源一级ID
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWirelessCloudConnectorsResponseBodyWirelessCloudConnectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_count is not None:
            result['CardCount'] = self.card_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_package_id is not None:
            result['DataPackageId'] = self.data_package_id
        if self.data_package_type is not None:
            result['DataPackageType'] = self.data_package_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.use_case is not None:
            result['UseCase'] = self.use_case
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardCount') is not None:
            self.card_count = m.get('CardCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataPackageId') is not None:
            self.data_package_id = m.get('DataPackageId')
        if m.get('DataPackageType') is not None:
            self.data_package_type = m.get('DataPackageType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UseCase') is not None:
            self.use_case = m.get('UseCase')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListWirelessCloudConnectorsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 wireless_cloud_connectors=None):
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str
        # 数组，返回示例目录。
        self.wireless_cloud_connectors = wireless_cloud_connectors  # type: list[ListWirelessCloudConnectorsResponseBodyWirelessCloudConnectors]

    def validate(self):
        if self.wireless_cloud_connectors:
            for k in self.wireless_cloud_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWirelessCloudConnectorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WirelessCloudConnectors'] = []
        if self.wireless_cloud_connectors is not None:
            for k in self.wireless_cloud_connectors:
                result['WirelessCloudConnectors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.wireless_cloud_connectors = []
        if m.get('WirelessCloudConnectors') is not None:
            for k in m.get('WirelessCloudConnectors'):
                temp_model = ListWirelessCloudConnectorsResponseBodyWirelessCloudConnectors()
                self.wireless_cloud_connectors.append(temp_model.from_map(k))
        return self


class ListWirelessCloudConnectorsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListWirelessCloudConnectorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWirelessCloudConnectorsResponse, self).to_map()
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
            temp_model = ListWirelessCloudConnectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZonesRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListZonesRequest, self).to_map()
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


class ListZonesResponseBodyZones(TeaModel):
    def __init__(self, local_name=None, zone_id=None):
        # 创建时间
        self.local_name = local_name  # type: str
        # 资源名称
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListZonesResponseBodyZones, self).to_map()
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


class ListZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, zones=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 数组，返回示例目录。
        self.zones = zones  # type: list[ListZonesResponseBodyZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListZonesResponseBody, self).to_map()
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
                temp_model = ListZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class ListZonesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListZonesResponse, self).to_map()
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
            temp_model = ListZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenCc5gServiceRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenCc5gServiceRequest, self).to_map()
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


class OpenCc5gServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenCc5gServiceResponseBody, self).to_map()
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


class OpenCc5gServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenCc5gServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenCc5gServiceResponse, self).to_map()
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
            temp_model = OpenCc5gServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthorizationRuleRequest(TeaModel):
    def __init__(self, authorization_rule_id=None, client_token=None, description=None, destination=None,
                 dry_run=None, name=None, policy=None, source_cidr=None, wireless_cloud_connector_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.destination = destination  # type: str
        self.dry_run = dry_run  # type: bool
        self.name = name  # type: str
        self.policy = policy  # type: str
        self.source_cidr = source_cidr  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuthorizationRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class UpdateAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuthorizationRuleResponseBody, self).to_map()
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


class UpdateAuthorizationRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAuthorizationRuleResponse, self).to_map()
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
            temp_model = UpdateAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCardRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, iccid=None, name=None,
                 wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.iccid = iccid  # type: str
        self.name = name  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.name is not None:
            result['Name'] = self.name
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class UpdateCardResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCardResponseBody, self).to_map()
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


class UpdateCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCardResponse, self).to_map()
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
            temp_model = UpdateCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDNSAuthorizationRuleRequest(TeaModel):
    def __init__(self, authorization_rule_id=None, client_token=None, description=None, destination_ip=None,
                 dry_run=None, name=None, source_dnsip=None, wireless_cloud_connector_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.destination_ip = destination_ip  # type: str
        self.dry_run = dry_run  # type: bool
        self.name = name  # type: str
        self.source_dnsip = source_dnsip  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDNSAuthorizationRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.source_dnsip is not None:
            result['SourceDNSIp'] = self.source_dnsip
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceDNSIp') is not None:
            self.source_dnsip = m.get('SourceDNSIp')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class UpdateDNSAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDNSAuthorizationRuleResponseBody, self).to_map()
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


class UpdateDNSAuthorizationRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDNSAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDNSAuthorizationRuleResponse, self).to_map()
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
            temp_model = UpdateDNSAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWirelessCloudConnectorRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, name=None,
                 wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.name = name  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWirelessCloudConnectorRequest, self).to_map()
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
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
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
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class UpdateWirelessCloudConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWirelessCloudConnectorResponseBody, self).to_map()
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


class UpdateWirelessCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateWirelessCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWirelessCloudConnectorResponse, self).to_map()
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
            temp_model = UpdateWirelessCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


