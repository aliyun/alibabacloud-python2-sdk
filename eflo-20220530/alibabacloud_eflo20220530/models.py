# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AssignPrivateIpAddressRequest(TeaModel):
    def __init__(self, assign_mac=None, client_token=None, network_interface_id=None, private_ip_address=None,
                 region_id=None, subnet_id=None):
        self.assign_mac = assign_mac  # type: bool
        self.client_token = client_token  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.region_id = region_id  # type: str
        self.subnet_id = subnet_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssignPrivateIpAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_mac is not None:
            result['AssignMac'] = self.assign_mac
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssignMac') is not None:
            self.assign_mac = m.get('AssignMac')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class AssignPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(self, ip_name=None, network_interface_id=None):
        self.ip_name = ip_name  # type: str
        self.network_interface_id = network_interface_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssignPrivateIpAddressResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        return self


class AssignPrivateIpAddressResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: AssignPrivateIpAddressResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(AssignPrivateIpAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = AssignPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssignPrivateIpAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssignPrivateIpAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssignPrivateIpAddressResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssignPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubnetRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubnetRequestTag, self).to_map()
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


class CreateSubnetRequest(TeaModel):
    def __init__(self, cidr=None, client_token=None, region_id=None, subnet_name=None, tag=None, type=None,
                 vpd_id=None, zone_id=None):
        self.cidr = cidr  # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.subnet_name = subnet_name  # type: str
        self.tag = tag  # type: list[CreateSubnetRequestTag]
        self.type = type  # type: str
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSubnetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateSubnetRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateSubnetResponseBodyContent(TeaModel):
    def __init__(self, subnet_id=None):
        self.subnet_id = subnet_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubnetResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class CreateSubnetResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: CreateSubnetResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(CreateSubnetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = CreateSubnetResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSubnetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSubnetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSubnetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSubnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVccRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVccRequestTag, self).to_map()
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


class CreateVccRequest(TeaModel):
    def __init__(self, access_could_service=None, bgp_cidr=None, cen_id=None, connection_type=None,
                 description=None, region_id=None, resource_group_id=None, tag=None, v_switch_id=None, vcc_id=None,
                 vcc_name=None, vpc_id=None, vpd_id=None, zone_id=None):
        self.access_could_service = access_could_service  # type: bool
        self.bgp_cidr = bgp_cidr  # type: str
        self.cen_id = cen_id  # type: str
        self.connection_type = connection_type  # type: str
        self.description = description  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[CreateVccRequestTag]
        self.v_switch_id = v_switch_id  # type: str
        self.vcc_id = vcc_id  # type: str
        self.vcc_name = vcc_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateVccRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_could_service is not None:
            result['AccessCouldService'] = self.access_could_service
        if self.bgp_cidr is not None:
            result['BgpCidr'] = self.bgp_cidr
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_name is not None:
            result['VccName'] = self.vcc_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessCouldService') is not None:
            self.access_could_service = m.get('AccessCouldService')
        if m.get('BgpCidr') is not None:
            self.bgp_cidr = m.get('BgpCidr')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateVccRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateVccResponseBodyContent(TeaModel):
    def __init__(self, vcc_id=None):
        self.vcc_id = vcc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVccResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class CreateVccResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: CreateVccResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(CreateVccResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = CreateVccResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVccResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVccResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVccResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpdRequestSubnets(TeaModel):
    def __init__(self, cidr=None, client_token=None, region_id=None, subnet_name=None, type=None, zone_id=None):
        self.cidr = cidr  # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.subnet_name = subnet_name  # type: str
        self.type = type  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpdRequestSubnets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name
        if self.type is not None:
            result['Type'] = self.type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateVpdRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpdRequestTag, self).to_map()
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


class CreateVpdRequest(TeaModel):
    def __init__(self, cidr=None, client_token=None, region_id=None, resource_group_id=None, subnets=None, tag=None,
                 vpd_name=None):
        self.cidr = cidr  # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.subnets = subnets  # type: list[CreateVpdRequestSubnets]
        self.tag = tag  # type: list[CreateVpdRequestTag]
        self.vpd_name = vpd_name  # type: str

    def validate(self):
        if self.subnets:
            for k in self.subnets:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateVpdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Subnets'] = []
        if self.subnets is not None:
            for k in self.subnets:
                result['Subnets'].append(k.to_map() if k else None)
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.subnets = []
        if m.get('Subnets') is not None:
            for k in m.get('Subnets'):
                temp_model = CreateVpdRequestSubnets()
                self.subnets.append(temp_model.from_map(k))
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateVpdRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class CreateVpdResponseBodyContent(TeaModel):
    def __init__(self, subnet_ids=None, vpd_id=None):
        self.subnet_ids = subnet_ids  # type: list[str]
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpdResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subnet_ids is not None:
            result['SubnetIds'] = self.subnet_ids
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubnetIds') is not None:
            self.subnet_ids = m.get('SubnetIds')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class CreateVpdResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: CreateVpdResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(CreateVpdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = CreateVpdResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVpdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVpdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVpdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpdGrantRuleRequest(TeaModel):
    def __init__(self, er_id=None, grant_tenant_id=None, instance_id=None, region_id=None):
        self.er_id = er_id  # type: str
        self.grant_tenant_id = grant_tenant_id  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpdGrantRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateVpdGrantRuleResponseBodyContent(TeaModel):
    def __init__(self, grant_rule_id=None):
        self.grant_rule_id = grant_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpdGrantRuleResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        return self


class CreateVpdGrantRuleResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: CreateVpdGrantRuleResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(CreateVpdGrantRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = CreateVpdGrantRuleResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVpdGrantRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVpdGrantRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpdGrantRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVpdGrantRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubnetRequest(TeaModel):
    def __init__(self, region_id=None, subnet_id=None, vpd_id=None, zone_id=None):
        self.region_id = region_id  # type: str
        self.subnet_id = subnet_id  # type: str
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubnetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DeleteSubnetResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubnetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSubnetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSubnetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSubnetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSubnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpdRequest(TeaModel):
    def __init__(self, region_id=None, vpd_id=None):
        self.region_id = region_id  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class DeleteVpdResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVpdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVpdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVpdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpdGrantRuleRequest(TeaModel):
    def __init__(self, er_id=None, grant_rule_id=None, grant_tenant_id=None, instance_id=None, region_id=None):
        self.er_id = er_id  # type: str
        self.grant_rule_id = grant_rule_id  # type: str
        self.grant_tenant_id = grant_tenant_id  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpdGrantRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteVpdGrantRuleResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpdGrantRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpdGrantRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVpdGrantRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVpdGrantRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVpdGrantRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlrRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlrResponseBodyContent(TeaModel):
    def __init__(self, has_role=None):
        self.has_role = has_role  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlrResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_role is not None:
            result['HasRole'] = self.has_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasRole') is not None:
            self.has_role = m.get('HasRole')
        return self


class DescribeSlrResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: DescribeSlrResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(DescribeSlrResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = DescribeSlrResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSlrResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlrResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLniPrivateIpAddressRequest(TeaModel):
    def __init__(self, client_token=None, ip_name=None, network_interface_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.ip_name = ip_name  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLniPrivateIpAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetLniPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(self, gmt_create=None, ip_address_mac=None, ip_name=None, message=None, network_interface_id=None,
                 private_ip_address=None, region_id=None, status=None):
        self.gmt_create = gmt_create  # type: str
        self.ip_address_mac = ip_address_mac  # type: str
        self.ip_name = ip_name  # type: str
        self.message = message  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLniPrivateIpAddressResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.ip_address_mac is not None:
            result['IpAddressMac'] = self.ip_address_mac
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.message is not None:
            result['Message'] = self.message
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('IpAddressMac') is not None:
            self.ip_address_mac = m.get('IpAddressMac')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetLniPrivateIpAddressResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: GetLniPrivateIpAddressResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(GetLniPrivateIpAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = GetLniPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLniPrivateIpAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLniPrivateIpAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLniPrivateIpAddressResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLniPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubnetRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, subnet_id=None, vpd_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.subnet_id = subnet_id  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubnetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class GetSubnetResponseBodyContentTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubnetResponseBodyContentTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetSubnetResponseBodyContentVpdBaseInfo(TeaModel):
    def __init__(self, cidr=None, create_time=None, vpd_id=None, vpd_name=None):
        self.cidr = cidr  # type: str
        self.create_time = create_time  # type: str
        self.vpd_id = vpd_id  # type: str
        self.vpd_name = vpd_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubnetResponseBodyContentVpdBaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class GetSubnetResponseBodyContent(TeaModel):
    def __init__(self, available_ips=None, cidr=None, create_time=None, description=None, gmt_modified=None,
                 lb_count=None, message=None, nc_count=None, region_id=None, resource_group_id=None, status=None,
                 subnet_id=None, subnet_name=None, tags=None, tenant_id=None, type=None, vpd_base_info=None, vpd_id=None,
                 zone_id=None):
        self.available_ips = available_ips  # type: int
        self.cidr = cidr  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.lb_count = lb_count  # type: long
        self.message = message  # type: str
        self.nc_count = nc_count  # type: long
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.subnet_id = subnet_id  # type: str
        self.subnet_name = subnet_name  # type: str
        self.tags = tags  # type: list[GetSubnetResponseBodyContentTags]
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.vpd_base_info = vpd_base_info  # type: GetSubnetResponseBodyContentVpdBaseInfo
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super(GetSubnetResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_ips is not None:
            result['AvailableIps'] = self.available_ips
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.lb_count is not None:
            result['LbCount'] = self.lb_count
        if self.message is not None:
            result['Message'] = self.message
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.vpd_base_info is not None:
            result['VpdBaseInfo'] = self.vpd_base_info.to_map()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableIps') is not None:
            self.available_ips = m.get('AvailableIps')
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LbCount') is not None:
            self.lb_count = m.get('LbCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetSubnetResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpdBaseInfo') is not None:
            temp_model = GetSubnetResponseBodyContentVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetSubnetResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: GetSubnetResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(GetSubnetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = GetSubnetResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSubnetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSubnetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSubnetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVccRequest(TeaModel):
    def __init__(self, enable_page=None, page_number=None, page_size=None, region_id=None, vcc_id=None):
        self.enable_page = enable_page  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.vcc_id = vcc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVccRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class GetVccResponseBodyContentAliyunRouterInfo(TeaModel):
    def __init__(self, local_gateway_ip=None, mask=None, pc_id=None, peer_gateway_ip=None, vbr_id=None, vlan_id=None):
        self.local_gateway_ip = local_gateway_ip  # type: str
        self.mask = mask  # type: str
        self.pc_id = pc_id  # type: str
        self.peer_gateway_ip = peer_gateway_ip  # type: str
        self.vbr_id = vbr_id  # type: str
        self.vlan_id = vlan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVccResponseBodyContentAliyunRouterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.pc_id is not None:
            result['PcId'] = self.pc_id
        if self.peer_gateway_ip is not None:
            result['PeerGatewayIp'] = self.peer_gateway_ip
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('PcId') is not None:
            self.pc_id = m.get('PcId')
        if m.get('PeerGatewayIp') is not None:
            self.peer_gateway_ip = m.get('PeerGatewayIp')
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')
        return self


class GetVccResponseBodyContentCisRouterInfoCcInfos(TeaModel):
    def __init__(self, cc_id=None, local_gateway_ip=None, remote_gateway_ip=None, status=None, subnet_mask=None,
                 vlan_id=None):
        self.cc_id = cc_id  # type: str
        self.local_gateway_ip = local_gateway_ip  # type: str
        self.remote_gateway_ip = remote_gateway_ip  # type: str
        self.status = status  # type: str
        self.subnet_mask = subnet_mask  # type: str
        # vlanid
        self.vlan_id = vlan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVccResponseBodyContentCisRouterInfoCcInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc_id is not None:
            result['CcId'] = self.cc_id
        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip
        if self.remote_gateway_ip is not None:
            result['RemoteGatewayIp'] = self.remote_gateway_ip
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_mask is not None:
            result['SubnetMask'] = self.subnet_mask
        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CcId') is not None:
            self.cc_id = m.get('CcId')
        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')
        if m.get('RemoteGatewayIp') is not None:
            self.remote_gateway_ip = m.get('RemoteGatewayIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetMask') is not None:
            self.subnet_mask = m.get('SubnetMask')
        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')
        return self


class GetVccResponseBodyContentCisRouterInfo(TeaModel):
    def __init__(self, cc_infos=None, ccr_id=None):
        self.cc_infos = cc_infos  # type: list[GetVccResponseBodyContentCisRouterInfoCcInfos]
        self.ccr_id = ccr_id  # type: str

    def validate(self):
        if self.cc_infos:
            for k in self.cc_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVccResponseBodyContentCisRouterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CcInfos'] = []
        if self.cc_infos is not None:
            for k in self.cc_infos:
                result['CcInfos'].append(k.to_map() if k else None)
        if self.ccr_id is not None:
            result['CcrId'] = self.ccr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cc_infos = []
        if m.get('CcInfos') is not None:
            for k in m.get('CcInfos'):
                temp_model = GetVccResponseBodyContentCisRouterInfoCcInfos()
                self.cc_infos.append(temp_model.from_map(k))
        if m.get('CcrId') is not None:
            self.ccr_id = m.get('CcrId')
        return self


class GetVccResponseBodyContentErInfos(TeaModel):
    def __init__(self, connections=None, create_time=None, description=None, er_id=None, er_name=None,
                 gmt_modified=None, master_zone_id=None, message=None, region_id=None, route_maps=None, status=None,
                 tenant_id=None):
        self.connections = connections  # type: long
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.er_id = er_id  # type: str
        self.er_name = er_name  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.master_zone_id = master_zone_id  # type: str
        self.message = message  # type: str
        self.region_id = region_id  # type: str
        self.route_maps = route_maps  # type: long
        self.status = status  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVccResponseBodyContentErInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMaps') is not None:
            self.route_maps = m.get('RouteMaps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetVccResponseBodyContentTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVccResponseBodyContentTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetVccResponseBodyContentVpdBaseInfo(TeaModel):
    def __init__(self, cidr=None, create_time=None, vpd_id=None, vpd_name=None):
        self.cidr = cidr  # type: str
        self.create_time = create_time  # type: str
        self.vpd_id = vpd_id  # type: str
        self.vpd_name = vpd_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVccResponseBodyContentVpdBaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class GetVccResponseBodyContent(TeaModel):
    def __init__(self, access_point_id=None, aliyun_router_info=None, attach_er_status=None, bandwidth_str=None,
                 bgp_cidr=None, cen_id=None, cis_router_info=None, commodity_code=None, connection_type=None,
                 create_time=None, current_node=None, duration=None, er_infos=None, expiration_date=None, gmt_modified=None,
                 internet_charge_type=None, line_operator=None, message=None, pay_type=None, port_type=None, pricing_cycle=None,
                 region_id=None, resource_group_id=None, spec=None, status=None, tags=None, tenant_id=None, v_switch_id=None,
                 vcc_id=None, vcc_name=None, vpc_id=None, vpd_base_info=None, vpd_id=None, zone_id=None):
        self.access_point_id = access_point_id  # type: str
        self.aliyun_router_info = aliyun_router_info  # type: list[GetVccResponseBodyContentAliyunRouterInfo]
        self.attach_er_status = attach_er_status  # type: bool
        self.bandwidth_str = bandwidth_str  # type: str
        self.bgp_cidr = bgp_cidr  # type: str
        self.cen_id = cen_id  # type: str
        self.cis_router_info = cis_router_info  # type: list[GetVccResponseBodyContentCisRouterInfo]
        self.commodity_code = commodity_code  # type: str
        self.connection_type = connection_type  # type: str
        self.create_time = create_time  # type: str
        self.current_node = current_node  # type: str
        self.duration = duration  # type: str
        self.er_infos = er_infos  # type: list[GetVccResponseBodyContentErInfos]
        self.expiration_date = expiration_date  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.line_operator = line_operator  # type: str
        self.message = message  # type: str
        self.pay_type = pay_type  # type: str
        self.port_type = port_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.spec = spec  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: list[GetVccResponseBodyContentTags]
        self.tenant_id = tenant_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vcc_id = vcc_id  # type: str
        self.vcc_name = vcc_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpd_base_info = vpd_base_info  # type: GetVccResponseBodyContentVpdBaseInfo
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.aliyun_router_info:
            for k in self.aliyun_router_info:
                if k:
                    k.validate()
        if self.cis_router_info:
            for k in self.cis_router_info:
                if k:
                    k.validate()
        if self.er_infos:
            for k in self.er_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super(GetVccResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        result['AliyunRouterInfo'] = []
        if self.aliyun_router_info is not None:
            for k in self.aliyun_router_info:
                result['AliyunRouterInfo'].append(k.to_map() if k else None)
        if self.attach_er_status is not None:
            result['AttachErStatus'] = self.attach_er_status
        if self.bandwidth_str is not None:
            result['BandwidthStr'] = self.bandwidth_str
        if self.bgp_cidr is not None:
            result['BgpCidr'] = self.bgp_cidr
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        result['CisRouterInfo'] = []
        if self.cis_router_info is not None:
            for k in self.cis_router_info:
                result['CisRouterInfo'].append(k.to_map() if k else None)
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_node is not None:
            result['CurrentNode'] = self.current_node
        if self.duration is not None:
            result['Duration'] = self.duration
        result['ErInfos'] = []
        if self.er_infos is not None:
            for k in self.er_infos:
                result['ErInfos'].append(k.to_map() if k else None)
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator
        if self.message is not None:
            result['Message'] = self.message
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port_type is not None:
            result['PortType'] = self.port_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_name is not None:
            result['VccName'] = self.vcc_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpd_base_info is not None:
            result['VpdBaseInfo'] = self.vpd_base_info.to_map()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        self.aliyun_router_info = []
        if m.get('AliyunRouterInfo') is not None:
            for k in m.get('AliyunRouterInfo'):
                temp_model = GetVccResponseBodyContentAliyunRouterInfo()
                self.aliyun_router_info.append(temp_model.from_map(k))
        if m.get('AttachErStatus') is not None:
            self.attach_er_status = m.get('AttachErStatus')
        if m.get('BandwidthStr') is not None:
            self.bandwidth_str = m.get('BandwidthStr')
        if m.get('BgpCidr') is not None:
            self.bgp_cidr = m.get('BgpCidr')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        self.cis_router_info = []
        if m.get('CisRouterInfo') is not None:
            for k in m.get('CisRouterInfo'):
                temp_model = GetVccResponseBodyContentCisRouterInfo()
                self.cis_router_info.append(temp_model.from_map(k))
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentNode') is not None:
            self.current_node = m.get('CurrentNode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k in m.get('ErInfos'):
                temp_model = GetVccResponseBodyContentErInfos()
                self.er_infos.append(temp_model.from_map(k))
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetVccResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdBaseInfo') is not None:
            temp_model = GetVccResponseBodyContentVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetVccResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: GetVccResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(GetVccResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = GetVccResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVccResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVccResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVccResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpdRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, vpd_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class GetVpdResponseBodyContentErInfos(TeaModel):
    def __init__(self, connections=None, create_time=None, description=None, er_id=None, er_name=None,
                 gmt_modified=None, master_zone_id=None, message=None, region_id=None, route_maps=None, status=None,
                 tenant_id=None):
        self.connections = connections  # type: long
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.er_id = er_id  # type: str
        self.er_name = er_name  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.master_zone_id = master_zone_id  # type: str
        self.message = message  # type: str
        self.region_id = region_id  # type: str
        self.route_maps = route_maps  # type: long
        self.status = status  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpdResponseBodyContentErInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMaps') is not None:
            self.route_maps = m.get('RouteMaps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetVpdResponseBodyContentTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpdResponseBodyContentTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetVpdResponseBodyContent(TeaModel):
    def __init__(self, attach_er_status=None, cidr=None, create_time=None, er_infos=None, gmt_modified=None,
                 message=None, nc_count=None, region_id=None, resource_group_id=None, service_cidr=None, status=None,
                 subnet_count=None, tags=None, tenant_id=None, vpd_id=None, vpd_name=None):
        self.attach_er_status = attach_er_status  # type: bool
        self.cidr = cidr  # type: str
        self.create_time = create_time  # type: str
        self.er_infos = er_infos  # type: list[GetVpdResponseBodyContentErInfos]
        self.gmt_modified = gmt_modified  # type: str
        self.message = message  # type: str
        self.nc_count = nc_count  # type: long
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.service_cidr = service_cidr  # type: str
        self.status = status  # type: str
        self.subnet_count = subnet_count  # type: long
        self.tags = tags  # type: list[GetVpdResponseBodyContentTags]
        self.tenant_id = tenant_id  # type: str
        self.vpd_id = vpd_id  # type: str
        self.vpd_name = vpd_name  # type: str

    def validate(self):
        if self.er_infos:
            for k in self.er_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVpdResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_er_status is not None:
            result['AttachErStatus'] = self.attach_er_status
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['ErInfos'] = []
        if self.er_infos is not None:
            for k in self.er_infos:
                result['ErInfos'].append(k.to_map() if k else None)
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_cidr is not None:
            result['ServiceCidr'] = self.service_cidr
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_count is not None:
            result['SubnetCount'] = self.subnet_count
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachErStatus') is not None:
            self.attach_er_status = m.get('AttachErStatus')
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k in m.get('ErInfos'):
                temp_model = GetVpdResponseBodyContentErInfos()
                self.er_infos.append(temp_model.from_map(k))
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceCidr') is not None:
            self.service_cidr = m.get('ServiceCidr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetCount') is not None:
            self.subnet_count = m.get('SubnetCount')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetVpdResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class GetVpdResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: GetVpdResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(GetVpdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = GetVpdResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVpdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVpdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVpdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVpdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeVccRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeVccRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class InitializeVccResponseBodyContent(TeaModel):
    def __init__(self, request_id=None, role_name=None):
        self.request_id = request_id  # type: str
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeVccResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class InitializeVccResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: InitializeVccResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(InitializeVccResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = InitializeVccResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InitializeVccResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitializeVccResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitializeVccResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitializeVccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLniPrivateIpAddressRequest(TeaModel):
    def __init__(self, enable_page=None, ip=None, ip_name=None, network_interface_id=None, page_number=None,
                 page_size=None, region_id=None):
        self.enable_page = enable_page  # type: bool
        self.ip = ip  # type: str
        self.ip_name = ip_name  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLniPrivateIpAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListLniPrivateIpAddressResponseBodyContentData(TeaModel):
    def __init__(self, gmt_create=None, ip_address_mac=None, ip_name=None, message=None, network_interface_id=None,
                 private_ip_address=None, region_id=None, status=None):
        self.gmt_create = gmt_create  # type: str
        self.ip_address_mac = ip_address_mac  # type: str
        self.ip_name = ip_name  # type: str
        self.message = message  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLniPrivateIpAddressResponseBodyContentData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.ip_address_mac is not None:
            result['IpAddressMac'] = self.ip_address_mac
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.message is not None:
            result['Message'] = self.message
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('IpAddressMac') is not None:
            self.ip_address_mac = m.get('IpAddressMac')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLniPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(self, data=None, total=None):
        self.data = data  # type: list[ListLniPrivateIpAddressResponseBodyContentData]
        self.total = total  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLniPrivateIpAddressResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListLniPrivateIpAddressResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListLniPrivateIpAddressResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: ListLniPrivateIpAddressResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(ListLniPrivateIpAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = ListLniPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLniPrivateIpAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLniPrivateIpAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLniPrivateIpAddressResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLniPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworkInterfacesRequest(TeaModel):
    def __init__(self, enable_page=None, ip=None, network_interface_id=None, node_id=None, page_number=None,
                 page_size=None, region_id=None, subnet_id=None, vpd_id=None):
        self.enable_page = enable_page  # type: bool
        self.ip = ip  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.node_id = node_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.subnet_id = subnet_id  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkInterfacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class ListNetworkInterfacesResponseBodyContentDataPrivateIpAddressMacGroup(TeaModel):
    def __init__(self, ip_address_mac=None, ip_name=None, message=None, private_ip_address=None, status=None):
        self.ip_address_mac = ip_address_mac  # type: str
        self.ip_name = ip_name  # type: str
        self.message = message  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkInterfacesResponseBodyContentDataPrivateIpAddressMacGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address_mac is not None:
            result['IpAddressMac'] = self.ip_address_mac
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.message is not None:
            result['Message'] = self.message
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpAddressMac') is not None:
            self.ip_address_mac = m.get('IpAddressMac')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListNetworkInterfacesResponseBodyContentDataSubnetBaseInfo(TeaModel):
    def __init__(self, cidr=None, gmt_create=None, name=None, subnet_id=None):
        self.cidr = cidr  # type: str
        self.gmt_create = gmt_create  # type: str
        self.name = name  # type: str
        self.subnet_id = subnet_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkInterfacesResponseBodyContentDataSubnetBaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class ListNetworkInterfacesResponseBodyContentDataVpdBaseInfo(TeaModel):
    def __init__(self, cidr=None, create_time=None, vpd_id=None, vpd_name=None):
        self.cidr = cidr  # type: str
        self.create_time = create_time  # type: str
        self.vpd_id = vpd_id  # type: str
        self.vpd_name = vpd_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNetworkInterfacesResponseBodyContentDataVpdBaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class ListNetworkInterfacesResponseBodyContentData(TeaModel):
    def __init__(self, create_time=None, ethernet=None, gateway=None, ip=None, nc_type=None,
                 network_interface_id=None, node_id=None, private_ip_address_mac_group=None, quota=None, region_id=None,
                 service_mac=None, status=None, subnet_base_info=None, tenant_id=None, vpd_base_info=None, zone_id=None):
        self.create_time = create_time  # type: str
        self.ethernet = ethernet  # type: list[str]
        self.gateway = gateway  # type: str
        self.ip = ip  # type: str
        self.nc_type = nc_type  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.node_id = node_id  # type: str
        self.private_ip_address_mac_group = private_ip_address_mac_group  # type: list[ListNetworkInterfacesResponseBodyContentDataPrivateIpAddressMacGroup]
        self.quota = quota  # type: int
        self.region_id = region_id  # type: str
        self.service_mac = service_mac  # type: str
        self.status = status  # type: str
        self.subnet_base_info = subnet_base_info  # type: ListNetworkInterfacesResponseBodyContentDataSubnetBaseInfo
        self.tenant_id = tenant_id  # type: str
        self.vpd_base_info = vpd_base_info  # type: ListNetworkInterfacesResponseBodyContentDataVpdBaseInfo
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.private_ip_address_mac_group:
            for k in self.private_ip_address_mac_group:
                if k:
                    k.validate()
        if self.subnet_base_info:
            self.subnet_base_info.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super(ListNetworkInterfacesResponseBodyContentData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ethernet is not None:
            result['Ethernet'] = self.ethernet
        if self.gateway is not None:
            result['Gateway'] = self.gateway
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.nc_type is not None:
            result['NcType'] = self.nc_type
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        result['PrivateIpAddressMacGroup'] = []
        if self.private_ip_address_mac_group is not None:
            for k in self.private_ip_address_mac_group:
                result['PrivateIpAddressMacGroup'].append(k.to_map() if k else None)
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_mac is not None:
            result['ServiceMac'] = self.service_mac
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_base_info is not None:
            result['SubnetBaseInfo'] = self.subnet_base_info.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vpd_base_info is not None:
            result['VpdBaseInfo'] = self.vpd_base_info.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Ethernet') is not None:
            self.ethernet = m.get('Ethernet')
        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NcType') is not None:
            self.nc_type = m.get('NcType')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        self.private_ip_address_mac_group = []
        if m.get('PrivateIpAddressMacGroup') is not None:
            for k in m.get('PrivateIpAddressMacGroup'):
                temp_model = ListNetworkInterfacesResponseBodyContentDataPrivateIpAddressMacGroup()
                self.private_ip_address_mac_group.append(temp_model.from_map(k))
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceMac') is not None:
            self.service_mac = m.get('ServiceMac')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetBaseInfo') is not None:
            temp_model = ListNetworkInterfacesResponseBodyContentDataSubnetBaseInfo()
            self.subnet_base_info = temp_model.from_map(m['SubnetBaseInfo'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VpdBaseInfo') is not None:
            temp_model = ListNetworkInterfacesResponseBodyContentDataVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListNetworkInterfacesResponseBodyContent(TeaModel):
    def __init__(self, data=None, total=None):
        self.data = data  # type: list[ListNetworkInterfacesResponseBodyContentData]
        self.total = total  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNetworkInterfacesResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListNetworkInterfacesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListNetworkInterfacesResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: ListNetworkInterfacesResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(ListNetworkInterfacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = ListNetworkInterfacesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNetworkInterfacesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNetworkInterfacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNetworkInterfacesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNetworkInterfacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubnetsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubnetsRequestTag, self).to_map()
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


class ListSubnetsRequest(TeaModel):
    def __init__(self, enable_page=None, page_number=None, page_size=None, region_id=None, resource_group_id=None,
                 status=None, subnet_id=None, subnet_name=None, tag=None, type=None, vpd_id=None, zone_id=None):
        self.enable_page = enable_page  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.subnet_id = subnet_id  # type: str
        self.subnet_name = subnet_name  # type: str
        self.tag = tag  # type: list[ListSubnetsRequestTag]
        self.type = type  # type: str
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubnetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListSubnetsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListSubnetsResponseBodyContentDataTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubnetsResponseBodyContentDataTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListSubnetsResponseBodyContentDataVpdBaseInfo(TeaModel):
    def __init__(self, cidr=None, create_time=None, vpd_id=None, vpd_name=None):
        self.cidr = cidr  # type: str
        self.create_time = create_time  # type: str
        self.vpd_id = vpd_id  # type: str
        self.vpd_name = vpd_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubnetsResponseBodyContentDataVpdBaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class ListSubnetsResponseBodyContentData(TeaModel):
    def __init__(self, cidr=None, create_time=None, gmt_modified=None, message=None, nc_count=None, region_id=None,
                 resource_group_id=None, status=None, subnet_id=None, subnet_name=None, tags=None, tenant_id=None, type=None,
                 vpd_base_info=None, vpd_id=None, zone_id=None):
        self.cidr = cidr  # type: str
        self.create_time = create_time  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.message = message  # type: str
        self.nc_count = nc_count  # type: long
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.subnet_id = subnet_id  # type: str
        self.subnet_name = subnet_name  # type: str
        self.tags = tags  # type: list[ListSubnetsResponseBodyContentDataTags]
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.vpd_base_info = vpd_base_info  # type: ListSubnetsResponseBodyContentDataVpdBaseInfo
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super(ListSubnetsResponseBodyContentData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.vpd_base_info is not None:
            result['VpdBaseInfo'] = self.vpd_base_info.to_map()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListSubnetsResponseBodyContentDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpdBaseInfo') is not None:
            temp_model = ListSubnetsResponseBodyContentDataVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListSubnetsResponseBodyContent(TeaModel):
    def __init__(self, data=None, total=None):
        self.data = data  # type: list[ListSubnetsResponseBodyContentData]
        self.total = total  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubnetsResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSubnetsResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSubnetsResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: ListSubnetsResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(ListSubnetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = ListSubnetsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSubnetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSubnetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubnetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubnetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVccGrantRulesRequest(TeaModel):
    def __init__(self, enable_page=None, er_id=None, for_select=None, grant_rule_id=None, grant_tenant_id=None,
                 instance_id=None, instance_name=None, page_number=None, page_size=None, region_id=None):
        self.enable_page = enable_page  # type: bool
        self.er_id = er_id  # type: str
        self.for_select = for_select  # type: bool
        self.grant_rule_id = grant_rule_id  # type: str
        self.grant_tenant_id = grant_tenant_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVccGrantRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.for_select is not None:
            result['ForSelect'] = self.for_select
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ForSelect') is not None:
            self.for_select = m.get('ForSelect')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListVccGrantRulesResponseBodyContentData(TeaModel):
    def __init__(self, create_time=None, er_id=None, grant_rule_id=None, grant_tenant_id=None, instance_id=None,
                 instance_name=None, product=None, region_id=None, tenant_id=None, used=None):
        self.create_time = create_time  # type: str
        self.er_id = er_id  # type: str
        self.grant_rule_id = grant_rule_id  # type: str
        self.grant_tenant_id = grant_tenant_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.product = product  # type: str
        self.region_id = region_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.used = used  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVccGrantRulesResponseBodyContentData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.used is not None:
            result['Used'] = self.used
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        return self


class ListVccGrantRulesResponseBodyContent(TeaModel):
    def __init__(self, data=None, total=None):
        self.data = data  # type: list[ListVccGrantRulesResponseBodyContentData]
        self.total = total  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVccGrantRulesResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVccGrantRulesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVccGrantRulesResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: ListVccGrantRulesResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(ListVccGrantRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = ListVccGrantRulesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVccGrantRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVccGrantRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVccGrantRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVccGrantRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVccsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVccsRequestTag, self).to_map()
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


class ListVccsRequest(TeaModel):
    def __init__(self, bandwidth=None, cen_id=None, enable_page=None, ex_status=None, filter_er_id=None,
                 page_number=None, page_size=None, region_id=None, resource_group_id=None, status=None, tag=None, vcc_id=None,
                 vpc_id=None, vpd_id=None):
        self.bandwidth = bandwidth  # type: int
        self.cen_id = cen_id  # type: str
        self.enable_page = enable_page  # type: bool
        self.ex_status = ex_status  # type: str
        self.filter_er_id = filter_er_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.tag = tag  # type: list[ListVccsRequestTag]
        self.vcc_id = vcc_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVccsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.ex_status is not None:
            result['ExStatus'] = self.ex_status
        if self.filter_er_id is not None:
            result['FilterErId'] = self.filter_er_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('ExStatus') is not None:
            self.ex_status = m.get('ExStatus')
        if m.get('FilterErId') is not None:
            self.filter_er_id = m.get('FilterErId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListVccsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class ListVccsResponseBodyContentDataErInfos(TeaModel):
    def __init__(self, connections=None, create_time=None, description=None, er_id=None, er_name=None,
                 gmt_modified=None, master_zone_id=None, message=None, region_id=None, route_maps=None, status=None,
                 tenant_id=None):
        self.connections = connections  # type: long
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.er_id = er_id  # type: str
        self.er_name = er_name  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.master_zone_id = master_zone_id  # type: str
        self.message = message  # type: str
        self.region_id = region_id  # type: str
        self.route_maps = route_maps  # type: long
        self.status = status  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVccsResponseBodyContentDataErInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMaps') is not None:
            self.route_maps = m.get('RouteMaps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListVccsResponseBodyContentDataTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVccsResponseBodyContentDataTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListVccsResponseBodyContentDataVpdBaseInfo(TeaModel):
    def __init__(self, cidr=None, create_time=None, vpd_id=None, vpd_name=None):
        self.cidr = cidr  # type: str
        self.create_time = create_time  # type: str
        self.vpd_id = vpd_id  # type: str
        self.vpd_name = vpd_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVccsResponseBodyContentDataVpdBaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class ListVccsResponseBodyContentData(TeaModel):
    def __init__(self, access_point_id=None, bandwidth_str=None, bgp_cidr=None, cen_id=None, commodity_code=None,
                 connection_type=None, create_time=None, current_node=None, er_infos=None, expiration_date=None, gmt_modified=None,
                 line_operator=None, message=None, port_type=None, rate=None, region_id=None, resource_group_id=None, spec=None,
                 status=None, tags=None, task_id=None, tenant_id=None, vcc_id=None, vcc_name=None, vpc_id=None,
                 vpd_base_info=None, vpd_id=None, zone_id=None):
        self.access_point_id = access_point_id  # type: str
        self.bandwidth_str = bandwidth_str  # type: str
        self.bgp_cidr = bgp_cidr  # type: str
        self.cen_id = cen_id  # type: str
        self.commodity_code = commodity_code  # type: str
        self.connection_type = connection_type  # type: str
        self.create_time = create_time  # type: str
        self.current_node = current_node  # type: str
        self.er_infos = er_infos  # type: list[ListVccsResponseBodyContentDataErInfos]
        self.expiration_date = expiration_date  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.line_operator = line_operator  # type: str
        self.message = message  # type: str
        self.port_type = port_type  # type: str
        self.rate = rate  # type: float
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.spec = spec  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: list[ListVccsResponseBodyContentDataTags]
        self.task_id = task_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.vcc_id = vcc_id  # type: str
        self.vcc_name = vcc_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpd_base_info = vpd_base_info  # type: ListVccsResponseBodyContentDataVpdBaseInfo
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.er_infos:
            for k in self.er_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super(ListVccsResponseBodyContentData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id
        if self.bandwidth_str is not None:
            result['BandwidthStr'] = self.bandwidth_str
        if self.bgp_cidr is not None:
            result['BgpCidr'] = self.bgp_cidr
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_node is not None:
            result['CurrentNode'] = self.current_node
        result['ErInfos'] = []
        if self.er_infos is not None:
            for k in self.er_infos:
                result['ErInfos'].append(k.to_map() if k else None)
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator
        if self.message is not None:
            result['Message'] = self.message
        if self.port_type is not None:
            result['PortType'] = self.port_type
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_name is not None:
            result['VccName'] = self.vcc_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpd_base_info is not None:
            result['VpdBaseInfo'] = self.vpd_base_info.to_map()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')
        if m.get('BandwidthStr') is not None:
            self.bandwidth_str = m.get('BandwidthStr')
        if m.get('BgpCidr') is not None:
            self.bgp_cidr = m.get('BgpCidr')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentNode') is not None:
            self.current_node = m.get('CurrentNode')
        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k in m.get('ErInfos'):
                temp_model = ListVccsResponseBodyContentDataErInfos()
                self.er_infos.append(temp_model.from_map(k))
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVccsResponseBodyContentDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdBaseInfo') is not None:
            temp_model = ListVccsResponseBodyContentDataVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m['VpdBaseInfo'])
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListVccsResponseBodyContent(TeaModel):
    def __init__(self, data=None, total=None):
        self.data = data  # type: list[ListVccsResponseBodyContentData]
        self.total = total  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVccsResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVccsResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVccsResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: ListVccsResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(ListVccsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = ListVccsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVccsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVccsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVccsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVccsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpdGrantRulesRequest(TeaModel):
    def __init__(self, enable_page=None, er_id=None, for_select=None, grant_rule_id=None, grant_tenant_id=None,
                 instance_id=None, instance_name=None, page_number=None, page_size=None, region_id=None):
        self.enable_page = enable_page  # type: bool
        self.er_id = er_id  # type: str
        self.for_select = for_select  # type: bool
        self.grant_rule_id = grant_rule_id  # type: str
        self.grant_tenant_id = grant_tenant_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpdGrantRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.for_select is not None:
            result['ForSelect'] = self.for_select
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ForSelect') is not None:
            self.for_select = m.get('ForSelect')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListVpdGrantRulesResponseBodyContentData(TeaModel):
    def __init__(self, create_time=None, er_id=None, grant_rule_id=None, grant_tenant_id=None, instance_id=None,
                 instance_name=None, product=None, region_id=None, tenant_id=None, used=None):
        self.create_time = create_time  # type: str
        self.er_id = er_id  # type: str
        self.grant_rule_id = grant_rule_id  # type: str
        self.grant_tenant_id = grant_tenant_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.product = product  # type: str
        self.region_id = region_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.used = used  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpdGrantRulesResponseBodyContentData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id
        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.used is not None:
            result['Used'] = self.used
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')
        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        return self


class ListVpdGrantRulesResponseBodyContent(TeaModel):
    def __init__(self, data=None, total=None):
        self.data = data  # type: list[ListVpdGrantRulesResponseBodyContentData]
        self.total = total  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpdGrantRulesResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVpdGrantRulesResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVpdGrantRulesResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: ListVpdGrantRulesResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(ListVpdGrantRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = ListVpdGrantRulesResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVpdGrantRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpdGrantRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpdGrantRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVpdGrantRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpdsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpdsRequestTag, self).to_map()
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


class ListVpdsRequest(TeaModel):
    def __init__(self, client_token=None, enable_page=None, filter_er_id=None, for_select=None, page_number=None,
                 page_size=None, region_id=None, resource_group_id=None, status=None, tag=None, vpd_id=None, vpd_name=None,
                 with_dependence=None, without_vcc=None):
        self.client_token = client_token  # type: str
        self.enable_page = enable_page  # type: bool
        self.filter_er_id = filter_er_id  # type: str
        self.for_select = for_select  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.tag = tag  # type: list[ListVpdsRequestTag]
        self.vpd_id = vpd_id  # type: str
        self.vpd_name = vpd_name  # type: str
        self.with_dependence = with_dependence  # type: bool
        self.without_vcc = without_vcc  # type: bool

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.filter_er_id is not None:
            result['FilterErId'] = self.filter_er_id
        if self.for_select is not None:
            result['ForSelect'] = self.for_select
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        if self.with_dependence is not None:
            result['WithDependence'] = self.with_dependence
        if self.without_vcc is not None:
            result['WithoutVcc'] = self.without_vcc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('FilterErId') is not None:
            self.filter_er_id = m.get('FilterErId')
        if m.get('ForSelect') is not None:
            self.for_select = m.get('ForSelect')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListVpdsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        if m.get('WithDependence') is not None:
            self.with_dependence = m.get('WithDependence')
        if m.get('WithoutVcc') is not None:
            self.without_vcc = m.get('WithoutVcc')
        return self


class ListVpdsResponseBodyContentDataErInfos(TeaModel):
    def __init__(self, connections=None, create_time=None, description=None, er_id=None, er_name=None,
                 gmt_modified=None, master_zone_id=None, message=None, region_id=None, route_maps=None, status=None,
                 tenant_id=None):
        self.connections = connections  # type: long
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.er_id = er_id  # type: str
        self.er_name = er_name  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.master_zone_id = master_zone_id  # type: str
        self.message = message  # type: str
        self.region_id = region_id  # type: str
        self.route_maps = route_maps  # type: long
        self.status = status  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpdsResponseBodyContentDataErInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connections is not None:
            result['Connections'] = self.connections
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.er_id is not None:
            result['ErId'] = self.er_id
        if self.er_name is not None:
            result['ErName'] = self.er_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')
        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RouteMaps') is not None:
            self.route_maps = m.get('RouteMaps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListVpdsResponseBodyContentDataTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpdsResponseBodyContentDataTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListVpdsResponseBodyContentData(TeaModel):
    def __init__(self, cidr=None, create_time=None, dependence=None, er_infos=None, gmt_modified=None, message=None,
                 nc_count=None, region_id=None, resource_group_id=None, service_cidr=None, status=None, subnet_count=None,
                 tags=None, tenant_id=None, vpd_id=None, vpd_name=None):
        self.cidr = cidr  # type: str
        self.create_time = create_time  # type: str
        self.dependence = dependence  # type: dict[str, any]
        self.er_infos = er_infos  # type: list[ListVpdsResponseBodyContentDataErInfos]
        self.gmt_modified = gmt_modified  # type: str
        self.message = message  # type: str
        self.nc_count = nc_count  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.service_cidr = service_cidr  # type: str
        self.status = status  # type: str
        self.subnet_count = subnet_count  # type: int
        self.tags = tags  # type: list[ListVpdsResponseBodyContentDataTags]
        self.tenant_id = tenant_id  # type: str
        # vpd id
        self.vpd_id = vpd_id  # type: str
        self.vpd_name = vpd_name  # type: str

    def validate(self):
        if self.er_infos:
            for k in self.er_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpdsResponseBodyContentData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dependence is not None:
            result['Dependence'] = self.dependence
        result['ErInfos'] = []
        if self.er_infos is not None:
            for k in self.er_infos:
                result['ErInfos'].append(k.to_map() if k else None)
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_cidr is not None:
            result['ServiceCidr'] = self.service_cidr
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_count is not None:
            result['SubnetCount'] = self.subnet_count
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Dependence') is not None:
            self.dependence = m.get('Dependence')
        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k in m.get('ErInfos'):
                temp_model = ListVpdsResponseBodyContentDataErInfos()
                self.er_infos.append(temp_model.from_map(k))
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceCidr') is not None:
            self.service_cidr = m.get('ServiceCidr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetCount') is not None:
            self.subnet_count = m.get('SubnetCount')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVpdsResponseBodyContentDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class ListVpdsResponseBodyContent(TeaModel):
    def __init__(self, data=None, total=None):
        self.data = data  # type: list[ListVpdsResponseBodyContentData]
        self.total = total  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpdsResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVpdsResponseBodyContentData()
                self.data.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVpdsResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: ListVpdsResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(ListVpdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = ListVpdsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVpdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpdsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVpdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnAssignPrivateIpAddressRequest(TeaModel):
    def __init__(self, client_token=None, ip_name=None, network_interface_id=None, private_ip_address=None,
                 region_id=None, subnet_id=None):
        self.client_token = client_token  # type: str
        self.ip_name = ip_name  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.region_id = region_id  # type: str
        self.subnet_id = subnet_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnAssignPrivateIpAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class UnAssignPrivateIpAddressResponseBodyContent(TeaModel):
    def __init__(self, ip_name=None, network_interface_id=None):
        self.ip_name = ip_name  # type: str
        self.network_interface_id = network_interface_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnAssignPrivateIpAddressResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        return self


class UnAssignPrivateIpAddressResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: UnAssignPrivateIpAddressResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(UnAssignPrivateIpAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = UnAssignPrivateIpAddressResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnAssignPrivateIpAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnAssignPrivateIpAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnAssignPrivateIpAddressResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnAssignPrivateIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubnetRequest(TeaModel):
    def __init__(self, description=None, region_id=None, subnet_id=None, subnet_name=None, vpd_id=None, zone_id=None):
        self.description = description  # type: str
        self.region_id = region_id  # type: str
        self.subnet_id = subnet_id  # type: str
        self.subnet_name = subnet_name  # type: str
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubnetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateSubnetResponseBodyContent(TeaModel):
    def __init__(self, subnet_id=None):
        self.subnet_id = subnet_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubnetResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        return self


class UpdateSubnetResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: UpdateSubnetResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(UpdateSubnetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = UpdateSubnetResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSubnetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSubnetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSubnetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSubnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVccRequest(TeaModel):
    def __init__(self, bandwidth=None, order_id=None, region_id=None, vcc_id=None, vcc_name=None):
        self.bandwidth = bandwidth  # type: int
        self.order_id = order_id  # type: str
        self.region_id = region_id  # type: str
        self.vcc_id = vcc_id  # type: str
        self.vcc_name = vcc_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVccRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vcc_name is not None:
            result['VccName'] = self.vcc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')
        return self


class UpdateVccResponseBodyContent(TeaModel):
    def __init__(self, vcc_id=None):
        self.vcc_id = vcc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVccResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        return self


class UpdateVccResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: UpdateVccResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(UpdateVccResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = UpdateVccResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateVccResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVccResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVccResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateVccResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVpdRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, vpd_id=None, vpd_name=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.vpd_id = vpd_id  # type: str
        self.vpd_name = vpd_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')
        return self


class UpdateVpdResponseBodyContent(TeaModel):
    def __init__(self, vpd_id=None):
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpdResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class UpdateVpdResponseBody(TeaModel):
    def __init__(self, code=None, content=None, message=None, request_id=None):
        self.code = code  # type: int
        self.content = content  # type: UpdateVpdResponseBodyContent
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(UpdateVpdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = UpdateVpdResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateVpdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVpdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVpdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateVpdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


