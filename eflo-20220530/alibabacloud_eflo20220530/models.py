# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateSubnetRequest(TeaModel):
    def __init__(self, cidr=None, name=None, region_id=None, type=None, vpd_id=None, zone_id=None):
        self.cidr = cidr  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubnetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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


class CreateVccRequest(TeaModel):
    def __init__(self, access_could_service=None, bgp_cidr=None, cen_id=None, description=None, region_id=None,
                 v_switch_id=None, vcc_id=None, vpc_id=None, vpd_id=None):
        self.access_could_service = access_could_service  # type: bool
        self.bgp_cidr = bgp_cidr  # type: str
        self.cen_id = cen_id  # type: str
        self.description = description  # type: str
        self.region_id = region_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vcc_id = vcc_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

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
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessCouldService') is not None:
            self.access_could_service = m.get('AccessCouldService')
        if m.get('BgpCidr') is not None:
            self.bgp_cidr = m.get('BgpCidr')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
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
    def __init__(self, cidr=None, name=None, region_id=None, type=None, zone_id=None):
        self.cidr = cidr  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
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
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateVpdRequest(TeaModel):
    def __init__(self, cidr=None, name=None, region_id=None, subnets=None):
        self.cidr = cidr  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.subnets = subnets  # type: list[CreateVpdRequestSubnets]

    def validate(self):
        if self.subnets:
            for k in self.subnets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateVpdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Subnets'] = []
        if self.subnets is not None:
            for k in self.subnets:
                result['Subnets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.subnets = []
        if m.get('Subnets') is not None:
            for k in m.get('Subnets'):
                temp_model = CreateVpdRequestSubnets()
                self.subnets.append(temp_model.from_map(k))
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


class GetSubnetRequest(TeaModel):
    def __init__(self, subnet_id=None):
        self.subnet_id = subnet_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubnetRequest, self).to_map()
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


class GetSubnetResponseBodyContentVpdBaseInfo(TeaModel):
    def __init__(self, cidr=None, gmt_create=None, name=None, vpd_id=None):
        self.cidr = cidr  # type: str
        self.gmt_create = gmt_create  # type: str
        self.name = name  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubnetResponseBodyContentVpdBaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class GetSubnetResponseBodyContent(TeaModel):
    def __init__(self, cidr=None, description=None, gmt_create=None, gmt_modified=None, id=None, lb_count=None,
                 message=None, name=None, nc_count=None, region_id=None, status=None, subnet_id=None, tenant_id=None,
                 type=None, vpd_base_info=None, vpd_id=None, zone_id=None):
        self.cidr = cidr  # type: str
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        # ID
        self.id = id  # type: long
        self.lb_count = lb_count  # type: long
        self.message = message  # type: str
        self.name = name  # type: str
        self.nc_count = nc_count  # type: long
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.subnet_id = subnet_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.vpd_base_info = vpd_base_info  # type: GetSubnetResponseBodyContentVpdBaseInfo
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super(GetSubnetResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.lb_count is not None:
            result['LbCount'] = self.lb_count
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
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
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LbCount') is not None:
            self.lb_count = m.get('LbCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
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
    def __init__(self, region_id=None, vcc_id=None):
        self.region_id = region_id  # type: str
        self.vcc_id = vcc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVccRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
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


class GetVccResponseBodyContentVpdBaseInfo(TeaModel):
    def __init__(self, cidr=None, gmt_create=None, name=None, vpd_id=None):
        self.cidr = cidr  # type: str
        self.gmt_create = gmt_create  # type: str
        self.name = name  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVccResponseBodyContentVpdBaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class GetVccResponseBodyContent(TeaModel):
    def __init__(self, access_point_id=None, aliyun_router_info=None, bandwidth_str=None, bgp_cidr=None,
                 cen_id=None, cis_router_info=None, commodity_code=None, create_time=None, current_node=None,
                 duration=None, gmt_modified=None, internet_charge_type=None, line_operator=None, message=None,
                 pay_type=None, port_type=None, pricing_cycle=None, region_id=None, spec=None, status=None, tenant_id=None,
                 v_switch_id=None, vcc_id=None, vcc_name=None, vpc_id=None, vpd_base_info=None, vpd_id=None):
        self.access_point_id = access_point_id  # type: str
        self.aliyun_router_info = aliyun_router_info  # type: list[GetVccResponseBodyContentAliyunRouterInfo]
        self.bandwidth_str = bandwidth_str  # type: str
        self.bgp_cidr = bgp_cidr  # type: str
        self.cen_id = cen_id  # type: str
        self.cis_router_info = cis_router_info  # type: list[GetVccResponseBodyContentCisRouterInfo]
        self.commodity_code = commodity_code  # type: str
        self.create_time = create_time  # type: str
        self.current_node = current_node  # type: str
        self.duration = duration  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.line_operator = line_operator  # type: str
        self.message = message  # type: str
        self.pay_type = pay_type  # type: str
        self.port_type = port_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.region_id = region_id  # type: str
        self.spec = spec  # type: str
        self.status = status  # type: str
        self.tenant_id = tenant_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vcc_id = vcc_id  # type: str
        self.vcc_name = vcc_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpd_base_info = vpd_base_info  # type: GetVccResponseBodyContentVpdBaseInfo
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        if self.aliyun_router_info:
            for k in self.aliyun_router_info:
                if k:
                    k.validate()
        if self.cis_router_info:
            for k in self.cis_router_info:
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_node is not None:
            result['CurrentNode'] = self.current_node
        if self.duration is not None:
            result['Duration'] = self.duration
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
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentNode') is not None:
            self.current_node = m.get('CurrentNode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
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
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
    def __init__(self, vpd_id=None):
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpdRequest, self).to_map()
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


class GetVpdResponseBodyContent(TeaModel):
    def __init__(self, cidr=None, description=None, gmt_create=None, gmt_modified=None, lb_count=None, message=None,
                 name=None, nc_count=None, region_id=None, route=None, service_cidr=None, status=None, subnet_count=None,
                 vcc_count=None, vpd_id=None):
        self.cidr = cidr  # type: str
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.lb_count = lb_count  # type: long
        self.message = message  # type: str
        self.name = name  # type: str
        self.nc_count = nc_count  # type: long
        self.region_id = region_id  # type: str
        self.route = route  # type: int
        self.service_cidr = service_cidr  # type: str
        self.status = status  # type: str
        self.subnet_count = subnet_count  # type: long
        self.vcc_count = vcc_count  # type: long
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpdResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.lb_count is not None:
            result['LbCount'] = self.lb_count
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route is not None:
            result['Route'] = self.route
        if self.service_cidr is not None:
            result['ServiceCidr'] = self.service_cidr
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_count is not None:
            result['SubnetCount'] = self.subnet_count
        if self.vcc_count is not None:
            result['VccCount'] = self.vcc_count
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LbCount') is not None:
            self.lb_count = m.get('LbCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('ServiceCidr') is not None:
            self.service_cidr = m.get('ServiceCidr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetCount') is not None:
            self.subnet_count = m.get('SubnetCount')
        if m.get('VccCount') is not None:
            self.vcc_count = m.get('VccCount')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
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


class ListSubnetsRequest(TeaModel):
    def __init__(self, enable_page=None, name=None, page_number=None, page_size=None, region_id=None, status=None,
                 subnet_id=None, type=None, vpd_id=None, zone_id=None):
        self.enable_page = enable_page  # type: bool
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.subnet_id = subnet_id  # type: str
        self.type = type  # type: str
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubnetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
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
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListSubnetsResponseBodyContentDataVpdBaseInfo(TeaModel):
    def __init__(self, cidr=None, gmt_create=None, name=None, vpd_id=None):
        self.cidr = cidr  # type: str
        self.gmt_create = gmt_create  # type: str
        self.name = name  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubnetsResponseBodyContentDataVpdBaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class ListSubnetsResponseBodyContentData(TeaModel):
    def __init__(self, cidr=None, gmt_create=None, gmt_modified=None, id=None, message=None, name=None, nc_count=None,
                 region_id=None, status=None, subnet_id=None, tenant_id=None, type=None, vpd_base_info=None, vpd_id=None,
                 zone_id=None):
        self.cidr = cidr  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.message = message  # type: str
        self.name = name  # type: str
        self.nc_count = nc_count  # type: long
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.subnet_id = subnet_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.vpd_base_info = vpd_base_info  # type: ListSubnetsResponseBodyContentDataVpdBaseInfo
        self.vpd_id = vpd_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        _map = super(ListSubnetsResponseBodyContentData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
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
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
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


class ListVccsRequest(TeaModel):
    def __init__(self, bandwidth=None, cen_id=None, enable_page=None, ex_status=None, page_number=None,
                 page_size=None, region_id=None, status=None, vcc_id=None, vpc_id=None, vpd_id=None):
        self.bandwidth = bandwidth  # type: int
        self.cen_id = cen_id  # type: str
        self.enable_page = enable_page  # type: bool
        self.ex_status = ex_status  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.vcc_id = vcc_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class ListVccsResponseBodyContentDataVpdBaseInfo(TeaModel):
    def __init__(self, cidr=None, gmt_create=None, name=None, vpd_id=None):
        self.cidr = cidr  # type: str
        self.gmt_create = gmt_create  # type: str
        self.name = name  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVccsResponseBodyContentDataVpdBaseInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class ListVccsResponseBodyContentData(TeaModel):
    def __init__(self, access_point_id=None, bandwidth_str=None, bgp_cidr=None, cen_id=None, create_time=None,
                 gmt_modified=None, line_operator=None, message=None, port_type=None, rate=None, region_id=None, spec=None,
                 status=None, tenant_id=None, vcc_id=None, vcc_name=None, vpc_id=None, vpd_base_info=None, vpd_id=None):
        self.access_point_id = access_point_id  # type: str
        self.bandwidth_str = bandwidth_str  # type: str
        self.bgp_cidr = bgp_cidr  # type: str
        self.cen_id = cen_id  # type: str
        self.create_time = create_time  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.line_operator = line_operator  # type: str
        self.message = message  # type: str
        self.port_type = port_type  # type: str
        self.rate = rate  # type: float
        self.region_id = region_id  # type: str
        self.spec = spec  # type: str
        self.status = status  # type: str
        self.tenant_id = tenant_id  # type: str
        self.vcc_id = vcc_id  # type: str
        self.vcc_name = vcc_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpd_base_info = vpd_base_info  # type: ListVccsResponseBodyContentDataVpdBaseInfo
        self.vpd_id = vpd_id  # type: str

    def validate(self):
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
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
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
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
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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


class ListVpdsRequest(TeaModel):
    def __init__(self, enable_page=None, filter_er_id=None, for_select=None, name=None, page_number=None,
                 page_size=None, region_id=None, status=None, vpd_id=None, with_dependence=None, without_vcc=None):
        self.enable_page = enable_page  # type: bool
        self.filter_er_id = filter_er_id  # type: str
        self.for_select = for_select  # type: bool
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.vpd_id = vpd_id  # type: str
        self.with_dependence = with_dependence  # type: bool
        self.without_vcc = without_vcc  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page
        if self.filter_er_id is not None:
            result['FilterErId'] = self.filter_er_id
        if self.for_select is not None:
            result['ForSelect'] = self.for_select
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.with_dependence is not None:
            result['WithDependence'] = self.with_dependence
        if self.without_vcc is not None:
            result['WithoutVcc'] = self.without_vcc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')
        if m.get('FilterErId') is not None:
            self.filter_er_id = m.get('FilterErId')
        if m.get('ForSelect') is not None:
            self.for_select = m.get('ForSelect')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('WithDependence') is not None:
            self.with_dependence = m.get('WithDependence')
        if m.get('WithoutVcc') is not None:
            self.without_vcc = m.get('WithoutVcc')
        return self


class ListVpdsResponseBodyContentData(TeaModel):
    def __init__(self, cidr=None, dependence=None, gmt_create=None, gmt_modified=None, message=None, name=None,
                 nc_count=None, region_id=None, route=None, service_cidr=None, status=None, subnet_count=None, vpd_id=None):
        self.cidr = cidr  # type: str
        self.dependence = dependence  # type: dict[str, any]
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.nc_count = nc_count  # type: int
        self.region_id = region_id  # type: str
        self.route = route  # type: int
        self.service_cidr = service_cidr  # type: str
        self.status = status  # type: str
        self.subnet_count = subnet_count  # type: int
        # vpd id
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpdsResponseBodyContentData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.dependence is not None:
            result['Dependence'] = self.dependence
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.nc_count is not None:
            result['NcCount'] = self.nc_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.route is not None:
            result['Route'] = self.route
        if self.service_cidr is not None:
            result['ServiceCidr'] = self.service_cidr
        if self.status is not None:
            result['Status'] = self.status
        if self.subnet_count is not None:
            result['SubnetCount'] = self.subnet_count
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('Dependence') is not None:
            self.dependence = m.get('Dependence')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('ServiceCidr') is not None:
            self.service_cidr = m.get('ServiceCidr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubnetCount') is not None:
            self.subnet_count = m.get('SubnetCount')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
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


class UpdateSubnetRequest(TeaModel):
    def __init__(self, description=None, name=None, region_id=None, subnet_id=None, vpd_id=None, zone_id=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.subnet_id = subnet_id  # type: str
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
        if self.name is not None:
            result['Name'] = self.name
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
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
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
    def __init__(self, description=None, name=None, region_id=None, vpd_id=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
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


