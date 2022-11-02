# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ActiveFlowLogRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, flow_log_id=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.flow_log_id = flow_log_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActiveFlowLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ActiveFlowLogResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActiveFlowLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActiveFlowLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ActiveFlowLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ActiveFlowLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ActiveFlowLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTrafficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules(TeaModel):
    def __init__(self, dst_cidr=None, dst_port_range=None, match_dscp=None, protocol=None, src_cidr=None,
                 src_port_range=None, traffic_match_rule_description=None, traffic_match_rule_name=None):
        self.dst_cidr = dst_cidr  # type: str
        self.dst_port_range = dst_port_range  # type: list[int]
        self.match_dscp = match_dscp  # type: int
        self.protocol = protocol  # type: str
        self.src_cidr = src_cidr  # type: str
        self.src_port_range = src_port_range  # type: list[int]
        self.traffic_match_rule_description = traffic_match_rule_description  # type: str
        self.traffic_match_rule_name = traffic_match_rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTrafficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_cidr is not None:
            result['DstCidr'] = self.dst_cidr
        if self.dst_port_range is not None:
            result['DstPortRange'] = self.dst_port_range
        if self.match_dscp is not None:
            result['MatchDscp'] = self.match_dscp
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.src_cidr is not None:
            result['SrcCidr'] = self.src_cidr
        if self.src_port_range is not None:
            result['SrcPortRange'] = self.src_port_range
        if self.traffic_match_rule_description is not None:
            result['TrafficMatchRuleDescription'] = self.traffic_match_rule_description
        if self.traffic_match_rule_name is not None:
            result['TrafficMatchRuleName'] = self.traffic_match_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DstCidr') is not None:
            self.dst_cidr = m.get('DstCidr')
        if m.get('DstPortRange') is not None:
            self.dst_port_range = m.get('DstPortRange')
        if m.get('MatchDscp') is not None:
            self.match_dscp = m.get('MatchDscp')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('SrcCidr') is not None:
            self.src_cidr = m.get('SrcCidr')
        if m.get('SrcPortRange') is not None:
            self.src_port_range = m.get('SrcPortRange')
        if m.get('TrafficMatchRuleDescription') is not None:
            self.traffic_match_rule_description = m.get('TrafficMatchRuleDescription')
        if m.get('TrafficMatchRuleName') is not None:
            self.traffic_match_rule_name = m.get('TrafficMatchRuleName')
        return self


class AddTrafficMatchRuleToTrafficMarkingPolicyRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_marking_policy_id=None, traffic_match_rules=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_marking_policy_id = traffic_marking_policy_id  # type: str
        self.traffic_match_rules = traffic_match_rules  # type: list[AddTrafficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules]

    def validate(self):
        if self.traffic_match_rules:
            for k in self.traffic_match_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddTrafficMatchRuleToTrafficMarkingPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id
        result['TrafficMatchRules'] = []
        if self.traffic_match_rules is not None:
            for k in self.traffic_match_rules:
                result['TrafficMatchRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')
        self.traffic_match_rules = []
        if m.get('TrafficMatchRules') is not None:
            for k in m.get('TrafficMatchRules'):
                temp_model = AddTrafficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules()
                self.traffic_match_rules.append(temp_model.from_map(k))
        return self


class AddTrafficMatchRuleToTrafficMarkingPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTrafficMatchRuleToTrafficMarkingPolicyResponseBody, self).to_map()
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


class AddTrafficMatchRuleToTrafficMarkingPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddTrafficMatchRuleToTrafficMarkingPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddTrafficMatchRuleToTrafficMarkingPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddTrafficMatchRuleToTrafficMarkingPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTraficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules(TeaModel):
    def __init__(self, dst_cidr=None, dst_port_range=None, match_dscp=None, protocol=None, src_cidr=None,
                 src_port_range=None, traffic_match_rule_description=None, traffic_match_rule_name=None):
        self.dst_cidr = dst_cidr  # type: str
        self.dst_port_range = dst_port_range  # type: list[int]
        self.match_dscp = match_dscp  # type: int
        self.protocol = protocol  # type: str
        self.src_cidr = src_cidr  # type: str
        self.src_port_range = src_port_range  # type: list[int]
        self.traffic_match_rule_description = traffic_match_rule_description  # type: str
        self.traffic_match_rule_name = traffic_match_rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTraficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_cidr is not None:
            result['DstCidr'] = self.dst_cidr
        if self.dst_port_range is not None:
            result['DstPortRange'] = self.dst_port_range
        if self.match_dscp is not None:
            result['MatchDscp'] = self.match_dscp
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.src_cidr is not None:
            result['SrcCidr'] = self.src_cidr
        if self.src_port_range is not None:
            result['SrcPortRange'] = self.src_port_range
        if self.traffic_match_rule_description is not None:
            result['TrafficMatchRuleDescription'] = self.traffic_match_rule_description
        if self.traffic_match_rule_name is not None:
            result['TrafficMatchRuleName'] = self.traffic_match_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DstCidr') is not None:
            self.dst_cidr = m.get('DstCidr')
        if m.get('DstPortRange') is not None:
            self.dst_port_range = m.get('DstPortRange')
        if m.get('MatchDscp') is not None:
            self.match_dscp = m.get('MatchDscp')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('SrcCidr') is not None:
            self.src_cidr = m.get('SrcCidr')
        if m.get('SrcPortRange') is not None:
            self.src_port_range = m.get('SrcPortRange')
        if m.get('TrafficMatchRuleDescription') is not None:
            self.traffic_match_rule_description = m.get('TrafficMatchRuleDescription')
        if m.get('TrafficMatchRuleName') is not None:
            self.traffic_match_rule_name = m.get('TrafficMatchRuleName')
        return self


class AddTraficMatchRuleToTrafficMarkingPolicyRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_marking_policy_id=None, traffic_match_rules=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_marking_policy_id = traffic_marking_policy_id  # type: str
        self.traffic_match_rules = traffic_match_rules  # type: list[AddTraficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules]

    def validate(self):
        if self.traffic_match_rules:
            for k in self.traffic_match_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddTraficMatchRuleToTrafficMarkingPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id
        result['TrafficMatchRules'] = []
        if self.traffic_match_rules is not None:
            for k in self.traffic_match_rules:
                result['TrafficMatchRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')
        self.traffic_match_rules = []
        if m.get('TrafficMatchRules') is not None:
            for k in m.get('TrafficMatchRules'):
                temp_model = AddTraficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules()
                self.traffic_match_rules.append(temp_model.from_map(k))
        return self


class AddTraficMatchRuleToTrafficMarkingPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTraficMatchRuleToTrafficMarkingPolicyResponseBody, self).to_map()
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


class AddTraficMatchRuleToTrafficMarkingPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddTraficMatchRuleToTrafficMarkingPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddTraficMatchRuleToTrafficMarkingPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddTraficMatchRuleToTrafficMarkingPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateCenBandwidthPackageRequest(TeaModel):
    def __init__(self, cen_bandwidth_package_id=None, cen_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateCenBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AssociateCenBandwidthPackageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateCenBandwidthPackageResponseBody, self).to_map()
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


class AssociateCenBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateCenBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateCenBandwidthPackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateCenBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateTransitRouterAttachmentWithRouteTableRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_route_table_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateTransitRouterAttachmentWithRouteTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class AssociateTransitRouterAttachmentWithRouteTableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateTransitRouterAttachmentWithRouteTableResponseBody, self).to_map()
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


class AssociateTransitRouterAttachmentWithRouteTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateTransitRouterAttachmentWithRouteTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateTransitRouterAttachmentWithRouteTableResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateTransitRouterAttachmentWithRouteTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateTransitRouterMulticastDomainRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_multicast_domain_id=None, v_switch_ids=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str
        self.v_switch_ids = v_switch_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateTransitRouterMulticastDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class AssociateTransitRouterMulticastDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateTransitRouterMulticastDomainResponseBody, self).to_map()
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


class AssociateTransitRouterMulticastDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateTransitRouterMulticastDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateTransitRouterMulticastDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateTransitRouterMulticastDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachCenChildInstanceRequest(TeaModel):
    def __init__(self, cen_id=None, child_instance_id=None, child_instance_owner_id=None,
                 child_instance_region_id=None, child_instance_type=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_owner_id = child_instance_owner_id  # type: long
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachCenChildInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AttachCenChildInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachCenChildInstanceResponseBody, self).to_map()
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


class AttachCenChildInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachCenChildInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachCenChildInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachCenChildInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTransitRouterServiceRequest(TeaModel):
    def __init__(self, client_token=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.client_token = client_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTransitRouterServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckTransitRouterServiceResponseBody(TeaModel):
    def __init__(self, enabled=None, request_id=None):
        self.enabled = enabled  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTransitRouterServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckTransitRouterServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckTransitRouterServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckTransitRouterServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckTransitRouterServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenRequest(TeaModel):
    def __init__(self, client_token=None, description=None, name=None, owner_account=None, owner_id=None,
                 protection_level=None, resource_owner_account=None, resource_owner_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.protection_level = protection_level  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateCenResponseBody(TeaModel):
    def __init__(self, cen_id=None, request_id=None):
        self.cen_id = cen_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenBandwidthPackageRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_renew=None, auto_renew_duration=None, bandwidth=None,
                 bandwidth_package_charge_type=None, client_token=None, description=None, geographic_region_aid=None, geographic_region_bid=None,
                 name=None, owner_account=None, owner_id=None, period=None, pricing_cycle=None,
                 resource_owner_account=None, resource_owner_id=None, service_type=None):
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_package_charge_type = bandwidth_package_charge_type  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.geographic_region_aid = geographic_region_aid  # type: str
        self.geographic_region_bid = geographic_region_bid  # type: str
        self.name = name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.period = period  # type: int
        self.pricing_cycle = pricing_cycle  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package_charge_type is not None:
            result['BandwidthPackageChargeType'] = self.bandwidth_package_charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.geographic_region_aid is not None:
            result['GeographicRegionAId'] = self.geographic_region_aid
        if self.geographic_region_bid is not None:
            result['GeographicRegionBId'] = self.geographic_region_bid
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackageChargeType') is not None:
            self.bandwidth_package_charge_type = m.get('BandwidthPackageChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GeographicRegionAId') is not None:
            self.geographic_region_aid = m.get('GeographicRegionAId')
        if m.get('GeographicRegionBId') is not None:
            self.geographic_region_bid = m.get('GeographicRegionBId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class CreateCenBandwidthPackageResponseBody(TeaModel):
    def __init__(self, cen_bandwidth_package_id=None, cen_bandwidth_package_order_id=None, request_id=None):
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.cen_bandwidth_package_order_id = cen_bandwidth_package_order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenBandwidthPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.cen_bandwidth_package_order_id is not None:
            result['CenBandwidthPackageOrderId'] = self.cen_bandwidth_package_order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('CenBandwidthPackageOrderId') is not None:
            self.cen_bandwidth_package_order_id = m.get('CenBandwidthPackageOrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCenBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCenBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCenBandwidthPackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCenBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenChildInstanceRouteEntryToAttachmentRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, destination_cidr_block=None, dry_run=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, route_table_id=None,
                 transit_router_attachment_id=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.route_table_id = route_table_id  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenChildInstanceRouteEntryToAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class CreateCenChildInstanceRouteEntryToAttachmentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenChildInstanceRouteEntryToAttachmentResponseBody, self).to_map()
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


class CreateCenChildInstanceRouteEntryToAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCenChildInstanceRouteEntryToAttachmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCenChildInstanceRouteEntryToAttachmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCenChildInstanceRouteEntryToAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenChildInstanceRouteEntryToCenRequest(TeaModel):
    def __init__(self, cen_id=None, child_instance_ali_uid=None, child_instance_id=None,
                 child_instance_region_id=None, child_instance_type=None, destination_cidr_block=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, route_table_id=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_ali_uid = child_instance_ali_uid  # type: long
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.route_table_id = route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenChildInstanceRouteEntryToCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_ali_uid is not None:
            result['ChildInstanceAliUid'] = self.child_instance_ali_uid
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceAliUid') is not None:
            self.child_instance_ali_uid = m.get('ChildInstanceAliUid')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class CreateCenChildInstanceRouteEntryToCenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenChildInstanceRouteEntryToCenResponseBody, self).to_map()
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


class CreateCenChildInstanceRouteEntryToCenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCenChildInstanceRouteEntryToCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCenChildInstanceRouteEntryToCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCenChildInstanceRouteEntryToCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenInterRegionTrafficQosPolicyRequestTrafficQosQueues(TeaModel):
    def __init__(self, dscps=None, qos_queue_description=None, qos_queue_name=None, remain_bandwidth_percent=None):
        self.dscps = dscps  # type: list[int]
        self.qos_queue_description = qos_queue_description  # type: str
        self.qos_queue_name = qos_queue_name  # type: str
        self.remain_bandwidth_percent = remain_bandwidth_percent  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenInterRegionTrafficQosPolicyRequestTrafficQosQueues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dscps is not None:
            result['Dscps'] = self.dscps
        if self.qos_queue_description is not None:
            result['QosQueueDescription'] = self.qos_queue_description
        if self.qos_queue_name is not None:
            result['QosQueueName'] = self.qos_queue_name
        if self.remain_bandwidth_percent is not None:
            result['RemainBandwidthPercent'] = self.remain_bandwidth_percent
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dscps') is not None:
            self.dscps = m.get('Dscps')
        if m.get('QosQueueDescription') is not None:
            self.qos_queue_description = m.get('QosQueueDescription')
        if m.get('QosQueueName') is not None:
            self.qos_queue_name = m.get('QosQueueName')
        if m.get('RemainBandwidthPercent') is not None:
            self.remain_bandwidth_percent = m.get('RemainBandwidthPercent')
        return self


class CreateCenInterRegionTrafficQosPolicyRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_qos_policy_description=None, traffic_qos_policy_name=None,
                 traffic_qos_queues=None, transit_router_attachment_id=None, transit_router_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_qos_policy_description = traffic_qos_policy_description  # type: str
        self.traffic_qos_policy_name = traffic_qos_policy_name  # type: str
        self.traffic_qos_queues = traffic_qos_queues  # type: list[CreateCenInterRegionTrafficQosPolicyRequestTrafficQosQueues]
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        if self.traffic_qos_queues:
            for k in self.traffic_qos_queues:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCenInterRegionTrafficQosPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_qos_policy_description is not None:
            result['TrafficQosPolicyDescription'] = self.traffic_qos_policy_description
        if self.traffic_qos_policy_name is not None:
            result['TrafficQosPolicyName'] = self.traffic_qos_policy_name
        result['TrafficQosQueues'] = []
        if self.traffic_qos_queues is not None:
            for k in self.traffic_qos_queues:
                result['TrafficQosQueues'].append(k.to_map() if k else None)
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficQosPolicyDescription') is not None:
            self.traffic_qos_policy_description = m.get('TrafficQosPolicyDescription')
        if m.get('TrafficQosPolicyName') is not None:
            self.traffic_qos_policy_name = m.get('TrafficQosPolicyName')
        self.traffic_qos_queues = []
        if m.get('TrafficQosQueues') is not None:
            for k in m.get('TrafficQosQueues'):
                temp_model = CreateCenInterRegionTrafficQosPolicyRequestTrafficQosQueues()
                self.traffic_qos_queues.append(temp_model.from_map(k))
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class CreateCenInterRegionTrafficQosPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, traffic_qos_policy_id=None):
        self.request_id = request_id  # type: str
        self.traffic_qos_policy_id = traffic_qos_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenInterRegionTrafficQosPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_qos_policy_id is not None:
            result['TrafficQosPolicyId'] = self.traffic_qos_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficQosPolicyId') is not None:
            self.traffic_qos_policy_id = m.get('TrafficQosPolicyId')
        return self


class CreateCenInterRegionTrafficQosPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCenInterRegionTrafficQosPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCenInterRegionTrafficQosPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCenInterRegionTrafficQosPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenInterRegionTrafficQosQueueRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, dscps=None, owner_account=None, owner_id=None,
                 qos_queue_description=None, qos_queue_name=None, remain_bandwidth_percent=None, resource_owner_account=None,
                 resource_owner_id=None, traffic_qos_policy_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.dscps = dscps  # type: list[int]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.qos_queue_description = qos_queue_description  # type: str
        self.qos_queue_name = qos_queue_name  # type: str
        self.remain_bandwidth_percent = remain_bandwidth_percent  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_qos_policy_id = traffic_qos_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenInterRegionTrafficQosQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.dscps is not None:
            result['Dscps'] = self.dscps
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qos_queue_description is not None:
            result['QosQueueDescription'] = self.qos_queue_description
        if self.qos_queue_name is not None:
            result['QosQueueName'] = self.qos_queue_name
        if self.remain_bandwidth_percent is not None:
            result['RemainBandwidthPercent'] = self.remain_bandwidth_percent
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_qos_policy_id is not None:
            result['TrafficQosPolicyId'] = self.traffic_qos_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Dscps') is not None:
            self.dscps = m.get('Dscps')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QosQueueDescription') is not None:
            self.qos_queue_description = m.get('QosQueueDescription')
        if m.get('QosQueueName') is not None:
            self.qos_queue_name = m.get('QosQueueName')
        if m.get('RemainBandwidthPercent') is not None:
            self.remain_bandwidth_percent = m.get('RemainBandwidthPercent')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficQosPolicyId') is not None:
            self.traffic_qos_policy_id = m.get('TrafficQosPolicyId')
        return self


class CreateCenInterRegionTrafficQosQueueResponseBody(TeaModel):
    def __init__(self, qos_queue_id=None, request_id=None):
        self.qos_queue_id = qos_queue_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenInterRegionTrafficQosQueueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qos_queue_id is not None:
            result['QosQueueId'] = self.qos_queue_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QosQueueId') is not None:
            self.qos_queue_id = m.get('QosQueueId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCenInterRegionTrafficQosQueueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCenInterRegionTrafficQosQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCenInterRegionTrafficQosQueueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCenInterRegionTrafficQosQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenRouteMapRequest(TeaModel):
    def __init__(self, as_path_match_mode=None, cen_id=None, cen_region_id=None, cidr_match_mode=None,
                 community_match_mode=None, community_operate_mode=None, description=None, destination_child_instance_types=None,
                 destination_cidr_blocks=None, destination_instance_ids=None, destination_instance_ids_reverse_match=None,
                 destination_route_table_ids=None, map_result=None, match_address_type=None, match_asns=None, match_community_set=None,
                 next_priority=None, operate_community_set=None, owner_account=None, owner_id=None, preference=None,
                 prepend_as_path=None, priority=None, resource_owner_account=None, resource_owner_id=None, route_types=None,
                 source_child_instance_types=None, source_instance_ids=None, source_instance_ids_reverse_match=None, source_region_ids=None,
                 source_route_table_ids=None, transit_router_route_table_id=None, transmit_direction=None):
        self.as_path_match_mode = as_path_match_mode  # type: str
        self.cen_id = cen_id  # type: str
        self.cen_region_id = cen_region_id  # type: str
        self.cidr_match_mode = cidr_match_mode  # type: str
        self.community_match_mode = community_match_mode  # type: str
        self.community_operate_mode = community_operate_mode  # type: str
        self.description = description  # type: str
        self.destination_child_instance_types = destination_child_instance_types  # type: list[str]
        self.destination_cidr_blocks = destination_cidr_blocks  # type: list[str]
        self.destination_instance_ids = destination_instance_ids  # type: list[str]
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match  # type: bool
        self.destination_route_table_ids = destination_route_table_ids  # type: list[str]
        self.map_result = map_result  # type: str
        self.match_address_type = match_address_type  # type: str
        self.match_asns = match_asns  # type: list[long]
        self.match_community_set = match_community_set  # type: list[str]
        self.next_priority = next_priority  # type: int
        self.operate_community_set = operate_community_set  # type: list[str]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.preference = preference  # type: int
        self.prepend_as_path = prepend_as_path  # type: list[long]
        self.priority = priority  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.route_types = route_types  # type: list[str]
        self.source_child_instance_types = source_child_instance_types  # type: list[str]
        self.source_instance_ids = source_instance_ids  # type: list[str]
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match  # type: bool
        self.source_region_ids = source_region_ids  # type: list[str]
        self.source_route_table_ids = source_route_table_ids  # type: list[str]
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str
        self.transmit_direction = transmit_direction  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenRouteMapRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path_match_mode is not None:
            result['AsPathMatchMode'] = self.as_path_match_mode
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.cidr_match_mode is not None:
            result['CidrMatchMode'] = self.cidr_match_mode
        if self.community_match_mode is not None:
            result['CommunityMatchMode'] = self.community_match_mode
        if self.community_operate_mode is not None:
            result['CommunityOperateMode'] = self.community_operate_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_child_instance_types is not None:
            result['DestinationChildInstanceTypes'] = self.destination_child_instance_types
        if self.destination_cidr_blocks is not None:
            result['DestinationCidrBlocks'] = self.destination_cidr_blocks
        if self.destination_instance_ids is not None:
            result['DestinationInstanceIds'] = self.destination_instance_ids
        if self.destination_instance_ids_reverse_match is not None:
            result['DestinationInstanceIdsReverseMatch'] = self.destination_instance_ids_reverse_match
        if self.destination_route_table_ids is not None:
            result['DestinationRouteTableIds'] = self.destination_route_table_ids
        if self.map_result is not None:
            result['MapResult'] = self.map_result
        if self.match_address_type is not None:
            result['MatchAddressType'] = self.match_address_type
        if self.match_asns is not None:
            result['MatchAsns'] = self.match_asns
        if self.match_community_set is not None:
            result['MatchCommunitySet'] = self.match_community_set
        if self.next_priority is not None:
            result['NextPriority'] = self.next_priority
        if self.operate_community_set is not None:
            result['OperateCommunitySet'] = self.operate_community_set
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preference is not None:
            result['Preference'] = self.preference
        if self.prepend_as_path is not None:
            result['PrependAsPath'] = self.prepend_as_path
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_types is not None:
            result['RouteTypes'] = self.route_types
        if self.source_child_instance_types is not None:
            result['SourceChildInstanceTypes'] = self.source_child_instance_types
        if self.source_instance_ids is not None:
            result['SourceInstanceIds'] = self.source_instance_ids
        if self.source_instance_ids_reverse_match is not None:
            result['SourceInstanceIdsReverseMatch'] = self.source_instance_ids_reverse_match
        if self.source_region_ids is not None:
            result['SourceRegionIds'] = self.source_region_ids
        if self.source_route_table_ids is not None:
            result['SourceRouteTableIds'] = self.source_route_table_ids
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        if self.transmit_direction is not None:
            result['TransmitDirection'] = self.transmit_direction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsPathMatchMode') is not None:
            self.as_path_match_mode = m.get('AsPathMatchMode')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('CidrMatchMode') is not None:
            self.cidr_match_mode = m.get('CidrMatchMode')
        if m.get('CommunityMatchMode') is not None:
            self.community_match_mode = m.get('CommunityMatchMode')
        if m.get('CommunityOperateMode') is not None:
            self.community_operate_mode = m.get('CommunityOperateMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationChildInstanceTypes') is not None:
            self.destination_child_instance_types = m.get('DestinationChildInstanceTypes')
        if m.get('DestinationCidrBlocks') is not None:
            self.destination_cidr_blocks = m.get('DestinationCidrBlocks')
        if m.get('DestinationInstanceIds') is not None:
            self.destination_instance_ids = m.get('DestinationInstanceIds')
        if m.get('DestinationInstanceIdsReverseMatch') is not None:
            self.destination_instance_ids_reverse_match = m.get('DestinationInstanceIdsReverseMatch')
        if m.get('DestinationRouteTableIds') is not None:
            self.destination_route_table_ids = m.get('DestinationRouteTableIds')
        if m.get('MapResult') is not None:
            self.map_result = m.get('MapResult')
        if m.get('MatchAddressType') is not None:
            self.match_address_type = m.get('MatchAddressType')
        if m.get('MatchAsns') is not None:
            self.match_asns = m.get('MatchAsns')
        if m.get('MatchCommunitySet') is not None:
            self.match_community_set = m.get('MatchCommunitySet')
        if m.get('NextPriority') is not None:
            self.next_priority = m.get('NextPriority')
        if m.get('OperateCommunitySet') is not None:
            self.operate_community_set = m.get('OperateCommunitySet')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Preference') is not None:
            self.preference = m.get('Preference')
        if m.get('PrependAsPath') is not None:
            self.prepend_as_path = m.get('PrependAsPath')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteTypes') is not None:
            self.route_types = m.get('RouteTypes')
        if m.get('SourceChildInstanceTypes') is not None:
            self.source_child_instance_types = m.get('SourceChildInstanceTypes')
        if m.get('SourceInstanceIds') is not None:
            self.source_instance_ids = m.get('SourceInstanceIds')
        if m.get('SourceInstanceIdsReverseMatch') is not None:
            self.source_instance_ids_reverse_match = m.get('SourceInstanceIdsReverseMatch')
        if m.get('SourceRegionIds') is not None:
            self.source_region_ids = m.get('SourceRegionIds')
        if m.get('SourceRouteTableIds') is not None:
            self.source_route_table_ids = m.get('SourceRouteTableIds')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        if m.get('TransmitDirection') is not None:
            self.transmit_direction = m.get('TransmitDirection')
        return self


class CreateCenRouteMapResponseBody(TeaModel):
    def __init__(self, request_id=None, route_map_id=None):
        self.request_id = request_id  # type: str
        self.route_map_id = route_map_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCenRouteMapResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        return self


class CreateCenRouteMapResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCenRouteMapResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCenRouteMapResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCenRouteMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowlogRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, description=None, flow_log_name=None, interval=None,
                 log_store_name=None, owner_account=None, owner_id=None, project_name=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.flow_log_name = flow_log_name  # type: str
        self.interval = interval  # type: long
        self.log_store_name = log_store_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowlogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class CreateFlowlogResponseBody(TeaModel):
    def __init__(self, flow_log_id=None, request_id=None, success=None):
        self.flow_log_id = flow_log_id  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowlogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFlowlogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFlowlogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowlogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFlowlogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrafficMarkingPolicyRequestTrafficMatchRules(TeaModel):
    def __init__(self, dst_cidr=None, dst_port_range=None, match_dscp=None, protocol=None, src_cidr=None,
                 src_port_range=None, traffic_match_rule_description=None, traffic_match_rule_name=None):
        self.dst_cidr = dst_cidr  # type: str
        self.dst_port_range = dst_port_range  # type: list[int]
        self.match_dscp = match_dscp  # type: int
        self.protocol = protocol  # type: str
        self.src_cidr = src_cidr  # type: str
        self.src_port_range = src_port_range  # type: list[int]
        self.traffic_match_rule_description = traffic_match_rule_description  # type: str
        self.traffic_match_rule_name = traffic_match_rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrafficMarkingPolicyRequestTrafficMatchRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_cidr is not None:
            result['DstCidr'] = self.dst_cidr
        if self.dst_port_range is not None:
            result['DstPortRange'] = self.dst_port_range
        if self.match_dscp is not None:
            result['MatchDscp'] = self.match_dscp
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.src_cidr is not None:
            result['SrcCidr'] = self.src_cidr
        if self.src_port_range is not None:
            result['SrcPortRange'] = self.src_port_range
        if self.traffic_match_rule_description is not None:
            result['TrafficMatchRuleDescription'] = self.traffic_match_rule_description
        if self.traffic_match_rule_name is not None:
            result['TrafficMatchRuleName'] = self.traffic_match_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DstCidr') is not None:
            self.dst_cidr = m.get('DstCidr')
        if m.get('DstPortRange') is not None:
            self.dst_port_range = m.get('DstPortRange')
        if m.get('MatchDscp') is not None:
            self.match_dscp = m.get('MatchDscp')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('SrcCidr') is not None:
            self.src_cidr = m.get('SrcCidr')
        if m.get('SrcPortRange') is not None:
            self.src_port_range = m.get('SrcPortRange')
        if m.get('TrafficMatchRuleDescription') is not None:
            self.traffic_match_rule_description = m.get('TrafficMatchRuleDescription')
        if m.get('TrafficMatchRuleName') is not None:
            self.traffic_match_rule_name = m.get('TrafficMatchRuleName')
        return self


class CreateTrafficMarkingPolicyRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, marking_dscp=None, owner_account=None, owner_id=None,
                 priority=None, resource_owner_account=None, resource_owner_id=None,
                 traffic_marking_policy_description=None, traffic_marking_policy_name=None, traffic_match_rules=None, transit_router_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.marking_dscp = marking_dscp  # type: int
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.priority = priority  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_marking_policy_description = traffic_marking_policy_description  # type: str
        self.traffic_marking_policy_name = traffic_marking_policy_name  # type: str
        self.traffic_match_rules = traffic_match_rules  # type: list[CreateTrafficMarkingPolicyRequestTrafficMatchRules]
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        if self.traffic_match_rules:
            for k in self.traffic_match_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTrafficMarkingPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.marking_dscp is not None:
            result['MarkingDscp'] = self.marking_dscp
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_marking_policy_description is not None:
            result['TrafficMarkingPolicyDescription'] = self.traffic_marking_policy_description
        if self.traffic_marking_policy_name is not None:
            result['TrafficMarkingPolicyName'] = self.traffic_marking_policy_name
        result['TrafficMatchRules'] = []
        if self.traffic_match_rules is not None:
            for k in self.traffic_match_rules:
                result['TrafficMatchRules'].append(k.to_map() if k else None)
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('MarkingDscp') is not None:
            self.marking_dscp = m.get('MarkingDscp')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficMarkingPolicyDescription') is not None:
            self.traffic_marking_policy_description = m.get('TrafficMarkingPolicyDescription')
        if m.get('TrafficMarkingPolicyName') is not None:
            self.traffic_marking_policy_name = m.get('TrafficMarkingPolicyName')
        self.traffic_match_rules = []
        if m.get('TrafficMatchRules') is not None:
            for k in m.get('TrafficMatchRules'):
                temp_model = CreateTrafficMarkingPolicyRequestTrafficMatchRules()
                self.traffic_match_rules.append(temp_model.from_map(k))
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class CreateTrafficMarkingPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, traffic_marking_policy_id=None):
        self.request_id = request_id  # type: str
        self.traffic_marking_policy_id = traffic_marking_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrafficMarkingPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')
        return self


class CreateTrafficMarkingPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTrafficMarkingPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTrafficMarkingPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTrafficMarkingPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransitRouterRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, support_multicast=None,
                 transit_router_description=None, transit_router_name=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.support_multicast = support_multicast  # type: bool
        self.transit_router_description = transit_router_description  # type: str
        self.transit_router_name = transit_router_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.support_multicast is not None:
            result['SupportMulticast'] = self.support_multicast
        if self.transit_router_description is not None:
            result['TransitRouterDescription'] = self.transit_router_description
        if self.transit_router_name is not None:
            result['TransitRouterName'] = self.transit_router_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SupportMulticast') is not None:
            self.support_multicast = m.get('SupportMulticast')
        if m.get('TransitRouterDescription') is not None:
            self.transit_router_description = m.get('TransitRouterDescription')
        if m.get('TransitRouterName') is not None:
            self.transit_router_name = m.get('TransitRouterName')
        return self


class CreateTransitRouterResponseBody(TeaModel):
    def __init__(self, request_id=None, transit_router_id=None):
        self.request_id = request_id  # type: str
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class CreateTransitRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransitRouterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransitRouterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransitRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransitRouterMulticastDomainRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, transit_router_id=None,
                 transit_router_multicast_domain_description=None, transit_router_multicast_domain_name=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_multicast_domain_description = transit_router_multicast_domain_description  # type: str
        self.transit_router_multicast_domain_name = transit_router_multicast_domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterMulticastDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_multicast_domain_description is not None:
            result['TransitRouterMulticastDomainDescription'] = self.transit_router_multicast_domain_description
        if self.transit_router_multicast_domain_name is not None:
            result['TransitRouterMulticastDomainName'] = self.transit_router_multicast_domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterMulticastDomainDescription') is not None:
            self.transit_router_multicast_domain_description = m.get('TransitRouterMulticastDomainDescription')
        if m.get('TransitRouterMulticastDomainName') is not None:
            self.transit_router_multicast_domain_name = m.get('TransitRouterMulticastDomainName')
        return self


class CreateTransitRouterMulticastDomainResponseBody(TeaModel):
    def __init__(self, request_id=None, transit_router_multicast_domain_id=None):
        self.request_id = request_id  # type: str
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterMulticastDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        return self


class CreateTransitRouterMulticastDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransitRouterMulticastDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransitRouterMulticastDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransitRouterMulticastDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransitRouterPeerAttachmentRequest(TeaModel):
    def __init__(self, auto_publish_route_enabled=None, bandwidth=None, bandwidth_type=None,
                 cen_bandwidth_package_id=None, cen_id=None, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 peer_transit_router_id=None, peer_transit_router_region_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, transit_router_attachment_description=None, transit_router_attachment_name=None,
                 transit_router_id=None):
        self.auto_publish_route_enabled = auto_publish_route_enabled  # type: bool
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.peer_transit_router_id = peer_transit_router_id  # type: str
        self.peer_transit_router_region_id = peer_transit_router_region_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterPeerAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.peer_transit_router_id is not None:
            result['PeerTransitRouterId'] = self.peer_transit_router_id
        if self.peer_transit_router_region_id is not None:
            result['PeerTransitRouterRegionId'] = self.peer_transit_router_region_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PeerTransitRouterId') is not None:
            self.peer_transit_router_id = m.get('PeerTransitRouterId')
        if m.get('PeerTransitRouterRegionId') is not None:
            self.peer_transit_router_region_id = m.get('PeerTransitRouterRegionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class CreateTransitRouterPeerAttachmentResponseBody(TeaModel):
    def __init__(self, request_id=None, transit_router_attachment_id=None):
        self.request_id = request_id  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterPeerAttachmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class CreateTransitRouterPeerAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransitRouterPeerAttachmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransitRouterPeerAttachmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransitRouterPeerAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransitRouterPrefixListAssociationRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, next_hop=None, next_hop_type=None, owner_account=None,
                 owner_id=None, owner_uid=None, prefix_list_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, transit_router_id=None, transit_router_table_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.next_hop = next_hop  # type: str
        self.next_hop_type = next_hop_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.owner_uid = owner_uid  # type: long
        self.prefix_list_id = prefix_list_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_table_id = transit_router_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterPrefixListAssociationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_table_id is not None:
            result['TransitRouterTableId'] = self.transit_router_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterTableId') is not None:
            self.transit_router_table_id = m.get('TransitRouterTableId')
        return self


class CreateTransitRouterPrefixListAssociationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterPrefixListAssociationResponseBody, self).to_map()
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


class CreateTransitRouterPrefixListAssociationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransitRouterPrefixListAssociationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransitRouterPrefixListAssociationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransitRouterPrefixListAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransitRouterRouteEntryRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_route_entry_description=None,
                 transit_router_route_entry_destination_cidr_block=None, transit_router_route_entry_name=None, transit_router_route_entry_next_hop_id=None,
                 transit_router_route_entry_next_hop_type=None, transit_router_route_table_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_route_entry_description = transit_router_route_entry_description  # type: str
        self.transit_router_route_entry_destination_cidr_block = transit_router_route_entry_destination_cidr_block  # type: str
        self.transit_router_route_entry_name = transit_router_route_entry_name  # type: str
        self.transit_router_route_entry_next_hop_id = transit_router_route_entry_next_hop_id  # type: str
        self.transit_router_route_entry_next_hop_type = transit_router_route_entry_next_hop_type  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterRouteEntryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_route_entry_description is not None:
            result['TransitRouterRouteEntryDescription'] = self.transit_router_route_entry_description
        if self.transit_router_route_entry_destination_cidr_block is not None:
            result['TransitRouterRouteEntryDestinationCidrBlock'] = self.transit_router_route_entry_destination_cidr_block
        if self.transit_router_route_entry_name is not None:
            result['TransitRouterRouteEntryName'] = self.transit_router_route_entry_name
        if self.transit_router_route_entry_next_hop_id is not None:
            result['TransitRouterRouteEntryNextHopId'] = self.transit_router_route_entry_next_hop_id
        if self.transit_router_route_entry_next_hop_type is not None:
            result['TransitRouterRouteEntryNextHopType'] = self.transit_router_route_entry_next_hop_type
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterRouteEntryDescription') is not None:
            self.transit_router_route_entry_description = m.get('TransitRouterRouteEntryDescription')
        if m.get('TransitRouterRouteEntryDestinationCidrBlock') is not None:
            self.transit_router_route_entry_destination_cidr_block = m.get('TransitRouterRouteEntryDestinationCidrBlock')
        if m.get('TransitRouterRouteEntryName') is not None:
            self.transit_router_route_entry_name = m.get('TransitRouterRouteEntryName')
        if m.get('TransitRouterRouteEntryNextHopId') is not None:
            self.transit_router_route_entry_next_hop_id = m.get('TransitRouterRouteEntryNextHopId')
        if m.get('TransitRouterRouteEntryNextHopType') is not None:
            self.transit_router_route_entry_next_hop_type = m.get('TransitRouterRouteEntryNextHopType')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class CreateTransitRouterRouteEntryResponseBody(TeaModel):
    def __init__(self, request_id=None, transit_router_route_entry_id=None):
        self.request_id = request_id  # type: str
        self.transit_router_route_entry_id = transit_router_route_entry_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterRouteEntryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transit_router_route_entry_id is not None:
            result['TransitRouterRouteEntryId'] = self.transit_router_route_entry_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransitRouterRouteEntryId') is not None:
            self.transit_router_route_entry_id = m.get('TransitRouterRouteEntryId')
        return self


class CreateTransitRouterRouteEntryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransitRouterRouteEntryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransitRouterRouteEntryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransitRouterRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransitRouterRouteTableRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_id=None,
                 transit_router_route_table_description=None, transit_router_route_table_name=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_route_table_description = transit_router_route_table_description  # type: str
        self.transit_router_route_table_name = transit_router_route_table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterRouteTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_route_table_description is not None:
            result['TransitRouterRouteTableDescription'] = self.transit_router_route_table_description
        if self.transit_router_route_table_name is not None:
            result['TransitRouterRouteTableName'] = self.transit_router_route_table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterRouteTableDescription') is not None:
            self.transit_router_route_table_description = m.get('TransitRouterRouteTableDescription')
        if m.get('TransitRouterRouteTableName') is not None:
            self.transit_router_route_table_name = m.get('TransitRouterRouteTableName')
        return self


class CreateTransitRouterRouteTableResponseBody(TeaModel):
    def __init__(self, request_id=None, transit_router_route_table_id=None):
        self.request_id = request_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterRouteTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class CreateTransitRouterRouteTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransitRouterRouteTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransitRouterRouteTableResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransitRouterRouteTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransitRouterVbrAttachmentRequest(TeaModel):
    def __init__(self, auto_publish_route_enabled=None, cen_id=None, client_token=None, dry_run=None,
                 owner_account=None, owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None,
                 transit_router_attachment_description=None, transit_router_attachment_name=None, transit_router_id=None, vbr_id=None, vbr_owner_id=None):
        self.auto_publish_route_enabled = auto_publish_route_enabled  # type: bool
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.vbr_id = vbr_id  # type: str
        self.vbr_owner_id = vbr_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterVbrAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        if self.vbr_owner_id is not None:
            result['VbrOwnerId'] = self.vbr_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        if m.get('VbrOwnerId') is not None:
            self.vbr_owner_id = m.get('VbrOwnerId')
        return self


class CreateTransitRouterVbrAttachmentResponseBody(TeaModel):
    def __init__(self, request_id=None, transit_router_attachment_id=None):
        self.request_id = request_id  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterVbrAttachmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class CreateTransitRouterVbrAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransitRouterVbrAttachmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransitRouterVbrAttachmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransitRouterVbrAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransitRouterVpcAttachmentRequestZoneMappings(TeaModel):
    def __init__(self, v_switch_id=None, zone_id=None):
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterVpcAttachmentRequestZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateTransitRouterVpcAttachmentRequest(TeaModel):
    def __init__(self, cen_id=None, charge_type=None, client_token=None, dry_run=None, owner_account=None,
                 owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None,
                 transit_router_attachment_description=None, transit_router_attachment_name=None, transit_router_id=None, vpc_id=None, vpc_owner_id=None,
                 zone_mappings=None):
        self.cen_id = cen_id  # type: str
        self.charge_type = charge_type  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_owner_id = vpc_owner_id  # type: long
        self.zone_mappings = zone_mappings  # type: list[CreateTransitRouterVpcAttachmentRequestZoneMappings]

    def validate(self):
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTransitRouterVpcAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = CreateTransitRouterVpcAttachmentRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class CreateTransitRouterVpcAttachmentResponseBody(TeaModel):
    def __init__(self, request_id=None, transit_router_attachment_id=None):
        self.request_id = request_id  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterVpcAttachmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class CreateTransitRouterVpcAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransitRouterVpcAttachmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransitRouterVpcAttachmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransitRouterVpcAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransitRouterVpnAttachmentRequestZone(TeaModel):
    def __init__(self, zone_id=None):
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterVpnAttachmentRequestZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateTransitRouterVpnAttachmentRequest(TeaModel):
    def __init__(self, auto_publish_route_enabled=None, cen_id=None, charge_type=None, client_token=None,
                 dry_run=None, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, transit_router_attachment_description=None, transit_router_attachment_name=None,
                 transit_router_id=None, vpn_id=None, vpn_owner_id=None, zone=None):
        self.auto_publish_route_enabled = auto_publish_route_enabled  # type: bool
        self.cen_id = cen_id  # type: str
        self.charge_type = charge_type  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.vpn_id = vpn_id  # type: str
        self.vpn_owner_id = vpn_owner_id  # type: long
        self.zone = zone  # type: list[CreateTransitRouterVpnAttachmentRequestZone]

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTransitRouterVpnAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.vpn_id is not None:
            result['VpnId'] = self.vpn_id
        if self.vpn_owner_id is not None:
            result['VpnOwnerId'] = self.vpn_owner_id
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('VpnId') is not None:
            self.vpn_id = m.get('VpnId')
        if m.get('VpnOwnerId') is not None:
            self.vpn_owner_id = m.get('VpnOwnerId')
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = CreateTransitRouterVpnAttachmentRequestZone()
                self.zone.append(temp_model.from_map(k))
        return self


class CreateTransitRouterVpnAttachmentResponseBody(TeaModel):
    def __init__(self, request_id=None, transit_router_attachment_id=None):
        self.request_id = request_id  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransitRouterVpnAttachmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class CreateTransitRouterVpnAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransitRouterVpnAttachmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransitRouterVpnAttachmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransitRouterVpnAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactiveFlowLogRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, flow_log_id=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.flow_log_id = flow_log_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeactiveFlowLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeactiveFlowLogResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeactiveFlowLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeactiveFlowLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeactiveFlowLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeactiveFlowLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeactiveFlowLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenRequest(TeaModel):
    def __init__(self, cen_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteCenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenResponseBody, self).to_map()
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


class DeleteCenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenBandwidthPackageRequest(TeaModel):
    def __init__(self, cen_bandwidth_package_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteCenBandwidthPackageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenBandwidthPackageResponseBody, self).to_map()
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


class DeleteCenBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCenBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCenBandwidthPackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCenBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenChildInstanceRouteEntryToAttachmentRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, destination_cidr_block=None, dry_run=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, route_table_id=None,
                 transit_router_attachment_id=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.route_table_id = route_table_id  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenChildInstanceRouteEntryToAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class DeleteCenChildInstanceRouteEntryToAttachmentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenChildInstanceRouteEntryToAttachmentResponseBody, self).to_map()
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


class DeleteCenChildInstanceRouteEntryToAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCenChildInstanceRouteEntryToAttachmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCenChildInstanceRouteEntryToAttachmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCenChildInstanceRouteEntryToAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenChildInstanceRouteEntryToCenRequest(TeaModel):
    def __init__(self, cen_id=None, child_instance_ali_uid=None, child_instance_id=None,
                 child_instance_region_id=None, child_instance_type=None, destination_cidr_block=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, route_table_id=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_ali_uid = child_instance_ali_uid  # type: long
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.route_table_id = route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenChildInstanceRouteEntryToCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_ali_uid is not None:
            result['ChildInstanceAliUid'] = self.child_instance_ali_uid
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceAliUid') is not None:
            self.child_instance_ali_uid = m.get('ChildInstanceAliUid')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DeleteCenChildInstanceRouteEntryToCenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenChildInstanceRouteEntryToCenResponseBody, self).to_map()
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


class DeleteCenChildInstanceRouteEntryToCenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCenChildInstanceRouteEntryToCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCenChildInstanceRouteEntryToCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCenChildInstanceRouteEntryToCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenInterRegionTrafficQosPolicyRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_qos_policy_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_qos_policy_id = traffic_qos_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenInterRegionTrafficQosPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_qos_policy_id is not None:
            result['TrafficQosPolicyId'] = self.traffic_qos_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficQosPolicyId') is not None:
            self.traffic_qos_policy_id = m.get('TrafficQosPolicyId')
        return self


class DeleteCenInterRegionTrafficQosPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenInterRegionTrafficQosPolicyResponseBody, self).to_map()
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


class DeleteCenInterRegionTrafficQosPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCenInterRegionTrafficQosPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCenInterRegionTrafficQosPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCenInterRegionTrafficQosPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenInterRegionTrafficQosQueueRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None, qos_queue_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.qos_queue_id = qos_queue_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenInterRegionTrafficQosQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qos_queue_id is not None:
            result['QosQueueId'] = self.qos_queue_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QosQueueId') is not None:
            self.qos_queue_id = m.get('QosQueueId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteCenInterRegionTrafficQosQueueResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenInterRegionTrafficQosQueueResponseBody, self).to_map()
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


class DeleteCenInterRegionTrafficQosQueueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCenInterRegionTrafficQosQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCenInterRegionTrafficQosQueueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCenInterRegionTrafficQosQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenRouteMapRequest(TeaModel):
    def __init__(self, cen_id=None, cen_region_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, route_map_id=None):
        self.cen_id = cen_id  # type: str
        self.cen_region_id = cen_region_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.route_map_id = route_map_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenRouteMapRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        return self


class DeleteCenRouteMapResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCenRouteMapResponseBody, self).to_map()
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


class DeleteCenRouteMapResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCenRouteMapResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCenRouteMapResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCenRouteMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowlogRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, flow_log_id=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.flow_log_id = flow_log_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowlogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteFlowlogResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowlogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFlowlogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFlowlogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowlogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFlowlogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRouteServiceInCenRequest(TeaModel):
    def __init__(self, access_region_id=None, cen_id=None, host=None, host_region_id=None, host_vpc_id=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.access_region_id = access_region_id  # type: str
        self.cen_id = cen_id  # type: str
        self.host = host  # type: str
        self.host_region_id = host_region_id  # type: str
        self.host_vpc_id = host_vpc_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRouteServiceInCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.host is not None:
            result['Host'] = self.host
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteRouteServiceInCenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRouteServiceInCenResponseBody, self).to_map()
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


class DeleteRouteServiceInCenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRouteServiceInCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRouteServiceInCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRouteServiceInCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrafficMarkingPolicyRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_marking_policy_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_marking_policy_id = traffic_marking_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrafficMarkingPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')
        return self


class DeleteTrafficMarkingPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrafficMarkingPolicyResponseBody, self).to_map()
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


class DeleteTrafficMarkingPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTrafficMarkingPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTrafficMarkingPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTrafficMarkingPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTransitRouterRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class DeleteTransitRouterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterResponseBody, self).to_map()
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


class DeleteTransitRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTransitRouterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTransitRouterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTransitRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTransitRouterMulticastDomainRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_multicast_domain_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterMulticastDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        return self


class DeleteTransitRouterMulticastDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterMulticastDomainResponseBody, self).to_map()
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


class DeleteTransitRouterMulticastDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTransitRouterMulticastDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTransitRouterMulticastDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTransitRouterMulticastDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTransitRouterPeerAttachmentRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterPeerAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class DeleteTransitRouterPeerAttachmentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterPeerAttachmentResponseBody, self).to_map()
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


class DeleteTransitRouterPeerAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTransitRouterPeerAttachmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTransitRouterPeerAttachmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTransitRouterPeerAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTransitRouterPrefixListAssociationRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, next_hop=None, next_hop_type=None, owner_account=None,
                 owner_id=None, prefix_list_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None,
                 transit_router_id=None, transit_router_table_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.next_hop = next_hop  # type: str
        self.next_hop_type = next_hop_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.prefix_list_id = prefix_list_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_table_id = transit_router_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterPrefixListAssociationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_table_id is not None:
            result['TransitRouterTableId'] = self.transit_router_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterTableId') is not None:
            self.transit_router_table_id = m.get('TransitRouterTableId')
        return self


class DeleteTransitRouterPrefixListAssociationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterPrefixListAssociationResponseBody, self).to_map()
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


class DeleteTransitRouterPrefixListAssociationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTransitRouterPrefixListAssociationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTransitRouterPrefixListAssociationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTransitRouterPrefixListAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTransitRouterRouteEntryRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_route_entry_destination_cidr_block=None,
                 transit_router_route_entry_id=None, transit_router_route_entry_next_hop_id=None,
                 transit_router_route_entry_next_hop_type=None, transit_router_route_table_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_route_entry_destination_cidr_block = transit_router_route_entry_destination_cidr_block  # type: str
        self.transit_router_route_entry_id = transit_router_route_entry_id  # type: str
        self.transit_router_route_entry_next_hop_id = transit_router_route_entry_next_hop_id  # type: str
        self.transit_router_route_entry_next_hop_type = transit_router_route_entry_next_hop_type  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterRouteEntryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_route_entry_destination_cidr_block is not None:
            result['TransitRouterRouteEntryDestinationCidrBlock'] = self.transit_router_route_entry_destination_cidr_block
        if self.transit_router_route_entry_id is not None:
            result['TransitRouterRouteEntryId'] = self.transit_router_route_entry_id
        if self.transit_router_route_entry_next_hop_id is not None:
            result['TransitRouterRouteEntryNextHopId'] = self.transit_router_route_entry_next_hop_id
        if self.transit_router_route_entry_next_hop_type is not None:
            result['TransitRouterRouteEntryNextHopType'] = self.transit_router_route_entry_next_hop_type
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterRouteEntryDestinationCidrBlock') is not None:
            self.transit_router_route_entry_destination_cidr_block = m.get('TransitRouterRouteEntryDestinationCidrBlock')
        if m.get('TransitRouterRouteEntryId') is not None:
            self.transit_router_route_entry_id = m.get('TransitRouterRouteEntryId')
        if m.get('TransitRouterRouteEntryNextHopId') is not None:
            self.transit_router_route_entry_next_hop_id = m.get('TransitRouterRouteEntryNextHopId')
        if m.get('TransitRouterRouteEntryNextHopType') is not None:
            self.transit_router_route_entry_next_hop_type = m.get('TransitRouterRouteEntryNextHopType')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class DeleteTransitRouterRouteEntryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterRouteEntryResponseBody, self).to_map()
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


class DeleteTransitRouterRouteEntryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTransitRouterRouteEntryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTransitRouterRouteEntryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTransitRouterRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTransitRouterRouteTableRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_route_table_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterRouteTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class DeleteTransitRouterRouteTableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterRouteTableResponseBody, self).to_map()
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


class DeleteTransitRouterRouteTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTransitRouterRouteTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTransitRouterRouteTableResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTransitRouterRouteTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTransitRouterVbrAttachmentRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterVbrAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class DeleteTransitRouterVbrAttachmentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterVbrAttachmentResponseBody, self).to_map()
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


class DeleteTransitRouterVbrAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTransitRouterVbrAttachmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTransitRouterVbrAttachmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTransitRouterVbrAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTransitRouterVpcAttachmentRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterVpcAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class DeleteTransitRouterVpcAttachmentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterVpcAttachmentResponseBody, self).to_map()
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


class DeleteTransitRouterVpcAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTransitRouterVpcAttachmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTransitRouterVpcAttachmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTransitRouterVpcAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTransitRouterVpnAttachmentRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterVpnAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class DeleteTransitRouterVpnAttachmentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTransitRouterVpnAttachmentResponseBody, self).to_map()
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


class DeleteTransitRouterVpnAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTransitRouterVpnAttachmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTransitRouterVpnAttachmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTransitRouterVpnAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeregisterTransitRouterMulticastGroupMembersRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, group_ip_address=None, network_interface_ids=None,
                 owner_account=None, owner_id=None, peer_transit_router_multicast_domains=None, resource_owner_account=None,
                 resource_owner_id=None, transit_router_multicast_domain_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.group_ip_address = group_ip_address  # type: str
        self.network_interface_ids = network_interface_ids  # type: list[str]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.peer_transit_router_multicast_domains = peer_transit_router_multicast_domains  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterTransitRouterMulticastGroupMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.group_ip_address is not None:
            result['GroupIpAddress'] = self.group_ip_address
        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.peer_transit_router_multicast_domains is not None:
            result['PeerTransitRouterMulticastDomains'] = self.peer_transit_router_multicast_domains
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GroupIpAddress') is not None:
            self.group_ip_address = m.get('GroupIpAddress')
        if m.get('NetworkInterfaceIds') is not None:
            self.network_interface_ids = m.get('NetworkInterfaceIds')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PeerTransitRouterMulticastDomains') is not None:
            self.peer_transit_router_multicast_domains = m.get('PeerTransitRouterMulticastDomains')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        return self


class DeregisterTransitRouterMulticastGroupMembersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterTransitRouterMulticastGroupMembersResponseBody, self).to_map()
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


class DeregisterTransitRouterMulticastGroupMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeregisterTransitRouterMulticastGroupMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeregisterTransitRouterMulticastGroupMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeregisterTransitRouterMulticastGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeregisterTransitRouterMulticastGroupSourcesRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, group_ip_address=None, network_interface_ids=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 transit_router_multicast_domain_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.group_ip_address = group_ip_address  # type: str
        self.network_interface_ids = network_interface_ids  # type: list[str]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterTransitRouterMulticastGroupSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.group_ip_address is not None:
            result['GroupIpAddress'] = self.group_ip_address
        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GroupIpAddress') is not None:
            self.group_ip_address = m.get('GroupIpAddress')
        if m.get('NetworkInterfaceIds') is not None:
            self.network_interface_ids = m.get('NetworkInterfaceIds')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        return self


class DeregisterTransitRouterMulticastGroupSourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterTransitRouterMulticastGroupSourcesResponseBody, self).to_map()
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


class DeregisterTransitRouterMulticastGroupSourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeregisterTransitRouterMulticastGroupSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeregisterTransitRouterMulticastGroupSourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeregisterTransitRouterMulticastGroupSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenAttachedChildInstanceAttributeRequest(TeaModel):
    def __init__(self, cen_id=None, child_instance_id=None, child_instance_region_id=None,
                 child_instance_type=None, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenAttachedChildInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeCenAttachedChildInstanceAttributeResponseBody(TeaModel):
    def __init__(self, cen_id=None, child_instance_attach_time=None, child_instance_id=None,
                 child_instance_name=None, child_instance_owner_id=None, child_instance_region_id=None, child_instance_type=None,
                 request_id=None, status=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_attach_time = child_instance_attach_time  # type: str
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_name = child_instance_name  # type: str
        self.child_instance_owner_id = child_instance_owner_id  # type: long
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenAttachedChildInstanceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_attach_time is not None:
            result['ChildInstanceAttachTime'] = self.child_instance_attach_time
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_name is not None:
            result['ChildInstanceName'] = self.child_instance_name
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceAttachTime') is not None:
            self.child_instance_attach_time = m.get('ChildInstanceAttachTime')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceName') is not None:
            self.child_instance_name = m.get('ChildInstanceName')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCenAttachedChildInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenAttachedChildInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenAttachedChildInstanceAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenAttachedChildInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenAttachedChildInstancesRequest(TeaModel):
    def __init__(self, cen_id=None, child_instance_region_id=None, child_instance_type=None, owner_account=None,
                 owner_id=None, page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenAttachedChildInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeCenAttachedChildInstancesResponseBodyChildInstancesChildInstance(TeaModel):
    def __init__(self, cen_id=None, child_instance_attach_time=None, child_instance_id=None,
                 child_instance_owner_id=None, child_instance_region_id=None, child_instance_type=None, status=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_attach_time = child_instance_attach_time  # type: str
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_owner_id = child_instance_owner_id  # type: long
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenAttachedChildInstancesResponseBodyChildInstancesChildInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_attach_time is not None:
            result['ChildInstanceAttachTime'] = self.child_instance_attach_time
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceAttachTime') is not None:
            self.child_instance_attach_time = m.get('ChildInstanceAttachTime')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCenAttachedChildInstancesResponseBodyChildInstances(TeaModel):
    def __init__(self, child_instance=None):
        self.child_instance = child_instance  # type: list[DescribeCenAttachedChildInstancesResponseBodyChildInstancesChildInstance]

    def validate(self):
        if self.child_instance:
            for k in self.child_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenAttachedChildInstancesResponseBodyChildInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChildInstance'] = []
        if self.child_instance is not None:
            for k in self.child_instance:
                result['ChildInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.child_instance = []
        if m.get('ChildInstance') is not None:
            for k in m.get('ChildInstance'):
                temp_model = DescribeCenAttachedChildInstancesResponseBodyChildInstancesChildInstance()
                self.child_instance.append(temp_model.from_map(k))
        return self


class DescribeCenAttachedChildInstancesResponseBody(TeaModel):
    def __init__(self, child_instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.child_instances = child_instances  # type: DescribeCenAttachedChildInstancesResponseBodyChildInstances
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.child_instances:
            self.child_instances.validate()

    def to_map(self):
        _map = super(DescribeCenAttachedChildInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_instances is not None:
            result['ChildInstances'] = self.child_instances.to_map()
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
        if m.get('ChildInstances') is not None:
            temp_model = DescribeCenAttachedChildInstancesResponseBodyChildInstances()
            self.child_instances = temp_model.from_map(m['ChildInstances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCenAttachedChildInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenAttachedChildInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenAttachedChildInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenAttachedChildInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenBandwidthPackagesRequestFilter(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenBandwidthPackagesRequestFilter, self).to_map()
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


class DescribeCenBandwidthPackagesRequest(TeaModel):
    def __init__(self, filter=None, include_reservation_data=None, is_or_key=None, owner_account=None,
                 owner_id=None, page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None):
        self.filter = filter  # type: list[DescribeCenBandwidthPackagesRequestFilter]
        self.include_reservation_data = include_reservation_data  # type: bool
        self.is_or_key = is_or_key  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenBandwidthPackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.include_reservation_data is not None:
            result['IncludeReservationData'] = self.include_reservation_data
        if self.is_or_key is not None:
            result['IsOrKey'] = self.is_or_key
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeCenBandwidthPackagesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('IncludeReservationData') is not None:
            self.include_reservation_data = m.get('IncludeReservationData')
        if m.get('IsOrKey') is not None:
            self.is_or_key = m.get('IsOrKey')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageCenIds(TeaModel):
    def __init__(self, cen_id=None):
        self.cen_id = cen_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageCenIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimitsOrginInterRegionBandwidthLimit(TeaModel):
    def __init__(self, bandwidth_limit=None, geographic_span_id=None, local_region_id=None,
                 opposite_region_id=None):
        self.bandwidth_limit = bandwidth_limit  # type: str
        self.geographic_span_id = geographic_span_id  # type: str
        self.local_region_id = local_region_id  # type: str
        self.opposite_region_id = opposite_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimitsOrginInterRegionBandwidthLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id
        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')
        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimits(TeaModel):
    def __init__(self, orgin_inter_region_bandwidth_limit=None):
        self.orgin_inter_region_bandwidth_limit = orgin_inter_region_bandwidth_limit  # type: list[DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimitsOrginInterRegionBandwidthLimit]

    def validate(self):
        if self.orgin_inter_region_bandwidth_limit:
            for k in self.orgin_inter_region_bandwidth_limit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrginInterRegionBandwidthLimit'] = []
        if self.orgin_inter_region_bandwidth_limit is not None:
            for k in self.orgin_inter_region_bandwidth_limit:
                result['OrginInterRegionBandwidthLimit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.orgin_inter_region_bandwidth_limit = []
        if m.get('OrginInterRegionBandwidthLimit') is not None:
            for k in m.get('OrginInterRegionBandwidthLimit'):
                temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimitsOrginInterRegionBandwidthLimit()
                self.orgin_inter_region_bandwidth_limit.append(temp_model.from_map(k))
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, bandwidth_package_charge_type=None, business_status=None,
                 cen_bandwidth_package_id=None, cen_ids=None, creation_time=None, description=None, expired_time=None,
                 geographic_region_aid=None, geographic_region_bid=None, geographic_span_id=None, has_reservation_data=None,
                 is_cross_border=None, name=None, orgin_inter_region_bandwidth_limits=None, reservation_active_time=None,
                 reservation_bandwidth=None, reservation_internet_charge_type=None, reservation_order_type=None, service_type=None,
                 status=None):
        self.bandwidth = bandwidth  # type: long
        self.bandwidth_package_charge_type = bandwidth_package_charge_type  # type: str
        self.business_status = business_status  # type: str
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.cen_ids = cen_ids  # type: DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageCenIds
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.expired_time = expired_time  # type: str
        self.geographic_region_aid = geographic_region_aid  # type: str
        self.geographic_region_bid = geographic_region_bid  # type: str
        self.geographic_span_id = geographic_span_id  # type: str
        self.has_reservation_data = has_reservation_data  # type: str
        self.is_cross_border = is_cross_border  # type: bool
        self.name = name  # type: str
        self.orgin_inter_region_bandwidth_limits = orgin_inter_region_bandwidth_limits  # type: DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimits
        self.reservation_active_time = reservation_active_time  # type: str
        self.reservation_bandwidth = reservation_bandwidth  # type: str
        self.reservation_internet_charge_type = reservation_internet_charge_type  # type: str
        self.reservation_order_type = reservation_order_type  # type: str
        self.service_type = service_type  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.cen_ids:
            self.cen_ids.validate()
        if self.orgin_inter_region_bandwidth_limits:
            self.orgin_inter_region_bandwidth_limits.validate()

    def to_map(self):
        _map = super(DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package_charge_type is not None:
            result['BandwidthPackageChargeType'] = self.bandwidth_package_charge_type
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.cen_ids is not None:
            result['CenIds'] = self.cen_ids.to_map()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.geographic_region_aid is not None:
            result['GeographicRegionAId'] = self.geographic_region_aid
        if self.geographic_region_bid is not None:
            result['GeographicRegionBId'] = self.geographic_region_bid
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.has_reservation_data is not None:
            result['HasReservationData'] = self.has_reservation_data
        if self.is_cross_border is not None:
            result['IsCrossBorder'] = self.is_cross_border
        if self.name is not None:
            result['Name'] = self.name
        if self.orgin_inter_region_bandwidth_limits is not None:
            result['OrginInterRegionBandwidthLimits'] = self.orgin_inter_region_bandwidth_limits.to_map()
        if self.reservation_active_time is not None:
            result['ReservationActiveTime'] = self.reservation_active_time
        if self.reservation_bandwidth is not None:
            result['ReservationBandwidth'] = self.reservation_bandwidth
        if self.reservation_internet_charge_type is not None:
            result['ReservationInternetChargeType'] = self.reservation_internet_charge_type
        if self.reservation_order_type is not None:
            result['ReservationOrderType'] = self.reservation_order_type
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackageChargeType') is not None:
            self.bandwidth_package_charge_type = m.get('BandwidthPackageChargeType')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('CenIds') is not None:
            temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageCenIds()
            self.cen_ids = temp_model.from_map(m['CenIds'])
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GeographicRegionAId') is not None:
            self.geographic_region_aid = m.get('GeographicRegionAId')
        if m.get('GeographicRegionBId') is not None:
            self.geographic_region_bid = m.get('GeographicRegionBId')
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('HasReservationData') is not None:
            self.has_reservation_data = m.get('HasReservationData')
        if m.get('IsCrossBorder') is not None:
            self.is_cross_border = m.get('IsCrossBorder')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrginInterRegionBandwidthLimits') is not None:
            temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimits()
            self.orgin_inter_region_bandwidth_limits = temp_model.from_map(m['OrginInterRegionBandwidthLimits'])
        if m.get('ReservationActiveTime') is not None:
            self.reservation_active_time = m.get('ReservationActiveTime')
        if m.get('ReservationBandwidth') is not None:
            self.reservation_bandwidth = m.get('ReservationBandwidth')
        if m.get('ReservationInternetChargeType') is not None:
            self.reservation_internet_charge_type = m.get('ReservationInternetChargeType')
        if m.get('ReservationOrderType') is not None:
            self.reservation_order_type = m.get('ReservationOrderType')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages(TeaModel):
    def __init__(self, cen_bandwidth_package=None):
        self.cen_bandwidth_package = cen_bandwidth_package  # type: list[DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackage]

    def validate(self):
        if self.cen_bandwidth_package:
            for k in self.cen_bandwidth_package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenBandwidthPackage'] = []
        if self.cen_bandwidth_package is not None:
            for k in self.cen_bandwidth_package:
                result['CenBandwidthPackage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cen_bandwidth_package = []
        if m.get('CenBandwidthPackage') is not None:
            for k in m.get('CenBandwidthPackage'):
                temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackage()
                self.cen_bandwidth_package.append(temp_model.from_map(k))
        return self


class DescribeCenBandwidthPackagesResponseBody(TeaModel):
    def __init__(self, cen_bandwidth_packages=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.cen_bandwidth_packages = cen_bandwidth_packages  # type: DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.cen_bandwidth_packages:
            self.cen_bandwidth_packages.validate()

    def to_map(self):
        _map = super(DescribeCenBandwidthPackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_bandwidth_packages is not None:
            result['CenBandwidthPackages'] = self.cen_bandwidth_packages.to_map()
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
        if m.get('CenBandwidthPackages') is not None:
            temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages()
            self.cen_bandwidth_packages = temp_model.from_map(m['CenBandwidthPackages'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCenBandwidthPackagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenBandwidthPackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenBandwidthPackagesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenBandwidthPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenChildInstanceRouteEntriesRequest(TeaModel):
    def __init__(self, cen_id=None, child_instance_id=None, child_instance_region_id=None,
                 child_instance_type=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, status=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths(TeaModel):
    def __init__(self, as_path=None):
        self.as_path = as_path  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path is not None:
            result['AsPath'] = self.as_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord(TeaModel):
    def __init__(self, region_id=None, route_map_id=None):
        self.region_id = region_id  # type: str
        self.route_map_id = route_map_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords(TeaModel):
    def __init__(self, cen_route_map_record=None):
        self.cen_route_map_record = cen_route_map_record  # type: list[DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord]

    def validate(self):
        if self.cen_route_map_record:
            for k in self.cen_route_map_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenRouteMapRecord'] = []
        if self.cen_route_map_record is not None:
            for k in self.cen_route_map_record:
                result['CenRouteMapRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cen_route_map_record = []
        if m.get('CenRouteMapRecord') is not None:
            for k in m.get('CenRouteMapRecord'):
                temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord()
                self.cen_route_map_record.append(temp_model.from_map(k))
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities(TeaModel):
    def __init__(self, community=None):
        self.community = community  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.community is not None:
            result['Community'] = self.community
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Community') is not None:
            self.community = m.get('Community')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflictsConflict(TeaModel):
    def __init__(self, destination_cidr_block=None, instance_id=None, instance_type=None, region_id=None,
                 status=None):
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflictsConflict, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflicts(TeaModel):
    def __init__(self, conflict=None):
        self.conflict = conflict  # type: list[DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflictsConflict]

    def validate(self):
        if self.conflict:
            for k in self.conflict:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflicts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conflict'] = []
        if self.conflict is not None:
            for k in self.conflict:
                result['Conflict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.conflict = []
        if m.get('Conflict') is not None:
            for k in m.get('Conflict'):
                temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflictsConflict()
                self.conflict.append(temp_model.from_map(k))
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry(TeaModel):
    def __init__(self, as_paths=None, cen_route_map_records=None, communities=None, conflicts=None,
                 destination_cidr_block=None, next_hop_instance_id=None, next_hop_region_id=None, next_hop_type=None,
                 operational_mode=None, publish_status=None, route_table_id=None, status=None, type=None):
        self.as_paths = as_paths  # type: DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths
        self.cen_route_map_records = cen_route_map_records  # type: DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords
        self.communities = communities  # type: DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities
        self.conflicts = conflicts  # type: DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflicts
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.next_hop_instance_id = next_hop_instance_id  # type: str
        self.next_hop_region_id = next_hop_region_id  # type: str
        self.next_hop_type = next_hop_type  # type: str
        self.operational_mode = operational_mode  # type: bool
        self.publish_status = publish_status  # type: str
        self.route_table_id = route_table_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.as_paths:
            self.as_paths.validate()
        if self.cen_route_map_records:
            self.cen_route_map_records.validate()
        if self.communities:
            self.communities.validate()
        if self.conflicts:
            self.conflicts.validate()

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_paths is not None:
            result['AsPaths'] = self.as_paths.to_map()
        if self.cen_route_map_records is not None:
            result['CenRouteMapRecords'] = self.cen_route_map_records.to_map()
        if self.communities is not None:
            result['Communities'] = self.communities.to_map()
        if self.conflicts is not None:
            result['Conflicts'] = self.conflicts.to_map()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        if self.next_hop_region_id is not None:
            result['NextHopRegionId'] = self.next_hop_region_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.operational_mode is not None:
            result['OperationalMode'] = self.operational_mode
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsPaths') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths()
            self.as_paths = temp_model.from_map(m['AsPaths'])
        if m.get('CenRouteMapRecords') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords()
            self.cen_route_map_records = temp_model.from_map(m['CenRouteMapRecords'])
        if m.get('Communities') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities()
            self.communities = temp_model.from_map(m['Communities'])
        if m.get('Conflicts') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflicts()
            self.conflicts = temp_model.from_map(m['Conflicts'])
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        if m.get('NextHopRegionId') is not None:
            self.next_hop_region_id = m.get('NextHopRegionId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('OperationalMode') is not None:
            self.operational_mode = m.get('OperationalMode')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries(TeaModel):
    def __init__(self, cen_route_entry=None):
        self.cen_route_entry = cen_route_entry  # type: list[DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry]

    def validate(self):
        if self.cen_route_entry:
            for k in self.cen_route_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenRouteEntry'] = []
        if self.cen_route_entry is not None:
            for k in self.cen_route_entry:
                result['CenRouteEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cen_route_entry = []
        if m.get('CenRouteEntry') is not None:
            for k in m.get('CenRouteEntry'):
                temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry()
                self.cen_route_entry.append(temp_model.from_map(k))
        return self


class DescribeCenChildInstanceRouteEntriesResponseBody(TeaModel):
    def __init__(self, cen_route_entries=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.cen_route_entries = cen_route_entries  # type: DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.cen_route_entries:
            self.cen_route_entries.validate()

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_route_entries is not None:
            result['CenRouteEntries'] = self.cen_route_entries.to_map()
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
        if m.get('CenRouteEntries') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries()
            self.cen_route_entries = temp_model.from_map(m['CenRouteEntries'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCenChildInstanceRouteEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenChildInstanceRouteEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenChildInstanceRouteEntriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenGeographicSpanRemainingBandwidthRequest(TeaModel):
    def __init__(self, cen_id=None, geographic_region_aid=None, geographic_region_bid=None, owner_account=None,
                 owner_id=None, page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.geographic_region_aid = geographic_region_aid  # type: str
        self.geographic_region_bid = geographic_region_bid  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenGeographicSpanRemainingBandwidthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.geographic_region_aid is not None:
            result['GeographicRegionAId'] = self.geographic_region_aid
        if self.geographic_region_bid is not None:
            result['GeographicRegionBId'] = self.geographic_region_bid
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('GeographicRegionAId') is not None:
            self.geographic_region_aid = m.get('GeographicRegionAId')
        if m.get('GeographicRegionBId') is not None:
            self.geographic_region_bid = m.get('GeographicRegionBId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeCenGeographicSpanRemainingBandwidthResponseBody(TeaModel):
    def __init__(self, remaining_bandwidth=None, request_id=None):
        self.remaining_bandwidth = remaining_bandwidth  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenGeographicSpanRemainingBandwidthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remaining_bandwidth is not None:
            result['RemainingBandwidth'] = self.remaining_bandwidth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RemainingBandwidth') is not None:
            self.remaining_bandwidth = m.get('RemainingBandwidth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCenGeographicSpanRemainingBandwidthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenGeographicSpanRemainingBandwidthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenGeographicSpanRemainingBandwidthResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenGeographicSpanRemainingBandwidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenGeographicSpansRequest(TeaModel):
    def __init__(self, geographic_span_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.geographic_span_id = geographic_span_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenGeographicSpansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeCenGeographicSpansResponseBodyGeographicSpanModelsGeographicSpanModel(TeaModel):
    def __init__(self, geographic_span_id=None, local_geo_region_id=None, opposite_geo_region_id=None):
        self.geographic_span_id = geographic_span_id  # type: str
        self.local_geo_region_id = local_geo_region_id  # type: str
        self.opposite_geo_region_id = opposite_geo_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenGeographicSpansResponseBodyGeographicSpanModelsGeographicSpanModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.local_geo_region_id is not None:
            result['LocalGeoRegionId'] = self.local_geo_region_id
        if self.opposite_geo_region_id is not None:
            result['OppositeGeoRegionId'] = self.opposite_geo_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('LocalGeoRegionId') is not None:
            self.local_geo_region_id = m.get('LocalGeoRegionId')
        if m.get('OppositeGeoRegionId') is not None:
            self.opposite_geo_region_id = m.get('OppositeGeoRegionId')
        return self


class DescribeCenGeographicSpansResponseBodyGeographicSpanModels(TeaModel):
    def __init__(self, geographic_span_model=None):
        self.geographic_span_model = geographic_span_model  # type: list[DescribeCenGeographicSpansResponseBodyGeographicSpanModelsGeographicSpanModel]

    def validate(self):
        if self.geographic_span_model:
            for k in self.geographic_span_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenGeographicSpansResponseBodyGeographicSpanModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GeographicSpanModel'] = []
        if self.geographic_span_model is not None:
            for k in self.geographic_span_model:
                result['GeographicSpanModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.geographic_span_model = []
        if m.get('GeographicSpanModel') is not None:
            for k in m.get('GeographicSpanModel'):
                temp_model = DescribeCenGeographicSpansResponseBodyGeographicSpanModelsGeographicSpanModel()
                self.geographic_span_model.append(temp_model.from_map(k))
        return self


class DescribeCenGeographicSpansResponseBody(TeaModel):
    def __init__(self, geographic_span_models=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.geographic_span_models = geographic_span_models  # type: DescribeCenGeographicSpansResponseBodyGeographicSpanModels
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.geographic_span_models:
            self.geographic_span_models.validate()

    def to_map(self):
        _map = super(DescribeCenGeographicSpansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.geographic_span_models is not None:
            result['GeographicSpanModels'] = self.geographic_span_models.to_map()
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
        if m.get('GeographicSpanModels') is not None:
            temp_model = DescribeCenGeographicSpansResponseBodyGeographicSpanModels()
            self.geographic_span_models = temp_model.from_map(m['GeographicSpanModels'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCenGeographicSpansResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenGeographicSpansResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenGeographicSpansResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenGeographicSpansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenInterRegionBandwidthLimitsRequest(TeaModel):
    def __init__(self, cen_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenInterRegionBandwidthLimitsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimitsCenInterRegionBandwidthLimit(TeaModel):
    def __init__(self, bandwidth_limit=None, bandwidth_package_id=None, cen_id=None, geographic_span_id=None,
                 local_region_id=None, opposite_region_id=None, status=None):
        self.bandwidth_limit = bandwidth_limit  # type: long
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.cen_id = cen_id  # type: str
        self.geographic_span_id = geographic_span_id  # type: str
        self.local_region_id = local_region_id  # type: str
        self.opposite_region_id = opposite_region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimitsCenInterRegionBandwidthLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id
        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')
        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits(TeaModel):
    def __init__(self, cen_inter_region_bandwidth_limit=None):
        self.cen_inter_region_bandwidth_limit = cen_inter_region_bandwidth_limit  # type: list[DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimitsCenInterRegionBandwidthLimit]

    def validate(self):
        if self.cen_inter_region_bandwidth_limit:
            for k in self.cen_inter_region_bandwidth_limit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenInterRegionBandwidthLimit'] = []
        if self.cen_inter_region_bandwidth_limit is not None:
            for k in self.cen_inter_region_bandwidth_limit:
                result['CenInterRegionBandwidthLimit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cen_inter_region_bandwidth_limit = []
        if m.get('CenInterRegionBandwidthLimit') is not None:
            for k in m.get('CenInterRegionBandwidthLimit'):
                temp_model = DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimitsCenInterRegionBandwidthLimit()
                self.cen_inter_region_bandwidth_limit.append(temp_model.from_map(k))
        return self


class DescribeCenInterRegionBandwidthLimitsResponseBody(TeaModel):
    def __init__(self, cen_inter_region_bandwidth_limits=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.cen_inter_region_bandwidth_limits = cen_inter_region_bandwidth_limits  # type: DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.cen_inter_region_bandwidth_limits:
            self.cen_inter_region_bandwidth_limits.validate()

    def to_map(self):
        _map = super(DescribeCenInterRegionBandwidthLimitsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_inter_region_bandwidth_limits is not None:
            result['CenInterRegionBandwidthLimits'] = self.cen_inter_region_bandwidth_limits.to_map()
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
        if m.get('CenInterRegionBandwidthLimits') is not None:
            temp_model = DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits()
            self.cen_inter_region_bandwidth_limits = temp_model.from_map(m['CenInterRegionBandwidthLimits'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCenInterRegionBandwidthLimitsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenInterRegionBandwidthLimitsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenInterRegionBandwidthLimitsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenInterRegionBandwidthLimitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenPrivateZoneRoutesRequest(TeaModel):
    def __init__(self, access_region_id=None, cen_id=None, host_region_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.access_region_id = access_region_id  # type: str
        self.cen_id = cen_id  # type: str
        self.host_region_id = host_region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenPrivateZoneRoutesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfosPrivateZoneInfo(TeaModel):
    def __init__(self, access_region_id=None, host_region_id=None, host_vpc_id=None, status=None):
        self.access_region_id = access_region_id  # type: str
        self.host_region_id = host_region_id  # type: str
        self.host_vpc_id = host_vpc_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfosPrivateZoneInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos(TeaModel):
    def __init__(self, private_zone_info=None):
        self.private_zone_info = private_zone_info  # type: list[DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfosPrivateZoneInfo]

    def validate(self):
        if self.private_zone_info:
            for k in self.private_zone_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrivateZoneInfo'] = []
        if self.private_zone_info is not None:
            for k in self.private_zone_info:
                result['PrivateZoneInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.private_zone_info = []
        if m.get('PrivateZoneInfo') is not None:
            for k in m.get('PrivateZoneInfo'):
                temp_model = DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfosPrivateZoneInfo()
                self.private_zone_info.append(temp_model.from_map(k))
        return self


class DescribeCenPrivateZoneRoutesResponseBody(TeaModel):
    def __init__(self, cen_id=None, page_number=None, page_size=None, private_zone_dns_servers=None,
                 private_zone_infos=None, request_id=None, total_count=None):
        self.cen_id = cen_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.private_zone_dns_servers = private_zone_dns_servers  # type: str
        self.private_zone_infos = private_zone_infos  # type: DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.private_zone_infos:
            self.private_zone_infos.validate()

    def to_map(self):
        _map = super(DescribeCenPrivateZoneRoutesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.private_zone_dns_servers is not None:
            result['PrivateZoneDnsServers'] = self.private_zone_dns_servers
        if self.private_zone_infos is not None:
            result['PrivateZoneInfos'] = self.private_zone_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrivateZoneDnsServers') is not None:
            self.private_zone_dns_servers = m.get('PrivateZoneDnsServers')
        if m.get('PrivateZoneInfos') is not None:
            temp_model = DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos()
            self.private_zone_infos = temp_model.from_map(m['PrivateZoneInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCenPrivateZoneRoutesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenPrivateZoneRoutesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenPrivateZoneRoutesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenPrivateZoneRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenRegionDomainRouteEntriesRequest(TeaModel):
    def __init__(self, cen_id=None, cen_region_id=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None, status=None):
        self.cen_id = cen_id  # type: str
        self.cen_region_id = cen_region_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths(TeaModel):
    def __init__(self, as_path=None):
        self.as_path = as_path  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path is not None:
            result['AsPath'] = self.as_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecordsCenOutRouteMapRecord(TeaModel):
    def __init__(self, region_id=None, route_map_id=None):
        self.region_id = region_id  # type: str
        self.route_map_id = route_map_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecordsCenOutRouteMapRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecords(TeaModel):
    def __init__(self, cen_out_route_map_record=None):
        self.cen_out_route_map_record = cen_out_route_map_record  # type: list[DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecordsCenOutRouteMapRecord]

    def validate(self):
        if self.cen_out_route_map_record:
            for k in self.cen_out_route_map_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenOutRouteMapRecord'] = []
        if self.cen_out_route_map_record is not None:
            for k in self.cen_out_route_map_record:
                result['CenOutRouteMapRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cen_out_route_map_record = []
        if m.get('CenOutRouteMapRecord') is not None:
            for k in m.get('CenOutRouteMapRecord'):
                temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecordsCenOutRouteMapRecord()
                self.cen_out_route_map_record.append(temp_model.from_map(k))
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord(TeaModel):
    def __init__(self, region_id=None, route_map_id=None):
        self.region_id = region_id  # type: str
        self.route_map_id = route_map_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords(TeaModel):
    def __init__(self, cen_route_map_record=None):
        self.cen_route_map_record = cen_route_map_record  # type: list[DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord]

    def validate(self):
        if self.cen_route_map_record:
            for k in self.cen_route_map_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenRouteMapRecord'] = []
        if self.cen_route_map_record is not None:
            for k in self.cen_route_map_record:
                result['CenRouteMapRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cen_route_map_record = []
        if m.get('CenRouteMapRecord') is not None:
            for k in m.get('CenRouteMapRecord'):
                temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord()
                self.cen_route_map_record.append(temp_model.from_map(k))
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities(TeaModel):
    def __init__(self, community=None):
        self.community = community  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.community is not None:
            result['Community'] = self.community
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Community') is not None:
            self.community = m.get('Community')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry(TeaModel):
    def __init__(self, as_paths=None, cen_out_route_map_records=None, cen_route_map_records=None, communities=None,
                 destination_cidr_block=None, next_hop_instance_id=None, next_hop_region_id=None, next_hop_type=None, preference=None,
                 status=None, to_other_region_status=None, type=None):
        self.as_paths = as_paths  # type: DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths
        self.cen_out_route_map_records = cen_out_route_map_records  # type: DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecords
        self.cen_route_map_records = cen_route_map_records  # type: DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords
        self.communities = communities  # type: DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.next_hop_instance_id = next_hop_instance_id  # type: str
        self.next_hop_region_id = next_hop_region_id  # type: str
        self.next_hop_type = next_hop_type  # type: str
        self.preference = preference  # type: int
        self.status = status  # type: str
        self.to_other_region_status = to_other_region_status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.as_paths:
            self.as_paths.validate()
        if self.cen_out_route_map_records:
            self.cen_out_route_map_records.validate()
        if self.cen_route_map_records:
            self.cen_route_map_records.validate()
        if self.communities:
            self.communities.validate()

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_paths is not None:
            result['AsPaths'] = self.as_paths.to_map()
        if self.cen_out_route_map_records is not None:
            result['CenOutRouteMapRecords'] = self.cen_out_route_map_records.to_map()
        if self.cen_route_map_records is not None:
            result['CenRouteMapRecords'] = self.cen_route_map_records.to_map()
        if self.communities is not None:
            result['Communities'] = self.communities.to_map()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        if self.next_hop_region_id is not None:
            result['NextHopRegionId'] = self.next_hop_region_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.preference is not None:
            result['Preference'] = self.preference
        if self.status is not None:
            result['Status'] = self.status
        if self.to_other_region_status is not None:
            result['ToOtherRegionStatus'] = self.to_other_region_status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsPaths') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths()
            self.as_paths = temp_model.from_map(m['AsPaths'])
        if m.get('CenOutRouteMapRecords') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecords()
            self.cen_out_route_map_records = temp_model.from_map(m['CenOutRouteMapRecords'])
        if m.get('CenRouteMapRecords') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords()
            self.cen_route_map_records = temp_model.from_map(m['CenRouteMapRecords'])
        if m.get('Communities') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities()
            self.communities = temp_model.from_map(m['Communities'])
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        if m.get('NextHopRegionId') is not None:
            self.next_hop_region_id = m.get('NextHopRegionId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('Preference') is not None:
            self.preference = m.get('Preference')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToOtherRegionStatus') is not None:
            self.to_other_region_status = m.get('ToOtherRegionStatus')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries(TeaModel):
    def __init__(self, cen_route_entry=None):
        self.cen_route_entry = cen_route_entry  # type: list[DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry]

    def validate(self):
        if self.cen_route_entry:
            for k in self.cen_route_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenRouteEntry'] = []
        if self.cen_route_entry is not None:
            for k in self.cen_route_entry:
                result['CenRouteEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cen_route_entry = []
        if m.get('CenRouteEntry') is not None:
            for k in m.get('CenRouteEntry'):
                temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry()
                self.cen_route_entry.append(temp_model.from_map(k))
        return self


class DescribeCenRegionDomainRouteEntriesResponseBody(TeaModel):
    def __init__(self, cen_route_entries=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.cen_route_entries = cen_route_entries  # type: DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.cen_route_entries:
            self.cen_route_entries.validate()

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_route_entries is not None:
            result['CenRouteEntries'] = self.cen_route_entries.to_map()
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
        if m.get('CenRouteEntries') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries()
            self.cen_route_entries = temp_model.from_map(m['CenRouteEntries'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCenRegionDomainRouteEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenRegionDomainRouteEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenRegionDomainRouteEntriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenRouteMapsRequest(TeaModel):
    def __init__(self, cen_id=None, cen_region_id=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None, route_map_id=None,
                 transit_router_route_table_id=None, transmit_direction=None):
        self.cen_id = cen_id  # type: str
        self.cen_region_id = cen_region_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.route_map_id = route_map_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str
        self.transmit_direction = transmit_direction  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        if self.transmit_direction is not None:
            result['TransmitDirection'] = self.transmit_direction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        if m.get('TransmitDirection') is not None:
            self.transmit_direction = m.get('TransmitDirection')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationChildInstanceTypes(TeaModel):
    def __init__(self, destination_child_instance_type=None):
        self.destination_child_instance_type = destination_child_instance_type  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationChildInstanceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_child_instance_type is not None:
            result['DestinationChildInstanceType'] = self.destination_child_instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationChildInstanceType') is not None:
            self.destination_child_instance_type = m.get('DestinationChildInstanceType')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationCidrBlocks(TeaModel):
    def __init__(self, destination_cidr_block=None):
        self.destination_cidr_block = destination_cidr_block  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationCidrBlocks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationInstanceIds(TeaModel):
    def __init__(self, destination_instance_id=None):
        self.destination_instance_id = destination_instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationInstanceIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_instance_id is not None:
            result['DestinationInstanceId'] = self.destination_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationInstanceId') is not None:
            self.destination_instance_id = m.get('DestinationInstanceId')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRouteTableIds(TeaModel):
    def __init__(self, destination_route_table_id=None):
        self.destination_route_table_id = destination_route_table_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRouteTableIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_route_table_id is not None:
            result['DestinationRouteTableId'] = self.destination_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationRouteTableId') is not None:
            self.destination_route_table_id = m.get('DestinationRouteTableId')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchAsns(TeaModel):
    def __init__(self, match_asn=None):
        self.match_asn = match_asn  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchAsns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_asn is not None:
            result['MatchAsn'] = self.match_asn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchAsn') is not None:
            self.match_asn = m.get('MatchAsn')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchCommunitySet(TeaModel):
    def __init__(self, match_community=None):
        self.match_community = match_community  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchCommunitySet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_community is not None:
            result['MatchCommunity'] = self.match_community
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchCommunity') is not None:
            self.match_community = m.get('MatchCommunity')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapOperateCommunitySet(TeaModel):
    def __init__(self, operate_community=None):
        self.operate_community = operate_community  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapOperateCommunitySet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_community is not None:
            result['OperateCommunity'] = self.operate_community
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperateCommunity') is not None:
            self.operate_community = m.get('OperateCommunity')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapPrependAsPath(TeaModel):
    def __init__(self, as_path=None):
        self.as_path = as_path  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapPrependAsPath, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path is not None:
            result['AsPath'] = self.as_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapRouteTypes(TeaModel):
    def __init__(self, route_type=None):
        self.route_type = route_type  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapRouteTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceChildInstanceTypes(TeaModel):
    def __init__(self, source_child_instance_type=None):
        self.source_child_instance_type = source_child_instance_type  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceChildInstanceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_child_instance_type is not None:
            result['SourceChildInstanceType'] = self.source_child_instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceChildInstanceType') is not None:
            self.source_child_instance_type = m.get('SourceChildInstanceType')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceInstanceIds(TeaModel):
    def __init__(self, source_instance_id=None):
        self.source_instance_id = source_instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceInstanceIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRegionIds(TeaModel):
    def __init__(self, source_region_id=None):
        self.source_region_id = source_region_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRegionIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRouteTableIds(TeaModel):
    def __init__(self, source_route_table_id=None):
        self.source_route_table_id = source_route_table_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRouteTableIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_route_table_id is not None:
            result['SourceRouteTableId'] = self.source_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceRouteTableId') is not None:
            self.source_route_table_id = m.get('SourceRouteTableId')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMap(TeaModel):
    def __init__(self, as_path_match_mode=None, cen_id=None, cen_region_id=None, cidr_match_mode=None,
                 community_match_mode=None, community_operate_mode=None, description=None, destination_child_instance_types=None,
                 destination_cidr_blocks=None, destination_instance_ids=None, destination_instance_ids_reverse_match=None,
                 destination_route_table_ids=None, map_result=None, match_address_type=None, match_asns=None, match_community_set=None,
                 next_priority=None, operate_community_set=None, preference=None, prepend_as_path=None, priority=None,
                 route_map_id=None, route_types=None, source_child_instance_types=None, source_instance_ids=None,
                 source_instance_ids_reverse_match=None, source_region_ids=None, source_route_table_ids=None, status=None,
                 transit_router_route_table_id=None, transmit_direction=None):
        self.as_path_match_mode = as_path_match_mode  # type: str
        self.cen_id = cen_id  # type: str
        self.cen_region_id = cen_region_id  # type: str
        self.cidr_match_mode = cidr_match_mode  # type: str
        self.community_match_mode = community_match_mode  # type: str
        self.community_operate_mode = community_operate_mode  # type: str
        self.description = description  # type: str
        self.destination_child_instance_types = destination_child_instance_types  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationChildInstanceTypes
        self.destination_cidr_blocks = destination_cidr_blocks  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationCidrBlocks
        self.destination_instance_ids = destination_instance_ids  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationInstanceIds
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match  # type: bool
        self.destination_route_table_ids = destination_route_table_ids  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRouteTableIds
        self.map_result = map_result  # type: str
        self.match_address_type = match_address_type  # type: str
        self.match_asns = match_asns  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchAsns
        self.match_community_set = match_community_set  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchCommunitySet
        self.next_priority = next_priority  # type: int
        self.operate_community_set = operate_community_set  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapOperateCommunitySet
        self.preference = preference  # type: int
        self.prepend_as_path = prepend_as_path  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapPrependAsPath
        self.priority = priority  # type: int
        self.route_map_id = route_map_id  # type: str
        self.route_types = route_types  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapRouteTypes
        self.source_child_instance_types = source_child_instance_types  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceChildInstanceTypes
        self.source_instance_ids = source_instance_ids  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceInstanceIds
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match  # type: bool
        self.source_region_ids = source_region_ids  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRegionIds
        self.source_route_table_ids = source_route_table_ids  # type: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRouteTableIds
        self.status = status  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str
        self.transmit_direction = transmit_direction  # type: str

    def validate(self):
        if self.destination_child_instance_types:
            self.destination_child_instance_types.validate()
        if self.destination_cidr_blocks:
            self.destination_cidr_blocks.validate()
        if self.destination_instance_ids:
            self.destination_instance_ids.validate()
        if self.destination_route_table_ids:
            self.destination_route_table_ids.validate()
        if self.match_asns:
            self.match_asns.validate()
        if self.match_community_set:
            self.match_community_set.validate()
        if self.operate_community_set:
            self.operate_community_set.validate()
        if self.prepend_as_path:
            self.prepend_as_path.validate()
        if self.route_types:
            self.route_types.validate()
        if self.source_child_instance_types:
            self.source_child_instance_types.validate()
        if self.source_instance_ids:
            self.source_instance_ids.validate()
        if self.source_region_ids:
            self.source_region_ids.validate()
        if self.source_route_table_ids:
            self.source_route_table_ids.validate()

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMapsRouteMap, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path_match_mode is not None:
            result['AsPathMatchMode'] = self.as_path_match_mode
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.cidr_match_mode is not None:
            result['CidrMatchMode'] = self.cidr_match_mode
        if self.community_match_mode is not None:
            result['CommunityMatchMode'] = self.community_match_mode
        if self.community_operate_mode is not None:
            result['CommunityOperateMode'] = self.community_operate_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_child_instance_types is not None:
            result['DestinationChildInstanceTypes'] = self.destination_child_instance_types.to_map()
        if self.destination_cidr_blocks is not None:
            result['DestinationCidrBlocks'] = self.destination_cidr_blocks.to_map()
        if self.destination_instance_ids is not None:
            result['DestinationInstanceIds'] = self.destination_instance_ids.to_map()
        if self.destination_instance_ids_reverse_match is not None:
            result['DestinationInstanceIdsReverseMatch'] = self.destination_instance_ids_reverse_match
        if self.destination_route_table_ids is not None:
            result['DestinationRouteTableIds'] = self.destination_route_table_ids.to_map()
        if self.map_result is not None:
            result['MapResult'] = self.map_result
        if self.match_address_type is not None:
            result['MatchAddressType'] = self.match_address_type
        if self.match_asns is not None:
            result['MatchAsns'] = self.match_asns.to_map()
        if self.match_community_set is not None:
            result['MatchCommunitySet'] = self.match_community_set.to_map()
        if self.next_priority is not None:
            result['NextPriority'] = self.next_priority
        if self.operate_community_set is not None:
            result['OperateCommunitySet'] = self.operate_community_set.to_map()
        if self.preference is not None:
            result['Preference'] = self.preference
        if self.prepend_as_path is not None:
            result['PrependAsPath'] = self.prepend_as_path.to_map()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.route_types is not None:
            result['RouteTypes'] = self.route_types.to_map()
        if self.source_child_instance_types is not None:
            result['SourceChildInstanceTypes'] = self.source_child_instance_types.to_map()
        if self.source_instance_ids is not None:
            result['SourceInstanceIds'] = self.source_instance_ids.to_map()
        if self.source_instance_ids_reverse_match is not None:
            result['SourceInstanceIdsReverseMatch'] = self.source_instance_ids_reverse_match
        if self.source_region_ids is not None:
            result['SourceRegionIds'] = self.source_region_ids.to_map()
        if self.source_route_table_ids is not None:
            result['SourceRouteTableIds'] = self.source_route_table_ids.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        if self.transmit_direction is not None:
            result['TransmitDirection'] = self.transmit_direction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsPathMatchMode') is not None:
            self.as_path_match_mode = m.get('AsPathMatchMode')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('CidrMatchMode') is not None:
            self.cidr_match_mode = m.get('CidrMatchMode')
        if m.get('CommunityMatchMode') is not None:
            self.community_match_mode = m.get('CommunityMatchMode')
        if m.get('CommunityOperateMode') is not None:
            self.community_operate_mode = m.get('CommunityOperateMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationChildInstanceTypes') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationChildInstanceTypes()
            self.destination_child_instance_types = temp_model.from_map(m['DestinationChildInstanceTypes'])
        if m.get('DestinationCidrBlocks') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationCidrBlocks()
            self.destination_cidr_blocks = temp_model.from_map(m['DestinationCidrBlocks'])
        if m.get('DestinationInstanceIds') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationInstanceIds()
            self.destination_instance_ids = temp_model.from_map(m['DestinationInstanceIds'])
        if m.get('DestinationInstanceIdsReverseMatch') is not None:
            self.destination_instance_ids_reverse_match = m.get('DestinationInstanceIdsReverseMatch')
        if m.get('DestinationRouteTableIds') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRouteTableIds()
            self.destination_route_table_ids = temp_model.from_map(m['DestinationRouteTableIds'])
        if m.get('MapResult') is not None:
            self.map_result = m.get('MapResult')
        if m.get('MatchAddressType') is not None:
            self.match_address_type = m.get('MatchAddressType')
        if m.get('MatchAsns') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchAsns()
            self.match_asns = temp_model.from_map(m['MatchAsns'])
        if m.get('MatchCommunitySet') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchCommunitySet()
            self.match_community_set = temp_model.from_map(m['MatchCommunitySet'])
        if m.get('NextPriority') is not None:
            self.next_priority = m.get('NextPriority')
        if m.get('OperateCommunitySet') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapOperateCommunitySet()
            self.operate_community_set = temp_model.from_map(m['OperateCommunitySet'])
        if m.get('Preference') is not None:
            self.preference = m.get('Preference')
        if m.get('PrependAsPath') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapPrependAsPath()
            self.prepend_as_path = temp_model.from_map(m['PrependAsPath'])
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('RouteTypes') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapRouteTypes()
            self.route_types = temp_model.from_map(m['RouteTypes'])
        if m.get('SourceChildInstanceTypes') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceChildInstanceTypes()
            self.source_child_instance_types = temp_model.from_map(m['SourceChildInstanceTypes'])
        if m.get('SourceInstanceIds') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceInstanceIds()
            self.source_instance_ids = temp_model.from_map(m['SourceInstanceIds'])
        if m.get('SourceInstanceIdsReverseMatch') is not None:
            self.source_instance_ids_reverse_match = m.get('SourceInstanceIdsReverseMatch')
        if m.get('SourceRegionIds') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRegionIds()
            self.source_region_ids = temp_model.from_map(m['SourceRegionIds'])
        if m.get('SourceRouteTableIds') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRouteTableIds()
            self.source_route_table_ids = temp_model.from_map(m['SourceRouteTableIds'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        if m.get('TransmitDirection') is not None:
            self.transmit_direction = m.get('TransmitDirection')
        return self


class DescribeCenRouteMapsResponseBodyRouteMaps(TeaModel):
    def __init__(self, route_map=None):
        self.route_map = route_map  # type: list[DescribeCenRouteMapsResponseBodyRouteMapsRouteMap]

    def validate(self):
        if self.route_map:
            for k in self.route_map:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBodyRouteMaps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteMap'] = []
        if self.route_map is not None:
            for k in self.route_map:
                result['RouteMap'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.route_map = []
        if m.get('RouteMap') is not None:
            for k in m.get('RouteMap'):
                temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMap()
                self.route_map.append(temp_model.from_map(k))
        return self


class DescribeCenRouteMapsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, route_maps=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.route_maps = route_maps  # type: DescribeCenRouteMapsResponseBodyRouteMaps
        self.total_count = total_count  # type: int

    def validate(self):
        if self.route_maps:
            self.route_maps.validate()

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps.to_map()
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
        if m.get('RouteMaps') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMaps()
            self.route_maps = temp_model.from_map(m['RouteMaps'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCenRouteMapsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenRouteMapsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenRouteMapsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenRouteMapsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenVbrHealthCheckRequest(TeaModel):
    def __init__(self, cen_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, vbr_instance_id=None, vbr_instance_owner_id=None,
                 vbr_instance_region_id=None):
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.vbr_instance_id = vbr_instance_id  # type: str
        self.vbr_instance_owner_id = vbr_instance_owner_id  # type: long
        self.vbr_instance_region_id = vbr_instance_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenVbrHealthCheckRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id
        if self.vbr_instance_owner_id is not None:
            result['VbrInstanceOwnerId'] = self.vbr_instance_owner_id
        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')
        if m.get('VbrInstanceOwnerId') is not None:
            self.vbr_instance_owner_id = m.get('VbrInstanceOwnerId')
        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')
        return self


class DescribeCenVbrHealthCheckResponseBodyVbrHealthChecksVbrHealthCheck(TeaModel):
    def __init__(self, cen_id=None, health_check_interval=None, health_check_only=None,
                 health_check_source_ip=None, health_check_target_ip=None, healthy_threshold=None, vbr_instance_id=None,
                 vbr_instance_region_id=None):
        self.cen_id = cen_id  # type: str
        self.health_check_interval = health_check_interval  # type: int
        self.health_check_only = health_check_only  # type: bool
        self.health_check_source_ip = health_check_source_ip  # type: str
        self.health_check_target_ip = health_check_target_ip  # type: str
        self.healthy_threshold = healthy_threshold  # type: int
        self.vbr_instance_id = vbr_instance_id  # type: str
        self.vbr_instance_region_id = vbr_instance_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenVbrHealthCheckResponseBodyVbrHealthChecksVbrHealthCheck, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_only is not None:
            result['HealthCheckOnly'] = self.health_check_only
        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip
        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id
        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckOnly') is not None:
            self.health_check_only = m.get('HealthCheckOnly')
        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')
        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')
        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')
        return self


class DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks(TeaModel):
    def __init__(self, vbr_health_check=None):
        self.vbr_health_check = vbr_health_check  # type: list[DescribeCenVbrHealthCheckResponseBodyVbrHealthChecksVbrHealthCheck]

    def validate(self):
        if self.vbr_health_check:
            for k in self.vbr_health_check:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VbrHealthCheck'] = []
        if self.vbr_health_check is not None:
            for k in self.vbr_health_check:
                result['VbrHealthCheck'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vbr_health_check = []
        if m.get('VbrHealthCheck') is not None:
            for k in m.get('VbrHealthCheck'):
                temp_model = DescribeCenVbrHealthCheckResponseBodyVbrHealthChecksVbrHealthCheck()
                self.vbr_health_check.append(temp_model.from_map(k))
        return self


class DescribeCenVbrHealthCheckResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, vbr_health_checks=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.vbr_health_checks = vbr_health_checks  # type: DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks

    def validate(self):
        if self.vbr_health_checks:
            self.vbr_health_checks.validate()

    def to_map(self):
        _map = super(DescribeCenVbrHealthCheckResponseBody, self).to_map()
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
        if self.vbr_health_checks is not None:
            result['VbrHealthChecks'] = self.vbr_health_checks.to_map()
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
        if m.get('VbrHealthChecks') is not None:
            temp_model = DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks()
            self.vbr_health_checks = temp_model.from_map(m['VbrHealthChecks'])
        return self


class DescribeCenVbrHealthCheckResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenVbrHealthCheckResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenVbrHealthCheckResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenVbrHealthCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenVpcFlowStatisticSwitchRequest(TeaModel):
    def __init__(self, cen_id=None, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenVpcFlowStatisticSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeCenVpcFlowStatisticSwitchResponseBody(TeaModel):
    def __init__(self, cen_id=None, invalid_date=None, region_id=None, request_id=None, state=None):
        self.cen_id = cen_id  # type: str
        self.invalid_date = invalid_date  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCenVpcFlowStatisticSwitchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.invalid_date is not None:
            result['InvalidDate'] = self.invalid_date
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('InvalidDate') is not None:
            self.invalid_date = m.get('InvalidDate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeCenVpcFlowStatisticSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCenVpcFlowStatisticSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCenVpcFlowStatisticSwitchResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCenVpcFlowStatisticSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCensRequestFilter(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCensRequestFilter, self).to_map()
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


class DescribeCensRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCensRequestTag, self).to_map()
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


class DescribeCensRequest(TeaModel):
    def __init__(self, filter=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, tag=None):
        self.filter = filter  # type: list[DescribeCensRequestFilter]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag = tag  # type: list[DescribeCensRequestTag]

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCensRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeCensRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeCensRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeCensResponseBodyCensCenCenBandwidthPackageIds(TeaModel):
    def __init__(self, cen_bandwidth_package_id=None):
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCensResponseBodyCensCenCenBandwidthPackageIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        return self


class DescribeCensResponseBodyCensCenTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCensResponseBodyCensCenTagsTag, self).to_map()
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


class DescribeCensResponseBodyCensCenTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeCensResponseBodyCensCenTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCensResponseBodyCensCenTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeCensResponseBodyCensCenTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeCensResponseBodyCensCen(TeaModel):
    def __init__(self, cen_bandwidth_package_ids=None, cen_id=None, creation_time=None, description=None,
                 ipv_6level=None, name=None, protection_level=None, resource_group_id=None, status=None, tags=None):
        self.cen_bandwidth_package_ids = cen_bandwidth_package_ids  # type: DescribeCensResponseBodyCensCenCenBandwidthPackageIds
        self.cen_id = cen_id  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.ipv_6level = ipv_6level  # type: str
        self.name = name  # type: str
        self.protection_level = protection_level  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: DescribeCensResponseBodyCensCenTags

    def validate(self):
        if self.cen_bandwidth_package_ids:
            self.cen_bandwidth_package_ids.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeCensResponseBodyCensCen, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_bandwidth_package_ids is not None:
            result['CenBandwidthPackageIds'] = self.cen_bandwidth_package_ids.to_map()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ipv_6level is not None:
            result['Ipv6Level'] = self.ipv_6level
        if self.name is not None:
            result['Name'] = self.name
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenBandwidthPackageIds') is not None:
            temp_model = DescribeCensResponseBodyCensCenCenBandwidthPackageIds()
            self.cen_bandwidth_package_ids = temp_model.from_map(m['CenBandwidthPackageIds'])
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Ipv6Level') is not None:
            self.ipv_6level = m.get('Ipv6Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeCensResponseBodyCensCenTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeCensResponseBodyCens(TeaModel):
    def __init__(self, cen=None):
        self.cen = cen  # type: list[DescribeCensResponseBodyCensCen]

    def validate(self):
        if self.cen:
            for k in self.cen:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCensResponseBodyCens, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cen'] = []
        if self.cen is not None:
            for k in self.cen:
                result['Cen'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cen = []
        if m.get('Cen') is not None:
            for k in m.get('Cen'):
                temp_model = DescribeCensResponseBodyCensCen()
                self.cen.append(temp_model.from_map(k))
        return self


class DescribeCensResponseBody(TeaModel):
    def __init__(self, cens=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.cens = cens  # type: DescribeCensResponseBodyCens
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.cens:
            self.cens.validate()

    def to_map(self):
        _map = super(DescribeCensResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cens is not None:
            result['Cens'] = self.cens.to_map()
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
        if m.get('Cens') is not None:
            temp_model = DescribeCensResponseBodyCens()
            self.cens = temp_model.from_map(m['Cens'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCensResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCensResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCensResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChildInstanceRegionsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, product_type=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.product_type = product_type  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChildInstanceRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeChildInstanceRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChildInstanceRegionsResponseBodyRegionsRegion, self).to_map()
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


class DescribeChildInstanceRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeChildInstanceRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeChildInstanceRegionsResponseBodyRegions, self).to_map()
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
                temp_model = DescribeChildInstanceRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeChildInstanceRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: DescribeChildInstanceRegionsResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeChildInstanceRegionsResponseBody, self).to_map()
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
            temp_model = DescribeChildInstanceRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeChildInstanceRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeChildInstanceRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeChildInstanceRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeChildInstanceRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowlogsRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, description=None, flow_log_id=None, flow_log_name=None,
                 log_store_name=None, owner_account=None, owner_id=None, page_number=None, page_size=None, project_name=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, status=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.flow_log_id = flow_log_id  # type: str
        self.flow_log_name = flow_log_name  # type: str
        self.log_store_name = log_store_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowlogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeFlowlogsResponseBodyFlowLogsFlowLog(TeaModel):
    def __init__(self, cen_id=None, creation_time=None, description=None, flow_log_id=None, flow_log_name=None,
                 log_store_name=None, project_name=None, region_id=None, status=None):
        self.cen_id = cen_id  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.flow_log_id = flow_log_id  # type: str
        self.flow_log_name = flow_log_name  # type: str
        self.log_store_name = log_store_name  # type: str
        self.project_name = project_name  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowlogsResponseBodyFlowLogsFlowLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeFlowlogsResponseBodyFlowLogs(TeaModel):
    def __init__(self, flow_log=None):
        self.flow_log = flow_log  # type: list[DescribeFlowlogsResponseBodyFlowLogsFlowLog]

    def validate(self):
        if self.flow_log:
            for k in self.flow_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFlowlogsResponseBodyFlowLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FlowLog'] = []
        if self.flow_log is not None:
            for k in self.flow_log:
                result['FlowLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flow_log = []
        if m.get('FlowLog') is not None:
            for k in m.get('FlowLog'):
                temp_model = DescribeFlowlogsResponseBodyFlowLogsFlowLog()
                self.flow_log.append(temp_model.from_map(k))
        return self


class DescribeFlowlogsResponseBody(TeaModel):
    def __init__(self, flow_logs=None, page_number=None, page_size=None, request_id=None, success=None,
                 total_count=None):
        self.flow_logs = flow_logs  # type: DescribeFlowlogsResponseBodyFlowLogs
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.flow_logs:
            self.flow_logs.validate()

    def to_map(self):
        _map = super(DescribeFlowlogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_logs is not None:
            result['FlowLogs'] = self.flow_logs.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowLogs') is not None:
            temp_model = DescribeFlowlogsResponseBodyFlowLogs()
            self.flow_logs = temp_model.from_map(m['FlowLogs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFlowlogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFlowlogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowlogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFlowlogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGeographicRegionMembershipRequest(TeaModel):
    def __init__(self, geographic_region_id=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None):
        self.geographic_region_id = geographic_region_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGeographicRegionMembershipRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.geographic_region_id is not None:
            result['GeographicRegionId'] = self.geographic_region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GeographicRegionId') is not None:
            self.geographic_region_id = m.get('GeographicRegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeGeographicRegionMembershipResponseBodyRegionIdsRegionId(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGeographicRegionMembershipResponseBodyRegionIdsRegionId, self).to_map()
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


class DescribeGeographicRegionMembershipResponseBodyRegionIds(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: list[DescribeGeographicRegionMembershipResponseBodyRegionIdsRegionId]

    def validate(self):
        if self.region_id:
            for k in self.region_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGeographicRegionMembershipResponseBodyRegionIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionId'] = []
        if self.region_id is not None:
            for k in self.region_id:
                result['RegionId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region_id = []
        if m.get('RegionId') is not None:
            for k in m.get('RegionId'):
                temp_model = DescribeGeographicRegionMembershipResponseBodyRegionIdsRegionId()
                self.region_id.append(temp_model.from_map(k))
        return self


class DescribeGeographicRegionMembershipResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_ids=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_ids = region_ids  # type: DescribeGeographicRegionMembershipResponseBodyRegionIds
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        _map = super(DescribeGeographicRegionMembershipResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()
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
        if m.get('RegionIds') is not None:
            temp_model = DescribeGeographicRegionMembershipResponseBodyRegionIds()
            self.region_ids = temp_model.from_map(m['RegionIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeGeographicRegionMembershipResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeGeographicRegionMembershipResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGeographicRegionMembershipResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeGeographicRegionMembershipResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGrantRulesToCenRequest(TeaModel):
    def __init__(self, cen_id=None, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 product_type=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.product_type = product_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGrantRulesToCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeGrantRulesToCenResponseBodyGrantRulesGrantRule(TeaModel):
    def __init__(self, cen_id=None, cen_owner_id=None, child_instance_id=None, child_instance_owner_id=None,
                 child_instance_region_id=None, child_instance_type=None, order_type=None):
        self.cen_id = cen_id  # type: str
        self.cen_owner_id = cen_owner_id  # type: long
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_owner_id = child_instance_owner_id  # type: long
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.order_type = order_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGrantRulesToCenResponseBodyGrantRulesGrantRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class DescribeGrantRulesToCenResponseBodyGrantRules(TeaModel):
    def __init__(self, grant_rule=None):
        self.grant_rule = grant_rule  # type: list[DescribeGrantRulesToCenResponseBodyGrantRulesGrantRule]

    def validate(self):
        if self.grant_rule:
            for k in self.grant_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGrantRulesToCenResponseBodyGrantRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GrantRule'] = []
        if self.grant_rule is not None:
            for k in self.grant_rule:
                result['GrantRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.grant_rule = []
        if m.get('GrantRule') is not None:
            for k in m.get('GrantRule'):
                temp_model = DescribeGrantRulesToCenResponseBodyGrantRulesGrantRule()
                self.grant_rule.append(temp_model.from_map(k))
        return self


class DescribeGrantRulesToCenResponseBody(TeaModel):
    def __init__(self, grant_rules=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.grant_rules = grant_rules  # type: DescribeGrantRulesToCenResponseBodyGrantRules
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.grant_rules:
            self.grant_rules.validate()

    def to_map(self):
        _map = super(DescribeGrantRulesToCenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_rules is not None:
            result['GrantRules'] = self.grant_rules.to_map()
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
        if m.get('GrantRules') is not None:
            temp_model = DescribeGrantRulesToCenResponseBodyGrantRules()
            self.grant_rules = temp_model.from_map(m['GrantRules'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeGrantRulesToCenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeGrantRulesToCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGrantRulesToCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeGrantRulesToCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGrantRulesToResourceRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, owner_account=None, owner_id=None, product_type=None,
                 region_id=None, resource_id=None, resource_owner_account=None, resource_owner_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.product_type = product_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGrantRulesToResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeGrantRulesToResourceResponseBodyGrantRules(TeaModel):
    def __init__(self, cen_id=None, cen_owner_id=None, order_type=None):
        self.cen_id = cen_id  # type: str
        self.cen_owner_id = cen_owner_id  # type: long
        self.order_type = order_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGrantRulesToResourceResponseBodyGrantRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class DescribeGrantRulesToResourceResponseBody(TeaModel):
    def __init__(self, grant_rules=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.grant_rules = grant_rules  # type: list[DescribeGrantRulesToResourceResponseBodyGrantRules]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.grant_rules:
            for k in self.grant_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGrantRulesToResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GrantRules'] = []
        if self.grant_rules is not None:
            for k in self.grant_rules:
                result['GrantRules'].append(k.to_map() if k else None)
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
        self.grant_rules = []
        if m.get('GrantRules') is not None:
            for k in m.get('GrantRules'):
                temp_model = DescribeGrantRulesToResourceResponseBodyGrantRules()
                self.grant_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeGrantRulesToResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeGrantRulesToResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGrantRulesToResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeGrantRulesToResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePublishedRouteEntriesRequest(TeaModel):
    def __init__(self, cen_id=None, child_instance_id=None, child_instance_region_id=None,
                 child_instance_route_table_id=None, child_instance_type=None, destination_cidr_block=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_route_table_id = child_instance_route_table_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePublishedRouteEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflictsConflict(TeaModel):
    def __init__(self, destination_cidr_block=None, instance_id=None, instance_type=None, region_id=None,
                 status=None):
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflictsConflict, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflicts(TeaModel):
    def __init__(self, conflict=None):
        self.conflict = conflict  # type: list[DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflictsConflict]

    def validate(self):
        if self.conflict:
            for k in self.conflict:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflicts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conflict'] = []
        if self.conflict is not None:
            for k in self.conflict:
                result['Conflict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.conflict = []
        if m.get('Conflict') is not None:
            for k in m.get('Conflict'):
                temp_model = DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflictsConflict()
                self.conflict.append(temp_model.from_map(k))
        return self


class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntry(TeaModel):
    def __init__(self, child_instance_route_table_id=None, conflicts=None, destination_cidr_block=None,
                 next_hop_id=None, next_hop_type=None, operational_mode=None, publish_status=None, route_type=None):
        self.child_instance_route_table_id = child_instance_route_table_id  # type: str
        self.conflicts = conflicts  # type: DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflicts
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.next_hop_id = next_hop_id  # type: str
        self.next_hop_type = next_hop_type  # type: str
        self.operational_mode = operational_mode  # type: bool
        self.publish_status = publish_status  # type: str
        self.route_type = route_type  # type: str

    def validate(self):
        if self.conflicts:
            self.conflicts.validate()

    def to_map(self):
        _map = super(DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntry, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.conflicts is not None:
            result['Conflicts'] = self.conflicts.to_map()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.operational_mode is not None:
            result['OperationalMode'] = self.operational_mode
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('Conflicts') is not None:
            temp_model = DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflicts()
            self.conflicts = temp_model.from_map(m['Conflicts'])
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('OperationalMode') is not None:
            self.operational_mode = m.get('OperationalMode')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        return self


class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries(TeaModel):
    def __init__(self, published_route_entry=None):
        self.published_route_entry = published_route_entry  # type: list[DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntry]

    def validate(self):
        if self.published_route_entry:
            for k in self.published_route_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PublishedRouteEntry'] = []
        if self.published_route_entry is not None:
            for k in self.published_route_entry:
                result['PublishedRouteEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.published_route_entry = []
        if m.get('PublishedRouteEntry') is not None:
            for k in m.get('PublishedRouteEntry'):
                temp_model = DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntry()
                self.published_route_entry.append(temp_model.from_map(k))
        return self


class DescribePublishedRouteEntriesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, published_route_entries=None, request_id=None,
                 total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.published_route_entries = published_route_entries  # type: DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.published_route_entries:
            self.published_route_entries.validate()

    def to_map(self):
        _map = super(DescribePublishedRouteEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.published_route_entries is not None:
            result['PublishedRouteEntries'] = self.published_route_entries.to_map()
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
        if m.get('PublishedRouteEntries') is not None:
            temp_model = DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries()
            self.published_route_entries = temp_model.from_map(m['PublishedRouteEntries'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePublishedRouteEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePublishedRouteEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePublishedRouteEntriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePublishedRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRouteConflictRequest(TeaModel):
    def __init__(self, child_instance_id=None, child_instance_region_id=None, child_instance_route_table_id=None,
                 child_instance_type=None, destination_cidr_block=None, owner_account=None, owner_id=None, page_number=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None):
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_route_table_id = child_instance_route_table_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRouteConflictRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRouteConflictResponseBodyRouteConflictsRouteConflict(TeaModel):
    def __init__(self, destination_cidr_block=None, instance_id=None, instance_type=None, region_id=None,
                 status=None):
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRouteConflictResponseBodyRouteConflictsRouteConflict, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeRouteConflictResponseBodyRouteConflicts(TeaModel):
    def __init__(self, route_conflict=None):
        self.route_conflict = route_conflict  # type: list[DescribeRouteConflictResponseBodyRouteConflictsRouteConflict]

    def validate(self):
        if self.route_conflict:
            for k in self.route_conflict:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRouteConflictResponseBodyRouteConflicts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteConflict'] = []
        if self.route_conflict is not None:
            for k in self.route_conflict:
                result['RouteConflict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.route_conflict = []
        if m.get('RouteConflict') is not None:
            for k in m.get('RouteConflict'):
                temp_model = DescribeRouteConflictResponseBodyRouteConflictsRouteConflict()
                self.route_conflict.append(temp_model.from_map(k))
        return self


class DescribeRouteConflictResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, route_conflicts=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.route_conflicts = route_conflicts  # type: DescribeRouteConflictResponseBodyRouteConflicts
        self.total_count = total_count  # type: int

    def validate(self):
        if self.route_conflicts:
            self.route_conflicts.validate()

    def to_map(self):
        _map = super(DescribeRouteConflictResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route_conflicts is not None:
            result['RouteConflicts'] = self.route_conflicts.to_map()
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
        if m.get('RouteConflicts') is not None:
            temp_model = DescribeRouteConflictResponseBodyRouteConflicts()
            self.route_conflicts = temp_model.from_map(m['RouteConflicts'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRouteConflictResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRouteConflictResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRouteConflictResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRouteConflictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRouteServicesInCenRequest(TeaModel):
    def __init__(self, access_region_id=None, cen_id=None, host=None, host_region_id=None, host_vpc_id=None,
                 owner_account=None, owner_id=None, page_number=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.access_region_id = access_region_id  # type: str
        self.cen_id = cen_id  # type: str
        self.host = host  # type: str
        self.host_region_id = host_region_id  # type: str
        self.host_vpc_id = host_vpc_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRouteServicesInCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.host is not None:
            result['Host'] = self.host
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntryCidrs(TeaModel):
    def __init__(self, cidr=None):
        self.cidr = cidr  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntryCidrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        return self


class DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntry(TeaModel):
    def __init__(self, access_region_id=None, cen_id=None, cidrs=None, description=None, host=None,
                 host_region_id=None, host_vpc_id=None, status=None):
        self.access_region_id = access_region_id  # type: str
        self.cen_id = cen_id  # type: str
        self.cidrs = cidrs  # type: DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntryCidrs
        self.description = description  # type: str
        self.host = host  # type: str
        self.host_region_id = host_region_id  # type: str
        self.host_vpc_id = host_vpc_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.cidrs:
            self.cidrs.validate()

    def to_map(self):
        _map = super(DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntry, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.host is not None:
            result['Host'] = self.host
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Cidrs') is not None:
            temp_model = DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntryCidrs()
            self.cidrs = temp_model.from_map(m['Cidrs'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeRouteServicesInCenResponseBodyRouteServiceEntries(TeaModel):
    def __init__(self, route_service_entry=None):
        self.route_service_entry = route_service_entry  # type: list[DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntry]

    def validate(self):
        if self.route_service_entry:
            for k in self.route_service_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRouteServicesInCenResponseBodyRouteServiceEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteServiceEntry'] = []
        if self.route_service_entry is not None:
            for k in self.route_service_entry:
                result['RouteServiceEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.route_service_entry = []
        if m.get('RouteServiceEntry') is not None:
            for k in m.get('RouteServiceEntry'):
                temp_model = DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntry()
                self.route_service_entry.append(temp_model.from_map(k))
        return self


class DescribeRouteServicesInCenResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, route_service_entries=None,
                 total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.route_service_entries = route_service_entries  # type: DescribeRouteServicesInCenResponseBodyRouteServiceEntries
        self.total_count = total_count  # type: int

    def validate(self):
        if self.route_service_entries:
            self.route_service_entries.validate()

    def to_map(self):
        _map = super(DescribeRouteServicesInCenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route_service_entries is not None:
            result['RouteServiceEntries'] = self.route_service_entries.to_map()
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
        if m.get('RouteServiceEntries') is not None:
            temp_model = DescribeRouteServicesInCenResponseBodyRouteServiceEntries()
            self.route_service_entries = temp_model.from_map(m['RouteServiceEntries'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRouteServicesInCenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRouteServicesInCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRouteServicesInCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRouteServicesInCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachCenChildInstanceRequest(TeaModel):
    def __init__(self, cen_id=None, cen_owner_id=None, child_instance_id=None, child_instance_owner_id=None,
                 child_instance_region_id=None, child_instance_type=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.cen_owner_id = cen_owner_id  # type: long
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_owner_id = child_instance_owner_id  # type: long
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachCenChildInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DetachCenChildInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachCenChildInstanceResponseBody, self).to_map()
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


class DetachCenChildInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachCenChildInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachCenChildInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachCenChildInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableCenVbrHealthCheckRequest(TeaModel):
    def __init__(self, cen_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, vbr_instance_id=None, vbr_instance_owner_id=None, vbr_instance_region_id=None):
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.vbr_instance_id = vbr_instance_id  # type: str
        self.vbr_instance_owner_id = vbr_instance_owner_id  # type: long
        self.vbr_instance_region_id = vbr_instance_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableCenVbrHealthCheckRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id
        if self.vbr_instance_owner_id is not None:
            result['VbrInstanceOwnerId'] = self.vbr_instance_owner_id
        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')
        if m.get('VbrInstanceOwnerId') is not None:
            self.vbr_instance_owner_id = m.get('VbrInstanceOwnerId')
        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')
        return self


class DisableCenVbrHealthCheckResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableCenVbrHealthCheckResponseBody, self).to_map()
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


class DisableCenVbrHealthCheckResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableCenVbrHealthCheckResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableCenVbrHealthCheckResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableCenVbrHealthCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableCenVpcFlowStatisticRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableCenVpcFlowStatisticRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DisableCenVpcFlowStatisticResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableCenVpcFlowStatisticResponseBody, self).to_map()
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


class DisableCenVpcFlowStatisticResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableCenVpcFlowStatisticResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableCenVpcFlowStatisticResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableCenVpcFlowStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableTransitRouterRouteTablePropagationRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_route_table_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableTransitRouterRouteTablePropagationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class DisableTransitRouterRouteTablePropagationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableTransitRouterRouteTablePropagationResponseBody, self).to_map()
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


class DisableTransitRouterRouteTablePropagationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableTransitRouterRouteTablePropagationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableTransitRouterRouteTablePropagationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableTransitRouterRouteTablePropagationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateTransitRouterMulticastDomainRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_multicast_domain_id=None, v_switch_ids=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str
        self.v_switch_ids = v_switch_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociateTransitRouterMulticastDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class DisassociateTransitRouterMulticastDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociateTransitRouterMulticastDomainResponseBody, self).to_map()
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


class DisassociateTransitRouterMulticastDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisassociateTransitRouterMulticastDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisassociateTransitRouterMulticastDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateTransitRouterMulticastDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateTransitRouterAttachmentFromRouteTableRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_route_table_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateTransitRouterAttachmentFromRouteTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class DissociateTransitRouterAttachmentFromRouteTableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateTransitRouterAttachmentFromRouteTableResponseBody, self).to_map()
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


class DissociateTransitRouterAttachmentFromRouteTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DissociateTransitRouterAttachmentFromRouteTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateTransitRouterAttachmentFromRouteTableResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DissociateTransitRouterAttachmentFromRouteTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableCenVbrHealthCheckRequest(TeaModel):
    def __init__(self, cen_id=None, health_check_interval=None, health_check_only=None,
                 health_check_source_ip=None, health_check_target_ip=None, healthy_threshold=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, vbr_instance_id=None, vbr_instance_owner_id=None,
                 vbr_instance_region_id=None):
        self.cen_id = cen_id  # type: str
        self.health_check_interval = health_check_interval  # type: int
        self.health_check_only = health_check_only  # type: bool
        self.health_check_source_ip = health_check_source_ip  # type: str
        self.health_check_target_ip = health_check_target_ip  # type: str
        self.healthy_threshold = healthy_threshold  # type: int
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.vbr_instance_id = vbr_instance_id  # type: str
        self.vbr_instance_owner_id = vbr_instance_owner_id  # type: long
        self.vbr_instance_region_id = vbr_instance_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableCenVbrHealthCheckRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_only is not None:
            result['HealthCheckOnly'] = self.health_check_only
        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip
        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id
        if self.vbr_instance_owner_id is not None:
            result['VbrInstanceOwnerId'] = self.vbr_instance_owner_id
        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckOnly') is not None:
            self.health_check_only = m.get('HealthCheckOnly')
        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')
        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')
        if m.get('VbrInstanceOwnerId') is not None:
            self.vbr_instance_owner_id = m.get('VbrInstanceOwnerId')
        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')
        return self


class EnableCenVbrHealthCheckResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableCenVbrHealthCheckResponseBody, self).to_map()
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


class EnableCenVbrHealthCheckResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableCenVbrHealthCheckResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableCenVbrHealthCheckResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableCenVbrHealthCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableCenVpcFlowStatisticRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, days=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.days = days  # type: int
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableCenVpcFlowStatisticRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.days is not None:
            result['Days'] = self.days
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class EnableCenVpcFlowStatisticResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableCenVpcFlowStatisticResponseBody, self).to_map()
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


class EnableCenVpcFlowStatisticResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableCenVpcFlowStatisticResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableCenVpcFlowStatisticResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableCenVpcFlowStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableTransitRouterRouteTablePropagationRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_route_table_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableTransitRouterRouteTablePropagationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class EnableTransitRouterRouteTablePropagationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableTransitRouterRouteTablePropagationResponseBody, self).to_map()
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


class EnableTransitRouterRouteTablePropagationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableTransitRouterRouteTablePropagationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableTransitRouterRouteTablePropagationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableTransitRouterRouteTablePropagationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantInstanceToTransitRouterRequest(TeaModel):
    def __init__(self, cen_id=None, cen_owner_id=None, instance_id=None, instance_type=None, order_type=None,
                 owner_account=None, owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.cen_owner_id = cen_owner_id  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.order_type = order_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantInstanceToTransitRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GrantInstanceToTransitRouterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantInstanceToTransitRouterResponseBody, self).to_map()
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


class GrantInstanceToTransitRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GrantInstanceToTransitRouterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantInstanceToTransitRouterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GrantInstanceToTransitRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCenInterRegionTrafficQosPoliciesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_qos_policy_description=None, traffic_qos_policy_id=None,
                 traffic_qos_policy_name=None, transit_router_attachment_id=None, transit_router_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_qos_policy_description = traffic_qos_policy_description  # type: str
        self.traffic_qos_policy_id = traffic_qos_policy_id  # type: str
        self.traffic_qos_policy_name = traffic_qos_policy_name  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCenInterRegionTrafficQosPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_qos_policy_description is not None:
            result['TrafficQosPolicyDescription'] = self.traffic_qos_policy_description
        if self.traffic_qos_policy_id is not None:
            result['TrafficQosPolicyId'] = self.traffic_qos_policy_id
        if self.traffic_qos_policy_name is not None:
            result['TrafficQosPolicyName'] = self.traffic_qos_policy_name
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficQosPolicyDescription') is not None:
            self.traffic_qos_policy_description = m.get('TrafficQosPolicyDescription')
        if m.get('TrafficQosPolicyId') is not None:
            self.traffic_qos_policy_id = m.get('TrafficQosPolicyId')
        if m.get('TrafficQosPolicyName') is not None:
            self.traffic_qos_policy_name = m.get('TrafficQosPolicyName')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPoliciesTrafficQosQueues(TeaModel):
    def __init__(self, dscps=None, qos_queue_description=None, qos_queue_id=None, qos_queue_name=None,
                 remain_bandwidth_percent=None):
        self.dscps = dscps  # type: list[int]
        self.qos_queue_description = qos_queue_description  # type: str
        self.qos_queue_id = qos_queue_id  # type: str
        self.qos_queue_name = qos_queue_name  # type: str
        self.remain_bandwidth_percent = remain_bandwidth_percent  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPoliciesTrafficQosQueues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dscps is not None:
            result['Dscps'] = self.dscps
        if self.qos_queue_description is not None:
            result['QosQueueDescription'] = self.qos_queue_description
        if self.qos_queue_id is not None:
            result['QosQueueId'] = self.qos_queue_id
        if self.qos_queue_name is not None:
            result['QosQueueName'] = self.qos_queue_name
        if self.remain_bandwidth_percent is not None:
            result['RemainBandwidthPercent'] = self.remain_bandwidth_percent
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dscps') is not None:
            self.dscps = m.get('Dscps')
        if m.get('QosQueueDescription') is not None:
            self.qos_queue_description = m.get('QosQueueDescription')
        if m.get('QosQueueId') is not None:
            self.qos_queue_id = m.get('QosQueueId')
        if m.get('QosQueueName') is not None:
            self.qos_queue_name = m.get('QosQueueName')
        if m.get('RemainBandwidthPercent') is not None:
            self.remain_bandwidth_percent = m.get('RemainBandwidthPercent')
        return self


class ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPolicies(TeaModel):
    def __init__(self, traffic_qos_policy_description=None, traffic_qos_policy_id=None,
                 traffic_qos_policy_name=None, traffic_qos_policy_status=None, traffic_qos_queues=None):
        self.traffic_qos_policy_description = traffic_qos_policy_description  # type: str
        self.traffic_qos_policy_id = traffic_qos_policy_id  # type: str
        self.traffic_qos_policy_name = traffic_qos_policy_name  # type: str
        self.traffic_qos_policy_status = traffic_qos_policy_status  # type: str
        self.traffic_qos_queues = traffic_qos_queues  # type: list[ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPoliciesTrafficQosQueues]

    def validate(self):
        if self.traffic_qos_queues:
            for k in self.traffic_qos_queues:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.traffic_qos_policy_description is not None:
            result['TrafficQosPolicyDescription'] = self.traffic_qos_policy_description
        if self.traffic_qos_policy_id is not None:
            result['TrafficQosPolicyId'] = self.traffic_qos_policy_id
        if self.traffic_qos_policy_name is not None:
            result['TrafficQosPolicyName'] = self.traffic_qos_policy_name
        if self.traffic_qos_policy_status is not None:
            result['TrafficQosPolicyStatus'] = self.traffic_qos_policy_status
        result['TrafficQosQueues'] = []
        if self.traffic_qos_queues is not None:
            for k in self.traffic_qos_queues:
                result['TrafficQosQueues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrafficQosPolicyDescription') is not None:
            self.traffic_qos_policy_description = m.get('TrafficQosPolicyDescription')
        if m.get('TrafficQosPolicyId') is not None:
            self.traffic_qos_policy_id = m.get('TrafficQosPolicyId')
        if m.get('TrafficQosPolicyName') is not None:
            self.traffic_qos_policy_name = m.get('TrafficQosPolicyName')
        if m.get('TrafficQosPolicyStatus') is not None:
            self.traffic_qos_policy_status = m.get('TrafficQosPolicyStatus')
        self.traffic_qos_queues = []
        if m.get('TrafficQosQueues') is not None:
            for k in m.get('TrafficQosQueues'):
                temp_model = ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPoliciesTrafficQosQueues()
                self.traffic_qos_queues.append(temp_model.from_map(k))
        return self


class ListCenInterRegionTrafficQosPoliciesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 traffic_qos_policies=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.traffic_qos_policies = traffic_qos_policies  # type: list[ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPolicies]

    def validate(self):
        if self.traffic_qos_policies:
            for k in self.traffic_qos_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCenInterRegionTrafficQosPoliciesResponseBody, self).to_map()
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
        result['TrafficQosPolicies'] = []
        if self.traffic_qos_policies is not None:
            for k in self.traffic_qos_policies:
                result['TrafficQosPolicies'].append(k.to_map() if k else None)
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
        self.traffic_qos_policies = []
        if m.get('TrafficQosPolicies') is not None:
            for k in m.get('TrafficQosPolicies'):
                temp_model = ListCenInterRegionTrafficQosPoliciesResponseBodyTrafficQosPolicies()
                self.traffic_qos_policies.append(temp_model.from_map(k))
        return self


class ListCenInterRegionTrafficQosPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCenInterRegionTrafficQosPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCenInterRegionTrafficQosPoliciesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCenInterRegionTrafficQosPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGrantVSwitchEnisRequest(TeaModel):
    def __init__(self, cen_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, v_switch_id=None, vpc_id=None):
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGrantVSwitchEnisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListGrantVSwitchEnisResponseBodyGrantVSwitchEnis(TeaModel):
    def __init__(self, description=None, network_interface_id=None, transit_router_flag=None, v_switch_id=None,
                 vpc_id=None):
        self.description = description  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.transit_router_flag = transit_router_flag  # type: bool
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGrantVSwitchEnisResponseBodyGrantVSwitchEnis, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.transit_router_flag is not None:
            result['TransitRouterFlag'] = self.transit_router_flag
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('TransitRouterFlag') is not None:
            self.transit_router_flag = m.get('TransitRouterFlag')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListGrantVSwitchEnisResponseBody(TeaModel):
    def __init__(self, grant_vswitch_enis=None, request_id=None, total_count=None):
        self.grant_vswitch_enis = grant_vswitch_enis  # type: list[ListGrantVSwitchEnisResponseBodyGrantVSwitchEnis]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.grant_vswitch_enis:
            for k in self.grant_vswitch_enis:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGrantVSwitchEnisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GrantVSwitchEnis'] = []
        if self.grant_vswitch_enis is not None:
            for k in self.grant_vswitch_enis:
                result['GrantVSwitchEnis'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.grant_vswitch_enis = []
        if m.get('GrantVSwitchEnis') is not None:
            for k in m.get('GrantVSwitchEnis'):
                temp_model = ListGrantVSwitchEnisResponseBodyGrantVSwitchEnis()
                self.grant_vswitch_enis.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGrantVSwitchEnisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGrantVSwitchEnisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGrantVSwitchEnisResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGrantVSwitchEnisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGrantVSwitchesToCenRequest(TeaModel):
    def __init__(self, cen_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, vpc_id=None, zone_id=None):
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGrantVSwitchesToCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListGrantVSwitchesToCenResponseBodyVSwitches(TeaModel):
    def __init__(self, v_switch_id=None, vpc_id=None, zone_id=None):
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGrantVSwitchesToCenResponseBodyVSwitches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListGrantVSwitchesToCenResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, v_switches=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.v_switches = v_switches  # type: list[ListGrantVSwitchesToCenResponseBodyVSwitches]

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGrantVSwitchesToCenResponseBody, self).to_map()
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
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
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
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = ListGrantVSwitchesToCenResponseBodyVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        return self


class ListGrantVSwitchesToCenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGrantVSwitchesToCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGrantVSwitchesToCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGrantVSwitchesToCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequestTag, self).to_map()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(self, next_token=None, owner_account=None, owner_id=None, page_size=None, resource_id=None,
                 resource_owner_account=None, resource_owner_id=None, resource_type=None, tag=None):
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_size = page_size  # type: int
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: list[ListTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrafficMarkingPoliciesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_marking_policy_description=None,
                 traffic_marking_policy_id=None, traffic_marking_policy_name=None, transit_router_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_marking_policy_description = traffic_marking_policy_description  # type: str
        self.traffic_marking_policy_id = traffic_marking_policy_id  # type: str
        self.traffic_marking_policy_name = traffic_marking_policy_name  # type: str
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrafficMarkingPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_marking_policy_description is not None:
            result['TrafficMarkingPolicyDescription'] = self.traffic_marking_policy_description
        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id
        if self.traffic_marking_policy_name is not None:
            result['TrafficMarkingPolicyName'] = self.traffic_marking_policy_name
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficMarkingPolicyDescription') is not None:
            self.traffic_marking_policy_description = m.get('TrafficMarkingPolicyDescription')
        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')
        if m.get('TrafficMarkingPolicyName') is not None:
            self.traffic_marking_policy_name = m.get('TrafficMarkingPolicyName')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPoliciesTrafficMatchRules(TeaModel):
    def __init__(self, dst_cidr=None, dst_port_range=None, match_dscp=None, protocol=None, src_cidr=None,
                 src_port_range=None, traffic_match_rule_description=None, traffic_match_rule_id=None,
                 traffic_match_rule_name=None, traffic_match_rule_status=None):
        self.dst_cidr = dst_cidr  # type: str
        self.dst_port_range = dst_port_range  # type: list[int]
        self.match_dscp = match_dscp  # type: int
        self.protocol = protocol  # type: str
        self.src_cidr = src_cidr  # type: str
        self.src_port_range = src_port_range  # type: list[int]
        self.traffic_match_rule_description = traffic_match_rule_description  # type: str
        self.traffic_match_rule_id = traffic_match_rule_id  # type: str
        self.traffic_match_rule_name = traffic_match_rule_name  # type: str
        self.traffic_match_rule_status = traffic_match_rule_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPoliciesTrafficMatchRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_cidr is not None:
            result['DstCidr'] = self.dst_cidr
        if self.dst_port_range is not None:
            result['DstPortRange'] = self.dst_port_range
        if self.match_dscp is not None:
            result['MatchDscp'] = self.match_dscp
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.src_cidr is not None:
            result['SrcCidr'] = self.src_cidr
        if self.src_port_range is not None:
            result['SrcPortRange'] = self.src_port_range
        if self.traffic_match_rule_description is not None:
            result['TrafficMatchRuleDescription'] = self.traffic_match_rule_description
        if self.traffic_match_rule_id is not None:
            result['TrafficMatchRuleId'] = self.traffic_match_rule_id
        if self.traffic_match_rule_name is not None:
            result['TrafficMatchRuleName'] = self.traffic_match_rule_name
        if self.traffic_match_rule_status is not None:
            result['TrafficMatchRuleStatus'] = self.traffic_match_rule_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DstCidr') is not None:
            self.dst_cidr = m.get('DstCidr')
        if m.get('DstPortRange') is not None:
            self.dst_port_range = m.get('DstPortRange')
        if m.get('MatchDscp') is not None:
            self.match_dscp = m.get('MatchDscp')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('SrcCidr') is not None:
            self.src_cidr = m.get('SrcCidr')
        if m.get('SrcPortRange') is not None:
            self.src_port_range = m.get('SrcPortRange')
        if m.get('TrafficMatchRuleDescription') is not None:
            self.traffic_match_rule_description = m.get('TrafficMatchRuleDescription')
        if m.get('TrafficMatchRuleId') is not None:
            self.traffic_match_rule_id = m.get('TrafficMatchRuleId')
        if m.get('TrafficMatchRuleName') is not None:
            self.traffic_match_rule_name = m.get('TrafficMatchRuleName')
        if m.get('TrafficMatchRuleStatus') is not None:
            self.traffic_match_rule_status = m.get('TrafficMatchRuleStatus')
        return self


class ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPolicies(TeaModel):
    def __init__(self, marking_dscp=None, priority=None, traffic_marking_policy_description=None,
                 traffic_marking_policy_id=None, traffic_marking_policy_name=None, traffic_marking_policy_status=None,
                 traffic_match_rules=None):
        self.marking_dscp = marking_dscp  # type: int
        self.priority = priority  # type: int
        self.traffic_marking_policy_description = traffic_marking_policy_description  # type: str
        self.traffic_marking_policy_id = traffic_marking_policy_id  # type: str
        self.traffic_marking_policy_name = traffic_marking_policy_name  # type: str
        self.traffic_marking_policy_status = traffic_marking_policy_status  # type: str
        self.traffic_match_rules = traffic_match_rules  # type: list[ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPoliciesTrafficMatchRules]

    def validate(self):
        if self.traffic_match_rules:
            for k in self.traffic_match_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marking_dscp is not None:
            result['MarkingDscp'] = self.marking_dscp
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.traffic_marking_policy_description is not None:
            result['TrafficMarkingPolicyDescription'] = self.traffic_marking_policy_description
        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id
        if self.traffic_marking_policy_name is not None:
            result['TrafficMarkingPolicyName'] = self.traffic_marking_policy_name
        if self.traffic_marking_policy_status is not None:
            result['TrafficMarkingPolicyStatus'] = self.traffic_marking_policy_status
        result['TrafficMatchRules'] = []
        if self.traffic_match_rules is not None:
            for k in self.traffic_match_rules:
                result['TrafficMatchRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MarkingDscp') is not None:
            self.marking_dscp = m.get('MarkingDscp')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('TrafficMarkingPolicyDescription') is not None:
            self.traffic_marking_policy_description = m.get('TrafficMarkingPolicyDescription')
        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')
        if m.get('TrafficMarkingPolicyName') is not None:
            self.traffic_marking_policy_name = m.get('TrafficMarkingPolicyName')
        if m.get('TrafficMarkingPolicyStatus') is not None:
            self.traffic_marking_policy_status = m.get('TrafficMarkingPolicyStatus')
        self.traffic_match_rules = []
        if m.get('TrafficMatchRules') is not None:
            for k in m.get('TrafficMatchRules'):
                temp_model = ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPoliciesTrafficMatchRules()
                self.traffic_match_rules.append(temp_model.from_map(k))
        return self


class ListTrafficMarkingPoliciesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 traffic_marking_policies=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.traffic_marking_policies = traffic_marking_policies  # type: list[ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPolicies]

    def validate(self):
        if self.traffic_marking_policies:
            for k in self.traffic_marking_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTrafficMarkingPoliciesResponseBody, self).to_map()
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
        result['TrafficMarkingPolicies'] = []
        if self.traffic_marking_policies is not None:
            for k in self.traffic_marking_policies:
                result['TrafficMarkingPolicies'].append(k.to_map() if k else None)
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
        self.traffic_marking_policies = []
        if m.get('TrafficMarkingPolicies') is not None:
            for k in m.get('TrafficMarkingPolicies'):
                temp_model = ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPolicies()
                self.traffic_marking_policies.append(temp_model.from_map(k))
        return self


class ListTrafficMarkingPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTrafficMarkingPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTrafficMarkingPoliciesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTrafficMarkingPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterAvailableResourceRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, support_multicast=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.support_multicast = support_multicast  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterAvailableResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.support_multicast is not None:
            result['SupportMulticast'] = self.support_multicast
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SupportMulticast') is not None:
            self.support_multicast = m.get('SupportMulticast')
        return self


class ListTransitRouterAvailableResourceResponseBody(TeaModel):
    def __init__(self, available_zones=None, master_zones=None, request_id=None, slave_zones=None):
        self.available_zones = available_zones  # type: list[str]
        self.master_zones = master_zones  # type: list[str]
        self.request_id = request_id  # type: str
        self.slave_zones = slave_zones  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterAvailableResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones
        if self.master_zones is not None:
            result['MasterZones'] = self.master_zones
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slave_zones is not None:
            result['SlaveZones'] = self.slave_zones
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            self.available_zones = m.get('AvailableZones')
        if m.get('MasterZones') is not None:
            self.master_zones = m.get('MasterZones')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlaveZones') is not None:
            self.slave_zones = m.get('SlaveZones')
        return self


class ListTransitRouterAvailableResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterAvailableResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterAvailableResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterMulticastDomainAssociationsRequest(TeaModel):
    def __init__(self, client_token=None, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 resource_id=None, resource_owner_account=None, resource_owner_id=None, resource_type=None,
                 transit_router_attachment_id=None, transit_router_multicast_domain_id=None, v_switch_ids=None):
        self.client_token = client_token  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_id = resource_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str
        self.v_switch_ids = v_switch_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainAssociationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class ListTransitRouterMulticastDomainAssociationsResponseBodyTransitRouterMulticastAssociations(TeaModel):
    def __init__(self, resource_id=None, resource_owner_id=None, resource_type=None, status=None,
                 transit_router_attachment_id=None, transit_router_multicast_domain_id=None, v_switch_id=None):
        self.resource_id = resource_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainAssociationsResponseBodyTransitRouterMulticastAssociations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class ListTransitRouterMulticastDomainAssociationsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_multicast_associations=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_multicast_associations = transit_router_multicast_associations  # type: list[ListTransitRouterMulticastDomainAssociationsResponseBodyTransitRouterMulticastAssociations]

    def validate(self):
        if self.transit_router_multicast_associations:
            for k in self.transit_router_multicast_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainAssociationsResponseBody, self).to_map()
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
        result['TransitRouterMulticastAssociations'] = []
        if self.transit_router_multicast_associations is not None:
            for k in self.transit_router_multicast_associations:
                result['TransitRouterMulticastAssociations'].append(k.to_map() if k else None)
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
        self.transit_router_multicast_associations = []
        if m.get('TransitRouterMulticastAssociations') is not None:
            for k in m.get('TransitRouterMulticastAssociations'):
                temp_model = ListTransitRouterMulticastDomainAssociationsResponseBodyTransitRouterMulticastAssociations()
                self.transit_router_multicast_associations.append(temp_model.from_map(k))
        return self


class ListTransitRouterMulticastDomainAssociationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterMulticastDomainAssociationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainAssociationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterMulticastDomainAssociationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterMulticastDomainVSwitchesRequest(TeaModel):
    def __init__(self, cen_id=None, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, v_switch_ids=None, vpc_id=None):
        self.cen_id = cen_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainVSwitchesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListTransitRouterMulticastDomainVSwitchesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None, v_switch_ids=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.v_switch_ids = v_switch_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainVSwitchesResponseBody, self).to_map()
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
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
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
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class ListTransitRouterMulticastDomainVSwitchesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterMulticastDomainVSwitchesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainVSwitchesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterMulticastDomainVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterMulticastDomainsRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, max_results=None, next_token=None, owner_account=None,
                 owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None, transit_router_id=None,
                 transit_router_multicast_domain_id=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        return self


class ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomains(TeaModel):
    def __init__(self, status=None, transit_router_multicast_domain_description=None,
                 transit_router_multicast_domain_id=None, transit_router_multicast_domain_name=None):
        self.status = status  # type: str
        self.transit_router_multicast_domain_description = transit_router_multicast_domain_description  # type: str
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str
        self.transit_router_multicast_domain_name = transit_router_multicast_domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_multicast_domain_description is not None:
            result['TransitRouterMulticastDomainDescription'] = self.transit_router_multicast_domain_description
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        if self.transit_router_multicast_domain_name is not None:
            result['TransitRouterMulticastDomainName'] = self.transit_router_multicast_domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterMulticastDomainDescription') is not None:
            self.transit_router_multicast_domain_description = m.get('TransitRouterMulticastDomainDescription')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        if m.get('TransitRouterMulticastDomainName') is not None:
            self.transit_router_multicast_domain_name = m.get('TransitRouterMulticastDomainName')
        return self


class ListTransitRouterMulticastDomainsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_multicast_domains=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_multicast_domains = transit_router_multicast_domains  # type: list[ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomains]

    def validate(self):
        if self.transit_router_multicast_domains:
            for k in self.transit_router_multicast_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainsResponseBody, self).to_map()
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
        result['TransitRouterMulticastDomains'] = []
        if self.transit_router_multicast_domains is not None:
            for k in self.transit_router_multicast_domains:
                result['TransitRouterMulticastDomains'].append(k.to_map() if k else None)
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
        self.transit_router_multicast_domains = []
        if m.get('TransitRouterMulticastDomains') is not None:
            for k in m.get('TransitRouterMulticastDomains'):
                temp_model = ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomains()
                self.transit_router_multicast_domains.append(temp_model.from_map(k))
        return self


class ListTransitRouterMulticastDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterMulticastDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterMulticastDomainsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterMulticastDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterMulticastGroupsRequest(TeaModel):
    def __init__(self, client_token=None, connect_peer_ids=None, group_ip_address=None, max_results=None,
                 next_token=None, owner_account=None, owner_id=None, peer_transit_router_multicast_domains=None,
                 resource_id=None, resource_owner_account=None, resource_owner_id=None, resource_type=None,
                 transit_router_attachment_id=None, transit_router_multicast_domain_id=None, v_switch_ids=None):
        self.client_token = client_token  # type: str
        self.connect_peer_ids = connect_peer_ids  # type: list[str]
        self.group_ip_address = group_ip_address  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.peer_transit_router_multicast_domains = peer_transit_router_multicast_domains  # type: list[str]
        self.resource_id = resource_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str
        self.v_switch_ids = v_switch_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterMulticastGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connect_peer_ids is not None:
            result['ConnectPeerIds'] = self.connect_peer_ids
        if self.group_ip_address is not None:
            result['GroupIpAddress'] = self.group_ip_address
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.peer_transit_router_multicast_domains is not None:
            result['PeerTransitRouterMulticastDomains'] = self.peer_transit_router_multicast_domains
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectPeerIds') is not None:
            self.connect_peer_ids = m.get('ConnectPeerIds')
        if m.get('GroupIpAddress') is not None:
            self.group_ip_address = m.get('GroupIpAddress')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PeerTransitRouterMulticastDomains') is not None:
            self.peer_transit_router_multicast_domains = m.get('PeerTransitRouterMulticastDomains')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class ListTransitRouterMulticastGroupsResponseBodyTransitRouterMulticastGroups(TeaModel):
    def __init__(self, group_ip_address=None, group_member=None, group_source=None, member_type=None,
                 network_interface_id=None, peer_transit_router_multicast_domain_id=None, resource_id=None, resource_owner_id=None,
                 resource_type=None, source_type=None, status=None, transit_router_attachment_id=None, v_switch_id=None):
        self.group_ip_address = group_ip_address  # type: str
        self.group_member = group_member  # type: bool
        self.group_source = group_source  # type: bool
        self.member_type = member_type  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.peer_transit_router_multicast_domain_id = peer_transit_router_multicast_domain_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.source_type = source_type  # type: str
        self.status = status  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterMulticastGroupsResponseBodyTransitRouterMulticastGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_ip_address is not None:
            result['GroupIpAddress'] = self.group_ip_address
        if self.group_member is not None:
            result['GroupMember'] = self.group_member
        if self.group_source is not None:
            result['GroupSource'] = self.group_source
        if self.member_type is not None:
            result['MemberType'] = self.member_type
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.peer_transit_router_multicast_domain_id is not None:
            result['PeerTransitRouterMulticastDomainId'] = self.peer_transit_router_multicast_domain_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupIpAddress') is not None:
            self.group_ip_address = m.get('GroupIpAddress')
        if m.get('GroupMember') is not None:
            self.group_member = m.get('GroupMember')
        if m.get('GroupSource') is not None:
            self.group_source = m.get('GroupSource')
        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PeerTransitRouterMulticastDomainId') is not None:
            self.peer_transit_router_multicast_domain_id = m.get('PeerTransitRouterMulticastDomainId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class ListTransitRouterMulticastGroupsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_multicast_groups=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_multicast_groups = transit_router_multicast_groups  # type: list[ListTransitRouterMulticastGroupsResponseBodyTransitRouterMulticastGroups]

    def validate(self):
        if self.transit_router_multicast_groups:
            for k in self.transit_router_multicast_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterMulticastGroupsResponseBody, self).to_map()
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
        result['TransitRouterMulticastGroups'] = []
        if self.transit_router_multicast_groups is not None:
            for k in self.transit_router_multicast_groups:
                result['TransitRouterMulticastGroups'].append(k.to_map() if k else None)
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
        self.transit_router_multicast_groups = []
        if m.get('TransitRouterMulticastGroups') is not None:
            for k in m.get('TransitRouterMulticastGroups'):
                temp_model = ListTransitRouterMulticastGroupsResponseBodyTransitRouterMulticastGroups()
                self.transit_router_multicast_groups.append(temp_model.from_map(k))
        return self


class ListTransitRouterMulticastGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterMulticastGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterMulticastGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterMulticastGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterPeerAttachmentsRequest(TeaModel):
    def __init__(self, cen_id=None, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_id=None):
        self.cen_id = cen_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterPeerAttachmentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class ListTransitRouterPeerAttachmentsResponseBodyTransitRouterAttachments(TeaModel):
    def __init__(self, auto_publish_route_enabled=None, bandwidth=None, bandwidth_type=None,
                 cen_bandwidth_package_id=None, creation_time=None, geographic_span_id=None, peer_transit_router_id=None,
                 peer_transit_router_owner_id=None, peer_transit_router_region_id=None, region_id=None, resource_type=None, status=None,
                 transit_router_attachment_description=None, transit_router_attachment_id=None, transit_router_attachment_name=None,
                 transit_router_id=None):
        self.auto_publish_route_enabled = auto_publish_route_enabled  # type: bool
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.creation_time = creation_time  # type: str
        self.geographic_span_id = geographic_span_id  # type: str
        self.peer_transit_router_id = peer_transit_router_id  # type: str
        self.peer_transit_router_owner_id = peer_transit_router_owner_id  # type: long
        self.peer_transit_router_region_id = peer_transit_router_region_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterPeerAttachmentsResponseBodyTransitRouterAttachments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.peer_transit_router_id is not None:
            result['PeerTransitRouterId'] = self.peer_transit_router_id
        if self.peer_transit_router_owner_id is not None:
            result['PeerTransitRouterOwnerId'] = self.peer_transit_router_owner_id
        if self.peer_transit_router_region_id is not None:
            result['PeerTransitRouterRegionId'] = self.peer_transit_router_region_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('PeerTransitRouterId') is not None:
            self.peer_transit_router_id = m.get('PeerTransitRouterId')
        if m.get('PeerTransitRouterOwnerId') is not None:
            self.peer_transit_router_owner_id = m.get('PeerTransitRouterOwnerId')
        if m.get('PeerTransitRouterRegionId') is not None:
            self.peer_transit_router_region_id = m.get('PeerTransitRouterRegionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class ListTransitRouterPeerAttachmentsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_attachments=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_attachments = transit_router_attachments  # type: list[ListTransitRouterPeerAttachmentsResponseBodyTransitRouterAttachments]

    def validate(self):
        if self.transit_router_attachments:
            for k in self.transit_router_attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterPeerAttachmentsResponseBody, self).to_map()
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
        result['TransitRouterAttachments'] = []
        if self.transit_router_attachments is not None:
            for k in self.transit_router_attachments:
                result['TransitRouterAttachments'].append(k.to_map() if k else None)
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
        self.transit_router_attachments = []
        if m.get('TransitRouterAttachments') is not None:
            for k in m.get('TransitRouterAttachments'):
                temp_model = ListTransitRouterPeerAttachmentsResponseBodyTransitRouterAttachments()
                self.transit_router_attachments.append(temp_model.from_map(k))
        return self


class ListTransitRouterPeerAttachmentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterPeerAttachmentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterPeerAttachmentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterPeerAttachmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterPrefixListAssociationRequest(TeaModel):
    def __init__(self, next_hop=None, next_hop_type=None, owner_account=None, owner_id=None, owner_uid=None,
                 page_number=None, page_size=None, prefix_list_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None, transit_router_id=None, transit_router_table_id=None):
        self.next_hop = next_hop  # type: str
        self.next_hop_type = next_hop_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.owner_uid = owner_uid  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.prefix_list_id = prefix_list_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_table_id = transit_router_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterPrefixListAssociationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_table_id is not None:
            result['TransitRouterTableId'] = self.transit_router_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterTableId') is not None:
            self.transit_router_table_id = m.get('TransitRouterTableId')
        return self


class ListTransitRouterPrefixListAssociationResponseBodyPrefixLists(TeaModel):
    def __init__(self, next_hop=None, next_hop_instance_id=None, next_hop_type=None, owner_uid=None,
                 prefix_list_id=None, status=None, transit_router_id=None, transit_router_table_id=None):
        self.next_hop = next_hop  # type: str
        self.next_hop_instance_id = next_hop_instance_id  # type: str
        self.next_hop_type = next_hop_type  # type: str
        self.owner_uid = owner_uid  # type: long
        self.prefix_list_id = prefix_list_id  # type: str
        self.status = status  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_table_id = transit_router_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterPrefixListAssociationResponseBodyPrefixLists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_hop is not None:
            result['NextHop'] = self.next_hop
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_table_id is not None:
            result['TransitRouterTableId'] = self.transit_router_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterTableId') is not None:
            self.transit_router_table_id = m.get('TransitRouterTableId')
        return self


class ListTransitRouterPrefixListAssociationResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, prefix_lists=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.prefix_lists = prefix_lists  # type: list[ListTransitRouterPrefixListAssociationResponseBodyPrefixLists]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.prefix_lists:
            for k in self.prefix_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterPrefixListAssociationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PrefixLists'] = []
        if self.prefix_lists is not None:
            for k in self.prefix_lists:
                result['PrefixLists'].append(k.to_map() if k else None)
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
        self.prefix_lists = []
        if m.get('PrefixLists') is not None:
            for k in m.get('PrefixLists'):
                temp_model = ListTransitRouterPrefixListAssociationResponseBodyPrefixLists()
                self.prefix_lists.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTransitRouterPrefixListAssociationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterPrefixListAssociationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterPrefixListAssociationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterPrefixListAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterRouteEntriesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_route_entry_destination_cidr_block=None,
                 transit_router_route_entry_ids=None, transit_router_route_entry_names=None, transit_router_route_entry_status=None,
                 transit_router_route_table_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_route_entry_destination_cidr_block = transit_router_route_entry_destination_cidr_block  # type: str
        self.transit_router_route_entry_ids = transit_router_route_entry_ids  # type: list[str]
        self.transit_router_route_entry_names = transit_router_route_entry_names  # type: list[str]
        self.transit_router_route_entry_status = transit_router_route_entry_status  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterRouteEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_route_entry_destination_cidr_block is not None:
            result['TransitRouterRouteEntryDestinationCidrBlock'] = self.transit_router_route_entry_destination_cidr_block
        if self.transit_router_route_entry_ids is not None:
            result['TransitRouterRouteEntryIds'] = self.transit_router_route_entry_ids
        if self.transit_router_route_entry_names is not None:
            result['TransitRouterRouteEntryNames'] = self.transit_router_route_entry_names
        if self.transit_router_route_entry_status is not None:
            result['TransitRouterRouteEntryStatus'] = self.transit_router_route_entry_status
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterRouteEntryDestinationCidrBlock') is not None:
            self.transit_router_route_entry_destination_cidr_block = m.get('TransitRouterRouteEntryDestinationCidrBlock')
        if m.get('TransitRouterRouteEntryIds') is not None:
            self.transit_router_route_entry_ids = m.get('TransitRouterRouteEntryIds')
        if m.get('TransitRouterRouteEntryNames') is not None:
            self.transit_router_route_entry_names = m.get('TransitRouterRouteEntryNames')
        if m.get('TransitRouterRouteEntryStatus') is not None:
            self.transit_router_route_entry_status = m.get('TransitRouterRouteEntryStatus')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class ListTransitRouterRouteEntriesResponseBodyTransitRouterRouteEntries(TeaModel):
    def __init__(self, create_time=None, operational_mode=None, tag=None,
                 transit_router_route_entry_description=None, transit_router_route_entry_destination_cidr_block=None,
                 transit_router_route_entry_id=None, transit_router_route_entry_name=None, transit_router_route_entry_next_hop_id=None,
                 transit_router_route_entry_next_hop_type=None, transit_router_route_entry_status=None, transit_router_route_entry_type=None):
        self.create_time = create_time  # type: str
        self.operational_mode = operational_mode  # type: bool
        self.tag = tag  # type: str
        self.transit_router_route_entry_description = transit_router_route_entry_description  # type: str
        self.transit_router_route_entry_destination_cidr_block = transit_router_route_entry_destination_cidr_block  # type: str
        self.transit_router_route_entry_id = transit_router_route_entry_id  # type: str
        self.transit_router_route_entry_name = transit_router_route_entry_name  # type: str
        self.transit_router_route_entry_next_hop_id = transit_router_route_entry_next_hop_id  # type: str
        self.transit_router_route_entry_next_hop_type = transit_router_route_entry_next_hop_type  # type: str
        self.transit_router_route_entry_status = transit_router_route_entry_status  # type: str
        self.transit_router_route_entry_type = transit_router_route_entry_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterRouteEntriesResponseBodyTransitRouterRouteEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.operational_mode is not None:
            result['OperationalMode'] = self.operational_mode
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.transit_router_route_entry_description is not None:
            result['TransitRouterRouteEntryDescription'] = self.transit_router_route_entry_description
        if self.transit_router_route_entry_destination_cidr_block is not None:
            result['TransitRouterRouteEntryDestinationCidrBlock'] = self.transit_router_route_entry_destination_cidr_block
        if self.transit_router_route_entry_id is not None:
            result['TransitRouterRouteEntryId'] = self.transit_router_route_entry_id
        if self.transit_router_route_entry_name is not None:
            result['TransitRouterRouteEntryName'] = self.transit_router_route_entry_name
        if self.transit_router_route_entry_next_hop_id is not None:
            result['TransitRouterRouteEntryNextHopId'] = self.transit_router_route_entry_next_hop_id
        if self.transit_router_route_entry_next_hop_type is not None:
            result['TransitRouterRouteEntryNextHopType'] = self.transit_router_route_entry_next_hop_type
        if self.transit_router_route_entry_status is not None:
            result['TransitRouterRouteEntryStatus'] = self.transit_router_route_entry_status
        if self.transit_router_route_entry_type is not None:
            result['TransitRouterRouteEntryType'] = self.transit_router_route_entry_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OperationalMode') is not None:
            self.operational_mode = m.get('OperationalMode')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TransitRouterRouteEntryDescription') is not None:
            self.transit_router_route_entry_description = m.get('TransitRouterRouteEntryDescription')
        if m.get('TransitRouterRouteEntryDestinationCidrBlock') is not None:
            self.transit_router_route_entry_destination_cidr_block = m.get('TransitRouterRouteEntryDestinationCidrBlock')
        if m.get('TransitRouterRouteEntryId') is not None:
            self.transit_router_route_entry_id = m.get('TransitRouterRouteEntryId')
        if m.get('TransitRouterRouteEntryName') is not None:
            self.transit_router_route_entry_name = m.get('TransitRouterRouteEntryName')
        if m.get('TransitRouterRouteEntryNextHopId') is not None:
            self.transit_router_route_entry_next_hop_id = m.get('TransitRouterRouteEntryNextHopId')
        if m.get('TransitRouterRouteEntryNextHopType') is not None:
            self.transit_router_route_entry_next_hop_type = m.get('TransitRouterRouteEntryNextHopType')
        if m.get('TransitRouterRouteEntryStatus') is not None:
            self.transit_router_route_entry_status = m.get('TransitRouterRouteEntryStatus')
        if m.get('TransitRouterRouteEntryType') is not None:
            self.transit_router_route_entry_type = m.get('TransitRouterRouteEntryType')
        return self


class ListTransitRouterRouteEntriesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_route_entries=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_route_entries = transit_router_route_entries  # type: list[ListTransitRouterRouteEntriesResponseBodyTransitRouterRouteEntries]

    def validate(self):
        if self.transit_router_route_entries:
            for k in self.transit_router_route_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterRouteEntriesResponseBody, self).to_map()
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
        result['TransitRouterRouteEntries'] = []
        if self.transit_router_route_entries is not None:
            for k in self.transit_router_route_entries:
                result['TransitRouterRouteEntries'].append(k.to_map() if k else None)
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
        self.transit_router_route_entries = []
        if m.get('TransitRouterRouteEntries') is not None:
            for k in m.get('TransitRouterRouteEntries'):
                temp_model = ListTransitRouterRouteEntriesResponseBodyTransitRouterRouteEntries()
                self.transit_router_route_entries.append(temp_model.from_map(k))
        return self


class ListTransitRouterRouteEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterRouteEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterRouteEntriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterRouteTableAssociationsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_route_table_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterRouteTableAssociationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class ListTransitRouterRouteTableAssociationsResponseBodyTransitRouterAssociations(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, status=None, transit_router_attachment_id=None,
                 transit_router_route_table_id=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterRouteTableAssociationsResponseBodyTransitRouterAssociations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class ListTransitRouterRouteTableAssociationsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_associations=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_associations = transit_router_associations  # type: list[ListTransitRouterRouteTableAssociationsResponseBodyTransitRouterAssociations]

    def validate(self):
        if self.transit_router_associations:
            for k in self.transit_router_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterRouteTableAssociationsResponseBody, self).to_map()
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
        result['TransitRouterAssociations'] = []
        if self.transit_router_associations is not None:
            for k in self.transit_router_associations:
                result['TransitRouterAssociations'].append(k.to_map() if k else None)
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
        self.transit_router_associations = []
        if m.get('TransitRouterAssociations') is not None:
            for k in m.get('TransitRouterAssociations'):
                temp_model = ListTransitRouterRouteTableAssociationsResponseBodyTransitRouterAssociations()
                self.transit_router_associations.append(temp_model.from_map(k))
        return self


class ListTransitRouterRouteTableAssociationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterRouteTableAssociationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterRouteTableAssociationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterRouteTableAssociationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterRouteTablePropagationsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_route_table_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterRouteTablePropagationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class ListTransitRouterRouteTablePropagationsResponseBodyTransitRouterPropagations(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, status=None, transit_router_attachment_id=None,
                 transit_router_route_table_id=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterRouteTablePropagationsResponseBodyTransitRouterPropagations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class ListTransitRouterRouteTablePropagationsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_propagations=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_propagations = transit_router_propagations  # type: list[ListTransitRouterRouteTablePropagationsResponseBodyTransitRouterPropagations]

    def validate(self):
        if self.transit_router_propagations:
            for k in self.transit_router_propagations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterRouteTablePropagationsResponseBody, self).to_map()
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
        result['TransitRouterPropagations'] = []
        if self.transit_router_propagations is not None:
            for k in self.transit_router_propagations:
                result['TransitRouterPropagations'].append(k.to_map() if k else None)
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
        self.transit_router_propagations = []
        if m.get('TransitRouterPropagations') is not None:
            for k in m.get('TransitRouterPropagations'):
                temp_model = ListTransitRouterRouteTablePropagationsResponseBodyTransitRouterPropagations()
                self.transit_router_propagations.append(temp_model.from_map(k))
        return self


class ListTransitRouterRouteTablePropagationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterRouteTablePropagationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterRouteTablePropagationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterRouteTablePropagationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterRouteTablesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_id=None, transit_router_route_table_ids=None,
                 transit_router_route_table_names=None, transit_router_route_table_status=None, transit_router_route_table_type=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_route_table_ids = transit_router_route_table_ids  # type: list[str]
        self.transit_router_route_table_names = transit_router_route_table_names  # type: list[str]
        self.transit_router_route_table_status = transit_router_route_table_status  # type: str
        self.transit_router_route_table_type = transit_router_route_table_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterRouteTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_route_table_ids is not None:
            result['TransitRouterRouteTableIds'] = self.transit_router_route_table_ids
        if self.transit_router_route_table_names is not None:
            result['TransitRouterRouteTableNames'] = self.transit_router_route_table_names
        if self.transit_router_route_table_status is not None:
            result['TransitRouterRouteTableStatus'] = self.transit_router_route_table_status
        if self.transit_router_route_table_type is not None:
            result['TransitRouterRouteTableType'] = self.transit_router_route_table_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterRouteTableIds') is not None:
            self.transit_router_route_table_ids = m.get('TransitRouterRouteTableIds')
        if m.get('TransitRouterRouteTableNames') is not None:
            self.transit_router_route_table_names = m.get('TransitRouterRouteTableNames')
        if m.get('TransitRouterRouteTableStatus') is not None:
            self.transit_router_route_table_status = m.get('TransitRouterRouteTableStatus')
        if m.get('TransitRouterRouteTableType') is not None:
            self.transit_router_route_table_type = m.get('TransitRouterRouteTableType')
        return self


class ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTables(TeaModel):
    def __init__(self, create_time=None, transit_router_route_table_description=None,
                 transit_router_route_table_id=None, transit_router_route_table_name=None, transit_router_route_table_status=None,
                 transit_router_route_table_type=None):
        self.create_time = create_time  # type: str
        self.transit_router_route_table_description = transit_router_route_table_description  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str
        self.transit_router_route_table_name = transit_router_route_table_name  # type: str
        self.transit_router_route_table_status = transit_router_route_table_status  # type: str
        self.transit_router_route_table_type = transit_router_route_table_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.transit_router_route_table_description is not None:
            result['TransitRouterRouteTableDescription'] = self.transit_router_route_table_description
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        if self.transit_router_route_table_name is not None:
            result['TransitRouterRouteTableName'] = self.transit_router_route_table_name
        if self.transit_router_route_table_status is not None:
            result['TransitRouterRouteTableStatus'] = self.transit_router_route_table_status
        if self.transit_router_route_table_type is not None:
            result['TransitRouterRouteTableType'] = self.transit_router_route_table_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TransitRouterRouteTableDescription') is not None:
            self.transit_router_route_table_description = m.get('TransitRouterRouteTableDescription')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        if m.get('TransitRouterRouteTableName') is not None:
            self.transit_router_route_table_name = m.get('TransitRouterRouteTableName')
        if m.get('TransitRouterRouteTableStatus') is not None:
            self.transit_router_route_table_status = m.get('TransitRouterRouteTableStatus')
        if m.get('TransitRouterRouteTableType') is not None:
            self.transit_router_route_table_type = m.get('TransitRouterRouteTableType')
        return self


class ListTransitRouterRouteTablesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_route_tables=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_route_tables = transit_router_route_tables  # type: list[ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTables]

    def validate(self):
        if self.transit_router_route_tables:
            for k in self.transit_router_route_tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterRouteTablesResponseBody, self).to_map()
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
        result['TransitRouterRouteTables'] = []
        if self.transit_router_route_tables is not None:
            for k in self.transit_router_route_tables:
                result['TransitRouterRouteTables'].append(k.to_map() if k else None)
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
        self.transit_router_route_tables = []
        if m.get('TransitRouterRouteTables') is not None:
            for k in m.get('TransitRouterRouteTables'):
                temp_model = ListTransitRouterRouteTablesResponseBodyTransitRouterRouteTables()
                self.transit_router_route_tables.append(temp_model.from_map(k))
        return self


class ListTransitRouterRouteTablesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterRouteTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterRouteTablesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterRouteTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterVbrAttachmentsRequest(TeaModel):
    def __init__(self, cen_id=None, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_id=None):
        self.cen_id = cen_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterVbrAttachmentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class ListTransitRouterVbrAttachmentsResponseBodyTransitRouterAttachments(TeaModel):
    def __init__(self, auto_publish_route_enabled=None, creation_time=None, resource_type=None, status=None,
                 transit_router_attachment_description=None, transit_router_attachment_id=None, transit_router_attachment_name=None,
                 transit_router_id=None, vbr_id=None, vbr_owner_id=None, vbr_region_id=None):
        self.auto_publish_route_enabled = auto_publish_route_enabled  # type: bool
        self.creation_time = creation_time  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.vbr_id = vbr_id  # type: str
        self.vbr_owner_id = vbr_owner_id  # type: long
        self.vbr_region_id = vbr_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterVbrAttachmentsResponseBodyTransitRouterAttachments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        if self.vbr_owner_id is not None:
            result['VbrOwnerId'] = self.vbr_owner_id
        if self.vbr_region_id is not None:
            result['VbrRegionId'] = self.vbr_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        if m.get('VbrOwnerId') is not None:
            self.vbr_owner_id = m.get('VbrOwnerId')
        if m.get('VbrRegionId') is not None:
            self.vbr_region_id = m.get('VbrRegionId')
        return self


class ListTransitRouterVbrAttachmentsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_attachments=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_attachments = transit_router_attachments  # type: list[ListTransitRouterVbrAttachmentsResponseBodyTransitRouterAttachments]

    def validate(self):
        if self.transit_router_attachments:
            for k in self.transit_router_attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterVbrAttachmentsResponseBody, self).to_map()
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
        result['TransitRouterAttachments'] = []
        if self.transit_router_attachments is not None:
            for k in self.transit_router_attachments:
                result['TransitRouterAttachments'].append(k.to_map() if k else None)
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
        self.transit_router_attachments = []
        if m.get('TransitRouterAttachments') is not None:
            for k in m.get('TransitRouterAttachments'):
                temp_model = ListTransitRouterVbrAttachmentsResponseBodyTransitRouterAttachments()
                self.transit_router_attachments.append(temp_model.from_map(k))
        return self


class ListTransitRouterVbrAttachmentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterVbrAttachmentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterVbrAttachmentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterVbrAttachmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterVpcAttachmentsRequest(TeaModel):
    def __init__(self, cen_id=None, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_id=None):
        self.cen_id = cen_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterVpcAttachmentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsZoneMappings(TeaModel):
    def __init__(self, network_interface_id=None, v_switch_id=None, zone_id=None):
        self.network_interface_id = network_interface_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachments(TeaModel):
    def __init__(self, charge_type=None, creation_time=None, resource_type=None, status=None,
                 transit_router_attachment_description=None, transit_router_attachment_id=None, transit_router_attachment_name=None,
                 transit_router_id=None, vpc_id=None, vpc_owner_id=None, vpc_region_id=None, zone_mappings=None):
        self.charge_type = charge_type  # type: str
        self.creation_time = creation_time  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_owner_id = vpc_owner_id  # type: long
        self.vpc_region_id = vpc_region_id  # type: str
        self.zone_mappings = zone_mappings  # type: list[ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsZoneMappings]

    def validate(self):
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id
        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')
        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachmentsZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class ListTransitRouterVpcAttachmentsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_attachments=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_attachments = transit_router_attachments  # type: list[ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachments]

    def validate(self):
        if self.transit_router_attachments:
            for k in self.transit_router_attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterVpcAttachmentsResponseBody, self).to_map()
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
        result['TransitRouterAttachments'] = []
        if self.transit_router_attachments is not None:
            for k in self.transit_router_attachments:
                result['TransitRouterAttachments'].append(k.to_map() if k else None)
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
        self.transit_router_attachments = []
        if m.get('TransitRouterAttachments') is not None:
            for k in m.get('TransitRouterAttachments'):
                temp_model = ListTransitRouterVpcAttachmentsResponseBodyTransitRouterAttachments()
                self.transit_router_attachments.append(temp_model.from_map(k))
        return self


class ListTransitRouterVpcAttachmentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterVpcAttachmentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterVpcAttachmentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterVpcAttachmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRouterVpnAttachmentsRequest(TeaModel):
    def __init__(self, cen_id=None, max_results=None, next_token=None, owner_account=None, owner_id=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_id=None):
        self.cen_id = cen_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterVpnAttachmentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachmentsZones(TeaModel):
    def __init__(self, zone_id=None):
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachmentsZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachments(TeaModel):
    def __init__(self, auto_publish_route_enabled=None, creation_time=None, resource_type=None, status=None,
                 transit_router_attachment_description=None, transit_router_attachment_id=None, transit_router_attachment_name=None,
                 transit_router_id=None, vpn_id=None, vpn_owner_id=None, vpn_region_id=None, zones=None):
        self.auto_publish_route_enabled = auto_publish_route_enabled  # type: bool
        self.creation_time = creation_time  # type: str
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.vpn_id = vpn_id  # type: str
        self.vpn_owner_id = vpn_owner_id  # type: long
        self.vpn_region_id = vpn_region_id  # type: str
        self.zones = zones  # type: list[ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachmentsZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.vpn_id is not None:
            result['VpnId'] = self.vpn_id
        if self.vpn_owner_id is not None:
            result['VpnOwnerId'] = self.vpn_owner_id
        if self.vpn_region_id is not None:
            result['VpnRegionId'] = self.vpn_region_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('VpnId') is not None:
            self.vpn_id = m.get('VpnId')
        if m.get('VpnOwnerId') is not None:
            self.vpn_owner_id = m.get('VpnOwnerId')
        if m.get('VpnRegionId') is not None:
            self.vpn_region_id = m.get('VpnRegionId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachmentsZones()
                self.zones.append(temp_model.from_map(k))
        return self


class ListTransitRouterVpnAttachmentsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 transit_router_attachments=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_router_attachments = transit_router_attachments  # type: list[ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachments]

    def validate(self):
        if self.transit_router_attachments:
            for k in self.transit_router_attachments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRouterVpnAttachmentsResponseBody, self).to_map()
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
        result['TransitRouterAttachments'] = []
        if self.transit_router_attachments is not None:
            for k in self.transit_router_attachments:
                result['TransitRouterAttachments'].append(k.to_map() if k else None)
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
        self.transit_router_attachments = []
        if m.get('TransitRouterAttachments') is not None:
            for k in m.get('TransitRouterAttachments'):
                temp_model = ListTransitRouterVpnAttachmentsResponseBodyTransitRouterAttachments()
                self.transit_router_attachments.append(temp_model.from_map(k))
        return self


class ListTransitRouterVpnAttachmentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRouterVpnAttachmentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRouterVpnAttachmentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRouterVpnAttachmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTransitRoutersRequest(TeaModel):
    def __init__(self, cen_id=None, owner_account=None, owner_id=None, page_number=None, page_size=None,
                 region_id=None, resource_owner_account=None, resource_owner_id=None, transit_router_id=None):
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRoutersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class ListTransitRoutersResponseBodyTransitRoutersTransitRouterCidrList(TeaModel):
    def __init__(self, cidr=None, description=None, name=None, publish_cidr_route=None, transit_router_cidr_id=None):
        self.cidr = cidr  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.publish_cidr_route = publish_cidr_route  # type: bool
        self.transit_router_cidr_id = transit_router_cidr_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTransitRoutersResponseBodyTransitRoutersTransitRouterCidrList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.publish_cidr_route is not None:
            result['PublishCidrRoute'] = self.publish_cidr_route
        if self.transit_router_cidr_id is not None:
            result['TransitRouterCidrId'] = self.transit_router_cidr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PublishCidrRoute') is not None:
            self.publish_cidr_route = m.get('PublishCidrRoute')
        if m.get('TransitRouterCidrId') is not None:
            self.transit_router_cidr_id = m.get('TransitRouterCidrId')
        return self


class ListTransitRoutersResponseBodyTransitRouters(TeaModel):
    def __init__(self, ali_uid=None, cen_id=None, creation_time=None, region_id=None, status=None,
                 support_multicast=None, transit_router_cidr_list=None, transit_router_description=None, transit_router_id=None,
                 transit_router_name=None, type=None):
        self.ali_uid = ali_uid  # type: long
        self.cen_id = cen_id  # type: str
        self.creation_time = creation_time  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.support_multicast = support_multicast  # type: bool
        self.transit_router_cidr_list = transit_router_cidr_list  # type: list[ListTransitRoutersResponseBodyTransitRoutersTransitRouterCidrList]
        self.transit_router_description = transit_router_description  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_name = transit_router_name  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.transit_router_cidr_list:
            for k in self.transit_router_cidr_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRoutersResponseBodyTransitRouters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.support_multicast is not None:
            result['SupportMulticast'] = self.support_multicast
        result['TransitRouterCidrList'] = []
        if self.transit_router_cidr_list is not None:
            for k in self.transit_router_cidr_list:
                result['TransitRouterCidrList'].append(k.to_map() if k else None)
        if self.transit_router_description is not None:
            result['TransitRouterDescription'] = self.transit_router_description
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_name is not None:
            result['TransitRouterName'] = self.transit_router_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportMulticast') is not None:
            self.support_multicast = m.get('SupportMulticast')
        self.transit_router_cidr_list = []
        if m.get('TransitRouterCidrList') is not None:
            for k in m.get('TransitRouterCidrList'):
                temp_model = ListTransitRoutersResponseBodyTransitRoutersTransitRouterCidrList()
                self.transit_router_cidr_list.append(temp_model.from_map(k))
        if m.get('TransitRouterDescription') is not None:
            self.transit_router_description = m.get('TransitRouterDescription')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterName') is not None:
            self.transit_router_name = m.get('TransitRouterName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTransitRoutersResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, transit_routers=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.transit_routers = transit_routers  # type: list[ListTransitRoutersResponseBodyTransitRouters]

    def validate(self):
        if self.transit_routers:
            for k in self.transit_routers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTransitRoutersResponseBody, self).to_map()
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
        result['TransitRouters'] = []
        if self.transit_routers is not None:
            for k in self.transit_routers:
                result['TransitRouters'].append(k.to_map() if k else None)
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
        self.transit_routers = []
        if m.get('TransitRouters') is not None:
            for k in m.get('TransitRouters'):
                temp_model = ListTransitRoutersResponseBodyTransitRouters()
                self.transit_routers.append(temp_model.from_map(k))
        return self


class ListTransitRoutersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTransitRoutersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTransitRoutersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTransitRoutersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCenAttributeRequest(TeaModel):
    def __init__(self, cen_id=None, description=None, name=None, owner_account=None, owner_id=None,
                 protection_level=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.protection_level = protection_level  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCenAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyCenAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCenAttributeResponseBody, self).to_map()
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


class ModifyCenAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyCenAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyCenAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyCenAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCenBandwidthPackageAttributeRequest(TeaModel):
    def __init__(self, cen_bandwidth_package_id=None, description=None, name=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCenBandwidthPackageAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyCenBandwidthPackageAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCenBandwidthPackageAttributeResponseBody, self).to_map()
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


class ModifyCenBandwidthPackageAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyCenBandwidthPackageAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyCenBandwidthPackageAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyCenBandwidthPackageAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCenBandwidthPackageSpecRequest(TeaModel):
    def __init__(self, bandwidth=None, cen_bandwidth_package_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, service_type=None):
        self.bandwidth = bandwidth  # type: int
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCenBandwidthPackageSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ModifyCenBandwidthPackageSpecResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCenBandwidthPackageSpecResponseBody, self).to_map()
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


class ModifyCenBandwidthPackageSpecResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyCenBandwidthPackageSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyCenBandwidthPackageSpecResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyCenBandwidthPackageSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCenRouteMapRequest(TeaModel):
    def __init__(self, as_path_match_mode=None, cen_id=None, cen_region_id=None, cidr_match_mode=None,
                 community_match_mode=None, community_operate_mode=None, description=None, destination_child_instance_types=None,
                 destination_cidr_blocks=None, destination_instance_ids=None, destination_instance_ids_reverse_match=None,
                 destination_route_table_ids=None, map_result=None, match_address_type=None, match_asns=None, match_community_set=None,
                 next_priority=None, operate_community_set=None, owner_account=None, owner_id=None, preference=None,
                 prepend_as_path=None, priority=None, resource_owner_account=None, resource_owner_id=None, route_map_id=None,
                 route_types=None, source_child_instance_types=None, source_instance_ids=None,
                 source_instance_ids_reverse_match=None, source_region_ids=None, source_route_table_ids=None):
        self.as_path_match_mode = as_path_match_mode  # type: str
        self.cen_id = cen_id  # type: str
        self.cen_region_id = cen_region_id  # type: str
        self.cidr_match_mode = cidr_match_mode  # type: str
        self.community_match_mode = community_match_mode  # type: str
        self.community_operate_mode = community_operate_mode  # type: str
        self.description = description  # type: str
        self.destination_child_instance_types = destination_child_instance_types  # type: list[str]
        self.destination_cidr_blocks = destination_cidr_blocks  # type: list[str]
        self.destination_instance_ids = destination_instance_ids  # type: list[str]
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match  # type: bool
        self.destination_route_table_ids = destination_route_table_ids  # type: list[str]
        self.map_result = map_result  # type: str
        self.match_address_type = match_address_type  # type: str
        self.match_asns = match_asns  # type: list[int]
        self.match_community_set = match_community_set  # type: list[str]
        self.next_priority = next_priority  # type: int
        self.operate_community_set = operate_community_set  # type: list[str]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.preference = preference  # type: int
        self.prepend_as_path = prepend_as_path  # type: list[long]
        self.priority = priority  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.route_map_id = route_map_id  # type: str
        self.route_types = route_types  # type: list[str]
        self.source_child_instance_types = source_child_instance_types  # type: list[str]
        self.source_instance_ids = source_instance_ids  # type: list[str]
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match  # type: bool
        self.source_region_ids = source_region_ids  # type: list[str]
        self.source_route_table_ids = source_route_table_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCenRouteMapRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path_match_mode is not None:
            result['AsPathMatchMode'] = self.as_path_match_mode
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.cidr_match_mode is not None:
            result['CidrMatchMode'] = self.cidr_match_mode
        if self.community_match_mode is not None:
            result['CommunityMatchMode'] = self.community_match_mode
        if self.community_operate_mode is not None:
            result['CommunityOperateMode'] = self.community_operate_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_child_instance_types is not None:
            result['DestinationChildInstanceTypes'] = self.destination_child_instance_types
        if self.destination_cidr_blocks is not None:
            result['DestinationCidrBlocks'] = self.destination_cidr_blocks
        if self.destination_instance_ids is not None:
            result['DestinationInstanceIds'] = self.destination_instance_ids
        if self.destination_instance_ids_reverse_match is not None:
            result['DestinationInstanceIdsReverseMatch'] = self.destination_instance_ids_reverse_match
        if self.destination_route_table_ids is not None:
            result['DestinationRouteTableIds'] = self.destination_route_table_ids
        if self.map_result is not None:
            result['MapResult'] = self.map_result
        if self.match_address_type is not None:
            result['MatchAddressType'] = self.match_address_type
        if self.match_asns is not None:
            result['MatchAsns'] = self.match_asns
        if self.match_community_set is not None:
            result['MatchCommunitySet'] = self.match_community_set
        if self.next_priority is not None:
            result['NextPriority'] = self.next_priority
        if self.operate_community_set is not None:
            result['OperateCommunitySet'] = self.operate_community_set
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preference is not None:
            result['Preference'] = self.preference
        if self.prepend_as_path is not None:
            result['PrependAsPath'] = self.prepend_as_path
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.route_types is not None:
            result['RouteTypes'] = self.route_types
        if self.source_child_instance_types is not None:
            result['SourceChildInstanceTypes'] = self.source_child_instance_types
        if self.source_instance_ids is not None:
            result['SourceInstanceIds'] = self.source_instance_ids
        if self.source_instance_ids_reverse_match is not None:
            result['SourceInstanceIdsReverseMatch'] = self.source_instance_ids_reverse_match
        if self.source_region_ids is not None:
            result['SourceRegionIds'] = self.source_region_ids
        if self.source_route_table_ids is not None:
            result['SourceRouteTableIds'] = self.source_route_table_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsPathMatchMode') is not None:
            self.as_path_match_mode = m.get('AsPathMatchMode')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('CidrMatchMode') is not None:
            self.cidr_match_mode = m.get('CidrMatchMode')
        if m.get('CommunityMatchMode') is not None:
            self.community_match_mode = m.get('CommunityMatchMode')
        if m.get('CommunityOperateMode') is not None:
            self.community_operate_mode = m.get('CommunityOperateMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationChildInstanceTypes') is not None:
            self.destination_child_instance_types = m.get('DestinationChildInstanceTypes')
        if m.get('DestinationCidrBlocks') is not None:
            self.destination_cidr_blocks = m.get('DestinationCidrBlocks')
        if m.get('DestinationInstanceIds') is not None:
            self.destination_instance_ids = m.get('DestinationInstanceIds')
        if m.get('DestinationInstanceIdsReverseMatch') is not None:
            self.destination_instance_ids_reverse_match = m.get('DestinationInstanceIdsReverseMatch')
        if m.get('DestinationRouteTableIds') is not None:
            self.destination_route_table_ids = m.get('DestinationRouteTableIds')
        if m.get('MapResult') is not None:
            self.map_result = m.get('MapResult')
        if m.get('MatchAddressType') is not None:
            self.match_address_type = m.get('MatchAddressType')
        if m.get('MatchAsns') is not None:
            self.match_asns = m.get('MatchAsns')
        if m.get('MatchCommunitySet') is not None:
            self.match_community_set = m.get('MatchCommunitySet')
        if m.get('NextPriority') is not None:
            self.next_priority = m.get('NextPriority')
        if m.get('OperateCommunitySet') is not None:
            self.operate_community_set = m.get('OperateCommunitySet')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Preference') is not None:
            self.preference = m.get('Preference')
        if m.get('PrependAsPath') is not None:
            self.prepend_as_path = m.get('PrependAsPath')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('RouteTypes') is not None:
            self.route_types = m.get('RouteTypes')
        if m.get('SourceChildInstanceTypes') is not None:
            self.source_child_instance_types = m.get('SourceChildInstanceTypes')
        if m.get('SourceInstanceIds') is not None:
            self.source_instance_ids = m.get('SourceInstanceIds')
        if m.get('SourceInstanceIdsReverseMatch') is not None:
            self.source_instance_ids_reverse_match = m.get('SourceInstanceIdsReverseMatch')
        if m.get('SourceRegionIds') is not None:
            self.source_region_ids = m.get('SourceRegionIds')
        if m.get('SourceRouteTableIds') is not None:
            self.source_route_table_ids = m.get('SourceRouteTableIds')
        return self


class ModifyCenRouteMapResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCenRouteMapResponseBody, self).to_map()
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


class ModifyCenRouteMapResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyCenRouteMapResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyCenRouteMapResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyCenRouteMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowLogAttributeRequest(TeaModel):
    def __init__(self, cen_id=None, client_token=None, description=None, flow_log_id=None, flow_log_name=None,
                 owner_account=None, owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.flow_log_id = flow_log_id  # type: str
        self.flow_log_name = flow_log_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowLogAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyFlowLogAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowLogAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyFlowLogAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFlowLogAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFlowLogAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFlowLogAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTransitRouterMulticastDomainRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_multicast_domain_description=None,
                 transit_router_multicast_domain_id=None, transit_router_multicast_domain_name=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_multicast_domain_description = transit_router_multicast_domain_description  # type: str
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str
        self.transit_router_multicast_domain_name = transit_router_multicast_domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTransitRouterMulticastDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_multicast_domain_description is not None:
            result['TransitRouterMulticastDomainDescription'] = self.transit_router_multicast_domain_description
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        if self.transit_router_multicast_domain_name is not None:
            result['TransitRouterMulticastDomainName'] = self.transit_router_multicast_domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterMulticastDomainDescription') is not None:
            self.transit_router_multicast_domain_description = m.get('TransitRouterMulticastDomainDescription')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        if m.get('TransitRouterMulticastDomainName') is not None:
            self.transit_router_multicast_domain_name = m.get('TransitRouterMulticastDomainName')
        return self


class ModifyTransitRouterMulticastDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTransitRouterMulticastDomainResponseBody, self).to_map()
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


class ModifyTransitRouterMulticastDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTransitRouterMulticastDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTransitRouterMulticastDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTransitRouterMulticastDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, new_resource_group_id=None, owner_account=None,
                 owner_id=None, resource_id=None, resource_owner_account=None, resource_owner_id=None, resource_type=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.new_resource_group_id = new_resource_group_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_id = resource_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBody, self).to_map()
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MoveResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenTransitRouterServiceRequest(TeaModel):
    def __init__(self, client_token=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.client_token = client_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenTransitRouterServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class OpenTransitRouterServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenTransitRouterServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenTransitRouterServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenTransitRouterServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenTransitRouterServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenTransitRouterServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRouteEntriesRequest(TeaModel):
    def __init__(self, cen_id=None, child_instance_id=None, child_instance_region_id=None,
                 child_instance_route_table_id=None, child_instance_type=None, destination_cidr_block=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_route_table_id = child_instance_route_table_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishRouteEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class PublishRouteEntriesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishRouteEntriesResponseBody, self).to_map()
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


class PublishRouteEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishRouteEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishRouteEntriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterTransitRouterMulticastGroupMembersRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, group_ip_address=None, network_interface_ids=None,
                 owner_account=None, owner_id=None, peer_transit_router_multicast_domains=None, resource_owner_account=None,
                 resource_owner_id=None, transit_router_multicast_domain_id=None, vpc_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.group_ip_address = group_ip_address  # type: str
        self.network_interface_ids = network_interface_ids  # type: list[str]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.peer_transit_router_multicast_domains = peer_transit_router_multicast_domains  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterTransitRouterMulticastGroupMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.group_ip_address is not None:
            result['GroupIpAddress'] = self.group_ip_address
        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.peer_transit_router_multicast_domains is not None:
            result['PeerTransitRouterMulticastDomains'] = self.peer_transit_router_multicast_domains
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GroupIpAddress') is not None:
            self.group_ip_address = m.get('GroupIpAddress')
        if m.get('NetworkInterfaceIds') is not None:
            self.network_interface_ids = m.get('NetworkInterfaceIds')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PeerTransitRouterMulticastDomains') is not None:
            self.peer_transit_router_multicast_domains = m.get('PeerTransitRouterMulticastDomains')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class RegisterTransitRouterMulticastGroupMembersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterTransitRouterMulticastGroupMembersResponseBody, self).to_map()
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


class RegisterTransitRouterMulticastGroupMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterTransitRouterMulticastGroupMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterTransitRouterMulticastGroupMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RegisterTransitRouterMulticastGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterTransitRouterMulticastGroupSourcesRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, group_ip_address=None, network_interface_ids=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 transit_router_multicast_domain_id=None, vpc_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.group_ip_address = group_ip_address  # type: str
        self.network_interface_ids = network_interface_ids  # type: list[str]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterTransitRouterMulticastGroupSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.group_ip_address is not None:
            result['GroupIpAddress'] = self.group_ip_address
        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GroupIpAddress') is not None:
            self.group_ip_address = m.get('GroupIpAddress')
        if m.get('NetworkInterfaceIds') is not None:
            self.network_interface_ids = m.get('NetworkInterfaceIds')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class RegisterTransitRouterMulticastGroupSourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterTransitRouterMulticastGroupSourcesResponseBody, self).to_map()
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


class RegisterTransitRouterMulticastGroupSourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterTransitRouterMulticastGroupSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterTransitRouterMulticastGroupSourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RegisterTransitRouterMulticastGroupSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_mark_rule_ids=None, traffic_marking_policy_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_mark_rule_ids = traffic_mark_rule_ids  # type: list[str]
        self.traffic_marking_policy_id = traffic_marking_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_mark_rule_ids is not None:
            result['TrafficMarkRuleIds'] = self.traffic_mark_rule_ids
        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficMarkRuleIds') is not None:
            self.traffic_mark_rule_ids = m.get('TrafficMarkRuleIds')
        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')
        return self


class RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponseBody, self).to_map()
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


class RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_mark_rule_ids=None, traffic_marking_policy_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_mark_rule_ids = traffic_mark_rule_ids  # type: list[str]
        self.traffic_marking_policy_id = traffic_marking_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_mark_rule_ids is not None:
            result['TrafficMarkRuleIds'] = self.traffic_mark_rule_ids
        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficMarkRuleIds') is not None:
            self.traffic_mark_rule_ids = m.get('TrafficMarkRuleIds')
        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')
        return self


class RemoveTraficMatchRuleFromTrafficMarkingPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveTraficMatchRuleFromTrafficMarkingPolicyResponseBody, self).to_map()
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


class RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveTraficMatchRuleFromTrafficMarkingPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveTraficMatchRuleFromTrafficMarkingPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceTransitRouterRouteTableAssociationRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None,
                 transit_router_route_table_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplaceTransitRouterRouteTableAssociationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        return self


class ReplaceTransitRouterRouteTableAssociationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplaceTransitRouterRouteTableAssociationResponseBody, self).to_map()
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


class ReplaceTransitRouterRouteTableAssociationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReplaceTransitRouterRouteTableAssociationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReplaceTransitRouterRouteTableAssociationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReplaceTransitRouterRouteTableAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResolveAndRouteServiceInCenRequest(TeaModel):
    def __init__(self, access_region_ids=None, cen_id=None, client_token=None, description=None, host=None,
                 host_region_id=None, host_vpc_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.access_region_ids = access_region_ids  # type: list[str]
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.host = host  # type: str
        self.host_region_id = host_region_id  # type: str
        self.host_vpc_id = host_vpc_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResolveAndRouteServiceInCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_region_ids is not None:
            result['AccessRegionIds'] = self.access_region_ids
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.host is not None:
            result['Host'] = self.host
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRegionIds') is not None:
            self.access_region_ids = m.get('AccessRegionIds')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ResolveAndRouteServiceInCenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResolveAndRouteServiceInCenResponseBody, self).to_map()
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


class ResolveAndRouteServiceInCenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResolveAndRouteServiceInCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResolveAndRouteServiceInCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResolveAndRouteServiceInCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeInstanceFromTransitRouterRequest(TeaModel):
    def __init__(self, cen_id=None, cen_owner_id=None, instance_id=None, instance_type=None, owner_account=None,
                 owner_id=None, region_id=None, resource_owner_account=None, resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.cen_owner_id = cen_owner_id  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeInstanceFromTransitRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RevokeInstanceFromTransitRouterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeInstanceFromTransitRouterResponseBody, self).to_map()
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


class RevokeInstanceFromTransitRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RevokeInstanceFromTransitRouterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeInstanceFromTransitRouterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevokeInstanceFromTransitRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RoutePrivateZoneInCenToVpcRequest(TeaModel):
    def __init__(self, access_region_id=None, cen_id=None, host_region_id=None, host_vpc_id=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.access_region_id = access_region_id  # type: str
        self.cen_id = cen_id  # type: str
        self.host_region_id = host_region_id  # type: str
        self.host_vpc_id = host_vpc_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RoutePrivateZoneInCenToVpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RoutePrivateZoneInCenToVpcResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RoutePrivateZoneInCenToVpcResponseBody, self).to_map()
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


class RoutePrivateZoneInCenToVpcResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RoutePrivateZoneInCenToVpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RoutePrivateZoneInCenToVpcResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RoutePrivateZoneInCenToVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCenInterRegionBandwidthLimitRequest(TeaModel):
    def __init__(self, bandwidth_limit=None, cen_id=None, local_region_id=None, opposite_region_id=None,
                 owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.bandwidth_limit = bandwidth_limit  # type: long
        self.cen_id = cen_id  # type: str
        self.local_region_id = local_region_id  # type: str
        self.opposite_region_id = opposite_region_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCenInterRegionBandwidthLimitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id
        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')
        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SetCenInterRegionBandwidthLimitResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCenInterRegionBandwidthLimitResponseBody, self).to_map()
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


class SetCenInterRegionBandwidthLimitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetCenInterRegionBandwidthLimitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetCenInterRegionBandwidthLimitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetCenInterRegionBandwidthLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTag, self).to_map()
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


class TagResourcesRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, resource_id=None, resource_owner_account=None,
                 resource_owner_id=None, resource_type=None, tag=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TempUpgradeCenBandwidthPackageSpecRequest(TeaModel):
    def __init__(self, bandwidth=None, cen_bandwidth_package_id=None, end_time=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.bandwidth = bandwidth  # type: int
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TempUpgradeCenBandwidthPackageSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class TempUpgradeCenBandwidthPackageSpecResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TempUpgradeCenBandwidthPackageSpecResponseBody, self).to_map()
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


class TempUpgradeCenBandwidthPackageSpecResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TempUpgradeCenBandwidthPackageSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TempUpgradeCenBandwidthPackageSpecResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TempUpgradeCenBandwidthPackageSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassociateCenBandwidthPackageRequest(TeaModel):
    def __init__(self, cen_bandwidth_package_id=None, cen_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnassociateCenBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UnassociateCenBandwidthPackageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnassociateCenBandwidthPackageResponseBody, self).to_map()
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


class UnassociateCenBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnassociateCenBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnassociateCenBandwidthPackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnassociateCenBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnroutePrivateZoneInCenToVpcRequest(TeaModel):
    def __init__(self, access_region_id=None, cen_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.access_region_id = access_region_id  # type: str
        self.cen_id = cen_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnroutePrivateZoneInCenToVpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UnroutePrivateZoneInCenToVpcResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnroutePrivateZoneInCenToVpcResponseBody, self).to_map()
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


class UnroutePrivateZoneInCenToVpcResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnroutePrivateZoneInCenToVpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnroutePrivateZoneInCenToVpcResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnroutePrivateZoneInCenToVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, owner_account=None, owner_id=None, resource_id=None, resource_owner_account=None,
                 resource_owner_id=None, resource_type=None, tag_key=None):
        self.all = all  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCenInterRegionTrafficQosPolicyAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_qos_policy_description=None, traffic_qos_policy_id=None,
                 traffic_qos_policy_name=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_qos_policy_description = traffic_qos_policy_description  # type: str
        self.traffic_qos_policy_id = traffic_qos_policy_id  # type: str
        self.traffic_qos_policy_name = traffic_qos_policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCenInterRegionTrafficQosPolicyAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_qos_policy_description is not None:
            result['TrafficQosPolicyDescription'] = self.traffic_qos_policy_description
        if self.traffic_qos_policy_id is not None:
            result['TrafficQosPolicyId'] = self.traffic_qos_policy_id
        if self.traffic_qos_policy_name is not None:
            result['TrafficQosPolicyName'] = self.traffic_qos_policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficQosPolicyDescription') is not None:
            self.traffic_qos_policy_description = m.get('TrafficQosPolicyDescription')
        if m.get('TrafficQosPolicyId') is not None:
            self.traffic_qos_policy_id = m.get('TrafficQosPolicyId')
        if m.get('TrafficQosPolicyName') is not None:
            self.traffic_qos_policy_name = m.get('TrafficQosPolicyName')
        return self


class UpdateCenInterRegionTrafficQosPolicyAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCenInterRegionTrafficQosPolicyAttributeResponseBody, self).to_map()
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


class UpdateCenInterRegionTrafficQosPolicyAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCenInterRegionTrafficQosPolicyAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCenInterRegionTrafficQosPolicyAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCenInterRegionTrafficQosPolicyAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCenInterRegionTrafficQosQueueAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, dscps=None, owner_account=None, owner_id=None,
                 qos_queue_description=None, qos_queue_id=None, qos_queue_name=None, remain_bandwidth_percent=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.dscps = dscps  # type: list[int]
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.qos_queue_description = qos_queue_description  # type: str
        self.qos_queue_id = qos_queue_id  # type: str
        self.qos_queue_name = qos_queue_name  # type: str
        self.remain_bandwidth_percent = remain_bandwidth_percent  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCenInterRegionTrafficQosQueueAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.dscps is not None:
            result['Dscps'] = self.dscps
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qos_queue_description is not None:
            result['QosQueueDescription'] = self.qos_queue_description
        if self.qos_queue_id is not None:
            result['QosQueueId'] = self.qos_queue_id
        if self.qos_queue_name is not None:
            result['QosQueueName'] = self.qos_queue_name
        if self.remain_bandwidth_percent is not None:
            result['RemainBandwidthPercent'] = self.remain_bandwidth_percent
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Dscps') is not None:
            self.dscps = m.get('Dscps')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QosQueueDescription') is not None:
            self.qos_queue_description = m.get('QosQueueDescription')
        if m.get('QosQueueId') is not None:
            self.qos_queue_id = m.get('QosQueueId')
        if m.get('QosQueueName') is not None:
            self.qos_queue_name = m.get('QosQueueName')
        if m.get('RemainBandwidthPercent') is not None:
            self.remain_bandwidth_percent = m.get('RemainBandwidthPercent')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateCenInterRegionTrafficQosQueueAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCenInterRegionTrafficQosQueueAttributeResponseBody, self).to_map()
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


class UpdateCenInterRegionTrafficQosQueueAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCenInterRegionTrafficQosQueueAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCenInterRegionTrafficQosQueueAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCenInterRegionTrafficQosQueueAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrafficMarkingPolicyAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, traffic_marking_policy_description=None,
                 traffic_marking_policy_id=None, traffic_marking_policy_name=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.traffic_marking_policy_description = traffic_marking_policy_description  # type: str
        self.traffic_marking_policy_id = traffic_marking_policy_id  # type: str
        self.traffic_marking_policy_name = traffic_marking_policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrafficMarkingPolicyAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.traffic_marking_policy_description is not None:
            result['TrafficMarkingPolicyDescription'] = self.traffic_marking_policy_description
        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id
        if self.traffic_marking_policy_name is not None:
            result['TrafficMarkingPolicyName'] = self.traffic_marking_policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TrafficMarkingPolicyDescription') is not None:
            self.traffic_marking_policy_description = m.get('TrafficMarkingPolicyDescription')
        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')
        if m.get('TrafficMarkingPolicyName') is not None:
            self.traffic_marking_policy_name = m.get('TrafficMarkingPolicyName')
        return self


class UpdateTrafficMarkingPolicyAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrafficMarkingPolicyAttributeResponseBody, self).to_map()
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


class UpdateTrafficMarkingPolicyAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTrafficMarkingPolicyAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTrafficMarkingPolicyAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTrafficMarkingPolicyAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTransitRouterRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_description=None, transit_router_id=None,
                 transit_router_name=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_description = transit_router_description  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_name = transit_router_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_description is not None:
            result['TransitRouterDescription'] = self.transit_router_description
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_name is not None:
            result['TransitRouterName'] = self.transit_router_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterDescription') is not None:
            self.transit_router_description = m.get('TransitRouterDescription')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterName') is not None:
            self.transit_router_name = m.get('TransitRouterName')
        return self


class UpdateTransitRouterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterResponseBody, self).to_map()
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


class UpdateTransitRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTransitRouterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTransitRouterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTransitRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTransitRouterPeerAttachmentAttributeRequest(TeaModel):
    def __init__(self, auto_publish_route_enabled=None, bandwidth=None, bandwidth_type=None,
                 cen_bandwidth_package_id=None, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_description=None,
                 transit_router_attachment_id=None, transit_router_attachment_name=None):
        self.auto_publish_route_enabled = auto_publish_route_enabled  # type: bool
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.cen_bandwidth_package_id = cen_bandwidth_package_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterPeerAttachmentAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        return self


class UpdateTransitRouterPeerAttachmentAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterPeerAttachmentAttributeResponseBody, self).to_map()
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


class UpdateTransitRouterPeerAttachmentAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTransitRouterPeerAttachmentAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTransitRouterPeerAttachmentAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTransitRouterPeerAttachmentAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTransitRouterRouteEntryRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_route_entry_description=None,
                 transit_router_route_entry_id=None, transit_router_route_entry_name=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_route_entry_description = transit_router_route_entry_description  # type: str
        self.transit_router_route_entry_id = transit_router_route_entry_id  # type: str
        self.transit_router_route_entry_name = transit_router_route_entry_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterRouteEntryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_route_entry_description is not None:
            result['TransitRouterRouteEntryDescription'] = self.transit_router_route_entry_description
        if self.transit_router_route_entry_id is not None:
            result['TransitRouterRouteEntryId'] = self.transit_router_route_entry_id
        if self.transit_router_route_entry_name is not None:
            result['TransitRouterRouteEntryName'] = self.transit_router_route_entry_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterRouteEntryDescription') is not None:
            self.transit_router_route_entry_description = m.get('TransitRouterRouteEntryDescription')
        if m.get('TransitRouterRouteEntryId') is not None:
            self.transit_router_route_entry_id = m.get('TransitRouterRouteEntryId')
        if m.get('TransitRouterRouteEntryName') is not None:
            self.transit_router_route_entry_name = m.get('TransitRouterRouteEntryName')
        return self


class UpdateTransitRouterRouteEntryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterRouteEntryResponseBody, self).to_map()
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


class UpdateTransitRouterRouteEntryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTransitRouterRouteEntryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTransitRouterRouteEntryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTransitRouterRouteEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTransitRouterRouteTableRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_route_table_description=None,
                 transit_router_route_table_id=None, transit_router_route_table_name=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_route_table_description = transit_router_route_table_description  # type: str
        self.transit_router_route_table_id = transit_router_route_table_id  # type: str
        self.transit_router_route_table_name = transit_router_route_table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterRouteTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_route_table_description is not None:
            result['TransitRouterRouteTableDescription'] = self.transit_router_route_table_description
        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id
        if self.transit_router_route_table_name is not None:
            result['TransitRouterRouteTableName'] = self.transit_router_route_table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterRouteTableDescription') is not None:
            self.transit_router_route_table_description = m.get('TransitRouterRouteTableDescription')
        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')
        if m.get('TransitRouterRouteTableName') is not None:
            self.transit_router_route_table_name = m.get('TransitRouterRouteTableName')
        return self


class UpdateTransitRouterRouteTableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterRouteTableResponseBody, self).to_map()
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


class UpdateTransitRouterRouteTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTransitRouterRouteTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTransitRouterRouteTableResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTransitRouterRouteTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTransitRouterVbrAttachmentAttributeRequest(TeaModel):
    def __init__(self, auto_publish_route_enabled=None, client_token=None, dry_run=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 transit_router_attachment_description=None, transit_router_attachment_id=None, transit_router_attachment_name=None):
        self.auto_publish_route_enabled = auto_publish_route_enabled  # type: bool
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterVbrAttachmentAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        return self


class UpdateTransitRouterVbrAttachmentAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterVbrAttachmentAttributeResponseBody, self).to_map()
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


class UpdateTransitRouterVbrAttachmentAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTransitRouterVbrAttachmentAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTransitRouterVbrAttachmentAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTransitRouterVbrAttachmentAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTransitRouterVpcAttachmentAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, transit_router_attachment_description=None,
                 transit_router_attachment_id=None, transit_router_attachment_name=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterVpcAttachmentAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        return self


class UpdateTransitRouterVpcAttachmentAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterVpcAttachmentAttributeResponseBody, self).to_map()
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


class UpdateTransitRouterVpcAttachmentAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTransitRouterVpcAttachmentAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTransitRouterVpcAttachmentAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTransitRouterVpcAttachmentAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTransitRouterVpcAttachmentZonesRequestAddZoneMappings(TeaModel):
    def __init__(self, v_switch_id=None, zone_id=None):
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterVpcAttachmentZonesRequestAddZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateTransitRouterVpcAttachmentZonesRequestRemoveZoneMappings(TeaModel):
    def __init__(self, v_switch_id=None, zone_id=None):
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterVpcAttachmentZonesRequestRemoveZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateTransitRouterVpcAttachmentZonesRequest(TeaModel):
    def __init__(self, add_zone_mappings=None, client_token=None, dry_run=None, owner_account=None, owner_id=None,
                 remove_zone_mappings=None, resource_owner_account=None, resource_owner_id=None, transit_router_attachment_id=None):
        self.add_zone_mappings = add_zone_mappings  # type: list[UpdateTransitRouterVpcAttachmentZonesRequestAddZoneMappings]
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.remove_zone_mappings = remove_zone_mappings  # type: list[UpdateTransitRouterVpcAttachmentZonesRequestRemoveZoneMappings]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str

    def validate(self):
        if self.add_zone_mappings:
            for k in self.add_zone_mappings:
                if k:
                    k.validate()
        if self.remove_zone_mappings:
            for k in self.remove_zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateTransitRouterVpcAttachmentZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AddZoneMappings'] = []
        if self.add_zone_mappings is not None:
            for k in self.add_zone_mappings:
                result['AddZoneMappings'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        result['RemoveZoneMappings'] = []
        if self.remove_zone_mappings is not None:
            for k in self.remove_zone_mappings:
                result['RemoveZoneMappings'].append(k.to_map() if k else None)
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.add_zone_mappings = []
        if m.get('AddZoneMappings') is not None:
            for k in m.get('AddZoneMappings'):
                temp_model = UpdateTransitRouterVpcAttachmentZonesRequestAddZoneMappings()
                self.add_zone_mappings.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        self.remove_zone_mappings = []
        if m.get('RemoveZoneMappings') is not None:
            for k in m.get('RemoveZoneMappings'):
                temp_model = UpdateTransitRouterVpcAttachmentZonesRequestRemoveZoneMappings()
                self.remove_zone_mappings.append(temp_model.from_map(k))
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        return self


class UpdateTransitRouterVpcAttachmentZonesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterVpcAttachmentZonesResponseBody, self).to_map()
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


class UpdateTransitRouterVpcAttachmentZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTransitRouterVpcAttachmentZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTransitRouterVpcAttachmentZonesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTransitRouterVpcAttachmentZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTransitRouterVpnAttachmentAttributeRequest(TeaModel):
    def __init__(self, auto_publish_route_enabled=None, client_token=None, dry_run=None, owner_account=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 transit_router_attachment_description=None, transit_router_attachment_id=None, transit_router_attachment_name=None):
        self.auto_publish_route_enabled = auto_publish_route_enabled  # type: bool
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.transit_router_attachment_description = transit_router_attachment_description  # type: str
        self.transit_router_attachment_id = transit_router_attachment_id  # type: str
        self.transit_router_attachment_name = transit_router_attachment_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterVpnAttachmentAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_publish_route_enabled is not None:
            result['AutoPublishRouteEnabled'] = self.auto_publish_route_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.transit_router_attachment_description is not None:
            result['TransitRouterAttachmentDescription'] = self.transit_router_attachment_description
        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id
        if self.transit_router_attachment_name is not None:
            result['TransitRouterAttachmentName'] = self.transit_router_attachment_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPublishRouteEnabled') is not None:
            self.auto_publish_route_enabled = m.get('AutoPublishRouteEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TransitRouterAttachmentDescription') is not None:
            self.transit_router_attachment_description = m.get('TransitRouterAttachmentDescription')
        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')
        if m.get('TransitRouterAttachmentName') is not None:
            self.transit_router_attachment_name = m.get('TransitRouterAttachmentName')
        return self


class UpdateTransitRouterVpnAttachmentAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTransitRouterVpnAttachmentAttributeResponseBody, self).to_map()
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


class UpdateTransitRouterVpnAttachmentAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTransitRouterVpnAttachmentAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTransitRouterVpnAttachmentAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTransitRouterVpnAttachmentAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WithdrawPublishedRouteEntriesRequest(TeaModel):
    def __init__(self, cen_id=None, child_instance_id=None, child_instance_region_id=None,
                 child_instance_route_table_id=None, child_instance_type=None, destination_cidr_block=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.cen_id = cen_id  # type: str
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_route_table_id = child_instance_route_table_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(WithdrawPublishedRouteEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class WithdrawPublishedRouteEntriesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WithdrawPublishedRouteEntriesResponseBody, self).to_map()
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


class WithdrawPublishedRouteEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: WithdrawPublishedRouteEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WithdrawPublishedRouteEntriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = WithdrawPublishedRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


