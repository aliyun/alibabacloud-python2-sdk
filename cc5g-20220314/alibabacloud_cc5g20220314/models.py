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


