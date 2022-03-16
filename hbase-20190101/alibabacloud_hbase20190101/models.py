# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddUserHdfsInfoRequest(TeaModel):
    def __init__(self, client_token=None, cluster_id=None, ext_info=None):
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.ext_info = ext_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserHdfsInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class AddUserHdfsInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserHdfsInfoResponseBody, self).to_map()
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


class AddUserHdfsInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUserHdfsInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserHdfsInfoResponse, self).to_map()
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
            temp_model = AddUserHdfsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocatePublicNetworkAddressRequest(TeaModel):
    def __init__(self, client_token=None, cluster_id=None):
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocatePublicNetworkAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class AllocatePublicNetworkAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocatePublicNetworkAddressResponseBody, self).to_map()
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


class AllocatePublicNetworkAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AllocatePublicNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllocatePublicNetworkAddressResponse, self).to_map()
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
            temp_model = AllocatePublicNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckComponentsVersionRequest(TeaModel):
    def __init__(self, cluster_id=None, components=None):
        self.cluster_id = cluster_id  # type: str
        self.components = components  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckComponentsVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.components is not None:
            result['Components'] = self.components
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        return self


class CheckComponentsVersionResponseBodyComponentsComponent(TeaModel):
    def __init__(self, component=None, is_latest_version=None):
        self.component = component  # type: str
        self.is_latest_version = is_latest_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckComponentsVersionResponseBodyComponentsComponent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component is not None:
            result['Component'] = self.component
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Component') is not None:
            self.component = m.get('Component')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        return self


class CheckComponentsVersionResponseBodyComponents(TeaModel):
    def __init__(self, component=None):
        self.component = component  # type: list[CheckComponentsVersionResponseBodyComponentsComponent]

    def validate(self):
        if self.component:
            for k in self.component:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CheckComponentsVersionResponseBodyComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Component'] = []
        if self.component is not None:
            for k in self.component:
                result['Component'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.component = []
        if m.get('Component') is not None:
            for k in m.get('Component'):
                temp_model = CheckComponentsVersionResponseBodyComponentsComponent()
                self.component.append(temp_model.from_map(k))
        return self


class CheckComponentsVersionResponseBody(TeaModel):
    def __init__(self, components=None, request_id=None):
        self.components = components  # type: CheckComponentsVersionResponseBodyComponents
        self.request_id = request_id  # type: str

    def validate(self):
        if self.components:
            self.components.validate()

    def to_map(self):
        _map = super(CheckComponentsVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.components is not None:
            result['Components'] = self.components.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Components') is not None:
            temp_model = CheckComponentsVersionResponseBodyComponents()
            self.components = temp_model.from_map(m['Components'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckComponentsVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckComponentsVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckComponentsVersionResponse, self).to_map()
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
            temp_model = CheckComponentsVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseBackupRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseBackupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class CloseBackupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseBackupResponseBody, self).to_map()
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


class CloseBackupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloseBackupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseBackupResponse, self).to_map()
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
            temp_model = CloseBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None, duration=None, pay_type=None, pricing_cycle=None):
        self.cluster_id = cluster_id  # type: str
        self.duration = duration  # type: int
        self.pay_type = pay_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class ConvertInstanceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertInstanceResponseBody, self).to_map()
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


class ConvertInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConvertInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConvertInstanceResponse, self).to_map()
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
            temp_model = ConvertInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupPlanRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class CreateBackupPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupPlanResponseBody, self).to_map()
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


class CreateBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateBackupPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBackupPlanResponse, self).to_map()
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
            temp_model = CreateBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, auto_renew_period=None, client_token=None, cluster_name=None, cold_storage_size=None,
                 core_instance_type=None, disk_size=None, disk_type=None, encryption_key=None, engine=None, engine_version=None,
                 master_instance_type=None, node_count=None, pay_type=None, period=None, period_unit=None, region_id=None,
                 resource_group_id=None, security_iplist=None, v_switch_id=None, vpc_id=None, zone_id=None):
        self.auto_renew_period = auto_renew_period  # type: int
        self.client_token = client_token  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cold_storage_size = cold_storage_size  # type: int
        self.core_instance_type = core_instance_type  # type: str
        self.disk_size = disk_size  # type: int
        self.disk_type = disk_type  # type: str
        self.encryption_key = encryption_key  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.master_instance_type = master_instance_type  # type: str
        self.node_count = node_count  # type: int
        self.pay_type = pay_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.security_iplist = security_iplist  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, order_id=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterResponse, self).to_map()
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGlobalResourceRequest(TeaModel):
    def __init__(self, client_token=None, cluster_id=None, resource_name=None, resource_type=None):
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGlobalResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateGlobalResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGlobalResourceResponseBody, self).to_map()
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


class CreateGlobalResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGlobalResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGlobalResourceResponse, self).to_map()
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
            temp_model = CreateGlobalResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHBaseSlbServerRequest(TeaModel):
    def __init__(self, client_token=None, cluster_id=None, slb_server=None):
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.slb_server = slb_server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHBaseSlbServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.slb_server is not None:
            result['SlbServer'] = self.slb_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SlbServer') is not None:
            self.slb_server = m.get('SlbServer')
        return self


class CreateHBaseSlbServerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHBaseSlbServerResponseBody, self).to_map()
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


class CreateHBaseSlbServerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateHBaseSlbServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHBaseSlbServerResponse, self).to_map()
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
            temp_model = CreateHBaseSlbServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHbaseHaSlbRequest(TeaModel):
    def __init__(self, bds_id=None, client_token=None, ha_id=None, ha_types=None, hbase_type=None):
        self.bds_id = bds_id  # type: str
        self.client_token = client_token  # type: str
        self.ha_id = ha_id  # type: str
        self.ha_types = ha_types  # type: str
        self.hbase_type = hbase_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHbaseHaSlbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ha_id is not None:
            result['HaId'] = self.ha_id
        if self.ha_types is not None:
            result['HaTypes'] = self.ha_types
        if self.hbase_type is not None:
            result['HbaseType'] = self.hbase_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('HaId') is not None:
            self.ha_id = m.get('HaId')
        if m.get('HaTypes') is not None:
            self.ha_types = m.get('HaTypes')
        if m.get('HbaseType') is not None:
            self.hbase_type = m.get('HbaseType')
        return self


class CreateHbaseHaSlbResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHbaseHaSlbResponseBody, self).to_map()
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


class CreateHbaseHaSlbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateHbaseHaSlbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHbaseHaSlbResponse, self).to_map()
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
            temp_model = CreateHbaseHaSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMultiZoneClusterRequest(TeaModel):
    def __init__(self, arbiter_vswitch_id=None, arbiter_zone_id=None, arch_version=None, auto_renew_period=None,
                 client_token=None, cluster_name=None, core_disk_size=None, core_disk_type=None, core_instance_type=None,
                 core_node_count=None, engine=None, engine_version=None, log_disk_size=None, log_disk_type=None,
                 log_instance_type=None, log_node_count=None, master_instance_type=None, multi_zone_combination=None, pay_type=None,
                 period=None, period_unit=None, primary_vswitch_id=None, primary_zone_id=None, region_id=None,
                 resource_group_id=None, security_iplist=None, standby_vswitch_id=None, standby_zone_id=None, vpc_id=None):
        self.arbiter_vswitch_id = arbiter_vswitch_id  # type: str
        self.arbiter_zone_id = arbiter_zone_id  # type: str
        self.arch_version = arch_version  # type: str
        self.auto_renew_period = auto_renew_period  # type: int
        self.client_token = client_token  # type: str
        self.cluster_name = cluster_name  # type: str
        self.core_disk_size = core_disk_size  # type: int
        self.core_disk_type = core_disk_type  # type: str
        self.core_instance_type = core_instance_type  # type: str
        self.core_node_count = core_node_count  # type: int
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.log_disk_size = log_disk_size  # type: int
        self.log_disk_type = log_disk_type  # type: str
        self.log_instance_type = log_instance_type  # type: str
        self.log_node_count = log_node_count  # type: int
        self.master_instance_type = master_instance_type  # type: str
        self.multi_zone_combination = multi_zone_combination  # type: str
        self.pay_type = pay_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.primary_vswitch_id = primary_vswitch_id  # type: str
        self.primary_zone_id = primary_zone_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.security_iplist = security_iplist  # type: str
        self.standby_vswitch_id = standby_vswitch_id  # type: str
        self.standby_zone_id = standby_zone_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMultiZoneClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size
        if self.log_disk_type is not None:
            result['LogDiskType'] = self.log_disk_type
        if self.log_instance_type is not None:
            result['LogInstanceType'] = self.log_instance_type
        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')
        if m.get('LogDiskType') is not None:
            self.log_disk_type = m.get('LogDiskType')
        if m.get('LogInstanceType') is not None:
            self.log_instance_type = m.get('LogInstanceType')
        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateMultiZoneClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, order_id=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMultiZoneClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMultiZoneClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateMultiZoneClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMultiZoneClusterResponse, self).to_map()
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
            temp_model = CreateMultiZoneClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRestorePlanRequest(TeaModel):
    def __init__(self, cluster_id=None, restore_all_table=None, restore_by_copy=None, restore_to_date=None,
                 tables=None, target_cluster_id=None):
        self.cluster_id = cluster_id  # type: str
        self.restore_all_table = restore_all_table  # type: bool
        self.restore_by_copy = restore_by_copy  # type: bool
        self.restore_to_date = restore_to_date  # type: str
        self.tables = tables  # type: str
        self.target_cluster_id = target_cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRestorePlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.restore_all_table is not None:
            result['RestoreAllTable'] = self.restore_all_table
        if self.restore_by_copy is not None:
            result['RestoreByCopy'] = self.restore_by_copy
        if self.restore_to_date is not None:
            result['RestoreToDate'] = self.restore_to_date
        if self.tables is not None:
            result['Tables'] = self.tables
        if self.target_cluster_id is not None:
            result['TargetClusterId'] = self.target_cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RestoreAllTable') is not None:
            self.restore_all_table = m.get('RestoreAllTable')
        if m.get('RestoreByCopy') is not None:
            self.restore_by_copy = m.get('RestoreByCopy')
        if m.get('RestoreToDate') is not None:
            self.restore_to_date = m.get('RestoreToDate')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        if m.get('TargetClusterId') is not None:
            self.target_cluster_id = m.get('TargetClusterId')
        return self


class CreateRestorePlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRestorePlanResponseBody, self).to_map()
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


class CreateRestorePlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRestorePlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRestorePlanResponse, self).to_map()
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
            temp_model = CreateRestorePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServerlessClusterRequest(TeaModel):
    def __init__(self, auto_renew_period=None, client_token=None, client_type=None, cluster_name=None,
                 disk_type=None, engine=None, engine_version=None, pay_type=None, period=None, period_unit=None,
                 region_id=None, resource_group_id=None, serverless_capability=None, serverless_spec=None,
                 serverless_storage=None, v_switch_id=None, vpc_id=None, zone_id=None):
        self.auto_renew_period = auto_renew_period  # type: int
        self.client_token = client_token  # type: str
        self.client_type = client_type  # type: str
        self.cluster_name = cluster_name  # type: str
        self.disk_type = disk_type  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.pay_type = pay_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.serverless_capability = serverless_capability  # type: int
        self.serverless_spec = serverless_spec  # type: str
        self.serverless_storage = serverless_storage  # type: int
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServerlessClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.serverless_capability is not None:
            result['ServerlessCapability'] = self.serverless_capability
        if self.serverless_spec is not None:
            result['ServerlessSpec'] = self.serverless_spec
        if self.serverless_storage is not None:
            result['ServerlessStorage'] = self.serverless_storage
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServerlessCapability') is not None:
            self.serverless_capability = m.get('ServerlessCapability')
        if m.get('ServerlessSpec') is not None:
            self.serverless_spec = m.get('ServerlessSpec')
        if m.get('ServerlessStorage') is not None:
            self.serverless_storage = m.get('ServerlessStorage')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateServerlessClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, order_id=None, pass_word=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.order_id = order_id  # type: str
        self.pass_word = pass_word  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServerlessClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServerlessClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServerlessClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServerlessClusterResponse, self).to_map()
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
            temp_model = CreateServerlessClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGlobalResourceRequest(TeaModel):
    def __init__(self, cluster_id=None, resource_name=None, resource_type=None):
        self.cluster_id = cluster_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGlobalResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DeleteGlobalResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGlobalResourceResponseBody, self).to_map()
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


class DeleteGlobalResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGlobalResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGlobalResourceResponse, self).to_map()
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
            temp_model = DeleteGlobalResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHBaseHaDBRequest(TeaModel):
    def __init__(self, bds_id=None, ha_id=None):
        self.bds_id = bds_id  # type: str
        self.ha_id = ha_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHBaseHaDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        if self.ha_id is not None:
            result['HaId'] = self.ha_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        if m.get('HaId') is not None:
            self.ha_id = m.get('HaId')
        return self


class DeleteHBaseHaDBResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHBaseHaDBResponseBody, self).to_map()
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


class DeleteHBaseHaDBResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteHBaseHaDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHBaseHaDBResponse, self).to_map()
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
            temp_model = DeleteHBaseHaDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHBaseSlbServerRequest(TeaModel):
    def __init__(self, cluster_id=None, slb_server=None):
        self.cluster_id = cluster_id  # type: str
        self.slb_server = slb_server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHBaseSlbServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.slb_server is not None:
            result['SlbServer'] = self.slb_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SlbServer') is not None:
            self.slb_server = m.get('SlbServer')
        return self


class DeleteHBaseSlbServerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHBaseSlbServerResponseBody, self).to_map()
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


class DeleteHBaseSlbServerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteHBaseSlbServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHBaseSlbServerResponse, self).to_map()
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
            temp_model = DeleteHBaseSlbServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHbaseHaSlbRequest(TeaModel):
    def __init__(self, bds_id=None, ha_id=None, ha_types=None):
        self.bds_id = bds_id  # type: str
        self.ha_id = ha_id  # type: str
        self.ha_types = ha_types  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHbaseHaSlbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        if self.ha_id is not None:
            result['HaId'] = self.ha_id
        if self.ha_types is not None:
            result['HaTypes'] = self.ha_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        if m.get('HaId') is not None:
            self.ha_id = m.get('HaId')
        if m.get('HaTypes') is not None:
            self.ha_types = m.get('HaTypes')
        return self


class DeleteHbaseHaSlbResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHbaseHaSlbResponseBody, self).to_map()
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


class DeleteHbaseHaSlbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteHbaseHaSlbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHbaseHaSlbResponse, self).to_map()
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
            temp_model = DeleteHbaseHaSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None, immediate_delete_flag=None):
        self.cluster_id = cluster_id  # type: str
        self.immediate_delete_flag = immediate_delete_flag  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.immediate_delete_flag is not None:
            result['ImmediateDeleteFlag'] = self.immediate_delete_flag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImmediateDeleteFlag') is not None:
            self.immediate_delete_flag = m.get('ImmediateDeleteFlag')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
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


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMultiZoneClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, immediate_delete_flag=None):
        self.cluster_id = cluster_id  # type: str
        self.immediate_delete_flag = immediate_delete_flag  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMultiZoneClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.immediate_delete_flag is not None:
            result['ImmediateDeleteFlag'] = self.immediate_delete_flag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImmediateDeleteFlag') is not None:
            self.immediate_delete_flag = m.get('ImmediateDeleteFlag')
        return self


class DeleteMultiZoneClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMultiZoneClusterResponseBody, self).to_map()
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


class DeleteMultiZoneClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteMultiZoneClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMultiZoneClusterResponse, self).to_map()
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
            temp_model = DeleteMultiZoneClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServerlessClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None, zone_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServerlessClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DeleteServerlessClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServerlessClusterResponseBody, self).to_map()
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


class DeleteServerlessClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServerlessClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServerlessClusterResponse, self).to_map()
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
            temp_model = DeleteServerlessClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserHdfsInfoRequest(TeaModel):
    def __init__(self, cluster_id=None, name_service=None):
        self.cluster_id = cluster_id  # type: str
        self.name_service = name_service  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserHdfsInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name_service is not None:
            result['NameService'] = self.name_service
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NameService') is not None:
            self.name_service = m.get('NameService')
        return self


class DeleteUserHdfsInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserHdfsInfoResponseBody, self).to_map()
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


class DeleteUserHdfsInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserHdfsInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserHdfsInfoResponse, self).to_map()
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
            temp_model = DeleteUserHdfsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self, charge_type=None, core_instance_type=None, disk_type=None, engine=None, engine_version=None,
                 region_id=None, zone_id=None):
        self.charge_type = charge_type  # type: str
        self.core_instance_type = core_instance_type  # type: str
        self.disk_type = disk_type  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail(TeaModel):
    def __init__(self, cpu=None, mem=None):
        self.cpu = cpu  # type: int
        self.mem = mem  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource(TeaModel):
    def __init__(self, instance_type=None, instance_type_detail=None):
        self.instance_type = instance_type  # type: str
        self.instance_type_detail = instance_type_detail  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail

    def validate(self):
        if self.instance_type_detail:
            self.instance_type_detail.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_type_detail is not None:
            result['InstanceTypeDetail'] = self.instance_type_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceTypeDetail') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail()
            self.instance_type_detail = temp_model.from_map(m['InstanceTypeDetail'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources(TeaModel):
    def __init__(self, master_resource=None):
        self.master_resource = master_resource  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource]

    def validate(self):
        if self.master_resource:
            for k in self.master_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MasterResource'] = []
        if self.master_resource is not None:
            for k in self.master_resource:
                result['MasterResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.master_resource = []
        if m.get('MasterResource') is not None:
            for k in m.get('MasterResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource()
                self.master_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange(TeaModel):
    def __init__(self, max_size=None, min_size=None, step_size=None):
        self.max_size = max_size  # type: int
        self.min_size = min_size  # type: int
        self.step_size = step_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.step_size is not None:
            result['StepSize'] = self.step_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('StepSize') is not None:
            self.step_size = m.get('StepSize')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail(TeaModel):
    def __init__(self, cpu=None, mem=None):
        self.cpu = cpu  # type: int
        self.mem = mem  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource(TeaModel):
    def __init__(self, dbinstance_storage_range=None, instance_type=None, instance_type_detail=None,
                 max_core_count=None):
        self.dbinstance_storage_range = dbinstance_storage_range  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange
        self.instance_type = instance_type  # type: str
        self.instance_type_detail = instance_type_detail  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail
        self.max_core_count = max_core_count  # type: int

    def validate(self):
        if self.dbinstance_storage_range:
            self.dbinstance_storage_range.validate()
        if self.instance_type_detail:
            self.instance_type_detail.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_storage_range is not None:
            result['DBInstanceStorageRange'] = self.dbinstance_storage_range.to_map()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_type_detail is not None:
            result['InstanceTypeDetail'] = self.instance_type_detail.to_map()
        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceStorageRange') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange()
            self.dbinstance_storage_range = temp_model.from_map(m['DBInstanceStorageRange'])
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceTypeDetail') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail()
            self.instance_type_detail = temp_model.from_map(m['InstanceTypeDetail'])
        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources(TeaModel):
    def __init__(self, core_resource=None):
        self.core_resource = core_resource  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource]

    def validate(self):
        if self.core_resource:
            for k in self.core_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CoreResource'] = []
        if self.core_resource is not None:
            for k in self.core_resource:
                result['CoreResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.core_resource = []
        if m.get('CoreResource') is not None:
            for k in m.get('CoreResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource()
                self.core_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType(TeaModel):
    def __init__(self, core_resources=None, storage_type=None):
        self.core_resources = core_resources  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources
        self.storage_type = storage_type  # type: str

    def validate(self):
        if self.core_resources:
            self.core_resources.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_resources is not None:
            result['CoreResources'] = self.core_resources.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoreResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources()
            self.core_resources = temp_model.from_map(m['CoreResources'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes(TeaModel):
    def __init__(self, supported_storage_type=None):
        self.supported_storage_type = supported_storage_type  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType]

    def validate(self):
        if self.supported_storage_type:
            for k in self.supported_storage_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedStorageType'] = []
        if self.supported_storage_type is not None:
            for k in self.supported_storage_type:
                result['SupportedStorageType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_storage_type = []
        if m.get('SupportedStorageType') is not None:
            for k in m.get('SupportedStorageType'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType()
                self.supported_storage_type.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories(TeaModel):
    def __init__(self, category=None, supported_storage_types=None):
        self.category = category  # type: str
        self.supported_storage_types = supported_storage_types  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes

    def validate(self):
        if self.supported_storage_types:
            self.supported_storage_types.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.supported_storage_types is not None:
            result['SupportedStorageTypes'] = self.supported_storage_types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('SupportedStorageTypes') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes()
            self.supported_storage_types = temp_model.from_map(m['SupportedStorageTypes'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories(TeaModel):
    def __init__(self, supported_categories=None):
        self.supported_categories = supported_categories  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories]

    def validate(self):
        if self.supported_categories:
            for k in self.supported_categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedCategories'] = []
        if self.supported_categories is not None:
            for k in self.supported_categories:
                result['SupportedCategories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_categories = []
        if m.get('SupportedCategories') is not None:
            for k in m.get('SupportedCategories'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories()
                self.supported_categories.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion(TeaModel):
    def __init__(self, supported_categories=None, version=None):
        self.supported_categories = supported_categories  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories
        self.version = version  # type: str

    def validate(self):
        if self.supported_categories:
            self.supported_categories.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_categories is not None:
            result['SupportedCategories'] = self.supported_categories.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedCategories') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories()
            self.supported_categories = temp_model.from_map(m['SupportedCategories'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions(TeaModel):
    def __init__(self, supported_engine_version=None):
        self.supported_engine_version = supported_engine_version  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion]

    def validate(self):
        if self.supported_engine_version:
            for k in self.supported_engine_version:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedEngineVersion'] = []
        if self.supported_engine_version is not None:
            for k in self.supported_engine_version:
                result['SupportedEngineVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_engine_version = []
        if m.get('SupportedEngineVersion') is not None:
            for k in m.get('SupportedEngineVersion'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion()
                self.supported_engine_version.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine(TeaModel):
    def __init__(self, engine=None, supported_engine_versions=None):
        self.engine = engine  # type: str
        self.supported_engine_versions = supported_engine_versions  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions

    def validate(self):
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.supported_engine_versions is not None:
            result['SupportedEngineVersions'] = self.supported_engine_versions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('SupportedEngineVersions') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions()
            self.supported_engine_versions = temp_model.from_map(m['SupportedEngineVersions'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines(TeaModel):
    def __init__(self, supported_engine=None):
        self.supported_engine = supported_engine  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine]

    def validate(self):
        if self.supported_engine:
            for k in self.supported_engine:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedEngine'] = []
        if self.supported_engine is not None:
            for k in self.supported_engine:
                result['SupportedEngine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_engine = []
        if m.get('SupportedEngine') is not None:
            for k in m.get('SupportedEngine'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine()
                self.supported_engine.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone(TeaModel):
    def __init__(self, master_resources=None, region_id=None, supported_engines=None, zone_id=None):
        self.master_resources = master_resources  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources
        self.region_id = region_id  # type: str
        self.supported_engines = supported_engines  # type: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.master_resources:
            self.master_resources.validate()
        if self.supported_engines:
            self.supported_engines.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.master_resources is not None:
            result['MasterResources'] = self.master_resources.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.supported_engines is not None:
            result['SupportedEngines'] = self.supported_engines.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MasterResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources()
            self.master_resources = temp_model.from_map(m['MasterResources'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupportedEngines') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines()
            self.supported_engines = temp_model.from_map(m['SupportedEngines'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZones(TeaModel):
    def __init__(self, available_zone=None):
        self.available_zone = available_zone  # type: list[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone]

    def validate(self):
        if self.available_zone:
            for k in self.available_zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBodyAvailableZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k in self.available_zone:
                result['AvailableZone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_zone = []
        if m.get('AvailableZone') is not None:
            for k in m.get('AvailableZone'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(self, available_zones=None, request_id=None):
        self.available_zones = available_zones  # type: DescribeAvailableResourceResponseBodyAvailableZones
        self.request_id = request_id  # type: str

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZones()
            self.available_zones = temp_model.from_map(m['AvailableZones'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAvailableResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAvailableResourceResponse, self).to_map()
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
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlanConfigRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlanConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeBackupPlanConfigResponseBodyTables(TeaModel):
    def __init__(self, table=None):
        self.table = table  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlanConfigResponseBodyTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeBackupPlanConfigResponseBody(TeaModel):
    def __init__(self, full_backup_cycle=None, min_hfile_backup_count=None, next_full_backup_date=None,
                 request_id=None, tables=None):
        self.full_backup_cycle = full_backup_cycle  # type: int
        self.min_hfile_backup_count = min_hfile_backup_count  # type: int
        self.next_full_backup_date = next_full_backup_date  # type: str
        self.request_id = request_id  # type: str
        self.tables = tables  # type: DescribeBackupPlanConfigResponseBodyTables

    def validate(self):
        if self.tables:
            self.tables.validate()

    def to_map(self):
        _map = super(DescribeBackupPlanConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_backup_cycle is not None:
            result['FullBackupCycle'] = self.full_backup_cycle
        if self.min_hfile_backup_count is not None:
            result['MinHFileBackupCount'] = self.min_hfile_backup_count
        if self.next_full_backup_date is not None:
            result['NextFullBackupDate'] = self.next_full_backup_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tables is not None:
            result['Tables'] = self.tables.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FullBackupCycle') is not None:
            self.full_backup_cycle = m.get('FullBackupCycle')
        if m.get('MinHFileBackupCount') is not None:
            self.min_hfile_backup_count = m.get('MinHFileBackupCount')
        if m.get('NextFullBackupDate') is not None:
            self.next_full_backup_date = m.get('NextFullBackupDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tables') is not None:
            temp_model = DescribeBackupPlanConfigResponseBodyTables()
            self.tables = temp_model.from_map(m['Tables'])
        return self


class DescribeBackupPlanConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupPlanConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupPlanConfigResponse, self).to_map()
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
            temp_model = DescribeBackupPlanConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(self, backup_retention_period=None, preferred_backup_end_time_utc=None,
                 preferred_backup_period=None, preferred_backup_start_time_utc=None, preferred_backup_time=None, request_id=None):
        self.backup_retention_period = backup_retention_period  # type: str
        self.preferred_backup_end_time_utc = preferred_backup_end_time_utc  # type: str
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_backup_start_time_utc = preferred_backup_start_time_utc  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.preferred_backup_end_time_utc is not None:
            result['PreferredBackupEndTimeUTC'] = self.preferred_backup_end_time_utc
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_start_time_utc is not None:
            result['PreferredBackupStartTimeUTC'] = self.preferred_backup_start_time_utc
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('PreferredBackupEndTimeUTC') is not None:
            self.preferred_backup_end_time_utc = m.get('PreferredBackupEndTimeUTC')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupStartTimeUTC') is not None:
            self.preferred_backup_start_time_utc = m.get('PreferredBackupStartTimeUTC')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupPolicyResponse, self).to_map()
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
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupStatusRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeBackupStatusResponseBody(TeaModel):
    def __init__(self, backup_status=None, bds_cluster_id=None, cluster_id=None, request_id=None):
        self.backup_status = backup_status  # type: str
        self.bds_cluster_id = bds_cluster_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.bds_cluster_id is not None:
            result['BdsClusterId'] = self.bds_cluster_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BdsClusterId') is not None:
            self.bds_cluster_id = m.get('BdsClusterId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupStatusResponse, self).to_map()
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
            temp_model = DescribeBackupStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupSummaryRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeBackupSummaryResponseBodyFullRecordsRecord(TeaModel):
    def __init__(self, create_time=None, data_size=None, finish_time=None, process=None, record_id=None, speed=None,
                 status=None):
        self.create_time = create_time  # type: str
        self.data_size = data_size  # type: str
        self.finish_time = finish_time  # type: str
        self.process = process  # type: str
        self.record_id = record_id  # type: str
        self.speed = speed  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupSummaryResponseBodyFullRecordsRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.process is not None:
            result['Process'] = self.process
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeBackupSummaryResponseBodyFullRecords(TeaModel):
    def __init__(self, record=None):
        self.record = record  # type: list[DescribeBackupSummaryResponseBodyFullRecordsRecord]

    def validate(self):
        if self.record:
            for k in self.record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupSummaryResponseBodyFullRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Record'] = []
        if self.record is not None:
            for k in self.record:
                result['Record'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.record = []
        if m.get('Record') is not None:
            for k in m.get('Record'):
                temp_model = DescribeBackupSummaryResponseBodyFullRecordsRecord()
                self.record.append(temp_model.from_map(k))
        return self


class DescribeBackupSummaryResponseBodyFull(TeaModel):
    def __init__(self, has_more=None, next_full_backup_date=None, page_number=None, page_size=None, records=None,
                 total=None):
        self.has_more = has_more  # type: str
        self.next_full_backup_date = next_full_backup_date  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.records = records  # type: DescribeBackupSummaryResponseBodyFullRecords
        self.total = total  # type: int

    def validate(self):
        if self.records:
            self.records.validate()

    def to_map(self):
        _map = super(DescribeBackupSummaryResponseBodyFull, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.next_full_backup_date is not None:
            result['NextFullBackupDate'] = self.next_full_backup_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.records is not None:
            result['Records'] = self.records.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('NextFullBackupDate') is not None:
            self.next_full_backup_date = m.get('NextFullBackupDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Records') is not None:
            temp_model = DescribeBackupSummaryResponseBodyFullRecords()
            self.records = temp_model.from_map(m['Records'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeBackupSummaryResponseBodyIncr(TeaModel):
    def __init__(self, backup_log_size=None, pos=None, queue_log_num=None, running_log_num=None, speed=None,
                 status=None):
        self.backup_log_size = backup_log_size  # type: str
        self.pos = pos  # type: str
        self.queue_log_num = queue_log_num  # type: str
        self.running_log_num = running_log_num  # type: str
        self.speed = speed  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupSummaryResponseBodyIncr, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_log_size is not None:
            result['BackupLogSize'] = self.backup_log_size
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.queue_log_num is not None:
            result['QueueLogNum'] = self.queue_log_num
        if self.running_log_num is not None:
            result['RunningLogNum'] = self.running_log_num
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupLogSize') is not None:
            self.backup_log_size = m.get('BackupLogSize')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('QueueLogNum') is not None:
            self.queue_log_num = m.get('QueueLogNum')
        if m.get('RunningLogNum') is not None:
            self.running_log_num = m.get('RunningLogNum')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeBackupSummaryResponseBody(TeaModel):
    def __init__(self, full=None, incr=None, request_id=None):
        self.full = full  # type: DescribeBackupSummaryResponseBodyFull
        self.incr = incr  # type: DescribeBackupSummaryResponseBodyIncr
        self.request_id = request_id  # type: str

    def validate(self):
        if self.full:
            self.full.validate()
        if self.incr:
            self.incr.validate()

    def to_map(self):
        _map = super(DescribeBackupSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full is not None:
            result['Full'] = self.full.to_map()
        if self.incr is not None:
            result['Incr'] = self.incr.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Full') is not None:
            temp_model = DescribeBackupSummaryResponseBodyFull()
            self.full = temp_model.from_map(m['Full'])
        if m.get('Incr') is not None:
            temp_model = DescribeBackupSummaryResponseBodyIncr()
            self.incr = temp_model.from_map(m['Incr'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupSummaryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupSummaryResponse, self).to_map()
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
            temp_model = DescribeBackupSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupTablesRequest(TeaModel):
    def __init__(self, backup_record_id=None, cluster_id=None, page_number=None, page_size=None):
        self.backup_record_id = backup_record_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_record_id is not None:
            result['BackupRecordId'] = self.backup_record_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRecordId') is not None:
            self.backup_record_id = m.get('BackupRecordId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeBackupTablesResponseBodyBackupRecordsBackupRecord(TeaModel):
    def __init__(self, data_size=None, end_time=None, message=None, process=None, speed=None, start_time=None,
                 state=None, table=None):
        self.data_size = data_size  # type: str
        self.end_time = end_time  # type: str
        self.message = message  # type: str
        self.process = process  # type: str
        self.speed = speed  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupTablesResponseBodyBackupRecordsBackupRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.message is not None:
            result['Message'] = self.message
        if self.process is not None:
            result['Process'] = self.process
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeBackupTablesResponseBodyBackupRecords(TeaModel):
    def __init__(self, backup_record=None):
        self.backup_record = backup_record  # type: list[DescribeBackupTablesResponseBodyBackupRecordsBackupRecord]

    def validate(self):
        if self.backup_record:
            for k in self.backup_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupTablesResponseBodyBackupRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupRecord'] = []
        if self.backup_record is not None:
            for k in self.backup_record:
                result['BackupRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backup_record = []
        if m.get('BackupRecord') is not None:
            for k in m.get('BackupRecord'):
                temp_model = DescribeBackupTablesResponseBodyBackupRecordsBackupRecord()
                self.backup_record.append(temp_model.from_map(k))
        return self


class DescribeBackupTablesResponseBodyTables(TeaModel):
    def __init__(self, table=None):
        self.table = table  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupTablesResponseBodyTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeBackupTablesResponseBody(TeaModel):
    def __init__(self, backup_records=None, page_number=None, page_size=None, request_id=None, tables=None,
                 total=None):
        self.backup_records = backup_records  # type: DescribeBackupTablesResponseBodyBackupRecords
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.tables = tables  # type: DescribeBackupTablesResponseBodyTables
        self.total = total  # type: long

    def validate(self):
        if self.backup_records:
            self.backup_records.validate()
        if self.tables:
            self.tables.validate()

    def to_map(self):
        _map = super(DescribeBackupTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_records is not None:
            result['BackupRecords'] = self.backup_records.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tables is not None:
            result['Tables'] = self.tables.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupRecords') is not None:
            temp_model = DescribeBackupTablesResponseBodyBackupRecords()
            self.backup_records = temp_model.from_map(m['BackupRecords'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tables') is not None:
            temp_model = DescribeBackupTablesResponseBodyTables()
            self.tables = temp_model.from_map(m['Tables'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeBackupTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupTablesResponse, self).to_map()
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
            temp_model = DescribeBackupTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(self, backup_id=None, cluster_id=None, end_time=None, end_time_utc=None, page_number=None,
                 page_size=None, start_time=None, start_time_utc=None):
        self.backup_id = backup_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.end_time = end_time  # type: str
        self.end_time_utc = end_time_utc  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.start_time = start_time  # type: str
        self.start_time_utc = start_time_utc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        return self


class DescribeBackupsResponseBodyBackupsBackup(TeaModel):
    def __init__(self, backup_dbnames=None, backup_download_url=None, backup_end_time=None,
                 backup_end_time_utc=None, backup_id=None, backup_method=None, backup_mode=None, backup_size=None,
                 backup_start_time=None, backup_start_time_utc=None, backup_status=None, backup_type=None):
        self.backup_dbnames = backup_dbnames  # type: str
        self.backup_download_url = backup_download_url  # type: str
        self.backup_end_time = backup_end_time  # type: str
        self.backup_end_time_utc = backup_end_time_utc  # type: str
        self.backup_id = backup_id  # type: int
        self.backup_method = backup_method  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_size = backup_size  # type: str
        self.backup_start_time = backup_start_time  # type: str
        self.backup_start_time_utc = backup_start_time_utc  # type: str
        self.backup_status = backup_status  # type: str
        self.backup_type = backup_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupsResponseBodyBackupsBackup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_dbnames is not None:
            result['BackupDBNames'] = self.backup_dbnames
        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_end_time_utc is not None:
            result['BackupEndTimeUTC'] = self.backup_end_time_utc
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_start_time_utc is not None:
            result['BackupStartTimeUTC'] = self.backup_start_time_utc
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupDBNames') is not None:
            self.backup_dbnames = m.get('BackupDBNames')
        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupEndTimeUTC') is not None:
            self.backup_end_time_utc = m.get('BackupEndTimeUTC')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStartTimeUTC') is not None:
            self.backup_start_time_utc = m.get('BackupStartTimeUTC')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        return self


class DescribeBackupsResponseBodyBackups(TeaModel):
    def __init__(self, backup=None):
        self.backup = backup  # type: list[DescribeBackupsResponseBodyBackupsBackup]

    def validate(self):
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponseBodyBackups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Backup'] = []
        if self.backup is not None:
            for k in self.backup:
                result['Backup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backup = []
        if m.get('Backup') is not None:
            for k in m.get('Backup'):
                temp_model = DescribeBackupsResponseBodyBackupsBackup()
                self.backup.append(temp_model.from_map(k))
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(self, backups=None, enable_status=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.backups = backups  # type: DescribeBackupsResponseBodyBackups
        self.enable_status = enable_status  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.backups:
            self.backups.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backups is not None:
            result['Backups'] = self.backups.to_map()
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status
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
        if m.get('Backups') is not None:
            temp_model = DescribeBackupsResponseBodyBackups()
            self.backups = temp_model.from_map(m['Backups'])
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponse, self).to_map()
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
            temp_model = DescribeBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterConnectionRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddrConnAddrInfo(TeaModel):
    def __init__(self, conn_addr=None, conn_addr_port=None, net_type=None):
        self.conn_addr = conn_addr  # type: str
        self.conn_addr_port = conn_addr_port  # type: str
        self.net_type = net_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddrConnAddrInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        return self


class DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddr(TeaModel):
    def __init__(self, conn_addr_info=None, conn_type=None):
        self.conn_addr_info = conn_addr_info  # type: DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddrConnAddrInfo
        self.conn_type = conn_type  # type: str

    def validate(self):
        if self.conn_addr_info:
            self.conn_addr_info.validate()

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddr, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_addr_info is not None:
            result['ConnAddrInfo'] = self.conn_addr_info.to_map()
        if self.conn_type is not None:
            result['ConnType'] = self.conn_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnAddrInfo') is not None:
            temp_model = DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddrConnAddrInfo()
            self.conn_addr_info = temp_model.from_map(m['ConnAddrInfo'])
        if m.get('ConnType') is not None:
            self.conn_type = m.get('ConnType')
        return self


class DescribeClusterConnectionResponseBodyServiceConnAddrs(TeaModel):
    def __init__(self, service_conn_addr=None):
        self.service_conn_addr = service_conn_addr  # type: list[DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddr]

    def validate(self):
        if self.service_conn_addr:
            for k in self.service_conn_addr:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBodyServiceConnAddrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServiceConnAddr'] = []
        if self.service_conn_addr is not None:
            for k in self.service_conn_addr:
                result['ServiceConnAddr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.service_conn_addr = []
        if m.get('ServiceConnAddr') is not None:
            for k in m.get('ServiceConnAddr'):
                temp_model = DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddr()
                self.service_conn_addr.append(temp_model.from_map(k))
        return self


class DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddrConnAddrInfo(TeaModel):
    def __init__(self, conn_addr=None, conn_addr_port=None, net_type=None):
        self.conn_addr = conn_addr  # type: str
        self.conn_addr_port = conn_addr_port  # type: str
        self.net_type = net_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddrConnAddrInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        return self


class DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddr(TeaModel):
    def __init__(self, conn_addr_info=None, slb_type=None):
        self.conn_addr_info = conn_addr_info  # type: DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddrConnAddrInfo
        self.slb_type = slb_type  # type: str

    def validate(self):
        if self.conn_addr_info:
            self.conn_addr_info.validate()

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddr, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_addr_info is not None:
            result['ConnAddrInfo'] = self.conn_addr_info.to_map()
        if self.slb_type is not None:
            result['SlbType'] = self.slb_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnAddrInfo') is not None:
            temp_model = DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddrConnAddrInfo()
            self.conn_addr_info = temp_model.from_map(m['ConnAddrInfo'])
        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')
        return self


class DescribeClusterConnectionResponseBodySlbConnAddrs(TeaModel):
    def __init__(self, slb_conn_addr=None):
        self.slb_conn_addr = slb_conn_addr  # type: list[DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddr]

    def validate(self):
        if self.slb_conn_addr:
            for k in self.slb_conn_addr:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBodySlbConnAddrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SlbConnAddr'] = []
        if self.slb_conn_addr is not None:
            for k in self.slb_conn_addr:
                result['SlbConnAddr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.slb_conn_addr = []
        if m.get('SlbConnAddr') is not None:
            for k in m.get('SlbConnAddr'):
                temp_model = DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddr()
                self.slb_conn_addr.append(temp_model.from_map(k))
        return self


class DescribeClusterConnectionResponseBodyThriftConn(TeaModel):
    def __init__(self, conn_addr=None, conn_addr_port=None, net_type=None):
        self.conn_addr = conn_addr  # type: str
        self.conn_addr_port = conn_addr_port  # type: str
        self.net_type = net_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBodyThriftConn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        return self


class DescribeClusterConnectionResponseBodyUiProxyConnAddrInfo(TeaModel):
    def __init__(self, conn_addr=None, conn_addr_port=None, net_type=None):
        self.conn_addr = conn_addr  # type: str
        self.conn_addr_port = conn_addr_port  # type: str
        self.net_type = net_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBodyUiProxyConnAddrInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        return self


class DescribeClusterConnectionResponseBodyZkConnAddrsZkConnAddr(TeaModel):
    def __init__(self, conn_addr=None, conn_addr_port=None, net_type=None):
        self.conn_addr = conn_addr  # type: str
        self.conn_addr_port = conn_addr_port  # type: str
        self.net_type = net_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBodyZkConnAddrsZkConnAddr, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        return self


class DescribeClusterConnectionResponseBodyZkConnAddrs(TeaModel):
    def __init__(self, zk_conn_addr=None):
        self.zk_conn_addr = zk_conn_addr  # type: list[DescribeClusterConnectionResponseBodyZkConnAddrsZkConnAddr]

    def validate(self):
        if self.zk_conn_addr:
            for k in self.zk_conn_addr:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBodyZkConnAddrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ZkConnAddr'] = []
        if self.zk_conn_addr is not None:
            for k in self.zk_conn_addr:
                result['ZkConnAddr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.zk_conn_addr = []
        if m.get('ZkConnAddr') is not None:
            for k in m.get('ZkConnAddr'):
                temp_model = DescribeClusterConnectionResponseBodyZkConnAddrsZkConnAddr()
                self.zk_conn_addr.append(temp_model.from_map(k))
        return self


class DescribeClusterConnectionResponseBody(TeaModel):
    def __init__(self, db_type=None, is_multimod=None, net_type=None, request_id=None, service_conn_addrs=None,
                 slb_conn_addrs=None, thrift_conn=None, ui_proxy_conn_addr_info=None, v_switch_id=None, vpc_id=None,
                 zk_conn_addrs=None):
        self.db_type = db_type  # type: str
        self.is_multimod = is_multimod  # type: str
        self.net_type = net_type  # type: str
        self.request_id = request_id  # type: str
        self.service_conn_addrs = service_conn_addrs  # type: DescribeClusterConnectionResponseBodyServiceConnAddrs
        self.slb_conn_addrs = slb_conn_addrs  # type: DescribeClusterConnectionResponseBodySlbConnAddrs
        self.thrift_conn = thrift_conn  # type: DescribeClusterConnectionResponseBodyThriftConn
        self.ui_proxy_conn_addr_info = ui_proxy_conn_addr_info  # type: DescribeClusterConnectionResponseBodyUiProxyConnAddrInfo
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zk_conn_addrs = zk_conn_addrs  # type: DescribeClusterConnectionResponseBodyZkConnAddrs

    def validate(self):
        if self.service_conn_addrs:
            self.service_conn_addrs.validate()
        if self.slb_conn_addrs:
            self.slb_conn_addrs.validate()
        if self.thrift_conn:
            self.thrift_conn.validate()
        if self.ui_proxy_conn_addr_info:
            self.ui_proxy_conn_addr_info.validate()
        if self.zk_conn_addrs:
            self.zk_conn_addrs.validate()

    def to_map(self):
        _map = super(DescribeClusterConnectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.is_multimod is not None:
            result['IsMultimod'] = self.is_multimod
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_conn_addrs is not None:
            result['ServiceConnAddrs'] = self.service_conn_addrs.to_map()
        if self.slb_conn_addrs is not None:
            result['SlbConnAddrs'] = self.slb_conn_addrs.to_map()
        if self.thrift_conn is not None:
            result['ThriftConn'] = self.thrift_conn.to_map()
        if self.ui_proxy_conn_addr_info is not None:
            result['UiProxyConnAddrInfo'] = self.ui_proxy_conn_addr_info.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zk_conn_addrs is not None:
            result['ZkConnAddrs'] = self.zk_conn_addrs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('IsMultimod') is not None:
            self.is_multimod = m.get('IsMultimod')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceConnAddrs') is not None:
            temp_model = DescribeClusterConnectionResponseBodyServiceConnAddrs()
            self.service_conn_addrs = temp_model.from_map(m['ServiceConnAddrs'])
        if m.get('SlbConnAddrs') is not None:
            temp_model = DescribeClusterConnectionResponseBodySlbConnAddrs()
            self.slb_conn_addrs = temp_model.from_map(m['SlbConnAddrs'])
        if m.get('ThriftConn') is not None:
            temp_model = DescribeClusterConnectionResponseBodyThriftConn()
            self.thrift_conn = temp_model.from_map(m['ThriftConn'])
        if m.get('UiProxyConnAddrInfo') is not None:
            temp_model = DescribeClusterConnectionResponseBodyUiProxyConnAddrInfo()
            self.ui_proxy_conn_addr_info = temp_model.from_map(m['UiProxyConnAddrInfo'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZkConnAddrs') is not None:
            temp_model = DescribeClusterConnectionResponseBodyZkConnAddrs()
            self.zk_conn_addrs = temp_model.from_map(m['ZkConnAddrs'])
        return self


class DescribeClusterConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterConnectionResponse, self).to_map()
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
            temp_model = DescribeClusterConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeColdStorageRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeColdStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeColdStorageResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cold_storage_size=None, cold_storage_type=None,
                 cold_storage_use_amount=None, cold_storage_use_percent=None, open_status=None, pay_type=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cold_storage_size = cold_storage_size  # type: str
        self.cold_storage_type = cold_storage_type  # type: str
        self.cold_storage_use_amount = cold_storage_use_amount  # type: str
        self.cold_storage_use_percent = cold_storage_use_percent  # type: str
        self.open_status = open_status  # type: str
        self.pay_type = pay_type  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeColdStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size
        if self.cold_storage_type is not None:
            result['ColdStorageType'] = self.cold_storage_type
        if self.cold_storage_use_amount is not None:
            result['ColdStorageUseAmount'] = self.cold_storage_use_amount
        if self.cold_storage_use_percent is not None:
            result['ColdStorageUsePercent'] = self.cold_storage_use_percent
        if self.open_status is not None:
            result['OpenStatus'] = self.open_status
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')
        if m.get('ColdStorageType') is not None:
            self.cold_storage_type = m.get('ColdStorageType')
        if m.get('ColdStorageUseAmount') is not None:
            self.cold_storage_use_amount = m.get('ColdStorageUseAmount')
        if m.get('ColdStorageUsePercent') is not None:
            self.cold_storage_use_percent = m.get('ColdStorageUsePercent')
        if m.get('OpenStatus') is not None:
            self.open_status = m.get('OpenStatus')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeColdStorageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeColdStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeColdStorageResponse, self).to_map()
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
            temp_model = DescribeColdStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceUsageRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeDBInstanceUsageResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeDBInstanceUsageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDBInstanceUsageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceUsageResponse, self).to_map()
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
            temp_model = DescribeDBInstanceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeletedInstancesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeletedInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDeletedInstancesResponseBodyInstancesInstance(TeaModel):
    def __init__(self, cluster_type=None, created_time=None, delete_time=None, engine=None, instance_id=None,
                 instance_name=None, major_version=None, module_stack_version=None, parent_id=None, region_id=None, status=None,
                 zone_id=None):
        self.cluster_type = cluster_type  # type: str
        self.created_time = created_time  # type: str
        self.delete_time = delete_time  # type: str
        self.engine = engine  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.major_version = major_version  # type: str
        self.module_stack_version = module_stack_version  # type: str
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeletedInstancesResponseBodyInstancesInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDeletedInstancesResponseBodyInstances(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance  # type: list[DescribeDeletedInstancesResponseBodyInstancesInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeletedInstancesResponseBodyInstances, self).to_map()
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
                temp_model = DescribeDeletedInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeDeletedInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.instances = instances  # type: DescribeDeletedInstancesResponseBodyInstances
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super(DescribeDeletedInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
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
        if m.get('Instances') is not None:
            temp_model = DescribeDeletedInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDeletedInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDeletedInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeletedInstancesResponse, self).to_map()
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
            temp_model = DescribeDeletedInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiskWarningLineRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskWarningLineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeDiskWarningLineResponseBody(TeaModel):
    def __init__(self, request_id=None, warning_line=None):
        self.request_id = request_id  # type: str
        self.warning_line = warning_line  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskWarningLineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.warning_line is not None:
            result['WarningLine'] = self.warning_line
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WarningLine') is not None:
            self.warning_line = m.get('WarningLine')
        return self


class DescribeDiskWarningLineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDiskWarningLineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiskWarningLineResponse, self).to_map()
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
            temp_model = DescribeDiskWarningLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeEndpointsResponseBodyConnAddrsConnAddrInfo(TeaModel):
    def __init__(self, conn_addr=None, conn_addr_port=None, conn_type=None, net_type=None):
        self.conn_addr = conn_addr  # type: str
        self.conn_addr_port = conn_addr_port  # type: str
        self.conn_type = conn_type  # type: str
        self.net_type = net_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndpointsResponseBodyConnAddrsConnAddrInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.conn_type is not None:
            result['ConnType'] = self.conn_type
        if self.net_type is not None:
            result['NetType'] = self.net_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('ConnType') is not None:
            self.conn_type = m.get('ConnType')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        return self


class DescribeEndpointsResponseBodyConnAddrs(TeaModel):
    def __init__(self, conn_addr_info=None):
        self.conn_addr_info = conn_addr_info  # type: list[DescribeEndpointsResponseBodyConnAddrsConnAddrInfo]

    def validate(self):
        if self.conn_addr_info:
            for k in self.conn_addr_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEndpointsResponseBodyConnAddrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnAddrInfo'] = []
        if self.conn_addr_info is not None:
            for k in self.conn_addr_info:
                result['ConnAddrInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.conn_addr_info = []
        if m.get('ConnAddrInfo') is not None:
            for k in m.get('ConnAddrInfo'):
                temp_model = DescribeEndpointsResponseBodyConnAddrsConnAddrInfo()
                self.conn_addr_info.append(temp_model.from_map(k))
        return self


class DescribeEndpointsResponseBody(TeaModel):
    def __init__(self, conn_addrs=None, engine=None, net_type=None, request_id=None, v_switch_id=None, vpc_id=None):
        self.conn_addrs = conn_addrs  # type: DescribeEndpointsResponseBodyConnAddrs
        self.engine = engine  # type: str
        self.net_type = net_type  # type: str
        self.request_id = request_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.conn_addrs:
            self.conn_addrs.validate()

    def to_map(self):
        _map = super(DescribeEndpointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_addrs is not None:
            result['ConnAddrs'] = self.conn_addrs.to_map()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnAddrs') is not None:
            temp_model = DescribeEndpointsResponseBodyConnAddrs()
            self.conn_addrs = temp_model.from_map(m['ConnAddrs'])
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeEndpointsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEndpointsResponse, self).to_map()
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
            temp_model = DescribeEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeInstanceResponseBodyNeedUpgradeComps(TeaModel):
    def __init__(self, comps=None):
        self.comps = comps  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyNeedUpgradeComps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comps is not None:
            result['Comps'] = self.comps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comps') is not None:
            self.comps = m.get('Comps')
        return self


class DescribeInstanceResponseBodyTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyTagsTag, self).to_map()
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


class DescribeInstanceResponseBodyTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeInstanceResponseBodyTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyTags, self).to_map()
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
                temp_model = DescribeInstanceResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(self, auto_renewal=None, backup_status=None, cluster_id=None, cluster_name=None, cluster_type=None,
                 cold_storage_size=None, cold_storage_status=None, confirm_maintain_time=None, core_disk_count=None,
                 core_disk_size=None, core_disk_type=None, core_instance_type=None, core_node_count=None, created_time=None,
                 created_time_utc=None, duration=None, encryption_key=None, encryption_type=None, engine=None, expire_time=None,
                 expire_time_utc=None, instance_id=None, instance_name=None, is_deletion_protection=None, is_ha=None,
                 is_latest_version=None, is_multi_model=None, maintain_end_time=None, maintain_start_time=None, major_version=None,
                 master_disk_size=None, master_disk_type=None, master_instance_type=None, master_node_count=None,
                 minor_version=None, module_id=None, module_stack_version=None, need_upgrade=None, need_upgrade_comps=None,
                 network_type=None, parent_id=None, pay_type=None, region_id=None, request_id=None, resource_group_id=None,
                 status=None, tags=None, task_progress=None, vpc_id=None, vswitch_id=None, zone_id=None):
        self.auto_renewal = auto_renewal  # type: bool
        self.backup_status = backup_status  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.cold_storage_size = cold_storage_size  # type: int
        self.cold_storage_status = cold_storage_status  # type: str
        self.confirm_maintain_time = confirm_maintain_time  # type: str
        self.core_disk_count = core_disk_count  # type: str
        self.core_disk_size = core_disk_size  # type: int
        self.core_disk_type = core_disk_type  # type: str
        self.core_instance_type = core_instance_type  # type: str
        self.core_node_count = core_node_count  # type: int
        self.created_time = created_time  # type: str
        self.created_time_utc = created_time_utc  # type: str
        self.duration = duration  # type: int
        self.encryption_key = encryption_key  # type: str
        self.encryption_type = encryption_type  # type: str
        self.engine = engine  # type: str
        self.expire_time = expire_time  # type: str
        self.expire_time_utc = expire_time_utc  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.is_deletion_protection = is_deletion_protection  # type: bool
        self.is_ha = is_ha  # type: bool
        self.is_latest_version = is_latest_version  # type: bool
        self.is_multi_model = is_multi_model  # type: bool
        self.maintain_end_time = maintain_end_time  # type: str
        self.maintain_start_time = maintain_start_time  # type: str
        self.major_version = major_version  # type: str
        self.master_disk_size = master_disk_size  # type: int
        self.master_disk_type = master_disk_type  # type: str
        self.master_instance_type = master_instance_type  # type: str
        self.master_node_count = master_node_count  # type: int
        self.minor_version = minor_version  # type: str
        self.module_id = module_id  # type: int
        self.module_stack_version = module_stack_version  # type: str
        self.need_upgrade = need_upgrade  # type: bool
        self.need_upgrade_comps = need_upgrade_comps  # type: DescribeInstanceResponseBodyNeedUpgradeComps
        self.network_type = network_type  # type: str
        self.parent_id = parent_id  # type: str
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: DescribeInstanceResponseBodyTags
        self.task_progress = task_progress  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.need_upgrade_comps:
            self.need_upgrade_comps.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size
        if self.cold_storage_status is not None:
            result['ColdStorageStatus'] = self.cold_storage_status
        if self.confirm_maintain_time is not None:
            result['ConfirmMaintainTime'] = self.confirm_maintain_time
        if self.core_disk_count is not None:
            result['CoreDiskCount'] = self.core_disk_count
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.created_time_utc is not None:
            result['CreatedTimeUTC'] = self.created_time_utc
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expire_time_utc is not None:
            result['ExpireTimeUTC'] = self.expire_time_utc
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_deletion_protection is not None:
            result['IsDeletionProtection'] = self.is_deletion_protection
        if self.is_ha is not None:
            result['IsHa'] = self.is_ha
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.is_multi_model is not None:
            result['IsMultiModel'] = self.is_multi_model
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.master_disk_size is not None:
            result['MasterDiskSize'] = self.master_disk_size
        if self.master_disk_type is not None:
            result['MasterDiskType'] = self.master_disk_type
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.master_node_count is not None:
            result['MasterNodeCount'] = self.master_node_count
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version
        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade
        if self.need_upgrade_comps is not None:
            result['NeedUpgradeComps'] = self.need_upgrade_comps.to_map()
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')
        if m.get('ColdStorageStatus') is not None:
            self.cold_storage_status = m.get('ColdStorageStatus')
        if m.get('ConfirmMaintainTime') is not None:
            self.confirm_maintain_time = m.get('ConfirmMaintainTime')
        if m.get('CoreDiskCount') is not None:
            self.core_disk_count = m.get('CoreDiskCount')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CreatedTimeUTC') is not None:
            self.created_time_utc = m.get('CreatedTimeUTC')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpireTimeUTC') is not None:
            self.expire_time_utc = m.get('ExpireTimeUTC')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsDeletionProtection') is not None:
            self.is_deletion_protection = m.get('IsDeletionProtection')
        if m.get('IsHa') is not None:
            self.is_ha = m.get('IsHa')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('IsMultiModel') is not None:
            self.is_multi_model = m.get('IsMultiModel')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('MasterDiskSize') is not None:
            self.master_disk_size = m.get('MasterDiskSize')
        if m.get('MasterDiskType') is not None:
            self.master_disk_type = m.get('MasterDiskType')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('MasterNodeCount') is not None:
            self.master_node_count = m.get('MasterNodeCount')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')
        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')
        if m.get('NeedUpgradeComps') is not None:
            temp_model = DescribeInstanceResponseBodyNeedUpgradeComps()
            self.need_upgrade_comps = temp_model.from_map(m['NeedUpgradeComps'])
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeInstanceResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponse, self).to_map()
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTypeRequest(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec(TeaModel):
    def __init__(self, cpu_size=None, instance_type=None, mem_size=None):
        self.cpu_size = cpu_size  # type: long
        self.instance_type = instance_type  # type: str
        self.mem_size = mem_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_size is not None:
            result['CpuSize'] = self.cpu_size
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuSize') is not None:
            self.cpu_size = m.get('CpuSize')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        return self


class DescribeInstanceTypeResponseBodyInstanceTypeSpecList(TeaModel):
    def __init__(self, instance_type_spec=None):
        self.instance_type_spec = instance_type_spec  # type: list[DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec]

    def validate(self):
        if self.instance_type_spec:
            for k in self.instance_type_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceTypeResponseBodyInstanceTypeSpecList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTypeSpec'] = []
        if self.instance_type_spec is not None:
            for k in self.instance_type_spec:
                result['InstanceTypeSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_type_spec = []
        if m.get('InstanceTypeSpec') is not None:
            for k in m.get('InstanceTypeSpec'):
                temp_model = DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec()
                self.instance_type_spec.append(temp_model.from_map(k))
        return self


class DescribeInstanceTypeResponseBody(TeaModel):
    def __init__(self, instance_type_spec_list=None, request_id=None):
        self.instance_type_spec_list = instance_type_spec_list  # type: DescribeInstanceTypeResponseBodyInstanceTypeSpecList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_type_spec_list:
            self.instance_type_spec_list.validate()

    def to_map(self):
        _map = super(DescribeInstanceTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type_spec_list is not None:
            result['InstanceTypeSpecList'] = self.instance_type_spec_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceTypeSpecList') is not None:
            temp_model = DescribeInstanceTypeResponseBodyInstanceTypeSpecList()
            self.instance_type_spec_list = temp_model.from_map(m['InstanceTypeSpecList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceTypeResponse, self).to_map()
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
            temp_model = DescribeInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesRequestTag, self).to_map()
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


class DescribeInstancesRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, db_type=None, page_number=None, page_size=None,
                 region_id=None, resource_group_id=None, tag=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.db_type = db_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[DescribeInstancesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesInstanceTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesInstanceTagsTag, self).to_map()
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


class DescribeInstancesResponseBodyInstancesInstanceTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeInstancesResponseBodyInstancesInstanceTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesInstanceTags, self).to_map()
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
                temp_model = DescribeInstancesResponseBodyInstancesInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesInstance(TeaModel):
    def __init__(self, auto_renewal=None, backup_status=None, cluster_id=None, cluster_name=None, cluster_type=None,
                 cold_storage_status=None, core_disk_count=None, core_disk_size=None, core_disk_type=None, core_instance_type=None,
                 core_node_count=None, created_time=None, created_time_utc=None, duration=None, engine=None, expire_time=None,
                 expire_time_utc=None, instance_id=None, instance_name=None, is_deletion_protection=None, is_ha=None,
                 major_version=None, master_disk_size=None, master_disk_type=None, master_instance_type=None,
                 master_node_count=None, module_id=None, module_stack_version=None, network_type=None, parent_id=None, pay_type=None,
                 region_id=None, resource_group_id=None, status=None, tags=None, vpc_id=None, vswitch_id=None, zone_id=None):
        self.auto_renewal = auto_renewal  # type: bool
        self.backup_status = backup_status  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.cold_storage_status = cold_storage_status  # type: str
        self.core_disk_count = core_disk_count  # type: str
        self.core_disk_size = core_disk_size  # type: int
        self.core_disk_type = core_disk_type  # type: str
        self.core_instance_type = core_instance_type  # type: str
        self.core_node_count = core_node_count  # type: int
        self.created_time = created_time  # type: str
        self.created_time_utc = created_time_utc  # type: str
        self.duration = duration  # type: int
        self.engine = engine  # type: str
        self.expire_time = expire_time  # type: str
        self.expire_time_utc = expire_time_utc  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.is_deletion_protection = is_deletion_protection  # type: bool
        self.is_ha = is_ha  # type: bool
        self.major_version = major_version  # type: str
        self.master_disk_size = master_disk_size  # type: int
        self.master_disk_type = master_disk_type  # type: str
        self.master_instance_type = master_instance_type  # type: str
        self.master_node_count = master_node_count  # type: int
        self.module_id = module_id  # type: int
        self.module_stack_version = module_stack_version  # type: str
        self.network_type = network_type  # type: str
        self.parent_id = parent_id  # type: str
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: DescribeInstancesResponseBodyInstancesInstanceTags
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cold_storage_status is not None:
            result['ColdStorageStatus'] = self.cold_storage_status
        if self.core_disk_count is not None:
            result['CoreDiskCount'] = self.core_disk_count
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.created_time_utc is not None:
            result['CreatedTimeUTC'] = self.created_time_utc
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expire_time_utc is not None:
            result['ExpireTimeUTC'] = self.expire_time_utc
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_deletion_protection is not None:
            result['IsDeletionProtection'] = self.is_deletion_protection
        if self.is_ha is not None:
            result['IsHa'] = self.is_ha
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.master_disk_size is not None:
            result['MasterDiskSize'] = self.master_disk_size
        if self.master_disk_type is not None:
            result['MasterDiskType'] = self.master_disk_type
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.master_node_count is not None:
            result['MasterNodeCount'] = self.master_node_count
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ColdStorageStatus') is not None:
            self.cold_storage_status = m.get('ColdStorageStatus')
        if m.get('CoreDiskCount') is not None:
            self.core_disk_count = m.get('CoreDiskCount')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CreatedTimeUTC') is not None:
            self.created_time_utc = m.get('CreatedTimeUTC')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpireTimeUTC') is not None:
            self.expire_time_utc = m.get('ExpireTimeUTC')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsDeletionProtection') is not None:
            self.is_deletion_protection = m.get('IsDeletionProtection')
        if m.get('IsHa') is not None:
            self.is_ha = m.get('IsHa')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('MasterDiskSize') is not None:
            self.master_disk_size = m.get('MasterDiskSize')
        if m.get('MasterDiskType') is not None:
            self.master_disk_type = m.get('MasterDiskType')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('MasterNodeCount') is not None:
            self.master_node_count = m.get('MasterNodeCount')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance  # type: list[DescribeInstancesResponseBodyInstancesInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstances, self).to_map()
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
                temp_model = DescribeInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.instances = instances  # type: DescribeInstancesResponseBodyInstances
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
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
        if m.get('Instances') is not None:
            temp_model = DescribeInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponse, self).to_map()
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpWhitelistRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeIpWhitelistResponseBodyGroupsGroupIpList(TeaModel):
    def __init__(self, ip=None):
        self.ip = ip  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpWhitelistResponseBodyGroupsGroupIpList, self).to_map()
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


class DescribeIpWhitelistResponseBodyGroupsGroup(TeaModel):
    def __init__(self, group_name=None, ip_list=None, ip_version=None):
        self.group_name = group_name  # type: str
        self.ip_list = ip_list  # type: DescribeIpWhitelistResponseBodyGroupsGroupIpList
        self.ip_version = ip_version  # type: int

    def validate(self):
        if self.ip_list:
            self.ip_list.validate()

    def to_map(self):
        _map = super(DescribeIpWhitelistResponseBodyGroupsGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_list is not None:
            result['IpList'] = self.ip_list.to_map()
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpList') is not None:
            temp_model = DescribeIpWhitelistResponseBodyGroupsGroupIpList()
            self.ip_list = temp_model.from_map(m['IpList'])
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class DescribeIpWhitelistResponseBodyGroups(TeaModel):
    def __init__(self, group=None):
        self.group = group  # type: list[DescribeIpWhitelistResponseBodyGroupsGroup]

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIpWhitelistResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = DescribeIpWhitelistResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class DescribeIpWhitelistResponseBody(TeaModel):
    def __init__(self, groups=None, request_id=None):
        self.groups = groups  # type: DescribeIpWhitelistResponseBodyGroups
        self.request_id = request_id  # type: str

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        _map = super(DescribeIpWhitelistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Groups') is not None:
            temp_model = DescribeIpWhitelistResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIpWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeIpWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpWhitelistResponse, self).to_map()
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
            temp_model = DescribeIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMultiZoneAvailableRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombineZones(TeaModel):
    def __init__(self, zone=None):
        self.zone = zone  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombineZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombine(TeaModel):
    def __init__(self, id=None, zones=None):
        self.id = id  # type: str
        self.zones = zones  # type: DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombineZones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Zones') is not None:
            temp_model = DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombineZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombines(TeaModel):
    def __init__(self, available_combine=None):
        self.available_combine = available_combine  # type: list[DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombine]

    def validate(self):
        if self.available_combine:
            for k in self.available_combine:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableCombine'] = []
        if self.available_combine is not None:
            for k in self.available_combine:
                result['AvailableCombine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_combine = []
        if m.get('AvailableCombine') is not None:
            for k in m.get('AvailableCombine'):
                temp_model = DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombine()
                self.available_combine.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, available_combines=None, local_name=None, region_endpoint=None, region_id=None):
        self.available_combines = available_combines  # type: DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombines
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.available_combines:
            self.available_combines.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_combines is not None:
            result['AvailableCombines'] = self.available_combines.to_map()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableCombines') is not None:
            temp_model = DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombines()
            self.available_combines = temp_model.from_map(m['AvailableCombines'])
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMultiZoneAvailableRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableRegionsResponseBodyRegions, self).to_map()
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
                temp_model = DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: DescribeMultiZoneAvailableRegionsResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableRegionsResponseBody, self).to_map()
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
            temp_model = DescribeMultiZoneAvailableRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMultiZoneAvailableRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeMultiZoneAvailableRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableRegionsResponse, self).to_map()
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
            temp_model = DescribeMultiZoneAvailableRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMultiZoneAvailableResourceRequest(TeaModel):
    def __init__(self, charge_type=None, region_id=None, zone_combination=None):
        self.charge_type = charge_type  # type: str
        self.region_id = region_id  # type: str
        self.zone_combination = zone_combination  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_combination is not None:
            result['ZoneCombination'] = self.zone_combination
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneCombination') is not None:
            self.zone_combination = m.get('ZoneCombination')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail(TeaModel):
    def __init__(self, cpu=None, mem=None):
        self.cpu = cpu  # type: int
        self.mem = mem  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource(TeaModel):
    def __init__(self, instance_type=None, instance_type_detail=None):
        self.instance_type = instance_type  # type: str
        self.instance_type_detail = instance_type_detail  # type: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail

    def validate(self):
        if self.instance_type_detail:
            self.instance_type_detail.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_type_detail is not None:
            result['InstanceTypeDetail'] = self.instance_type_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceTypeDetail') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail()
            self.instance_type_detail = temp_model.from_map(m['InstanceTypeDetail'])
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources(TeaModel):
    def __init__(self, master_resource=None):
        self.master_resource = master_resource  # type: list[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource]

    def validate(self):
        if self.master_resource:
            for k in self.master_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MasterResource'] = []
        if self.master_resource is not None:
            for k in self.master_resource:
                result['MasterResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.master_resource = []
        if m.get('MasterResource') is not None:
            for k in m.get('MasterResource'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource()
                self.master_resource.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange(TeaModel):
    def __init__(self, max_size=None, min_size=None, step_size=None):
        self.max_size = max_size  # type: int
        self.min_size = min_size  # type: int
        self.step_size = step_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        if self.step_size is not None:
            result['StepSize'] = self.step_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        if m.get('StepSize') is not None:
            self.step_size = m.get('StepSize')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail(TeaModel):
    def __init__(self, cpu=None, mem=None):
        self.cpu = cpu  # type: int
        self.mem = mem  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource(TeaModel):
    def __init__(self, dbinstance_storage_range=None, instance_type=None, instance_type_detail=None,
                 max_core_count=None):
        self.dbinstance_storage_range = dbinstance_storage_range  # type: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange
        self.instance_type = instance_type  # type: str
        self.instance_type_detail = instance_type_detail  # type: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail
        self.max_core_count = max_core_count  # type: int

    def validate(self):
        if self.dbinstance_storage_range:
            self.dbinstance_storage_range.validate()
        if self.instance_type_detail:
            self.instance_type_detail.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_storage_range is not None:
            result['DBInstanceStorageRange'] = self.dbinstance_storage_range.to_map()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_type_detail is not None:
            result['InstanceTypeDetail'] = self.instance_type_detail.to_map()
        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceStorageRange') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange()
            self.dbinstance_storage_range = temp_model.from_map(m['DBInstanceStorageRange'])
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceTypeDetail') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail()
            self.instance_type_detail = temp_model.from_map(m['InstanceTypeDetail'])
        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources(TeaModel):
    def __init__(self, core_resource=None):
        self.core_resource = core_resource  # type: list[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource]

    def validate(self):
        if self.core_resource:
            for k in self.core_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CoreResource'] = []
        if self.core_resource is not None:
            for k in self.core_resource:
                result['CoreResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.core_resource = []
        if m.get('CoreResource') is not None:
            for k in m.get('CoreResource'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource()
                self.core_resource.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType(TeaModel):
    def __init__(self, core_resources=None, storage_type=None):
        self.core_resources = core_resources  # type: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources
        self.storage_type = storage_type  # type: str

    def validate(self):
        if self.core_resources:
            self.core_resources.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_resources is not None:
            result['CoreResources'] = self.core_resources.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoreResources') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources()
            self.core_resources = temp_model.from_map(m['CoreResources'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes(TeaModel):
    def __init__(self, supported_storage_type=None):
        self.supported_storage_type = supported_storage_type  # type: list[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType]

    def validate(self):
        if self.supported_storage_type:
            for k in self.supported_storage_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedStorageType'] = []
        if self.supported_storage_type is not None:
            for k in self.supported_storage_type:
                result['SupportedStorageType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_storage_type = []
        if m.get('SupportedStorageType') is not None:
            for k in m.get('SupportedStorageType'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType()
                self.supported_storage_type.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories(TeaModel):
    def __init__(self, category=None, supported_storage_types=None):
        self.category = category  # type: str
        self.supported_storage_types = supported_storage_types  # type: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes

    def validate(self):
        if self.supported_storage_types:
            self.supported_storage_types.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.supported_storage_types is not None:
            result['SupportedStorageTypes'] = self.supported_storage_types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('SupportedStorageTypes') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes()
            self.supported_storage_types = temp_model.from_map(m['SupportedStorageTypes'])
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories(TeaModel):
    def __init__(self, supported_categories=None):
        self.supported_categories = supported_categories  # type: list[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories]

    def validate(self):
        if self.supported_categories:
            for k in self.supported_categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedCategories'] = []
        if self.supported_categories is not None:
            for k in self.supported_categories:
                result['SupportedCategories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_categories = []
        if m.get('SupportedCategories') is not None:
            for k in m.get('SupportedCategories'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories()
                self.supported_categories.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion(TeaModel):
    def __init__(self, supported_categories=None, version=None):
        self.supported_categories = supported_categories  # type: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories
        self.version = version  # type: str

    def validate(self):
        if self.supported_categories:
            self.supported_categories.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_categories is not None:
            result['SupportedCategories'] = self.supported_categories.to_map()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedCategories') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories()
            self.supported_categories = temp_model.from_map(m['SupportedCategories'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions(TeaModel):
    def __init__(self, supported_engine_version=None):
        self.supported_engine_version = supported_engine_version  # type: list[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion]

    def validate(self):
        if self.supported_engine_version:
            for k in self.supported_engine_version:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedEngineVersion'] = []
        if self.supported_engine_version is not None:
            for k in self.supported_engine_version:
                result['SupportedEngineVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_engine_version = []
        if m.get('SupportedEngineVersion') is not None:
            for k in m.get('SupportedEngineVersion'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion()
                self.supported_engine_version.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine(TeaModel):
    def __init__(self, engine=None, supported_engine_versions=None):
        self.engine = engine  # type: str
        self.supported_engine_versions = supported_engine_versions  # type: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions

    def validate(self):
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.supported_engine_versions is not None:
            result['SupportedEngineVersions'] = self.supported_engine_versions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('SupportedEngineVersions') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions()
            self.supported_engine_versions = temp_model.from_map(m['SupportedEngineVersions'])
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines(TeaModel):
    def __init__(self, supported_engine=None):
        self.supported_engine = supported_engine  # type: list[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine]

    def validate(self):
        if self.supported_engine:
            for k in self.supported_engine:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedEngine'] = []
        if self.supported_engine is not None:
            for k in self.supported_engine:
                result['SupportedEngine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_engine = []
        if m.get('SupportedEngine') is not None:
            for k in m.get('SupportedEngine'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine()
                self.supported_engine.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZone(TeaModel):
    def __init__(self, master_resources=None, region_id=None, supported_engines=None, zone_combination=None):
        self.master_resources = master_resources  # type: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources
        self.region_id = region_id  # type: str
        self.supported_engines = supported_engines  # type: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines
        self.zone_combination = zone_combination  # type: str

    def validate(self):
        if self.master_resources:
            self.master_resources.validate()
        if self.supported_engines:
            self.supported_engines.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.master_resources is not None:
            result['MasterResources'] = self.master_resources.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.supported_engines is not None:
            result['SupportedEngines'] = self.supported_engines.to_map()
        if self.zone_combination is not None:
            result['ZoneCombination'] = self.zone_combination
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MasterResources') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources()
            self.master_resources = temp_model.from_map(m['MasterResources'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupportedEngines') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines()
            self.supported_engines = temp_model.from_map(m['SupportedEngines'])
        if m.get('ZoneCombination') is not None:
            self.zone_combination = m.get('ZoneCombination')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZones(TeaModel):
    def __init__(self, available_zone=None):
        self.available_zone = available_zone  # type: list[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZone]

    def validate(self):
        if self.available_zone:
            for k in self.available_zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBodyAvailableZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k in self.available_zone:
                result['AvailableZone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_zone = []
        if m.get('AvailableZone') is not None:
            for k in m.get('AvailableZone'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBody(TeaModel):
    def __init__(self, available_zones=None, request_id=None):
        self.available_zones = available_zones  # type: DescribeMultiZoneAvailableResourceResponseBodyAvailableZones
        self.request_id = request_id  # type: str

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZones()
            self.available_zones = temp_model.from_map(m['AvailableZones'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMultiZoneAvailableResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeMultiZoneAvailableResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneAvailableResourceResponse, self).to_map()
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
            temp_model = DescribeMultiZoneAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMultiZoneClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiZoneClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModelsMultiZoneInstanceModel(TeaModel):
    def __init__(self, ins_name=None, is_latest_version=None, minor_version=None, role=None, status=None):
        self.ins_name = ins_name  # type: str
        self.is_latest_version = is_latest_version  # type: bool
        self.minor_version = minor_version  # type: str
        self.role = role  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModelsMultiZoneInstanceModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModels(TeaModel):
    def __init__(self, multi_zone_instance_model=None):
        self.multi_zone_instance_model = multi_zone_instance_model  # type: list[DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModelsMultiZoneInstanceModel]

    def validate(self):
        if self.multi_zone_instance_model:
            for k in self.multi_zone_instance_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MultiZoneInstanceModel'] = []
        if self.multi_zone_instance_model is not None:
            for k in self.multi_zone_instance_model:
                result['MultiZoneInstanceModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.multi_zone_instance_model = []
        if m.get('MultiZoneInstanceModel') is not None:
            for k in m.get('MultiZoneInstanceModel'):
                temp_model = DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModelsMultiZoneInstanceModel()
                self.multi_zone_instance_model.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneClusterResponseBodyTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMultiZoneClusterResponseBodyTagsTag, self).to_map()
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


class DescribeMultiZoneClusterResponseBodyTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeMultiZoneClusterResponseBodyTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneClusterResponseBodyTags, self).to_map()
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
                temp_model = DescribeMultiZoneClusterResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneClusterResponseBody(TeaModel):
    def __init__(self, arbiter_vswitch_ids=None, arbiter_zone_id=None, auto_renewal=None, cluster_id=None,
                 cluster_name=None, core_disk_count=None, core_disk_size=None, core_disk_type=None, core_instance_type=None,
                 core_node_count=None, created_time=None, created_time_utc=None, duration=None, encryption_key=None,
                 encryption_type=None, engine=None, expire_time=None, expire_time_utc=None, instance_id=None, instance_name=None,
                 is_deletion_protection=None, log_disk_count=None, log_disk_size=None, log_disk_type=None, log_instance_type=None,
                 log_node_count=None, maintain_end_time=None, maintain_start_time=None, major_version=None, master_disk_size=None,
                 master_disk_type=None, master_instance_type=None, master_node_count=None, module_id=None,
                 module_stack_version=None, multi_zone_combination=None, multi_zone_instance_models=None, network_type=None,
                 parent_id=None, pay_type=None, primary_vswitch_ids=None, primary_zone_id=None, region_id=None,
                 request_id=None, resource_group_id=None, standby_vswitch_ids=None, standby_zone_id=None, status=None,
                 tags=None, vpc_id=None):
        self.arbiter_vswitch_ids = arbiter_vswitch_ids  # type: str
        self.arbiter_zone_id = arbiter_zone_id  # type: str
        self.auto_renewal = auto_renewal  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.core_disk_count = core_disk_count  # type: str
        self.core_disk_size = core_disk_size  # type: int
        self.core_disk_type = core_disk_type  # type: str
        self.core_instance_type = core_instance_type  # type: str
        self.core_node_count = core_node_count  # type: int
        self.created_time = created_time  # type: str
        self.created_time_utc = created_time_utc  # type: str
        self.duration = duration  # type: int
        self.encryption_key = encryption_key  # type: str
        self.encryption_type = encryption_type  # type: str
        self.engine = engine  # type: str
        self.expire_time = expire_time  # type: str
        self.expire_time_utc = expire_time_utc  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.is_deletion_protection = is_deletion_protection  # type: bool
        self.log_disk_count = log_disk_count  # type: str
        self.log_disk_size = log_disk_size  # type: int
        self.log_disk_type = log_disk_type  # type: str
        self.log_instance_type = log_instance_type  # type: str
        self.log_node_count = log_node_count  # type: int
        self.maintain_end_time = maintain_end_time  # type: str
        self.maintain_start_time = maintain_start_time  # type: str
        self.major_version = major_version  # type: str
        self.master_disk_size = master_disk_size  # type: int
        self.master_disk_type = master_disk_type  # type: str
        self.master_instance_type = master_instance_type  # type: str
        self.master_node_count = master_node_count  # type: int
        self.module_id = module_id  # type: int
        self.module_stack_version = module_stack_version  # type: str
        self.multi_zone_combination = multi_zone_combination  # type: str
        self.multi_zone_instance_models = multi_zone_instance_models  # type: DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModels
        self.network_type = network_type  # type: str
        self.parent_id = parent_id  # type: str
        self.pay_type = pay_type  # type: str
        self.primary_vswitch_ids = primary_vswitch_ids  # type: str
        self.primary_zone_id = primary_zone_id  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.standby_vswitch_ids = standby_vswitch_ids  # type: str
        self.standby_zone_id = standby_zone_id  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: DescribeMultiZoneClusterResponseBodyTags
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.multi_zone_instance_models:
            self.multi_zone_instance_models.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arbiter_vswitch_ids is not None:
            result['ArbiterVSwitchIds'] = self.arbiter_vswitch_ids
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.core_disk_count is not None:
            result['CoreDiskCount'] = self.core_disk_count
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.created_time_utc is not None:
            result['CreatedTimeUTC'] = self.created_time_utc
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expire_time_utc is not None:
            result['ExpireTimeUTC'] = self.expire_time_utc
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_deletion_protection is not None:
            result['IsDeletionProtection'] = self.is_deletion_protection
        if self.log_disk_count is not None:
            result['LogDiskCount'] = self.log_disk_count
        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size
        if self.log_disk_type is not None:
            result['LogDiskType'] = self.log_disk_type
        if self.log_instance_type is not None:
            result['LogInstanceType'] = self.log_instance_type
        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.master_disk_size is not None:
            result['MasterDiskSize'] = self.master_disk_size
        if self.master_disk_type is not None:
            result['MasterDiskType'] = self.master_disk_type
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.master_node_count is not None:
            result['MasterNodeCount'] = self.master_node_count
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version
        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination
        if self.multi_zone_instance_models is not None:
            result['MultiZoneInstanceModels'] = self.multi_zone_instance_models.to_map()
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.primary_vswitch_ids is not None:
            result['PrimaryVSwitchIds'] = self.primary_vswitch_ids
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.standby_vswitch_ids is not None:
            result['StandbyVSwitchIds'] = self.standby_vswitch_ids
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArbiterVSwitchIds') is not None:
            self.arbiter_vswitch_ids = m.get('ArbiterVSwitchIds')
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CoreDiskCount') is not None:
            self.core_disk_count = m.get('CoreDiskCount')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CreatedTimeUTC') is not None:
            self.created_time_utc = m.get('CreatedTimeUTC')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpireTimeUTC') is not None:
            self.expire_time_utc = m.get('ExpireTimeUTC')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsDeletionProtection') is not None:
            self.is_deletion_protection = m.get('IsDeletionProtection')
        if m.get('LogDiskCount') is not None:
            self.log_disk_count = m.get('LogDiskCount')
        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')
        if m.get('LogDiskType') is not None:
            self.log_disk_type = m.get('LogDiskType')
        if m.get('LogInstanceType') is not None:
            self.log_instance_type = m.get('LogInstanceType')
        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('MasterDiskSize') is not None:
            self.master_disk_size = m.get('MasterDiskSize')
        if m.get('MasterDiskType') is not None:
            self.master_disk_type = m.get('MasterDiskType')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('MasterNodeCount') is not None:
            self.master_node_count = m.get('MasterNodeCount')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')
        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')
        if m.get('MultiZoneInstanceModels') is not None:
            temp_model = DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModels()
            self.multi_zone_instance_models = temp_model.from_map(m['MultiZoneInstanceModels'])
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PrimaryVSwitchIds') is not None:
            self.primary_vswitch_ids = m.get('PrimaryVSwitchIds')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StandbyVSwitchIds') is not None:
            self.standby_vswitch_ids = m.get('StandbyVSwitchIds')
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeMultiZoneClusterResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeMultiZoneClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeMultiZoneClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMultiZoneClusterResponse, self).to_map()
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
            temp_model = DescribeMultiZoneClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecoverableTimeRangeRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecoverableTimeRangeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeRecoverableTimeRangeResponseBody(TeaModel):
    def __init__(self, request_id=None, time_begin=None, time_end=None):
        self.request_id = request_id  # type: str
        self.time_begin = time_begin  # type: str
        self.time_end = time_end  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecoverableTimeRangeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_begin is not None:
            result['TimeBegin'] = self.time_begin
        if self.time_end is not None:
            result['TimeEnd'] = self.time_end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeBegin') is not None:
            self.time_begin = m.get('TimeBegin')
        if m.get('TimeEnd') is not None:
            self.time_end = m.get('TimeEnd')
        return self


class DescribeRecoverableTimeRangeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRecoverableTimeRangeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRecoverableTimeRangeResponse, self).to_map()
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
            temp_model = DescribeRecoverableTimeRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, engine=None):
        self.accept_language = accept_language  # type: str
        self.engine = engine  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegionZonesZone, self).to_map()
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


class DescribeRegionsResponseBodyRegionsRegionZones(TeaModel):
    def __init__(self, zone=None):
        self.zone = zone  # type: list[DescribeRegionsResponseBodyRegionsRegionZonesZone]

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegionZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None, zones=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str
        self.zones = zones  # type: DescribeRegionsResponseBodyRegionsRegionZones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
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
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
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
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeRestoreFullDetailsRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None, restore_record_id=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.restore_record_id = restore_record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreFullDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.restore_record_id is not None:
            result['RestoreRecordId'] = self.restore_record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RestoreRecordId') is not None:
            self.restore_record_id = m.get('RestoreRecordId')
        return self


class DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail(TeaModel):
    def __init__(self, data_size=None, end_time=None, message=None, process=None, speed=None, start_time=None,
                 state=None, table=None):
        self.data_size = data_size  # type: str
        self.end_time = end_time  # type: str
        self.message = message  # type: str
        self.process = process  # type: str
        self.speed = speed  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.message is not None:
            result['Message'] = self.message
        if self.process is not None:
            result['Process'] = self.process
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetails(TeaModel):
    def __init__(self, restore_full_detail=None):
        self.restore_full_detail = restore_full_detail  # type: list[DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail]

    def validate(self):
        if self.restore_full_detail:
            for k in self.restore_full_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RestoreFullDetail'] = []
        if self.restore_full_detail is not None:
            for k in self.restore_full_detail:
                result['RestoreFullDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.restore_full_detail = []
        if m.get('RestoreFullDetail') is not None:
            for k in m.get('RestoreFullDetail'):
                temp_model = DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail()
                self.restore_full_detail.append(temp_model.from_map(k))
        return self


class DescribeRestoreFullDetailsResponseBodyRestoreFull(TeaModel):
    def __init__(self, data_size=None, fail=None, page_number=None, page_size=None, restore_full_details=None,
                 speed=None, succeed=None, total=None):
        self.data_size = data_size  # type: str
        self.fail = fail  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.restore_full_details = restore_full_details  # type: DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetails
        self.speed = speed  # type: str
        self.succeed = succeed  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.restore_full_details:
            self.restore_full_details.validate()

    def to_map(self):
        _map = super(DescribeRestoreFullDetailsResponseBodyRestoreFull, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.restore_full_details is not None:
            result['RestoreFullDetails'] = self.restore_full_details.to_map()
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RestoreFullDetails') is not None:
            temp_model = DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetails()
            self.restore_full_details = temp_model.from_map(m['RestoreFullDetails'])
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRestoreFullDetailsResponseBody(TeaModel):
    def __init__(self, request_id=None, restore_full=None):
        self.request_id = request_id  # type: str
        self.restore_full = restore_full  # type: DescribeRestoreFullDetailsResponseBodyRestoreFull

    def validate(self):
        if self.restore_full:
            self.restore_full.validate()

    def to_map(self):
        _map = super(DescribeRestoreFullDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_full is not None:
            result['RestoreFull'] = self.restore_full.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreFull') is not None:
            temp_model = DescribeRestoreFullDetailsResponseBodyRestoreFull()
            self.restore_full = temp_model.from_map(m['RestoreFull'])
        return self


class DescribeRestoreFullDetailsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRestoreFullDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRestoreFullDetailsResponse, self).to_map()
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
            temp_model = DescribeRestoreFullDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreIncrDetailRequest(TeaModel):
    def __init__(self, cluster_id=None, restore_record_id=None):
        self.cluster_id = cluster_id  # type: str
        self.restore_record_id = restore_record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreIncrDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.restore_record_id is not None:
            result['RestoreRecordId'] = self.restore_record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RestoreRecordId') is not None:
            self.restore_record_id = m.get('RestoreRecordId')
        return self


class DescribeRestoreIncrDetailResponseBodyRestoreIncrDetail(TeaModel):
    def __init__(self, end_time=None, process=None, restore_delay=None, restore_start_ts=None, restored_ts=None,
                 start_time=None, state=None):
        self.end_time = end_time  # type: str
        self.process = process  # type: str
        self.restore_delay = restore_delay  # type: str
        self.restore_start_ts = restore_start_ts  # type: str
        self.restored_ts = restored_ts  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreIncrDetailResponseBodyRestoreIncrDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.process is not None:
            result['Process'] = self.process
        if self.restore_delay is not None:
            result['RestoreDelay'] = self.restore_delay
        if self.restore_start_ts is not None:
            result['RestoreStartTs'] = self.restore_start_ts
        if self.restored_ts is not None:
            result['RestoredTs'] = self.restored_ts
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('RestoreDelay') is not None:
            self.restore_delay = m.get('RestoreDelay')
        if m.get('RestoreStartTs') is not None:
            self.restore_start_ts = m.get('RestoreStartTs')
        if m.get('RestoredTs') is not None:
            self.restored_ts = m.get('RestoredTs')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeRestoreIncrDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, restore_incr_detail=None):
        self.request_id = request_id  # type: str
        self.restore_incr_detail = restore_incr_detail  # type: DescribeRestoreIncrDetailResponseBodyRestoreIncrDetail

    def validate(self):
        if self.restore_incr_detail:
            self.restore_incr_detail.validate()

    def to_map(self):
        _map = super(DescribeRestoreIncrDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_incr_detail is not None:
            result['RestoreIncrDetail'] = self.restore_incr_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreIncrDetail') is not None:
            temp_model = DescribeRestoreIncrDetailResponseBodyRestoreIncrDetail()
            self.restore_incr_detail = temp_model.from_map(m['RestoreIncrDetail'])
        return self


class DescribeRestoreIncrDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRestoreIncrDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRestoreIncrDetailResponse, self).to_map()
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
            temp_model = DescribeRestoreIncrDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreSchemaDetailsRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None, restore_record_id=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.restore_record_id = restore_record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreSchemaDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.restore_record_id is not None:
            result['RestoreRecordId'] = self.restore_record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RestoreRecordId') is not None:
            self.restore_record_id = m.get('RestoreRecordId')
        return self


class DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail(TeaModel):
    def __init__(self, end_time=None, message=None, start_time=None, state=None, table=None):
        self.end_time = end_time  # type: str
        self.message = message  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.message is not None:
            result['Message'] = self.message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetails(TeaModel):
    def __init__(self, restore_schema_detail=None):
        self.restore_schema_detail = restore_schema_detail  # type: list[DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail]

    def validate(self):
        if self.restore_schema_detail:
            for k in self.restore_schema_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RestoreSchemaDetail'] = []
        if self.restore_schema_detail is not None:
            for k in self.restore_schema_detail:
                result['RestoreSchemaDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.restore_schema_detail = []
        if m.get('RestoreSchemaDetail') is not None:
            for k in m.get('RestoreSchemaDetail'):
                temp_model = DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail()
                self.restore_schema_detail.append(temp_model.from_map(k))
        return self


class DescribeRestoreSchemaDetailsResponseBodyRestoreSchema(TeaModel):
    def __init__(self, fail=None, page_number=None, page_size=None, restore_schema_details=None, succeed=None,
                 total=None):
        self.fail = fail  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.restore_schema_details = restore_schema_details  # type: DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetails
        self.succeed = succeed  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.restore_schema_details:
            self.restore_schema_details.validate()

    def to_map(self):
        _map = super(DescribeRestoreSchemaDetailsResponseBodyRestoreSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.restore_schema_details is not None:
            result['RestoreSchemaDetails'] = self.restore_schema_details.to_map()
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RestoreSchemaDetails') is not None:
            temp_model = DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetails()
            self.restore_schema_details = temp_model.from_map(m['RestoreSchemaDetails'])
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRestoreSchemaDetailsResponseBody(TeaModel):
    def __init__(self, request_id=None, restore_schema=None):
        self.request_id = request_id  # type: str
        self.restore_schema = restore_schema  # type: DescribeRestoreSchemaDetailsResponseBodyRestoreSchema

    def validate(self):
        if self.restore_schema:
            self.restore_schema.validate()

    def to_map(self):
        _map = super(DescribeRestoreSchemaDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_schema is not None:
            result['RestoreSchema'] = self.restore_schema.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreSchema') is not None:
            temp_model = DescribeRestoreSchemaDetailsResponseBodyRestoreSchema()
            self.restore_schema = temp_model.from_map(m['RestoreSchema'])
        return self


class DescribeRestoreSchemaDetailsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRestoreSchemaDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRestoreSchemaDetailsResponse, self).to_map()
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
            temp_model = DescribeRestoreSchemaDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreSummaryRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRestoreSummaryResponseBodyRescordsRescord(TeaModel):
    def __init__(self, bulk_load_process=None, create_time=None, finish_time=None, hfile_restore_process=None,
                 log_process=None, record_id=None, schema_process=None, status=None):
        self.bulk_load_process = bulk_load_process  # type: str
        self.create_time = create_time  # type: str
        self.finish_time = finish_time  # type: str
        self.hfile_restore_process = hfile_restore_process  # type: str
        self.log_process = log_process  # type: str
        self.record_id = record_id  # type: str
        self.schema_process = schema_process  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreSummaryResponseBodyRescordsRescord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bulk_load_process is not None:
            result['BulkLoadProcess'] = self.bulk_load_process
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.hfile_restore_process is not None:
            result['HfileRestoreProcess'] = self.hfile_restore_process
        if self.log_process is not None:
            result['LogProcess'] = self.log_process
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.schema_process is not None:
            result['SchemaProcess'] = self.schema_process
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BulkLoadProcess') is not None:
            self.bulk_load_process = m.get('BulkLoadProcess')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('HfileRestoreProcess') is not None:
            self.hfile_restore_process = m.get('HfileRestoreProcess')
        if m.get('LogProcess') is not None:
            self.log_process = m.get('LogProcess')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('SchemaProcess') is not None:
            self.schema_process = m.get('SchemaProcess')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeRestoreSummaryResponseBodyRescords(TeaModel):
    def __init__(self, rescord=None):
        self.rescord = rescord  # type: list[DescribeRestoreSummaryResponseBodyRescordsRescord]

    def validate(self):
        if self.rescord:
            for k in self.rescord:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRestoreSummaryResponseBodyRescords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rescord'] = []
        if self.rescord is not None:
            for k in self.rescord:
                result['Rescord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rescord = []
        if m.get('Rescord') is not None:
            for k in m.get('Rescord'):
                temp_model = DescribeRestoreSummaryResponseBodyRescordsRescord()
                self.rescord.append(temp_model.from_map(k))
        return self


class DescribeRestoreSummaryResponseBody(TeaModel):
    def __init__(self, has_more_restore_record=None, page_number=None, page_size=None, request_id=None,
                 rescords=None, total=None):
        self.has_more_restore_record = has_more_restore_record  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.rescords = rescords  # type: DescribeRestoreSummaryResponseBodyRescords
        self.total = total  # type: int

    def validate(self):
        if self.rescords:
            self.rescords.validate()

    def to_map(self):
        _map = super(DescribeRestoreSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more_restore_record is not None:
            result['HasMoreRestoreRecord'] = self.has_more_restore_record
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rescords is not None:
            result['Rescords'] = self.rescords.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasMoreRestoreRecord') is not None:
            self.has_more_restore_record = m.get('HasMoreRestoreRecord')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rescords') is not None:
            temp_model = DescribeRestoreSummaryResponseBodyRescords()
            self.rescords = temp_model.from_map(m['Rescords'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRestoreSummaryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRestoreSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRestoreSummaryResponse, self).to_map()
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
            temp_model = DescribeRestoreSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreTablesRequest(TeaModel):
    def __init__(self, cluster_id=None, restore_record_id=None):
        self.cluster_id = cluster_id  # type: str
        self.restore_record_id = restore_record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.restore_record_id is not None:
            result['RestoreRecordId'] = self.restore_record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RestoreRecordId') is not None:
            self.restore_record_id = m.get('RestoreRecordId')
        return self


class DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail(TeaModel):
    def __init__(self, data_size=None, end_time=None, message=None, process=None, speed=None, start_time=None,
                 state=None, table=None):
        self.data_size = data_size  # type: str
        self.end_time = end_time  # type: str
        self.message = message  # type: str
        self.process = process  # type: str
        self.speed = speed  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.message is not None:
            result['Message'] = self.message
        if self.process is not None:
            result['Process'] = self.process
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetails(TeaModel):
    def __init__(self, restore_full_detail=None):
        self.restore_full_detail = restore_full_detail  # type: list[DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail]

    def validate(self):
        if self.restore_full_detail:
            for k in self.restore_full_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RestoreFullDetail'] = []
        if self.restore_full_detail is not None:
            for k in self.restore_full_detail:
                result['RestoreFullDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.restore_full_detail = []
        if m.get('RestoreFullDetail') is not None:
            for k in m.get('RestoreFullDetail'):
                temp_model = DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail()
                self.restore_full_detail.append(temp_model.from_map(k))
        return self


class DescribeRestoreTablesResponseBodyRestoreFull(TeaModel):
    def __init__(self, data_size=None, fail=None, page_number=None, page_size=None, restore_full_details=None,
                 speed=None, succeed=None, total=None):
        self.data_size = data_size  # type: str
        self.fail = fail  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.restore_full_details = restore_full_details  # type: DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetails
        self.speed = speed  # type: str
        self.succeed = succeed  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.restore_full_details:
            self.restore_full_details.validate()

    def to_map(self):
        _map = super(DescribeRestoreTablesResponseBodyRestoreFull, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.restore_full_details is not None:
            result['RestoreFullDetails'] = self.restore_full_details.to_map()
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RestoreFullDetails') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetails()
            self.restore_full_details = temp_model.from_map(m['RestoreFullDetails'])
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRestoreTablesResponseBodyRestoreIncrDetail(TeaModel):
    def __init__(self, end_time=None, process=None, restore_delay=None, restore_start_ts=None, restored_ts=None,
                 start_time=None, state=None):
        self.end_time = end_time  # type: str
        self.process = process  # type: str
        self.restore_delay = restore_delay  # type: str
        self.restore_start_ts = restore_start_ts  # type: str
        self.restored_ts = restored_ts  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreTablesResponseBodyRestoreIncrDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.process is not None:
            result['Process'] = self.process
        if self.restore_delay is not None:
            result['RestoreDelay'] = self.restore_delay
        if self.restore_start_ts is not None:
            result['RestoreStartTs'] = self.restore_start_ts
        if self.restored_ts is not None:
            result['RestoredTs'] = self.restored_ts
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('RestoreDelay') is not None:
            self.restore_delay = m.get('RestoreDelay')
        if m.get('RestoreStartTs') is not None:
            self.restore_start_ts = m.get('RestoreStartTs')
        if m.get('RestoredTs') is not None:
            self.restored_ts = m.get('RestoredTs')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail(TeaModel):
    def __init__(self, end_time=None, message=None, start_time=None, state=None, table=None):
        self.end_time = end_time  # type: str
        self.message = message  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.message is not None:
            result['Message'] = self.message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetails(TeaModel):
    def __init__(self, restore_schema_detail=None):
        self.restore_schema_detail = restore_schema_detail  # type: list[DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail]

    def validate(self):
        if self.restore_schema_detail:
            for k in self.restore_schema_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RestoreSchemaDetail'] = []
        if self.restore_schema_detail is not None:
            for k in self.restore_schema_detail:
                result['RestoreSchemaDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.restore_schema_detail = []
        if m.get('RestoreSchemaDetail') is not None:
            for k in m.get('RestoreSchemaDetail'):
                temp_model = DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail()
                self.restore_schema_detail.append(temp_model.from_map(k))
        return self


class DescribeRestoreTablesResponseBodyRestoreSchema(TeaModel):
    def __init__(self, fail=None, page_number=None, page_size=None, restore_schema_details=None, succeed=None,
                 total=None):
        self.fail = fail  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.restore_schema_details = restore_schema_details  # type: DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetails
        self.succeed = succeed  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.restore_schema_details:
            self.restore_schema_details.validate()

    def to_map(self):
        _map = super(DescribeRestoreTablesResponseBodyRestoreSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.restore_schema_details is not None:
            result['RestoreSchemaDetails'] = self.restore_schema_details.to_map()
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RestoreSchemaDetails') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetails()
            self.restore_schema_details = temp_model.from_map(m['RestoreSchemaDetails'])
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRestoreTablesResponseBodyRestoreSummary(TeaModel):
    def __init__(self, end_time=None, record_id=None, restore_to_date=None, start_time=None, state=None,
                 target_cluster=None):
        self.end_time = end_time  # type: str
        self.record_id = record_id  # type: str
        self.restore_to_date = restore_to_date  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str
        self.target_cluster = target_cluster  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreTablesResponseBodyRestoreSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.restore_to_date is not None:
            result['RestoreToDate'] = self.restore_to_date
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.target_cluster is not None:
            result['TargetCluster'] = self.target_cluster
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RestoreToDate') is not None:
            self.restore_to_date = m.get('RestoreToDate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TargetCluster') is not None:
            self.target_cluster = m.get('TargetCluster')
        return self


class DescribeRestoreTablesResponseBodyTables(TeaModel):
    def __init__(self, table=None):
        self.table = table  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRestoreTablesResponseBodyTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeRestoreTablesResponseBody(TeaModel):
    def __init__(self, request_id=None, restore_full=None, restore_incr_detail=None, restore_schema=None,
                 restore_summary=None, tables=None):
        self.request_id = request_id  # type: str
        self.restore_full = restore_full  # type: DescribeRestoreTablesResponseBodyRestoreFull
        self.restore_incr_detail = restore_incr_detail  # type: DescribeRestoreTablesResponseBodyRestoreIncrDetail
        self.restore_schema = restore_schema  # type: DescribeRestoreTablesResponseBodyRestoreSchema
        self.restore_summary = restore_summary  # type: DescribeRestoreTablesResponseBodyRestoreSummary
        self.tables = tables  # type: DescribeRestoreTablesResponseBodyTables

    def validate(self):
        if self.restore_full:
            self.restore_full.validate()
        if self.restore_incr_detail:
            self.restore_incr_detail.validate()
        if self.restore_schema:
            self.restore_schema.validate()
        if self.restore_summary:
            self.restore_summary.validate()
        if self.tables:
            self.tables.validate()

    def to_map(self):
        _map = super(DescribeRestoreTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_full is not None:
            result['RestoreFull'] = self.restore_full.to_map()
        if self.restore_incr_detail is not None:
            result['RestoreIncrDetail'] = self.restore_incr_detail.to_map()
        if self.restore_schema is not None:
            result['RestoreSchema'] = self.restore_schema.to_map()
        if self.restore_summary is not None:
            result['RestoreSummary'] = self.restore_summary.to_map()
        if self.tables is not None:
            result['Tables'] = self.tables.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreFull') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreFull()
            self.restore_full = temp_model.from_map(m['RestoreFull'])
        if m.get('RestoreIncrDetail') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreIncrDetail()
            self.restore_incr_detail = temp_model.from_map(m['RestoreIncrDetail'])
        if m.get('RestoreSchema') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreSchema()
            self.restore_schema = temp_model.from_map(m['RestoreSchema'])
        if m.get('RestoreSummary') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreSummary()
            self.restore_summary = temp_model.from_map(m['RestoreSummary'])
        if m.get('Tables') is not None:
            temp_model = DescribeRestoreTablesResponseBodyTables()
            self.tables = temp_model.from_map(m['Tables'])
        return self


class DescribeRestoreTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRestoreTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRestoreTablesResponse, self).to_map()
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
            temp_model = DescribeRestoreTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityGroupsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeSecurityGroupsResponseBodySecurityGroupIds(TeaModel):
    def __init__(self, security_group_id=None):
        self.security_group_id = security_group_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityGroupsResponseBodySecurityGroupIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DescribeSecurityGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, security_group_ids=None):
        self.request_id = request_id  # type: str
        self.security_group_ids = security_group_ids  # type: DescribeSecurityGroupsResponseBodySecurityGroupIds

    def validate(self):
        if self.security_group_ids:
            self.security_group_ids.validate()

    def to_map(self):
        _map = super(DescribeSecurityGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupIds') is not None:
            temp_model = DescribeSecurityGroupsResponseBodySecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m['SecurityGroupIds'])
        return self


class DescribeSecurityGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecurityGroupsResponse, self).to_map()
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
            temp_model = DescribeSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServerlessClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, zone_id=None):
        self.cluster_id = cluster_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServerlessClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeServerlessClusterResponseBody(TeaModel):
    def __init__(self, auto_renew=None, cluster_type=None, create_time=None, cu_size=None, disk_size=None,
                 expire_time=None, ha_type=None, has_user=None, inner_endpoint=None, instance_id=None, instance_name=None,
                 is_deletion_protection=None, lock_mode=None, main_version=None, outer_endpoint=None, pay_type=None, region_id=None,
                 request_id=None, reserver_max_qps_num=None, reserver_min_qps_num=None, resource_group_id=None, status=None,
                 update_status=None, v_switch_id=None, vpc_id=None, zone_id=None):
        self.auto_renew = auto_renew  # type: str
        self.cluster_type = cluster_type  # type: str
        self.create_time = create_time  # type: str
        self.cu_size = cu_size  # type: str
        self.disk_size = disk_size  # type: str
        self.expire_time = expire_time  # type: str
        self.ha_type = ha_type  # type: str
        self.has_user = has_user  # type: str
        self.inner_endpoint = inner_endpoint  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.is_deletion_protection = is_deletion_protection  # type: str
        self.lock_mode = lock_mode  # type: str
        self.main_version = main_version  # type: str
        self.outer_endpoint = outer_endpoint  # type: str
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.reserver_max_qps_num = reserver_max_qps_num  # type: str
        self.reserver_min_qps_num = reserver_min_qps_num  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.update_status = update_status  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServerlessClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cu_size is not None:
            result['CuSize'] = self.cu_size
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ha_type is not None:
            result['HaType'] = self.ha_type
        if self.has_user is not None:
            result['HasUser'] = self.has_user
        if self.inner_endpoint is not None:
            result['InnerEndpoint'] = self.inner_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_deletion_protection is not None:
            result['IsDeletionProtection'] = self.is_deletion_protection
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.main_version is not None:
            result['MainVersion'] = self.main_version
        if self.outer_endpoint is not None:
            result['OuterEndpoint'] = self.outer_endpoint
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reserver_max_qps_num is not None:
            result['ReserverMaxQpsNum'] = self.reserver_max_qps_num
        if self.reserver_min_qps_num is not None:
            result['ReserverMinQpsNum'] = self.reserver_min_qps_num
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_status is not None:
            result['UpdateStatus'] = self.update_status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CuSize') is not None:
            self.cu_size = m.get('CuSize')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HaType') is not None:
            self.ha_type = m.get('HaType')
        if m.get('HasUser') is not None:
            self.has_user = m.get('HasUser')
        if m.get('InnerEndpoint') is not None:
            self.inner_endpoint = m.get('InnerEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsDeletionProtection') is not None:
            self.is_deletion_protection = m.get('IsDeletionProtection')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MainVersion') is not None:
            self.main_version = m.get('MainVersion')
        if m.get('OuterEndpoint') is not None:
            self.outer_endpoint = m.get('OuterEndpoint')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReserverMaxQpsNum') is not None:
            self.reserver_max_qps_num = m.get('ReserverMaxQpsNum')
        if m.get('ReserverMinQpsNum') is not None:
            self.reserver_min_qps_num = m.get('ReserverMinQpsNum')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateStatus') is not None:
            self.update_status = m.get('UpdateStatus')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeServerlessClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeServerlessClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServerlessClusterResponse, self).to_map()
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
            temp_model = DescribeServerlessClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubDomainRequest(TeaModel):
    def __init__(self, region_id=None, zone_id=None):
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSubDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeSubDomainResponseBody(TeaModel):
    def __init__(self, request_id=None, sub_domain=None):
        self.request_id = request_id  # type: str
        self.sub_domain = sub_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSubDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class DescribeSubDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSubDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSubDomainResponse, self).to_map()
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
            temp_model = DescribeSubDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableHBaseueBackupRequest(TeaModel):
    def __init__(self, client_token=None, cold_storage_size=None, hbaseue_cluster_id=None, node_count=None):
        self.client_token = client_token  # type: str
        self.cold_storage_size = cold_storage_size  # type: int
        self.hbaseue_cluster_id = hbaseue_cluster_id  # type: str
        self.node_count = node_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableHBaseueBackupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size
        if self.hbaseue_cluster_id is not None:
            result['HbaseueClusterId'] = self.hbaseue_cluster_id
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')
        if m.get('HbaseueClusterId') is not None:
            self.hbaseue_cluster_id = m.get('HbaseueClusterId')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        return self


class EnableHBaseueBackupResponseBody(TeaModel):
    def __init__(self, cluster_id=None, order_id=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableHBaseueBackupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableHBaseueBackupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableHBaseueBackupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableHBaseueBackupResponse, self).to_map()
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
            temp_model = EnableHBaseueBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableHBaseueModuleRequest(TeaModel):
    def __init__(self, auto_renew_period=None, bds_id=None, client_token=None, core_instance_type=None,
                 disk_size=None, disk_type=None, hbaseue_cluster_id=None, master_instance_type=None,
                 module_cluster_name=None, module_type_name=None, node_count=None, pay_type=None, period=None, period_unit=None,
                 region_id=None, vpc_id=None, vswitch_id=None, zone_id=None):
        self.auto_renew_period = auto_renew_period  # type: int
        self.bds_id = bds_id  # type: str
        self.client_token = client_token  # type: str
        self.core_instance_type = core_instance_type  # type: str
        self.disk_size = disk_size  # type: int
        self.disk_type = disk_type  # type: str
        self.hbaseue_cluster_id = hbaseue_cluster_id  # type: str
        self.master_instance_type = master_instance_type  # type: str
        self.module_cluster_name = module_cluster_name  # type: str
        self.module_type_name = module_type_name  # type: str
        self.node_count = node_count  # type: int
        self.pay_type = pay_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableHBaseueModuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.hbaseue_cluster_id is not None:
            result['HbaseueClusterId'] = self.hbaseue_cluster_id
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.module_cluster_name is not None:
            result['ModuleClusterName'] = self.module_cluster_name
        if self.module_type_name is not None:
            result['ModuleTypeName'] = self.module_type_name
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HbaseueClusterId') is not None:
            self.hbaseue_cluster_id = m.get('HbaseueClusterId')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('ModuleClusterName') is not None:
            self.module_cluster_name = m.get('ModuleClusterName')
        if m.get('ModuleTypeName') is not None:
            self.module_type_name = m.get('ModuleTypeName')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class EnableHBaseueModuleResponseBody(TeaModel):
    def __init__(self, cluster_id=None, order_id=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableHBaseueModuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableHBaseueModuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableHBaseueModuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableHBaseueModuleResponse, self).to_map()
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
            temp_model = EnableHBaseueModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvaluateMultiZoneResourceRequest(TeaModel):
    def __init__(self, arbiter_vswitch_id=None, arbiter_zone_id=None, arch_version=None, auto_renew_period=None,
                 client_token=None, cluster_name=None, core_disk_size=None, core_disk_type=None, core_instance_type=None,
                 core_node_count=None, engine=None, engine_version=None, log_disk_size=None, log_disk_type=None,
                 log_instance_type=None, log_node_count=None, master_instance_type=None, multi_zone_combination=None, pay_type=None,
                 period=None, period_unit=None, primary_vswitch_id=None, primary_zone_id=None, region_id=None,
                 security_iplist=None, standby_vswitch_id=None, standby_zone_id=None, vpc_id=None):
        self.arbiter_vswitch_id = arbiter_vswitch_id  # type: str
        self.arbiter_zone_id = arbiter_zone_id  # type: str
        self.arch_version = arch_version  # type: str
        self.auto_renew_period = auto_renew_period  # type: int
        self.client_token = client_token  # type: str
        self.cluster_name = cluster_name  # type: str
        self.core_disk_size = core_disk_size  # type: int
        self.core_disk_type = core_disk_type  # type: str
        self.core_instance_type = core_instance_type  # type: str
        self.core_node_count = core_node_count  # type: int
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.log_disk_size = log_disk_size  # type: int
        self.log_disk_type = log_disk_type  # type: str
        self.log_instance_type = log_instance_type  # type: str
        self.log_node_count = log_node_count  # type: int
        self.master_instance_type = master_instance_type  # type: str
        self.multi_zone_combination = multi_zone_combination  # type: str
        self.pay_type = pay_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.primary_vswitch_id = primary_vswitch_id  # type: str
        self.primary_zone_id = primary_zone_id  # type: str
        self.region_id = region_id  # type: str
        self.security_iplist = security_iplist  # type: str
        self.standby_vswitch_id = standby_vswitch_id  # type: str
        self.standby_zone_id = standby_zone_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EvaluateMultiZoneResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size
        if self.log_disk_type is not None:
            result['LogDiskType'] = self.log_disk_type
        if self.log_instance_type is not None:
            result['LogInstanceType'] = self.log_instance_type
        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')
        if m.get('LogDiskType') is not None:
            self.log_disk_type = m.get('LogDiskType')
        if m.get('LogInstanceType') is not None:
            self.log_instance_type = m.get('LogInstanceType')
        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class EvaluateMultiZoneResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EvaluateMultiZoneResourceResponseBody, self).to_map()
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


class EvaluateMultiZoneResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EvaluateMultiZoneResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EvaluateMultiZoneResourceResponse, self).to_map()
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
            temp_model = EvaluateMultiZoneResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultimodeCmsUrlRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMultimodeCmsUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetMultimodeCmsUrlResponseBody(TeaModel):
    def __init__(self, cluster_id=None, multimod_cms_url=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.multimod_cms_url = multimod_cms_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMultimodeCmsUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.multimod_cms_url is not None:
            result['MultimodCmsUrl'] = self.multimod_cms_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MultimodCmsUrl') is not None:
            self.multimod_cms_url = m.get('MultimodCmsUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMultimodeCmsUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMultimodeCmsUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMultimodeCmsUrlResponse, self).to_map()
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
            temp_model = GetMultimodeCmsUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHBaseInstancesRequest(TeaModel):
    def __init__(self, vpc_id=None):
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHBaseInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListHBaseInstancesResponseBodyInstancesInstance(TeaModel):
    def __init__(self, instance_id=None, instance_name=None, is_default=None):
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.is_default = is_default  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHBaseInstancesResponseBodyInstancesInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        return self


class ListHBaseInstancesResponseBodyInstances(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance  # type: list[ListHBaseInstancesResponseBodyInstancesInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHBaseInstancesResponseBodyInstances, self).to_map()
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
                temp_model = ListHBaseInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class ListHBaseInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None):
        self.instances = instances  # type: ListHBaseInstancesResponseBodyInstances
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super(ListHBaseInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = ListHBaseInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHBaseInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHBaseInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHBaseInstancesResponse, self).to_map()
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
            temp_model = ListHBaseInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceServiceConfigHistoriesRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceServiceConfigHistoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryListConfig(TeaModel):
    def __init__(self, configure_name=None, create_time=None, effective=None, new_value=None, old_value=None):
        self.configure_name = configure_name  # type: str
        self.create_time = create_time  # type: str
        self.effective = effective  # type: str
        self.new_value = new_value  # type: str
        self.old_value = old_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryListConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configure_name is not None:
            result['ConfigureName'] = self.configure_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigureName') is not None:
            self.configure_name = m.get('ConfigureName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        return self


class ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryList(TeaModel):
    def __init__(self, config=None):
        self.config = config  # type: list[ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryListConfig]

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Config'] = []
        if self.config is not None:
            for k in self.config:
                result['Config'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config = []
        if m.get('Config') is not None:
            for k in m.get('Config'):
                temp_model = ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryListConfig()
                self.config.append(temp_model.from_map(k))
        return self


class ListInstanceServiceConfigHistoriesResponseBody(TeaModel):
    def __init__(self, configure_history_list=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.configure_history_list = configure_history_list  # type: ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryList
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: long

    def validate(self):
        if self.configure_history_list:
            self.configure_history_list.validate()

    def to_map(self):
        _map = super(ListInstanceServiceConfigHistoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configure_history_list is not None:
            result['ConfigureHistoryList'] = self.configure_history_list.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigureHistoryList') is not None:
            temp_model = ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryList()
            self.configure_history_list = temp_model.from_map(m['ConfigureHistoryList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class ListInstanceServiceConfigHistoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstanceServiceConfigHistoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceServiceConfigHistoriesResponse, self).to_map()
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
            temp_model = ListInstanceServiceConfigHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceServiceConfigurationsRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceServiceConfigurationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInstanceServiceConfigurationsResponseBodyConfigureListConfig(TeaModel):
    def __init__(self, configure_name=None, configure_unit=None, default_value=None, description=None,
                 need_restart=None, running_value=None, value_range=None):
        self.configure_name = configure_name  # type: str
        self.configure_unit = configure_unit  # type: str
        self.default_value = default_value  # type: str
        self.description = description  # type: str
        self.need_restart = need_restart  # type: str
        self.running_value = running_value  # type: str
        self.value_range = value_range  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceServiceConfigurationsResponseBodyConfigureListConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configure_name is not None:
            result['ConfigureName'] = self.configure_name
        if self.configure_unit is not None:
            result['ConfigureUnit'] = self.configure_unit
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.need_restart is not None:
            result['NeedRestart'] = self.need_restart
        if self.running_value is not None:
            result['RunningValue'] = self.running_value
        if self.value_range is not None:
            result['ValueRange'] = self.value_range
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigureName') is not None:
            self.configure_name = m.get('ConfigureName')
        if m.get('ConfigureUnit') is not None:
            self.configure_unit = m.get('ConfigureUnit')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NeedRestart') is not None:
            self.need_restart = m.get('NeedRestart')
        if m.get('RunningValue') is not None:
            self.running_value = m.get('RunningValue')
        if m.get('ValueRange') is not None:
            self.value_range = m.get('ValueRange')
        return self


class ListInstanceServiceConfigurationsResponseBodyConfigureList(TeaModel):
    def __init__(self, config=None):
        self.config = config  # type: list[ListInstanceServiceConfigurationsResponseBodyConfigureListConfig]

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceServiceConfigurationsResponseBodyConfigureList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Config'] = []
        if self.config is not None:
            for k in self.config:
                result['Config'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config = []
        if m.get('Config') is not None:
            for k in m.get('Config'):
                temp_model = ListInstanceServiceConfigurationsResponseBodyConfigureListConfig()
                self.config.append(temp_model.from_map(k))
        return self


class ListInstanceServiceConfigurationsResponseBody(TeaModel):
    def __init__(self, configure_list=None, page_number=None, page_record_count=None, request_id=None,
                 total_record_count=None):
        self.configure_list = configure_list  # type: ListInstanceServiceConfigurationsResponseBodyConfigureList
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.total_record_count = total_record_count  # type: long

    def validate(self):
        if self.configure_list:
            self.configure_list.validate()

    def to_map(self):
        _map = super(ListInstanceServiceConfigurationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configure_list is not None:
            result['ConfigureList'] = self.configure_list.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigureList') is not None:
            temp_model = ListInstanceServiceConfigurationsResponseBodyConfigureList()
            self.configure_list = temp_model.from_map(m['ConfigureList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class ListInstanceServiceConfigurationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstanceServiceConfigurationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceServiceConfigurationsResponse, self).to_map()
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
            temp_model = ListInstanceServiceConfigurationsResponseBody()
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
    def __init__(self, next_token=None, region_id=None, resource_id=None, tag=None):
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsRequest, self).to_map()
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


class ListTagsResponseBodyTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsResponseBodyTagsTag, self).to_map()
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


class ListTagsResponseBodyTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[ListTagsResponseBodyTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsResponseBodyTags, self).to_map()
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
                temp_model = ListTagsResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None):
        self.request_id = request_id  # type: str
        self.tags = tags  # type: ListTagsResponseBodyTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(ListTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            temp_model = ListTagsResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class ListTagsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagsResponse, self).to_map()
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
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPlanConfigRequest(TeaModel):
    def __init__(self, cluster_id=None, full_backup_cycle=None, min_hfile_backup_count=None,
                 next_full_backup_date=None, tables=None):
        self.cluster_id = cluster_id  # type: str
        self.full_backup_cycle = full_backup_cycle  # type: str
        self.min_hfile_backup_count = min_hfile_backup_count  # type: str
        self.next_full_backup_date = next_full_backup_date  # type: str
        self.tables = tables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPlanConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.full_backup_cycle is not None:
            result['FullBackupCycle'] = self.full_backup_cycle
        if self.min_hfile_backup_count is not None:
            result['MinHFileBackupCount'] = self.min_hfile_backup_count
        if self.next_full_backup_date is not None:
            result['NextFullBackupDate'] = self.next_full_backup_date
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('FullBackupCycle') is not None:
            self.full_backup_cycle = m.get('FullBackupCycle')
        if m.get('MinHFileBackupCount') is not None:
            self.min_hfile_backup_count = m.get('MinHFileBackupCount')
        if m.get('NextFullBackupDate') is not None:
            self.next_full_backup_date = m.get('NextFullBackupDate')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class ModifyBackupPlanConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPlanConfigResponseBody, self).to_map()
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


class ModifyBackupPlanConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyBackupPlanConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBackupPlanConfigResponse, self).to_map()
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
            temp_model = ModifyBackupPlanConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, cluster_id=None, preferred_backup_end_time_utc=None, preferred_backup_period=None,
                 preferred_backup_start_time_utc=None, preferred_backup_time=None):
        self.cluster_id = cluster_id  # type: str
        self.preferred_backup_end_time_utc = preferred_backup_end_time_utc  # type: str
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.preferred_backup_start_time_utc = preferred_backup_start_time_utc  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.preferred_backup_end_time_utc is not None:
            result['PreferredBackupEndTimeUTC'] = self.preferred_backup_end_time_utc
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_start_time_utc is not None:
            result['PreferredBackupStartTimeUTC'] = self.preferred_backup_start_time_utc
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PreferredBackupEndTimeUTC') is not None:
            self.preferred_backup_end_time_utc = m.get('PreferredBackupEndTimeUTC')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupStartTimeUTC') is not None:
            self.preferred_backup_start_time_utc = m.get('PreferredBackupStartTimeUTC')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPolicyResponseBody, self).to_map()
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


class ModifyBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBackupPolicyResponse, self).to_map()
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
            temp_model = ModifyBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterDeletionProtectionRequest(TeaModel):
    def __init__(self, cluster_id=None, protection=None):
        self.cluster_id = cluster_id  # type: str
        self.protection = protection  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterDeletionProtectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.protection is not None:
            result['Protection'] = self.protection
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Protection') is not None:
            self.protection = m.get('Protection')
        return self


class ModifyClusterDeletionProtectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterDeletionProtectionResponseBody, self).to_map()
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


class ModifyClusterDeletionProtectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyClusterDeletionProtectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyClusterDeletionProtectionResponse, self).to_map()
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
            temp_model = ModifyClusterDeletionProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskWarningLineRequest(TeaModel):
    def __init__(self, cluster_id=None, warning_line=None):
        self.cluster_id = cluster_id  # type: str
        self.warning_line = warning_line  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDiskWarningLineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.warning_line is not None:
            result['WarningLine'] = self.warning_line
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('WarningLine') is not None:
            self.warning_line = m.get('WarningLine')
        return self


class ModifyDiskWarningLineResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDiskWarningLineResponseBody, self).to_map()
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


class ModifyDiskWarningLineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDiskWarningLineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDiskWarningLineResponse, self).to_map()
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
            temp_model = ModifyDiskWarningLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMaintainTimeRequest(TeaModel):
    def __init__(self, cluster_id=None, maintain_end_time=None, maintain_start_time=None):
        self.cluster_id = cluster_id  # type: str
        self.maintain_end_time = maintain_end_time  # type: str
        self.maintain_start_time = maintain_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        return self


class ModifyInstanceMaintainTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeResponseBody, self).to_map()
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


class ModifyInstanceMaintainTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceMaintainTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeResponse, self).to_map()
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
            temp_model = ModifyInstanceMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceNameRequest(TeaModel):
    def __init__(self, client_token=None, cluster_id=None, cluster_name=None, region_id=None, zone_id=None):
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ModifyInstanceNameResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceNameResponseBody, self).to_map()
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


class ModifyInstanceNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceNameResponse, self).to_map()
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
            temp_model = ModifyInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceServiceConfigRequest(TeaModel):
    def __init__(self, cluster_id=None, configure_name=None, configure_value=None, parameters=None, restart=None):
        self.cluster_id = cluster_id  # type: str
        self.configure_name = configure_name  # type: str
        self.configure_value = configure_value  # type: str
        self.parameters = parameters  # type: str
        self.restart = restart  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceServiceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.configure_name is not None:
            result['ConfigureName'] = self.configure_name
        if self.configure_value is not None:
            result['ConfigureValue'] = self.configure_value
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.restart is not None:
            result['Restart'] = self.restart
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConfigureName') is not None:
            self.configure_name = m.get('ConfigureName')
        if m.get('ConfigureValue') is not None:
            self.configure_value = m.get('ConfigureValue')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Restart') is not None:
            self.restart = m.get('Restart')
        return self


class ModifyInstanceServiceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceServiceConfigResponseBody, self).to_map()
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


class ModifyInstanceServiceConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceServiceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceServiceConfigResponse, self).to_map()
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
            temp_model = ModifyInstanceServiceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceTypeRequest(TeaModel):
    def __init__(self, cluster_id=None, core_instance_type=None, master_instance_type=None):
        self.cluster_id = cluster_id  # type: str
        self.core_instance_type = core_instance_type  # type: str
        self.master_instance_type = master_instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        return self


class ModifyInstanceTypeResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTypeResponseBody, self).to_map()
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


class ModifyInstanceTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceTypeResponse, self).to_map()
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
            temp_model = ModifyInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpWhitelistRequest(TeaModel):
    def __init__(self, cluster_id=None, group_name=None, ip_list=None, ip_version=None):
        self.cluster_id = cluster_id  # type: str
        self.group_name = group_name  # type: str
        self.ip_list = ip_list  # type: str
        self.ip_version = ip_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class ModifyIpWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpWhitelistResponseBody, self).to_map()
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


class ModifyIpWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyIpWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyIpWhitelistResponse, self).to_map()
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
            temp_model = ModifyIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMultiZoneClusterNodeTypeRequest(TeaModel):
    def __init__(self, cluster_id=None, core_instance_type=None, log_instance_type=None, master_instance_type=None):
        self.cluster_id = cluster_id  # type: str
        self.core_instance_type = core_instance_type  # type: str
        self.log_instance_type = log_instance_type  # type: str
        self.master_instance_type = master_instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMultiZoneClusterNodeTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.log_instance_type is not None:
            result['LogInstanceType'] = self.log_instance_type
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('LogInstanceType') is not None:
            self.log_instance_type = m.get('LogInstanceType')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        return self


class ModifyMultiZoneClusterNodeTypeResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMultiZoneClusterNodeTypeResponseBody, self).to_map()
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


class ModifyMultiZoneClusterNodeTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyMultiZoneClusterNodeTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyMultiZoneClusterNodeTypeResponse, self).to_map()
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
            temp_model = ModifyMultiZoneClusterNodeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupsRequest(TeaModel):
    def __init__(self, cluster_id=None, security_group_ids=None):
        self.cluster_id = cluster_id  # type: str
        self.security_group_ids = security_group_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class ModifySecurityGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityGroupsResponseBody, self).to_map()
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


class ModifySecurityGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifySecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySecurityGroupsResponse, self).to_map()
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
            temp_model = ModifySecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUIAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, cluster_id=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUIAccountPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ModifyUIAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUIAccountPasswordResponseBody, self).to_map()
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


class ModifyUIAccountPasswordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyUIAccountPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyUIAccountPasswordResponse, self).to_map()
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
            temp_model = ModifyUIAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, cluster_id=None, new_resource_group_id=None):
        self.cluster_id = cluster_id  # type: str
        self.new_resource_group_id = new_resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MoveResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenBackupRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenBackupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class OpenBackupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenBackupResponseBody, self).to_map()
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


class OpenBackupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenBackupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenBackupResponse, self).to_map()
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
            temp_model = OpenBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurgeInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PurgeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class PurgeInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PurgeInstanceResponseBody, self).to_map()
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


class PurgeInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PurgeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PurgeInstanceResponse, self).to_map()
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
            temp_model = PurgeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHBaseHaDBRequest(TeaModel):
    def __init__(self, bds_id=None):
        self.bds_id = bds_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHBaseHaDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        return self


class QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnListHaSlbConn(TeaModel):
    def __init__(self, hbase_type=None, slb_conn_addr=None, slb_type=None):
        self.hbase_type = hbase_type  # type: str
        self.slb_conn_addr = slb_conn_addr  # type: str
        self.slb_type = slb_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnListHaSlbConn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hbase_type is not None:
            result['HbaseType'] = self.hbase_type
        if self.slb_conn_addr is not None:
            result['SlbConnAddr'] = self.slb_conn_addr
        if self.slb_type is not None:
            result['SlbType'] = self.slb_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HbaseType') is not None:
            self.hbase_type = m.get('HbaseType')
        if m.get('SlbConnAddr') is not None:
            self.slb_conn_addr = m.get('SlbConnAddr')
        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')
        return self


class QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnList(TeaModel):
    def __init__(self, ha_slb_conn=None):
        self.ha_slb_conn = ha_slb_conn  # type: list[QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnListHaSlbConn]

    def validate(self):
        if self.ha_slb_conn:
            for k in self.ha_slb_conn:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HaSlbConn'] = []
        if self.ha_slb_conn is not None:
            for k in self.ha_slb_conn:
                result['HaSlbConn'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ha_slb_conn = []
        if m.get('HaSlbConn') is not None:
            for k in m.get('HaSlbConn'):
                temp_model = QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnListHaSlbConn()
                self.ha_slb_conn.append(temp_model.from_map(k))
        return self


class QueryHBaseHaDBResponseBodyClusterListCluster(TeaModel):
    def __init__(self, active_name=None, bds_name=None, ha_name=None, ha_slb_conn_list=None, standby_name=None):
        self.active_name = active_name  # type: str
        self.bds_name = bds_name  # type: str
        self.ha_name = ha_name  # type: str
        self.ha_slb_conn_list = ha_slb_conn_list  # type: QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnList
        self.standby_name = standby_name  # type: str

    def validate(self):
        if self.ha_slb_conn_list:
            self.ha_slb_conn_list.validate()

    def to_map(self):
        _map = super(QueryHBaseHaDBResponseBodyClusterListCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_name is not None:
            result['ActiveName'] = self.active_name
        if self.bds_name is not None:
            result['BdsName'] = self.bds_name
        if self.ha_name is not None:
            result['HaName'] = self.ha_name
        if self.ha_slb_conn_list is not None:
            result['HaSlbConnList'] = self.ha_slb_conn_list.to_map()
        if self.standby_name is not None:
            result['StandbyName'] = self.standby_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveName') is not None:
            self.active_name = m.get('ActiveName')
        if m.get('BdsName') is not None:
            self.bds_name = m.get('BdsName')
        if m.get('HaName') is not None:
            self.ha_name = m.get('HaName')
        if m.get('HaSlbConnList') is not None:
            temp_model = QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnList()
            self.ha_slb_conn_list = temp_model.from_map(m['HaSlbConnList'])
        if m.get('StandbyName') is not None:
            self.standby_name = m.get('StandbyName')
        return self


class QueryHBaseHaDBResponseBodyClusterList(TeaModel):
    def __init__(self, cluster=None):
        self.cluster = cluster  # type: list[QueryHBaseHaDBResponseBodyClusterListCluster]

    def validate(self):
        if self.cluster:
            for k in self.cluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryHBaseHaDBResponseBodyClusterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cluster'] = []
        if self.cluster is not None:
            for k in self.cluster:
                result['Cluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k in m.get('Cluster'):
                temp_model = QueryHBaseHaDBResponseBodyClusterListCluster()
                self.cluster.append(temp_model.from_map(k))
        return self


class QueryHBaseHaDBResponseBody(TeaModel):
    def __init__(self, cluster_list=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.cluster_list = cluster_list  # type: QueryHBaseHaDBResponseBodyClusterList
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.cluster_list:
            self.cluster_list.validate()

    def to_map(self):
        _map = super(QueryHBaseHaDBResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_list is not None:
            result['ClusterList'] = self.cluster_list.to_map()
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
        if m.get('ClusterList') is not None:
            temp_model = QueryHBaseHaDBResponseBodyClusterList()
            self.cluster_list = temp_model.from_map(m['ClusterList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryHBaseHaDBResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryHBaseHaDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryHBaseHaDBResponse, self).to_map()
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
            temp_model = QueryHBaseHaDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryXpackRelateDBRequest(TeaModel):
    def __init__(self, cluster_id=None, has_single_node=None, relate_db_type=None):
        self.cluster_id = cluster_id  # type: str
        self.has_single_node = has_single_node  # type: bool
        self.relate_db_type = relate_db_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryXpackRelateDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.has_single_node is not None:
            result['HasSingleNode'] = self.has_single_node
        if self.relate_db_type is not None:
            result['RelateDbType'] = self.relate_db_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HasSingleNode') is not None:
            self.has_single_node = m.get('HasSingleNode')
        if m.get('RelateDbType') is not None:
            self.relate_db_type = m.get('RelateDbType')
        return self


class QueryXpackRelateDBResponseBodyClusterListCluster(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, dbtype=None, dbversion=None, is_related=None,
                 lock_mode=None, status=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.dbtype = dbtype  # type: str
        self.dbversion = dbversion  # type: str
        self.is_related = is_related  # type: bool
        self.lock_mode = lock_mode  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryXpackRelateDBResponseBodyClusterListCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.is_related is not None:
            result['IsRelated'] = self.is_related
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('IsRelated') is not None:
            self.is_related = m.get('IsRelated')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryXpackRelateDBResponseBodyClusterList(TeaModel):
    def __init__(self, cluster=None):
        self.cluster = cluster  # type: list[QueryXpackRelateDBResponseBodyClusterListCluster]

    def validate(self):
        if self.cluster:
            for k in self.cluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryXpackRelateDBResponseBodyClusterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cluster'] = []
        if self.cluster is not None:
            for k in self.cluster:
                result['Cluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k in m.get('Cluster'):
                temp_model = QueryXpackRelateDBResponseBodyClusterListCluster()
                self.cluster.append(temp_model.from_map(k))
        return self


class QueryXpackRelateDBResponseBody(TeaModel):
    def __init__(self, cluster_list=None, request_id=None):
        self.cluster_list = cluster_list  # type: QueryXpackRelateDBResponseBodyClusterList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cluster_list:
            self.cluster_list.validate()

    def to_map(self):
        _map = super(QueryXpackRelateDBResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_list is not None:
            result['ClusterList'] = self.cluster_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterList') is not None:
            temp_model = QueryXpackRelateDBResponseBodyClusterList()
            self.cluster_list = temp_model.from_map(m['ClusterList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryXpackRelateDBResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryXpackRelateDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryXpackRelateDBResponse, self).to_map()
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
            temp_model = QueryXpackRelateDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RelateDbForHBaseHaRequest(TeaModel):
    def __init__(self, cluster_id=None, ha_active=None, ha_active_cluster_key=None, ha_active_dbtype=None,
                 ha_active_hbase_fs_dir=None, ha_active_hdfs_uri=None, ha_active_password=None, ha_active_user=None,
                 ha_active_version=None, ha_migrate_type=None, ha_standby=None, ha_standby_cluster_key=None, ha_standby_dbtype=None,
                 ha_standby_hbase_fs_dir=None, ha_standby_hdfs_uri=None, ha_standby_password=None, ha_standby_user=None,
                 ha_standby_version=None, ha_tables=None, is_active_standard=None, is_standby_standard=None):
        self.cluster_id = cluster_id  # type: str
        self.ha_active = ha_active  # type: str
        self.ha_active_cluster_key = ha_active_cluster_key  # type: str
        self.ha_active_dbtype = ha_active_dbtype  # type: str
        self.ha_active_hbase_fs_dir = ha_active_hbase_fs_dir  # type: str
        self.ha_active_hdfs_uri = ha_active_hdfs_uri  # type: str
        self.ha_active_password = ha_active_password  # type: str
        self.ha_active_user = ha_active_user  # type: str
        self.ha_active_version = ha_active_version  # type: str
        self.ha_migrate_type = ha_migrate_type  # type: str
        self.ha_standby = ha_standby  # type: str
        self.ha_standby_cluster_key = ha_standby_cluster_key  # type: str
        self.ha_standby_dbtype = ha_standby_dbtype  # type: str
        self.ha_standby_hbase_fs_dir = ha_standby_hbase_fs_dir  # type: str
        self.ha_standby_hdfs_uri = ha_standby_hdfs_uri  # type: str
        self.ha_standby_password = ha_standby_password  # type: str
        self.ha_standby_user = ha_standby_user  # type: str
        self.ha_standby_version = ha_standby_version  # type: str
        self.ha_tables = ha_tables  # type: str
        self.is_active_standard = is_active_standard  # type: bool
        self.is_standby_standard = is_standby_standard  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RelateDbForHBaseHaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ha_active is not None:
            result['HaActive'] = self.ha_active
        if self.ha_active_cluster_key is not None:
            result['HaActiveClusterKey'] = self.ha_active_cluster_key
        if self.ha_active_dbtype is not None:
            result['HaActiveDBType'] = self.ha_active_dbtype
        if self.ha_active_hbase_fs_dir is not None:
            result['HaActiveHbaseFsDir'] = self.ha_active_hbase_fs_dir
        if self.ha_active_hdfs_uri is not None:
            result['HaActiveHdfsUri'] = self.ha_active_hdfs_uri
        if self.ha_active_password is not None:
            result['HaActivePassword'] = self.ha_active_password
        if self.ha_active_user is not None:
            result['HaActiveUser'] = self.ha_active_user
        if self.ha_active_version is not None:
            result['HaActiveVersion'] = self.ha_active_version
        if self.ha_migrate_type is not None:
            result['HaMigrateType'] = self.ha_migrate_type
        if self.ha_standby is not None:
            result['HaStandby'] = self.ha_standby
        if self.ha_standby_cluster_key is not None:
            result['HaStandbyClusterKey'] = self.ha_standby_cluster_key
        if self.ha_standby_dbtype is not None:
            result['HaStandbyDBType'] = self.ha_standby_dbtype
        if self.ha_standby_hbase_fs_dir is not None:
            result['HaStandbyHbaseFsDir'] = self.ha_standby_hbase_fs_dir
        if self.ha_standby_hdfs_uri is not None:
            result['HaStandbyHdfsUri'] = self.ha_standby_hdfs_uri
        if self.ha_standby_password is not None:
            result['HaStandbyPassword'] = self.ha_standby_password
        if self.ha_standby_user is not None:
            result['HaStandbyUser'] = self.ha_standby_user
        if self.ha_standby_version is not None:
            result['HaStandbyVersion'] = self.ha_standby_version
        if self.ha_tables is not None:
            result['HaTables'] = self.ha_tables
        if self.is_active_standard is not None:
            result['IsActiveStandard'] = self.is_active_standard
        if self.is_standby_standard is not None:
            result['IsStandbyStandard'] = self.is_standby_standard
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HaActive') is not None:
            self.ha_active = m.get('HaActive')
        if m.get('HaActiveClusterKey') is not None:
            self.ha_active_cluster_key = m.get('HaActiveClusterKey')
        if m.get('HaActiveDBType') is not None:
            self.ha_active_dbtype = m.get('HaActiveDBType')
        if m.get('HaActiveHbaseFsDir') is not None:
            self.ha_active_hbase_fs_dir = m.get('HaActiveHbaseFsDir')
        if m.get('HaActiveHdfsUri') is not None:
            self.ha_active_hdfs_uri = m.get('HaActiveHdfsUri')
        if m.get('HaActivePassword') is not None:
            self.ha_active_password = m.get('HaActivePassword')
        if m.get('HaActiveUser') is not None:
            self.ha_active_user = m.get('HaActiveUser')
        if m.get('HaActiveVersion') is not None:
            self.ha_active_version = m.get('HaActiveVersion')
        if m.get('HaMigrateType') is not None:
            self.ha_migrate_type = m.get('HaMigrateType')
        if m.get('HaStandby') is not None:
            self.ha_standby = m.get('HaStandby')
        if m.get('HaStandbyClusterKey') is not None:
            self.ha_standby_cluster_key = m.get('HaStandbyClusterKey')
        if m.get('HaStandbyDBType') is not None:
            self.ha_standby_dbtype = m.get('HaStandbyDBType')
        if m.get('HaStandbyHbaseFsDir') is not None:
            self.ha_standby_hbase_fs_dir = m.get('HaStandbyHbaseFsDir')
        if m.get('HaStandbyHdfsUri') is not None:
            self.ha_standby_hdfs_uri = m.get('HaStandbyHdfsUri')
        if m.get('HaStandbyPassword') is not None:
            self.ha_standby_password = m.get('HaStandbyPassword')
        if m.get('HaStandbyUser') is not None:
            self.ha_standby_user = m.get('HaStandbyUser')
        if m.get('HaStandbyVersion') is not None:
            self.ha_standby_version = m.get('HaStandbyVersion')
        if m.get('HaTables') is not None:
            self.ha_tables = m.get('HaTables')
        if m.get('IsActiveStandard') is not None:
            self.is_active_standard = m.get('IsActiveStandard')
        if m.get('IsStandbyStandard') is not None:
            self.is_standby_standard = m.get('IsStandbyStandard')
        return self


class RelateDbForHBaseHaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RelateDbForHBaseHaResponseBody, self).to_map()
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


class RelateDbForHBaseHaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RelateDbForHBaseHaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RelateDbForHBaseHaResponse, self).to_map()
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
            temp_model = RelateDbForHBaseHaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePublicNetworkAddressRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleasePublicNetworkAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ReleasePublicNetworkAddressResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleasePublicNetworkAddressResponseBody, self).to_map()
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


class ReleasePublicNetworkAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReleasePublicNetworkAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleasePublicNetworkAddressResponse, self).to_map()
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
            temp_model = ReleasePublicNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None, duration=None, pricing_cycle=None):
        self.cluster_id = cluster_id  # type: str
        self.duration = duration  # type: int
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceResponseBody, self).to_map()
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


class RenewInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RenewInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeColdStorageSizeRequest(TeaModel):
    def __init__(self, cluster_id=None, cold_storage_size=None):
        self.cluster_id = cluster_id  # type: str
        self.cold_storage_size = cold_storage_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeColdStorageSizeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')
        return self


class ResizeColdStorageSizeResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeColdStorageSizeResponseBody, self).to_map()
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


class ResizeColdStorageSizeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResizeColdStorageSizeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResizeColdStorageSizeResponse, self).to_map()
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
            temp_model = ResizeColdStorageSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeDiskSizeRequest(TeaModel):
    def __init__(self, cluster_id=None, node_disk_size=None):
        self.cluster_id = cluster_id  # type: str
        self.node_disk_size = node_disk_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeDiskSizeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node_disk_size is not None:
            result['NodeDiskSize'] = self.node_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NodeDiskSize') is not None:
            self.node_disk_size = m.get('NodeDiskSize')
        return self


class ResizeDiskSizeResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeDiskSizeResponseBody, self).to_map()
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


class ResizeDiskSizeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResizeDiskSizeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResizeDiskSizeResponse, self).to_map()
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
            temp_model = ResizeDiskSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeMultiZoneClusterDiskSizeRequest(TeaModel):
    def __init__(self, cluster_id=None, core_disk_size=None, log_disk_size=None):
        self.cluster_id = cluster_id  # type: str
        self.core_disk_size = core_disk_size  # type: int
        self.log_disk_size = log_disk_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeMultiZoneClusterDiskSizeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')
        return self


class ResizeMultiZoneClusterDiskSizeResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeMultiZoneClusterDiskSizeResponseBody, self).to_map()
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


class ResizeMultiZoneClusterDiskSizeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResizeMultiZoneClusterDiskSizeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResizeMultiZoneClusterDiskSizeResponse, self).to_map()
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
            temp_model = ResizeMultiZoneClusterDiskSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeMultiZoneClusterNodeCountRequest(TeaModel):
    def __init__(self, arbiter_vswitch_id=None, cluster_id=None, core_node_count=None, log_node_count=None,
                 primary_core_node_count=None, primary_vswitch_id=None, standby_core_node_count=None, standby_vswitch_id=None):
        self.arbiter_vswitch_id = arbiter_vswitch_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.core_node_count = core_node_count  # type: int
        self.log_node_count = log_node_count  # type: int
        self.primary_core_node_count = primary_core_node_count  # type: int
        self.primary_vswitch_id = primary_vswitch_id  # type: str
        self.standby_core_node_count = standby_core_node_count  # type: int
        self.standby_vswitch_id = standby_vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeMultiZoneClusterNodeCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count
        if self.primary_core_node_count is not None:
            result['PrimaryCoreNodeCount'] = self.primary_core_node_count
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.standby_core_node_count is not None:
            result['StandbyCoreNodeCount'] = self.standby_core_node_count
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')
        if m.get('PrimaryCoreNodeCount') is not None:
            self.primary_core_node_count = m.get('PrimaryCoreNodeCount')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('StandbyCoreNodeCount') is not None:
            self.standby_core_node_count = m.get('StandbyCoreNodeCount')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        return self


class ResizeMultiZoneClusterNodeCountResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeMultiZoneClusterNodeCountResponseBody, self).to_map()
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


class ResizeMultiZoneClusterNodeCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResizeMultiZoneClusterNodeCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResizeMultiZoneClusterNodeCountResponse, self).to_map()
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
            temp_model = ResizeMultiZoneClusterNodeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeNodeCountRequest(TeaModel):
    def __init__(self, cluster_id=None, node_count=None, v_switch_id=None, zone_id=None):
        self.cluster_id = cluster_id  # type: str
        self.node_count = node_count  # type: int
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeNodeCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ResizeNodeCountResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeNodeCountResponseBody, self).to_map()
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


class ResizeNodeCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResizeNodeCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResizeNodeCountResponse, self).to_map()
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
            temp_model = ResizeNodeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None, components=None):
        self.cluster_id = cluster_id  # type: str
        self.components = components  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.components is not None:
            result['Components'] = self.components
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        return self


class RestartInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceResponseBody, self).to_map()
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


class RestartInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchHbaseHaSlbRequest(TeaModel):
    def __init__(self, bds_id=None, ha_id=None, ha_types=None, hbase_type=None):
        self.bds_id = bds_id  # type: str
        self.ha_id = ha_id  # type: str
        self.ha_types = ha_types  # type: str
        self.hbase_type = hbase_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchHbaseHaSlbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        if self.ha_id is not None:
            result['HaId'] = self.ha_id
        if self.ha_types is not None:
            result['HaTypes'] = self.ha_types
        if self.hbase_type is not None:
            result['HbaseType'] = self.hbase_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        if m.get('HaId') is not None:
            self.ha_id = m.get('HaId')
        if m.get('HaTypes') is not None:
            self.ha_types = m.get('HaTypes')
        if m.get('HbaseType') is not None:
            self.hbase_type = m.get('HbaseType')
        return self


class SwitchHbaseHaSlbResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchHbaseHaSlbResponseBody, self).to_map()
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


class SwitchHbaseHaSlbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SwitchHbaseHaSlbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchHbaseHaSlbResponse, self).to_map()
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
            temp_model = SwitchHbaseHaSlbResponseBody()
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
    def __init__(self, region_id=None, resource_id=None, tag=None):
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnTagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_id=None, tag_key=None):
        self.all = all  # type: bool
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UnTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnTagResourcesResponseBody, self).to_map()
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


class UnTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnTagResourcesResponse, self).to_map()
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
            temp_model = UnTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMinorVersionRequest(TeaModel):
    def __init__(self, cluster_id=None, components=None):
        self.cluster_id = cluster_id  # type: str
        self.components = components  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeMinorVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.components is not None:
            result['Components'] = self.components
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        return self


class UpgradeMinorVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, upgrading_components=None):
        self.request_id = request_id  # type: str
        self.upgrading_components = upgrading_components  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeMinorVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upgrading_components is not None:
            result['UpgradingComponents'] = self.upgrading_components
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpgradingComponents') is not None:
            self.upgrading_components = m.get('UpgradingComponents')
        return self


class UpgradeMinorVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeMinorVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeMinorVersionResponse, self).to_map()
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
            temp_model = UpgradeMinorVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMultiZoneClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, components=None, restart_components=None, run_mode=None,
                 upgrade_ins_name=None, versions=None):
        self.cluster_id = cluster_id  # type: str
        self.components = components  # type: str
        self.restart_components = restart_components  # type: str
        self.run_mode = run_mode  # type: str
        self.upgrade_ins_name = upgrade_ins_name  # type: str
        self.versions = versions  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeMultiZoneClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.components is not None:
            result['Components'] = self.components
        if self.restart_components is not None:
            result['RestartComponents'] = self.restart_components
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        if self.upgrade_ins_name is not None:
            result['UpgradeInsName'] = self.upgrade_ins_name
        if self.versions is not None:
            result['Versions'] = self.versions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('RestartComponents') is not None:
            self.restart_components = m.get('RestartComponents')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        if m.get('UpgradeInsName') is not None:
            self.upgrade_ins_name = m.get('UpgradeInsName')
        if m.get('Versions') is not None:
            self.versions = m.get('Versions')
        return self


class UpgradeMultiZoneClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, upgrading_components=None):
        self.request_id = request_id  # type: str
        self.upgrading_components = upgrading_components  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeMultiZoneClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upgrading_components is not None:
            result['UpgradingComponents'] = self.upgrading_components
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpgradingComponents') is not None:
            self.upgrading_components = m.get('UpgradingComponents')
        return self


class UpgradeMultiZoneClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeMultiZoneClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeMultiZoneClusterResponse, self).to_map()
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
            temp_model = UpgradeMultiZoneClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class XpackRelateDBRequest(TeaModel):
    def __init__(self, cluster_id=None, db_cluster_ids=None, relate_db_type=None):
        self.cluster_id = cluster_id  # type: str
        self.db_cluster_ids = db_cluster_ids  # type: str
        self.relate_db_type = relate_db_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(XpackRelateDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_cluster_ids is not None:
            result['DbClusterIds'] = self.db_cluster_ids
        if self.relate_db_type is not None:
            result['RelateDbType'] = self.relate_db_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbClusterIds') is not None:
            self.db_cluster_ids = m.get('DbClusterIds')
        if m.get('RelateDbType') is not None:
            self.relate_db_type = m.get('RelateDbType')
        return self


class XpackRelateDBResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(XpackRelateDBResponseBody, self).to_map()
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


class XpackRelateDBResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: XpackRelateDBResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(XpackRelateDBResponse, self).to_map()
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
            temp_model = XpackRelateDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


