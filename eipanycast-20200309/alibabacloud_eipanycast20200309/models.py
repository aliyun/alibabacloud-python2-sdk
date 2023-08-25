# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllocateAnycastEipAddressRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, description=None, instance_charge_type=None,
                 internet_charge_type=None, name=None, resource_group_id=None, service_location=None):
        # The maximum bandwidth of the Anycast EIP. Unit: Mbit/s.
        # 
        # Valid values: **200** to **1000**.
        # 
        # Default value: **1000**.
        # 
        # >  The maximum bandwidth value is not a guaranteed value. It indicates the upper limit of bandwidth and is for reference only.
        self.bandwidth = bandwidth  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The client token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **ClientToken**. The value of **RequestId** may be different for each API request.
        self.client_token = client_token  # type: str
        # The description of the Anycast EIP.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description  # type: str
        # The billing method of the Anycast EIP.
        # 
        # Set the value to **PostPaid**, which specifies the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type  # type: str
        # The metering method of the Anycast EIP.
        # 
        # Set the value to **PayByTraffic**, which specifies the pay-by-data-transfer metering method.
        self.internet_charge_type = internet_charge_type  # type: str
        # The name of the Anycast EIP.
        # 
        # The name must be 0 to 128 characters in length, and can contain letters, digits, underscores (\_), and hyphens (-). It must start with a letter.
        self.name = name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The access area of the Anycast EIP.
        # 
        # Set the value to **international**, which specifies the regions outside the Chinese mainland.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        return self


class AllocateAnycastEipAddressResponseBody(TeaModel):
    def __init__(self, anycast_id=None, order_id=None, request_id=None):
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AllocateAnycastEipAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AllocateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAnycastEipAddressRequestPopLocations(TeaModel):
    def __init__(self, pop_location=None):
        # The information about the access points in associated access areas when you associate an Anycast EIP with a cloud resource.
        # 
        # If this is your first time to associate an Anycast EIP with a cloud resource, ignore this parameter. The system automatically associates all access areas.
        # 
        # You can call the [DescribeAnycastPopLocations](~~171938~~) operation to query information about access points in supported access areas.
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
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id  # type: str
        # The association mode. Valid values:
        # 
        # *   **Default**: the default mode. In this mode, cloud resources to be associated are set as default origin servers.
        # *   **Normal**: the standard mode. In this mode, cloud resources to be associated are set as standard origin servers.
        # 
        # > You can associate an Anycast EIP with cloud resources in multiple regions. However, you can set only one cloud resource as the default origin server. Other cloud resources are set as standard origin servers. If you do not specify or add an access point, requests are forwarded to the default origin server.
        # 
        # *   If this is your first time to associate an Anycast EIP with a cloud resource, set the value to **Default**.
        # *   If not, you can also set the value to **Default**, which specifies a new default origin server. In this case, the previous origin server functions as a standard origin server.
        self.association_mode = association_mode  # type: str
        # The ID of the cloud resource with which you want to associate the Anycast EIP.
        self.bind_instance_id = bind_instance_id  # type: str
        # The ID of the region where the cloud resource is deployed.
        # 
        # You can associate Anycast EIPs only with cloud resources in specific regions. You can call the [DescribeAnycastServerRegions](~~171939~~) operation to query the region IDs.
        self.bind_instance_region_id = bind_instance_region_id  # type: str
        # The type of cloud resource with which you want to associate the Anycast EIP. Valid values:
        # 
        # *   **SlbInstance**: an internal-facing Server Load Balancer (SLB) instance that is deployed in a virtual private cloud (VPC)
        # *   **NetworkInterface**: an elastic network interface (ENI)
        self.bind_instance_type = bind_instance_type  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # >  If you do not set this parameter, the system automatically uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token  # type: str
        # Specifies whether to only precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request. After the request passes the precheck, the Anycast EIP is not associated with the instance. The system checks the required parameters, request syntax, and limits. If the request fails to pass the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the API request. If the request passes the precheck, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The information about the access points in associated access areas when you associate an Anycast EIP with a cloud resource.
        # 
        # If this is your first time to associate an Anycast EIP with a cloud resource, ignore this parameter. The system automatically associates all access areas.
        # 
        # You can call the [DescribeAnycastPopLocations](~~171938~~) operation to query information about access points in supported access areas.
        self.pop_locations = pop_locations  # type: list[AssociateAnycastEipAddressRequestPopLocations]
        # The secondary private IP address of the ENI with which you want to associate the Anycast EIP.
        # 
        # This parameter is valid only when you set **BindInstanceType** to **NetworkInterface**. If you do not set this parameter, the primary private IP address of the ENI is used.
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateAnycastEipAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AssociateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastEipAddressRequest(TeaModel):
    def __init__(self, anycast_id=None, bind_instance_id=None, ip=None):
        # The ID of the Anycast EIP.
        # 
        # >  You must specify at least one of **Ip** and **AnycastId**.
        self.anycast_id = anycast_id  # type: str
        # The ID of the cloud resource with which the Anycast EIP is associated.
        self.bind_instance_id = bind_instance_id  # type: str
        # The IP address of the Anycast EIP.
        # 
        # >  You must specify at least one of **Ip** and **AnycastId**.
        self.ip = ip  # type: str

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
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations(TeaModel):
    def __init__(self, pop_location=None):
        # The information about the access points in associated access areas when you associate an Anycast EIP with a cloud resource.
        # 
        # If this is your first time associating an Anycast EIP with a cloud resource, the system returns information about access points in all access areas.
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
        # The association mode. Valid values:
        # 
        # *   **Default**: the default mode. In this mode, associated cloud resources are set as default origin servers.
        # *   **Normal**: the standard mode. In this mode, associated cloud resources are set as standard origin servers.
        self.association_mode = association_mode  # type: str
        # The ID of the cloud resource with which the Anycast EIP is associated.
        self.bind_instance_id = bind_instance_id  # type: str
        # The ID of the region in which the cloud resource is deployed.
        self.bind_instance_region_id = bind_instance_region_id  # type: str
        # The type of cloud resource with which the Anycast EIP is associated. Valid values:
        # 
        # *   **SlbInstance**: an internal-facing Server Load Balancer (SLB) instance that is deployed in a virtual private cloud (VPC)
        # *   **NetworkInterface**: an elastic network interface (ENI)
        self.bind_instance_type = bind_instance_type  # type: str
        # The time when the Anycast EIP was associated.
        # 
        # The time follows the ISO8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.bind_time = bind_time  # type: str
        # The information about the access points in associated access areas when you associate an Anycast EIP with a cloud resource.
        # 
        # If this is your first time associating an Anycast EIP with a cloud resource, the system returns information about access points in all access areas.
        self.pop_locations = pop_locations  # type: list[DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations]
        # The secondary private IP address of the associated ENI.
        # 
        # This parameter is valid only when **BindInstanceType** is set to **NetworkInterface**.
        self.private_ip_address = private_ip_address  # type: str
        # The status of the cloud resource. Valid values:
        # 
        # *   **BINDING**\
        # *   **BINDED**\
        # *   **UNBINDING**\
        # *   **DELETED**\
        # *   **MODIFYING**\
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


class DescribeAnycastEipAddressResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAnycastEipAddressResponseBodyTags, self).to_map()
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


class DescribeAnycastEipAddressResponseBody(TeaModel):
    def __init__(self, ali_uid=None, anycast_eip_bind_info_list=None, anycast_id=None, bandwidth=None, bid=None,
                 business_status=None, create_time=None, description=None, instance_charge_type=None, internet_charge_type=None,
                 ip_address=None, name=None, request_id=None, resource_group_id=None, service_location=None, status=None,
                 tags=None):
        # The ID of the account to which the Anycast EIP belongs.
        self.ali_uid = ali_uid  # type: long
        # The information about the cloud resource with which the Anycast EIP is associated.
        self.anycast_eip_bind_info_list = anycast_eip_bind_info_list  # type: list[DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList]
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id  # type: str
        # The maximum bandwidth of the Anycast EIP. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: int
        # The BID of the account to which the Anycast EIP belongs.
        self.bid = bid  # type: str
        # The service status of the Anycast EIP. Valid values:
        # 
        # *   **Normal**\
        # *   **FinancialLocked**\
        self.business_status = business_status  # type: str
        # The time when the Anycast EIP was created.
        # 
        # The time follows the ISO8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the Anycast EIP.
        self.description = description  # type: str
        # The billing method of the Anycast EIP.
        # 
        # Only **PostPaid** may be returned, which indicates the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type  # type: str
        # The metering method of the Anycast EIP.
        # 
        # Only **PayByTraffic** may be returned, which indicates the pay-by-data-transfer metering method.
        self.internet_charge_type = internet_charge_type  # type: str
        # The IP address of the Anycast EIP.
        self.ip_address = ip_address  # type: str
        # The name of the Anycast EIP.
        self.name = name  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The area from which you can use the Anycast EIP to access the backend server over the Internet.
        # 
        # Only **international** may be returned, which indicates the areas outside the Chinese mainland.
        self.service_location = service_location  # type: str
        # The status of the Anycast EIP. Valid values:
        # 
        # *   **Associating**\
        # *   **Unassociating**\
        # *   **Allocated**\
        # *   **Associated**\
        # *   **Modifying**\
        # *   **Releasing**\
        # *   **Released**\
        self.status = status  # type: str
        # The tag information.
        self.tags = tags  # type: list[DescribeAnycastEipAddressResponseBodyTags]

    def validate(self):
        if self.anycast_eip_bind_info_list:
            for k in self.anycast_eip_bind_info_list:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeAnycastEipAddressResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeAnycastEipAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAnycastEipAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastPopLocationsRequest(TeaModel):
    def __init__(self, service_location=None):
        # The access area of the Anycast elastic IP address (EIP).
        # 
        # Set the value to **international**, which specifies the regions outside the Chinese mainland.
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
        # The ID of the region where the access point is deployed.
        self.region_id = region_id  # type: str
        # The name of the region where the access point is deployed.
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
        # The list of access points in the specified access area.
        self.anycast_pop_location_list = anycast_pop_location_list  # type: list[DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList]
        # The number of access points.
        self.count = count  # type: str
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAnycastPopLocationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeAnycastPopLocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastServerRegionsRequest(TeaModel):
    def __init__(self, service_location=None):
        # The access area from which you use the Anycast EIP to communicate with the Internet.
        # 
        # Set the value to **international**, which specifies the regions outside the Chinese mainland.
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
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the region.
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
        # The list of regions where you can associate Anycast EIPs with backend servers.
        self.anycast_server_region_list = anycast_server_region_list  # type: list[DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList]
        # The total number of entries returned.
        self.count = count  # type: str
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAnycastServerRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeAnycastServerRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnycastEipAddressesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the resource. You can specify up to 20 tag keys. You cannot specify empty strings as tag keys.
        # 
        # The key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        # 
        # >  You must specify at least one of **Tag.N** (**Tag.N.Key** and **Tag.N.Value**).
        self.key = key  # type: str
        # The tag value of the resource. You can specify up to 20 tag values. It can be an empty string.
        # 
        # The value cannot exceed 128 characters in length and can contain digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter but cannot start with `aliyun` or `acs:`. The value cannot contain `http://` or `https://`.
        # 
        # >  You must specify at least one of **Tag.N** (**Tag.N.Key** and **Tag.N.Value**).
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnycastEipAddressesRequestTags, self).to_map()
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


class ListAnycastEipAddressesRequest(TeaModel):
    def __init__(self, anycast_eip_address=None, anycast_id=None, anycast_ids=None, bind_instance_ids=None,
                 business_status=None, instance_charge_type=None, internet_charge_type=None, max_results=None, name=None,
                 next_token=None, resource_group_id=None, service_location=None, status=None, tags=None):
        # The IP address that is allocated to the Anycast EIP.
        self.anycast_eip_address = anycast_eip_address  # type: str
        # The ID of the Anycast EIP.
        # 
        # >  To ensure the accuracy of the query result, we do not recommend that you specify **AnycastIds** and **AnycastId** at the same time.
        self.anycast_id = anycast_id  # type: str
        # The IDs of Anycast EIPs.
        # 
        # You can enter at most 50 Anycast EIP IDs.
        # 
        # >  To ensure the accuracy of the query result, we do not recommend that you specify **AnycastIds** and **AnycastId** at the same time.
        self.anycast_ids = anycast_ids  # type: list[str]
        # The IDs of the cloud resources with which the Anycast EIPs are associated.
        # 
        # You can enter at most 100 cloud resource IDs.
        self.bind_instance_ids = bind_instance_ids  # type: list[str]
        # The service status of the Anycast EIP. Valid values:
        # 
        # *   **Normal**\
        # *   **FinancialLocked**\
        self.business_status = business_status  # type: str
        # The billing method of the Anycast EIP.
        # 
        # Set the value to **PostPaid**, which specifies the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type  # type: str
        # The metering method of the Anycast EIP.
        # 
        # Set the value to **PayByTraffic**, which specifies the pay-by-data-transfer metering method.
        self.internet_charge_type = internet_charge_type  # type: str
        # The number of entries to return on each page. Valid values: **20 to 100**. Default value: **50**.
        self.max_results = max_results  # type: int
        # The name of the Anycast EIP.
        # 
        # The name must be 0 to 128 characters in length, and can contain digits, hyphens (-), and underscores (\_). The name must start with a letter.
        self.name = name  # type: str
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The access area of the Anycast EIP.
        # 
        # Set the value to **international**, which specifies the regions outside the Chinese mainland.
        self.service_location = service_location  # type: str
        # The status of the Anycast EIP. Valid values:
        # 
        # *   **Associating**\
        # *   **Unassociating**\
        # *   **Allocated**\
        # *   **Associated**\
        # *   **Modifying**\
        # *   **Releasing**\
        # *   **Released**\
        self.status = status  # type: str
        # The tags.
        self.tags = tags  # type: list[ListAnycastEipAddressesRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnycastEipAddressesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_eip_address is not None:
            result['AnycastEipAddress'] = self.anycast_eip_address
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.anycast_ids is not None:
            result['AnycastIds'] = self.anycast_ids
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnycastEipAddress') is not None:
            self.anycast_eip_address = m.get('AnycastEipAddress')
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('AnycastIds') is not None:
            self.anycast_ids = m.get('AnycastIds')
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListAnycastEipAddressesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList(TeaModel):
    def __init__(self, bind_instance_id=None, bind_instance_region_id=None, bind_instance_type=None,
                 bind_time=None):
        # The ID of the cloud resource with which the Anycast EIP is associated.
        self.bind_instance_id = bind_instance_id  # type: str
        # The ID of the region where the cloud resource is deployed.
        self.bind_instance_region_id = bind_instance_region_id  # type: str
        # The type of cloud resource with which the Anycast EIP is associated.
        # 
        # *   **SlbInstance**: an internal-facing Classic Load Balancer (CLB) instance deployed in a virtual private cloud (VPC). CLB is formerly known as Server Load Balancer (SLB).
        # *   **NetworkInterface**: an elastic network interface (ENI).
        self.bind_instance_type = bind_instance_type  # type: str
        # The time when the Anycast EIP was associated.
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


class ListAnycastEipAddressesResponseBodyAnycastListTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnycastEipAddressesResponseBodyAnycastListTags, self).to_map()
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


class ListAnycastEipAddressesResponseBodyAnycastList(TeaModel):
    def __init__(self, ali_uid=None, anycast_eip_bind_info_list=None, anycast_id=None, bandwidth=None,
                 business_status=None, create_time=None, description=None, instance_charge_type=None, internet_charge_type=None,
                 ip_address=None, name=None, resource_group_id=None, service_location=None, service_managed=None, status=None,
                 tags=None):
        # The ID of the account to which the Anycast EIP belongs.
        self.ali_uid = ali_uid  # type: long
        # The list of cloud resources with which the Anycast EIPs are associated.
        self.anycast_eip_bind_info_list = anycast_eip_bind_info_list  # type: list[ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList]
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id  # type: str
        # The maximum bandwidth of the Anycast EIP. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: int
        # The service status of the Anycast EIP. Valid values:
        # 
        # *   **Normal**\
        # *   **FinancialLocked**\
        self.business_status = business_status  # type: str
        # The time when the Anycast EIP was created.
        self.create_time = create_time  # type: str
        # The description of the Anycast EIP.
        self.description = description  # type: str
        # The billing method of the Anycast EIP.
        # 
        # **PostPaid**: pay-as-you-go
        self.instance_charge_type = instance_charge_type  # type: str
        # The metering method of the Anycast EIP.
        # 
        # **PayByTraffic**: pay-by-data-transfer
        self.internet_charge_type = internet_charge_type  # type: str
        # The IP address of the Anycast EIP.
        self.ip_address = ip_address  # type: str
        # The name of the Anycast EIP.
        self.name = name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # The access area of the Anycast EIP.
        # 
        # **international**: regions outside the Chinese mainland
        self.service_location = service_location  # type: str
        # Indicates whether the resource is created by the service account.
        # 
        # *   **0**: no
        # *   **1**: yes
        self.service_managed = service_managed  # type: int
        # The status of the Anycast EIP.
        # 
        # *   **Associating**\
        # *   **Unassociating**\
        # *   **Allocated**\
        # *   **Associated**\
        # *   **Modifying**\
        # *   **Releasing**\
        # *   **Released**\
        self.status = status  # type: str
        # The information about the tags.
        self.tags = tags  # type: list[ListAnycastEipAddressesResponseBodyAnycastListTags]

    def validate(self):
        if self.anycast_eip_bind_info_list:
            for k in self.anycast_eip_bind_info_list:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListAnycastEipAddressesResponseBodyAnycastListTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListAnycastEipAddressesResponseBody(TeaModel):
    def __init__(self, anycast_list=None, next_token=None, request_id=None, total_count=None):
        # The list of Anycast EIPs.
        self.anycast_list = anycast_list  # type: list[ListAnycastEipAddressesResponseBodyAnycastList]
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If **NextToken** is not empty, the value of NextToken can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The number of entries returned.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAnycastEipAddressesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAnycastEipAddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N to add to the resource. You can specify up to 20 tag keys. It cannot be an empty string.
        # 
        # The key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        # 
        # >  Specify at least one of **ResourceId.N** or **Tag.N** (**Tag.N.Key** and **Tag.N.Value**).
        self.key = key  # type: str
        # The value of tag N to add to the resource. You can specify up to 20 tag values. It can be an empty string.
        # 
        # The value can be up to 128 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter but cannot start with `aliyun` or `acs:`. The value cannot contain `http://` or `https://`.
        # 
        # >  Specify at least one of **ResourceId.N** or **Tag.N** (**Tag.N.Key** and **Tag.N.Value**).
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
    def __init__(self, max_results=None, next_token=None, resource_id=None, resource_type=None, tag=None):
        # The number of entries to return on each page. Valid values:**1** to **50**. Default value: **50**.
        self.max_results = max_results  # type: str
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If this is your first query or no subsequent query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the value to the value of **NextToken** that is returned in the last call.
        self.next_token = next_token  # type: str
        # The ID of the resource.
        self.resource_id = resource_id  # type: list[str]
        # The resource type. Set the value to **ANYCASTEIPADDRESS**.
        self.resource_type = resource_type  # type: str
        # The tags
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The resource ID.
        self.resource_id = resource_id  # type: str
        # The resource type. Set the value to **ANYCASTEIPADDRESS**.
        self.resource_type = resource_type  # type: str
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If the **NextToken** parameter is empty, no next page exists.
        # *   If the return value of **NextToken** is not empty, the value indicates the token that is used for the next query.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The resources to which the tags are added.
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
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


class ModifyAnycastEipAddressAttributeRequest(TeaModel):
    def __init__(self, anycast_id=None, description=None, name=None):
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id  # type: str
        # The description of the Anycast EIP.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description  # type: str
        # The name of the Anycast EIP.
        # 
        # The name must be 0 to 128 characters in length, and can contain letters, digits, underscores (\_), and hyphens (-). It must start with a letter.
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAnycastEipAddressAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyAnycastEipAddressAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAnycastEipAddressSpecRequest(TeaModel):
    def __init__(self, anycast_id=None, bandwidth=None):
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id  # type: str
        # The maximum bandwidth of the Anycast EIP. Unit: Mbit/s.
        # 
        # Valid values: **200** to **1000**.
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAnycastEipAddressSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyAnycastEipAddressSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseAnycastEipAddressRequest(TeaModel):
    def __init__(self, anycast_id=None, client_token=None):
        # The ID of the Anycast EIP to be released.
        self.anycast_id = anycast_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value. Make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseAnycastEipAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ReleaseAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N to add to the resource. You must enter at least one tag key and at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The key cannot exceed 64 characters in length, and can contain digits, periods (.), underscores (\_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        # 
        # >  When you call this operation, you must specify **Tag.N.Key**.
        self.key = key  # type: str
        # The value of tag N to add to the resource. You must enter at least one tag value and at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value cannot exceed 128 characters in length, and can contain digits, periods (.), underscores (\_), and hyphens (-). It must start with a letter but cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # >  When you call this operation, you must specify **Tag.N.Value**.
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
    def __init__(self, resource_id=None, resource_type=None, tag=None):
        # The list of resource IDs.
        self.resource_id = resource_id  # type: list[str]
        # The resource type. Set the value to **ANYCASTEIPADDRESS**.
        self.resource_type = resource_type  # type: str
        # The tags.
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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values:
        # 
        # **true**\
        # 
        # **false**\
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class UnassociateAnycastEipAddressRequest(TeaModel):
    def __init__(self, anycast_id=None, bind_instance_id=None, bind_instance_region_id=None,
                 bind_instance_type=None, client_token=None, dry_run=None, private_ip_address=None):
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id  # type: str
        # The ID of the cloud resource from which you want to disassociate the Anycast EIP.
        self.bind_instance_id = bind_instance_id  # type: str
        # The region where the cloud resource is deployed.
        self.bind_instance_region_id = bind_instance_region_id  # type: str
        # The type of cloud resource from which you want to disassociate the Anycast EIP. Valid values:
        # 
        # *   **SlbInstance**: an internal-facing Server Load Balancer (SLB) instance that is deployed in a virtual private cloud (VPC)
        # *   **NetworkInterface**: an elastic network interface (ENI)
        self.bind_instance_type = bind_instance_type  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # >  If you do not set this parameter, the system automatically uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token  # type: str
        # Specifies whether to only precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request without disassociating the Anycast EIP. The system checks the required parameters, request syntax, and limits. If the request fails to pass the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the API request. If the request passes the precheck, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: str
        # The secondary private IP address of the ENI from which you want to disassociate the Anycast EIP.
        # 
        # This parameter is valid only when you set **BindInstanceType** to **NetworkInterface**. If you do not set this parameter, the primary private IP address of the ENI is returned.
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnassociateAnycastEipAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UnassociateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None):
        # The ID of the resource.
        self.resource_id = resource_id  # type: list[str]
        # The resource type. Set the value to **ANYCASTEIPADDRESS**.
        self.resource_type = resource_type  # type: str
        # The tag keys of the resource.
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the call was successful. Valid values:
        # 
        # **true**\
        # 
        # **false**\
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UpdateAnycastEipAddressAssociationsRequestPopLocationAddList(TeaModel):
    def __init__(self, pop_location=None):
        # The access points in the access areas to be added.
        # 
        # You can call the [DescribeAnycastPopLocations](~~171938~~) operation to query the access points in supported access areas.
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
        # The access points in the access areas to be deleted.
        # 
        # >  If the access point in the access area is associated with a default origin server, you cannot delete the access point in the access area.
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
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id  # type: str
        # The association mode. Valid values:
        # 
        # *   **Default**: the default mode. In this mode, cloud resources to be associated are set as default origin servers.
        # *   **Normal**: the standard mode. In this mode, cloud resources to be associated are set as standard origin servers.
        self.association_mode = association_mode  # type: str
        # The ID of the cloud resource with which you want to associate the Anycast EIP.
        self.bind_instance_id = bind_instance_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # >  If you do not set this parameter, the system automatically uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token  # type: str
        # Specifies whether to only precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request without updating the association information. The system checks the required parameters, request syntax, and limits. If the request fails to pass the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the API request. If the request passes the precheck, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The access areas and access points to be added.
        self.pop_location_add_list = pop_location_add_list  # type: list[UpdateAnycastEipAddressAssociationsRequestPopLocationAddList]
        # The access areas and access points to be deleted.
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAnycastEipAddressAssociationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateAnycastEipAddressAssociationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


