# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec(TeaModel):
    def __init__(self, cpu=None, memory_gb=None):
        # cpu数量。
        self.cpu = cpu  # type: int
        # 内存大小。
        self.memory_gb = memory_gb  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs(TeaModel):
    def __init__(self, namespace=None, resource_spec=None):
        # namespace名称，
        self.namespace = namespace  # type: str
        # 资源规格。
        self.resource_spec = resource_spec  # type: ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super(ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ResourceSpec') is not None:
            temp_model = ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ConvertInstanceRequestConvertPostpayInstanceRequest(TeaModel):
    def __init__(self, duration=None, instance_id=None, is_auto_renew=None, namespace_resource_specs=None,
                 pricing_cycle=None, region=None):
        # 订购周期数量
        self.duration = duration  # type: int
        self.instance_id = instance_id  # type: str
        # 是否自动续费
        self.is_auto_renew = is_auto_renew  # type: bool
        # 项目空间资源规格。
        self.namespace_resource_specs = namespace_resource_specs  # type: list[ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs]
        # 订购周期
        self.pricing_cycle = pricing_cycle  # type: str
        self.region = region  # type: str

    def validate(self):
        if self.namespace_resource_specs:
            for k in self.namespace_resource_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ConvertInstanceRequestConvertPostpayInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew
        result['NamespaceResourceSpecs'] = []
        if self.namespace_resource_specs is not None:
            for k in self.namespace_resource_specs:
                result['NamespaceResourceSpecs'].append(k.to_map() if k else None)
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsAutoRenew') is not None:
            self.is_auto_renew = m.get('IsAutoRenew')
        self.namespace_resource_specs = []
        if m.get('NamespaceResourceSpecs') is not None:
            for k in m.get('NamespaceResourceSpecs'):
                temp_model = ConvertInstanceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs()
                self.namespace_resource_specs.append(temp_model.from_map(k))
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ConvertInstanceRequest(TeaModel):
    def __init__(self, convert_postpay_instance_request=None):
        self.convert_postpay_instance_request = convert_postpay_instance_request  # type: ConvertInstanceRequestConvertPostpayInstanceRequest

    def validate(self):
        if self.convert_postpay_instance_request:
            self.convert_postpay_instance_request.validate()

    def to_map(self):
        _map = super(ConvertInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_postpay_instance_request is not None:
            result['ConvertPostpayInstanceRequest'] = self.convert_postpay_instance_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConvertPostpayInstanceRequest') is not None:
            temp_model = ConvertInstanceRequestConvertPostpayInstanceRequest()
            self.convert_postpay_instance_request = temp_model.from_map(m['ConvertPostpayInstanceRequest'])
        return self


class ConvertInstanceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None, success=None):
        # 订单id
        self.order_id = order_id  # type: long
        # 请求id
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class CreateInstanceRequestCreateInstanceRequestResourceSpec(TeaModel):
    def __init__(self, cpu=None, memory_gb=None):
        self.cpu = cpu  # type: int
        self.memory_gb = memory_gb  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestCreateInstanceRequestResourceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class CreateInstanceRequestCreateInstanceRequestStorageOss(TeaModel):
    def __init__(self, bucket=None):
        self.bucket = bucket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestCreateInstanceRequestStorageOss, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class CreateInstanceRequestCreateInstanceRequestStorage(TeaModel):
    def __init__(self, oss=None):
        self.oss = oss  # type: CreateInstanceRequestCreateInstanceRequestStorageOss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        _map = super(CreateInstanceRequestCreateInstanceRequestStorage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss is not None:
            result['Oss'] = self.oss.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Oss') is not None:
            temp_model = CreateInstanceRequestCreateInstanceRequestStorageOss()
            self.oss = temp_model.from_map(m['Oss'])
        return self


class CreateInstanceRequestCreateInstanceRequest(TeaModel):
    def __init__(self, auto_renew=None, charge_type=None, duration=None, instance_name=None, pricing_cycle=None,
                 region=None, resource_spec=None, storage=None, v_switch_ids=None, vpc_id=None, zone_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.charge_type = charge_type  # type: str
        self.duration = duration  # type: int
        self.instance_name = instance_name  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.region = region  # type: str
        self.resource_spec = resource_spec  # type: CreateInstanceRequestCreateInstanceRequestResourceSpec
        self.storage = storage  # type: CreateInstanceRequestCreateInstanceRequestStorage
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()

    def to_map(self):
        _map = super(CreateInstanceRequestCreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.storage is not None:
            result['Storage'] = self.storage.to_map()
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = CreateInstanceRequestCreateInstanceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('Storage') is not None:
            temp_model = CreateInstanceRequestCreateInstanceRequestStorage()
            self.storage = temp_model.from_map(m['Storage'])
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, create_instance_request=None):
        self.create_instance_request = create_instance_request  # type: CreateInstanceRequestCreateInstanceRequest

    def validate(self):
        if self.create_instance_request:
            self.create_instance_request.validate()

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_instance_request is not None:
            result['CreateInstanceRequest'] = self.create_instance_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateInstanceRequest') is not None:
            temp_model = CreateInstanceRequestCreateInstanceRequest()
            self.create_instance_request = temp_model.from_map(m['CreateInstanceRequest'])
        return self


class CreateInstanceResponseBodyOrderInfo(TeaModel):
    def __init__(self, instance_id=None, order_id=None):
        # 实例id
        self.instance_id = instance_id  # type: str
        # 订单id
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBodyOrderInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, order_info=None, request_id=None, success=None):
        # 订单信息
        self.order_info = order_info  # type: CreateInstanceResponseBodyOrderInfo
        # 请求id
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.order_info:
            self.order_info.validate()

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_info is not None:
            result['OrderInfo'] = self.order_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderInfo') is not None:
            temp_model = CreateInstanceResponseBodyOrderInfo()
            self.order_info = temp_model.from_map(m['OrderInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequestCreateNamespaceRequestResourceSpec(TeaModel):
    def __init__(self, cpu=None, memory_gb=None):
        self.cpu = cpu  # type: int
        self.memory_gb = memory_gb  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNamespaceRequestCreateNamespaceRequestResourceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class CreateNamespaceRequestCreateNamespaceRequest(TeaModel):
    def __init__(self, instance_id=None, namespace=None, region=None, resource_spec=None):
        self.instance_id = instance_id  # type: str
        self.namespace = namespace  # type: str
        self.region = region  # type: str
        self.resource_spec = resource_spec  # type: CreateNamespaceRequestCreateNamespaceRequestResourceSpec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super(CreateNamespaceRequestCreateNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = CreateNamespaceRequestCreateNamespaceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(self, create_namespace_request=None):
        self.create_namespace_request = create_namespace_request  # type: CreateNamespaceRequestCreateNamespaceRequest

    def validate(self):
        if self.create_namespace_request:
            self.create_namespace_request.validate()

    def to_map(self):
        _map = super(CreateNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_namespace_request is not None:
            result['CreateNamespaceRequest'] = self.create_namespace_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateNamespaceRequest') is not None:
            temp_model = CreateNamespaceRequestCreateNamespaceRequest()
            self.create_namespace_request = temp_model.from_map(m['CreateNamespaceRequest'])
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # 请求id
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNamespaceResponseBody, self).to_map()
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


class CreateNamespaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNamespaceResponse, self).to_map()
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
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequestDeleteInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, region=None):
        self.instance_id = instance_id  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceRequestDeleteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(self, delete_instance_request=None):
        self.delete_instance_request = delete_instance_request  # type: DeleteInstanceRequestDeleteInstanceRequest

    def validate(self):
        if self.delete_instance_request:
            self.delete_instance_request.validate()

    def to_map(self):
        _map = super(DeleteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_instance_request is not None:
            result['DeleteInstanceRequest'] = self.delete_instance_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteInstanceRequest') is not None:
            temp_model = DeleteInstanceRequestDeleteInstanceRequest()
            self.delete_instance_request = temp_model.from_map(m['DeleteInstanceRequest'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # 请求id
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
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


class DeleteNamespaceRequestDeleteNamespaceRequest(TeaModel):
    def __init__(self, instance_id=None, namespace=None, region=None):
        self.instance_id = instance_id  # type: str
        self.namespace = namespace  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNamespaceRequestDeleteNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(self, delete_namespace_request=None):
        self.delete_namespace_request = delete_namespace_request  # type: DeleteNamespaceRequestDeleteNamespaceRequest

    def validate(self):
        if self.delete_namespace_request:
            self.delete_namespace_request.validate()

    def to_map(self):
        _map = super(DeleteNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_namespace_request is not None:
            result['DeleteNamespaceRequest'] = self.delete_namespace_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteNamespaceRequest') is not None:
            temp_model = DeleteNamespaceRequestDeleteNamespaceRequest()
            self.delete_namespace_request = temp_model.from_map(m['DeleteNamespaceRequest'])
        return self


class DeleteNamespaceResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # 请求id
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNamespaceResponseBody, self).to_map()
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


class DeleteNamespaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNamespaceResponse, self).to_map()
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
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestDescribeInstancesRequest(TeaModel):
    def __init__(self, charge_type=None, instance_id=None, page_index=None, page_size=None, region=None):
        # 付款类型
        self.charge_type = charge_type  # type: str
        self.instance_id = instance_id  # type: str
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesRequestDescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(self, describe_instances_request=None):
        self.describe_instances_request = describe_instances_request  # type: DescribeInstancesRequestDescribeInstancesRequest

    def validate(self):
        if self.describe_instances_request:
            self.describe_instances_request.validate()

    def to_map(self):
        _map = super(DescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.describe_instances_request is not None:
            result['DescribeInstancesRequest'] = self.describe_instances_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DescribeInstancesRequest') is not None:
            temp_model = DescribeInstancesRequestDescribeInstancesRequest()
            self.describe_instances_request = temp_model.from_map(m['DescribeInstancesRequest'])
        return self


class DescribeInstancesResponseBodyInstancesResourceSpec(TeaModel):
    def __init__(self, cpu=None, memory_gb=None):
        self.cpu = cpu  # type: int
        self.memory_gb = memory_gb  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesResourceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class DescribeInstancesResponseBodyInstancesStorageOss(TeaModel):
    def __init__(self, bucket=None):
        self.bucket = bucket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesStorageOss, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class DescribeInstancesResponseBodyInstancesStorage(TeaModel):
    def __init__(self, oss=None):
        self.oss = oss  # type: DescribeInstancesResponseBodyInstancesStorageOss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstancesStorage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss is not None:
            result['Oss'] = self.oss.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Oss') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesStorageOss()
            self.oss = temp_model.from_map(m['Oss'])
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(self, charge_type=None, cluster_status=None, instance_id=None, instance_name=None,
                 order_state=None, region=None, resource_create_time=None, resource_id=None, resource_spec=None, storage=None,
                 uid=None, v_switch_ids=None, vpc_id=None, zone_id=None):
        self.charge_type = charge_type  # type: str
        self.cluster_status = cluster_status  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.order_state = order_state  # type: str
        self.region = region  # type: str
        self.resource_create_time = resource_create_time  # type: long
        self.resource_id = resource_id  # type: str
        self.resource_spec = resource_spec  # type: DescribeInstancesResponseBodyInstancesResourceSpec
        self.storage = storage  # type: DescribeInstancesResponseBodyInstancesStorage
        self.uid = uid  # type: str
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.order_state is not None:
            result['OrderState'] = self.order_state
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.storage is not None:
            result['Storage'] = self.storage.to_map()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('OrderState') is not None:
            self.order_state = m.get('OrderState')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceSpec') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('Storage') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesStorage()
            self.storage = temp_model.from_map(m['Storage'])
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, page_index=None, page_size=None, request_id=None, success=None,
                 total_count=None, total_page=None):
        self.instances = instances  # type: list[DescribeInstancesResponseBodyInstances]
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: long
        self.total_page = total_page  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
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


class DescribeNamespacesRequestDescribeNamespacesRequest(TeaModel):
    def __init__(self, instance_id=None, namespace=None, page_index=None, page_size=None, region=None):
        # 实例id
        self.instance_id = instance_id  # type: str
        # 命名空间名称
        self.namespace = namespace  # type: str
        # 当前页数
        self.page_index = page_index  # type: int
        # 每页大小
        self.page_size = page_size  # type: int
        # regionId
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespacesRequestDescribeNamespacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeNamespacesRequest(TeaModel):
    def __init__(self, describe_namespaces_request=None):
        self.describe_namespaces_request = describe_namespaces_request  # type: DescribeNamespacesRequestDescribeNamespacesRequest

    def validate(self):
        if self.describe_namespaces_request:
            self.describe_namespaces_request.validate()

    def to_map(self):
        _map = super(DescribeNamespacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.describe_namespaces_request is not None:
            result['DescribeNamespacesRequest'] = self.describe_namespaces_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DescribeNamespacesRequest') is not None:
            temp_model = DescribeNamespacesRequestDescribeNamespacesRequest()
            self.describe_namespaces_request = temp_model.from_map(m['DescribeNamespacesRequest'])
        return self


class DescribeNamespacesResponseBodyNamespacesResourceSpec(TeaModel):
    def __init__(self, cpu=None, memory_gb=None):
        self.cpu = cpu  # type: int
        self.memory_gb = memory_gb  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespacesResponseBodyNamespacesResourceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class DescribeNamespacesResponseBodyNamespacesResourceUsed(TeaModel):
    def __init__(self, cpu=None, memory_gb=None):
        self.cpu = cpu  # type: float
        self.memory_gb = memory_gb  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespacesResponseBodyNamespacesResourceUsed, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class DescribeNamespacesResponseBodyNamespaces(TeaModel):
    def __init__(self, gmt_create=None, gmt_modified=None, namespace=None, resource_spec=None, resource_used=None,
                 status=None):
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.namespace = namespace  # type: str
        self.resource_spec = resource_spec  # type: DescribeNamespacesResponseBodyNamespacesResourceSpec
        self.resource_used = resource_used  # type: DescribeNamespacesResponseBodyNamespacesResourceUsed
        self.status = status  # type: str

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()
        if self.resource_used:
            self.resource_used.validate()

    def to_map(self):
        _map = super(DescribeNamespacesResponseBodyNamespaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.resource_used is not None:
            result['ResourceUsed'] = self.resource_used.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ResourceSpec') is not None:
            temp_model = DescribeNamespacesResponseBodyNamespacesResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('ResourceUsed') is not None:
            temp_model = DescribeNamespacesResponseBodyNamespacesResourceUsed()
            self.resource_used = temp_model.from_map(m['ResourceUsed'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeNamespacesResponseBody(TeaModel):
    def __init__(self, namespaces=None, page_index=None, page_size=None, request_id=None, success=None,
                 total_count=None, total_page=None):
        self.namespaces = namespaces  # type: list[DescribeNamespacesResponseBodyNamespaces]
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        # 请求id
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool
        self.total_count = total_count  # type: long
        self.total_page = total_page  # type: int

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNamespacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = DescribeNamespacesResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribeNamespacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeNamespacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNamespacesResponse, self).to_map()
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
            temp_model = DescribeNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequestResourceSpec(TeaModel):
    def __init__(self, cpu=None, memory_gb=None):
        self.cpu = cpu  # type: int
        self.memory_gb = memory_gb  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequestResourceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequest(TeaModel):
    def __init__(self, instance_id=None, region=None, resource_spec=None):
        self.instance_id = instance_id  # type: str
        self.region = region  # type: str
        self.resource_spec = resource_spec  # type: ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequestResourceSpec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super(ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ModifyPrepayInstanceSpecRequest(TeaModel):
    def __init__(self, modify_prepay_instance_spec_request=None):
        self.modify_prepay_instance_spec_request = modify_prepay_instance_spec_request  # type: ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequest

    def validate(self):
        if self.modify_prepay_instance_spec_request:
            self.modify_prepay_instance_spec_request.validate()

    def to_map(self):
        _map = super(ModifyPrepayInstanceSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_prepay_instance_spec_request is not None:
            result['ModifyPrepayInstanceSpecRequest'] = self.modify_prepay_instance_spec_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModifyPrepayInstanceSpecRequest') is not None:
            temp_model = ModifyPrepayInstanceSpecRequestModifyPrepayInstanceSpecRequest()
            self.modify_prepay_instance_spec_request = temp_model.from_map(m['ModifyPrepayInstanceSpecRequest'])
        return self


class ModifyPrepayInstanceSpecResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None, success=None):
        # 订单id
        self.order_id = order_id  # type: long
        # 请求id
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPrepayInstanceSpecResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyPrepayInstanceSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyPrepayInstanceSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPrepayInstanceSpecResponse, self).to_map()
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
            temp_model = ModifyPrepayInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequestResourceSpec(TeaModel):
    def __init__(self, cpu=None, memory_gb=None):
        self.cpu = cpu  # type: int
        self.memory_gb = memory_gb  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequestResourceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequest(TeaModel):
    def __init__(self, instance_id=None, namespace=None, region=None, resource_spec=None):
        self.instance_id = instance_id  # type: str
        self.namespace = namespace  # type: str
        self.region = region  # type: str
        self.resource_spec = resource_spec  # type: ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequestResourceSpec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super(ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceSpec') is not None:
            temp_model = ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class ModifyPrepayNamespaceSpecRequest(TeaModel):
    def __init__(self, modify_prepay_namespace_spec_request=None):
        self.modify_prepay_namespace_spec_request = modify_prepay_namespace_spec_request  # type: ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequest

    def validate(self):
        if self.modify_prepay_namespace_spec_request:
            self.modify_prepay_namespace_spec_request.validate()

    def to_map(self):
        _map = super(ModifyPrepayNamespaceSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_prepay_namespace_spec_request is not None:
            result['ModifyPrepayNamespaceSpecRequest'] = self.modify_prepay_namespace_spec_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModifyPrepayNamespaceSpecRequest') is not None:
            temp_model = ModifyPrepayNamespaceSpecRequestModifyPrepayNamespaceSpecRequest()
            self.modify_prepay_namespace_spec_request = temp_model.from_map(m['ModifyPrepayNamespaceSpecRequest'])
        return self


class ModifyPrepayNamespaceSpecResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # 请求id
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPrepayNamespaceSpecResponseBody, self).to_map()
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


class ModifyPrepayNamespaceSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyPrepayNamespaceSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPrepayNamespaceSpecResponse, self).to_map()
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
            temp_model = ModifyPrepayNamespaceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec(TeaModel):
    def __init__(self, cpu=None, memory_gb=None):
        # cpu数量。
        self.cpu = cpu  # type: int
        # 内存大小。
        self.memory_gb = memory_gb  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')
        return self


class QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs(TeaModel):
    def __init__(self, namespace=None, resource_spec=None):
        # namespace名称，
        self.namespace = namespace  # type: str
        # 资源规格。
        self.resource_spec = resource_spec  # type: QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super(QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ResourceSpec') is not None:
            temp_model = QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecsResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        return self


class QueryConvertInstancePriceRequestConvertPostpayInstanceRequest(TeaModel):
    def __init__(self, duration=None, instance_id=None, is_auto_renew=None, namespace_resource_specs=None,
                 pricing_cycle=None, region=None):
        # 订购周期数量
        self.duration = duration  # type: int
        self.instance_id = instance_id  # type: str
        # 是否自动续费
        self.is_auto_renew = is_auto_renew  # type: bool
        # 项目空间资源规格。
        self.namespace_resource_specs = namespace_resource_specs  # type: list[QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs]
        # 订购周期
        self.pricing_cycle = pricing_cycle  # type: str
        self.region = region  # type: str

    def validate(self):
        if self.namespace_resource_specs:
            for k in self.namespace_resource_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryConvertInstancePriceRequestConvertPostpayInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_auto_renew is not None:
            result['IsAutoRenew'] = self.is_auto_renew
        result['NamespaceResourceSpecs'] = []
        if self.namespace_resource_specs is not None:
            for k in self.namespace_resource_specs:
                result['NamespaceResourceSpecs'].append(k.to_map() if k else None)
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsAutoRenew') is not None:
            self.is_auto_renew = m.get('IsAutoRenew')
        self.namespace_resource_specs = []
        if m.get('NamespaceResourceSpecs') is not None:
            for k in m.get('NamespaceResourceSpecs'):
                temp_model = QueryConvertInstancePriceRequestConvertPostpayInstanceRequestNamespaceResourceSpecs()
                self.namespace_resource_specs.append(temp_model.from_map(k))
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class QueryConvertInstancePriceRequest(TeaModel):
    def __init__(self, convert_postpay_instance_request=None):
        self.convert_postpay_instance_request = convert_postpay_instance_request  # type: QueryConvertInstancePriceRequestConvertPostpayInstanceRequest

    def validate(self):
        if self.convert_postpay_instance_request:
            self.convert_postpay_instance_request.validate()

    def to_map(self):
        _map = super(QueryConvertInstancePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convert_postpay_instance_request is not None:
            result['ConvertPostpayInstanceRequest'] = self.convert_postpay_instance_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConvertPostpayInstanceRequest') is not None:
            temp_model = QueryConvertInstancePriceRequestConvertPostpayInstanceRequest()
            self.convert_postpay_instance_request = temp_model.from_map(m['ConvertPostpayInstanceRequest'])
        return self


class QueryConvertInstancePriceResponseBodyPriceInfoOptionalPromotions(TeaModel):
    def __init__(self, promotion_desc=None, promotion_name=None, promotion_option_no=None, selected=None):
        # 优惠券描述
        self.promotion_desc = promotion_desc  # type: str
        # 优惠券名称
        self.promotion_name = promotion_name  # type: str
        # 优惠券编号
        self.promotion_option_no = promotion_option_no  # type: str
        self.selected = selected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryConvertInstancePriceResponseBodyPriceInfoOptionalPromotions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class QueryConvertInstancePriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(self, description=None, rule_id=None):
        # 活动规则描述。
        self.description = description  # type: str
        # 活动ID。
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryConvertInstancePriceResponseBodyPriceInfoRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class QueryConvertInstancePriceResponseBodyPriceInfo(TeaModel):
    def __init__(self, code=None, currency=None, discount_amount=None, message=None, optional_promotions=None,
                 original_amount=None, rules=None, trade_amount=None):
        # 错误码
        self.code = code  # type: str
        # 货币单位。
        self.currency = currency  # type: str
        # 折扣
        self.discount_amount = discount_amount  # type: float
        # 错误信息
        self.message = message  # type: str
        # 可选择的优惠券
        self.optional_promotions = optional_promotions  # type: QueryConvertInstancePriceResponseBodyPriceInfoOptionalPromotions
        # 原价
        self.original_amount = original_amount  # type: float
        # 活动规则。
        self.rules = rules  # type: list[QueryConvertInstancePriceResponseBodyPriceInfoRules]
        # 最终价，为原价减去折扣。
        self.trade_amount = trade_amount  # type: float

    def validate(self):
        if self.optional_promotions:
            self.optional_promotions.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryConvertInstancePriceResponseBodyPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.message is not None:
            result['Message'] = self.message
        if self.optional_promotions is not None:
            result['OptionalPromotions'] = self.optional_promotions.to_map()
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OptionalPromotions') is not None:
            temp_model = QueryConvertInstancePriceResponseBodyPriceInfoOptionalPromotions()
            self.optional_promotions = temp_model.from_map(m['OptionalPromotions'])
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = QueryConvertInstancePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class QueryConvertInstancePriceResponseBody(TeaModel):
    def __init__(self, price_info=None, request_id=None, success=None):
        # 价格信息，包括价格和优惠规则。
        self.price_info = price_info  # type: QueryConvertInstancePriceResponseBodyPriceInfo
        # 请求id
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super(QueryConvertInstancePriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = QueryConvertInstancePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryConvertInstancePriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryConvertInstancePriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryConvertInstancePriceResponse, self).to_map()
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
            temp_model = QueryConvertInstancePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequestRenewInstanceRequest(TeaModel):
    def __init__(self, duration=None, instance_id=None, pricing_cycle=None, region=None):
        # 订购周期数量
        self.duration = duration  # type: int
        # 实例id
        self.instance_id = instance_id  # type: str
        # 订购周期
        self.pricing_cycle = pricing_cycle  # type: str
        # 地域id
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceRequestRenewInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, renew_instance_request=None):
        self.renew_instance_request = renew_instance_request  # type: RenewInstanceRequestRenewInstanceRequest

    def validate(self):
        if self.renew_instance_request:
            self.renew_instance_request.validate()

    def to_map(self):
        _map = super(RenewInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.renew_instance_request is not None:
            result['RenewInstanceRequest'] = self.renew_instance_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RenewInstanceRequest') is not None:
            temp_model = RenewInstanceRequestRenewInstanceRequest()
            self.renew_instance_request = temp_model.from_map(m['RenewInstanceRequest'])
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None, success=None):
        # orderId
        self.order_id = order_id  # type: long
        # 请求id
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


