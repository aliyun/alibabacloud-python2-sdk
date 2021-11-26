# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllocateAnycastEipAddressRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, description=None, instance_charge_type=None,
                 internet_charge_type=None, name=None, service_location=None):
        self.bandwidth = bandwidth  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.name = name  # type: str
        self.service_location = service_location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateAnycastEipAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        return self


class AllocateAnycastEipAddressResponseBody(TeaModel):
    def __init__(self, anycast_id=None, order_id=None, request_id=None):
        self.anycast_id = anycast_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateAnycastEipAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocateAnycastEipAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AllocateAnycastEipAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllocateAnycastEipAddressResponse, self).to_map()
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
            temp_model = AllocateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAnycastEipAddressRequestPopLocations(TeaModel):
    def __init__(self, pop_location=None):
        # pop location
        self.pop_location = pop_location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAnycastEipAddressRequestPopLocations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class AssociateAnycastEipAddressRequest(TeaModel):
    def __init__(self, anycast_id=None, association_mode=None, bind_instance_id=None, bind_instance_region_id=None,
                 bind_instance_type=None, client_token=None, dry_run=None, pop_locations=None, private_ip_address=None):
        self.anycast_id = anycast_id  # type: str
        # 关联模式，默认模式、普通模式Default/Normal
        self.association_mode = association_mode  # type: str
        self.bind_instance_id = bind_instance_id  # type: str
        self.bind_instance_region_id = bind_instance_region_id  # type: str
        self.bind_instance_type = bind_instance_type  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        # 绑定时关联的pop location，如果是绑定的第一个实例，该参数会忽略，会下发到全部pop点
        self.pop_locations = pop_locations  # type: list[AssociateAnycastEipAddressRequestPopLocations]
        # 私网ip地址
        self.private_ip_address = private_ip_address  # type: str

    def validate(self):
        if self.pop_locations:
            for k in self.pop_locations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AssociateAnycastEipAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.association_mode is not None:
            result['AssociationMode'] = self.association_mode
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['PopLocations'] = []
        if self.pop_locations is not None:
            for k in self.pop_locations:
                result['PopLocations'].append(k.to_map() if k else None)
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('AssociationMode') is not None:
            self.association_mode = m.get('AssociationMode')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.pop_locations = []
        if m.get('PopLocations') is not None:
            for k in m.get('PopLocations'):
                temp_model = AssociateAnycastEipAddressRequestPopLocations()
                self.pop_locations.append(temp_model.from_map(k))
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class AssociateAnycastEipAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAnycastEipAddressResponseBody, self).to_map()
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


class AssociateAnycastEipAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssociateAnycastEipAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateAnycastEipAddressResponse, self).to_map()
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
            temp_model = AssociateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastEipAddressRequest(TeaModel):
    def __init__(self, anycast_id=None, bind_instance_id=None):
        self.anycast_id = anycast_id  # type: str
        self.bind_instance_id = bind_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAnycastEipAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        return self


class DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations(TeaModel):
    def __init__(self, pop_location=None):
        # PopLocation
        self.pop_location = pop_location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList(TeaModel):
    def __init__(self, association_mode=None, bind_instance_id=None, bind_instance_region_id=None,
                 bind_instance_type=None, bind_time=None, pop_locations=None, private_ip_address=None, status=None):
        # 绑定模式 Normal、Default
        self.association_mode = association_mode  # type: str
        self.bind_instance_id = bind_instance_id  # type: str
        self.bind_instance_region_id = bind_instance_region_id  # type: str
        self.bind_instance_type = bind_instance_type  # type: str
        self.bind_time = bind_time  # type: str
        # 关联的pop点
        self.pop_locations = pop_locations  # type: list[DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations]
        # ip地址
        self.private_ip_address = private_ip_address  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.pop_locations:
            for k in self.pop_locations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_mode is not None:
            result['AssociationMode'] = self.association_mode
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.bind_time is not None:
            result['BindTime'] = self.bind_time
        result['PopLocations'] = []
        if self.pop_locations is not None:
            for k in self.pop_locations:
                result['PopLocations'].append(k.to_map() if k else None)
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociationMode') is not None:
            self.association_mode = m.get('AssociationMode')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')
        self.pop_locations = []
        if m.get('PopLocations') is not None:
            for k in m.get('PopLocations'):
                temp_model = DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations()
                self.pop_locations.append(temp_model.from_map(k))
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAnycastEipAddressResponseBody(TeaModel):
    def __init__(self, ali_uid=None, anycast_eip_bind_info_list=None, anycast_id=None, bandwidth=None, bid=None,
                 business_status=None, create_time=None, description=None, instance_charge_type=None, internet_charge_type=None,
                 ip_address=None, name=None, request_id=None, service_location=None, status=None):
        self.ali_uid = ali_uid  # type: long
        self.anycast_eip_bind_info_list = anycast_eip_bind_info_list  # type: list[DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList]
        self.anycast_id = anycast_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.bid = bid  # type: str
        self.business_status = business_status  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.ip_address = ip_address  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.service_location = service_location  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.anycast_eip_bind_info_list:
            for k in self.anycast_eip_bind_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAnycastEipAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['AnycastEipBindInfoList'] = []
        if self.anycast_eip_bind_info_list is not None:
            for k in self.anycast_eip_bind_info_list:
                result['AnycastEipBindInfoList'].append(k.to_map() if k else None)
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.anycast_eip_bind_info_list = []
        if m.get('AnycastEipBindInfoList') is not None:
            for k in m.get('AnycastEipBindInfoList'):
                temp_model = DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList()
                self.anycast_eip_bind_info_list.append(temp_model.from_map(k))
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAnycastEipAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAnycastEipAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAnycastEipAddressResponse, self).to_map()
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
            temp_model = DescribeAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastPopLocationsRequest(TeaModel):
    def __init__(self, service_location=None):
        self.service_location = service_location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAnycastPopLocationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        return self


class DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList(TeaModel):
    def __init__(self, region_id=None, region_name=None):
        self.region_id = region_id  # type: str
        self.region_name = region_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeAnycastPopLocationsResponseBody(TeaModel):
    def __init__(self, anycast_pop_location_list=None, count=None, request_id=None):
        self.anycast_pop_location_list = anycast_pop_location_list  # type: list[DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList]
        self.count = count  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.anycast_pop_location_list:
            for k in self.anycast_pop_location_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAnycastPopLocationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnycastPopLocationList'] = []
        if self.anycast_pop_location_list is not None:
            for k in self.anycast_pop_location_list:
                result['AnycastPopLocationList'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.anycast_pop_location_list = []
        if m.get('AnycastPopLocationList') is not None:
            for k in m.get('AnycastPopLocationList'):
                temp_model = DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList()
                self.anycast_pop_location_list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAnycastPopLocationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAnycastPopLocationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAnycastPopLocationsResponse, self).to_map()
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
            temp_model = DescribeAnycastPopLocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastServerRegionsRequest(TeaModel):
    def __init__(self, service_location=None):
        self.service_location = service_location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAnycastServerRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        return self


class DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList(TeaModel):
    def __init__(self, region_id=None, region_name=None):
        self.region_id = region_id  # type: str
        self.region_name = region_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeAnycastServerRegionsResponseBody(TeaModel):
    def __init__(self, anycast_server_region_list=None, count=None, request_id=None):
        self.anycast_server_region_list = anycast_server_region_list  # type: list[DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList]
        self.count = count  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.anycast_server_region_list:
            for k in self.anycast_server_region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAnycastServerRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnycastServerRegionList'] = []
        if self.anycast_server_region_list is not None:
            for k in self.anycast_server_region_list:
                result['AnycastServerRegionList'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.anycast_server_region_list = []
        if m.get('AnycastServerRegionList') is not None:
            for k in m.get('AnycastServerRegionList'):
                temp_model = DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList()
                self.anycast_server_region_list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAnycastServerRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAnycastServerRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAnycastServerRegionsResponse, self).to_map()
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
            temp_model = DescribeAnycastServerRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnycastEipAddressesRequest(TeaModel):
    def __init__(self, anycast_eip_address=None, anycast_id=None, bind_instance_ids=None, business_status=None,
                 instance_charge_type=None, internet_charge_type=None, max_results=None, name=None, next_token=None,
                 service_location=None, status=None):
        self.anycast_eip_address = anycast_eip_address  # type: str
        self.anycast_id = anycast_id  # type: str
        self.bind_instance_ids = bind_instance_ids  # type: list[str]
        self.business_status = business_status  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.max_results = max_results  # type: int
        self.name = name  # type: str
        self.next_token = next_token  # type: str
        self.service_location = service_location  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnycastEipAddressesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_eip_address is not None:
            result['AnycastEipAddress'] = self.anycast_eip_address
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bind_instance_ids is not None:
            result['BindInstanceIds'] = self.bind_instance_ids
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastEipAddress') is not None:
            self.anycast_eip_address = m.get('AnycastEipAddress')
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('BindInstanceIds') is not None:
            self.bind_instance_ids = m.get('BindInstanceIds')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList(TeaModel):
    def __init__(self, bind_instance_id=None, bind_instance_region_id=None, bind_instance_type=None,
                 bind_time=None):
        self.bind_instance_id = bind_instance_id  # type: str
        self.bind_instance_region_id = bind_instance_region_id  # type: str
        self.bind_instance_type = bind_instance_type  # type: str
        self.bind_time = bind_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.bind_time is not None:
            result['BindTime'] = self.bind_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')
        return self


class ListAnycastEipAddressesResponseBodyAnycastList(TeaModel):
    def __init__(self, ali_uid=None, anycast_eip_bind_info_list=None, anycast_id=None, bandwidth=None, bid=None,
                 business_status=None, create_time=None, description=None, instance_charge_type=None, internet_charge_type=None,
                 ip_address=None, name=None, service_location=None, status=None):
        self.ali_uid = ali_uid  # type: long
        self.anycast_eip_bind_info_list = anycast_eip_bind_info_list  # type: list[ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList]
        self.anycast_id = anycast_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.bid = bid  # type: str
        self.business_status = business_status  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.ip_address = ip_address  # type: str
        self.name = name  # type: str
        self.service_location = service_location  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.anycast_eip_bind_info_list:
            for k in self.anycast_eip_bind_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnycastEipAddressesResponseBodyAnycastList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['AnycastEipBindInfoList'] = []
        if self.anycast_eip_bind_info_list is not None:
            for k in self.anycast_eip_bind_info_list:
                result['AnycastEipBindInfoList'].append(k.to_map() if k else None)
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.name is not None:
            result['Name'] = self.name
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.anycast_eip_bind_info_list = []
        if m.get('AnycastEipBindInfoList') is not None:
            for k in m.get('AnycastEipBindInfoList'):
                temp_model = ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList()
                self.anycast_eip_bind_info_list.append(temp_model.from_map(k))
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAnycastEipAddressesResponseBody(TeaModel):
    def __init__(self, anycast_list=None, next_token=None, request_id=None, total_count=None):
        self.anycast_list = anycast_list  # type: list[ListAnycastEipAddressesResponseBodyAnycastList]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.anycast_list:
            for k in self.anycast_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnycastEipAddressesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnycastList'] = []
        if self.anycast_list is not None:
            for k in self.anycast_list:
                result['AnycastList'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.anycast_list = []
        if m.get('AnycastList') is not None:
            for k in m.get('AnycastList'):
                temp_model = ListAnycastEipAddressesResponseBodyAnycastList()
                self.anycast_list.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAnycastEipAddressesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAnycastEipAddressesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAnycastEipAddressesResponse, self).to_map()
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
            temp_model = ListAnycastEipAddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAnycastEipAddressAttributeRequest(TeaModel):
    def __init__(self, anycast_id=None, description=None, name=None):
        self.anycast_id = anycast_id  # type: str
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAnycastEipAddressAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyAnycastEipAddressAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAnycastEipAddressAttributeResponseBody, self).to_map()
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


class ModifyAnycastEipAddressAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyAnycastEipAddressAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAnycastEipAddressAttributeResponse, self).to_map()
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
            temp_model = ModifyAnycastEipAddressAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAnycastEipAddressSpecRequest(TeaModel):
    def __init__(self, anycast_id=None, bandwidth=None):
        self.anycast_id = anycast_id  # type: str
        self.bandwidth = bandwidth  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAnycastEipAddressSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class ModifyAnycastEipAddressSpecResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAnycastEipAddressSpecResponseBody, self).to_map()
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


class ModifyAnycastEipAddressSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyAnycastEipAddressSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAnycastEipAddressSpecResponse, self).to_map()
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
            temp_model = ModifyAnycastEipAddressSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseAnycastEipAddressRequest(TeaModel):
    def __init__(self, anycast_id=None, client_token=None):
        self.anycast_id = anycast_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseAnycastEipAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ReleaseAnycastEipAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseAnycastEipAddressResponseBody, self).to_map()
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


class ReleaseAnycastEipAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReleaseAnycastEipAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseAnycastEipAddressResponse, self).to_map()
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
            temp_model = ReleaseAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassociateAnycastEipAddressRequest(TeaModel):
    def __init__(self, anycast_id=None, bind_instance_id=None, bind_instance_region_id=None,
                 bind_instance_type=None, client_token=None, dry_run=None, private_ip_address=None):
        self.anycast_id = anycast_id  # type: str
        self.bind_instance_id = bind_instance_id  # type: str
        self.bind_instance_region_id = bind_instance_region_id  # type: str
        self.bind_instance_type = bind_instance_type  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: str
        self.private_ip_address = private_ip_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnassociateAnycastEipAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class UnassociateAnycastEipAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 私网IP地址
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnassociateAnycastEipAddressResponseBody, self).to_map()
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


class UnassociateAnycastEipAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnassociateAnycastEipAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnassociateAnycastEipAddressResponse, self).to_map()
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
            temp_model = UnassociateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAnycastEipAddressAssociationsRequestPopLocationAddList(TeaModel):
    def __init__(self, pop_location=None):
        # pop location
        self.pop_location = pop_location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAnycastEipAddressAssociationsRequestPopLocationAddList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class UpdateAnycastEipAddressAssociationsRequestPopLocationDeleteList(TeaModel):
    def __init__(self, pop_location=None):
        # pop location
        self.pop_location = pop_location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAnycastEipAddressAssociationsRequestPopLocationDeleteList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class UpdateAnycastEipAddressAssociationsRequest(TeaModel):
    def __init__(self, anycast_id=None, association_mode=None, bind_instance_id=None, client_token=None,
                 dry_run=None, pop_location_add_list=None, pop_location_delete_list=None):
        self.anycast_id = anycast_id  # type: str
        # 关联模式，默认模式、普通模式Default/Normal
        self.association_mode = association_mode  # type: str
        self.bind_instance_id = bind_instance_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        # 新增关联的pop location
        self.pop_location_add_list = pop_location_add_list  # type: list[UpdateAnycastEipAddressAssociationsRequestPopLocationAddList]
        # 待删除的关联pop location
        self.pop_location_delete_list = pop_location_delete_list  # type: list[UpdateAnycastEipAddressAssociationsRequestPopLocationDeleteList]

    def validate(self):
        if self.pop_location_add_list:
            for k in self.pop_location_add_list:
                if k:
                    k.validate()
        if self.pop_location_delete_list:
            for k in self.pop_location_delete_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateAnycastEipAddressAssociationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.association_mode is not None:
            result['AssociationMode'] = self.association_mode
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['PopLocationAddList'] = []
        if self.pop_location_add_list is not None:
            for k in self.pop_location_add_list:
                result['PopLocationAddList'].append(k.to_map() if k else None)
        result['PopLocationDeleteList'] = []
        if self.pop_location_delete_list is not None:
            for k in self.pop_location_delete_list:
                result['PopLocationDeleteList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('AssociationMode') is not None:
            self.association_mode = m.get('AssociationMode')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.pop_location_add_list = []
        if m.get('PopLocationAddList') is not None:
            for k in m.get('PopLocationAddList'):
                temp_model = UpdateAnycastEipAddressAssociationsRequestPopLocationAddList()
                self.pop_location_add_list.append(temp_model.from_map(k))
        self.pop_location_delete_list = []
        if m.get('PopLocationDeleteList') is not None:
            for k in m.get('PopLocationDeleteList'):
                temp_model = UpdateAnycastEipAddressAssociationsRequestPopLocationDeleteList()
                self.pop_location_delete_list.append(temp_model.from_map(k))
        return self


class UpdateAnycastEipAddressAssociationsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAnycastEipAddressAssociationsResponseBody, self).to_map()
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


class UpdateAnycastEipAddressAssociationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAnycastEipAddressAssociationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAnycastEipAddressAssociationsResponse, self).to_map()
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
            temp_model = UpdateAnycastEipAddressAssociationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


