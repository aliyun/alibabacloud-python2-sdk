# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateDrdsAccountRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, password=None, user_name=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.password = password  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDrdsAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateDrdsAccountResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDrdsAccountResponseBody, self).to_map()
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


class CreateDrdsAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDrdsAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDrdsAccountResponse, self).to_map()
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
            temp_model = CreateDrdsAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDrdsDBRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, encode=None, password=None, rds_instances=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.encode = encode  # type: str
        self.password = password  # type: str
        self.rds_instances = rds_instances  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDrdsDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.encode is not None:
            result['Encode'] = self.encode
        if self.password is not None:
            result['Password'] = self.password
        if self.rds_instances is not None:
            result['RdsInstances'] = self.rds_instances
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('Encode') is not None:
            self.encode = m.get('Encode')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RdsInstances') is not None:
            self.rds_instances = m.get('RdsInstances')
        return self


class CreateDrdsDBResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDrdsDBResponseBody, self).to_map()
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


class CreateDrdsDBResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDrdsDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDrdsDBResponse, self).to_map()
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
            temp_model = CreateDrdsDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDrdsInstanceRequest(TeaModel):
    def __init__(self, client_token=None, description=None, duration=None, instance_series=None, is_auto_renew=None,
                 is_ha=None, pay_type=None, pricing_cycle=None, quantity=None, region_id=None, specification=None,
                 type=None, vpc_id=None, vswitch_id=None, zone_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.duration = duration  # type: int
        self.instance_series = instance_series  # type: str
        self.is_auto_renew = is_auto_renew  # type: bool
        self.is_ha = is_ha  # type: bool
        self.pay_type = pay_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.quantity = quantity  # type: int
        self.region_id = region_id  # type: str
        self.specification = specification  # type: str
        self.type = type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDrdsInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_series is not None:
            result['InstanceSeries'] = self.instance_series
        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew
        if self.is_ha is not None:
            result['IsHa'] = self.is_ha
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceSeries') is not None:
            self.instance_series = m.get('InstanceSeries')
        if m.get('IsAutoRenew') is not None:
            self.is_auto_renew = m.get('IsAutoRenew')
        if m.get('IsHa') is not None:
            self.is_ha = m.get('IsHa')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDrdsInstanceResponseBodyDataDrdsInstanceIdList(TeaModel):
    def __init__(self, drds_instance_id=None):
        self.drds_instance_id = drds_instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDrdsInstanceResponseBodyDataDrdsInstanceIdList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class CreateDrdsInstanceResponseBodyData(TeaModel):
    def __init__(self, drds_instance_id_list=None, order_id=None):
        self.drds_instance_id_list = drds_instance_id_list  # type: CreateDrdsInstanceResponseBodyDataDrdsInstanceIdList
        self.order_id = order_id  # type: long

    def validate(self):
        if self.drds_instance_id_list:
            self.drds_instance_id_list.validate()

    def to_map(self):
        _map = super(CreateDrdsInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id_list is not None:
            result['DrdsInstanceIdList'] = self.drds_instance_id_list.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsInstanceIdList') is not None:
            temp_model = CreateDrdsInstanceResponseBodyDataDrdsInstanceIdList()
            self.drds_instance_id_list = temp_model.from_map(m['DrdsInstanceIdList'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateDrdsInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: CreateDrdsInstanceResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateDrdsInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateDrdsInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDrdsInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDrdsInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDrdsInstanceResponse, self).to_map()
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
            temp_model = CreateDrdsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReadOnlyAccountRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, password=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.password = password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReadOnlyAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self


class CreateReadOnlyAccountResponseBodyData(TeaModel):
    def __init__(self, account_name=None, db_name=None, drds_instance_id=None):
        self.account_name = account_name  # type: str
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReadOnlyAccountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class CreateReadOnlyAccountResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: CreateReadOnlyAccountResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateReadOnlyAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateReadOnlyAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateReadOnlyAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateReadOnlyAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateReadOnlyAccountResponse, self).to_map()
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
            temp_model = CreateReadOnlyAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDrdsDBRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDrdsDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class DeleteDrdsDBResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDrdsDBResponseBody, self).to_map()
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


class DeleteDrdsDBResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDrdsDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDrdsDBResponse, self).to_map()
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
            temp_model = DeleteDrdsDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFailedDrdsDBRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFailedDrdsDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class DeleteFailedDrdsDBResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFailedDrdsDBResponseBody, self).to_map()
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


class DeleteFailedDrdsDBResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFailedDrdsDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFailedDrdsDBResponse, self).to_map()
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
            temp_model = DeleteFailedDrdsDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCreateDrdsInstanceStatusRequest(TeaModel):
    def __init__(self, drds_instance_id=None):
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCreateDrdsInstanceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class DescribeCreateDrdsInstanceStatusResponseBodyData(TeaModel):
    def __init__(self, status=None):
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCreateDrdsInstanceStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCreateDrdsInstanceStatusResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeCreateDrdsInstanceStatusResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCreateDrdsInstanceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeCreateDrdsInstanceStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCreateDrdsInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCreateDrdsInstanceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCreateDrdsInstanceStatusResponse, self).to_map()
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
            temp_model = DescribeCreateDrdsInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDrdsDBRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class DescribeDrdsDBResponseBodyData(TeaModel):
    def __init__(self, create_time=None, db_name=None, mode=None, msg=None, status=None):
        self.create_time = create_time  # type: str
        self.db_name = db_name  # type: str
        self.mode = mode  # type: str
        self.msg = msg  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsDBResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDrdsDBResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeDrdsDBResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDrdsDBResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDrdsDBResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDrdsDBResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDrdsDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDrdsDBResponse, self).to_map()
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
            temp_model = DescribeDrdsDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDrdsDBIpWhiteListRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, group_name=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.group_name = group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsDBIpWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeDrdsDBIpWhiteListResponseBodyDataIpWhiteList(TeaModel):
    def __init__(self, ip=None):
        self.ip = ip  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsDBIpWhiteListResponseBodyDataIpWhiteList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDrdsDBIpWhiteListResponseBodyData(TeaModel):
    def __init__(self, ip_white_list=None):
        self.ip_white_list = ip_white_list  # type: DescribeDrdsDBIpWhiteListResponseBodyDataIpWhiteList

    def validate(self):
        if self.ip_white_list:
            self.ip_white_list.validate()

    def to_map(self):
        _map = super(DescribeDrdsDBIpWhiteListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_white_list is not None:
            result['IpWhiteList'] = self.ip_white_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpWhiteList') is not None:
            temp_model = DescribeDrdsDBIpWhiteListResponseBodyDataIpWhiteList()
            self.ip_white_list = temp_model.from_map(m['IpWhiteList'])
        return self


class DescribeDrdsDBIpWhiteListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeDrdsDBIpWhiteListResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDrdsDBIpWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDrdsDBIpWhiteListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDrdsDBIpWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDrdsDBIpWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDrdsDBIpWhiteListResponse, self).to_map()
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
            temp_model = DescribeDrdsDBIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDrdsDBsRequest(TeaModel):
    def __init__(self, drds_instance_id=None):
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsDBsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class DescribeDrdsDBsResponseBodyDataDb(TeaModel):
    def __init__(self, create_time=None, db_name=None, mode=None, msg=None, status=None):
        self.create_time = create_time  # type: str
        self.db_name = db_name  # type: str
        self.mode = mode  # type: str
        self.msg = msg  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsDBsResponseBodyDataDb, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDrdsDBsResponseBodyData(TeaModel):
    def __init__(self, db=None):
        self.db = db  # type: list[DescribeDrdsDBsResponseBodyDataDb]

    def validate(self):
        if self.db:
            for k in self.db:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDrdsDBsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Db'] = []
        if self.db is not None:
            for k in self.db:
                result['Db'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.db = []
        if m.get('Db') is not None:
            for k in m.get('Db'):
                temp_model = DescribeDrdsDBsResponseBodyDataDb()
                self.db.append(temp_model.from_map(k))
        return self


class DescribeDrdsDBsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeDrdsDBsResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDrdsDBsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDrdsDBsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDrdsDBsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDrdsDBsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDrdsDBsResponse, self).to_map()
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
            temp_model = DescribeDrdsDBsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDrdsInstanceRequest(TeaModel):
    def __init__(self, drds_instance_id=None):
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class DescribeDrdsInstanceResponseBodyDataVipsVip(TeaModel):
    def __init__(self, ip=None, port=None, type=None, vpc_id=None, vswitch_id=None):
        self.ip = ip  # type: str
        self.port = port  # type: str
        self.type = type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstanceResponseBodyDataVipsVip, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeDrdsInstanceResponseBodyDataVips(TeaModel):
    def __init__(self, vip=None):
        self.vip = vip  # type: list[DescribeDrdsInstanceResponseBodyDataVipsVip]

    def validate(self):
        if self.vip:
            for k in self.vip:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceResponseBodyDataVips, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vip'] = []
        if self.vip is not None:
            for k in self.vip:
                result['Vip'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vip = []
        if m.get('Vip') is not None:
            for k in m.get('Vip'):
                temp_model = DescribeDrdsInstanceResponseBodyDataVipsVip()
                self.vip.append(temp_model.from_map(k))
        return self


class DescribeDrdsInstanceResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, drds_instance_id=None, network_type=None, region_id=None,
                 specification=None, status=None, type=None, version=None, vips=None, vpc_cloud_instance_id=None, zone_id=None):
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.network_type = network_type  # type: str
        self.region_id = region_id  # type: str
        self.specification = specification  # type: str
        self.status = status  # type: str
        self.type = type  # type: str
        self.version = version  # type: long
        self.vips = vips  # type: DescribeDrdsInstanceResponseBodyDataVips
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.vips:
            self.vips.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        if self.vips is not None:
            result['Vips'] = self.vips.to_map()
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Vips') is not None:
            temp_model = DescribeDrdsInstanceResponseBodyDataVips()
            self.vips = temp_model.from_map(m['Vips'])
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDrdsInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeDrdsInstanceResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDrdsInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDrdsInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDrdsInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceResponse, self).to_map()
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
            temp_model = DescribeDrdsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDrdsInstanceDbMonitorRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, end_time=None, key=None, start_time=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.end_time = end_time  # type: long
        self.key = key  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstanceDbMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceDataValuesPerformanceValue(TeaModel):
    def __init__(self, date=None, value=None):
        self.date = date  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceDataValuesPerformanceValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceDataValues(TeaModel):
    def __init__(self, performance_value=None):
        self.performance_value = performance_value  # type: list[DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceDataValuesPerformanceValue]

    def validate(self):
        if self.performance_value:
            for k in self.performance_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceDataValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceValue'] = []
        if self.performance_value is not None:
            for k in self.performance_value:
                result['PerformanceValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.performance_value = []
        if m.get('PerformanceValue') is not None:
            for k in m.get('PerformanceValue'):
                temp_model = DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceDataValuesPerformanceValue()
                self.performance_value.append(temp_model.from_map(k))
        return self


class DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceData(TeaModel):
    def __init__(self, key=None, unit=None, values=None):
        self.key = key  # type: str
        self.unit = unit  # type: str
        self.values = values  # type: DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceDataValues

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('Values') is not None:
            temp_model = DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class DescribeDrdsInstanceDbMonitorResponseBodyData(TeaModel):
    def __init__(self, partial_performance_data=None):
        self.partial_performance_data = partial_performance_data  # type: list[DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceData]

    def validate(self):
        if self.partial_performance_data:
            for k in self.partial_performance_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceDbMonitorResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PartialPerformanceData'] = []
        if self.partial_performance_data is not None:
            for k in self.partial_performance_data:
                result['PartialPerformanceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.partial_performance_data = []
        if m.get('PartialPerformanceData') is not None:
            for k in m.get('PartialPerformanceData'):
                temp_model = DescribeDrdsInstanceDbMonitorResponseBodyDataPartialPerformanceData()
                self.partial_performance_data.append(temp_model.from_map(k))
        return self


class DescribeDrdsInstanceDbMonitorResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeDrdsInstanceDbMonitorResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceDbMonitorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDrdsInstanceDbMonitorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDrdsInstanceDbMonitorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDrdsInstanceDbMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceDbMonitorResponse, self).to_map()
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
            temp_model = DescribeDrdsInstanceDbMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDrdsInstanceMonitorRequest(TeaModel):
    def __init__(self, drds_instance_id=None, end_time=None, key=None, period_multiple=None, start_time=None):
        self.drds_instance_id = drds_instance_id  # type: str
        self.end_time = end_time  # type: long
        self.key = key  # type: str
        self.period_multiple = period_multiple  # type: int
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstanceMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.period_multiple is not None:
            result['PeriodMultiple'] = self.period_multiple
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('PeriodMultiple') is not None:
            self.period_multiple = m.get('PeriodMultiple')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceDataValuesPerformanceValue(TeaModel):
    def __init__(self, date=None, value=None):
        self.date = date  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceDataValuesPerformanceValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceDataValues(TeaModel):
    def __init__(self, performance_value=None):
        self.performance_value = performance_value  # type: list[DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceDataValuesPerformanceValue]

    def validate(self):
        if self.performance_value:
            for k in self.performance_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceDataValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceValue'] = []
        if self.performance_value is not None:
            for k in self.performance_value:
                result['PerformanceValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.performance_value = []
        if m.get('PerformanceValue') is not None:
            for k in m.get('PerformanceValue'):
                temp_model = DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceDataValuesPerformanceValue()
                self.performance_value.append(temp_model.from_map(k))
        return self


class DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceData(TeaModel):
    def __init__(self, key=None, unit=None, values=None):
        self.key = key  # type: str
        self.unit = unit  # type: str
        self.values = values  # type: DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceDataValues

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('Values') is not None:
            temp_model = DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceDataValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class DescribeDrdsInstanceMonitorResponseBodyData(TeaModel):
    def __init__(self, partial_performance_data=None):
        self.partial_performance_data = partial_performance_data  # type: list[DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceData]

    def validate(self):
        if self.partial_performance_data:
            for k in self.partial_performance_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceMonitorResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PartialPerformanceData'] = []
        if self.partial_performance_data is not None:
            for k in self.partial_performance_data:
                result['PartialPerformanceData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.partial_performance_data = []
        if m.get('PartialPerformanceData') is not None:
            for k in m.get('PartialPerformanceData'):
                temp_model = DescribeDrdsInstanceMonitorResponseBodyDataPartialPerformanceData()
                self.partial_performance_data.append(temp_model.from_map(k))
        return self


class DescribeDrdsInstanceMonitorResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeDrdsInstanceMonitorResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceMonitorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDrdsInstanceMonitorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDrdsInstanceMonitorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDrdsInstanceMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceMonitorResponse, self).to_map()
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
            temp_model = DescribeDrdsInstanceMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDrdsInstanceNetInfoForInnerRequest(TeaModel):
    def __init__(self, drds_instance_id=None):
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstanceNetInfoForInnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class DescribeDrdsInstanceNetInfoForInnerResponseBodyNetInfosNetInfo(TeaModel):
    def __init__(self, ip=None, is_for_vpc=None, port=None, type=None):
        self.ip = ip  # type: str
        self.is_for_vpc = is_for_vpc  # type: bool
        self.port = port  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstanceNetInfoForInnerResponseBodyNetInfosNetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.is_for_vpc is not None:
            result['IsForVpc'] = self.is_for_vpc
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('IsForVpc') is not None:
            self.is_for_vpc = m.get('IsForVpc')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDrdsInstanceNetInfoForInnerResponseBodyNetInfos(TeaModel):
    def __init__(self, net_info=None):
        self.net_info = net_info  # type: list[DescribeDrdsInstanceNetInfoForInnerResponseBodyNetInfosNetInfo]

    def validate(self):
        if self.net_info:
            for k in self.net_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceNetInfoForInnerResponseBodyNetInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetInfo'] = []
        if self.net_info is not None:
            for k in self.net_info:
                result['NetInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.net_info = []
        if m.get('NetInfo') is not None:
            for k in m.get('NetInfo'):
                temp_model = DescribeDrdsInstanceNetInfoForInnerResponseBodyNetInfosNetInfo()
                self.net_info.append(temp_model.from_map(k))
        return self


class DescribeDrdsInstanceNetInfoForInnerResponseBody(TeaModel):
    def __init__(self, drds_instance_id=None, net_infos=None, network_type=None, request_id=None, success=None):
        self.drds_instance_id = drds_instance_id  # type: str
        self.net_infos = net_infos  # type: DescribeDrdsInstanceNetInfoForInnerResponseBodyNetInfos
        self.network_type = network_type  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.net_infos:
            self.net_infos.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceNetInfoForInnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.net_infos is not None:
            result['NetInfos'] = self.net_infos.to_map()
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('NetInfos') is not None:
            temp_model = DescribeDrdsInstanceNetInfoForInnerResponseBodyNetInfos()
            self.net_infos = temp_model.from_map(m['NetInfos'])
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDrdsInstanceNetInfoForInnerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDrdsInstanceNetInfoForInnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstanceNetInfoForInnerResponse, self).to_map()
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
            temp_model = DescribeDrdsInstanceNetInfoForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDrdsInstancesRequest(TeaModel):
    def __init__(self, region_id=None, tags=None, type=None):
        self.region_id = region_id  # type: str
        self.tags = tags  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDrdsInstancesResponseBodyDataInstanceSlaveInstId(TeaModel):
    def __init__(self, inst_id=None):
        self.inst_id = inst_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstancesResponseBodyDataInstanceSlaveInstId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inst_id is not None:
            result['instId'] = self.inst_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instId') is not None:
            self.inst_id = m.get('instId')
        return self


class DescribeDrdsInstancesResponseBodyDataInstanceVipsVip(TeaModel):
    def __init__(self, ip=None, port=None, type=None, vpc_id=None, vswitch_id=None):
        self.ip = ip  # type: str
        self.port = port  # type: str
        self.type = type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDrdsInstancesResponseBodyDataInstanceVipsVip, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeDrdsInstancesResponseBodyDataInstanceVips(TeaModel):
    def __init__(self, vip=None):
        self.vip = vip  # type: list[DescribeDrdsInstancesResponseBodyDataInstanceVipsVip]

    def validate(self):
        if self.vip:
            for k in self.vip:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstancesResponseBodyDataInstanceVips, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vip'] = []
        if self.vip is not None:
            for k in self.vip:
                result['Vip'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vip = []
        if m.get('Vip') is not None:
            for k in m.get('Vip'):
                temp_model = DescribeDrdsInstancesResponseBodyDataInstanceVipsVip()
                self.vip.append(temp_model.from_map(k))
        return self


class DescribeDrdsInstancesResponseBodyDataInstance(TeaModel):
    def __init__(self, create_time=None, description=None, drds_instance_id=None, inst_role=None,
                 master_inst_id=None, network_type=None, region_id=None, slave_inst_id=None, status=None, type=None, version=None,
                 vips=None, vpc_cloud_instance_id=None, zone_id=None):
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.inst_role = inst_role  # type: str
        self.master_inst_id = master_inst_id  # type: str
        self.network_type = network_type  # type: str
        self.region_id = region_id  # type: str
        self.slave_inst_id = slave_inst_id  # type: DescribeDrdsInstancesResponseBodyDataInstanceSlaveInstId
        self.status = status  # type: str
        self.type = type  # type: str
        self.version = version  # type: long
        self.vips = vips  # type: DescribeDrdsInstancesResponseBodyDataInstanceVips
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.slave_inst_id:
            self.slave_inst_id.validate()
        if self.vips:
            self.vips.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstancesResponseBodyDataInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.inst_role is not None:
            result['InstRole'] = self.inst_role
        if self.master_inst_id is not None:
            result['MasterInstId'] = self.master_inst_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.slave_inst_id is not None:
            result['SlaveInstId'] = self.slave_inst_id.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        if self.vips is not None:
            result['Vips'] = self.vips.to_map()
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('InstRole') is not None:
            self.inst_role = m.get('InstRole')
        if m.get('MasterInstId') is not None:
            self.master_inst_id = m.get('MasterInstId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SlaveInstId') is not None:
            temp_model = DescribeDrdsInstancesResponseBodyDataInstanceSlaveInstId()
            self.slave_inst_id = temp_model.from_map(m['SlaveInstId'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Vips') is not None:
            temp_model = DescribeDrdsInstancesResponseBodyDataInstanceVips()
            self.vips = temp_model.from_map(m['Vips'])
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDrdsInstancesResponseBodyData(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance  # type: list[DescribeDrdsInstancesResponseBodyDataInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeDrdsInstancesResponseBodyDataInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeDrdsInstancesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeDrdsInstancesResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDrdsInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDrdsInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDrdsInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDrdsInstancesResponse, self).to_map()
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
            temp_model = DescribeDrdsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRdsListRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, region_id=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRdsListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRdsListResponseBodyDataRdsInstanceReadOnlyChildrenChild(TeaModel):
    def __init__(self, connect_url=None, db_type=None, instance_id=None, instance_name=None, instance_status=None,
                 read_weight=None, port=None):
        self.connect_url = connect_url  # type: str
        self.db_type = db_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_status = instance_status  # type: str
        self.read_weight = read_weight  # type: int
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRdsListResponseBodyDataRdsInstanceReadOnlyChildrenChild, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_url is not None:
            result['ConnectUrl'] = self.connect_url
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.read_weight is not None:
            result['ReadWeight'] = self.read_weight
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectUrl') is not None:
            self.connect_url = m.get('ConnectUrl')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('ReadWeight') is not None:
            self.read_weight = m.get('ReadWeight')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self


class DescribeRdsListResponseBodyDataRdsInstanceReadOnlyChildren(TeaModel):
    def __init__(self, child=None):
        self.child = child  # type: list[DescribeRdsListResponseBodyDataRdsInstanceReadOnlyChildrenChild]

    def validate(self):
        if self.child:
            for k in self.child:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRdsListResponseBodyDataRdsInstanceReadOnlyChildren, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Child'] = []
        if self.child is not None:
            for k in self.child:
                result['Child'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.child = []
        if m.get('Child') is not None:
            for k in m.get('Child'):
                temp_model = DescribeRdsListResponseBodyDataRdsInstanceReadOnlyChildrenChild()
                self.child.append(temp_model.from_map(k))
        return self


class DescribeRdsListResponseBodyDataRdsInstance(TeaModel):
    def __init__(self, connect_url=None, db_type=None, instance_id=None, instance_name=None, instance_status=None,
                 port=None, read_only_children=None, read_weight=None):
        self.connect_url = connect_url  # type: str
        self.db_type = db_type  # type: str
        self.instance_id = instance_id  # type: int
        self.instance_name = instance_name  # type: str
        self.instance_status = instance_status  # type: str
        self.port = port  # type: int
        self.read_only_children = read_only_children  # type: DescribeRdsListResponseBodyDataRdsInstanceReadOnlyChildren
        self.read_weight = read_weight  # type: int

    def validate(self):
        if self.read_only_children:
            self.read_only_children.validate()

    def to_map(self):
        _map = super(DescribeRdsListResponseBodyDataRdsInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_url is not None:
            result['ConnectUrl'] = self.connect_url
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.port is not None:
            result['Port'] = self.port
        if self.read_only_children is not None:
            result['ReadOnlyChildren'] = self.read_only_children.to_map()
        if self.read_weight is not None:
            result['ReadWeight'] = self.read_weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectUrl') is not None:
            self.connect_url = m.get('ConnectUrl')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ReadOnlyChildren') is not None:
            temp_model = DescribeRdsListResponseBodyDataRdsInstanceReadOnlyChildren()
            self.read_only_children = temp_model.from_map(m['ReadOnlyChildren'])
        if m.get('ReadWeight') is not None:
            self.read_weight = m.get('ReadWeight')
        return self


class DescribeRdsListResponseBodyData(TeaModel):
    def __init__(self, rds_instance=None):
        self.rds_instance = rds_instance  # type: list[DescribeRdsListResponseBodyDataRdsInstance]

    def validate(self):
        if self.rds_instance:
            for k in self.rds_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRdsListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RdsInstance'] = []
        if self.rds_instance is not None:
            for k in self.rds_instance:
                result['RdsInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rds_instance = []
        if m.get('RdsInstance') is not None:
            for k in m.get('RdsInstance'):
                temp_model = DescribeRdsListResponseBodyDataRdsInstance()
                self.rds_instance.append(temp_model.from_map(k))
        return self


class DescribeRdsListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeRdsListResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeRdsListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeRdsListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRdsListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRdsListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRdsListResponse, self).to_map()
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
            temp_model = DescribeRdsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeReadOnlyAccountRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReadOnlyAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class DescribeReadOnlyAccountResponseBodyData(TeaModel):
    def __init__(self, account_name=None, db_name=None, drds_instance_id=None):
        self.account_name = account_name  # type: str
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReadOnlyAccountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class DescribeReadOnlyAccountResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeReadOnlyAccountResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeReadOnlyAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeReadOnlyAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeReadOnlyAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeReadOnlyAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeReadOnlyAccountResponse, self).to_map()
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
            temp_model = DescribeReadOnlyAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeriesSpecListSpec(TeaModel):
    def __init__(self, spec_id=None, spec_name=None):
        self.spec_id = spec_id  # type: str
        self.spec_name = spec_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeriesSpecListSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.spec_name is not None:
            result['SpecName'] = self.spec_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')
        return self


class DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeriesSpecList(TeaModel):
    def __init__(self, spec=None):
        self.spec = spec  # type: list[DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeriesSpecListSpec]

    def validate(self):
        if self.spec:
            for k in self.spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeriesSpecList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Spec'] = []
        if self.spec is not None:
            for k in self.spec:
                result['Spec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.spec = []
        if m.get('Spec') is not None:
            for k in m.get('Spec'):
                temp_model = DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeriesSpecListSpec()
                self.spec.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeries(TeaModel):
    def __init__(self, series_id=None, series_name=None, spec_list=None):
        self.series_id = series_id  # type: str
        self.series_name = series_name  # type: str
        self.spec_list = spec_list  # type: DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeriesSpecList

    def validate(self):
        if self.spec_list:
            self.spec_list.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.series_id is not None:
            result['SeriesId'] = self.series_id
        if self.series_name is not None:
            result['SeriesName'] = self.series_name
        if self.spec_list is not None:
            result['SpecList'] = self.spec_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SeriesId') is not None:
            self.series_id = m.get('SeriesId')
        if m.get('SeriesName') is not None:
            self.series_name = m.get('SeriesName')
        if m.get('SpecList') is not None:
            temp_model = DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeriesSpecList()
            self.spec_list = temp_model.from_map(m['SpecList'])
        return self


class DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesList(TeaModel):
    def __init__(self, instance_series=None):
        self.instance_series = instance_series  # type: list[DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeries]

    def validate(self):
        if self.instance_series:
            for k in self.instance_series:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceSeries'] = []
        if self.instance_series is not None:
            for k in self.instance_series:
                result['InstanceSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_series = []
        if m.get('InstanceSeries') is not None:
            for k in m.get('InstanceSeries'):
                temp_model = DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesListInstanceSeries()
                self.instance_series.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyDrdsRegionsDrdsRegion(TeaModel):
    def __init__(self, instance_series_list=None, region_id=None, region_name=None, zone_id=None, zone_name=None):
        self.instance_series_list = instance_series_list  # type: DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesList
        self.region_id = region_id  # type: str
        self.region_name = region_name  # type: str
        self.zone_id = zone_id  # type: str
        self.zone_name = zone_name  # type: str

    def validate(self):
        if self.instance_series_list:
            self.instance_series_list.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyDrdsRegionsDrdsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_series_list is not None:
            result['InstanceSeriesList'] = self.instance_series_list.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceSeriesList') is not None:
            temp_model = DescribeRegionsResponseBodyDrdsRegionsDrdsRegionInstanceSeriesList()
            self.instance_series_list = temp_model.from_map(m['InstanceSeriesList'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class DescribeRegionsResponseBodyDrdsRegions(TeaModel):
    def __init__(self, drds_region=None):
        self.drds_region = drds_region  # type: list[DescribeRegionsResponseBodyDrdsRegionsDrdsRegion]

    def validate(self):
        if self.drds_region:
            for k in self.drds_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyDrdsRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DrdsRegion'] = []
        if self.drds_region is not None:
            for k in self.drds_region:
                result['DrdsRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.drds_region = []
        if m.get('DrdsRegion') is not None:
            for k in m.get('DrdsRegion'):
                temp_model = DescribeRegionsResponseBodyDrdsRegionsDrdsRegion()
                self.drds_region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, drds_regions=None, request_id=None, success=None):
        self.drds_regions = drds_regions  # type: DescribeRegionsResponseBodyDrdsRegions
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.drds_regions:
            self.drds_regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_regions is not None:
            result['DrdsRegions'] = self.drds_regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsRegions') is not None:
            temp_model = DescribeRegionsResponseBodyDrdsRegions()
            self.drds_regions = temp_model.from_map(m['DrdsRegions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeShardDBsRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeShardDBsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class DescribeShardDBsResponseBodyDataDbIntancePair(TeaModel):
    def __init__(self, group_name=None, instance_name=None, sub_db_name=None):
        self.group_name = group_name  # type: str
        self.instance_name = instance_name  # type: str
        self.sub_db_name = sub_db_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeShardDBsResponseBodyDataDbIntancePair, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.sub_db_name is not None:
            result['SubDbName'] = self.sub_db_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('SubDbName') is not None:
            self.sub_db_name = m.get('SubDbName')
        return self


class DescribeShardDBsResponseBodyData(TeaModel):
    def __init__(self, db_intance_pair=None):
        self.db_intance_pair = db_intance_pair  # type: list[DescribeShardDBsResponseBodyDataDbIntancePair]

    def validate(self):
        if self.db_intance_pair:
            for k in self.db_intance_pair:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeShardDBsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DbIntancePair'] = []
        if self.db_intance_pair is not None:
            for k in self.db_intance_pair:
                result['DbIntancePair'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.db_intance_pair = []
        if m.get('DbIntancePair') is not None:
            for k in m.get('DbIntancePair'):
                temp_model = DescribeShardDBsResponseBodyDataDbIntancePair()
                self.db_intance_pair.append(temp_model.from_map(k))
        return self


class DescribeShardDBsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: DescribeShardDBsResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeShardDBsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeShardDBsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeShardDBsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeShardDBsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeShardDBsResponse, self).to_map()
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
            temp_model = DescribeShardDBsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeShardDbConnectionInfoRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, sub_db_name=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.sub_db_name = sub_db_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeShardDbConnectionInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.sub_db_name is not None:
            result['SubDbName'] = self.sub_db_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('SubDbName') is not None:
            self.sub_db_name = m.get('SubDbName')
        return self


class DescribeShardDbConnectionInfoResponseBodyConnectionInfo(TeaModel):
    def __init__(self, instance_name=None, instance_url=None, blocking_timeout=None, connection_properties=None,
                 db_status=None, db_type=None, idle_time_out=None, max_pool_size=None, min_pool_size=None,
                 prepared_statement_cache_size=None, sub_db_name=None, user_name=None):
        self.instance_name = instance_name  # type: str
        self.instance_url = instance_url  # type: str
        self.blocking_timeout = blocking_timeout  # type: int
        self.connection_properties = connection_properties  # type: str
        self.db_status = db_status  # type: str
        self.db_type = db_type  # type: str
        self.idle_time_out = idle_time_out  # type: int
        self.max_pool_size = max_pool_size  # type: int
        self.min_pool_size = min_pool_size  # type: int
        self.prepared_statement_cache_size = prepared_statement_cache_size  # type: int
        self.sub_db_name = sub_db_name  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeShardDbConnectionInfoResponseBodyConnectionInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_url is not None:
            result['InstanceUrl'] = self.instance_url
        if self.blocking_timeout is not None:
            result['blockingTimeout'] = self.blocking_timeout
        if self.connection_properties is not None:
            result['connectionProperties'] = self.connection_properties
        if self.db_status is not None:
            result['dbStatus'] = self.db_status
        if self.db_type is not None:
            result['dbType'] = self.db_type
        if self.idle_time_out is not None:
            result['idleTimeOut'] = self.idle_time_out
        if self.max_pool_size is not None:
            result['maxPoolSize'] = self.max_pool_size
        if self.min_pool_size is not None:
            result['minPoolSize'] = self.min_pool_size
        if self.prepared_statement_cache_size is not None:
            result['preparedStatementCacheSize'] = self.prepared_statement_cache_size
        if self.sub_db_name is not None:
            result['subDbName'] = self.sub_db_name
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceUrl') is not None:
            self.instance_url = m.get('InstanceUrl')
        if m.get('blockingTimeout') is not None:
            self.blocking_timeout = m.get('blockingTimeout')
        if m.get('connectionProperties') is not None:
            self.connection_properties = m.get('connectionProperties')
        if m.get('dbStatus') is not None:
            self.db_status = m.get('dbStatus')
        if m.get('dbType') is not None:
            self.db_type = m.get('dbType')
        if m.get('idleTimeOut') is not None:
            self.idle_time_out = m.get('idleTimeOut')
        if m.get('maxPoolSize') is not None:
            self.max_pool_size = m.get('maxPoolSize')
        if m.get('minPoolSize') is not None:
            self.min_pool_size = m.get('minPoolSize')
        if m.get('preparedStatementCacheSize') is not None:
            self.prepared_statement_cache_size = m.get('preparedStatementCacheSize')
        if m.get('subDbName') is not None:
            self.sub_db_name = m.get('subDbName')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class DescribeShardDbConnectionInfoResponseBody(TeaModel):
    def __init__(self, connection_info=None, request_id=None, success=None):
        self.connection_info = connection_info  # type: DescribeShardDbConnectionInfoResponseBodyConnectionInfo
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.connection_info:
            self.connection_info.validate()

    def to_map(self):
        _map = super(DescribeShardDbConnectionInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_info is not None:
            result['ConnectionInfo'] = self.connection_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionInfo') is not None:
            temp_model = DescribeShardDbConnectionInfoResponseBodyConnectionInfo()
            self.connection_info = temp_model.from_map(m['ConnectionInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeShardDbConnectionInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeShardDbConnectionInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeShardDbConnectionInfoResponse, self).to_map()
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
            temp_model = DescribeShardDbConnectionInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableInstanceRequest(TeaModel):
    def __init__(self, backup_id=None, client_token=None, db_instance_class=None, drds_instance_id=None,
                 engine_version=None, restore_time=None, source_db_inst_id=None, switch_id=None, vpc_id=None, zone_id=None):
        self.backup_id = backup_id  # type: str
        self.client_token = client_token  # type: str
        self.db_instance_class = db_instance_class  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.engine_version = engine_version  # type: str
        self.restore_time = restore_time  # type: str
        self.source_db_inst_id = source_db_inst_id  # type: str
        self.switch_id = switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.db_instance_class is not None:
            result['DbInstanceClass'] = self.db_instance_class
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.source_db_inst_id is not None:
            result['SourceDbInstId'] = self.source_db_inst_id
        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DbInstanceClass') is not None:
            self.db_instance_class = m.get('DbInstanceClass')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('SourceDbInstId') is not None:
            self.source_db_inst_id = m.get('SourceDbInstId')
        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class EnableInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, success=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableInstanceResponse, self).to_map()
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
            temp_model = EnableInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDrdsDBPasswdRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, new_passwd=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.new_passwd = new_passwd  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDrdsDBPasswdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.new_passwd is not None:
            result['NewPasswd'] = self.new_passwd
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('NewPasswd') is not None:
            self.new_passwd = m.get('NewPasswd')
        return self


class ModifyDrdsDBPasswdResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDrdsDBPasswdResponseBody, self).to_map()
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


class ModifyDrdsDBPasswdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDrdsDBPasswdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDrdsDBPasswdResponse, self).to_map()
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
            temp_model = ModifyDrdsDBPasswdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDrdsInstanceDescriptionRequest(TeaModel):
    def __init__(self, description=None, drds_instance_id=None):
        self.description = description  # type: str
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDrdsInstanceDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class ModifyDrdsInstanceDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDrdsInstanceDescriptionResponseBody, self).to_map()
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


class ModifyDrdsInstanceDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDrdsInstanceDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDrdsInstanceDescriptionResponse, self).to_map()
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
            temp_model = ModifyDrdsInstanceDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDrdsIpWhiteListRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, group_attribute=None, group_name=None,
                 ip_white_list=None, mode=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.group_attribute = group_attribute  # type: str
        self.group_name = group_name  # type: str
        self.ip_white_list = ip_white_list  # type: str
        self.mode = mode  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDrdsIpWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.group_attribute is not None:
            result['GroupAttribute'] = self.group_attribute
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_white_list is not None:
            result['IpWhiteList'] = self.ip_white_list
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('GroupAttribute') is not None:
            self.group_attribute = m.get('GroupAttribute')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpWhiteList') is not None:
            self.ip_white_list = m.get('IpWhiteList')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ModifyDrdsIpWhiteListResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDrdsIpWhiteListResponseBody, self).to_map()
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


class ModifyDrdsIpWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDrdsIpWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDrdsIpWhiteListResponse, self).to_map()
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
            temp_model = ModifyDrdsIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFullTableScanRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, full_table_scan=None, table_names=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.full_table_scan = full_table_scan  # type: bool
        self.table_names = table_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFullTableScanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.full_table_scan is not None:
            result['FullTableScan'] = self.full_table_scan
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('FullTableScan') is not None:
            self.full_table_scan = m.get('FullTableScan')
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class ModifyFullTableScanResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFullTableScanResponseBody, self).to_map()
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


class ModifyFullTableScanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyFullTableScanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFullTableScanResponse, self).to_map()
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
            temp_model = ModifyFullTableScanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRdsReadWeightRequest(TeaModel):
    def __init__(self, db_name=None, drds_instance_id=None, instance_names=None, weights=None):
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.instance_names = instance_names  # type: str
        self.weights = weights  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRdsReadWeightRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.instance_names is not None:
            result['InstanceNames'] = self.instance_names
        if self.weights is not None:
            result['Weights'] = self.weights
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('InstanceNames') is not None:
            self.instance_names = m.get('InstanceNames')
        if m.get('Weights') is not None:
            self.weights = m.get('Weights')
        return self


class ModifyRdsReadWeightResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRdsReadWeightResponseBody, self).to_map()
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


class ModifyRdsReadWeightResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyRdsReadWeightResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyRdsReadWeightResponse, self).to_map()
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
            temp_model = ModifyRdsReadWeightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyReadOnlyAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, db_name=None, drds_instance_id=None, new_passwd=None,
                 origin_password=None):
        self.account_name = account_name  # type: str
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.new_passwd = new_passwd  # type: str
        self.origin_password = origin_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyReadOnlyAccountPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.new_passwd is not None:
            result['NewPasswd'] = self.new_passwd
        if self.origin_password is not None:
            result['OriginPassword'] = self.origin_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('NewPasswd') is not None:
            self.new_passwd = m.get('NewPasswd')
        if m.get('OriginPassword') is not None:
            self.origin_password = m.get('OriginPassword')
        return self


class ModifyReadOnlyAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyReadOnlyAccountPasswordResponseBody, self).to_map()
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


class ModifyReadOnlyAccountPasswordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyReadOnlyAccountPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyReadOnlyAccountPasswordResponse, self).to_map()
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
            temp_model = ModifyReadOnlyAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceInfoByConnRequest(TeaModel):
    def __init__(self, host=None, port=None, user_name=None):
        self.host = host  # type: str
        self.port = port  # type: int
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInstanceInfoByConnRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryInstanceInfoByConnResponseBodyDataVipsVip(TeaModel):
    def __init__(self, ip=None, port=None, type=None, vpc_id=None, vswitch_id=None):
        self.ip = ip  # type: str
        self.port = port  # type: str
        self.type = type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInstanceInfoByConnResponseBodyDataVipsVip, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class QueryInstanceInfoByConnResponseBodyDataVips(TeaModel):
    def __init__(self, vip=None):
        self.vip = vip  # type: list[QueryInstanceInfoByConnResponseBodyDataVipsVip]

    def validate(self):
        if self.vip:
            for k in self.vip:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryInstanceInfoByConnResponseBodyDataVips, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vip'] = []
        if self.vip is not None:
            for k in self.vip:
                result['Vip'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vip = []
        if m.get('Vip') is not None:
            for k in m.get('Vip'):
                temp_model = QueryInstanceInfoByConnResponseBodyDataVipsVip()
                self.vip.append(temp_model.from_map(k))
        return self


class QueryInstanceInfoByConnResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, drds_instance_id=None, network_type=None, region_id=None,
                 spec_type_id=None, spec_type_name=None, specification=None, status=None, type=None, version=None, vips=None,
                 vpc_cloud_instance_id=None, zone_id=None):
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.drds_instance_id = drds_instance_id  # type: str
        self.network_type = network_type  # type: str
        self.region_id = region_id  # type: str
        self.spec_type_id = spec_type_id  # type: str
        self.spec_type_name = spec_type_name  # type: str
        self.specification = specification  # type: str
        self.status = status  # type: str
        self.type = type  # type: str
        self.version = version  # type: long
        self.vips = vips  # type: QueryInstanceInfoByConnResponseBodyDataVips
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.vips:
            self.vips.validate()

    def to_map(self):
        _map = super(QueryInstanceInfoByConnResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spec_type_id is not None:
            result['SpecTypeId'] = self.spec_type_id
        if self.spec_type_name is not None:
            result['SpecTypeName'] = self.spec_type_name
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        if self.vips is not None:
            result['Vips'] = self.vips.to_map()
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpecTypeId') is not None:
            self.spec_type_id = m.get('SpecTypeId')
        if m.get('SpecTypeName') is not None:
            self.spec_type_name = m.get('SpecTypeName')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Vips') is not None:
            temp_model = QueryInstanceInfoByConnResponseBodyDataVips()
            self.vips = temp_model.from_map(m['Vips'])
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class QueryInstanceInfoByConnResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, success=None):
        self.data = data  # type: QueryInstanceInfoByConnResponseBodyData
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryInstanceInfoByConnResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryInstanceInfoByConnResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryInstanceInfoByConnResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryInstanceInfoByConnResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryInstanceInfoByConnResponse, self).to_map()
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
            temp_model = QueryInstanceInfoByConnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDrdsInstanceRequest(TeaModel):
    def __init__(self, drds_instance_id=None):
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveDrdsInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class RemoveDrdsInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveDrdsInstanceResponseBody, self).to_map()
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


class RemoveDrdsInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveDrdsInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveDrdsInstanceResponse, self).to_map()
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
            temp_model = RemoveDrdsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveReadOnlyAccountRequest(TeaModel):
    def __init__(self, account_name=None, db_name=None, drds_instance_id=None):
        self.account_name = account_name  # type: str
        self.db_name = db_name  # type: str
        self.drds_instance_id = drds_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveReadOnlyAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.drds_instance_id is not None:
            result['DrdsInstanceId'] = self.drds_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DrdsInstanceId') is not None:
            self.drds_instance_id = m.get('DrdsInstanceId')
        return self


class RemoveReadOnlyAccountResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveReadOnlyAccountResponseBody, self).to_map()
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


class RemoveReadOnlyAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveReadOnlyAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveReadOnlyAccountResponse, self).to_map()
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
            temp_model = RemoveReadOnlyAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


