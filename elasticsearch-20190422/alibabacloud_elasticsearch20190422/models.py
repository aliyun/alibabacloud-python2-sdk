# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeVSwitchesRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, page_number=None, page_size=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, vpc_id=None, zone_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVSwitchesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeVSwitchesResponseBodyVSwitchesVSwitch(TeaModel):
    def __init__(self, cidr_block=None, gmt_create=None, is_default=None, status=None, v_switch_id=None,
                 v_switch_name=None):
        self.cidr_block = cidr_block  # type: str
        self.gmt_create = gmt_create  # type: str
        self.is_default = is_default  # type: bool
        self.status = status  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.v_switch_name = v_switch_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVSwitchesResponseBodyVSwitchesVSwitch, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeVSwitchesResponseBodyVSwitches(TeaModel):
    def __init__(self, v_switch=None):
        self.v_switch = v_switch  # type: list[DescribeVSwitchesResponseBodyVSwitchesVSwitch]

    def validate(self):
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVSwitchesResponseBodyVSwitches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k in m.get('VSwitch'):
                temp_model = DescribeVSwitchesResponseBodyVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        return self


class DescribeVSwitchesResponseBody(TeaModel):
    def __init__(self, request_id=None, v_switches=None):
        self.request_id = request_id  # type: str
        self.v_switches = v_switches  # type: DescribeVSwitchesResponseBodyVSwitches

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        _map = super(DescribeVSwitchesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitches') is not None:
            temp_model = DescribeVSwitchesResponseBodyVSwitches()
            self.v_switches = temp_model.from_map(m['VSwitches'])
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVSwitchesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVSwitchesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, page_number=None, page_size=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, security_token=None, zone_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_token = security_token  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeVpcsResponseBodyVpcsVpc(TeaModel):
    def __init__(self, cidr_block=None, gmt_create=None, gmt_modified=None, is_default=None, region_no=None,
                 status=None, v_switchs=None, vpc_id=None, vpc_name=None):
        self.cidr_block = cidr_block  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.is_default = is_default  # type: bool
        self.region_no = region_no  # type: str
        self.status = status  # type: str
        self.v_switchs = v_switchs  # type: list[str]
        self.vpc_id = vpc_id  # type: str
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcsResponseBodyVpcsVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switchs is not None:
            result['VSwitchs'] = self.v_switchs
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchs') is not None:
            self.v_switchs = m.get('VSwitchs')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcsResponseBodyVpcs(TeaModel):
    def __init__(self, vpc=None):
        self.vpc = vpc  # type: list[DescribeVpcsResponseBodyVpcsVpc]

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcsResponseBodyVpcs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = DescribeVpcsResponseBodyVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class DescribeVpcsResponseBody(TeaModel):
    def __init__(self, request_id=None, vpcs=None):
        self.request_id = request_id  # type: str
        self.vpcs = vpcs  # type: DescribeVpcsResponseBodyVpcs

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        _map = super(DescribeVpcsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Vpcs') is not None:
            temp_model = DescribeVpcsResponseBodyVpcs()
            self.vpcs = temp_model.from_map(m['Vpcs'])
        return self


class DescribeVpcsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVpcsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVpcsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


