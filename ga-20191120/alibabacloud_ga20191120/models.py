# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeIpSetRequest(TeaModel):
    def __init__(self, region_id=None, ip_set_id=None):
        self.region_id = region_id  # type: str
        self.ip_set_id = ip_set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        return self


class DescribeIpSetResponseBody(TeaModel):
    def __init__(self, ip_set_id=None, request_id=None, ip_version=None, state=None, bandwidth=None,
                 ip_address_list=None, accelerate_region_id=None, accelerator_id=None):
        self.ip_set_id = ip_set_id  # type: str
        self.request_id = request_id  # type: str
        self.ip_version = ip_version  # type: str
        self.state = state  # type: str
        self.bandwidth = bandwidth  # type: int
        self.ip_address_list = ip_address_list  # type: list[str]
        self.accelerate_region_id = accelerate_region_id  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.state is not None:
            result['State'] = self.state
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_address_list is not None:
            result['IpAddressList'] = self.ip_address_list
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpAddressList') is not None:
            self.ip_address_list = m.get('IpAddressList')
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class DescribeIpSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpSetResponse, self).to_map()
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
            temp_model = DescribeIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAclsRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, acl_ids=None, acl_name=None, next_token=None,
                 max_results=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.acl_ids = acl_ids  # type: list[str]
        self.acl_name = acl_name  # type: str
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAclsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListAclsResponseBodyAcls(TeaModel):
    def __init__(self, acl_id=None, acl_name=None, address_ipversion=None, acl_status=None):
        self.acl_id = acl_id  # type: str
        self.acl_name = acl_name  # type: str
        self.address_ipversion = address_ipversion  # type: str
        self.acl_status = acl_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAclsResponseBodyAcls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        return self


class ListAclsResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, next_token=None, max_results=None, acls=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.acls = acls  # type: list[ListAclsResponseBodyAcls]

    def validate(self):
        if self.acls:
            for k in self.acls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAclsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Acls'] = []
        if self.acls is not None:
            for k in self.acls:
                result['Acls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.acls = []
        if m.get('Acls') is not None:
            for k in m.get('Acls'):
                temp_model = ListAclsResponseBodyAcls()
                self.acls.append(temp_model.from_map(k))
        return self


class ListAclsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAclsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAclsResponse, self).to_map()
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
            temp_model = ListAclsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAcceleratorRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, name=None, duration=None, pricing_cycle=None, spec=None,
                 auto_pay=None, auto_use_coupon=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.name = name  # type: str
        self.duration = duration  # type: int
        self.pricing_cycle = pricing_cycle  # type: str
        self.spec = spec  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.auto_use_coupon = auto_use_coupon  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        return self


class CreateAcceleratorResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None, accelerator_id=None):
        self.request_id = request_id  # type: str
        self.order_id = order_id  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class CreateAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAcceleratorResponse, self).to_map()
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
            temp_model = CreateAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeListenerRequest(TeaModel):
    def __init__(self, region_id=None, listener_id=None):
        self.region_id = region_id  # type: str
        self.listener_id = listener_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class DescribeListenerResponseBodyPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerResponseBodyPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class DescribeListenerResponseBodyBackendPorts(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: str
        self.to_port = to_port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerResponseBodyBackendPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class DescribeListenerResponseBodyCertificates(TeaModel):
    def __init__(self, type=None, id=None):
        self.type = type  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerResponseBodyCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeListenerResponseBodyRelatedAcls(TeaModel):
    def __init__(self, acl_id=None, status=None):
        self.acl_id = acl_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerResponseBodyRelatedAcls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeListenerResponseBody(TeaModel):
    def __init__(self, description=None, request_id=None, state=None, create_time=None, port_ranges=None,
                 backend_ports=None, certificates=None, protocol=None, listener_id=None, client_affinity=None, name=None,
                 related_acls=None, acl_type=None, accelerator_id=None, proxy_protocol=None):
        self.description = description  # type: str
        self.request_id = request_id  # type: str
        self.state = state  # type: str
        self.create_time = create_time  # type: str
        self.port_ranges = port_ranges  # type: list[DescribeListenerResponseBodyPortRanges]
        self.backend_ports = backend_ports  # type: list[DescribeListenerResponseBodyBackendPorts]
        self.certificates = certificates  # type: list[DescribeListenerResponseBodyCertificates]
        self.protocol = protocol  # type: str
        self.listener_id = listener_id  # type: str
        self.client_affinity = client_affinity  # type: str
        self.name = name  # type: str
        self.related_acls = related_acls  # type: list[DescribeListenerResponseBodyRelatedAcls]
        self.acl_type = acl_type  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.proxy_protocol = proxy_protocol  # type: bool

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.backend_ports:
            for k in self.backend_ports:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.related_acls:
            for k in self.related_acls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k in self.backend_ports:
                result['BackendPorts'].append(k.to_map() if k else None)
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.name is not None:
            result['Name'] = self.name
        result['RelatedAcls'] = []
        if self.related_acls is not None:
            for k in self.related_acls:
                result['RelatedAcls'].append(k.to_map() if k else None)
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = DescribeListenerResponseBodyPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k in m.get('BackendPorts'):
                temp_model = DescribeListenerResponseBodyBackendPorts()
                self.backend_ports.append(temp_model.from_map(k))
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = DescribeListenerResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.related_acls = []
        if m.get('RelatedAcls') is not None:
            for k in m.get('RelatedAcls'):
                temp_model = DescribeListenerResponseBodyRelatedAcls()
                self.related_acls.append(temp_model.from_map(k))
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        return self


class DescribeListenerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeListenerResponse, self).to_map()
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
            temp_model = DescribeListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpareIpsRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dry_run=None, accelerator_id=None, spare_ips=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.accelerator_id = accelerator_id  # type: str
        self.spare_ips = spare_ips  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSpareIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.spare_ips is not None:
            result['SpareIps'] = self.spare_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('SpareIps') is not None:
            self.spare_ips = m.get('SpareIps')
        return self


class DeleteSpareIpsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSpareIpsResponseBody, self).to_map()
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


class DeleteSpareIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSpareIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSpareIpsResponse, self).to_map()
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
            temp_model = DeleteSpareIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpSetsRequestIpSets(TeaModel):
    def __init__(self, bandwidth=None, ip_set_id=None):
        self.bandwidth = bandwidth  # type: int
        self.ip_set_id = ip_set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIpSetsRequestIpSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        return self


class UpdateIpSetsRequest(TeaModel):
    def __init__(self, region_id=None, ip_sets=None):
        self.region_id = region_id  # type: str
        self.ip_sets = ip_sets  # type: list[UpdateIpSetsRequestIpSets]

    def validate(self):
        if self.ip_sets:
            for k in self.ip_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateIpSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['IpSets'] = []
        if self.ip_sets is not None:
            for k in self.ip_sets:
                result['IpSets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k in m.get('IpSets'):
                temp_model = UpdateIpSetsRequestIpSets()
                self.ip_sets.append(temp_model.from_map(k))
        return self


class UpdateIpSetsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIpSetsResponseBody, self).to_map()
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


class UpdateIpSetsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateIpSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIpSetsResponse, self).to_map()
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
            temp_model = UpdateIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigEndpointProbeRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, endpoint_group_id=None, endpoint_type=None, endpoint=None,
                 probe_protocol=None, probe_port=None, enable=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.endpoint = endpoint  # type: str
        self.probe_protocol = probe_protocol  # type: str
        self.probe_port = probe_port  # type: str
        self.enable = enable  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigEndpointProbeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol
        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')
        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ConfigEndpointProbeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigEndpointProbeResponseBody, self).to_map()
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


class ConfigEndpointProbeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConfigEndpointProbeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigEndpointProbeResponse, self).to_map()
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
            temp_model = ConfigEndpointProbeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveEntriesFromAclRequestAclEntries(TeaModel):
    def __init__(self, entry=None):
        self.entry = entry  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveEntriesFromAclRequestAclEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class RemoveEntriesFromAclRequest(TeaModel):
    def __init__(self, region_id=None, acl_id=None, acl_entries=None, client_token=None, dry_run=None):
        self.region_id = region_id  # type: str
        self.acl_id = acl_id  # type: str
        self.acl_entries = acl_entries  # type: list[RemoveEntriesFromAclRequestAclEntries]
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RemoveEntriesFromAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = RemoveEntriesFromAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class RemoveEntriesFromAclResponseBody(TeaModel):
    def __init__(self, request_id=None, acl_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.acl_id = acl_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveEntriesFromAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        return self


class RemoveEntriesFromAclResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveEntriesFromAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveEntriesFromAclResponse, self).to_map()
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
            temp_model = RemoveEntriesFromAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBandwidthPackageRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None):
        self.region_id = region_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        return self


class DescribeBandwidthPackageResponseBody(TeaModel):
    def __init__(self, cbn_geographic_region_id_b=None, cbn_geographic_region_id_a=None, description=None,
                 request_id=None, create_time=None, name=None, bandwidth_type=None, type=None, accelerators=None, state=None,
                 charge_type=None, bandwidth=None, expired_time=None, bandwidth_package_id=None, region_id=None,
                 billing_type=None, ratio=None):
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b  # type: str
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a  # type: str
        self.description = description  # type: str
        self.request_id = request_id  # type: str
        self.create_time = create_time  # type: str
        self.name = name  # type: str
        self.bandwidth_type = bandwidth_type  # type: str
        self.type = type  # type: str
        self.accelerators = accelerators  # type: list[str]
        self.state = state  # type: str
        self.charge_type = charge_type  # type: str
        self.bandwidth = bandwidth  # type: int
        self.expired_time = expired_time  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.region_id = region_id  # type: str
        self.billing_type = billing_type  # type: str
        self.ratio = ratio  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBandwidthPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b
        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.type is not None:
            result['Type'] = self.type
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.state is not None:
            result['State'] = self.state
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')
        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        return self


class DescribeBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBandwidthPackageResponse, self).to_map()
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
            temp_model = DescribeBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBandwidthPackagesRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, state=None, type=None,
                 bandwidth_package_id=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.state = state  # type: str
        self.type = type  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBandwidthPackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        return self


class ListBandwidthPackagesResponseBodyBandwidthPackages(TeaModel):
    def __init__(self, type=None, bandwidth_type=None, state=None, create_time=None, charge_type=None,
                 region_id=None, cbn_geographic_region_id_a=None, bandwidth_package_id=None, bandwidth=None,
                 description=None, expired_time=None, accelerators=None, cbn_geographic_region_id_b=None, name=None,
                 billing_type=None, ratio=None):
        self.type = type  # type: str
        self.bandwidth_type = bandwidth_type  # type: str
        self.state = state  # type: str
        self.create_time = create_time  # type: str
        self.charge_type = charge_type  # type: str
        self.region_id = region_id  # type: str
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.description = description  # type: str
        self.expired_time = expired_time  # type: str
        self.accelerators = accelerators  # type: list[str]
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b  # type: str
        self.name = name  # type: str
        self.billing_type = billing_type  # type: str
        self.ratio = ratio  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBandwidthPackagesResponseBodyBandwidthPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b
        if self.name is not None:
            result['Name'] = self.name
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        return self


class ListBandwidthPackagesResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, bandwidth_packages=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.bandwidth_packages = bandwidth_packages  # type: list[ListBandwidthPackagesResponseBodyBandwidthPackages]

    def validate(self):
        if self.bandwidth_packages:
            for k in self.bandwidth_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBandwidthPackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['BandwidthPackages'] = []
        if self.bandwidth_packages is not None:
            for k in self.bandwidth_packages:
                result['BandwidthPackages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.bandwidth_packages = []
        if m.get('BandwidthPackages') is not None:
            for k in m.get('BandwidthPackages'):
                temp_model = ListBandwidthPackagesResponseBodyBandwidthPackages()
                self.bandwidth_packages.append(temp_model.from_map(k))
        return self


class ListBandwidthPackagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBandwidthPackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBandwidthPackagesResponse, self).to_map()
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
            temp_model = ListBandwidthPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEndpointGroupRequestEndpointConfigurations(TeaModel):
    def __init__(self, type=None, enable_client_ippreservation=None, weight=None, endpoint=None):
        self.type = type  # type: str
        self.enable_client_ippreservation = enable_client_ippreservation  # type: bool
        self.weight = weight  # type: int
        self.endpoint = endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupRequestEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        return self


class UpdateEndpointGroupRequestPortOverrides(TeaModel):
    def __init__(self, listener_port=None, endpoint_port=None):
        self.listener_port = listener_port  # type: int
        self.endpoint_port = endpoint_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupRequestPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        return self


class UpdateEndpointGroupRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, endpoint_group_id=None, name=None, description=None,
                 endpoint_group_region=None, traffic_percentage=None, health_check_interval_seconds=None, health_check_path=None,
                 health_check_port=None, health_check_protocol=None, threshold_count=None, endpoint_configurations=None,
                 endpoint_request_protocol=None, port_overrides=None, health_check_enabled=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.traffic_percentage = traffic_percentage  # type: int
        self.health_check_interval_seconds = health_check_interval_seconds  # type: int
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: int
        self.health_check_protocol = health_check_protocol  # type: str
        self.threshold_count = threshold_count  # type: int
        self.endpoint_configurations = endpoint_configurations  # type: list[UpdateEndpointGroupRequestEndpointConfigurations]
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.port_overrides = port_overrides  # type: list[UpdateEndpointGroupRequestPortOverrides]
        self.health_check_enabled = health_check_enabled  # type: bool

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = UpdateEndpointGroupRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = UpdateEndpointGroupRequestPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        return self


class UpdateEndpointGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupResponseBody, self).to_map()
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


class UpdateEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupResponse, self).to_map()
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
            temp_model = UpdateEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDdosToAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, ddos_id=None, ddos_region_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.ddos_id = ddos_id  # type: str
        self.ddos_region_id = ddos_region_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachDdosToAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachDdosToAcceleratorResponseBody(TeaModel):
    def __init__(self, ddos_id=None, request_id=None, ga_id=None):
        self.ddos_id = ddos_id  # type: str
        self.request_id = request_id  # type: str
        self.ga_id = ga_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachDdosToAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ga_id is not None:
            result['GaId'] = self.ga_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GaId') is not None:
            self.ga_id = m.get('GaId')
        return self


class AttachDdosToAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachDdosToAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachDdosToAcceleratorResponse, self).to_map()
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
            temp_model = AttachDdosToAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAclRequest(TeaModel):
    def __init__(self, region_id=None, acl_id=None):
        self.region_id = region_id  # type: str
        self.acl_id = acl_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        return self


class GetAclResponseBodyAclEntries(TeaModel):
    def __init__(self, entry=None, entry_description=None):
        self.entry = entry  # type: str
        self.entry_description = entry_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAclResponseBodyAclEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')
        return self


class GetAclResponseBodyRelatedListeners(TeaModel):
    def __init__(self, listener_id=None, acl_type=None, accelerator_id=None):
        self.listener_id = listener_id  # type: str
        self.acl_type = acl_type  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAclResponseBodyRelatedListeners, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class GetAclResponseBody(TeaModel):
    def __init__(self, request_id=None, acl_id=None, address_ipversion=None, acl_status=None, acl_entries=None,
                 related_listeners=None, acl_name=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.acl_id = acl_id  # type: str
        self.address_ipversion = address_ipversion  # type: str
        self.acl_status = acl_status  # type: str
        self.acl_entries = acl_entries  # type: list[GetAclResponseBodyAclEntries]
        self.related_listeners = related_listeners  # type: list[GetAclResponseBodyRelatedListeners]
        self.acl_name = acl_name  # type: str

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()
        if self.related_listeners:
            for k in self.related_listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k in self.related_listeners:
                result['RelatedListeners'].append(k.to_map() if k else None)
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = GetAclResponseBodyAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k in m.get('RelatedListeners'):
                temp_model = GetAclResponseBodyRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k))
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        return self


class GetAclResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAclResponse, self).to_map()
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
            temp_model = GetAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAclsWithListenerRequest(TeaModel):
    def __init__(self, region_id=None, acl_ids=None, listener_id=None, acl_type=None, client_token=None,
                 dry_run=None):
        self.region_id = region_id  # type: str
        self.acl_ids = acl_ids  # type: list[str]
        self.listener_id = listener_id  # type: str
        self.acl_type = acl_type  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAclsWithListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class AssociateAclsWithListenerResponseBody(TeaModel):
    def __init__(self, request_id=None, acl_ids=None, listener_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.acl_ids = acl_ids  # type: list[str]
        self.listener_id = listener_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAclsWithListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class AssociateAclsWithListenerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssociateAclsWithListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateAclsWithListenerResponse, self).to_map()
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
            temp_model = AssociateAclsWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListForwardingRulesRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, listener_id=None, accelerator_id=None,
                 forwarding_rule_id=None, next_token=None, max_results=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.listener_id = listener_id  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.forwarding_rule_id = forwarding_rule_id  # type: str
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListForwardingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleConditions(TeaModel):
    def __init__(self, rule_condition_type=None, path_config=None, host_config=None):
        self.rule_condition_type = rule_condition_type  # type: str
        self.path_config = path_config  # type: ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig
        self.host_config = host_config  # type: ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig

    def validate(self):
        if self.path_config:
            self.path_config.validate()
        if self.host_config:
            self.host_config.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')
        if m.get('PathConfig') is not None:
            temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('HostConfig') is not None:
            temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(self, endpoint_group_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(self, server_group_tuples=None):
        self.server_group_tuples = server_group_tuples  # type: list[ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples]

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleActions(TeaModel):
    def __init__(self, order=None, rule_action_type=None, forward_group_config=None):
        self.order = order  # type: int
        self.rule_action_type = rule_action_type  # type: str
        self.forward_group_config = forward_group_config  # type: ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('ForwardGroupConfig') is not None:
            temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        return self


class ListForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(self, priority=None, forwarding_rule_id=None, forwarding_rule_name=None,
                 forwarding_rule_status=None, rule_conditions=None, rule_actions=None, listener_id=None):
        self.priority = priority  # type: int
        self.forwarding_rule_id = forwarding_rule_id  # type: str
        self.forwarding_rule_name = forwarding_rule_name  # type: str
        self.forwarding_rule_status = forwarding_rule_status  # type: str
        self.rule_conditions = rule_conditions  # type: list[ListForwardingRulesResponseBodyForwardingRulesRuleConditions]
        self.rule_actions = rule_actions  # type: list[ListForwardingRulesResponseBodyForwardingRulesRuleActions]
        self.listener_id = listener_id  # type: str

    def validate(self):
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name
        if self.forwarding_rule_status is not None:
            result['ForwardingRuleStatus'] = self.forwarding_rule_status
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')
        if m.get('ForwardingRuleStatus') is not None:
            self.forwarding_rule_status = m.get('ForwardingRuleStatus')
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class ListForwardingRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, next_token=None, max_results=None, forwarding_rules=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.forwarding_rules = forwarding_rules  # type: list[ListForwardingRulesResponseBodyForwardingRules]

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = ListForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        return self


class ListForwardingRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListForwardingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponse, self).to_map()
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
            temp_model = ListForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBandwidthPackageRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth=None, duration=None, pricing_cycle=None, auto_pay=None,
                 client_token=None, type=None, bandwidth_type=None, auto_use_coupon=None, ratio=None, billing_type=None,
                 charge_type=None, cbn_geographic_region_id_a=None, cbn_geographic_region_id_b=None):
        self.region_id = region_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.duration = duration  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.client_token = client_token  # type: str
        self.type = type  # type: str
        self.bandwidth_type = bandwidth_type  # type: str
        self.auto_use_coupon = auto_use_coupon  # type: str
        self.ratio = ratio  # type: int
        self.billing_type = billing_type  # type: str
        self.charge_type = charge_type  # type: str
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a  # type: str
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.type is not None:
            result['Type'] = self.type
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a
        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')
        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')
        return self


class CreateBandwidthPackageResponseBody(TeaModel):
    def __init__(self, request_id=None, bandwidth_package_id=None, order_id=None):
        self.request_id = request_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBandwidthPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBandwidthPackageResponse, self).to_map()
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
            temp_model = CreateBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBandwidthackagesRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBandwidthackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListBandwidthackagesResponseBodyBandwidthPackages(TeaModel):
    def __init__(self, bandwidth_package_id=None, bandwidth=None, description=None, expired_time=None, state=None,
                 create_time=None, charge_type=None, accelerators=None, name=None, region_id=None):
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.description = description  # type: str
        self.expired_time = expired_time  # type: str
        self.state = state  # type: str
        self.create_time = create_time  # type: str
        self.charge_type = charge_type  # type: str
        self.accelerators = accelerators  # type: list[str]
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBandwidthackagesResponseBodyBandwidthPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBandwidthackagesResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, bandwidth_packages=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.bandwidth_packages = bandwidth_packages  # type: list[ListBandwidthackagesResponseBodyBandwidthPackages]

    def validate(self):
        if self.bandwidth_packages:
            for k in self.bandwidth_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBandwidthackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['BandwidthPackages'] = []
        if self.bandwidth_packages is not None:
            for k in self.bandwidth_packages:
                result['BandwidthPackages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.bandwidth_packages = []
        if m.get('BandwidthPackages') is not None:
            for k in m.get('BandwidthPackages'):
                temp_model = ListBandwidthackagesResponseBodyBandwidthPackages()
                self.bandwidth_packages.append(temp_model.from_map(k))
        return self


class ListBandwidthackagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBandwidthackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBandwidthackagesResponse, self).to_map()
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
            temp_model = ListBandwidthackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBandwidthPackageRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, client_token=None):
        self.region_id = region_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteBandwidthPackageResponseBody(TeaModel):
    def __init__(self, request_id=None, bandwidth_package_id=None):
        self.request_id = request_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBandwidthPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        return self


class DeleteBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBandwidthPackageResponse, self).to_map()
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
            temp_model = DeleteBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHealthStatusRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dry_run=None, accelerator_id=None, listener_id=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHealthStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class GetHealthStatusResponseBodyEndpointGroupsEndpoints(TeaModel):
    def __init__(self, endpoint_id=None, address=None, health_status=None, health_detail=None, port=None, type=None):
        self.endpoint_id = endpoint_id  # type: str
        self.address = address  # type: str
        self.health_status = health_status  # type: str
        self.health_detail = health_detail  # type: str
        self.port = port  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHealthStatusResponseBodyEndpointGroupsEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.address is not None:
            result['Address'] = self.address
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.health_detail is not None:
            result['HealthDetail'] = self.health_detail
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('HealthDetail') is not None:
            self.health_detail = m.get('HealthDetail')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetHealthStatusResponseBodyEndpointGroups(TeaModel):
    def __init__(self, endpoint_group_id=None, endpoint_group_type=None, health_status=None,
                 forwarding_rule_ids=None, endpoints=None):
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.health_status = health_status  # type: str
        self.forwarding_rule_ids = forwarding_rule_ids  # type: list[str]
        self.endpoints = endpoints  # type: list[GetHealthStatusResponseBodyEndpointGroupsEndpoints]

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHealthStatusResponseBodyEndpointGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = GetHealthStatusResponseBodyEndpointGroupsEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        return self


class GetHealthStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, listener_id=None, health_status=None, endpoint_groups=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.listener_id = listener_id  # type: str
        self.health_status = health_status  # type: str
        self.endpoint_groups = endpoint_groups  # type: list[GetHealthStatusResponseBodyEndpointGroups]

    def validate(self):
        if self.endpoint_groups:
            for k in self.endpoint_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHealthStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        result['EndpointGroups'] = []
        if self.endpoint_groups is not None:
            for k in self.endpoint_groups:
                result['EndpointGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        self.endpoint_groups = []
        if m.get('EndpointGroups') is not None:
            for k in m.get('EndpointGroups'):
                temp_model = GetHealthStatusResponseBodyEndpointGroups()
                self.endpoint_groups.append(temp_model.from_map(k))
        return self


class GetHealthStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHealthStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHealthStatusResponse, self).to_map()
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
            temp_model = GetHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAcceleratorRequest(TeaModel):
    def __init__(self, region_id=None, accelerator_id=None):
        self.region_id = region_id  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeAcceleratorResponseBodyBasicBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, bandwidth_type=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAcceleratorResponseBodyBasicBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeAcceleratorResponseBody(TeaModel):
    def __init__(self, ddos_id=None, dns_name=None, description=None, request_id=None, instance_charge_type=None,
                 create_time=None, cross_domain_bandwidth_package=None, second_dns_name=None, name=None,
                 basic_bandwidth_package=None, state=None, expired_time=None, cen_id=None, region_id=None, spec=None, accelerator_id=None):
        self.ddos_id = ddos_id  # type: str
        self.dns_name = dns_name  # type: str
        self.description = description  # type: str
        self.request_id = request_id  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.create_time = create_time  # type: long
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package  # type: DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage
        self.second_dns_name = second_dns_name  # type: str
        self.name = name  # type: str
        self.basic_bandwidth_package = basic_bandwidth_package  # type: DescribeAcceleratorResponseBodyBasicBandwidthPackage
        self.state = state  # type: str
        self.expired_time = expired_time  # type: long
        self.cen_id = cen_id  # type: str
        self.region_id = region_id  # type: str
        self.spec = spec  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()

    def to_map(self):
        _map = super(DescribeAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()
        if self.second_dns_name is not None:
            result['SecondDnsName'] = self.second_dns_name
        if self.name is not None:
            result['Name'] = self.name
        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()
        if self.state is not None:
            result['State'] = self.state
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m['CrossDomainBandwidthPackage'])
        if m.get('SecondDnsName') is not None:
            self.second_dns_name = m.get('SecondDnsName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BasicBandwidthPackage') is not None:
            temp_model = DescribeAcceleratorResponseBodyBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m['BasicBandwidthPackage'])
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class DescribeAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAcceleratorResponse, self).to_map()
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
            temp_model = DescribeAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachLogStoreFromEndpointGroupRequest(TeaModel):
    def __init__(self, region_id=None, accelerator_id=None, listener_id=None, endpoint_group_ids=None,
                 client_token=None):
        self.region_id = region_id  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachLogStoreFromEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DetachLogStoreFromEndpointGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachLogStoreFromEndpointGroupResponseBody, self).to_map()
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


class DetachLogStoreFromEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachLogStoreFromEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachLogStoreFromEndpointGroupResponse, self).to_map()
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
            temp_model = DetachLogStoreFromEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpSetsRequestAccelerateRegion(TeaModel):
    def __init__(self, accelerate_region_id=None, ip_version=None, bandwidth=None):
        self.accelerate_region_id = accelerate_region_id  # type: str
        self.ip_version = ip_version  # type: str
        self.bandwidth = bandwidth  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIpSetsRequestAccelerateRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class CreateIpSetsRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, accelerator_id=None, accelerate_region=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.accelerate_region = accelerate_region  # type: list[CreateIpSetsRequestAccelerateRegion]

    def validate(self):
        if self.accelerate_region:
            for k in self.accelerate_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateIpSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        result['AccelerateRegion'] = []
        if self.accelerate_region is not None:
            for k in self.accelerate_region:
                result['AccelerateRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        self.accelerate_region = []
        if m.get('AccelerateRegion') is not None:
            for k in m.get('AccelerateRegion'):
                temp_model = CreateIpSetsRequestAccelerateRegion()
                self.accelerate_region.append(temp_model.from_map(k))
        return self


class CreateIpSetsResponseBodyIpSets(TeaModel):
    def __init__(self, accelerate_region_id=None, bandwidth=None, ip_set_id=None, ip_list=None):
        self.accelerate_region_id = accelerate_region_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.ip_set_id = ip_set_id  # type: str
        self.ip_list = ip_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIpSetsResponseBodyIpSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class CreateIpSetsResponseBody(TeaModel):
    def __init__(self, request_id=None, ip_sets=None, accelerator_id=None):
        self.request_id = request_id  # type: str
        self.ip_sets = ip_sets  # type: list[CreateIpSetsResponseBodyIpSets]
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        if self.ip_sets:
            for k in self.ip_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateIpSetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['IpSets'] = []
        if self.ip_sets is not None:
            for k in self.ip_sets:
                result['IpSets'].append(k.to_map() if k else None)
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k in m.get('IpSets'):
                temp_model = CreateIpSetsResponseBodyIpSets()
                self.ip_sets.append(temp_model.from_map(k))
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class CreateIpSetsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIpSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIpSetsResponse, self).to_map()
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
            temp_model = CreateIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleConditions(TeaModel):
    def __init__(self, rule_condition_type=None, path_config=None, host_config=None):
        self.rule_condition_type = rule_condition_type  # type: str
        self.path_config = path_config  # type: CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig
        self.host_config = host_config  # type: CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig

    def validate(self):
        if self.path_config:
            self.path_config.validate()
        if self.host_config:
            self.host_config.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')
        if m.get('PathConfig') is not None:
            temp_model = CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('HostConfig') is not None:
            temp_model = CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        return self


class CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(self, endpoint_group_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(self, server_group_tuples=None):
        self.server_group_tuples = server_group_tuples  # type: list[CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples]

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class CreateForwardingRulesRequestForwardingRulesRuleActions(TeaModel):
    def __init__(self, order=None, rule_action_type=None, forward_group_config=None):
        self.order = order  # type: int
        self.rule_action_type = rule_action_type  # type: str
        self.forward_group_config = forward_group_config  # type: CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('ForwardGroupConfig') is not None:
            temp_model = CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        return self


class CreateForwardingRulesRequestForwardingRules(TeaModel):
    def __init__(self, priority=None, rule_conditions=None, rule_actions=None, forwarding_rule_name=None):
        self.priority = priority  # type: int
        self.rule_conditions = rule_conditions  # type: list[CreateForwardingRulesRequestForwardingRulesRuleConditions]
        self.rule_actions = rule_actions  # type: list[CreateForwardingRulesRequestForwardingRulesRuleActions]
        self.forwarding_rule_name = forwarding_rule_name  # type: str

    def validate(self):
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = CreateForwardingRulesRequestForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = CreateForwardingRulesRequestForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')
        return self


class CreateForwardingRulesRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, accelerator_id=None, listener_id=None,
                 forwarding_rules=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.forwarding_rules = forwarding_rules  # type: list[CreateForwardingRulesRequestForwardingRules]

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = CreateForwardingRulesRequestForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        return self


class CreateForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(self, forwarding_rule_id=None):
        self.forwarding_rule_id = forwarding_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateForwardingRulesResponseBodyForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        return self


class CreateForwardingRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, forwarding_rules=None):
        self.request_id = request_id  # type: str
        self.forwarding_rules = forwarding_rules  # type: list[CreateForwardingRulesResponseBodyForwardingRules]

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = CreateForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        return self


class CreateForwardingRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateForwardingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesResponse, self).to_map()
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
            temp_model = CreateForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableAccelerateAreasRequest(TeaModel):
    def __init__(self, region_id=None, accelerator_id=None):
        self.region_id = region_id  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableAccelerateAreasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class ListAvailableAccelerateAreasResponseBodyAreasRegionList(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableAccelerateAreasResponseBodyAreasRegionList, self).to_map()
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


class ListAvailableAccelerateAreasResponseBodyAreas(TeaModel):
    def __init__(self, local_name=None, area_id=None, region_list=None):
        self.local_name = local_name  # type: str
        self.area_id = area_id  # type: str
        self.region_list = region_list  # type: list[ListAvailableAccelerateAreasResponseBodyAreasRegionList]

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableAccelerateAreasResponseBodyAreas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = ListAvailableAccelerateAreasResponseBodyAreasRegionList()
                self.region_list.append(temp_model.from_map(k))
        return self


class ListAvailableAccelerateAreasResponseBody(TeaModel):
    def __init__(self, request_id=None, areas=None):
        self.request_id = request_id  # type: str
        self.areas = areas  # type: list[ListAvailableAccelerateAreasResponseBodyAreas]

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableAccelerateAreasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Areas'] = []
        if self.areas is not None:
            for k in self.areas:
                result['Areas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.areas = []
        if m.get('Areas') is not None:
            for k in m.get('Areas'):
                temp_model = ListAvailableAccelerateAreasResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        return self


class ListAvailableAccelerateAreasResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAvailableAccelerateAreasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAvailableAccelerateAreasResponse, self).to_map()
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
            temp_model = ListAvailableAccelerateAreasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAclRequest(TeaModel):
    def __init__(self, region_id=None, acl_id=None, client_token=None, dry_run=None):
        self.region_id = region_id  # type: str
        self.acl_id = acl_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class DeleteAclResponseBody(TeaModel):
    def __init__(self, request_id=None, acl_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.acl_id = acl_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        return self


class DeleteAclResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAclResponse, self).to_map()
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
            temp_model = DeleteAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEntriesToAclRequestAclEntries(TeaModel):
    def __init__(self, entry=None, entry_description=None):
        self.entry = entry  # type: str
        self.entry_description = entry_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEntriesToAclRequestAclEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')
        return self


class AddEntriesToAclRequest(TeaModel):
    def __init__(self, region_id=None, acl_id=None, acl_entries=None, client_token=None, dry_run=None):
        self.region_id = region_id  # type: str
        self.acl_id = acl_id  # type: str
        self.acl_entries = acl_entries  # type: list[AddEntriesToAclRequestAclEntries]
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddEntriesToAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = AddEntriesToAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class AddEntriesToAclResponseBody(TeaModel):
    def __init__(self, request_id=None, acl_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.acl_id = acl_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEntriesToAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        return self


class AddEntriesToAclResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddEntriesToAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddEntriesToAclResponse, self).to_map()
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
            temp_model = AddEntriesToAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSpareIpsRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dry_run=None, accelerator_id=None, spare_ips=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.accelerator_id = accelerator_id  # type: str
        self.spare_ips = spare_ips  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSpareIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.spare_ips is not None:
            result['SpareIps'] = self.spare_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('SpareIps') is not None:
            self.spare_ips = m.get('SpareIps')
        return self


class CreateSpareIpsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSpareIpsResponseBody, self).to_map()
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


class CreateSpareIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSpareIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSpareIpsResponse, self).to_map()
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
            temp_model = CreateSpareIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateAdditionalCertificatesFromListenerRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, accelerator_id=None, listener_id=None, domains=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.domains = domains  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateAdditionalCertificatesFromListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DissociateAdditionalCertificatesFromListenerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateAdditionalCertificatesFromListenerResponseBody, self).to_map()
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


class DissociateAdditionalCertificatesFromListenerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DissociateAdditionalCertificatesFromListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateAdditionalCertificatesFromListenerResponse, self).to_map()
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
            temp_model = DissociateAdditionalCertificatesFromListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEndpointGroupsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, accelerator_id=None, listener_id=None,
                 endpoint_group_type=None, access_log_switch=None, endpoint_group_id=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.access_log_switch = access_log_switch  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations(TeaModel):
    def __init__(self, type=None, enable_client_ippreservation=None, weight=None, probe_protocol=None,
                 endpoint=None, probe_port=None, endpoint_id=None):
        self.type = type  # type: str
        self.enable_client_ippreservation = enable_client_ippreservation  # type: bool
        self.weight = weight  # type: int
        self.probe_protocol = probe_protocol  # type: str
        self.endpoint = endpoint  # type: str
        self.probe_port = probe_port  # type: int
        self.endpoint_id = endpoint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        return self


class ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides(TeaModel):
    def __init__(self, listener_port=None, endpoint_port=None):
        self.listener_port = listener_port  # type: int
        self.endpoint_port = endpoint_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        return self


class ListEndpointGroupsResponseBodyEndpointGroups(TeaModel):
    def __init__(self, endpoint_group_id=None, endpoint_group_ip_list=None,
                 endpoint_group_unconfirmed_ip_list=None, state=None, health_check_path=None, endpoint_group_region=None,
                 health_check_interval_seconds=None, traffic_percentage=None, health_check_protocol=None, threshold_count=None, listener_id=None,
                 accelerator_id=None, endpoint_configurations=None, port_overrides=None, forwarding_rule_ids=None,
                 endpoint_group_type=None, endpoint_request_protocol=None, description=None, name=None, health_check_port=None,
                 health_check_enabled=None):
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_ip_list = endpoint_group_ip_list  # type: list[str]
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list  # type: list[str]
        self.state = state  # type: str
        self.health_check_path = health_check_path  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.health_check_interval_seconds = health_check_interval_seconds  # type: int
        self.traffic_percentage = traffic_percentage  # type: int
        self.health_check_protocol = health_check_protocol  # type: str
        self.threshold_count = threshold_count  # type: int
        self.listener_id = listener_id  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.endpoint_configurations = endpoint_configurations  # type: list[ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations]
        self.port_overrides = port_overrides  # type: list[ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides]
        self.forwarding_rule_ids = forwarding_rule_ids  # type: list[str]
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.health_check_port = health_check_port  # type: int
        self.health_check_enabled = health_check_enabled  # type: bool

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEndpointGroupsResponseBodyEndpointGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list
        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list
        if self.state is not None:
            result['State'] = self.state
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')
        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        return self


class ListEndpointGroupsResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, endpoint_groups=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.endpoint_groups = endpoint_groups  # type: list[ListEndpointGroupsResponseBodyEndpointGroups]

    def validate(self):
        if self.endpoint_groups:
            for k in self.endpoint_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEndpointGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['EndpointGroups'] = []
        if self.endpoint_groups is not None:
            for k in self.endpoint_groups:
                result['EndpointGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.endpoint_groups = []
        if m.get('EndpointGroups') is not None:
            for k in m.get('EndpointGroups'):
                temp_model = ListEndpointGroupsResponseBodyEndpointGroups()
                self.endpoint_groups.append(temp_model.from_map(k))
        return self


class ListEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEndpointGroupsResponse, self).to_map()
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
            temp_model = ListEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBusiRegionsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBusiRegionsRequest, self).to_map()
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


class ListBusiRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBusiRegionsResponseBodyRegions, self).to_map()
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


class ListBusiRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id  # type: str
        self.regions = regions  # type: list[ListBusiRegionsResponseBodyRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBusiRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListBusiRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class ListBusiRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBusiRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBusiRegionsResponse, self).to_map()
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
            temp_model = ListBusiRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceBandwidthPackageRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, target_bandwidth_package_id=None):
        self.region_id = region_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.target_bandwidth_package_id = target_bandwidth_package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplaceBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.target_bandwidth_package_id is not None:
            result['TargetBandwidthPackageId'] = self.target_bandwidth_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('TargetBandwidthPackageId') is not None:
            self.target_bandwidth_package_id = m.get('TargetBandwidthPackageId')
        return self


class ReplaceBandwidthPackageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplaceBandwidthPackageResponseBody, self).to_map()
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


class ReplaceBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReplaceBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReplaceBandwidthPackageResponse, self).to_map()
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
            temp_model = ReplaceBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEndpointGroupAttributeRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, endpoint_group_id=None, name=None, description=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateEndpointGroupAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupAttributeResponseBody, self).to_map()
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


class UpdateEndpointGroupAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEndpointGroupAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupAttributeResponse, self).to_map()
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
            temp_model = UpdateEndpointGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleConditions(TeaModel):
    def __init__(self, rule_condition_type=None, path_config=None, host_config=None):
        self.rule_condition_type = rule_condition_type  # type: str
        self.path_config = path_config  # type: UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig
        self.host_config = host_config  # type: UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig

    def validate(self):
        if self.path_config:
            self.path_config.validate()
        if self.host_config:
            self.host_config.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')
        if m.get('PathConfig') is not None:
            temp_model = UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('HostConfig') is not None:
            temp_model = UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(self, endpoint_group_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(self, server_group_tuples=None):
        self.server_group_tuples = server_group_tuples  # type: list[UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples]

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleActions(TeaModel):
    def __init__(self, order=None, rule_action_type=None, forward_group_config=None):
        self.order = order  # type: int
        self.rule_action_type = rule_action_type  # type: str
        self.forward_group_config = forward_group_config  # type: UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('ForwardGroupConfig') is not None:
            temp_model = UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        return self


class UpdateForwardingRulesRequestForwardingRules(TeaModel):
    def __init__(self, priority=None, rule_conditions=None, rule_actions=None, forwarding_rule_id=None,
                 forwarding_rule_name=None):
        self.priority = priority  # type: int
        self.rule_conditions = rule_conditions  # type: list[UpdateForwardingRulesRequestForwardingRulesRuleConditions]
        self.rule_actions = rule_actions  # type: list[UpdateForwardingRulesRequestForwardingRulesRuleActions]
        self.forwarding_rule_id = forwarding_rule_id  # type: str
        self.forwarding_rule_name = forwarding_rule_name  # type: str

    def validate(self):
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = UpdateForwardingRulesRequestForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = UpdateForwardingRulesRequestForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')
        return self


class UpdateForwardingRulesRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, accelerator_id=None, listener_id=None,
                 forwarding_rules=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.forwarding_rules = forwarding_rules  # type: list[UpdateForwardingRulesRequestForwardingRules]

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = UpdateForwardingRulesRequestForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        return self


class UpdateForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(self, forwarding_rule_id=None):
        self.forwarding_rule_id = forwarding_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateForwardingRulesResponseBodyForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        return self


class UpdateForwardingRulesResponseBody(TeaModel):
    def __init__(self, forwarding_rules=None, request_id=None):
        self.forwarding_rules = forwarding_rules  # type: list[UpdateForwardingRulesResponseBodyForwardingRules]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = UpdateForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateForwardingRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateForwardingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesResponse, self).to_map()
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
            temp_model = UpdateForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, accelerator_id=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class ListListenersResponseBodyListenersCertificates(TeaModel):
    def __init__(self, type=None, id=None):
        self.type = type  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersResponseBodyListenersCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListListenersResponseBodyListenersBackendPorts(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: str
        self.to_port = to_port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersResponseBodyListenersBackendPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListListenersResponseBodyListenersPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersResponseBodyListenersPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListListenersResponseBodyListeners(TeaModel):
    def __init__(self, certificates=None, backend_ports=None, listener_id=None, description=None, state=None,
                 client_affinity=None, protocol=None, create_time=None, port_ranges=None, name=None, proxy_protocol=None,
                 accelerator_id=None):
        self.certificates = certificates  # type: list[ListListenersResponseBodyListenersCertificates]
        self.backend_ports = backend_ports  # type: list[ListListenersResponseBodyListenersBackendPorts]
        self.listener_id = listener_id  # type: str
        self.description = description  # type: str
        self.state = state  # type: str
        self.client_affinity = client_affinity  # type: str
        self.protocol = protocol  # type: str
        self.create_time = create_time  # type: long
        self.port_ranges = port_ranges  # type: list[ListListenersResponseBodyListenersPortRanges]
        self.name = name  # type: str
        self.proxy_protocol = proxy_protocol  # type: bool
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.backend_ports:
            for k in self.backend_ports:
                if k:
                    k.validate()
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenersResponseBodyListeners, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k in self.backend_ports:
                result['BackendPorts'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.description is not None:
            result['Description'] = self.description
        if self.state is not None:
            result['State'] = self.state
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = ListListenersResponseBodyListenersCertificates()
                self.certificates.append(temp_model.from_map(k))
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k in m.get('BackendPorts'):
                temp_model = ListListenersResponseBodyListenersBackendPorts()
                self.backend_ports.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListListenersResponseBodyListenersPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class ListListenersResponseBody(TeaModel):
    def __init__(self, total_count=None, listeners=None, page_size=None, request_id=None, page_number=None):
        self.total_count = total_count  # type: int
        self.listeners = listeners  # type: list[ListListenersResponseBodyListeners]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListListenersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListListenersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListListenersResponse, self).to_map()
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
            temp_model = ListListenersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointGroupRequest(TeaModel):
    def __init__(self, region_id=None, endpoint_group_id=None):
        self.region_id = region_id  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class DescribeEndpointGroupResponseBodyEndpointConfigurations(TeaModel):
    def __init__(self, type=None, enable_client_ippreservation=None, weight=None, probe_protocol=None,
                 endpoint=None, probe_port=None):
        self.type = type  # type: str
        self.enable_client_ippreservation = enable_client_ippreservation  # type: bool
        self.weight = weight  # type: int
        self.probe_protocol = probe_protocol  # type: str
        self.endpoint = endpoint  # type: str
        self.probe_port = probe_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndpointGroupResponseBodyEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')
        return self


class DescribeEndpointGroupResponseBodyPortOverrides(TeaModel):
    def __init__(self, listener_port=None, endpoint_port=None):
        self.listener_port = listener_port  # type: int
        self.endpoint_port = endpoint_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndpointGroupResponseBodyPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        return self


class DescribeEndpointGroupResponseBody(TeaModel):
    def __init__(self, health_check_interval_seconds=None, traffic_percentage=None, endpoint_group_id=None,
                 description=None, endpoint_group_ip_list=None, endpoint_group_unconfirmed_ip_list=None, request_id=None,
                 health_check_path=None, threshold_count=None, name=None, endpoint_group_region=None, total_count=None, state=None,
                 health_check_protocol=None, health_check_port=None, endpoint_configurations=None, port_overrides=None,
                 endpoint_request_protocol=None, endpoint_group_type=None, forwarding_rule_ids=None, accelerator_id=None, listener_id=None,
                 sls_region=None, sls_project_name=None, sls_log_store_name=None, access_log_switch=None,
                 enable_access_log=None, health_check_enabled=None):
        self.health_check_interval_seconds = health_check_interval_seconds  # type: int
        self.traffic_percentage = traffic_percentage  # type: int
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.description = description  # type: str
        self.endpoint_group_ip_list = endpoint_group_ip_list  # type: list[str]
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list  # type: list[str]
        self.request_id = request_id  # type: str
        self.health_check_path = health_check_path  # type: str
        self.threshold_count = threshold_count  # type: int
        self.name = name  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.total_count = total_count  # type: int
        self.state = state  # type: str
        self.health_check_protocol = health_check_protocol  # type: str
        self.health_check_port = health_check_port  # type: int
        self.endpoint_configurations = endpoint_configurations  # type: list[DescribeEndpointGroupResponseBodyEndpointConfigurations]
        self.port_overrides = port_overrides  # type: list[DescribeEndpointGroupResponseBodyPortOverrides]
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.forwarding_rule_ids = forwarding_rule_ids  # type: list[str]
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.sls_region = sls_region  # type: str
        self.sls_project_name = sls_project_name  # type: str
        self.sls_log_store_name = sls_log_store_name  # type: str
        self.access_log_switch = access_log_switch  # type: str
        self.enable_access_log = enable_access_log  # type: bool
        self.health_check_enabled = health_check_enabled  # type: bool

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEndpointGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list
        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.name is not None:
            result['Name'] = self.name
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.state is not None:
            result['State'] = self.state
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.sls_region is not None:
            result['SlsRegion'] = self.sls_region
        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name
        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name
        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch
        if self.enable_access_log is not None:
            result['EnableAccessLog'] = self.enable_access_log
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')
        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = DescribeEndpointGroupResponseBodyEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = DescribeEndpointGroupResponseBodyPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('SlsRegion') is not None:
            self.sls_region = m.get('SlsRegion')
        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')
        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')
        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')
        if m.get('EnableAccessLog') is not None:
            self.enable_access_log = m.get('EnableAccessLog')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        return self


class DescribeEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEndpointGroupResponse, self).to_map()
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
            temp_model = DescribeEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteListenerRequest(TeaModel):
    def __init__(self, client_token=None, accelerator_id=None, listener_id=None):
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class DeleteListenerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteListenerResponseBody, self).to_map()
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


class DeleteListenerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteListenerResponse, self).to_map()
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
            temp_model = DeleteListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAdditionalCertificatesWithListenerRequestCertificates(TeaModel):
    def __init__(self, id=None, domain=None):
        self.id = id  # type: str
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerRequestCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class AssociateAdditionalCertificatesWithListenerRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, accelerator_id=None, listener_id=None, certificates=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.certificates = certificates  # type: list[AssociateAdditionalCertificatesWithListenerRequestCertificates]

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = AssociateAdditionalCertificatesWithListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        return self


class AssociateAdditionalCertificatesWithListenerResponseBody(TeaModel):
    def __init__(self, request_id=None, listener_id=None):
        self.request_id = request_id  # type: str
        self.listener_id = listener_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class AssociateAdditionalCertificatesWithListenerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssociateAdditionalCertificatesWithListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerResponse, self).to_map()
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
            temp_model = AssociateAdditionalCertificatesWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachLogStoreToEndpointGroupRequest(TeaModel):
    def __init__(self, region_id=None, sls_project_name=None, sls_log_store_name=None, accelerator_id=None,
                 listener_id=None, sls_region_id=None, endpoint_group_ids=None, client_token=None):
        self.region_id = region_id  # type: str
        self.sls_project_name = sls_project_name  # type: str
        self.sls_log_store_name = sls_log_store_name  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.sls_region_id = sls_region_id  # type: str
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachLogStoreToEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name
        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')
        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AttachLogStoreToEndpointGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachLogStoreToEndpointGroupResponseBody, self).to_map()
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


class AttachLogStoreToEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachLogStoreToEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachLogStoreToEndpointGroupResponse, self).to_map()
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
            temp_model = AttachLogStoreToEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCrossBorderPackageComplianceStatusRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dry_run=None, compliance_status=None, instance_id=None,
                 description=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.compliance_status = compliance_status  # type: str
        self.instance_id = instance_id  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCrossBorderPackageComplianceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.compliance_status is not None:
            result['ComplianceStatus'] = self.compliance_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ComplianceStatus') is not None:
            self.compliance_status = m.get('ComplianceStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateCrossBorderPackageComplianceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCrossBorderPackageComplianceStatusResponseBody, self).to_map()
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


class UpdateCrossBorderPackageComplianceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateCrossBorderPackageComplianceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCrossBorderPackageComplianceStatusResponse, self).to_map()
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
            temp_model = UpdateCrossBorderPackageComplianceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBandwidthPackageRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, name=None, description=None, bandwidth=None,
                 bandwidth_type=None, auto_pay=None, auto_use_coupon=None):
        self.region_id = region_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.auto_use_coupon = auto_use_coupon  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        return self


class UpdateBandwidthPackageResponseBody(TeaModel):
    def __init__(self, bandwidth_package=None, description=None, request_id=None, name=None):
        self.bandwidth_package = bandwidth_package  # type: str
        self.description = description  # type: str
        self.request_id = request_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBandwidthPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package is not None:
            result['BandwidthPackage'] = self.bandwidth_package
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthPackage') is not None:
            self.bandwidth_package = m.get('BandwidthPackage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBandwidthPackageResponse, self).to_map()
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
            temp_model = UpdateBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAcceleratorRequest(TeaModel):
    def __init__(self, region_id=None, accelerator_id=None):
        self.region_id = region_id  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class DeleteAcceleratorResponseBody(TeaModel):
    def __init__(self, request_id=None, accelerator_id=None):
        self.request_id = request_id  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class DeleteAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAcceleratorResponse, self).to_map()
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
            temp_model = DeleteAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEndpointGroupRequestEndpointConfigurations(TeaModel):
    def __init__(self, type=None, enable_client_ippreservation=None, weight=None, endpoint=None):
        self.type = type  # type: str
        self.enable_client_ippreservation = enable_client_ippreservation  # type: bool
        self.weight = weight  # type: int
        self.endpoint = endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupRequestEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        return self


class CreateEndpointGroupRequestPortOverrides(TeaModel):
    def __init__(self, listener_port=None, endpoint_port=None):
        self.listener_port = listener_port  # type: int
        self.endpoint_port = endpoint_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupRequestPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        return self


class CreateEndpointGroupRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, accelerator_id=None, name=None, description=None,
                 endpoint_group_region=None, listener_id=None, traffic_percentage=None, health_check_interval_seconds=None,
                 health_check_path=None, health_check_port=None, health_check_protocol=None, threshold_count=None,
                 endpoint_configurations=None, endpoint_request_protocol=None, endpoint_group_type=None, port_overrides=None,
                 health_check_enabled=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.listener_id = listener_id  # type: str
        self.traffic_percentage = traffic_percentage  # type: int
        self.health_check_interval_seconds = health_check_interval_seconds  # type: int
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: int
        self.health_check_protocol = health_check_protocol  # type: str
        self.threshold_count = threshold_count  # type: int
        self.endpoint_configurations = endpoint_configurations  # type: list[CreateEndpointGroupRequestEndpointConfigurations]
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.port_overrides = port_overrides  # type: list[CreateEndpointGroupRequestPortOverrides]
        self.health_check_enabled = health_check_enabled  # type: bool

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateEndpointGroupRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = CreateEndpointGroupRequestPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        return self


class CreateEndpointGroupResponseBody(TeaModel):
    def __init__(self, endpoint_group_id=None, request_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEndpointGroupResponse, self).to_map()
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
            temp_model = CreateEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEndpointGroupRequest(TeaModel):
    def __init__(self, client_token=None, accelerator_id=None, endpoint_group_id=None):
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class DeleteEndpointGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEndpointGroupResponseBody, self).to_map()
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


class DeleteEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEndpointGroupResponse, self).to_map()
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
            temp_model = DeleteEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpSetsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, accelerator_id=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIpSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class ListIpSetsResponseBodyIpSets(TeaModel):
    def __init__(self, accelerate_region_id=None, ip_version=None, bandwidth=None, state=None, ip_set_id=None,
                 ip_address_list=None):
        self.accelerate_region_id = accelerate_region_id  # type: str
        self.ip_version = ip_version  # type: str
        self.bandwidth = bandwidth  # type: int
        self.state = state  # type: str
        self.ip_set_id = ip_set_id  # type: str
        self.ip_address_list = ip_address_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIpSetsResponseBodyIpSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.state is not None:
            result['State'] = self.state
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.ip_address_list is not None:
            result['IpAddressList'] = self.ip_address_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('IpAddressList') is not None:
            self.ip_address_list = m.get('IpAddressList')
        return self


class ListIpSetsResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, ip_sets=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.ip_sets = ip_sets  # type: list[ListIpSetsResponseBodyIpSets]

    def validate(self):
        if self.ip_sets:
            for k in self.ip_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIpSetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['IpSets'] = []
        if self.ip_sets is not None:
            for k in self.ip_sets:
                result['IpSets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k in m.get('IpSets'):
                temp_model = ListIpSetsResponseBodyIpSets()
                self.ip_sets.append(temp_model.from_map(k))
        return self


class ListIpSetsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIpSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIpSetsResponse, self).to_map()
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
            temp_model = ListIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAcceleratorConfirmRequest(TeaModel):
    def __init__(self, region_id=None, accelerator_id=None):
        self.region_id = region_id  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAcceleratorConfirmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class UpdateAcceleratorConfirmResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAcceleratorConfirmResponseBody, self).to_map()
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


class UpdateAcceleratorConfirmResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAcceleratorConfirmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAcceleratorConfirmResponse, self).to_map()
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
            temp_model = UpdateAcceleratorConfirmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BandwidthPackageRemoveAcceleratorRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, accelerator_id=None):
        self.region_id = region_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BandwidthPackageRemoveAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class BandwidthPackageRemoveAcceleratorResponseBody(TeaModel):
    def __init__(self, request_id=None, accelerators=None, bandwidth_package_id=None):
        self.request_id = request_id  # type: str
        self.accelerators = accelerators  # type: list[str]
        self.bandwidth_package_id = bandwidth_package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BandwidthPackageRemoveAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        return self


class BandwidthPackageRemoveAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BandwidthPackageRemoveAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BandwidthPackageRemoveAcceleratorResponse, self).to_map()
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
            temp_model = BandwidthPackageRemoveAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteForwardingRulesRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, forwarding_rule_ids=None, accelerator_id=None,
                 listener_id=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.forwarding_rule_ids = forwarding_rule_ids  # type: list[str]
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteForwardingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class DeleteForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(self, forwarding_rule_id=None):
        self.forwarding_rule_id = forwarding_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteForwardingRulesResponseBodyForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        return self


class DeleteForwardingRulesResponseBody(TeaModel):
    def __init__(self, forwarding_rules=None, request_id=None):
        self.forwarding_rules = forwarding_rules  # type: list[DeleteForwardingRulesResponseBodyForwardingRules]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteForwardingRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = DeleteForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteForwardingRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteForwardingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteForwardingRulesResponse, self).to_map()
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
            temp_model = DeleteForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateAclsFromListenerRequest(TeaModel):
    def __init__(self, region_id=None, acl_ids=None, listener_id=None, client_token=None, dry_run=None):
        self.region_id = region_id  # type: str
        self.acl_ids = acl_ids  # type: list[str]
        self.listener_id = listener_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateAclsFromListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class DissociateAclsFromListenerResponseBody(TeaModel):
    def __init__(self, request_id=None, acl_ids=None, listener_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.acl_ids = acl_ids  # type: list[str]
        self.listener_id = listener_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateAclsFromListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class DissociateAclsFromListenerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DissociateAclsFromListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateAclsFromListenerResponse, self).to_map()
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
            temp_model = DissociateAclsFromListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCrossBorderPackageForComplianceRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dry_run=None, resource_uid=None, is_binded=None,
                 next_token=None, max_result=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.resource_uid = resource_uid  # type: long
        self.is_binded = is_binded  # type: bool
        self.next_token = next_token  # type: str
        self.max_result = max_result  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCrossBorderPackageForComplianceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid
        if self.is_binded is not None:
            result['IsBinded'] = self.is_binded
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')
        if m.get('IsBinded') is not None:
            self.is_binded = m.get('IsBinded')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        return self


class ListCrossBorderPackageForComplianceResponseBodyBandwidthPackages(TeaModel):
    def __init__(self, is_binded=None, create_time=None, cbn_geographic_region_id_a=None,
                 bandwidth_package_id=None, bandwidth=None, expired_time=None, cbn_geographic_region_id_b=None, ali_uid=None,
                 bind_time=None):
        self.is_binded = is_binded  # type: bool
        self.create_time = create_time  # type: long
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.expired_time = expired_time  # type: long
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b  # type: str
        self.ali_uid = ali_uid  # type: long
        self.bind_time = bind_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCrossBorderPackageForComplianceResponseBodyBandwidthPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_binded is not None:
            result['IsBinded'] = self.is_binded
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bind_time is not None:
            result['BindTime'] = self.bind_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsBinded') is not None:
            self.is_binded = m.get('IsBinded')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')
        return self


class ListCrossBorderPackageForComplianceResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, next_token=None, max_results=None,
                 bandwidth_packages=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.bandwidth_packages = bandwidth_packages  # type: list[ListCrossBorderPackageForComplianceResponseBodyBandwidthPackages]

    def validate(self):
        if self.bandwidth_packages:
            for k in self.bandwidth_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCrossBorderPackageForComplianceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['BandwidthPackages'] = []
        if self.bandwidth_packages is not None:
            for k in self.bandwidth_packages:
                result['BandwidthPackages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.bandwidth_packages = []
        if m.get('BandwidthPackages') is not None:
            for k in m.get('BandwidthPackages'):
                temp_model = ListCrossBorderPackageForComplianceResponseBodyBandwidthPackages()
                self.bandwidth_packages.append(temp_model.from_map(k))
        return self


class ListCrossBorderPackageForComplianceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCrossBorderPackageForComplianceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCrossBorderPackageForComplianceResponse, self).to_map()
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
            temp_model = ListCrossBorderPackageForComplianceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccelerateAreasRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccelerateAreasRequest, self).to_map()
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


class ListAccelerateAreasResponseBodyAreasRegionList(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccelerateAreasResponseBodyAreasRegionList, self).to_map()
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


class ListAccelerateAreasResponseBodyAreas(TeaModel):
    def __init__(self, local_name=None, area_id=None, region_list=None):
        self.local_name = local_name  # type: str
        self.area_id = area_id  # type: str
        self.region_list = region_list  # type: list[ListAccelerateAreasResponseBodyAreasRegionList]

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccelerateAreasResponseBodyAreas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = ListAccelerateAreasResponseBodyAreasRegionList()
                self.region_list.append(temp_model.from_map(k))
        return self


class ListAccelerateAreasResponseBody(TeaModel):
    def __init__(self, request_id=None, areas=None):
        self.request_id = request_id  # type: str
        self.areas = areas  # type: list[ListAccelerateAreasResponseBodyAreas]

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccelerateAreasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Areas'] = []
        if self.areas is not None:
            for k in self.areas:
                result['Areas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.areas = []
        if m.get('Areas') is not None:
            for k in m.get('Areas'):
                temp_model = ListAccelerateAreasResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        return self


class ListAccelerateAreasResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAccelerateAreasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccelerateAreasResponse, self).to_map()
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
            temp_model = ListAccelerateAreasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenerCertificatesRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, accelerator_id=None, listener_id=None, next_token=None,
                 max_results=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenerCertificatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListListenerCertificatesResponseBodyCertificates(TeaModel):
    def __init__(self, certificate_id=None, type=None, is_default=None, domain=None):
        self.certificate_id = certificate_id  # type: str
        self.type = type  # type: str
        self.is_default = is_default  # type: bool
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenerCertificatesResponseBodyCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.type is not None:
            result['Type'] = self.type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class ListListenerCertificatesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, next_token=None, max_results=None, certificates=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.certificates = certificates  # type: list[ListListenerCertificatesResponseBodyCertificates]

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenerCertificatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = ListListenerCertificatesResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        return self


class ListListenerCertificatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListListenerCertificatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListListenerCertificatesResponse, self).to_map()
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
            temp_model = ListListenerCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpSetRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, ip_set_id=None, bandwidth=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.ip_set_id = ip_set_id  # type: str
        self.bandwidth = bandwidth  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class UpdateIpSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIpSetResponseBody, self).to_map()
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


class UpdateIpSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIpSetResponse, self).to_map()
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
            temp_model = UpdateIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAclRequestAclEntries(TeaModel):
    def __init__(self, entry=None, entry_description=None):
        self.entry = entry  # type: str
        self.entry_description = entry_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAclRequestAclEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')
        return self


class CreateAclRequest(TeaModel):
    def __init__(self, region_id=None, acl_name=None, address_ipversion=None, acl_entries=None, client_token=None,
                 dry_run=None):
        self.region_id = region_id  # type: str
        self.acl_name = acl_name  # type: str
        self.address_ipversion = address_ipversion  # type: str
        self.acl_entries = acl_entries  # type: list[CreateAclRequestAclEntries]
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = CreateAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class CreateAclResponseBody(TeaModel):
    def __init__(self, request_id=None, acl_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.acl_id = acl_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        return self


class CreateAclResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAclResponse, self).to_map()
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
            temp_model = CreateAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
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


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
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


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id  # type: str
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
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


class UpdateListenerRequestPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerRequestPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateListenerRequestCertificates(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerRequestCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateListenerRequestBackendPorts(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerRequestBackendPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateListenerRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, name=None, description=None, client_affinity=None,
                 protocol=None, listener_id=None, proxy_protocol=None, port_ranges=None, certificates=None,
                 backend_ports=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.client_affinity = client_affinity  # type: str
        self.protocol = protocol  # type: str
        self.listener_id = listener_id  # type: str
        self.proxy_protocol = proxy_protocol  # type: str
        self.port_ranges = port_ranges  # type: list[UpdateListenerRequestPortRanges]
        self.certificates = certificates  # type: list[UpdateListenerRequestCertificates]
        self.backend_ports = backend_ports  # type: list[UpdateListenerRequestBackendPorts]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.backend_ports:
            for k in self.backend_ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k in self.backend_ports:
                result['BackendPorts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = UpdateListenerRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = UpdateListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k in m.get('BackendPorts'):
                temp_model = UpdateListenerRequestBackendPorts()
                self.backend_ports.append(temp_model.from_map(k))
        return self


class UpdateListenerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerResponseBody, self).to_map()
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


class UpdateListenerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateListenerResponse, self).to_map()
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
            temp_model = UpdateListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableBusiRegionsRequest(TeaModel):
    def __init__(self, region_id=None, accelerator_id=None):
        self.region_id = region_id  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableBusiRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class ListAvailableBusiRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableBusiRegionsResponseBodyRegions, self).to_map()
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


class ListAvailableBusiRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id  # type: str
        self.regions = regions  # type: list[ListAvailableBusiRegionsResponseBodyRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableBusiRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListAvailableBusiRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class ListAvailableBusiRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAvailableBusiRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAvailableBusiRegionsResponse, self).to_map()
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
            temp_model = ListAvailableBusiRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAcceleratorRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, name=None, description=None, accelerator_id=None,
                 spec=None, auto_pay=None, auto_use_coupon=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.spec = spec  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.auto_use_coupon = auto_use_coupon  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        return self


class UpdateAcceleratorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAcceleratorResponseBody, self).to_map()
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


class UpdateAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAcceleratorResponse, self).to_map()
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
            temp_model = UpdateAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEndpointGroupsRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dry_run=None, endpoint_group_ids=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        return self


class DeleteEndpointGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEndpointGroupsResponseBody, self).to_map()
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


class DeleteEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEndpointGroupsResponse, self).to_map()
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
            temp_model = DeleteEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpSetRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, accelerator_id=None, ip_set_id=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.ip_set_id = ip_set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        return self


class DeleteIpSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpSetResponseBody, self).to_map()
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


class DeleteIpSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIpSetResponse, self).to_map()
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
            temp_model = DeleteIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(self, type=None, weight=None, endpoint=None):
        self.type = type  # type: str
        self.weight = weight  # type: long
        self.endpoint = endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        return self


class UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides(TeaModel):
    def __init__(self, listener_port=None, endpoint_port=None):
        self.listener_port = listener_port  # type: long
        self.endpoint_port = endpoint_port  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        return self


class UpdateEndpointGroupsRequestEndpointGroupConfigurations(TeaModel):
    def __init__(self, endpoint_group_name=None, endpoint_group_description=None, traffic_percentage=None,
                 health_check_enabled=None, health_check_interval_seconds=None, health_check_path=None, health_check_port=None,
                 health_check_protocol=None, threshold_count=None, endpoint_configurations=None, endpoint_request_protocol=None,
                 port_overrides=None, enable_client_ippreservation_toa=None, enable_client_ippreservation_proxy_protocol=None,
                 endpoint_group_id=None):
        self.endpoint_group_name = endpoint_group_name  # type: str
        self.endpoint_group_description = endpoint_group_description  # type: str
        self.traffic_percentage = traffic_percentage  # type: long
        self.health_check_enabled = health_check_enabled  # type: bool
        self.health_check_interval_seconds = health_check_interval_seconds  # type: long
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: long
        self.health_check_protocol = health_check_protocol  # type: str
        self.threshold_count = threshold_count  # type: long
        self.endpoint_configurations = endpoint_configurations  # type: list[UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations]
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.port_overrides = port_overrides  # type: list[UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides]
        self.enable_client_ippreservation_toa = enable_client_ippreservation_toa  # type: bool
        self.enable_client_ippreservation_proxy_protocol = enable_client_ippreservation_proxy_protocol  # type: bool
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupsRequestEndpointGroupConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_name is not None:
            result['EndpointGroupName'] = self.endpoint_group_name
        if self.endpoint_group_description is not None:
            result['EndpointGroupDescription'] = self.endpoint_group_description
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.enable_client_ippreservation_toa is not None:
            result['EnableClientIPPreservationToa'] = self.enable_client_ippreservation_toa
        if self.enable_client_ippreservation_proxy_protocol is not None:
            result['EnableClientIPPreservationProxyProtocol'] = self.enable_client_ippreservation_proxy_protocol
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupName') is not None:
            self.endpoint_group_name = m.get('EndpointGroupName')
        if m.get('EndpointGroupDescription') is not None:
            self.endpoint_group_description = m.get('EndpointGroupDescription')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('EnableClientIPPreservationToa') is not None:
            self.enable_client_ippreservation_toa = m.get('EnableClientIPPreservationToa')
        if m.get('EnableClientIPPreservationProxyProtocol') is not None:
            self.enable_client_ippreservation_proxy_protocol = m.get('EnableClientIPPreservationProxyProtocol')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class UpdateEndpointGroupsRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dry_run=None, endpoint_group_configurations=None,
                 listener_id=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.endpoint_group_configurations = endpoint_group_configurations  # type: list[UpdateEndpointGroupsRequestEndpointGroupConfigurations]
        self.listener_id = listener_id  # type: str

    def validate(self):
        if self.endpoint_group_configurations:
            for k in self.endpoint_group_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k in m.get('EndpointGroupConfigurations'):
                temp_model = UpdateEndpointGroupsRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class UpdateEndpointGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, endpoint_group_ids=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        return self


class UpdateEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupsResponse, self).to_map()
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
            temp_model = UpdateEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpSetsRequest(TeaModel):
    def __init__(self, region_id=None, ip_set_ids=None):
        self.region_id = region_id  # type: str
        self.ip_set_ids = ip_set_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ip_set_ids is not None:
            result['IpSetIds'] = self.ip_set_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IpSetIds') is not None:
            self.ip_set_ids = m.get('IpSetIds')
        return self


class DeleteIpSetsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpSetsResponseBody, self).to_map()
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


class DeleteIpSetsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteIpSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIpSetsResponse, self).to_map()
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
            temp_model = DeleteIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BandwidthPackageAddAcceleratorRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, accelerator_id=None):
        self.region_id = region_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BandwidthPackageAddAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class BandwidthPackageAddAcceleratorResponseBody(TeaModel):
    def __init__(self, request_id=None, accelerators=None, bandwidth_package_id=None):
        self.request_id = request_id  # type: str
        self.accelerators = accelerators  # type: list[str]
        self.bandwidth_package_id = bandwidth_package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BandwidthPackageAddAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        return self


class BandwidthPackageAddAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BandwidthPackageAddAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BandwidthPackageAddAcceleratorResponse, self).to_map()
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
            temp_model = BandwidthPackageAddAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAclAttributeRequest(TeaModel):
    def __init__(self, region_id=None, acl_id=None, acl_name=None, client_token=None, dry_run=None):
        self.region_id = region_id  # type: str
        self.acl_id = acl_id  # type: str
        self.acl_name = acl_name  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAclAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class UpdateAclAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None, acl_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.acl_id = acl_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAclAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        return self


class UpdateAclAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAclAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAclAttributeResponse, self).to_map()
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
            temp_model = UpdateAclAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAcceleratorsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, accelerator_id=None, state=None):
        self.region_id = region_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.accelerator_id = accelerator_id  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAcceleratorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, bandwidth_type=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAcceleratorsResponseBodyAccelerators(TeaModel):
    def __init__(self, dns_name=None, type=None, second_dns_name=None, spec=None, state=None, create_time=None,
                 cen_id=None, ddos_id=None, basic_bandwidth_package=None, region_id=None, instance_charge_type=None,
                 accelerator_id=None, description=None, bandwidth=None, expired_time=None, name=None,
                 cross_domain_bandwidth_package=None):
        self.dns_name = dns_name  # type: str
        self.type = type  # type: str
        self.second_dns_name = second_dns_name  # type: str
        self.spec = spec  # type: str
        self.state = state  # type: str
        self.create_time = create_time  # type: long
        self.cen_id = cen_id  # type: str
        self.ddos_id = ddos_id  # type: str
        self.basic_bandwidth_package = basic_bandwidth_package  # type: ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage
        self.region_id = region_id  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.description = description  # type: str
        self.bandwidth = bandwidth  # type: int
        self.expired_time = expired_time  # type: long
        self.name = name  # type: str
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package  # type: ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()

    def to_map(self):
        _map = super(ListAcceleratorsResponseBodyAccelerators, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.type is not None:
            result['Type'] = self.type
        if self.second_dns_name is not None:
            result['SecondDnsName'] = self.second_dns_name
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.state is not None:
            result['State'] = self.state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.name is not None:
            result['Name'] = self.name
        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('SecondDnsName') is not None:
            self.second_dns_name = m.get('SecondDnsName')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('BasicBandwidthPackage') is not None:
            temp_model = ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m['BasicBandwidthPackage'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m['CrossDomainBandwidthPackage'])
        return self


class ListAcceleratorsResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, accelerators=None, page_number=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.accelerators = accelerators  # type: list[ListAcceleratorsResponseBodyAccelerators]
        self.page_number = page_number  # type: int

    def validate(self):
        if self.accelerators:
            for k in self.accelerators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAcceleratorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Accelerators'] = []
        if self.accelerators is not None:
            for k in self.accelerators:
                result['Accelerators'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.accelerators = []
        if m.get('Accelerators') is not None:
            for k in m.get('Accelerators'):
                temp_model = ListAcceleratorsResponseBodyAccelerators()
                self.accelerators.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListAcceleratorsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAcceleratorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAcceleratorsResponse, self).to_map()
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
            temp_model = ListAcceleratorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateListenerRequestPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateListenerRequestCertificates(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateListenerRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, accelerator_id=None, name=None, description=None,
                 client_affinity=None, protocol=None, proxy_protocol=None, port_ranges=None, certificates=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.client_affinity = client_affinity  # type: str
        self.protocol = protocol  # type: str
        self.proxy_protocol = proxy_protocol  # type: bool
        self.port_ranges = port_ranges  # type: list[CreateListenerRequestPortRanges]
        self.certificates = certificates  # type: list[CreateListenerRequestCertificates]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateListenerRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = CreateListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        return self


class CreateListenerResponseBody(TeaModel):
    def __init__(self, request_id=None, listener_id=None):
        self.request_id = request_id  # type: str
        self.listener_id = listener_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class CreateListenerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateListenerResponse, self).to_map()
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
            temp_model = CreateListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSpareIpsRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dry_run=None, accelerator_id=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.accelerator_id = accelerator_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSpareIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        return self


class ListSpareIpsResponseBodySpareIps(TeaModel):
    def __init__(self, spare_ip=None, state=None):
        self.spare_ip = spare_ip  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSpareIpsResponseBodySpareIps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spare_ip is not None:
            result['SpareIp'] = self.spare_ip
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpareIp') is not None:
            self.spare_ip = m.get('SpareIp')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListSpareIpsResponseBody(TeaModel):
    def __init__(self, request_id=None, spare_ips=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.spare_ips = spare_ips  # type: list[ListSpareIpsResponseBodySpareIps]

    def validate(self):
        if self.spare_ips:
            for k in self.spare_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSpareIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SpareIps'] = []
        if self.spare_ips is not None:
            for k in self.spare_ips:
                result['SpareIps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spare_ips = []
        if m.get('SpareIps') is not None:
            for k in m.get('SpareIps'):
                temp_model = ListSpareIpsResponseBodySpareIps()
                self.spare_ips.append(temp_model.from_map(k))
        return self


class ListSpareIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSpareIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSpareIpsResponse, self).to_map()
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
            temp_model = ListSpareIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(self, type=None, weight=None, endpoint=None):
        self.type = type  # type: str
        self.weight = weight  # type: long
        self.endpoint = endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        return self


class CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides(TeaModel):
    def __init__(self, listener_port=None, endpoint_port=None):
        self.listener_port = listener_port  # type: long
        self.endpoint_port = endpoint_port  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        return self


class CreateEndpointGroupsRequestEndpointGroupConfigurations(TeaModel):
    def __init__(self, endpoint_group_name=None, endpoint_group_description=None, endpoint_group_region=None,
                 traffic_percentage=None, health_check_enabled=None, health_check_interval_seconds=None, health_check_path=None,
                 health_check_port=None, health_check_protocol=None, threshold_count=None, endpoint_configurations=None,
                 endpoint_request_protocol=None, endpoint_group_type=None, port_overrides=None, enable_client_ippreservation_toa=None,
                 enable_client_ippreservation_proxy_protocol=None):
        self.endpoint_group_name = endpoint_group_name  # type: str
        self.endpoint_group_description = endpoint_group_description  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.traffic_percentage = traffic_percentage  # type: long
        self.health_check_enabled = health_check_enabled  # type: bool
        self.health_check_interval_seconds = health_check_interval_seconds  # type: long
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: long
        self.health_check_protocol = health_check_protocol  # type: str
        self.threshold_count = threshold_count  # type: long
        self.endpoint_configurations = endpoint_configurations  # type: list[CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations]
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.port_overrides = port_overrides  # type: list[CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides]
        self.enable_client_ippreservation_toa = enable_client_ippreservation_toa  # type: bool
        self.enable_client_ippreservation_proxy_protocol = enable_client_ippreservation_proxy_protocol  # type: bool

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEndpointGroupsRequestEndpointGroupConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_name is not None:
            result['EndpointGroupName'] = self.endpoint_group_name
        if self.endpoint_group_description is not None:
            result['EndpointGroupDescription'] = self.endpoint_group_description
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.enable_client_ippreservation_toa is not None:
            result['EnableClientIPPreservationToa'] = self.enable_client_ippreservation_toa
        if self.enable_client_ippreservation_proxy_protocol is not None:
            result['EnableClientIPPreservationProxyProtocol'] = self.enable_client_ippreservation_proxy_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupName') is not None:
            self.endpoint_group_name = m.get('EndpointGroupName')
        if m.get('EndpointGroupDescription') is not None:
            self.endpoint_group_description = m.get('EndpointGroupDescription')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('EnableClientIPPreservationToa') is not None:
            self.enable_client_ippreservation_toa = m.get('EnableClientIPPreservationToa')
        if m.get('EnableClientIPPreservationProxyProtocol') is not None:
            self.enable_client_ippreservation_proxy_protocol = m.get('EnableClientIPPreservationProxyProtocol')
        return self


class CreateEndpointGroupsRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dry_run=None, accelerator_id=None, listener_id=None,
                 endpoint_group_configurations=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.endpoint_group_configurations = endpoint_group_configurations  # type: list[CreateEndpointGroupsRequestEndpointGroupConfigurations]

    def validate(self):
        if self.endpoint_group_configurations:
            for k in self.endpoint_group_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k in m.get('EndpointGroupConfigurations'):
                temp_model = CreateEndpointGroupsRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k))
        return self


class CreateEndpointGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, endpoint_group_ids=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        return self


class CreateEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEndpointGroupsResponse, self).to_map()
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
            temp_model = CreateEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDdosFromAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachDdosFromAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachDdosFromAcceleratorResponseBody(TeaModel):
    def __init__(self, ddos_id=None, request_id=None):
        self.ddos_id = ddos_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachDdosFromAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachDdosFromAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachDdosFromAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachDdosFromAcceleratorResponse, self).to_map()
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
            temp_model = DetachDdosFromAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpareIpRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dry_run=None, accelerator_id=None, spare_ip=None):
        self.region_id = region_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.accelerator_id = accelerator_id  # type: str
        self.spare_ip = spare_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSpareIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.spare_ip is not None:
            result['SpareIp'] = self.spare_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('SpareIp') is not None:
            self.spare_ip = m.get('SpareIp')
        return self


class GetSpareIpResponseBody(TeaModel):
    def __init__(self, request_id=None, state=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSpareIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetSpareIpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSpareIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSpareIpResponse, self).to_map()
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
            temp_model = GetSpareIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


