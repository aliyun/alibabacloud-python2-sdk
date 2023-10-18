# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateInstanceRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_renew=None, charge_type=None, cold_storage_size=None, cpu=None,
                 duration=None, gateway_count=None, initial_databases=None, instance_name=None, instance_type=None,
                 leader_instance_id=None, pricing_cycle=None, region_id=None, resource_group_id=None, storage_size=None,
                 v_switch_id=None, vpc_id=None, zone_id=None):
        # Specifies whether to enable auto-payment. Default value: true. Valid values:
        # 
        # *   true
        # *   false
        # 
        # > The default value is true. If the balance of your account is insufficient, you can set this parameter to false. In this case, an unpaid order is generated. You can log on to the User Center to pay for the order.
        self.auto_pay = auto_pay  # type: bool
        # Specifies whether to enable monthly auto-renewal. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.auto_renew = auto_renew  # type: bool
        # The billing method of the instance. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        # 
        # > This parameter is invalid for shared instances. Shared instances have fixed specifications and are pay-as-you-go instances.
        self.charge_type = charge_type  # type: str
        # The infrequent access (IA) storage space of the instance. Unit: GB.
        # 
        # > This parameter is invalid for pay-as-you-go instances.
        self.cold_storage_size = cold_storage_size  # type: long
        # The instance specifications. Valid values:
        # 
        # *   8-core 32 GB (number of compute nodes: 1)
        # *   16-core 64 GB (number of compute nodes: 1)
        # *   32-core 128 GB (number of compute nodes: 2)
        # *   64-core 256 GB (number of compute nodes: 4)
        # *   96-core 384 GB (number of compute nodes: 6)
        # *   128-core 512 GB (number of compute nodes: 8)
        # *   Others
        # 
        # > 
        # 
        # *   Set this parameter to the number of cores.
        # 
        # *   If you want to set this parameter to specifications with more than 1,024 compute units (CUs), you must submit a ticket.
        # 
        # *   If you want to purchase a shared instance, you do not need to configure this parameter.
        # 
        # *   The specifications of 8-core 32 GB (number of compute nodes: 1) are for trial use only and cannot be used for production.
        self.cpu = cpu  # type: long
        # The validity period of the instance that you want to purchase. For example, you can specify a validity period of two months.
        # 
        # > You do not need to configure this parameter for pay-as-you-go instances.
        self.duration = duration  # type: long
        # The number of gateways. Valid values: 2 to 50.
        # 
        # > This parameter is required only for virtual warehouse instances.
        self.gateway_count = gateway_count  # type: long
        self.initial_databases = initial_databases  # type: str
        # The name of the Hologres instance that you want to purchase. The name must be 2 to 64 characters in length.
        self.instance_name = instance_name  # type: str
        # The type of the instance. Valid values:
        # 
        # *   Standard: general-purpose instance
        # *   Follower: read-only secondary instance
        # *   Warehouse: virtual warehouse instance
        # *   Shared: shared instance
        self.instance_type = instance_type  # type: str
        # The ID of the primary instance. This parameter is required for read-only secondary instances.
        # 
        # > The primary instance and secondary instances must meet the following requirements:
        # 
        # *   The primary instance is in the Running state.
        # 
        # *   The primary instance and secondary instances are deployed in the same region.
        # 
        # *   The primary instance and secondary instances are deployed in the same zone.
        # 
        # *   Less than 10 secondary instances are associated with the primary instance.
        # 
        # *   The primary and secondary instances belong to the same Alibaba Cloud account.
        self.leader_instance_id = leader_instance_id  # type: str
        # The billing cycle. Valid values:
        # 
        # *   Month
        # *   Hour
        # 
        # > 
        # 
        # *   This parameter can only be set to Month for subscription instances.
        # 
        # *   This parameter can only be set to Hour for pay-as-you-go instances.
        # 
        # *   By default, this parameter is set to Hour for shared instances.
        self.pricing_cycle = pricing_cycle  # type: str
        # The ID of the region. You can go to the [OpenAPI Explorer](https://api.aliyun.com/product/Hologram) or the Usage notes section to view the ID of the region.
        self.region_id = region_id  # type: str
        # The resource group. If you do not specify this parameter, the default resource group of the account is used.
        self.resource_group_id = resource_group_id  # type: str
        # The standard storage space of the instance. Unit: GB.
        # 
        # > This parameter is invalid for pay-as-you-go instances.
        self.storage_size = storage_size  # type: long
        # The ID of the vSwitch. The zone in which the vSwitch resides must be the same as the zone in which the instance resides.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the virtual private cloud (VPC). The region in which the VPC resides must be the same as the region in which the Hologres instance resides.
        self.vpc_id = vpc_id  # type: str
        # The ID of the zone. For more information about how to obtain the ID of the zone, see the Usage notes section.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['autoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.cold_storage_size is not None:
            result['coldStorageSize'] = self.cold_storage_size
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.duration is not None:
            result['duration'] = self.duration
        if self.gateway_count is not None:
            result['gatewayCount'] = self.gateway_count
        if self.initial_databases is not None:
            result['initialDatabases'] = self.initial_databases
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.leader_instance_id is not None:
            result['leaderInstanceId'] = self.leader_instance_id
        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.storage_size is not None:
            result['storageSize'] = self.storage_size
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoPay') is not None:
            self.auto_pay = m.get('autoPay')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('coldStorageSize') is not None:
            self.cold_storage_size = m.get('coldStorageSize')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('gatewayCount') is not None:
            self.gateway_count = m.get('gatewayCount')
        if m.get('initialDatabases') is not None:
            self.initial_databases = m.get('initialDatabases')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('leaderInstanceId') is not None:
            self.leader_instance_id = m.get('leaderInstanceId')
        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class CreateInstanceResponseBodyData(TeaModel):
    def __init__(self, code=None, instance_id=None, message=None, order_id=None, success=None):
        # The error code returned.
        self.code = code  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The error details.
        self.message = message  # type: str
        # The order ID.
        self.order_id = order_id  # type: str
        # Indicates whether the instance was created.
        # 
        # *   true
        # *   false
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None):
        # The returned data.
        self.data = data  # type: CreateInstanceResponseBodyData
        # The error code returned.
        self.error_code = error_code  # type: str
        # The error message returned.
        self.error_message = error_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceResponse, self).to_map()
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(self, region_id=None):
        # The ID of the region in which the Hologres instance resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceRequest, self).to_map()
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


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 success=None):
        # The returned result, which indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data  # type: bool
        # The error code returned.
        self.error_code = error_code  # type: str
        # The error message returned.
        self.error_message = error_message  # type: str
        # The HTTP status Code
        self.http_status_code = http_status_code  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the call was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceResponse, self).to_map()
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyInstanceEndpoints(TeaModel):
    def __init__(self, alternative_endpoints=None, enabled=None, endpoint=None, type=None, v_switch_id=None,
                 vpc_id=None, vpc_instance_id=None):
        # The endpoint. This parameter is returned if both the AnyTunnel and SingleTunnel modes are enabled for an instance, and the instance is switched from the AnyTunnel mode to the SingleTunnel mode. In this case, two endpoints are returned.
        self.alternative_endpoints = alternative_endpoints  # type: str
        # Indicates whether the network is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enabled = enabled  # type: bool
        # The endpoint.
        self.endpoint = endpoint  # type: str
        # The network type.
        # 
        # Valid values:
        # 
        # *   VPCSingleTunnel
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     virtual private cloud (VPC)
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Intranet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     internal network
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   VPCAnyTunnel
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     not supported by new instances
        # 
        #     <!-- -->
        # 
        # *   Internet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Internet
        # 
        #     <!-- -->
        # 
        #     .
        self.type = type  # type: str
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The VPC ID.
        self.vpc_id = vpc_id  # type: str
        # The ID of VPC to which the instance belongs.
        self.vpc_instance_id = vpc_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstanceEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alternative_endpoints is not None:
            result['AlternativeEndpoints'] = self.alternative_endpoints
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlternativeEndpoints') is not None:
            self.alternative_endpoints = m.get('AlternativeEndpoints')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class GetInstanceResponseBodyInstanceTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstanceTags, self).to_map()
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


class GetInstanceResponseBodyInstance(TeaModel):
    def __init__(self, auto_renewal=None, cold_storage=None, commodity_code=None, compute_node_count=None, cpu=None,
                 creation_time=None, disk=None, enable_hive_access=None, endpoints=None, expiration_time=None, gateway_count=None,
                 gateway_cpu=None, gateway_memory=None, instance_charge_type=None, instance_id=None, instance_name=None,
                 instance_owner=None, instance_status=None, instance_type=None, leader_instance_id=None, memory=None,
                 region_id=None, resource_group_id=None, suspend_reason=None, tags=None, version=None, zone_id=None):
        # Indicates whether auto-renewal is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.auto_renewal = auto_renewal  # type: str
        # The cold storage capacity of the instance. Unit: GB. Standard SSD is used for hot storage, and HDD is used for cold storage.
        self.cold_storage = cold_storage  # type: long
        # The commodity code.
        # 
        # Valid values:
        # 
        # *   hologram_maxcomputeAccelerate_public_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Lakehouse Acceleration Edition
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_combo_public_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Subscription
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_prepay_public_intl
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     International site/Subscription
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_storage_dp_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Storage plan
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_postpay_public_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Pay-as-you-go
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_postpay_public_intl
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     International site/Pay-as-you-go
        # 
        #     <!-- -->
        # 
        # *   hologram_maxcomputeAccelerate_public_intl
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     International site/Lakehouse Acceleration Edition
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   hologram_cu_dp_cn
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     China site/Compute plan
        # 
        #     <!-- -->
        self.commodity_code = commodity_code  # type: str
        # The number of compute nodes. In a typical configuration, a node has 16 vCPUs and 32 GB of memory.
        self.compute_node_count = compute_node_count  # type: long
        # The number of vCPUs.
        self.cpu = cpu  # type: long
        # The creation time.
        self.creation_time = creation_time  # type: str
        # The amount of data that can be stored in the disk of the Standard storage class. Unit: GB.
        self.disk = disk  # type: str
        # Indicates whether data lake acceleration is enabled.
        self.enable_hive_access = enable_hive_access  # type: str
        # The list of endpoints.
        self.endpoints = endpoints  # type: list[GetInstanceResponseBodyInstanceEndpoints]
        # The expiration time. This parameter is invalid for pay-as-you-go instances.
        self.expiration_time = expiration_time  # type: str
        # 网关节点数量。
        self.gateway_count = gateway_count  # type: long
        # 网关cpu资源。
        # 单位：core。
        self.gateway_cpu = gateway_cpu  # type: long
        # 网关内存资源。
        # 单位：GB。
        self.gateway_memory = gateway_memory  # type: long
        # The billing method of the instance.
        # 
        # Valid values:
        # 
        # *   PostPaid
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     pay-as-you-go
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   PrePaid
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     subscription
        # 
        #     <!-- -->
        # 
        #     .
        self.instance_charge_type = instance_charge_type  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The instance name. The instance name must be 2 to 64 characters in length.
        self.instance_name = instance_name  # type: str
        # The owner of the instance.
        self.instance_owner = instance_owner  # type: str
        # The status of the instance.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Suspended
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Allocating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.instance_status = instance_status  # type: str
        # The type of the instance.
        # 
        # Valid values:
        # 
        # *   Follower
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     read-only secondary instance
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Standard
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     normal instance
        # 
        #     <!-- -->
        # 
        #     .
        self.instance_type = instance_type  # type: str
        # The ID of the primary instance.
        self.leader_instance_id = leader_instance_id  # type: str
        # The memory size. Unit: GB.
        self.memory = memory  # type: long
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The reason for the suspension.
        self.suspend_reason = suspend_reason  # type: str
        # The instance tag.
        self.tags = tags  # type: list[GetInstanceResponseBodyInstanceTags]
        # The instance version.
        self.version = version  # type: str
        # The ID of the zone where the instance resides.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.compute_node_count is not None:
            result['ComputeNodeCount'] = self.compute_node_count
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.enable_hive_access is not None:
            result['EnableHiveAccess'] = self.enable_hive_access
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time
        if self.gateway_count is not None:
            result['GatewayCount'] = self.gateway_count
        if self.gateway_cpu is not None:
            result['GatewayCpu'] = self.gateway_cpu
        if self.gateway_memory is not None:
            result['GatewayMemory'] = self.gateway_memory
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_owner is not None:
            result['InstanceOwner'] = self.instance_owner
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.leader_instance_id is not None:
            result['LeaderInstanceId'] = self.leader_instance_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.suspend_reason is not None:
            result['SuspendReason'] = self.suspend_reason
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ComputeNodeCount') is not None:
            self.compute_node_count = m.get('ComputeNodeCount')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('EnableHiveAccess') is not None:
            self.enable_hive_access = m.get('EnableHiveAccess')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = GetInstanceResponseBodyInstanceEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')
        if m.get('GatewayCount') is not None:
            self.gateway_count = m.get('GatewayCount')
        if m.get('GatewayCpu') is not None:
            self.gateway_cpu = m.get('GatewayCpu')
        if m.get('GatewayMemory') is not None:
            self.gateway_memory = m.get('GatewayMemory')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceOwner') is not None:
            self.instance_owner = m.get('InstanceOwner')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LeaderInstanceId') is not None:
            self.leader_instance_id = m.get('LeaderInstanceId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SuspendReason') is not None:
            self.suspend_reason = m.get('SuspendReason')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetInstanceResponseBodyInstanceTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, instance=None, request_id=None,
                 success=None):
        # The error code returned if the request failed.
        self.error_code = error_code  # type: str
        # The error message returned if the request failed.
        self.error_message = error_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: str
        # The details of the instance.
        self.instance = instance  # type: GetInstanceResponseBodyInstance
        # The request ID.
        self.request_id = request_id  # type: str
        # The request result, which indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Instance') is not None:
            temp_model = GetInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceResponse, self).to_map()
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, cms_instance_type=None, resource_group_id=None, tag=None):
        self.cms_instance_type = cms_instance_type  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags to add to the resource.
        self.tag = tag  # type: list[ListInstancesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cms_instance_type is not None:
            result['cmsInstanceType'] = self.cms_instance_type
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cmsInstanceType') is not None:
            self.cms_instance_type = m.get('cmsInstanceType')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListInstancesResponseBodyInstanceListEndpoints(TeaModel):
    def __init__(self, enabled=None, endpoint=None, type=None, v_switch_id=None, vpc_id=None, vpc_instance_id=None):
        # Indicates whether the endpoint is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enabled = enabled  # type: bool
        # The endpoint.
        self.endpoint = endpoint  # type: str
        # The network type.
        # 
        # Valid values:
        # 
        # *   VPCSingleTunnel
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     virtual private cloud (VPC)
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Intranet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     internal network
        # 
        #     <!-- -->
        # 
        # *   VPCAnyTunnel
        # 
        #     <!-- -->
        # 
        #     : This value is not supported by new instances
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Internet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Internet
        # 
        #     <!-- -->
        # 
        #     .
        self.type = type  # type: str
        # The vSwitch ID.
        self.v_switch_id = v_switch_id  # type: str
        # The VPC ID.
        self.vpc_id = vpc_id  # type: str
        # The ID of the VPC to which the instance belongs.
        self.vpc_instance_id = vpc_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstanceListEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class ListInstancesResponseBodyInstanceListTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstanceListTags, self).to_map()
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


class ListInstancesResponseBodyInstanceList(TeaModel):
    def __init__(self, commodity_code=None, creation_time=None, enable_hive_access=None, endpoints=None,
                 expiration_time=None, instance_charge_type=None, instance_id=None, instance_name=None, instance_status=None,
                 instance_type=None, leader_instance_id=None, region_id=None, resource_group_id=None, suspend_reason=None,
                 tags=None, version=None, zone_id=None):
        # The commodity code, which is the same as that on the Billing Management page.
        self.commodity_code = commodity_code  # type: str
        # The time when the cluster was created.
        self.creation_time = creation_time  # type: str
        # Indicates whether lakehouse acceleration is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable_hive_access = enable_hive_access  # type: str
        # The list of endpoints.
        self.endpoints = endpoints  # type: list[ListInstancesResponseBodyInstanceListEndpoints]
        # The time when the cluster expires.
        self.expiration_time = expiration_time  # type: str
        # The billing method of the instance. Valid values:
        # 
        # Valid values:
        # 
        # *   PostPaid
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     pay-as-you-go
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   PrePaid
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     subscription
        # 
        #     <!-- -->
        # 
        #     .
        self.instance_charge_type = instance_charge_type  # type: str
        # The instance ID.
        self.instance_id = instance_id  # type: str
        # The name of the instance.
        self.instance_name = instance_name  # type: str
        # The status of the instance.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Suspended
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Allocating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.instance_status = instance_status  # type: str
        # The type of the instance.
        # 
        # Valid values:
        # 
        # *   Follower
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     read-only secondary instance
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Standard
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     normal instance
        # 
        #     <!-- -->
        # 
        #     .
        self.instance_type = instance_type  # type: str
        # The ID of the primary instance.
        self.leader_instance_id = leader_instance_id  # type: str
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The reason for the suspension.
        self.suspend_reason = suspend_reason  # type: str
        # The tags that are added to the resource.
        self.tags = tags  # type: list[ListInstancesResponseBodyInstanceListTags]
        # The version of the cluster.
        self.version = version  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstanceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.enable_hive_access is not None:
            result['EnableHiveAccess'] = self.enable_hive_access
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.leader_instance_id is not None:
            result['LeaderInstanceId'] = self.leader_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.suspend_reason is not None:
            result['SuspendReason'] = self.suspend_reason
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EnableHiveAccess') is not None:
            self.enable_hive_access = m.get('EnableHiveAccess')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = ListInstancesResponseBodyInstanceListEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LeaderInstanceId') is not None:
            self.leader_instance_id = m.get('LeaderInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SuspendReason') is not None:
            self.suspend_reason = m.get('SuspendReason')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListInstancesResponseBodyInstanceListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_status_code=None, instance_list=None,
                 request_id=None, success=None):
        # The error code returned if the request failed.
        self.error_code = error_code  # type: str
        # The error message returned if the request failed.
        self.error_message = error_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: str
        # The list of queried instances.
        self.instance_list = instance_list  # type: list[ListInstancesResponseBodyInstanceList]
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        self.success = success  # type: str

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = ListInstancesResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancesResponse, self).to_map()
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, auto_renew=None, duration=None):
        # Specifies whether to enable monthly auto-renewal. The default value is false. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  If you enable auto-renewal for an instance for which auto-renewal is enabled, an error is reported.
        self.auto_renew = auto_renew  # type: bool
        # The renewal duration. Unit: month.
        self.duration = duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.duration is not None:
            result['duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        return self


class RenewInstanceResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None, order_id=None, success=None):
        # The error code returned.
        self.code = code  # type: str
        # The error details.
        self.message = message  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: str
        # Indicates whether the renewal was successful.
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 success=None):
        # The returned data.
        self.data = data  # type: RenewInstanceResponseBodyData
        # The error code returned.
        self.error_code = error_code  # type: str
        # The error message returned.
        self.error_message = error_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The request result, which indicates whether the request was successful.
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RenewInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RenewInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewInstanceResponse, self).to_map()
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstanceResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 success=None):
        # Indicates whether the operation was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data  # type: bool
        # The error code returned if the request failed.
        self.error_code = error_code  # type: str
        # The error message returned if the request failed.
        self.error_message = error_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The request result, which indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartInstanceResponse, self).to_map()
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
            temp_model = RestartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeInstanceResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 success=None):
        # The returned result, which indicates whether the operation was successful.
        self.data = data  # type: bool
        # The error code returned if the request failed.
        self.error_code = error_code  # type: str
        # The error message returned if the request failed.
        self.error_message = error_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The request result, which indicates whether the request was successful.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResumeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeInstanceResponse, self).to_map()
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
            temp_model = ResumeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleInstanceRequest(TeaModel):
    def __init__(self, cold_storage_size=None, cpu=None, gateway_count=None, scale_type=None, storage_size=None):
        # The infrequent access (IA) storage space of the instance. Unit: GB.
        # 
        # > This parameter is invalid for pay-as-you-go instances.
        self.cold_storage_size = cold_storage_size  # type: long
        # The specifications of the instance. Valid values:
        # 
        # *   8-core 32 GB (number of compute Nodes: 1)
        # *   16-core 64 GB (number of compute nodes: 1)
        # *   32-core 128 GB (number of compute nodes: 2)
        # *   64-core 256 GB (number of compute nodes: 4)
        # *   96-core 384 GB (number of compute nodes: 6)
        # *   128-core 512 GB (number of compute nodes: 8)
        # *   Others
        # 
        # > 
        # 
        # *   Set this parameter to the number of cores.
        # 
        # *   If you want to set this parameter to specifications with more than 1,024 compute units (CUs), you must submit a ticket.
        # 
        # *   This parameter is invalid for shared instances.
        # 
        # *   The specifications of 8-core 32 GB (number of compute nodes: 1) are for trial use only and cannot be used for production.
        self.cpu = cpu  # type: long
        self.gateway_count = gateway_count  # type: long
        # The specification change type. Valid values:
        # 
        # *   UPGRADE
        # *   DOWNGRADE
        # 
        # > 
        # 
        # *   If you set this parameter to UPGRADE, the new specifications must be higher than the original specifications. You must configure at least one of the cpu, storageSize, and coldStorageSize parameters. If you leave a parameter empty, the related configuration remains unchanged.
        # 
        # *   If you set this parameter to DOWNGRADE, the new specifications must be lower than the original specifications. You must configure at least one of the cpu, storageSize, and coldStorageSize parameters. If you leave a parameter empty, the related configuration remains unchanged.
        self.scale_type = scale_type  # type: str
        # The standard storage space of the instance. Unit: GB.
        # 
        # > This parameter is invalid for pay-as-you-go instances.
        self.storage_size = storage_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cold_storage_size is not None:
            result['coldStorageSize'] = self.cold_storage_size
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.gateway_count is not None:
            result['gatewayCount'] = self.gateway_count
        if self.scale_type is not None:
            result['scaleType'] = self.scale_type
        if self.storage_size is not None:
            result['storageSize'] = self.storage_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('coldStorageSize') is not None:
            self.cold_storage_size = m.get('coldStorageSize')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('gatewayCount') is not None:
            self.gateway_count = m.get('gatewayCount')
        if m.get('scaleType') is not None:
            self.scale_type = m.get('scaleType')
        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')
        return self


class ScaleInstanceResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None, order_id=None, success=None):
        # The error code returned.
        self.code = code  # type: str
        # The error details.
        self.message = message  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: str
        # Indicates whether the change to specifications was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScaleInstanceResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None):
        # The returned data.
        self.data = data  # type: ScaleInstanceResponseBodyData
        # The error code returned.
        self.error_code = error_code  # type: str
        # The error message returned.
        self.error_message = error_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ScaleInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ScaleInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ScaleInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ScaleInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScaleInstanceResponse, self).to_map()
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
            temp_model = ScaleInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 success=None):
        # The returned result, which indicates whether the operation was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data  # type: bool
        # The error code returned if the request failed.
        self.error_code = error_code  # type: str
        # The error message returned if the request failed.
        self.error_message = error_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The request result, which indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopInstanceResponse, self).to_map()
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceNameRequest(TeaModel):
    def __init__(self, instance_name=None):
        # The new name of the instance.
        self.instance_name = instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        return self


class UpdateInstanceNameResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 success=None):
        # The returned result, which indicates whether the operation was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data  # type: bool
        # The error code returned if the request failed.
        self.error_code = error_code  # type: str
        # The error message returned if the request failed.
        self.error_message = error_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The request result, which indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceNameResponse, self).to_map()
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
            temp_model = UpdateInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceNetworkTypeRequest(TeaModel):
    def __init__(self, any_tunnel_to_single_tunnel=None, network_types=None, v_switch_id=None, vpc_id=None,
                 vpc_owner_id=None, vpc_region_id=None):
        # Specifies whether to change the network type from AnyTunnel to SingleTunnel. This parameter is invalid for new instances. For new instances, this parameter is set to null by default.
        # 
        # Valid values:
        # 
        # *   others/null
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.any_tunnel_to_single_tunnel = any_tunnel_to_single_tunnel  # type: str
        # A list of network types that you want to enable. The list of enabled network types is randomly ordered. For example, the Internet, internal network, and VPCSingleTunnel network types are enabled. If you want to disable the Internet type, set this parameter to Intranet,VPCSingleTunnel.
        self.network_types = network_types  # type: str
        # The vSwitch ID.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the VPC to which the instance belongs.
        self.vpc_id = vpc_id  # type: str
        # The owner ID of the VPC, which is the ID of the Alibaba Cloud account.
        self.vpc_owner_id = vpc_owner_id  # type: str
        # The region ID of the VPC.
        self.vpc_region_id = vpc_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceNetworkTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.any_tunnel_to_single_tunnel is not None:
            result['anyTunnelToSingleTunnel'] = self.any_tunnel_to_single_tunnel
        if self.network_types is not None:
            result['networkTypes'] = self.network_types
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_owner_id is not None:
            result['vpcOwnerId'] = self.vpc_owner_id
        if self.vpc_region_id is not None:
            result['vpcRegionId'] = self.vpc_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('anyTunnelToSingleTunnel') is not None:
            self.any_tunnel_to_single_tunnel = m.get('anyTunnelToSingleTunnel')
        if m.get('networkTypes') is not None:
            self.network_types = m.get('networkTypes')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcOwnerId') is not None:
            self.vpc_owner_id = m.get('vpcOwnerId')
        if m.get('vpcRegionId') is not None:
            self.vpc_region_id = m.get('vpcRegionId')
        return self


class UpdateInstanceNetworkTypeResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_status_code=None, request_id=None,
                 success=None):
        # The returned result, which indicates whether the operation was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.data = data  # type: str
        # The error code returned if the request failed.
        self.error_code = error_code  # type: str
        # The error message returned if the request failed.
        self.error_message = error_message  # type: str
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceNetworkTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceNetworkTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceNetworkTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceNetworkTypeResponse, self).to_map()
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
            temp_model = UpdateInstanceNetworkTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


