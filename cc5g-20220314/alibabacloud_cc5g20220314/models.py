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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddDNSAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachVpcToNetLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachVpcToNetLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthorizationRuleRequest(TeaModel):
    def __init__(self, client_token=None, description=None, destination=None, destination_port=None,
                 destination_type=None, dry_run=None, name=None, policy=None, protocol=None, source_cidr=None,
                 wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.destination = destination  # type: str
        self.destination_port = destination_port  # type: str
        self.destination_type = destination_type  # type: str
        self.dry_run = dry_run  # type: bool
        self.name = name  # type: str
        self.policy = policy  # type: str
        self.protocol = protocol  # type: str
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
        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.protocol is not None:
            result['Protocol'] = self.protocol
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
        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBatchOperateCardsTaskRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, effect_type=None, iccids=None,
                 iccids_oss_file_path=None, name=None, operate_type=None, region_id=None, threshold=None,
                 wireless_cloud_connector_ids=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.effect_type = effect_type  # type: str
        self.iccids = iccids  # type: list[str]
        self.iccids_oss_file_path = iccids_oss_file_path  # type: str
        self.name = name  # type: str
        self.operate_type = operate_type  # type: str
        self.region_id = region_id  # type: str
        self.threshold = threshold  # type: long
        self.wireless_cloud_connector_ids = wireless_cloud_connector_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBatchOperateCardsTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.effect_type is not None:
            result['EffectType'] = self.effect_type
        if self.iccids is not None:
            result['Iccids'] = self.iccids
        if self.iccids_oss_file_path is not None:
            result['IccidsOssFilePath'] = self.iccids_oss_file_path
        if self.name is not None:
            result['Name'] = self.name
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.wireless_cloud_connector_ids is not None:
            result['WirelessCloudConnectorIds'] = self.wireless_cloud_connector_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EffectType') is not None:
            self.effect_type = m.get('EffectType')
        if m.get('Iccids') is not None:
            self.iccids = m.get('Iccids')
        if m.get('IccidsOssFilePath') is not None:
            self.iccids_oss_file_path = m.get('IccidsOssFilePath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('WirelessCloudConnectorIds') is not None:
            self.wireless_cloud_connector_ids = m.get('WirelessCloudConnectorIds')
        return self


class CreateBatchOperateCardsTaskResponseBody(TeaModel):
    def __init__(self, batch_operate_cards_task_id=None, operate_result_oss_file_path=None, request_id=None):
        self.batch_operate_cards_task_id = batch_operate_cards_task_id  # type: str
        self.operate_result_oss_file_path = operate_result_oss_file_path  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBatchOperateCardsTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_operate_cards_task_id is not None:
            result['BatchOperateCardsTaskId'] = self.batch_operate_cards_task_id
        if self.operate_result_oss_file_path is not None:
            result['OperateResultOssFilePath'] = self.operate_result_oss_file_path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchOperateCardsTaskId') is not None:
            self.batch_operate_cards_task_id = m.get('BatchOperateCardsTaskId')
        if m.get('OperateResultOssFilePath') is not None:
            self.operate_result_oss_file_path = m.get('OperateResultOssFilePath')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBatchOperateCardsTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBatchOperateCardsTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBatchOperateCardsTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBatchOperateCardsTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIoTCloudConnectorBackhaulRouteRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, net_link_id=None, wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.net_link_id = net_link_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIoTCloudConnectorBackhaulRouteRequest, self).to_map()
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


class CreateIoTCloudConnectorBackhaulRouteResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIoTCloudConnectorBackhaulRouteResponseBody, self).to_map()
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


class CreateIoTCloudConnectorBackhaulRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIoTCloudConnectorBackhaulRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIoTCloudConnectorBackhaulRouteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateIoTCloudConnectorBackhaulRouteResponseBody()
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
    def __init__(self, business_type=None, client_token=None, description=None, dry_run=None, isp=None, name=None,
                 net_links=None, region_id=None, use_case=None):
        self.business_type = business_type  # type: str
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
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
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
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWirelessCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBatchOperateCardsTaskRequest(TeaModel):
    def __init__(self, batch_operate_cards_task_id=None, client_token=None, dry_run=None, region_id=None):
        self.batch_operate_cards_task_id = batch_operate_cards_task_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBatchOperateCardsTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_operate_cards_task_id is not None:
            result['BatchOperateCardsTaskId'] = self.batch_operate_cards_task_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchOperateCardsTaskId') is not None:
            self.batch_operate_cards_task_id = m.get('BatchOperateCardsTaskId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBatchOperateCardsTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBatchOperateCardsTaskResponseBody, self).to_map()
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


class DeleteBatchOperateCardsTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBatchOperateCardsTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBatchOperateCardsTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBatchOperateCardsTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIoTCloudConnectorBackhaulRouteRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, net_link_id=None, wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.net_link_id = net_link_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorBackhaulRouteRequest, self).to_map()
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


class DeleteIoTCloudConnectorBackhaulRouteResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorBackhaulRouteResponseBody, self).to_map()
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


class DeleteIoTCloudConnectorBackhaulRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIoTCloudConnectorBackhaulRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorBackhaulRouteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIoTCloudConnectorBackhaulRouteResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWirelessCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachVpcFromNetLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachVpcFromNetLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FailCardsRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, iccids=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.iccids = iccids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailCardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.iccids is not None:
            result['Iccids'] = self.iccids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Iccids') is not None:
            self.iccids = m.get('Iccids')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class FailCardsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailCardsResponseBody, self).to_map()
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


class FailCardsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FailCardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FailCardsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FailCardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardRequest(TeaModel):
    def __init__(self, iccid=None):
        self.iccid = iccid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class GetCardResponseBody(TeaModel):
    def __init__(self, apn=None, activated_time=None, alarm_threshold=None, cloud_connector_id=None,
                 description=None, isp=None, iccid=None, imei=None, imsi=None, ip_address=None, limit_threshold=None, lock=None,
                 msisdn=None, name=None, net_type=None, order_id=None, request_id=None, sim_status=None, spec=None,
                 status=None, stop_threshold=None, usage_data_month=None, usage_data_total=None,
                 wireless_cloud_connector_id=None):
        self.apn = apn  # type: str
        self.activated_time = activated_time  # type: str
        self.alarm_threshold = alarm_threshold  # type: long
        self.cloud_connector_id = cloud_connector_id  # type: str
        self.description = description  # type: str
        self.isp = isp  # type: str
        self.iccid = iccid  # type: str
        self.imei = imei  # type: str
        self.imsi = imsi  # type: str
        self.ip_address = ip_address  # type: str
        self.limit_threshold = limit_threshold  # type: long
        self.lock = lock  # type: str
        self.msisdn = msisdn  # type: str
        self.name = name  # type: str
        self.net_type = net_type  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str
        self.sim_status = sim_status  # type: str
        self.spec = spec  # type: str
        self.status = status  # type: str
        self.stop_threshold = stop_threshold  # type: long
        self.usage_data_month = usage_data_month  # type: int
        self.usage_data_total = usage_data_total  # type: long
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['APN'] = self.apn
        if self.activated_time is not None:
            result['ActivatedTime'] = self.activated_time
        if self.alarm_threshold is not None:
            result['AlarmThreshold'] = self.alarm_threshold
        if self.cloud_connector_id is not None:
            result['CloudConnectorId'] = self.cloud_connector_id
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
        if self.limit_threshold is not None:
            result['LimitThreshold'] = self.limit_threshold
        if self.lock is not None:
            result['Lock'] = self.lock
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.name is not None:
            result['Name'] = self.name
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sim_status is not None:
            result['SimStatus'] = self.sim_status
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        if self.stop_threshold is not None:
            result['StopThreshold'] = self.stop_threshold
        if self.usage_data_month is not None:
            result['UsageDataMonth'] = self.usage_data_month
        if self.usage_data_total is not None:
            result['UsageDataTotal'] = self.usage_data_total
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('ActivatedTime') is not None:
            self.activated_time = m.get('ActivatedTime')
        if m.get('AlarmThreshold') is not None:
            self.alarm_threshold = m.get('AlarmThreshold')
        if m.get('CloudConnectorId') is not None:
            self.cloud_connector_id = m.get('CloudConnectorId')
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
        if m.get('LimitThreshold') is not None:
            self.limit_threshold = m.get('LimitThreshold')
        if m.get('Lock') is not None:
            self.lock = m.get('Lock')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SimStatus') is not None:
            self.sim_status = m.get('SimStatus')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StopThreshold') is not None:
            self.stop_threshold = m.get('StopThreshold')
        if m.get('UsageDataMonth') is not None:
            self.usage_data_month = m.get('UsageDataMonth')
        if m.get('UsageDataTotal') is not None:
            self.usage_data_total = m.get('UsageDataTotal')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class GetCardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardLockReasonRequest(TeaModel):
    def __init__(self, iccid=None):
        self.iccid = iccid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardLockReasonRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class GetCardLockReasonResponseBody(TeaModel):
    def __init__(self, lock_reason=None, request_id=None):
        self.lock_reason = lock_reason  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardLockReasonResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCardLockReasonResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCardLockReasonResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCardLockReasonResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCardLockReasonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCreateCustomerInformationRequest(TeaModel):
    def __init__(self, region_id=None, wireless_cloud_connector_id=None):
        self.region_id = region_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCreateCustomerInformationRequest, self).to_map()
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


class GetCreateCustomerInformationResponseBody(TeaModel):
    def __init__(self, can_buy_card=None, request_id=None, url=None):
        self.can_buy_card = can_buy_card  # type: str
        self.request_id = request_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCreateCustomerInformationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_buy_card is not None:
            result['CanBuyCard'] = self.can_buy_card
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanBuyCard') is not None:
            self.can_buy_card = m.get('CanBuyCard')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class GetCreateCustomerInformationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCreateCustomerInformationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCreateCustomerInformationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCreateCustomerInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiagnoseResultForSingleCardRequest(TeaModel):
    def __init__(self, diagnose_task_id=None, region_no=None):
        self.diagnose_task_id = diagnose_task_id  # type: str
        self.region_no = region_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDiagnoseResultForSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnose_task_id is not None:
            result['DiagnoseTaskId'] = self.diagnose_task_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiagnoseTaskId') is not None:
            self.diagnose_task_id = m.get('DiagnoseTaskId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
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
    def __init__(self, begin_time=None, card_ip=None, destination=None, destination_type=None, diagnose_item=None,
                 end_time=None, error_result=None, icc_id=None, request_id=None, status=None,
                 wireless_cloud_connector_id=None):
        self.begin_time = begin_time  # type: long
        self.card_ip = card_ip  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.diagnose_item = diagnose_item  # type: list[GetDiagnoseResultForSingleCardResponseBodyDiagnoseItem]
        self.end_time = end_time  # type: long
        self.error_result = error_result  # type: list[GetDiagnoseResultForSingleCardResponseBodyErrorResult]
        self.icc_id = icc_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

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
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class GetDiagnoseResultForSingleCardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDiagnoseResultForSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDiagnoseResultForSingleCardResponseBody()
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
    def __init__(self, apn=None, create_time=None, description=None, grant_ali_uid=None, isp=None, name=None,
                 net_link_id=None, region_id=None, status=None, v_switchs=None, vpc_id=None):
        self.apn = apn  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.grant_ali_uid = grant_ali_uid  # type: str
        self.isp = isp  # type: str
        self.name = name  # type: str
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
        if self.grant_ali_uid is not None:
            result['GrantAliUid'] = self.grant_ali_uid
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
        if m.get('GrantAliUid') is not None:
            self.grant_ali_uid = m.get('GrantAliUid')
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
    def __init__(self, business_type=None, card_count=None, create_time=None, data_package_id=None,
                 data_package_type=None, description=None, features=None, name=None, net_links=None, region_id=None, request_id=None,
                 service_type=None, status=None, use_case=None, wireless_cloud_connector_id=None):
        self.business_type = business_type  # type: str
        self.card_count = card_count  # type: str
        self.create_time = create_time  # type: str
        self.data_package_id = data_package_id  # type: str
        self.data_package_type = data_package_type  # type: str
        self.description = description  # type: str
        self.features = features  # type: list[str]
        self.name = name  # type: str
        self.net_links = net_links  # type: list[GetWirelessCloudConnectorResponseBodyNetLinks]
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.service_type = service_type  # type: str
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
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
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
        if self.features is not None:
            result['Features'] = self.features
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
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.use_case is not None:
            result['UseCase'] = self.use_case
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
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
        if m.get('Features') is not None:
            self.features = m.get('Features')
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
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UseCase') is not None:
            self.use_case = m.get('UseCase')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class GetWirelessCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWirelessCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWirelessCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantNetLinkRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, grant_ali_uid=None, net_link_id=None,
                 wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.grant_ali_uid = grant_ali_uid  # type: long
        self.net_link_id = net_link_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantNetLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.grant_ali_uid is not None:
            result['GrantAliUid'] = self.grant_ali_uid
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
        if m.get('GrantAliUid') is not None:
            self.grant_ali_uid = m.get('GrantAliUid')
        if m.get('NetLinkId') is not None:
            self.net_link_id = m.get('NetLinkId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class GrantNetLinkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantNetLinkResponseBody, self).to_map()
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


class GrantNetLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GrantNetLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantNetLinkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GrantNetLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAPNsRequest(TeaModel):
    def __init__(self, apn=None, isp=None, max_results=None, next_token=None, region_id=None):
        self.apn = apn  # type: str
        self.isp = isp  # type: str
        self.max_results = max_results  # type: long
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
    def __init__(self, apn=None, description=None, isp=None, name=None, zones=None):
        self.apn = apn  # type: str
        self.description = description  # type: str
        self.isp = isp  # type: str
        self.name = name  # type: str
        self.zones = zones  # type: list[str]

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
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class ListAPNsResponseBody(TeaModel):
    def __init__(self, apns=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.apns = apns  # type: list[ListAPNsResponseBodyAPNs]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAPNsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAPNsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizationRulesRequest(TeaModel):
    def __init__(self, authorization_rule_ids=None, destination=None, destination_port=None, destination_type=None,
                 dns=None, max_results=None, names=None, next_token=None, policy=None, protocol=None, statuses=None,
                 type=None, wireless_cloud_connector_id=None):
        self.authorization_rule_ids = authorization_rule_ids  # type: list[str]
        self.destination = destination  # type: str
        self.destination_port = destination_port  # type: str
        self.destination_type = destination_type  # type: str
        self.dns = dns  # type: bool
        self.max_results = max_results  # type: long
        self.names = names  # type: list[str]
        self.next_token = next_token  # type: str
        self.policy = policy  # type: str
        self.protocol = protocol  # type: str
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
        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port
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
        if self.protocol is not None:
            result['Protocol'] = self.protocol
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
        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')
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
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListAuthorizationRulesResponseBodyAuthorizationRules(TeaModel):
    def __init__(self, authorization_rule_id=None, create_time=None, description=None, destination=None,
                 destination_port=None, destination_type=None, dns=None, name=None, policy=None, protocol=None, source_cidr=None,
                 status=None, type=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.destination = destination  # type: str
        self.destination_port = destination_port  # type: str
        self.destination_type = destination_type  # type: str
        self.dns = dns  # type: bool
        self.name = name  # type: str
        self.policy = policy  # type: str
        self.protocol = protocol  # type: str
        self.source_cidr = source_cidr  # type: str
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
        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dns is not None:
            result['Dns'] = self.dns
        if self.name is not None:
            result['Name'] = self.name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.protocol is not None:
            result['Protocol'] = self.protocol
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
        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Dns') is not None:
            self.dns = m.get('Dns')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
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
        self.authorization_rules = authorization_rules  # type: list[ListAuthorizationRulesResponseBodyAuthorizationRules]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAuthorizationRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAuthorizationRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBatchOperateCardsTasksRequest(TeaModel):
    def __init__(self, batch_operate_cards_task_ids=None, max_results=None, names=None, next_token=None,
                 region_id=None, statuses=None):
        self.batch_operate_cards_task_ids = batch_operate_cards_task_ids  # type: list[str]
        self.max_results = max_results  # type: long
        self.names = names  # type: list[str]
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.statuses = statuses  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBatchOperateCardsTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_operate_cards_task_ids is not None:
            result['BatchOperateCardsTaskIds'] = self.batch_operate_cards_task_ids
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchOperateCardsTaskIds') is not None:
            self.batch_operate_cards_task_ids = m.get('BatchOperateCardsTaskIds')
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
        return self


class ListBatchOperateCardsTasksResponseBodyBatchOperateCardsTasksWirelessCloudConnectors(TeaModel):
    def __init__(self, status=None, wireless_cloud_connector_id=None):
        self.status = status  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBatchOperateCardsTasksResponseBodyBatchOperateCardsTasksWirelessCloudConnectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListBatchOperateCardsTasksResponseBodyBatchOperateCardsTasks(TeaModel):
    def __init__(self, batch_operate_cards_task_id=None, create_time=None, description=None, effect_type=None,
                 iccids_oss_file_path=None, name=None, operate_result_oss_file_path=None, operate_type=None, status=None, threshold=None,
                 wireless_cloud_connectors=None):
        self.batch_operate_cards_task_id = batch_operate_cards_task_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.effect_type = effect_type  # type: str
        self.iccids_oss_file_path = iccids_oss_file_path  # type: str
        self.name = name  # type: str
        self.operate_result_oss_file_path = operate_result_oss_file_path  # type: str
        self.operate_type = operate_type  # type: str
        self.status = status  # type: str
        self.threshold = threshold  # type: str
        self.wireless_cloud_connectors = wireless_cloud_connectors  # type: list[ListBatchOperateCardsTasksResponseBodyBatchOperateCardsTasksWirelessCloudConnectors]

    def validate(self):
        if self.wireless_cloud_connectors:
            for k in self.wireless_cloud_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBatchOperateCardsTasksResponseBodyBatchOperateCardsTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_operate_cards_task_id is not None:
            result['BatchOperateCardsTaskId'] = self.batch_operate_cards_task_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.effect_type is not None:
            result['EffectType'] = self.effect_type
        if self.iccids_oss_file_path is not None:
            result['IccidsOssFilePath'] = self.iccids_oss_file_path
        if self.name is not None:
            result['Name'] = self.name
        if self.operate_result_oss_file_path is not None:
            result['OperateResultOssFilePath'] = self.operate_result_oss_file_path
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.status is not None:
            result['Status'] = self.status
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        result['WirelessCloudConnectors'] = []
        if self.wireless_cloud_connectors is not None:
            for k in self.wireless_cloud_connectors:
                result['WirelessCloudConnectors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchOperateCardsTaskId') is not None:
            self.batch_operate_cards_task_id = m.get('BatchOperateCardsTaskId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectType') is not None:
            self.effect_type = m.get('EffectType')
        if m.get('IccidsOssFilePath') is not None:
            self.iccids_oss_file_path = m.get('IccidsOssFilePath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperateResultOssFilePath') is not None:
            self.operate_result_oss_file_path = m.get('OperateResultOssFilePath')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        self.wireless_cloud_connectors = []
        if m.get('WirelessCloudConnectors') is not None:
            for k in m.get('WirelessCloudConnectors'):
                temp_model = ListBatchOperateCardsTasksResponseBodyBatchOperateCardsTasksWirelessCloudConnectors()
                self.wireless_cloud_connectors.append(temp_model.from_map(k))
        return self


class ListBatchOperateCardsTasksResponseBody(TeaModel):
    def __init__(self, batch_operate_cards_tasks=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        self.batch_operate_cards_tasks = batch_operate_cards_tasks  # type: list[ListBatchOperateCardsTasksResponseBodyBatchOperateCardsTasks]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.batch_operate_cards_tasks:
            for k in self.batch_operate_cards_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBatchOperateCardsTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BatchOperateCardsTasks'] = []
        if self.batch_operate_cards_tasks is not None:
            for k in self.batch_operate_cards_tasks:
                result['BatchOperateCardsTasks'].append(k.to_map() if k else None)
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
        self.batch_operate_cards_tasks = []
        if m.get('BatchOperateCardsTasks') is not None:
            for k in m.get('BatchOperateCardsTasks'):
                temp_model = ListBatchOperateCardsTasksResponseBodyBatchOperateCardsTasks()
                self.batch_operate_cards_tasks.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBatchOperateCardsTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBatchOperateCardsTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBatchOperateCardsTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBatchOperateCardsTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCardsRequest(TeaModel):
    def __init__(self, apn=None, iccid=None, iccids=None, ip_address=None, lock=None, max_results=None, msisdn=None,
                 net_link_id=None, next_token=None, online=None, statuses=None, wireless_cloud_connector_id=None):
        self.apn = apn  # type: str
        self.iccid = iccid  # type: str
        self.iccids = iccids  # type: list[str]
        self.ip_address = ip_address  # type: str
        self.lock = lock  # type: bool
        self.max_results = max_results  # type: long
        self.msisdn = msisdn  # type: str
        self.net_link_id = net_link_id  # type: str
        self.next_token = next_token  # type: str
        self.online = online  # type: bool
        self.statuses = statuses  # type: list[str]
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
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.iccids is not None:
            result['Iccids'] = self.iccids
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.lock is not None:
            result['Lock'] = self.lock
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.net_link_id is not None:
            result['NetLinkId'] = self.net_link_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.online is not None:
            result['Online'] = self.online
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Iccids') is not None:
            self.iccids = m.get('Iccids')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Lock') is not None:
            self.lock = m.get('Lock')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('NetLinkId') is not None:
            self.net_link_id = m.get('NetLinkId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListCardsResponseBodyCards(TeaModel):
    def __init__(self, apn=None, activated_time=None, business_status=None, description=None, isp=None, iccid=None,
                 imei=None, imsi=None, ip_address=None, lock=None, msisdn=None, name=None, net_type=None, order_id=None,
                 spec=None, status=None, usage_data_month=None, usage_data_total=None):
        self.apn = apn  # type: str
        self.activated_time = activated_time  # type: str
        self.business_status = business_status  # type: str
        self.description = description  # type: str
        self.isp = isp  # type: str
        self.iccid = iccid  # type: str
        self.imei = imei  # type: str
        self.imsi = imsi  # type: str
        self.ip_address = ip_address  # type: str
        self.lock = lock  # type: bool
        self.msisdn = msisdn  # type: str
        self.name = name  # type: str
        self.net_type = net_type  # type: str
        self.order_id = order_id  # type: str
        self.spec = spec  # type: str
        self.status = status  # type: str
        self.usage_data_month = usage_data_month  # type: long
        self.usage_data_total = usage_data_total  # type: str

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
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
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
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
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
        if self.usage_data_total is not None:
            result['UsageDataTotal'] = self.usage_data_total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('ActivatedTime') is not None:
            self.activated_time = m.get('ActivatedTime')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
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
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
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
        if m.get('UsageDataTotal') is not None:
            self.usage_data_total = m.get('UsageDataTotal')
        return self


class ListCardsResponseBody(TeaModel):
    def __init__(self, cards=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.cards = cards  # type: list[ListCardsResponseBodyCards]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        self.name = name  # type: str
        self.size = size  # type: str
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
        self.data_packages = data_packages  # type: list[ListDataPackagesResponseBodyDataPackages]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataPackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiagnoseInfoForSingleCardRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_no=None, source=None, source_type=None, status=None,
                 wireless_cloud_connector_id=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_no = region_no  # type: str
        self.source = source  # type: str
        self.source_type = source_type  # type: str
        self.status = status  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDiagnoseInfoForSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListDiagnoseInfoForSingleCardResponseBodyDiagnoseInfo(TeaModel):
    def __init__(self, begin_time=None, card_ip=None, destination=None, destination_type=None,
                 diagnose_task_id=None, diagnose_time=None, end_time=None, icc_id=None, source=None, source_type=None, status=None,
                 wireless_cloud_connector_id=None):
        self.begin_time = begin_time  # type: long
        self.card_ip = card_ip  # type: str
        self.destination = destination  # type: str
        self.destination_type = destination_type  # type: str
        self.diagnose_task_id = diagnose_task_id  # type: str
        self.diagnose_time = diagnose_time  # type: long
        self.end_time = end_time  # type: long
        self.icc_id = icc_id  # type: str
        self.source = source  # type: str
        self.source_type = source_type  # type: str
        self.status = status  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

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
        if self.diagnose_task_id is not None:
            result['DiagnoseTaskId'] = self.diagnose_task_id
        if self.diagnose_time is not None:
            result['DiagnoseTime'] = self.diagnose_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.icc_id is not None:
            result['IccId'] = self.icc_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
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
        if m.get('DiagnoseTaskId') is not None:
            self.diagnose_task_id = m.get('DiagnoseTaskId')
        if m.get('DiagnoseTime') is not None:
            self.diagnose_time = m.get('DiagnoseTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IccId') is not None:
            self.icc_id = m.get('IccId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDiagnoseInfoForSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDiagnoseInfoForSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorBackhaulRouteRequest(TeaModel):
    def __init__(self, net_link_id=None, region_id=None, wireless_cloud_connector_id=None):
        self.net_link_id = net_link_id  # type: str
        self.region_id = region_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorBackhaulRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_link_id is not None:
            result['NetLinkId'] = self.net_link_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetLinkId') is not None:
            self.net_link_id = m.get('NetLinkId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListIoTCloudConnectorBackhaulRouteResponseBodyRoutes(TeaModel):
    def __init__(self, description=None, destination_cidr_block=None, next_hop_id=None, next_hop_type=None,
                 status=None):
        self.description = description  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.next_hop_id = next_hop_id  # type: str
        self.next_hop_type = next_hop_type  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorBackhaulRouteResponseBodyRoutes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListIoTCloudConnectorBackhaulRouteResponseBody(TeaModel):
    def __init__(self, net_link_id=None, request_id=None, routes=None):
        self.net_link_id = net_link_id  # type: str
        self.request_id = request_id  # type: str
        self.routes = routes  # type: list[ListIoTCloudConnectorBackhaulRouteResponseBodyRoutes]

    def validate(self):
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorBackhaulRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_link_id is not None:
            result['NetLinkId'] = self.net_link_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['Routes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetLinkId') is not None:
            self.net_link_id = m.get('NetLinkId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.routes = []
        if m.get('Routes') is not None:
            for k in m.get('Routes'):
                temp_model = ListIoTCloudConnectorBackhaulRouteResponseBodyRoutes()
                self.routes.append(temp_model.from_map(k))
        return self


class ListIoTCloudConnectorBackhaulRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIoTCloudConnectorBackhaulRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorBackhaulRouteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListIoTCloudConnectorBackhaulRouteResponseBody()
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
        self.orders = orders  # type: list[ListOrdersResponseBodyOrders]
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOrdersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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


class ListWirelessCloudConnectorsRequest(TeaModel):
    def __init__(self, business_type=None, is_in_group=None, max_results=None, names=None, next_token=None,
                 region_id=None, statuses=None, wireless_cloud_connector_group_id=None, wireless_cloud_connector_ids=None):
        self.business_type = business_type  # type: str
        self.is_in_group = is_in_group  # type: str
        self.max_results = max_results  # type: long
        self.names = names  # type: list[str]
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.statuses = statuses  # type: list[str]
        self.wireless_cloud_connector_group_id = wireless_cloud_connector_group_id  # type: str
        self.wireless_cloud_connector_ids = wireless_cloud_connector_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWirelessCloudConnectorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.is_in_group is not None:
            result['IsInGroup'] = self.is_in_group
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
        if self.wireless_cloud_connector_group_id is not None:
            result['WirelessCloudConnectorGroupId'] = self.wireless_cloud_connector_group_id
        if self.wireless_cloud_connector_ids is not None:
            result['WirelessCloudConnectorIds'] = self.wireless_cloud_connector_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('IsInGroup') is not None:
            self.is_in_group = m.get('IsInGroup')
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
        if m.get('WirelessCloudConnectorGroupId') is not None:
            self.wireless_cloud_connector_group_id = m.get('WirelessCloudConnectorGroupId')
        if m.get('WirelessCloudConnectorIds') is not None:
            self.wireless_cloud_connector_ids = m.get('WirelessCloudConnectorIds')
        return self


class ListWirelessCloudConnectorsResponseBodyWirelessCloudConnectors(TeaModel):
    def __init__(self, business_type=None, card_count=None, create_time=None, data_package_id=None,
                 data_package_type=None, description=None, name=None, region_id=None, service_type=None, status=None, use_case=None,
                 wireless_cloud_connector_group_id=None, wireless_cloud_connector_id=None):
        self.business_type = business_type  # type: str
        self.card_count = card_count  # type: str
        self.create_time = create_time  # type: str
        self.data_package_id = data_package_id  # type: str
        self.data_package_type = data_package_type  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.service_type = service_type  # type: str
        self.status = status  # type: str
        self.use_case = use_case  # type: str
        self.wireless_cloud_connector_group_id = wireless_cloud_connector_group_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWirelessCloudConnectorsResponseBodyWirelessCloudConnectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
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
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.use_case is not None:
            result['UseCase'] = self.use_case
        if self.wireless_cloud_connector_group_id is not None:
            result['WirelessCloudConnectorGroupId'] = self.wireless_cloud_connector_group_id
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
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
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UseCase') is not None:
            self.use_case = m.get('UseCase')
        if m.get('WirelessCloudConnectorGroupId') is not None:
            self.wireless_cloud_connector_group_id = m.get('WirelessCloudConnectorGroupId')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ListWirelessCloudConnectorsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None,
                 wireless_cloud_connectors=None):
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListWirelessCloudConnectorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        self.local_name = local_name  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockCardsRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, iccids=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.iccids = iccids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockCardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.iccids is not None:
            result['Iccids'] = self.iccids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Iccids') is not None:
            self.iccids = m.get('Iccids')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class LockCardsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockCardsResponseBody, self).to_map()
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


class LockCardsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LockCardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LockCardsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LockCardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWirelessCloudConnectorFeatureRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, feature_name=None, feature_value=None,
                 wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.feature_name = feature_name  # type: str
        self.feature_value = feature_value  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWirelessCloudConnectorFeatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_value is not None:
            result['FeatureValue'] = self.feature_value
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureValue') is not None:
            self.feature_value = m.get('FeatureValue')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class ModifyWirelessCloudConnectorFeatureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWirelessCloudConnectorFeatureResponseBody, self).to_map()
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


class ModifyWirelessCloudConnectorFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWirelessCloudConnectorFeatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWirelessCloudConnectorFeatureResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyWirelessCloudConnectorFeatureResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenCc5gServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenCc5gServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeCardsRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, iccids=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.iccids = iccids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeCardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.iccids is not None:
            result['Iccids'] = self.iccids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Iccids') is not None:
            self.iccids = m.get('Iccids')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResumeCardsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeCardsResponseBody, self).to_map()
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


class ResumeCardsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResumeCardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeCardsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResumeCardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeNetLinkRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, net_link_id=None, wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.net_link_id = net_link_id  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeNetLinkRequest, self).to_map()
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


class RevokeNetLinkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeNetLinkResponseBody, self).to_map()
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


class RevokeNetLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RevokeNetLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeNetLinkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevokeNetLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCardsRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, iccids=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.iccids = iccids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopCardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.iccids is not None:
            result['Iccids'] = self.iccids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Iccids') is not None:
            self.iccids = m.get('Iccids')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopCardsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopCardsResponseBody, self).to_map()
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


class StopCardsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopCardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopCardsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopCardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDiagnoseTaskForSingleCardRequest(TeaModel):
    def __init__(self, begin_time=None, destination=None, end_time=None, region_no=None, resource_uid=None,
                 source=None, wireless_cloud_connector_id=None):
        self.begin_time = begin_time  # type: long
        self.destination = destination  # type: str
        self.end_time = end_time  # type: long
        self.region_no = region_no  # type: str
        self.resource_uid = resource_uid  # type: long
        self.source = source  # type: str
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid
        if self.source is not None:
            result['Source'] = self.source
        if self.wireless_cloud_connector_id is not None:
            result['WirelessCloudConnectorId'] = self.wireless_cloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitDiagnoseTaskForSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitDiagnoseTaskForSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchWirelessCloudConnectorToBusinessRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, wireless_cloud_connector_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.wireless_cloud_connector_id = wireless_cloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchWirelessCloudConnectorToBusinessRequest, self).to_map()
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


class SwitchWirelessCloudConnectorToBusinessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchWirelessCloudConnectorToBusinessResponseBody, self).to_map()
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


class SwitchWirelessCloudConnectorToBusinessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchWirelessCloudConnectorToBusinessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchWirelessCloudConnectorToBusinessResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SwitchWirelessCloudConnectorToBusinessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockCardsRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, iccids=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.iccids = iccids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockCardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.iccids is not None:
            result['Iccids'] = self.iccids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Iccids') is not None:
            self.iccids = m.get('Iccids')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UnlockCardsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockCardsResponseBody, self).to_map()
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


class UnlockCardsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnlockCardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnlockCardsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnlockCardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthorizationRuleRequest(TeaModel):
    def __init__(self, authorization_rule_id=None, client_token=None, description=None, destination=None,
                 destination_port=None, dry_run=None, name=None, policy=None, protocol=None, source_cidr=None,
                 wireless_cloud_connector_id=None):
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.destination = destination  # type: str
        self.destination_port = destination_port  # type: str
        self.dry_run = dry_run  # type: bool
        self.name = name  # type: str
        self.policy = policy  # type: str
        self.protocol = protocol  # type: str
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
        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.protocol is not None:
            result['Protocol'] = self.protocol
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
        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')
        if m.get('WirelessCloudConnectorId') is not None:
            self.wireless_cloud_connector_id = m.get('WirelessCloudConnectorId')
        return self


class UpdateAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBatchOperateCardsTaskRequest(TeaModel):
    def __init__(self, batch_operate_cards_task_id=None, client_token=None, description=None, dry_run=None,
                 effect_type=None, iccids=None, iccids_oss_file_path=None, name=None, operate_type=None, region_id=None,
                 threshold=None, wireless_cloud_connector_ids=None):
        self.batch_operate_cards_task_id = batch_operate_cards_task_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.effect_type = effect_type  # type: str
        self.iccids = iccids  # type: list[str]
        self.iccids_oss_file_path = iccids_oss_file_path  # type: str
        self.name = name  # type: str
        self.operate_type = operate_type  # type: str
        self.region_id = region_id  # type: str
        self.threshold = threshold  # type: long
        self.wireless_cloud_connector_ids = wireless_cloud_connector_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBatchOperateCardsTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_operate_cards_task_id is not None:
            result['BatchOperateCardsTaskId'] = self.batch_operate_cards_task_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.effect_type is not None:
            result['EffectType'] = self.effect_type
        if self.iccids is not None:
            result['Iccids'] = self.iccids
        if self.iccids_oss_file_path is not None:
            result['IccidsOssFilePath'] = self.iccids_oss_file_path
        if self.name is not None:
            result['Name'] = self.name
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.wireless_cloud_connector_ids is not None:
            result['WirelessCloudConnectorIds'] = self.wireless_cloud_connector_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchOperateCardsTaskId') is not None:
            self.batch_operate_cards_task_id = m.get('BatchOperateCardsTaskId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EffectType') is not None:
            self.effect_type = m.get('EffectType')
        if m.get('Iccids') is not None:
            self.iccids = m.get('Iccids')
        if m.get('IccidsOssFilePath') is not None:
            self.iccids_oss_file_path = m.get('IccidsOssFilePath')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('WirelessCloudConnectorIds') is not None:
            self.wireless_cloud_connector_ids = m.get('WirelessCloudConnectorIds')
        return self


class UpdateBatchOperateCardsTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBatchOperateCardsTaskResponseBody, self).to_map()
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


class UpdateBatchOperateCardsTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBatchOperateCardsTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBatchOperateCardsTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateBatchOperateCardsTaskResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDNSAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWirelessCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWirelessCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


