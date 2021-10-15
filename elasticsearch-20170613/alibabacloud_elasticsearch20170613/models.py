# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ActivateZonesRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActivateZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ActivateZonesResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActivateZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ActivateZonesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ActivateZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ActivateZonesResponse, self).to_map()
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
            temp_model = ActivateZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddConnectableClusterRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddConnectableClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class AddConnectableClusterResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddConnectableClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddConnectableClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddConnectableClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddConnectableClusterResponse, self).to_map()
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
            temp_model = AddConnectableClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSnapshotRepoResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSnapshotRepoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddSnapshotRepoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddSnapshotRepoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSnapshotRepoResponse, self).to_map()
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
            temp_model = AddSnapshotRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDeletionRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDeletionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CancelDeletionResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDeletionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelDeletionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelDeletionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelDeletionResponse, self).to_map()
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
            temp_model = CancelDeletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelLogstashDeletionRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelLogstashDeletionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CancelLogstashDeletionResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelLogstashDeletionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelLogstashDeletionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelLogstashDeletionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelLogstashDeletionResponse, self).to_map()
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
            temp_model = CancelLogstashDeletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTaskRequest(TeaModel):
    def __init__(self, task_type=None, client_token=None):
        self.task_type = task_type  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CancelTaskResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelTaskResponse, self).to_map()
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
            temp_model = CancelTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CapacityPlanRequestDataInfo(TeaModel):
    def __init__(self, code=None, size=None, type=None, unit=None, total_count=None):
        self.code = code  # type: str
        self.size = size  # type: long
        self.type = type  # type: str
        self.unit = unit  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CapacityPlanRequestDataInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        if self.unit is not None:
            result['unit'] = self.unit
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class CapacityPlanRequestMetric(TeaModel):
    def __init__(self, code=None, concurrent=None, throughput=None, type=None, peak_qps=None, average_qps=None,
                 response_time=None):
        self.code = code  # type: str
        self.concurrent = concurrent  # type: long
        self.throughput = throughput  # type: long
        self.type = type  # type: str
        self.peak_qps = peak_qps  # type: int
        self.average_qps = average_qps  # type: int
        self.response_time = response_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CapacityPlanRequestMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.concurrent is not None:
            result['concurrent'] = self.concurrent
        if self.throughput is not None:
            result['throughput'] = self.throughput
        if self.type is not None:
            result['type'] = self.type
        if self.peak_qps is not None:
            result['peakQps'] = self.peak_qps
        if self.average_qps is not None:
            result['averageQps'] = self.average_qps
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('concurrent') is not None:
            self.concurrent = m.get('concurrent')
        if m.get('throughput') is not None:
            self.throughput = m.get('throughput')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('peakQps') is not None:
            self.peak_qps = m.get('peakQps')
        if m.get('averageQps') is not None:
            self.average_qps = m.get('averageQps')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        return self


class CapacityPlanRequest(TeaModel):
    def __init__(self, complex_query_available=None, data_info=None, metric=None, usage_scenario=None):
        self.complex_query_available = complex_query_available  # type: bool
        self.data_info = data_info  # type: list[CapacityPlanRequestDataInfo]
        self.metric = metric  # type: list[CapacityPlanRequestMetric]
        self.usage_scenario = usage_scenario  # type: str

    def validate(self):
        if self.data_info:
            for k in self.data_info:
                if k:
                    k.validate()
        if self.metric:
            for k in self.metric:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CapacityPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complex_query_available is not None:
            result['complexQueryAvailable'] = self.complex_query_available
        result['dataInfo'] = []
        if self.data_info is not None:
            for k in self.data_info:
                result['dataInfo'].append(k.to_map() if k else None)
        result['metric'] = []
        if self.metric is not None:
            for k in self.metric:
                result['metric'].append(k.to_map() if k else None)
        if self.usage_scenario is not None:
            result['usageScenario'] = self.usage_scenario
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('complexQueryAvailable') is not None:
            self.complex_query_available = m.get('complexQueryAvailable')
        self.data_info = []
        if m.get('dataInfo') is not None:
            for k in m.get('dataInfo'):
                temp_model = CapacityPlanRequestDataInfo()
                self.data_info.append(temp_model.from_map(k))
        self.metric = []
        if m.get('metric') is not None:
            for k in m.get('metric'):
                temp_model = CapacityPlanRequestMetric()
                self.metric.append(temp_model.from_map(k))
        if m.get('usageScenario') is not None:
            self.usage_scenario = m.get('usageScenario')
        return self


class CapacityPlanResponseBodyResultExtendConfigs(TeaModel):
    def __init__(self, config_type=None, disk=None, disk_type=None):
        self.config_type = config_type  # type: str
        self.disk = disk  # type: long
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CapacityPlanResponseBodyResultExtendConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class CapacityPlanResponseBodyResultNodeConfigurations(TeaModel):
    def __init__(self, amount=None, cpu=None, disk=None, disk_type=None, memory=None, node_type=None):
        self.amount = amount  # type: long
        self.cpu = cpu  # type: long
        self.disk = disk  # type: long
        self.disk_type = disk_type  # type: str
        self.memory = memory  # type: long
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CapacityPlanResponseBodyResultNodeConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.disk is not None:
            result['Disk'] = self.disk
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Disk') is not None:
            self.disk = m.get('Disk')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class CapacityPlanResponseBodyResult(TeaModel):
    def __init__(self, extend_configs=None, instance_category=None, node_configurations=None,
                 oversized_cluster=None):
        self.extend_configs = extend_configs  # type: list[CapacityPlanResponseBodyResultExtendConfigs]
        self.instance_category = instance_category  # type: str
        self.node_configurations = node_configurations  # type: list[CapacityPlanResponseBodyResultNodeConfigurations]
        self.oversized_cluster = oversized_cluster  # type: bool

    def validate(self):
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()
        if self.node_configurations:
            for k in self.node_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CapacityPlanResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExtendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['ExtendConfigs'].append(k.to_map() if k else None)
        if self.instance_category is not None:
            result['InstanceCategory'] = self.instance_category
        result['NodeConfigurations'] = []
        if self.node_configurations is not None:
            for k in self.node_configurations:
                result['NodeConfigurations'].append(k.to_map() if k else None)
        if self.oversized_cluster is not None:
            result['OversizedCluster'] = self.oversized_cluster
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.extend_configs = []
        if m.get('ExtendConfigs') is not None:
            for k in m.get('ExtendConfigs'):
                temp_model = CapacityPlanResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
        if m.get('InstanceCategory') is not None:
            self.instance_category = m.get('InstanceCategory')
        self.node_configurations = []
        if m.get('NodeConfigurations') is not None:
            for k in m.get('NodeConfigurations'):
                temp_model = CapacityPlanResponseBodyResultNodeConfigurations()
                self.node_configurations.append(temp_model.from_map(k))
        if m.get('OversizedCluster') is not None:
            self.oversized_cluster = m.get('OversizedCluster')
        return self


class CapacityPlanResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CapacityPlanResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CapacityPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CapacityPlanResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CapacityPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CapacityPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CapacityPlanResponse, self).to_map()
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
            temp_model = CapacityPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseDiagnosisRequest(TeaModel):
    def __init__(self, client_token=None, lang=None):
        self.client_token = client_token  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseDiagnosisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class CloseDiagnosisResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseDiagnosisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloseDiagnosisResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloseDiagnosisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseDiagnosisResponse, self).to_map()
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
            temp_model = CloseDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseHttpsRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseHttpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CloseHttpsResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseHttpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloseHttpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloseHttpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseHttpsResponse, self).to_map()
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
            temp_model = CloseHttpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseManagedIndexRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseManagedIndexRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CloseManagedIndexResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseManagedIndexResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloseManagedIndexResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloseManagedIndexResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseManagedIndexResponse, self).to_map()
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
            temp_model = CloseManagedIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCollectorRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCollectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CreateCollectorResponseBodyResult(TeaModel):
    def __init__(self, res_id=None):
        self.res_id = res_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCollectorResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_id is not None:
            result['resId'] = self.res_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resId') is not None:
            self.res_id = m.get('resId')
        return self


class CreateCollectorResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateCollectorResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateCollectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateCollectorResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateCollectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCollectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCollectorResponse, self).to_map()
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
            temp_model = CreateCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataStreamRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDataStreamResponseBodyResult(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataStreamResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateDataStreamResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateDataStreamResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateDataStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateDataStreamResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateDataStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDataStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataStreamResponse, self).to_map()
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
            temp_model = CreateDataStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataTasksRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDataTasksResponseBodyResultSourceCluster(TeaModel):
    def __init__(self, password=None, index=None, type=None, endpoint=None, username=None, vpc_id=None,
                 vpc_instance_id=None, vpc_instance_port=None, data_source_type=None):
        self.password = password  # type: str
        self.index = index  # type: str
        self.type = type  # type: str
        self.endpoint = endpoint  # type: str
        self.username = username  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_instance_id = vpc_instance_id  # type: str
        self.vpc_instance_port = vpc_instance_port  # type: int
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataTasksResponseBodyResultSourceCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.index is not None:
            result['index'] = self.index
        if self.type is not None:
            result['type'] = self.type
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id
        if self.vpc_instance_port is not None:
            result['vpcInstancePort'] = self.vpc_instance_port
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')
        if m.get('vpcInstancePort') is not None:
            self.vpc_instance_port = m.get('vpcInstancePort')
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')
        return self


class CreateDataTasksResponseBodyResultSinkCluster(TeaModel):
    def __init__(self, password=None, index=None, settings=None, mapping=None, type=None, routing=None, username=None,
                 vpc_id=None, vpc_instance_port=None, vpc_instance_id=None, data_source_type=None):
        self.password = password  # type: str
        self.index = index  # type: str
        self.settings = settings  # type: str
        self.mapping = mapping  # type: str
        self.type = type  # type: str
        self.routing = routing  # type: str
        self.username = username  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_instance_port = vpc_instance_port  # type: str
        self.vpc_instance_id = vpc_instance_id  # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataTasksResponseBodyResultSinkCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.index is not None:
            result['index'] = self.index
        if self.settings is not None:
            result['settings'] = self.settings
        if self.mapping is not None:
            result['mapping'] = self.mapping
        if self.type is not None:
            result['type'] = self.type
        if self.routing is not None:
            result['routing'] = self.routing
        if self.username is not None:
            result['username'] = self.username
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_instance_port is not None:
            result['vpcInstancePort'] = self.vpc_instance_port
        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        if m.get('mapping') is not None:
            self.mapping = m.get('mapping')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('routing') is not None:
            self.routing = m.get('routing')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcInstancePort') is not None:
            self.vpc_instance_port = m.get('vpcInstancePort')
        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')
        return self


class CreateDataTasksResponseBodyResult(TeaModel):
    def __init__(self, source_cluster=None, sink_cluster=None):
        self.source_cluster = source_cluster  # type: CreateDataTasksResponseBodyResultSourceCluster
        self.sink_cluster = sink_cluster  # type: CreateDataTasksResponseBodyResultSinkCluster

    def validate(self):
        if self.source_cluster:
            self.source_cluster.validate()
        if self.sink_cluster:
            self.sink_cluster.validate()

    def to_map(self):
        _map = super(CreateDataTasksResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_cluster is not None:
            result['sourceCluster'] = self.source_cluster.to_map()
        if self.sink_cluster is not None:
            result['sinkCluster'] = self.sink_cluster.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sourceCluster') is not None:
            temp_model = CreateDataTasksResponseBodyResultSourceCluster()
            self.source_cluster = temp_model.from_map(m['sourceCluster'])
        if m.get('sinkCluster') is not None:
            temp_model = CreateDataTasksResponseBodyResultSinkCluster()
            self.sink_cluster = temp_model.from_map(m['sinkCluster'])
        return self


class CreateDataTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[CreateDataTasksResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDataTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = CreateDataTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class CreateDataTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDataTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataTasksResponse, self).to_map()
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
            temp_model = CreateDataTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateILMPolicyRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateILMPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateILMPolicyResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateILMPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateILMPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateILMPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateILMPolicyResponse, self).to_map()
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
            temp_model = CreateILMPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIndexTemplateRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIndexTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateIndexTemplateResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIndexTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIndexTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIndexTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIndexTemplateResponse, self).to_map()
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
            temp_model = CreateIndexTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CreateInstanceResponseBodyResult(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateInstanceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
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


class CreateLogstashRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogstashRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CreateLogstashResponseBodyResult(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogstashResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class CreateLogstashResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateLogstashResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateLogstashResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateLogstashResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateLogstashResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateLogstashResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLogstashResponse, self).to_map()
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
            temp_model = CreateLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePipelinesRequest(TeaModel):
    def __init__(self, trigger=None, client_token=None):
        self.trigger = trigger  # type: bool
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePipelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger is not None:
            result['trigger'] = self.trigger
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreatePipelinesResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePipelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePipelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreatePipelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePipelinesResponse, self).to_map()
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
            temp_model = CreatePipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSnapshotResponse, self).to_map()
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
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcEndpointRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateVpcEndpointResponseBodyResult(TeaModel):
    def __init__(self, service_id=None, endpoint_domain=None, endpoint_id=None, endpoint_name=None):
        self.service_id = service_id  # type: str
        self.endpoint_domain = endpoint_domain  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.endpoint_name = endpoint_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcEndpointResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.endpoint_domain is not None:
            result['endpointDomain'] = self.endpoint_domain
        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('endpointDomain') is not None:
            self.endpoint_domain = m.get('endpointDomain')
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')
        return self


class CreateVpcEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateVpcEndpointResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateVpcEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateVpcEndpointResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateVpcEndpointResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateVpcEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpcEndpointResponse, self).to_map()
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
            temp_model = CreateVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactivateZonesRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeactivateZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class DeactivateZonesResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeactivateZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeactivateZonesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeactivateZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeactivateZonesResponse, self).to_map()
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
            temp_model = DeactivateZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCollectorRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCollectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteCollectorResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCollectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCollectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCollectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCollectorResponse, self).to_map()
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
            temp_model = DeleteCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnectedClusterRequest(TeaModel):
    def __init__(self, client_token=None, connected_instance_id=None):
        self.client_token = client_token  # type: str
        self.connected_instance_id = connected_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConnectedClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.connected_instance_id is not None:
            result['connectedInstanceId'] = self.connected_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('connectedInstanceId') is not None:
            self.connected_instance_id = m.get('connectedInstanceId')
        return self


class DeleteConnectedClusterResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConnectedClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConnectedClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteConnectedClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteConnectedClusterResponse, self).to_map()
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
            temp_model = DeleteConnectedClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataStreamRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteDataStreamResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDataStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDataStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataStreamResponse, self).to_map()
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
            temp_model = DeleteDataStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataTaskRequest(TeaModel):
    def __init__(self, client_token=None, task_id=None):
        self.client_token = client_token  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DeleteDataTaskResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDataTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDataTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataTaskResponse, self).to_map()
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
            temp_model = DeleteDataTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteILMPolicyResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteILMPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteILMPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteILMPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteILMPolicyResponse, self).to_map()
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
            temp_model = DeleteILMPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIndexTemplateResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIndexTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIndexTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteIndexTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIndexTemplateResponse, self).to_map()
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
            temp_model = DeleteIndexTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(self, client_token=None, delete_type=None):
        self.client_token = client_token  # type: str
        self.delete_type = delete_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.delete_type is not None:
            result['deleteType'] = self.delete_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('deleteType') is not None:
            self.delete_type = m.get('deleteType')
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


class DeleteLogstashRequest(TeaModel):
    def __init__(self, client_token=None, delete_type=None):
        self.client_token = client_token  # type: str
        self.delete_type = delete_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLogstashRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.delete_type is not None:
            result['deleteType'] = self.delete_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('deleteType') is not None:
            self.delete_type = m.get('deleteType')
        return self


class DeleteLogstashResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLogstashResponseBody, self).to_map()
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


class DeleteLogstashResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteLogstashResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLogstashResponse, self).to_map()
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
            temp_model = DeleteLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePipelinesRequest(TeaModel):
    def __init__(self, client_token=None, pipeline_ids=None):
        self.client_token = client_token  # type: str
        self.pipeline_ids = pipeline_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePipelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.pipeline_ids is not None:
            result['pipelineIds'] = self.pipeline_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('pipelineIds') is not None:
            self.pipeline_ids = m.get('pipelineIds')
        return self


class DeletePipelinesResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePipelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePipelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeletePipelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePipelinesResponse, self).to_map()
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
            temp_model = DeletePipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRepoRequest(TeaModel):
    def __init__(self, repo_path=None, client_token=None):
        self.repo_path = repo_path  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotRepoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_path is not None:
            result['repoPath'] = self.repo_path
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('repoPath') is not None:
            self.repo_path = m.get('repoPath')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class DeleteSnapshotRepoResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotRepoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSnapshotRepoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSnapshotRepoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSnapshotRepoResponse, self).to_map()
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
            temp_model = DeleteSnapshotRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcEndpointRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteVpcEndpointResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVpcEndpointResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteVpcEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVpcEndpointResponse, self).to_map()
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
            temp_model = DeleteVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAckOperatorResponseBodyResult(TeaModel):
    def __init__(self, version=None, status=None):
        self.version = version  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAckOperatorResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeAckOperatorResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeAckOperatorResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAckOperatorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAckOperatorResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAckOperatorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAckOperatorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAckOperatorResponse, self).to_map()
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
            temp_model = DescribeAckOperatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCollectorResponseBodyResultConfigs(TeaModel):
    def __init__(self, content=None, file_name=None):
        self.content = content  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCollectorResponseBodyResultConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class DescribeCollectorResponseBodyResultExtendConfigsMachines(TeaModel):
    def __init__(self, agent_status=None, instance_id=None):
        self.agent_status = agent_status  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCollectorResponseBodyResultExtendConfigsMachines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['agentStatus'] = self.agent_status
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('agentStatus') is not None:
            self.agent_status = m.get('agentStatus')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class DescribeCollectorResponseBodyResultExtendConfigs(TeaModel):
    def __init__(self, success_pods_count=None, protocol=None, user_name=None, total_pods_count=None, type=None,
                 kibana_host=None, enable_monitoring=None, config_type=None, instance_type=None, group_id=None, host=None,
                 instance_id=None, machines=None, hosts=None):
        self.success_pods_count = success_pods_count  # type: str
        self.protocol = protocol  # type: str
        self.user_name = user_name  # type: str
        self.total_pods_count = total_pods_count  # type: str
        self.type = type  # type: str
        self.kibana_host = kibana_host  # type: str
        self.enable_monitoring = enable_monitoring  # type: bool
        self.config_type = config_type  # type: str
        self.instance_type = instance_type  # type: str
        self.group_id = group_id  # type: str
        self.host = host  # type: str
        self.instance_id = instance_id  # type: str
        self.machines = machines  # type: list[DescribeCollectorResponseBodyResultExtendConfigsMachines]
        self.hosts = hosts  # type: list[str]

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCollectorResponseBodyResultExtendConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_pods_count is not None:
            result['successPodsCount'] = self.success_pods_count
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.total_pods_count is not None:
            result['totalPodsCount'] = self.total_pods_count
        if self.type is not None:
            result['type'] = self.type
        if self.kibana_host is not None:
            result['kibanaHost'] = self.kibana_host
        if self.enable_monitoring is not None:
            result['enableMonitoring'] = self.enable_monitoring
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.host is not None:
            result['host'] = self.host
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['machines'] = []
        if self.machines is not None:
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
        if self.hosts is not None:
            result['hosts'] = self.hosts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('successPodsCount') is not None:
            self.success_pods_count = m.get('successPodsCount')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('totalPodsCount') is not None:
            self.total_pods_count = m.get('totalPodsCount')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('kibanaHost') is not None:
            self.kibana_host = m.get('kibanaHost')
        if m.get('enableMonitoring') is not None:
            self.enable_monitoring = m.get('enableMonitoring')
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.machines = []
        if m.get('machines') is not None:
            for k in m.get('machines'):
                temp_model = DescribeCollectorResponseBodyResultExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k))
        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')
        return self


class DescribeCollectorResponseBodyResult(TeaModel):
    def __init__(self, res_id=None, gmt_update_time=None, dry_run=None, owner_id=None, vpc_id=None, res_type=None,
                 res_version=None, gmt_created_time=None, status=None, name=None, configs=None, extend_configs=None,
                 collector_paths=None):
        self.res_id = res_id  # type: str
        self.gmt_update_time = gmt_update_time  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_id = owner_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.res_type = res_type  # type: str
        self.res_version = res_version  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.status = status  # type: str
        self.name = name  # type: str
        self.configs = configs  # type: list[DescribeCollectorResponseBodyResultConfigs]
        self.extend_configs = extend_configs  # type: list[DescribeCollectorResponseBodyResultExtendConfigs]
        self.collector_paths = collector_paths  # type: list[str]

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCollectorResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_id is not None:
            result['resId'] = self.res_id
        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.res_type is not None:
            result['resType'] = self.res_type
        if self.res_version is not None:
            result['resVersion'] = self.res_version
        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['extendConfigs'].append(k.to_map() if k else None)
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resId') is not None:
            self.res_id = m.get('resId')
        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('resType') is not None:
            self.res_type = m.get('resType')
        if m.get('resVersion') is not None:
            self.res_version = m.get('resVersion')
        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = DescribeCollectorResponseBodyResultConfigs()
                self.configs.append(temp_model.from_map(k))
        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k in m.get('extendConfigs'):
                temp_model = DescribeCollectorResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
        if m.get('collectorPaths') is not None:
            self.collector_paths = m.get('collectorPaths')
        return self


class DescribeCollectorResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeCollectorResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeCollectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeCollectorResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeCollectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCollectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCollectorResponse, self).to_map()
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
            temp_model = DescribeCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConnectableClustersRequest(TeaModel):
    def __init__(self, already_set_items=None):
        self.already_set_items = already_set_items  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConnectableClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_set_items is not None:
            result['alreadySetItems'] = self.already_set_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alreadySetItems') is not None:
            self.already_set_items = m.get('alreadySetItems')
        return self


class DescribeConnectableClustersResponseBodyResult(TeaModel):
    def __init__(self, network_type=None, instances=None):
        self.network_type = network_type  # type: str
        self.instances = instances  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConnectableClustersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.instances is not None:
            result['instances'] = self.instances
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        return self


class DescribeConnectableClustersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeConnectableClustersResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeConnectableClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeConnectableClustersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeConnectableClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeConnectableClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeConnectableClustersResponse, self).to_map()
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
            temp_model = DescribeConnectableClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnoseReportRequest(TeaModel):
    def __init__(self, lang=None):
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnoseReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class DescribeDiagnoseReportResponseBodyResultDiagnoseItemsDetail(TeaModel):
    def __init__(self, type=None, name=None, desc=None, result=None, suggest=None):
        self.type = type  # type: str
        self.name = name  # type: str
        self.desc = desc  # type: str
        self.result = result  # type: str
        self.suggest = suggest  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnoseReportResponseBodyResultDiagnoseItemsDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.result is not None:
            result['result'] = self.result
        if self.suggest is not None:
            result['suggest'] = self.suggest
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('suggest') is not None:
            self.suggest = m.get('suggest')
        return self


class DescribeDiagnoseReportResponseBodyResultDiagnoseItems(TeaModel):
    def __init__(self, item=None, health=None, detail=None):
        self.item = item  # type: str
        self.health = health  # type: str
        self.detail = detail  # type: DescribeDiagnoseReportResponseBodyResultDiagnoseItemsDetail

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super(DescribeDiagnoseReportResponseBodyResultDiagnoseItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item is not None:
            result['item'] = self.item
        if self.health is not None:
            result['health'] = self.health
        if self.detail is not None:
            result['detail'] = self.detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('item') is not None:
            self.item = m.get('item')
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('detail') is not None:
            temp_model = DescribeDiagnoseReportResponseBodyResultDiagnoseItemsDetail()
            self.detail = temp_model.from_map(m['detail'])
        return self


class DescribeDiagnoseReportResponseBodyResult(TeaModel):
    def __init__(self, trigger=None, create_time=None, report_id=None, state=None, instance_id=None, health=None,
                 diagnose_items=None):
        self.trigger = trigger  # type: str
        self.create_time = create_time  # type: long
        self.report_id = report_id  # type: str
        self.state = state  # type: str
        self.instance_id = instance_id  # type: str
        self.health = health  # type: str
        self.diagnose_items = diagnose_items  # type: list[DescribeDiagnoseReportResponseBodyResultDiagnoseItems]

    def validate(self):
        if self.diagnose_items:
            for k in self.diagnose_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiagnoseReportResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger is not None:
            result['trigger'] = self.trigger
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.report_id is not None:
            result['reportId'] = self.report_id
        if self.state is not None:
            result['state'] = self.state
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.health is not None:
            result['health'] = self.health
        result['diagnoseItems'] = []
        if self.diagnose_items is not None:
            for k in self.diagnose_items:
                result['diagnoseItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('health') is not None:
            self.health = m.get('health')
        self.diagnose_items = []
        if m.get('diagnoseItems') is not None:
            for k in m.get('diagnoseItems'):
                temp_model = DescribeDiagnoseReportResponseBodyResultDiagnoseItems()
                self.diagnose_items.append(temp_model.from_map(k))
        return self


class DescribeDiagnoseReportResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeDiagnoseReportResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeDiagnoseReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeDiagnoseReportResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeDiagnoseReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDiagnoseReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiagnoseReportResponse, self).to_map()
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
            temp_model = DescribeDiagnoseReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosisSettingsRequest(TeaModel):
    def __init__(self, lang=None):
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosisSettingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class DescribeDiagnosisSettingsResponseBodyResult(TeaModel):
    def __init__(self, update_time=None, scene=None):
        self.update_time = update_time  # type: long
        self.scene = scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosisSettingsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class DescribeDiagnosisSettingsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeDiagnosisSettingsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeDiagnosisSettingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeDiagnosisSettingsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeDiagnosisSettingsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDiagnosisSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiagnosisSettingsResponse, self).to_map()
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
            temp_model = DescribeDiagnosisSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElasticsearchHealthResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeElasticsearchHealthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeElasticsearchHealthResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeElasticsearchHealthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeElasticsearchHealthResponse, self).to_map()
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
            temp_model = DescribeElasticsearchHealthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeILMPolicyResponseBodyResult(TeaModel):
    def __init__(self, name=None, phases=None):
        self.name = name  # type: str
        self.phases = phases  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeILMPolicyResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.phases is not None:
            result['phases'] = self.phases
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phases') is not None:
            self.phases = m.get('phases')
        return self


class DescribeILMPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeILMPolicyResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeILMPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeILMPolicyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeILMPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeILMPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeILMPolicyResponse, self).to_map()
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
            temp_model = DescribeILMPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIndexTemplateResponseBodyResultTemplate(TeaModel):
    def __init__(self, settings=None, mappings=None, aliases=None):
        self.settings = settings  # type: str
        self.mappings = mappings  # type: str
        self.aliases = aliases  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIndexTemplateResponseBodyResultTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.settings is not None:
            result['settings'] = self.settings
        if self.mappings is not None:
            result['mappings'] = self.mappings
        if self.aliases is not None:
            result['aliases'] = self.aliases
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        if m.get('mappings') is not None:
            self.mappings = m.get('mappings')
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')
        return self


class DescribeIndexTemplateResponseBodyResult(TeaModel):
    def __init__(self, data_stream=None, index_template=None, ilm_policy=None, priority=None, index_patterns=None,
                 template=None):
        self.data_stream = data_stream  # type: bool
        self.index_template = index_template  # type: str
        self.ilm_policy = ilm_policy  # type: str
        self.priority = priority  # type: int
        self.index_patterns = index_patterns  # type: list[str]
        self.template = template  # type: DescribeIndexTemplateResponseBodyResultTemplate

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(DescribeIndexTemplateResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_stream is not None:
            result['dataStream'] = self.data_stream
        if self.index_template is not None:
            result['indexTemplate'] = self.index_template
        if self.ilm_policy is not None:
            result['ilmPolicy'] = self.ilm_policy
        if self.priority is not None:
            result['priority'] = self.priority
        if self.index_patterns is not None:
            result['indexPatterns'] = self.index_patterns
        if self.template is not None:
            result['template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataStream') is not None:
            self.data_stream = m.get('dataStream')
        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')
        if m.get('ilmPolicy') is not None:
            self.ilm_policy = m.get('ilmPolicy')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('indexPatterns') is not None:
            self.index_patterns = m.get('indexPatterns')
        if m.get('template') is not None:
            temp_model = DescribeIndexTemplateResponseBodyResultTemplate()
            self.template = temp_model.from_map(m['template'])
        return self


class DescribeIndexTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeIndexTemplateResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeIndexTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeIndexTemplateResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeIndexTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeIndexTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIndexTemplateResponse, self).to_map()
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
            temp_model = DescribeIndexTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceResponseBodyResultDictList(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultDictList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeInstanceResponseBodyResultSynonymsDicts(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultSynonymsDicts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeInstanceResponseBodyResultZoneInfos(TeaModel):
    def __init__(self, status=None, zone_id=None):
        self.status = status  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultZoneInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class DescribeInstanceResponseBodyResultAliwsDicts(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultAliwsDicts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeInstanceResponseBodyResultTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class DescribeInstanceResponseBodyResultNodeSpec(TeaModel):
    def __init__(self, spec=None, disk=None, disk_encryption=None, disk_type=None):
        self.spec = spec  # type: str
        self.disk = disk  # type: int
        self.disk_encryption = disk_encryption  # type: bool
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultNodeSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class DescribeInstanceResponseBodyResultNetworkConfigWhiteIpGroupList(TeaModel):
    def __init__(self, white_ip_type=None, group_name=None, ips=None):
        self.white_ip_type = white_ip_type  # type: str
        self.group_name = group_name  # type: str
        self.ips = ips  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultNetworkConfigWhiteIpGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.white_ip_type is not None:
            result['whiteIpType'] = self.white_ip_type
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('whiteIpType') is not None:
            self.white_ip_type = m.get('whiteIpType')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        return self


class DescribeInstanceResponseBodyResultNetworkConfig(TeaModel):
    def __init__(self, vpc_id=None, vs_area=None, type=None, vswitch_id=None, white_ip_group_list=None):
        self.vpc_id = vpc_id  # type: str
        self.vs_area = vs_area  # type: str
        self.type = type  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.white_ip_group_list = white_ip_group_list  # type: list[DescribeInstanceResponseBodyResultNetworkConfigWhiteIpGroupList]

    def validate(self):
        if self.white_ip_group_list:
            for k in self.white_ip_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultNetworkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.type is not None:
            result['type'] = self.type
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        result['whiteIpGroupList'] = []
        if self.white_ip_group_list is not None:
            for k in self.white_ip_group_list:
                result['whiteIpGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        self.white_ip_group_list = []
        if m.get('whiteIpGroupList') is not None:
            for k in m.get('whiteIpGroupList'):
                temp_model = DescribeInstanceResponseBodyResultNetworkConfigWhiteIpGroupList()
                self.white_ip_group_list.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBodyResultKibanaConfiguration(TeaModel):
    def __init__(self, amount=None, spec=None):
        self.amount = amount  # type: int
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultKibanaConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeInstanceResponseBodyResultMasterConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultMasterConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class DescribeInstanceResponseBodyResultClientNodeConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultClientNodeConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class DescribeInstanceResponseBodyResultWarmNodeConfiguration(TeaModel):
    def __init__(self, amount=None, spec=None, disk=None, disk_encryption=None, disk_type=None):
        self.amount = amount  # type: int
        self.spec = spec  # type: str
        self.disk = disk  # type: int
        self.disk_encryption = disk_encryption  # type: bool
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultWarmNodeConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.spec is not None:
            result['spec'] = self.spec
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class DescribeInstanceResponseBodyResultAdvancedSetting(TeaModel):
    def __init__(self, gc_name=None):
        self.gc_name = gc_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultAdvancedSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gc_name is not None:
            result['gcName'] = self.gc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('gcName') is not None:
            self.gc_name = m.get('gcName')
        return self


class DescribeInstanceResponseBodyResultElasticDataNodeConfiguration(TeaModel):
    def __init__(self, amount=None, spec=None, disk=None, disk_encryption=None, disk_type=None):
        self.amount = amount  # type: int
        self.spec = spec  # type: str
        self.disk = disk  # type: int
        self.disk_encryption = disk_encryption  # type: bool
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResultElasticDataNodeConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.spec is not None:
            result['spec'] = self.spec
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class DescribeInstanceResponseBodyResult(TeaModel):
    def __init__(self, advanced_dedicate_master=None, protocol=None, enable_kibana_public_network=None,
                 node_amount=None, created_at=None, enable_kibana_private_network=None, vpc_instance_id=None, port=None,
                 enable_public=None, dedicate_master=None, kibana_port=None, es_config=None, resource_group_id=None,
                 payment_type=None, postpaid_service_status=None, es_version=None, have_kibana=None, is_new_deployment=None,
                 warm_node=None, updated_at=None, instance_id=None, zone_count=None, public_domain=None, status=None,
                 service_vpc=None, public_port=None, have_client_node=None, domain=None, description=None, kibana_domain=None,
                 dict_list=None, synonyms_dicts=None, zone_infos=None, aliws_dicts=None, tags=None, es_ipwhitelist=None,
                 extend_configs=None, private_network_ip_white_list=None, public_ip_whitelist=None,
                 kibana_private_ipwhitelist=None, es_ipblacklist=None, kibana_ipwhitelist=None, node_spec=None, network_config=None,
                 kibana_configuration=None, master_configuration=None, client_node_configuration=None, warm_node_configuration=None,
                 advanced_setting=None, elastic_data_node_configuration=None):
        self.advanced_dedicate_master = advanced_dedicate_master  # type: bool
        self.protocol = protocol  # type: str
        self.enable_kibana_public_network = enable_kibana_public_network  # type: bool
        self.node_amount = node_amount  # type: int
        self.created_at = created_at  # type: str
        self.enable_kibana_private_network = enable_kibana_private_network  # type: bool
        self.vpc_instance_id = vpc_instance_id  # type: str
        self.port = port  # type: int
        self.enable_public = enable_public  # type: bool
        self.dedicate_master = dedicate_master  # type: bool
        self.kibana_port = kibana_port  # type: int
        self.es_config = es_config  # type: dict[str, any]
        self.resource_group_id = resource_group_id  # type: str
        self.payment_type = payment_type  # type: str
        self.postpaid_service_status = postpaid_service_status  # type: str
        self.es_version = es_version  # type: str
        self.have_kibana = have_kibana  # type: bool
        self.is_new_deployment = is_new_deployment  # type: bool
        self.warm_node = warm_node  # type: bool
        self.updated_at = updated_at  # type: str
        self.instance_id = instance_id  # type: str
        self.zone_count = zone_count  # type: int
        self.public_domain = public_domain  # type: str
        self.status = status  # type: str
        self.service_vpc = service_vpc  # type: bool
        self.public_port = public_port  # type: int
        self.have_client_node = have_client_node  # type: bool
        self.domain = domain  # type: str
        self.description = description  # type: str
        self.kibana_domain = kibana_domain  # type: str
        self.dict_list = dict_list  # type: list[DescribeInstanceResponseBodyResultDictList]
        self.synonyms_dicts = synonyms_dicts  # type: list[DescribeInstanceResponseBodyResultSynonymsDicts]
        self.zone_infos = zone_infos  # type: list[DescribeInstanceResponseBodyResultZoneInfos]
        self.aliws_dicts = aliws_dicts  # type: list[DescribeInstanceResponseBodyResultAliwsDicts]
        self.tags = tags  # type: list[DescribeInstanceResponseBodyResultTags]
        self.es_ipwhitelist = es_ipwhitelist  # type: list[str]
        self.extend_configs = extend_configs  # type: list[dict[str, any]]
        self.private_network_ip_white_list = private_network_ip_white_list  # type: list[str]
        self.public_ip_whitelist = public_ip_whitelist  # type: list[str]
        self.kibana_private_ipwhitelist = kibana_private_ipwhitelist  # type: list[str]
        self.es_ipblacklist = es_ipblacklist  # type: list[str]
        self.kibana_ipwhitelist = kibana_ipwhitelist  # type: list[str]
        self.node_spec = node_spec  # type: DescribeInstanceResponseBodyResultNodeSpec
        self.network_config = network_config  # type: DescribeInstanceResponseBodyResultNetworkConfig
        self.kibana_configuration = kibana_configuration  # type: DescribeInstanceResponseBodyResultKibanaConfiguration
        self.master_configuration = master_configuration  # type: DescribeInstanceResponseBodyResultMasterConfiguration
        self.client_node_configuration = client_node_configuration  # type: DescribeInstanceResponseBodyResultClientNodeConfiguration
        self.warm_node_configuration = warm_node_configuration  # type: DescribeInstanceResponseBodyResultWarmNodeConfiguration
        self.advanced_setting = advanced_setting  # type: DescribeInstanceResponseBodyResultAdvancedSetting
        self.elastic_data_node_configuration = elastic_data_node_configuration  # type: DescribeInstanceResponseBodyResultElasticDataNodeConfiguration

    def validate(self):
        if self.dict_list:
            for k in self.dict_list:
                if k:
                    k.validate()
        if self.synonyms_dicts:
            for k in self.synonyms_dicts:
                if k:
                    k.validate()
        if self.zone_infos:
            for k in self.zone_infos:
                if k:
                    k.validate()
        if self.aliws_dicts:
            for k in self.aliws_dicts:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.network_config:
            self.network_config.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.client_node_configuration:
            self.client_node_configuration.validate()
        if self.warm_node_configuration:
            self.warm_node_configuration.validate()
        if self.advanced_setting:
            self.advanced_setting.validate()
        if self.elastic_data_node_configuration:
            self.elastic_data_node_configuration.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_dedicate_master is not None:
            result['advancedDedicateMaster'] = self.advanced_dedicate_master
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.enable_kibana_public_network is not None:
            result['enableKibanaPublicNetwork'] = self.enable_kibana_public_network
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.enable_kibana_private_network is not None:
            result['enableKibanaPrivateNetwork'] = self.enable_kibana_private_network
        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id
        if self.port is not None:
            result['port'] = self.port
        if self.enable_public is not None:
            result['enablePublic'] = self.enable_public
        if self.dedicate_master is not None:
            result['dedicateMaster'] = self.dedicate_master
        if self.kibana_port is not None:
            result['kibanaPort'] = self.kibana_port
        if self.es_config is not None:
            result['esConfig'] = self.es_config
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.postpaid_service_status is not None:
            result['postpaidServiceStatus'] = self.postpaid_service_status
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.have_kibana is not None:
            result['haveKibana'] = self.have_kibana
        if self.is_new_deployment is not None:
            result['isNewDeployment'] = self.is_new_deployment
        if self.warm_node is not None:
            result['warmNode'] = self.warm_node
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.zone_count is not None:
            result['zoneCount'] = self.zone_count
        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain
        if self.status is not None:
            result['status'] = self.status
        if self.service_vpc is not None:
            result['serviceVpc'] = self.service_vpc
        if self.public_port is not None:
            result['publicPort'] = self.public_port
        if self.have_client_node is not None:
            result['haveClientNode'] = self.have_client_node
        if self.domain is not None:
            result['domain'] = self.domain
        if self.description is not None:
            result['description'] = self.description
        if self.kibana_domain is not None:
            result['kibanaDomain'] = self.kibana_domain
        result['dictList'] = []
        if self.dict_list is not None:
            for k in self.dict_list:
                result['dictList'].append(k.to_map() if k else None)
        result['synonymsDicts'] = []
        if self.synonyms_dicts is not None:
            for k in self.synonyms_dicts:
                result['synonymsDicts'].append(k.to_map() if k else None)
        result['zoneInfos'] = []
        if self.zone_infos is not None:
            for k in self.zone_infos:
                result['zoneInfos'].append(k.to_map() if k else None)
        result['aliwsDicts'] = []
        if self.aliws_dicts is not None:
            for k in self.aliws_dicts:
                result['aliwsDicts'].append(k.to_map() if k else None)
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.es_ipwhitelist is not None:
            result['esIPWhitelist'] = self.es_ipwhitelist
        if self.extend_configs is not None:
            result['extendConfigs'] = self.extend_configs
        if self.private_network_ip_white_list is not None:
            result['privateNetworkIpWhiteList'] = self.private_network_ip_white_list
        if self.public_ip_whitelist is not None:
            result['publicIpWhitelist'] = self.public_ip_whitelist
        if self.kibana_private_ipwhitelist is not None:
            result['kibanaPrivateIPWhitelist'] = self.kibana_private_ipwhitelist
        if self.es_ipblacklist is not None:
            result['esIPBlacklist'] = self.es_ipblacklist
        if self.kibana_ipwhitelist is not None:
            result['kibanaIPWhitelist'] = self.kibana_ipwhitelist
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()
        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()
        if self.client_node_configuration is not None:
            result['clientNodeConfiguration'] = self.client_node_configuration.to_map()
        if self.warm_node_configuration is not None:
            result['warmNodeConfiguration'] = self.warm_node_configuration.to_map()
        if self.advanced_setting is not None:
            result['advancedSetting'] = self.advanced_setting.to_map()
        if self.elastic_data_node_configuration is not None:
            result['elasticDataNodeConfiguration'] = self.elastic_data_node_configuration.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('advancedDedicateMaster') is not None:
            self.advanced_dedicate_master = m.get('advancedDedicateMaster')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('enableKibanaPublicNetwork') is not None:
            self.enable_kibana_public_network = m.get('enableKibanaPublicNetwork')
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('enableKibanaPrivateNetwork') is not None:
            self.enable_kibana_private_network = m.get('enableKibanaPrivateNetwork')
        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')
        if m.get('dedicateMaster') is not None:
            self.dedicate_master = m.get('dedicateMaster')
        if m.get('kibanaPort') is not None:
            self.kibana_port = m.get('kibanaPort')
        if m.get('esConfig') is not None:
            self.es_config = m.get('esConfig')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('postpaidServiceStatus') is not None:
            self.postpaid_service_status = m.get('postpaidServiceStatus')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('haveKibana') is not None:
            self.have_kibana = m.get('haveKibana')
        if m.get('isNewDeployment') is not None:
            self.is_new_deployment = m.get('isNewDeployment')
        if m.get('warmNode') is not None:
            self.warm_node = m.get('warmNode')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('zoneCount') is not None:
            self.zone_count = m.get('zoneCount')
        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('serviceVpc') is not None:
            self.service_vpc = m.get('serviceVpc')
        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')
        if m.get('haveClientNode') is not None:
            self.have_client_node = m.get('haveClientNode')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('kibanaDomain') is not None:
            self.kibana_domain = m.get('kibanaDomain')
        self.dict_list = []
        if m.get('dictList') is not None:
            for k in m.get('dictList'):
                temp_model = DescribeInstanceResponseBodyResultDictList()
                self.dict_list.append(temp_model.from_map(k))
        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k in m.get('synonymsDicts'):
                temp_model = DescribeInstanceResponseBodyResultSynonymsDicts()
                self.synonyms_dicts.append(temp_model.from_map(k))
        self.zone_infos = []
        if m.get('zoneInfos') is not None:
            for k in m.get('zoneInfos'):
                temp_model = DescribeInstanceResponseBodyResultZoneInfos()
                self.zone_infos.append(temp_model.from_map(k))
        self.aliws_dicts = []
        if m.get('aliwsDicts') is not None:
            for k in m.get('aliwsDicts'):
                temp_model = DescribeInstanceResponseBodyResultAliwsDicts()
                self.aliws_dicts.append(temp_model.from_map(k))
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = DescribeInstanceResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('esIPWhitelist') is not None:
            self.es_ipwhitelist = m.get('esIPWhitelist')
        if m.get('extendConfigs') is not None:
            self.extend_configs = m.get('extendConfigs')
        if m.get('privateNetworkIpWhiteList') is not None:
            self.private_network_ip_white_list = m.get('privateNetworkIpWhiteList')
        if m.get('publicIpWhitelist') is not None:
            self.public_ip_whitelist = m.get('publicIpWhitelist')
        if m.get('kibanaPrivateIPWhitelist') is not None:
            self.kibana_private_ipwhitelist = m.get('kibanaPrivateIPWhitelist')
        if m.get('esIPBlacklist') is not None:
            self.es_ipblacklist = m.get('esIPBlacklist')
        if m.get('kibanaIPWhitelist') is not None:
            self.kibana_ipwhitelist = m.get('kibanaIPWhitelist')
        if m.get('nodeSpec') is not None:
            temp_model = DescribeInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('networkConfig') is not None:
            temp_model = DescribeInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('kibanaConfiguration') is not None:
            temp_model = DescribeInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m['kibanaConfiguration'])
        if m.get('masterConfiguration') is not None:
            temp_model = DescribeInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m['masterConfiguration'])
        if m.get('clientNodeConfiguration') is not None:
            temp_model = DescribeInstanceResponseBodyResultClientNodeConfiguration()
            self.client_node_configuration = temp_model.from_map(m['clientNodeConfiguration'])
        if m.get('warmNodeConfiguration') is not None:
            temp_model = DescribeInstanceResponseBodyResultWarmNodeConfiguration()
            self.warm_node_configuration = temp_model.from_map(m['warmNodeConfiguration'])
        if m.get('advancedSetting') is not None:
            temp_model = DescribeInstanceResponseBodyResultAdvancedSetting()
            self.advanced_setting = temp_model.from_map(m['advancedSetting'])
        if m.get('elasticDataNodeConfiguration') is not None:
            temp_model = DescribeInstanceResponseBodyResultElasticDataNodeConfiguration()
            self.elastic_data_node_configuration = temp_model.from_map(m['elasticDataNodeConfiguration'])
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeInstanceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
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


class DescribeKibanaSettingsResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: dict[str, any]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKibanaSettingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeKibanaSettingsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeKibanaSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeKibanaSettingsResponse, self).to_map()
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
            temp_model = DescribeKibanaSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogstashResponseBodyResultEndpointList(TeaModel):
    def __init__(self, zone_id=None, port=None, host=None):
        self.zone_id = zone_id  # type: str
        self.port = port  # type: str
        self.host = host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogstashResponseBodyResultEndpointList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        if self.port is not None:
            result['port'] = self.port
        if self.host is not None:
            result['host'] = self.host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('host') is not None:
            self.host = m.get('host')
        return self


class DescribeLogstashResponseBodyResultTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogstashResponseBodyResultTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class DescribeLogstashResponseBodyResultZoneInfos(TeaModel):
    def __init__(self, status=None, zone_id=None):
        self.status = status  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogstashResponseBodyResultZoneInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class DescribeLogstashResponseBodyResultNodeSpec(TeaModel):
    def __init__(self, spec=None, disk=None, disk_encryption=None, disk_type=None):
        self.spec = spec  # type: str
        self.disk = disk  # type: int
        self.disk_encryption = disk_encryption  # type: bool
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogstashResponseBodyResultNodeSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class DescribeLogstashResponseBodyResultNetworkConfig(TeaModel):
    def __init__(self, vpc_id=None, vs_area=None, type=None, vswitch_id=None):
        self.vpc_id = vpc_id  # type: str
        self.vs_area = vs_area  # type: str
        self.type = type  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogstashResponseBodyResultNetworkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.type is not None:
            result['type'] = self.type
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class DescribeLogstashResponseBodyResult(TeaModel):
    def __init__(self, config=None, payment_type=None, resource_group_id=None, node_amount=None, description=None,
                 created_at=None, status=None, vpc_instance_id=None, updated_at=None, version=None, instance_id=None,
                 endpoint_list=None, tags=None, zone_infos=None, extend_configs=None, node_spec=None, network_config=None):
        self.config = config  # type: dict[str, any]
        self.payment_type = payment_type  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.node_amount = node_amount  # type: int
        self.description = description  # type: str
        self.created_at = created_at  # type: str
        self.status = status  # type: str
        self.vpc_instance_id = vpc_instance_id  # type: str
        self.updated_at = updated_at  # type: str
        self.version = version  # type: str
        self.instance_id = instance_id  # type: str
        self.endpoint_list = endpoint_list  # type: list[DescribeLogstashResponseBodyResultEndpointList]
        self.tags = tags  # type: list[DescribeLogstashResponseBodyResultTags]
        self.zone_infos = zone_infos  # type: list[DescribeLogstashResponseBodyResultZoneInfos]
        self.extend_configs = extend_configs  # type: list[dict[str, any]]
        self.node_spec = node_spec  # type: DescribeLogstashResponseBodyResultNodeSpec
        self.network_config = network_config  # type: DescribeLogstashResponseBodyResultNetworkConfig

    def validate(self):
        if self.endpoint_list:
            for k in self.endpoint_list:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.zone_infos:
            for k in self.zone_infos:
                if k:
                    k.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.network_config:
            self.network_config.validate()

    def to_map(self):
        _map = super(DescribeLogstashResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.description is not None:
            result['description'] = self.description
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.status is not None:
            result['status'] = self.status
        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.version is not None:
            result['version'] = self.version
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['endpointList'] = []
        if self.endpoint_list is not None:
            for k in self.endpoint_list:
                result['endpointList'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['ZoneInfos'] = []
        if self.zone_infos is not None:
            for k in self.zone_infos:
                result['ZoneInfos'].append(k.to_map() if k else None)
        if self.extend_configs is not None:
            result['ExtendConfigs'] = self.extend_configs
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.endpoint_list = []
        if m.get('endpointList') is not None:
            for k in m.get('endpointList'):
                temp_model = DescribeLogstashResponseBodyResultEndpointList()
                self.endpoint_list.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeLogstashResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        self.zone_infos = []
        if m.get('ZoneInfos') is not None:
            for k in m.get('ZoneInfos'):
                temp_model = DescribeLogstashResponseBodyResultZoneInfos()
                self.zone_infos.append(temp_model.from_map(k))
        if m.get('ExtendConfigs') is not None:
            self.extend_configs = m.get('ExtendConfigs')
        if m.get('nodeSpec') is not None:
            temp_model = DescribeLogstashResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('networkConfig') is not None:
            temp_model = DescribeLogstashResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        return self


class DescribeLogstashResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeLogstashResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeLogstashResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeLogstashResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeLogstashResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLogstashResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogstashResponse, self).to_map()
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
            temp_model = DescribeLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePipelineResponseBodyResult(TeaModel):
    def __init__(self, pipeline_id=None, gmt_update_time=None, queue_type=None, queue_check_point_writes=None,
                 queue_max_bytes=None, config=None, batch_delay=None, workers=None, description=None, gmt_created_time=None,
                 batch_size=None, pipeline_status=None):
        self.pipeline_id = pipeline_id  # type: str
        self.gmt_update_time = gmt_update_time  # type: str
        self.queue_type = queue_type  # type: str
        self.queue_check_point_writes = queue_check_point_writes  # type: int
        self.queue_max_bytes = queue_max_bytes  # type: int
        self.config = config  # type: str
        self.batch_delay = batch_delay  # type: int
        self.workers = workers  # type: int
        self.description = description  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.batch_size = batch_size  # type: int
        self.pipeline_status = pipeline_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePipelineResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time
        if self.queue_type is not None:
            result['queueType'] = self.queue_type
        if self.queue_check_point_writes is not None:
            result['queueCheckPointWrites'] = self.queue_check_point_writes
        if self.queue_max_bytes is not None:
            result['queueMaxBytes'] = self.queue_max_bytes
        if self.config is not None:
            result['config'] = self.config
        if self.batch_delay is not None:
            result['batchDelay'] = self.batch_delay
        if self.workers is not None:
            result['workers'] = self.workers
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time
        if self.batch_size is not None:
            result['batchSize'] = self.batch_size
        if self.pipeline_status is not None:
            result['pipelineStatus'] = self.pipeline_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')
        if m.get('queueType') is not None:
            self.queue_type = m.get('queueType')
        if m.get('queueCheckPointWrites') is not None:
            self.queue_check_point_writes = m.get('queueCheckPointWrites')
        if m.get('queueMaxBytes') is not None:
            self.queue_max_bytes = m.get('queueMaxBytes')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('batchDelay') is not None:
            self.batch_delay = m.get('batchDelay')
        if m.get('workers') is not None:
            self.workers = m.get('workers')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')
        if m.get('batchSize') is not None:
            self.batch_size = m.get('batchSize')
        if m.get('pipelineStatus') is not None:
            self.pipeline_status = m.get('pipelineStatus')
        return self


class DescribePipelineResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribePipelineResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribePipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribePipelineResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribePipelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePipelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePipelineResponse, self).to_map()
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
            temp_model = DescribePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePipelineManagementConfigRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePipelineManagementConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class DescribePipelineManagementConfigResponseBodyResult(TeaModel):
    def __init__(self, endpoints=None, user_name=None, pipeline_management_type=None, es_instance_id=None,
                 pipeline_ids=None):
        self.endpoints = endpoints  # type: str
        self.user_name = user_name  # type: str
        self.pipeline_management_type = pipeline_management_type  # type: str
        self.es_instance_id = es_instance_id  # type: str
        self.pipeline_ids = pipeline_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePipelineManagementConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoints is not None:
            result['endpoints'] = self.endpoints
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.pipeline_management_type is not None:
            result['pipelineManagementType'] = self.pipeline_management_type
        if self.es_instance_id is not None:
            result['esInstanceId'] = self.es_instance_id
        if self.pipeline_ids is not None:
            result['pipelineIds'] = self.pipeline_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('pipelineManagementType') is not None:
            self.pipeline_management_type = m.get('pipelineManagementType')
        if m.get('esInstanceId') is not None:
            self.es_instance_id = m.get('esInstanceId')
        if m.get('pipelineIds') is not None:
            self.pipeline_ids = m.get('pipelineIds')
        return self


class DescribePipelineManagementConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribePipelineManagementConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribePipelineManagementConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribePipelineManagementConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribePipelineManagementConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePipelineManagementConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePipelineManagementConfigResponse, self).to_map()
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
            temp_model = DescribePipelineManagementConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyResult(TeaModel):
    def __init__(self, region_id=None, status=None, region_endpoint=None, local_name=None, console_endpoint=None):
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.local_name = local_name  # type: str
        self.console_endpoint = console_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.region_endpoint is not None:
            result['regionEndpoint'] = self.region_endpoint
        if self.local_name is not None:
            result['localName'] = self.local_name
        if self.console_endpoint is not None:
            result['consoleEndpoint'] = self.console_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('regionEndpoint') is not None:
            self.region_endpoint = m.get('regionEndpoint')
        if m.get('localName') is not None:
            self.local_name = m.get('localName')
        if m.get('consoleEndpoint') is not None:
            self.console_endpoint = m.get('consoleEndpoint')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeRegionsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
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


class DescribeSnapshotSettingResponseBodyResult(TeaModel):
    def __init__(self, enable=None, quartz_regex=None):
        self.enable = enable  # type: bool
        self.quartz_regex = quartz_regex  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSnapshotSettingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.quartz_regex is not None:
            result['QuartzRegex'] = self.quartz_regex
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('QuartzRegex') is not None:
            self.quartz_regex = m.get('QuartzRegex')
        return self


class DescribeSnapshotSettingResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeSnapshotSettingResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeSnapshotSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeSnapshotSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeSnapshotSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSnapshotSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSnapshotSettingResponse, self).to_map()
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
            temp_model = DescribeSnapshotSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplatesResponseBodyResult(TeaModel):
    def __init__(self, content=None, template_name=None):
        self.content = content  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplatesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.template_name is not None:
            result['templateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        return self


class DescribeTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeTemplatesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeTemplatesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTemplatesResponse, self).to_map()
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
            temp_model = DescribeTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeXpackMonitorConfigResponseBodyResult(TeaModel):
    def __init__(self, user_name=None, es_instance_id=None, enable=None, endpoints=None, pipeline_ids=None):
        self.user_name = user_name  # type: str
        self.es_instance_id = es_instance_id  # type: str
        self.enable = enable  # type: bool
        self.endpoints = endpoints  # type: list[str]
        self.pipeline_ids = pipeline_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeXpackMonitorConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.es_instance_id is not None:
            result['esInstanceId'] = self.es_instance_id
        if self.enable is not None:
            result['enable'] = self.enable
        if self.endpoints is not None:
            result['endpoints'] = self.endpoints
        if self.pipeline_ids is not None:
            result['pipelineIds'] = self.pipeline_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('esInstanceId') is not None:
            self.es_instance_id = m.get('esInstanceId')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')
        if m.get('pipelineIds') is not None:
            self.pipeline_ids = m.get('pipelineIds')
        return self


class DescribeXpackMonitorConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeXpackMonitorConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeXpackMonitorConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeXpackMonitorConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeXpackMonitorConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeXpackMonitorConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeXpackMonitorConfigResponse, self).to_map()
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
            temp_model = DescribeXpackMonitorConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DiagnoseInstanceRequest(TeaModel):
    def __init__(self, lang=None, client_token=None):
        self.lang = lang  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DiagnoseInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['lang'] = self.lang
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DiagnoseInstanceResponseBodyResultDiagnoseItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DiagnoseInstanceResponseBodyResultDiagnoseItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item is not None:
            result['item'] = self.item
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('item') is not None:
            self.item = m.get('item')
        return self


class DiagnoseInstanceResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, report_id=None, state=None, instance_id=None, diagnose_items=None):
        self.create_time = create_time  # type: long
        self.report_id = report_id  # type: str
        self.state = state  # type: str
        self.instance_id = instance_id  # type: str
        self.diagnose_items = diagnose_items  # type: list[DiagnoseInstanceResponseBodyResultDiagnoseItems]

    def validate(self):
        if self.diagnose_items:
            for k in self.diagnose_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DiagnoseInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.report_id is not None:
            result['reportId'] = self.report_id
        if self.state is not None:
            result['state'] = self.state
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['diagnoseItems'] = []
        if self.diagnose_items is not None:
            for k in self.diagnose_items:
                result['diagnoseItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.diagnose_items = []
        if m.get('diagnoseItems') is not None:
            for k in m.get('diagnoseItems'):
                temp_model = DiagnoseInstanceResponseBodyResultDiagnoseItems()
                self.diagnose_items.append(temp_model.from_map(k))
        return self


class DiagnoseInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DiagnoseInstanceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DiagnoseInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DiagnoseInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DiagnoseInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DiagnoseInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DiagnoseInstanceResponse, self).to_map()
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
            temp_model = DiagnoseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EstimatedLogstashRestartTimeRequest(TeaModel):
    def __init__(self, force=None):
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EstimatedLogstashRestartTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class EstimatedLogstashRestartTimeResponseBodyResult(TeaModel):
    def __init__(self, unit=None, value=None):
        self.unit = unit  # type: str
        self.value = value  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EstimatedLogstashRestartTimeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class EstimatedLogstashRestartTimeResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: EstimatedLogstashRestartTimeResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(EstimatedLogstashRestartTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = EstimatedLogstashRestartTimeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EstimatedLogstashRestartTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EstimatedLogstashRestartTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EstimatedLogstashRestartTimeResponse, self).to_map()
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
            temp_model = EstimatedLogstashRestartTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EstimatedRestartTimeRequest(TeaModel):
    def __init__(self, force=None):
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EstimatedRestartTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class EstimatedRestartTimeResponseBodyResult(TeaModel):
    def __init__(self, unit=None, value=None):
        self.unit = unit  # type: str
        self.value = value  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EstimatedRestartTimeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class EstimatedRestartTimeResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: EstimatedRestartTimeResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(EstimatedRestartTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = EstimatedRestartTimeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EstimatedRestartTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EstimatedRestartTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EstimatedRestartTimeResponse, self).to_map()
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
            temp_model = EstimatedRestartTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterDataInformationResponseBodyResultMetaInfo(TeaModel):
    def __init__(self, mapping=None, settings=None, type_name=None, fields=None, indices=None):
        self.mapping = mapping  # type: str
        self.settings = settings  # type: str
        self.type_name = type_name  # type: list[str]
        self.fields = fields  # type: list[str]
        self.indices = indices  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterDataInformationResponseBodyResultMetaInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mapping is not None:
            result['mapping'] = self.mapping
        if self.settings is not None:
            result['settings'] = self.settings
        if self.type_name is not None:
            result['typeName'] = self.type_name
        if self.fields is not None:
            result['fields'] = self.fields
        if self.indices is not None:
            result['indices'] = self.indices
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('mapping') is not None:
            self.mapping = m.get('mapping')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        if m.get('typeName') is not None:
            self.type_name = m.get('typeName')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('indices') is not None:
            self.indices = m.get('indices')
        return self


class GetClusterDataInformationResponseBodyResult(TeaModel):
    def __init__(self, connectable=None, meta_info=None):
        self.connectable = connectable  # type: bool
        self.meta_info = meta_info  # type: GetClusterDataInformationResponseBodyResultMetaInfo

    def validate(self):
        if self.meta_info:
            self.meta_info.validate()

    def to_map(self):
        _map = super(GetClusterDataInformationResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connectable is not None:
            result['connectable'] = self.connectable
        if self.meta_info is not None:
            result['metaInfo'] = self.meta_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('connectable') is not None:
            self.connectable = m.get('connectable')
        if m.get('metaInfo') is not None:
            temp_model = GetClusterDataInformationResponseBodyResultMetaInfo()
            self.meta_info = temp_model.from_map(m['metaInfo'])
        return self


class GetClusterDataInformationResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: GetClusterDataInformationResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetClusterDataInformationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetClusterDataInformationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetClusterDataInformationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetClusterDataInformationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClusterDataInformationResponse, self).to_map()
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
            temp_model = GetClusterDataInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetElastictaskResponseBodyResultElasticExpansionTask(TeaModel):
    def __init__(self, trigger_type=None, replica_count=None, elastic_node_count=None, cron_expression=None,
                 target_indices=None):
        self.trigger_type = trigger_type  # type: str
        self.replica_count = replica_count  # type: int
        self.elastic_node_count = elastic_node_count  # type: int
        self.cron_expression = cron_expression  # type: str
        self.target_indices = target_indices  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElastictaskResponseBodyResultElasticExpansionTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count
        if self.elastic_node_count is not None:
            result['elasticNodeCount'] = self.elastic_node_count
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.target_indices is not None:
            result['targetIndices'] = self.target_indices
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')
        if m.get('elasticNodeCount') is not None:
            self.elastic_node_count = m.get('elasticNodeCount')
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('targetIndices') is not None:
            self.target_indices = m.get('targetIndices')
        return self


class GetElastictaskResponseBodyResultElasticShrinkTask(TeaModel):
    def __init__(self, trigger_type=None, replica_count=None, elastic_node_count=None, cron_expression=None,
                 target_indices=None):
        self.trigger_type = trigger_type  # type: str
        self.replica_count = replica_count  # type: int
        self.elastic_node_count = elastic_node_count  # type: int
        self.cron_expression = cron_expression  # type: str
        self.target_indices = target_indices  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetElastictaskResponseBodyResultElasticShrinkTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count
        if self.elastic_node_count is not None:
            result['elasticNodeCount'] = self.elastic_node_count
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.target_indices is not None:
            result['targetIndices'] = self.target_indices
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')
        if m.get('elasticNodeCount') is not None:
            self.elastic_node_count = m.get('elasticNodeCount')
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('targetIndices') is not None:
            self.target_indices = m.get('targetIndices')
        return self


class GetElastictaskResponseBodyResult(TeaModel):
    def __init__(self, elastic_expansion_task=None, elastic_shrink_task=None):
        self.elastic_expansion_task = elastic_expansion_task  # type: GetElastictaskResponseBodyResultElasticExpansionTask
        self.elastic_shrink_task = elastic_shrink_task  # type: GetElastictaskResponseBodyResultElasticShrinkTask

    def validate(self):
        if self.elastic_expansion_task:
            self.elastic_expansion_task.validate()
        if self.elastic_shrink_task:
            self.elastic_shrink_task.validate()

    def to_map(self):
        _map = super(GetElastictaskResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_expansion_task is not None:
            result['elasticExpansionTask'] = self.elastic_expansion_task.to_map()
        if self.elastic_shrink_task is not None:
            result['elasticShrinkTask'] = self.elastic_shrink_task.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('elasticExpansionTask') is not None:
            temp_model = GetElastictaskResponseBodyResultElasticExpansionTask()
            self.elastic_expansion_task = temp_model.from_map(m['elasticExpansionTask'])
        if m.get('elasticShrinkTask') is not None:
            temp_model = GetElastictaskResponseBodyResultElasticShrinkTask()
            self.elastic_shrink_task = temp_model.from_map(m['elasticShrinkTask'])
        return self


class GetElastictaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: GetElastictaskResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetElastictaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetElastictaskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetElastictaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetElastictaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetElastictaskResponse, self).to_map()
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
            temp_model = GetElastictaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmonGrafanaAlertsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEmonGrafanaAlertsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEmonGrafanaAlertsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEmonGrafanaAlertsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEmonGrafanaAlertsResponse, self).to_map()
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
            temp_model = GetEmonGrafanaAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmonGrafanaDashboardsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEmonGrafanaDashboardsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEmonGrafanaDashboardsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEmonGrafanaDashboardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEmonGrafanaDashboardsResponse, self).to_map()
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
            temp_model = GetEmonGrafanaDashboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmonMonitorDataResponseBodyResult(TeaModel):
    def __init__(self, integrity=None, summary=None, message_watermark=None, dps=None, tags=None, metric=None):
        self.integrity = integrity  # type: float
        self.summary = summary  # type: float
        self.message_watermark = message_watermark  # type: long
        self.dps = dps  # type: dict[str, any]
        self.tags = tags  # type: dict[str, any]
        self.metric = metric  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEmonMonitorDataResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.integrity is not None:
            result['integrity'] = self.integrity
        if self.summary is not None:
            result['summary'] = self.summary
        if self.message_watermark is not None:
            result['messageWatermark'] = self.message_watermark
        if self.dps is not None:
            result['dps'] = self.dps
        if self.tags is not None:
            result['tags'] = self.tags
        if self.metric is not None:
            result['metric'] = self.metric
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('integrity') is not None:
            self.integrity = m.get('integrity')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('messageWatermark') is not None:
            self.message_watermark = m.get('messageWatermark')
        if m.get('dps') is not None:
            self.dps = m.get('dps')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        return self


class GetEmonMonitorDataResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.result = result  # type: list[GetEmonMonitorDataResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEmonMonitorDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetEmonMonitorDataResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetEmonMonitorDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEmonMonitorDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEmonMonitorDataResponse, self).to_map()
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
            temp_model = GetEmonMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenStoreUsageResponseBodyResult(TeaModel):
    def __init__(self, last_day_usage=None, current_usage=None):
        # 昨日使用容量
        self.last_day_usage = last_day_usage  # type: long
        # 当前使用量
        self.current_usage = current_usage  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOpenStoreUsageResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_day_usage is not None:
            result['lastDayUsage'] = self.last_day_usage
        if self.current_usage is not None:
            result['currentUsage'] = self.current_usage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('lastDayUsage') is not None:
            self.last_day_usage = m.get('lastDayUsage')
        if m.get('currentUsage') is not None:
            self.current_usage = m.get('currentUsage')
        return self


class GetOpenStoreUsageResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: GetOpenStoreUsageResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetOpenStoreUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetOpenStoreUsageResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetOpenStoreUsageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOpenStoreUsageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOpenStoreUsageResponse, self).to_map()
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
            temp_model = GetOpenStoreUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegionConfigurationRequest(TeaModel):
    def __init__(self, zone_id=None):
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        return self


class GetRegionConfigurationResponseBodyResultDataDiskList(TeaModel):
    def __init__(self, scale_limit=None, min_size=None, max_size=None, disk_type=None, value_limit_set=None):
        self.scale_limit = scale_limit  # type: int
        self.min_size = min_size  # type: int
        self.max_size = max_size  # type: int
        self.disk_type = disk_type  # type: str
        self.value_limit_set = value_limit_set  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultDataDiskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit
        if self.min_size is not None:
            result['minSize'] = self.min_size
        if self.max_size is not None:
            result['maxSize'] = self.max_size
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')
        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')
        return self


class GetRegionConfigurationResponseBodyResultEsVersionsLatestList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultEsVersionsLatestList, self).to_map()
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


class GetRegionConfigurationResponseBodyResultNodeSpecList(TeaModel):
    def __init__(self, memory_size=None, cpu_count=None, disk_type=None, spec=None, disk=None, spec_group_type=None,
                 enable=None):
        self.memory_size = memory_size  # type: int
        self.cpu_count = cpu_count  # type: int
        self.disk_type = disk_type  # type: str
        self.spec = spec  # type: str
        self.disk = disk  # type: int
        self.spec_group_type = spec_group_type  # type: str
        self.enable = enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultNodeSpecList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.spec is not None:
            result['spec'] = self.spec
        if self.disk is not None:
            result['disk'] = self.disk
        if self.spec_group_type is not None:
            result['specGroupType'] = self.spec_group_type
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('specGroupType') is not None:
            self.spec_group_type = m.get('specGroupType')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class GetRegionConfigurationResponseBodyResultClientNodeDiskList(TeaModel):
    def __init__(self, scale_limit=None, min_size=None, max_size=None, disk_type=None):
        self.scale_limit = scale_limit  # type: int
        self.min_size = min_size  # type: int
        self.max_size = max_size  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultClientNodeDiskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit
        if self.min_size is not None:
            result['minSize'] = self.min_size
        if self.max_size is not None:
            result['maxSize'] = self.max_size
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')
        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class GetRegionConfigurationResponseBodyResultMasterDiskList(TeaModel):
    def __init__(self, scale_limit=None, min_size=None, max_size=None, disk_type=None):
        self.scale_limit = scale_limit  # type: int
        self.min_size = min_size  # type: int
        self.max_size = max_size  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultMasterDiskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit
        if self.min_size is not None:
            result['minSize'] = self.min_size
        if self.max_size is not None:
            result['maxSize'] = self.max_size
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')
        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class GetRegionConfigurationResponseBodyResultSupportVersionsSupportVersionList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultSupportVersionsSupportVersionList, self).to_map()
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


class GetRegionConfigurationResponseBodyResultSupportVersions(TeaModel):
    def __init__(self, instance_category=None, support_version_list=None):
        self.instance_category = instance_category  # type: str
        self.support_version_list = support_version_list  # type: list[GetRegionConfigurationResponseBodyResultSupportVersionsSupportVersionList]

    def validate(self):
        if self.support_version_list:
            for k in self.support_version_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultSupportVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_category is not None:
            result['instanceCategory'] = self.instance_category
        result['supportVersionList'] = []
        if self.support_version_list is not None:
            for k in self.support_version_list:
                result['supportVersionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceCategory') is not None:
            self.instance_category = m.get('instanceCategory')
        self.support_version_list = []
        if m.get('supportVersionList') is not None:
            for k in m.get('supportVersionList'):
                temp_model = GetRegionConfigurationResponseBodyResultSupportVersionsSupportVersionList()
                self.support_version_list.append(temp_model.from_map(k))
        return self


class GetRegionConfigurationResponseBodyResultNode(TeaModel):
    def __init__(self, max_amount=None, min_amount=None):
        self.max_amount = max_amount  # type: int
        self.min_amount = min_amount  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['minAmount'] = self.min_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')
        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')
        return self


class GetRegionConfigurationResponseBodyResultJvmConfine(TeaModel):
    def __init__(self, memory=None, support_es_versions=None, support_gcs=None):
        self.memory = memory  # type: int
        self.support_es_versions = support_es_versions  # type: list[str]
        self.support_gcs = support_gcs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultJvmConfine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.memory is not None:
            result['memory'] = self.memory
        if self.support_es_versions is not None:
            result['supportEsVersions'] = self.support_es_versions
        if self.support_gcs is not None:
            result['supportGcs'] = self.support_gcs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('supportEsVersions') is not None:
            self.support_es_versions = m.get('supportEsVersions')
        if m.get('supportGcs') is not None:
            self.support_gcs = m.get('supportGcs')
        return self


class GetRegionConfigurationResponseBodyResultClientNodeAmountRange(TeaModel):
    def __init__(self, max_amount=None, min_amount=None):
        self.max_amount = max_amount  # type: int
        self.min_amount = min_amount  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultClientNodeAmountRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['minAmount'] = self.min_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')
        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')
        return self


class GetRegionConfigurationResponseBodyResultWarmNodePropertiesDiskList(TeaModel):
    def __init__(self, scale_limit=None, min_size=None, disk_encryption=None, max_size=None, disk_type=None,
                 value_limit_set=None):
        self.scale_limit = scale_limit  # type: int
        self.min_size = min_size  # type: int
        self.disk_encryption = disk_encryption  # type: bool
        self.max_size = max_size  # type: int
        self.disk_type = disk_type  # type: str
        self.value_limit_set = value_limit_set  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultWarmNodePropertiesDiskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit
        if self.min_size is not None:
            result['minSize'] = self.min_size
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.max_size is not None:
            result['maxSize'] = self.max_size
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')
        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')
        return self


class GetRegionConfigurationResponseBodyResultWarmNodePropertiesAmountRange(TeaModel):
    def __init__(self, max_amount=None, min_amount=None):
        self.max_amount = max_amount  # type: int
        self.min_amount = min_amount  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultWarmNodePropertiesAmountRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['minAmount'] = self.min_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')
        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')
        return self


class GetRegionConfigurationResponseBodyResultWarmNodeProperties(TeaModel):
    def __init__(self, disk_list=None, spec=None, amount_range=None):
        self.disk_list = disk_list  # type: list[GetRegionConfigurationResponseBodyResultWarmNodePropertiesDiskList]
        self.spec = spec  # type: list[str]
        self.amount_range = amount_range  # type: GetRegionConfigurationResponseBodyResultWarmNodePropertiesAmountRange

    def validate(self):
        if self.disk_list:
            for k in self.disk_list:
                if k:
                    k.validate()
        if self.amount_range:
            self.amount_range.validate()

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultWarmNodeProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['diskList'] = []
        if self.disk_list is not None:
            for k in self.disk_list:
                result['diskList'].append(k.to_map() if k else None)
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount_range is not None:
            result['amountRange'] = self.amount_range.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.disk_list = []
        if m.get('diskList') is not None:
            for k in m.get('diskList'):
                temp_model = GetRegionConfigurationResponseBodyResultWarmNodePropertiesDiskList()
                self.disk_list.append(temp_model.from_map(k))
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amountRange') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultWarmNodePropertiesAmountRange()
            self.amount_range = temp_model.from_map(m['amountRange'])
        return self


class GetRegionConfigurationResponseBodyResultKibanaNodePropertiesAmountRange(TeaModel):
    def __init__(self, max_amount=None, min_amount=None):
        self.max_amount = max_amount  # type: int
        self.min_amount = min_amount  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultKibanaNodePropertiesAmountRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['minAmount'] = self.min_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')
        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')
        return self


class GetRegionConfigurationResponseBodyResultKibanaNodeProperties(TeaModel):
    def __init__(self, spec=None, amount_range=None):
        self.spec = spec  # type: list[str]
        self.amount_range = amount_range  # type: GetRegionConfigurationResponseBodyResultKibanaNodePropertiesAmountRange

    def validate(self):
        if self.amount_range:
            self.amount_range.validate()

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultKibanaNodeProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount_range is not None:
            result['amountRange'] = self.amount_range.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amountRange') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultKibanaNodePropertiesAmountRange()
            self.amount_range = temp_model.from_map(m['amountRange'])
        return self


class GetRegionConfigurationResponseBodyResultElasticNodePropertiesDiskList(TeaModel):
    def __init__(self, scale_limit=None, min_size=None, disk_encryption=None, max_size=None, disk_type=None,
                 value_limit_set=None):
        self.scale_limit = scale_limit  # type: int
        self.min_size = min_size  # type: int
        self.disk_encryption = disk_encryption  # type: bool
        self.max_size = max_size  # type: int
        self.disk_type = disk_type  # type: str
        self.value_limit_set = value_limit_set  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultElasticNodePropertiesDiskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit
        if self.min_size is not None:
            result['minSize'] = self.min_size
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.max_size is not None:
            result['maxSize'] = self.max_size
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')
        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')
        return self


class GetRegionConfigurationResponseBodyResultElasticNodePropertiesAmountRange(TeaModel):
    def __init__(self, max_amount=None, min_amount=None):
        self.max_amount = max_amount  # type: int
        self.min_amount = min_amount  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultElasticNodePropertiesAmountRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['minAmount'] = self.min_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')
        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')
        return self


class GetRegionConfigurationResponseBodyResultElasticNodeProperties(TeaModel):
    def __init__(self, disk_list=None, spec=None, amount_range=None):
        self.disk_list = disk_list  # type: list[GetRegionConfigurationResponseBodyResultElasticNodePropertiesDiskList]
        self.spec = spec  # type: list[str]
        self.amount_range = amount_range  # type: GetRegionConfigurationResponseBodyResultElasticNodePropertiesAmountRange

    def validate(self):
        if self.disk_list:
            for k in self.disk_list:
                if k:
                    k.validate()
        if self.amount_range:
            self.amount_range.validate()

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResultElasticNodeProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['diskList'] = []
        if self.disk_list is not None:
            for k in self.disk_list:
                result['diskList'].append(k.to_map() if k else None)
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount_range is not None:
            result['amountRange'] = self.amount_range.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.disk_list = []
        if m.get('diskList') is not None:
            for k in m.get('diskList'):
                temp_model = GetRegionConfigurationResponseBodyResultElasticNodePropertiesDiskList()
                self.disk_list.append(temp_model.from_map(k))
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amountRange') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultElasticNodePropertiesAmountRange()
            self.amount_range = temp_model.from_map(m['amountRange'])
        return self


class GetRegionConfigurationResponseBodyResult(TeaModel):
    def __init__(self, env=None, region_id=None, create_url=None, data_disk_list=None, es_versions_latest_list=None,
                 node_spec_list=None, client_node_disk_list=None, master_disk_list=None, support_versions=None, master_spec=None,
                 client_node_spec=None, zones=None, instance_support_nodes=None, es_versions=None, node=None, jvm_confine=None,
                 client_node_amount_range=None, warm_node_properties=None, kibana_node_properties=None, elastic_node_properties=None):
        self.env = env  # type: str
        self.region_id = region_id  # type: str
        self.create_url = create_url  # type: str
        self.data_disk_list = data_disk_list  # type: list[GetRegionConfigurationResponseBodyResultDataDiskList]
        self.es_versions_latest_list = es_versions_latest_list  # type: list[GetRegionConfigurationResponseBodyResultEsVersionsLatestList]
        self.node_spec_list = node_spec_list  # type: list[GetRegionConfigurationResponseBodyResultNodeSpecList]
        self.client_node_disk_list = client_node_disk_list  # type: list[GetRegionConfigurationResponseBodyResultClientNodeDiskList]
        self.master_disk_list = master_disk_list  # type: list[GetRegionConfigurationResponseBodyResultMasterDiskList]
        self.support_versions = support_versions  # type: list[GetRegionConfigurationResponseBodyResultSupportVersions]
        self.master_spec = master_spec  # type: list[str]
        self.client_node_spec = client_node_spec  # type: list[str]
        self.zones = zones  # type: list[str]
        self.instance_support_nodes = instance_support_nodes  # type: list[str]
        self.es_versions = es_versions  # type: list[str]
        self.node = node  # type: GetRegionConfigurationResponseBodyResultNode
        self.jvm_confine = jvm_confine  # type: GetRegionConfigurationResponseBodyResultJvmConfine
        self.client_node_amount_range = client_node_amount_range  # type: GetRegionConfigurationResponseBodyResultClientNodeAmountRange
        self.warm_node_properties = warm_node_properties  # type: GetRegionConfigurationResponseBodyResultWarmNodeProperties
        self.kibana_node_properties = kibana_node_properties  # type: GetRegionConfigurationResponseBodyResultKibanaNodeProperties
        self.elastic_node_properties = elastic_node_properties  # type: GetRegionConfigurationResponseBodyResultElasticNodeProperties

    def validate(self):
        if self.data_disk_list:
            for k in self.data_disk_list:
                if k:
                    k.validate()
        if self.es_versions_latest_list:
            for k in self.es_versions_latest_list:
                if k:
                    k.validate()
        if self.node_spec_list:
            for k in self.node_spec_list:
                if k:
                    k.validate()
        if self.client_node_disk_list:
            for k in self.client_node_disk_list:
                if k:
                    k.validate()
        if self.master_disk_list:
            for k in self.master_disk_list:
                if k:
                    k.validate()
        if self.support_versions:
            for k in self.support_versions:
                if k:
                    k.validate()
        if self.node:
            self.node.validate()
        if self.jvm_confine:
            self.jvm_confine.validate()
        if self.client_node_amount_range:
            self.client_node_amount_range.validate()
        if self.warm_node_properties:
            self.warm_node_properties.validate()
        if self.kibana_node_properties:
            self.kibana_node_properties.validate()
        if self.elastic_node_properties:
            self.elastic_node_properties.validate()

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['env'] = self.env
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.create_url is not None:
            result['createUrl'] = self.create_url
        result['dataDiskList'] = []
        if self.data_disk_list is not None:
            for k in self.data_disk_list:
                result['dataDiskList'].append(k.to_map() if k else None)
        result['esVersionsLatestList'] = []
        if self.es_versions_latest_list is not None:
            for k in self.es_versions_latest_list:
                result['esVersionsLatestList'].append(k.to_map() if k else None)
        result['nodeSpecList'] = []
        if self.node_spec_list is not None:
            for k in self.node_spec_list:
                result['nodeSpecList'].append(k.to_map() if k else None)
        result['clientNodeDiskList'] = []
        if self.client_node_disk_list is not None:
            for k in self.client_node_disk_list:
                result['clientNodeDiskList'].append(k.to_map() if k else None)
        result['masterDiskList'] = []
        if self.master_disk_list is not None:
            for k in self.master_disk_list:
                result['masterDiskList'].append(k.to_map() if k else None)
        result['supportVersions'] = []
        if self.support_versions is not None:
            for k in self.support_versions:
                result['supportVersions'].append(k.to_map() if k else None)
        if self.master_spec is not None:
            result['masterSpec'] = self.master_spec
        if self.client_node_spec is not None:
            result['clientNodeSpec'] = self.client_node_spec
        if self.zones is not None:
            result['zones'] = self.zones
        if self.instance_support_nodes is not None:
            result['instanceSupportNodes'] = self.instance_support_nodes
        if self.es_versions is not None:
            result['esVersions'] = self.es_versions
        if self.node is not None:
            result['node'] = self.node.to_map()
        if self.jvm_confine is not None:
            result['jvmConfine'] = self.jvm_confine.to_map()
        if self.client_node_amount_range is not None:
            result['clientNodeAmountRange'] = self.client_node_amount_range.to_map()
        if self.warm_node_properties is not None:
            result['warmNodeProperties'] = self.warm_node_properties.to_map()
        if self.kibana_node_properties is not None:
            result['kibanaNodeProperties'] = self.kibana_node_properties.to_map()
        if self.elastic_node_properties is not None:
            result['elasticNodeProperties'] = self.elastic_node_properties.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('env') is not None:
            self.env = m.get('env')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('createUrl') is not None:
            self.create_url = m.get('createUrl')
        self.data_disk_list = []
        if m.get('dataDiskList') is not None:
            for k in m.get('dataDiskList'):
                temp_model = GetRegionConfigurationResponseBodyResultDataDiskList()
                self.data_disk_list.append(temp_model.from_map(k))
        self.es_versions_latest_list = []
        if m.get('esVersionsLatestList') is not None:
            for k in m.get('esVersionsLatestList'):
                temp_model = GetRegionConfigurationResponseBodyResultEsVersionsLatestList()
                self.es_versions_latest_list.append(temp_model.from_map(k))
        self.node_spec_list = []
        if m.get('nodeSpecList') is not None:
            for k in m.get('nodeSpecList'):
                temp_model = GetRegionConfigurationResponseBodyResultNodeSpecList()
                self.node_spec_list.append(temp_model.from_map(k))
        self.client_node_disk_list = []
        if m.get('clientNodeDiskList') is not None:
            for k in m.get('clientNodeDiskList'):
                temp_model = GetRegionConfigurationResponseBodyResultClientNodeDiskList()
                self.client_node_disk_list.append(temp_model.from_map(k))
        self.master_disk_list = []
        if m.get('masterDiskList') is not None:
            for k in m.get('masterDiskList'):
                temp_model = GetRegionConfigurationResponseBodyResultMasterDiskList()
                self.master_disk_list.append(temp_model.from_map(k))
        self.support_versions = []
        if m.get('supportVersions') is not None:
            for k in m.get('supportVersions'):
                temp_model = GetRegionConfigurationResponseBodyResultSupportVersions()
                self.support_versions.append(temp_model.from_map(k))
        if m.get('masterSpec') is not None:
            self.master_spec = m.get('masterSpec')
        if m.get('clientNodeSpec') is not None:
            self.client_node_spec = m.get('clientNodeSpec')
        if m.get('zones') is not None:
            self.zones = m.get('zones')
        if m.get('instanceSupportNodes') is not None:
            self.instance_support_nodes = m.get('instanceSupportNodes')
        if m.get('esVersions') is not None:
            self.es_versions = m.get('esVersions')
        if m.get('node') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultNode()
            self.node = temp_model.from_map(m['node'])
        if m.get('jvmConfine') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultJvmConfine()
            self.jvm_confine = temp_model.from_map(m['jvmConfine'])
        if m.get('clientNodeAmountRange') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultClientNodeAmountRange()
            self.client_node_amount_range = temp_model.from_map(m['clientNodeAmountRange'])
        if m.get('warmNodeProperties') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultWarmNodeProperties()
            self.warm_node_properties = temp_model.from_map(m['warmNodeProperties'])
        if m.get('kibanaNodeProperties') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultKibanaNodeProperties()
            self.kibana_node_properties = temp_model.from_map(m['kibanaNodeProperties'])
        if m.get('elasticNodeProperties') is not None:
            temp_model = GetRegionConfigurationResponseBodyResultElasticNodeProperties()
            self.elastic_node_properties = temp_model.from_map(m['elasticNodeProperties'])
        return self


class GetRegionConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: GetRegionConfigurationResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetRegionConfigurationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetRegionConfigurationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRegionConfigurationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRegionConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRegionConfigurationResponse, self).to_map()
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
            temp_model = GetRegionConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSuggestShrinkableNodesRequest(TeaModel):
    def __init__(self, node_type=None, count=None, ignore_status=None):
        self.node_type = node_type  # type: str
        self.count = count  # type: int
        self.ignore_status = ignore_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSuggestShrinkableNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.count is not None:
            result['count'] = self.count
        if self.ignore_status is not None:
            result['ignoreStatus'] = self.ignore_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('ignoreStatus') is not None:
            self.ignore_status = m.get('ignoreStatus')
        return self


class GetSuggestShrinkableNodesResponseBodyResult(TeaModel):
    def __init__(self, port=None, host=None):
        self.port = port  # type: int
        self.host = host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSuggestShrinkableNodesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.host is not None:
            result['host'] = self.host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('host') is not None:
            self.host = m.get('host')
        return self


class GetSuggestShrinkableNodesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetSuggestShrinkableNodesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSuggestShrinkableNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetSuggestShrinkableNodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetSuggestShrinkableNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSuggestShrinkableNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSuggestShrinkableNodesResponse, self).to_map()
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
            temp_model = GetSuggestShrinkableNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTransferableNodesRequest(TeaModel):
    def __init__(self, node_type=None, count=None):
        self.node_type = node_type  # type: str
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTransferableNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetTransferableNodesResponseBodyResult(TeaModel):
    def __init__(self, port=None, host=None):
        self.port = port  # type: int
        self.host = host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTransferableNodesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['port'] = self.port
        if self.host is not None:
            result['host'] = self.host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('host') is not None:
            self.host = m.get('host')
        return self


class GetTransferableNodesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetTransferableNodesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTransferableNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetTransferableNodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetTransferableNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTransferableNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTransferableNodesResponse, self).to_map()
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
            temp_model = GetTransferableNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeOperationRoleRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeOperationRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class InitializeOperationRoleResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeOperationRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InitializeOperationRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InitializeOperationRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitializeOperationRoleResponse, self).to_map()
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
            temp_model = InitializeOperationRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallAckOperatorRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallAckOperatorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class InstallAckOperatorResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallAckOperatorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InstallAckOperatorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InstallAckOperatorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallAckOperatorResponse, self).to_map()
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
            temp_model = InstallAckOperatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallKibanaSystemPluginRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallKibanaSystemPluginRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class InstallKibanaSystemPluginResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallKibanaSystemPluginResponseBody, self).to_map()
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


class InstallKibanaSystemPluginResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InstallKibanaSystemPluginResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallKibanaSystemPluginResponse, self).to_map()
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
            temp_model = InstallKibanaSystemPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallLogstashSystemPluginRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallLogstashSystemPluginRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class InstallLogstashSystemPluginResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallLogstashSystemPluginResponseBody, self).to_map()
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


class InstallLogstashSystemPluginResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InstallLogstashSystemPluginResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallLogstashSystemPluginResponse, self).to_map()
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
            temp_model = InstallLogstashSystemPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallSystemPluginRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallSystemPluginRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class InstallSystemPluginResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallSystemPluginResponseBody, self).to_map()
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


class InstallSystemPluginResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InstallSystemPluginResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallSystemPluginResponse, self).to_map()
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
            temp_model = InstallSystemPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallUserPluginsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallUserPluginsResponseBody, self).to_map()
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


class InstallUserPluginsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InstallUserPluginsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallUserPluginsResponse, self).to_map()
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
            temp_model = InstallUserPluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InterruptElasticsearchTaskRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InterruptElasticsearchTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class InterruptElasticsearchTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InterruptElasticsearchTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InterruptElasticsearchTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InterruptElasticsearchTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InterruptElasticsearchTaskResponse, self).to_map()
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
            temp_model = InterruptElasticsearchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InterruptLogstashTaskRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InterruptLogstashTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class InterruptLogstashTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InterruptLogstashTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class InterruptLogstashTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InterruptLogstashTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InterruptLogstashTaskResponse, self).to_map()
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
            temp_model = InterruptLogstashTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAckClustersRequest(TeaModel):
    def __init__(self, page=None, size=None, vpc_id=None):
        self.page = page  # type: int
        self.size = size  # type: int
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAckClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListAckClustersResponseBodyResult(TeaModel):
    def __init__(self, cluster_type=None, vpc_id=None, name=None, cluster_id=None):
        self.cluster_type = cluster_type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.name = name  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAckClustersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.name is not None:
            result['name'] = self.name
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        return self


class ListAckClustersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListAckClustersResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAckClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAckClustersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAckClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAckClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAckClustersResponse, self).to_map()
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
            temp_model = ListAckClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAckNamespacesRequest(TeaModel):
    def __init__(self, page=None, size=None):
        self.page = page  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAckNamespacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAckNamespacesResponseBodyResult(TeaModel):
    def __init__(self, namespace=None, status=None):
        self.namespace = namespace  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAckNamespacesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListAckNamespacesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListAckNamespacesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAckNamespacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAckNamespacesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAckNamespacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAckNamespacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAckNamespacesResponse, self).to_map()
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
            temp_model = ListAckNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllNodeRequest(TeaModel):
    def __init__(self, extended=None):
        self.extended = extended  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAllNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended is not None:
            result['extended'] = self.extended
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('extended') is not None:
            self.extended = m.get('extended')
        return self


class ListAllNodeResponseBodyResult(TeaModel):
    def __init__(self, heap_percent=None, zone_id=None, cpu_percent=None, host=None, node_type=None,
                 disk_used_percent=None, port=None, load_one_m=None, health=None):
        self.heap_percent = heap_percent  # type: str
        self.zone_id = zone_id  # type: str
        self.cpu_percent = cpu_percent  # type: str
        self.host = host  # type: str
        self.node_type = node_type  # type: str
        self.disk_used_percent = disk_used_percent  # type: str
        self.port = port  # type: int
        self.load_one_m = load_one_m  # type: str
        self.health = health  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAllNodeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.heap_percent is not None:
            result['heapPercent'] = self.heap_percent
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        if self.cpu_percent is not None:
            result['cpuPercent'] = self.cpu_percent
        if self.host is not None:
            result['host'] = self.host
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.disk_used_percent is not None:
            result['diskUsedPercent'] = self.disk_used_percent
        if self.port is not None:
            result['port'] = self.port
        if self.load_one_m is not None:
            result['loadOneM'] = self.load_one_m
        if self.health is not None:
            result['health'] = self.health
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('heapPercent') is not None:
            self.heap_percent = m.get('heapPercent')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        if m.get('cpuPercent') is not None:
            self.cpu_percent = m.get('cpuPercent')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('diskUsedPercent') is not None:
            self.disk_used_percent = m.get('diskUsedPercent')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('loadOneM') is not None:
            self.load_one_m = m.get('loadOneM')
        if m.get('health') is not None:
            self.health = m.get('health')
        return self


class ListAllNodeResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListAllNodeResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAllNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAllNodeResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAllNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAllNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAllNodeResponse, self).to_map()
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
            temp_model = ListAllNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlternativeSnapshotReposRequest(TeaModel):
    def __init__(self, already_set_items=None):
        self.already_set_items = already_set_items  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlternativeSnapshotReposRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_set_items is not None:
            result['alreadySetItems'] = self.already_set_items
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alreadySetItems') is not None:
            self.already_set_items = m.get('alreadySetItems')
        return self


class ListAlternativeSnapshotReposResponseBodyResult(TeaModel):
    def __init__(self, repo_path=None, instance_id=None):
        self.repo_path = repo_path  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlternativeSnapshotReposResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_path is not None:
            result['repoPath'] = self.repo_path
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('repoPath') is not None:
            self.repo_path = m.get('repoPath')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ListAlternativeSnapshotReposResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListAlternativeSnapshotReposResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlternativeSnapshotReposResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAlternativeSnapshotReposResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAlternativeSnapshotReposResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlternativeSnapshotReposResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlternativeSnapshotReposResponse, self).to_map()
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
            temp_model = ListAlternativeSnapshotReposResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableEsInstanceIdsResponseBodyResult(TeaModel):
    def __init__(self, endpoint=None, description=None, kibana_endpoint=None, es_instance_id=None):
        self.endpoint = endpoint  # type: str
        self.description = description  # type: str
        self.kibana_endpoint = kibana_endpoint  # type: str
        self.es_instance_id = es_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableEsInstanceIdsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.description is not None:
            result['description'] = self.description
        if self.kibana_endpoint is not None:
            result['kibanaEndpoint'] = self.kibana_endpoint
        if self.es_instance_id is not None:
            result['esInstanceId'] = self.es_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('kibanaEndpoint') is not None:
            self.kibana_endpoint = m.get('kibanaEndpoint')
        if m.get('esInstanceId') is not None:
            self.es_instance_id = m.get('esInstanceId')
        return self


class ListAvailableEsInstanceIdsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListAvailableEsInstanceIdsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableEsInstanceIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAvailableEsInstanceIdsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAvailableEsInstanceIdsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAvailableEsInstanceIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAvailableEsInstanceIdsResponse, self).to_map()
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
            temp_model = ListAvailableEsInstanceIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCollectorsRequest(TeaModel):
    def __init__(self, res_id=None, name=None, instance_id=None, page=None, size=None, source_type=None):
        self.res_id = res_id  # type: str
        self.name = name  # type: str
        self.instance_id = instance_id  # type: str
        self.page = page  # type: int
        self.size = size  # type: int
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_id is not None:
            result['resId'] = self.res_id
        if self.name is not None:
            result['name'] = self.name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resId') is not None:
            self.res_id = m.get('resId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class ListCollectorsResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectorsResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListCollectorsResponseBodyResultConfigs(TeaModel):
    def __init__(self, content=None, file_name=None):
        self.content = content  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectorsResponseBodyResultConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class ListCollectorsResponseBodyResultExtendConfigsMachines(TeaModel):
    def __init__(self, agent_status=None, instance_id=None):
        self.agent_status = agent_status  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCollectorsResponseBodyResultExtendConfigsMachines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['agentStatus'] = self.agent_status
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('agentStatus') is not None:
            self.agent_status = m.get('agentStatus')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ListCollectorsResponseBodyResultExtendConfigs(TeaModel):
    def __init__(self, success_pods_count=None, protocol=None, user_name=None, total_pods_count=None, type=None,
                 kibana_host=None, enable_monitoring=None, config_type=None, instance_type=None, group_id=None, host=None,
                 instance_id=None, machines=None, hosts=None):
        self.success_pods_count = success_pods_count  # type: str
        self.protocol = protocol  # type: str
        self.user_name = user_name  # type: str
        self.total_pods_count = total_pods_count  # type: str
        self.type = type  # type: str
        self.kibana_host = kibana_host  # type: str
        self.enable_monitoring = enable_monitoring  # type: bool
        self.config_type = config_type  # type: str
        self.instance_type = instance_type  # type: str
        self.group_id = group_id  # type: str
        self.host = host  # type: str
        self.instance_id = instance_id  # type: str
        self.machines = machines  # type: list[ListCollectorsResponseBodyResultExtendConfigsMachines]
        self.hosts = hosts  # type: list[str]

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCollectorsResponseBodyResultExtendConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_pods_count is not None:
            result['successPodsCount'] = self.success_pods_count
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.total_pods_count is not None:
            result['totalPodsCount'] = self.total_pods_count
        if self.type is not None:
            result['type'] = self.type
        if self.kibana_host is not None:
            result['kibanaHost'] = self.kibana_host
        if self.enable_monitoring is not None:
            result['enableMonitoring'] = self.enable_monitoring
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.host is not None:
            result['host'] = self.host
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['machines'] = []
        if self.machines is not None:
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
        if self.hosts is not None:
            result['hosts'] = self.hosts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('successPodsCount') is not None:
            self.success_pods_count = m.get('successPodsCount')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('totalPodsCount') is not None:
            self.total_pods_count = m.get('totalPodsCount')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('kibanaHost') is not None:
            self.kibana_host = m.get('kibanaHost')
        if m.get('enableMonitoring') is not None:
            self.enable_monitoring = m.get('enableMonitoring')
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.machines = []
        if m.get('machines') is not None:
            for k in m.get('machines'):
                temp_model = ListCollectorsResponseBodyResultExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k))
        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')
        return self


class ListCollectorsResponseBodyResult(TeaModel):
    def __init__(self, res_id=None, gmt_update_time=None, dry_run=None, owner_id=None, vpc_id=None, res_type=None,
                 res_version=None, gmt_created_time=None, status=None, name=None, configs=None, extend_configs=None,
                 collector_paths=None):
        self.res_id = res_id  # type: str
        self.gmt_update_time = gmt_update_time  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_id = owner_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.res_type = res_type  # type: str
        self.res_version = res_version  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.status = status  # type: str
        self.name = name  # type: str
        self.configs = configs  # type: list[ListCollectorsResponseBodyResultConfigs]
        self.extend_configs = extend_configs  # type: list[ListCollectorsResponseBodyResultExtendConfigs]
        self.collector_paths = collector_paths  # type: list[str]

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCollectorsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_id is not None:
            result['resId'] = self.res_id
        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.res_type is not None:
            result['resType'] = self.res_type
        if self.res_version is not None:
            result['resVersion'] = self.res_version
        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['extendConfigs'].append(k.to_map() if k else None)
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resId') is not None:
            self.res_id = m.get('resId')
        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('resType') is not None:
            self.res_type = m.get('resType')
        if m.get('resVersion') is not None:
            self.res_version = m.get('resVersion')
        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = ListCollectorsResponseBodyResultConfigs()
                self.configs.append(temp_model.from_map(k))
        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k in m.get('extendConfigs'):
                temp_model = ListCollectorsResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
        if m.get('collectorPaths') is not None:
            self.collector_paths = m.get('collectorPaths')
        return self


class ListCollectorsResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListCollectorsResponseBodyHeaders
        self.result = result  # type: list[ListCollectorsResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCollectorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListCollectorsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCollectorsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListCollectorsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCollectorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCollectorsResponse, self).to_map()
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
            temp_model = ListCollectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectedClustersResponseBodyResultResult(TeaModel):
    def __init__(self, network_type=None, instances=None):
        self.network_type = network_type  # type: str
        self.instances = instances  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectedClustersResponseBodyResultResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.instances is not None:
            result['instances'] = self.instances
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        return self


class ListConnectedClustersResponseBodyResult(TeaModel):
    def __init__(self, result=None):
        self.result = result  # type: list[ListConnectedClustersResponseBodyResultResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConnectedClustersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListConnectedClustersResponseBodyResultResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListConnectedClustersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ListConnectedClustersResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListConnectedClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListConnectedClustersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListConnectedClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListConnectedClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConnectedClustersResponse, self).to_map()
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
            temp_model = ListConnectedClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataStreamsRequest(TeaModel):
    def __init__(self, is_managed=None, name=None):
        self.is_managed = is_managed  # type: bool
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataStreamsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_managed is not None:
            result['isManaged'] = self.is_managed
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListDataStreamsResponseBodyHeaders(TeaModel):
    def __init__(self, x_managed_storage_size=None, x_managed_count=None):
        self.x_managed_storage_size = x_managed_storage_size  # type: long
        self.x_managed_count = x_managed_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataStreamsResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_managed_storage_size is not None:
            result['X-Managed-StorageSize'] = self.x_managed_storage_size
        if self.x_managed_count is not None:
            result['X-Managed-Count'] = self.x_managed_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Managed-StorageSize') is not None:
            self.x_managed_storage_size = m.get('X-Managed-StorageSize')
        if m.get('X-Managed-Count') is not None:
            self.x_managed_count = m.get('X-Managed-Count')
        return self


class ListDataStreamsResponseBodyResultIndices(TeaModel):
    def __init__(self, is_managed=None, create_time=None, size=None, managed_status=None, name=None, health=None):
        self.is_managed = is_managed  # type: bool
        self.create_time = create_time  # type: str
        self.size = size  # type: long
        self.managed_status = managed_status  # type: str
        self.name = name  # type: str
        self.health = health  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataStreamsResponseBodyResultIndices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_managed is not None:
            result['isManaged'] = self.is_managed
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.size is not None:
            result['size'] = self.size
        if self.managed_status is not None:
            result['managedStatus'] = self.managed_status
        if self.name is not None:
            result['name'] = self.name
        if self.health is not None:
            result['health'] = self.health
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('managedStatus') is not None:
            self.managed_status = m.get('managedStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('health') is not None:
            self.health = m.get('health')
        return self


class ListDataStreamsResponseBodyResult(TeaModel):
    def __init__(self, total_storage_size=None, index_template_name=None, ilm_policy_name=None, name=None,
                 health=None, managed_storage_size=None, indices=None):
        self.total_storage_size = total_storage_size  # type: long
        self.index_template_name = index_template_name  # type: str
        self.ilm_policy_name = ilm_policy_name  # type: str
        self.name = name  # type: str
        self.health = health  # type: str
        self.managed_storage_size = managed_storage_size  # type: long
        self.indices = indices  # type: list[ListDataStreamsResponseBodyResultIndices]

    def validate(self):
        if self.indices:
            for k in self.indices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataStreamsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_storage_size is not None:
            result['totalStorageSize'] = self.total_storage_size
        if self.index_template_name is not None:
            result['indexTemplateName'] = self.index_template_name
        if self.ilm_policy_name is not None:
            result['ilmPolicyName'] = self.ilm_policy_name
        if self.name is not None:
            result['name'] = self.name
        if self.health is not None:
            result['health'] = self.health
        if self.managed_storage_size is not None:
            result['managedStorageSize'] = self.managed_storage_size
        result['indices'] = []
        if self.indices is not None:
            for k in self.indices:
                result['indices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('totalStorageSize') is not None:
            self.total_storage_size = m.get('totalStorageSize')
        if m.get('indexTemplateName') is not None:
            self.index_template_name = m.get('indexTemplateName')
        if m.get('ilmPolicyName') is not None:
            self.ilm_policy_name = m.get('ilmPolicyName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('managedStorageSize') is not None:
            self.managed_storage_size = m.get('managedStorageSize')
        self.indices = []
        if m.get('indices') is not None:
            for k in m.get('indices'):
                temp_model = ListDataStreamsResponseBodyResultIndices()
                self.indices.append(temp_model.from_map(k))
        return self


class ListDataStreamsResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListDataStreamsResponseBodyHeaders
        self.result = result  # type: list[ListDataStreamsResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataStreamsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListDataStreamsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDataStreamsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataStreamsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataStreamsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataStreamsResponse, self).to_map()
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
            temp_model = ListDataStreamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataTasksResponseBodyResultSinkCluster(TeaModel):
    def __init__(self, index=None, type=None, endpoint=None, vpc_id=None, vpc_instance_port=None,
                 vpc_instance_id=None, data_source_type=None):
        self.index = index  # type: str
        self.type = type  # type: str
        self.endpoint = endpoint  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_instance_port = vpc_instance_port  # type: str
        self.vpc_instance_id = vpc_instance_id  # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataTasksResponseBodyResultSinkCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['index'] = self.index
        if self.type is not None:
            result['type'] = self.type
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_instance_port is not None:
            result['vpcInstancePort'] = self.vpc_instance_port
        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcInstancePort') is not None:
            self.vpc_instance_port = m.get('vpcInstancePort')
        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')
        return self


class ListDataTasksResponseBodyResultSourceCluster(TeaModel):
    def __init__(self, index=None, settings=None, mapping=None, type=None, routing=None, data_source_type=None):
        self.index = index  # type: str
        self.settings = settings  # type: str
        self.mapping = mapping  # type: str
        self.type = type  # type: str
        self.routing = routing  # type: str
        self.data_source_type = data_source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataTasksResponseBodyResultSourceCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['index'] = self.index
        if self.settings is not None:
            result['settings'] = self.settings
        if self.mapping is not None:
            result['mapping'] = self.mapping
        if self.type is not None:
            result['type'] = self.type
        if self.routing is not None:
            result['routing'] = self.routing
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        if m.get('mapping') is not None:
            self.mapping = m.get('mapping')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('routing') is not None:
            self.routing = m.get('routing')
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')
        return self


class ListDataTasksResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, task_id=None, status=None, sink_cluster=None, source_cluster=None):
        self.create_time = create_time  # type: str
        self.task_id = task_id  # type: str
        self.status = status  # type: str
        self.sink_cluster = sink_cluster  # type: ListDataTasksResponseBodyResultSinkCluster
        self.source_cluster = source_cluster  # type: ListDataTasksResponseBodyResultSourceCluster

    def validate(self):
        if self.sink_cluster:
            self.sink_cluster.validate()
        if self.source_cluster:
            self.source_cluster.validate()

    def to_map(self):
        _map = super(ListDataTasksResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.status is not None:
            result['status'] = self.status
        if self.sink_cluster is not None:
            result['sinkCluster'] = self.sink_cluster.to_map()
        if self.source_cluster is not None:
            result['sourceCluster'] = self.source_cluster.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sinkCluster') is not None:
            temp_model = ListDataTasksResponseBodyResultSinkCluster()
            self.sink_cluster = temp_model.from_map(m['sinkCluster'])
        if m.get('sourceCluster') is not None:
            temp_model = ListDataTasksResponseBodyResultSourceCluster()
            self.source_cluster = temp_model.from_map(m['sourceCluster'])
        return self


class ListDataTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListDataTasksResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDataTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataTasksResponse, self).to_map()
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
            temp_model = ListDataTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDefaultCollectorConfigurationsRequest(TeaModel):
    def __init__(self, res_type=None, res_version=None, source_type=None):
        self.res_type = res_type  # type: str
        self.res_version = res_version  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDefaultCollectorConfigurationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_type is not None:
            result['resType'] = self.res_type
        if self.res_version is not None:
            result['resVersion'] = self.res_version
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resType') is not None:
            self.res_type = m.get('resType')
        if m.get('resVersion') is not None:
            self.res_version = m.get('resVersion')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class ListDefaultCollectorConfigurationsResponseBodyResult(TeaModel):
    def __init__(self, content=None, file_name=None):
        self.content = content  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDefaultCollectorConfigurationsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class ListDefaultCollectorConfigurationsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListDefaultCollectorConfigurationsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDefaultCollectorConfigurationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDefaultCollectorConfigurationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDefaultCollectorConfigurationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDefaultCollectorConfigurationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDefaultCollectorConfigurationsResponse, self).to_map()
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
            temp_model = ListDefaultCollectorConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiagnoseIndicesRequest(TeaModel):
    def __init__(self, lang=None):
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDiagnoseIndicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class ListDiagnoseIndicesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDiagnoseIndicesResponseBody, self).to_map()
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


class ListDiagnoseIndicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDiagnoseIndicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDiagnoseIndicesResponse, self).to_map()
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
            temp_model = ListDiagnoseIndicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiagnoseReportRequest(TeaModel):
    def __init__(self, lang=None, start_time=None, end_time=None, page=None, size=None, detail=None, trigger=None):
        self.lang = lang  # type: str
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.page = page  # type: int
        self.size = size  # type: int
        self.detail = detail  # type: bool
        self.trigger = trigger  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDiagnoseReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['lang'] = self.lang
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.detail is not None:
            result['detail'] = self.detail
        if self.trigger is not None:
            result['trigger'] = self.trigger
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        return self


class ListDiagnoseReportResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDiagnoseReportResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail(TeaModel):
    def __init__(self, type=None, name=None, desc=None, result=None, suggest=None):
        self.type = type  # type: str
        self.name = name  # type: str
        self.desc = desc  # type: str
        self.result = result  # type: str
        self.suggest = suggest  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.result is not None:
            result['result'] = self.result
        if self.suggest is not None:
            result['suggest'] = self.suggest
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('suggest') is not None:
            self.suggest = m.get('suggest')
        return self


class ListDiagnoseReportResponseBodyResultDiagnoseItems(TeaModel):
    def __init__(self, item=None, health=None, detail=None):
        self.item = item  # type: str
        self.health = health  # type: str
        self.detail = detail  # type: ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super(ListDiagnoseReportResponseBodyResultDiagnoseItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item is not None:
            result['item'] = self.item
        if self.health is not None:
            result['health'] = self.health
        if self.detail is not None:
            result['detail'] = self.detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('item') is not None:
            self.item = m.get('item')
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('detail') is not None:
            temp_model = ListDiagnoseReportResponseBodyResultDiagnoseItemsDetail()
            self.detail = temp_model.from_map(m['detail'])
        return self


class ListDiagnoseReportResponseBodyResult(TeaModel):
    def __init__(self, trigger=None, create_time=None, report_id=None, state=None, instance_id=None, health=None,
                 diagnose_items=None):
        self.trigger = trigger  # type: str
        self.create_time = create_time  # type: long
        self.report_id = report_id  # type: str
        self.state = state  # type: str
        self.instance_id = instance_id  # type: str
        self.health = health  # type: str
        self.diagnose_items = diagnose_items  # type: list[ListDiagnoseReportResponseBodyResultDiagnoseItems]

    def validate(self):
        if self.diagnose_items:
            for k in self.diagnose_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDiagnoseReportResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger is not None:
            result['trigger'] = self.trigger
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.report_id is not None:
            result['reportId'] = self.report_id
        if self.state is not None:
            result['state'] = self.state
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.health is not None:
            result['health'] = self.health
        result['diagnoseItems'] = []
        if self.diagnose_items is not None:
            for k in self.diagnose_items:
                result['diagnoseItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('health') is not None:
            self.health = m.get('health')
        self.diagnose_items = []
        if m.get('diagnoseItems') is not None:
            for k in m.get('diagnoseItems'):
                temp_model = ListDiagnoseReportResponseBodyResultDiagnoseItems()
                self.diagnose_items.append(temp_model.from_map(k))
        return self


class ListDiagnoseReportResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListDiagnoseReportResponseBodyHeaders
        self.result = result  # type: list[ListDiagnoseReportResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDiagnoseReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListDiagnoseReportResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDiagnoseReportResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDiagnoseReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDiagnoseReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDiagnoseReportResponse, self).to_map()
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
            temp_model = ListDiagnoseReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiagnoseReportIdsRequest(TeaModel):
    def __init__(self, lang=None, start_time=None, end_time=None, page=None, size=None, trigger=None):
        self.lang = lang  # type: str
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.page = page  # type: int
        self.size = size  # type: int
        self.trigger = trigger  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDiagnoseReportIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['lang'] = self.lang
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.trigger is not None:
            result['trigger'] = self.trigger
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        return self


class ListDiagnoseReportIdsResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDiagnoseReportIdsResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListDiagnoseReportIdsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, headers=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]
        self.headers = headers  # type: ListDiagnoseReportIdsResponseBodyHeaders

    def validate(self):
        if self.headers:
            self.headers.validate()

    def to_map(self):
        _map = super(ListDiagnoseReportIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Headers') is not None:
            temp_model = ListDiagnoseReportIdsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        return self


class ListDiagnoseReportIdsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDiagnoseReportIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDiagnoseReportIdsResponse, self).to_map()
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
            temp_model = ListDiagnoseReportIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDictInformationRequest(TeaModel):
    def __init__(self, bucket_name=None, key=None, analyzer_type=None):
        self.bucket_name = bucket_name  # type: str
        self.key = key  # type: str
        self.analyzer_type = analyzer_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDictInformationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.key is not None:
            result['key'] = self.key
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')
        return self


class ListDictInformationResponseBodyResultOssObject(TeaModel):
    def __init__(self, key=None, bucket_name=None, etag=None):
        self.key = key  # type: str
        self.bucket_name = bucket_name  # type: str
        self.etag = etag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDictInformationResponseBodyResultOssObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.etag is not None:
            result['etag'] = self.etag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        return self


class ListDictInformationResponseBodyResult(TeaModel):
    def __init__(self, type=None, file_size=None, oss_object=None):
        self.type = type  # type: str
        self.file_size = file_size  # type: long
        self.oss_object = oss_object  # type: ListDictInformationResponseBodyResultOssObject

    def validate(self):
        if self.oss_object:
            self.oss_object.validate()

    def to_map(self):
        _map = super(ListDictInformationResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.oss_object is not None:
            result['ossObject'] = self.oss_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('ossObject') is not None:
            temp_model = ListDictInformationResponseBodyResultOssObject()
            self.oss_object = temp_model.from_map(m['ossObject'])
        return self


class ListDictInformationResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ListDictInformationResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListDictInformationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListDictInformationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListDictInformationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDictInformationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDictInformationResponse, self).to_map()
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
            temp_model = ListDictInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDictsRequest(TeaModel):
    def __init__(self, analyzer_type=None, name=None):
        self.analyzer_type = analyzer_type  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDictsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListDictsResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDictsResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListDictsResponseBodyResult(TeaModel):
    def __init__(self, file_size=None, download_url=None, source_type=None, type=None, name=None):
        self.file_size = file_size  # type: long
        self.download_url = download_url  # type: str
        self.source_type = source_type  # type: str
        self.type = type  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDictsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.type is not None:
            result['type'] = self.type
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListDictsResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListDictsResponseBodyHeaders
        self.result = result  # type: list[ListDictsResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDictsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListDictsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDictsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDictsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDictsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDictsResponse, self).to_map()
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
            temp_model = ListDictsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEcsInstancesRequest(TeaModel):
    def __init__(self, page=None, size=None, ecs_instance_ids=None, ecs_instance_name=None, tags=None, vpc_id=None):
        self.page = page  # type: int
        self.size = size  # type: int
        self.ecs_instance_ids = ecs_instance_ids  # type: str
        self.ecs_instance_name = ecs_instance_name  # type: str
        self.tags = tags  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEcsInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.ecs_instance_ids is not None:
            result['ecsInstanceIds'] = self.ecs_instance_ids
        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name
        if self.tags is not None:
            result['tags'] = self.tags
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('ecsInstanceIds') is not None:
            self.ecs_instance_ids = m.get('ecsInstanceIds')
        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListEcsInstancesResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEcsInstancesResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListEcsInstancesResponseBodyResultIpAddress(TeaModel):
    def __init__(self, ip_type=None, host=None):
        self.ip_type = ip_type  # type: str
        self.host = host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEcsInstancesResponseBodyResultIpAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_type is not None:
            result['ipType'] = self.ip_type
        if self.host is not None:
            result['host'] = self.host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ipType') is not None:
            self.ip_type = m.get('ipType')
        if m.get('host') is not None:
            self.host = m.get('host')
        return self


class ListEcsInstancesResponseBodyResultCollectorsConfigs(TeaModel):
    def __init__(self, content=None, file_name=None):
        self.content = content  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEcsInstancesResponseBodyResultCollectorsConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class ListEcsInstancesResponseBodyResultCollectorsExtendConfigsMachines(TeaModel):
    def __init__(self, agent_status=None, instance_id=None):
        self.agent_status = agent_status  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEcsInstancesResponseBodyResultCollectorsExtendConfigsMachines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['agentStatus'] = self.agent_status
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('agentStatus') is not None:
            self.agent_status = m.get('agentStatus')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ListEcsInstancesResponseBodyResultCollectorsExtendConfigs(TeaModel):
    def __init__(self, enable_monitoring=None, group_id=None, config_type=None, instance_type=None, protocol=None,
                 user_name=None, type=None, instance_id=None, machines=None, hosts=None):
        self.enable_monitoring = enable_monitoring  # type: bool
        self.group_id = group_id  # type: str
        self.config_type = config_type  # type: str
        self.instance_type = instance_type  # type: str
        self.protocol = protocol  # type: str
        self.user_name = user_name  # type: str
        self.type = type  # type: str
        self.instance_id = instance_id  # type: str
        self.machines = machines  # type: list[ListEcsInstancesResponseBodyResultCollectorsExtendConfigsMachines]
        self.hosts = hosts  # type: list[str]

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEcsInstancesResponseBodyResultCollectorsExtendConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_monitoring is not None:
            result['enableMonitoring'] = self.enable_monitoring
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.type is not None:
            result['type'] = self.type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['machines'] = []
        if self.machines is not None:
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
        if self.hosts is not None:
            result['hosts'] = self.hosts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enableMonitoring') is not None:
            self.enable_monitoring = m.get('enableMonitoring')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.machines = []
        if m.get('machines') is not None:
            for k in m.get('machines'):
                temp_model = ListEcsInstancesResponseBodyResultCollectorsExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k))
        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')
        return self


class ListEcsInstancesResponseBodyResultCollectors(TeaModel):
    def __init__(self, res_id=None, gmt_update_time=None, dry_run=None, owner_id=None, vpc_id=None, res_type=None,
                 res_version=None, gmt_created_time=None, status=None, name=None, configs=None, extend_configs=None,
                 collector_paths=None):
        self.res_id = res_id  # type: str
        self.gmt_update_time = gmt_update_time  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_id = owner_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.res_type = res_type  # type: str
        self.res_version = res_version  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.status = status  # type: str
        self.name = name  # type: str
        self.configs = configs  # type: list[ListEcsInstancesResponseBodyResultCollectorsConfigs]
        self.extend_configs = extend_configs  # type: list[ListEcsInstancesResponseBodyResultCollectorsExtendConfigs]
        self.collector_paths = collector_paths  # type: list[str]

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEcsInstancesResponseBodyResultCollectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_id is not None:
            result['resId'] = self.res_id
        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.res_type is not None:
            result['resType'] = self.res_type
        if self.res_version is not None:
            result['resVersion'] = self.res_version
        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['extendConfigs'].append(k.to_map() if k else None)
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resId') is not None:
            self.res_id = m.get('resId')
        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('resType') is not None:
            self.res_type = m.get('resType')
        if m.get('resVersion') is not None:
            self.res_version = m.get('resVersion')
        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = ListEcsInstancesResponseBodyResultCollectorsConfigs()
                self.configs.append(temp_model.from_map(k))
        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k in m.get('extendConfigs'):
                temp_model = ListEcsInstancesResponseBodyResultCollectorsExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
        if m.get('collectorPaths') is not None:
            self.collector_paths = m.get('collectorPaths')
        return self


class ListEcsInstancesResponseBodyResult(TeaModel):
    def __init__(self, cloud_assistant_status=None, ecs_instance_name=None, ecs_instance_id=None, tags=None,
                 os_type=None, status=None, ip_address=None, collectors=None):
        self.cloud_assistant_status = cloud_assistant_status  # type: str
        self.ecs_instance_name = ecs_instance_name  # type: str
        self.ecs_instance_id = ecs_instance_id  # type: str
        self.tags = tags  # type: str
        self.os_type = os_type  # type: str
        self.status = status  # type: str
        self.ip_address = ip_address  # type: list[ListEcsInstancesResponseBodyResultIpAddress]
        self.collectors = collectors  # type: list[ListEcsInstancesResponseBodyResultCollectors]

    def validate(self):
        if self.ip_address:
            for k in self.ip_address:
                if k:
                    k.validate()
        if self.collectors:
            for k in self.collectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEcsInstancesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_assistant_status is not None:
            result['cloudAssistantStatus'] = self.cloud_assistant_status
        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name
        if self.ecs_instance_id is not None:
            result['ecsInstanceId'] = self.ecs_instance_id
        if self.tags is not None:
            result['tags'] = self.tags
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.status is not None:
            result['status'] = self.status
        result['ipAddress'] = []
        if self.ip_address is not None:
            for k in self.ip_address:
                result['ipAddress'].append(k.to_map() if k else None)
        result['collectors'] = []
        if self.collectors is not None:
            for k in self.collectors:
                result['collectors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cloudAssistantStatus') is not None:
            self.cloud_assistant_status = m.get('cloudAssistantStatus')
        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')
        if m.get('ecsInstanceId') is not None:
            self.ecs_instance_id = m.get('ecsInstanceId')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.ip_address = []
        if m.get('ipAddress') is not None:
            for k in m.get('ipAddress'):
                temp_model = ListEcsInstancesResponseBodyResultIpAddress()
                self.ip_address.append(temp_model.from_map(k))
        self.collectors = []
        if m.get('collectors') is not None:
            for k in m.get('collectors'):
                temp_model = ListEcsInstancesResponseBodyResultCollectors()
                self.collectors.append(temp_model.from_map(k))
        return self


class ListEcsInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListEcsInstancesResponseBodyHeaders
        self.result = result  # type: list[ListEcsInstancesResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEcsInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListEcsInstancesResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListEcsInstancesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListEcsInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEcsInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEcsInstancesResponse, self).to_map()
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
            temp_model = ListEcsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExtendfilesResponseBodyResult(TeaModel):
    def __init__(self, file_path=None, file_size=None, name=None, source_type=None):
        self.file_path = file_path  # type: str
        self.file_size = file_size  # type: long
        self.name = name  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExtendfilesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class ListExtendfilesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListExtendfilesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExtendfilesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListExtendfilesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListExtendfilesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListExtendfilesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExtendfilesResponse, self).to_map()
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
            temp_model = ListExtendfilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListILMPoliciesRequest(TeaModel):
    def __init__(self, policy_name=None):
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListILMPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        return self


class ListILMPoliciesResponseBodyResult(TeaModel):
    def __init__(self, name=None, phases=None):
        self.name = name  # type: str
        self.phases = phases  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListILMPoliciesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.phases is not None:
            result['phases'] = self.phases
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phases') is not None:
            self.phases = m.get('phases')
        return self


class ListILMPoliciesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListILMPoliciesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListILMPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListILMPoliciesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListILMPoliciesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListILMPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListILMPoliciesResponse, self).to_map()
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
            temp_model = ListILMPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexTemplatesRequest(TeaModel):
    def __init__(self, index_template=None):
        self.index_template = index_template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIndexTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_template is not None:
            result['indexTemplate'] = self.index_template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')
        return self


class ListIndexTemplatesResponseBodyResultTemplate(TeaModel):
    def __init__(self, settings=None, mappings=None, aliases=None):
        self.settings = settings  # type: str
        self.mappings = mappings  # type: str
        self.aliases = aliases  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIndexTemplatesResponseBodyResultTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.settings is not None:
            result['settings'] = self.settings
        if self.mappings is not None:
            result['mappings'] = self.mappings
        if self.aliases is not None:
            result['aliases'] = self.aliases
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        if m.get('mappings') is not None:
            self.mappings = m.get('mappings')
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')
        return self


class ListIndexTemplatesResponseBodyResult(TeaModel):
    def __init__(self, data_stream=None, index_template=None, ilm_policy=None, priority=None, index_patterns=None,
                 template=None):
        self.data_stream = data_stream  # type: bool
        self.index_template = index_template  # type: str
        self.ilm_policy = ilm_policy  # type: str
        self.priority = priority  # type: int
        self.index_patterns = index_patterns  # type: list[str]
        self.template = template  # type: ListIndexTemplatesResponseBodyResultTemplate

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(ListIndexTemplatesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_stream is not None:
            result['dataStream'] = self.data_stream
        if self.index_template is not None:
            result['indexTemplate'] = self.index_template
        if self.ilm_policy is not None:
            result['ilmPolicy'] = self.ilm_policy
        if self.priority is not None:
            result['priority'] = self.priority
        if self.index_patterns is not None:
            result['indexPatterns'] = self.index_patterns
        if self.template is not None:
            result['template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataStream') is not None:
            self.data_stream = m.get('dataStream')
        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')
        if m.get('ilmPolicy') is not None:
            self.ilm_policy = m.get('ilmPolicy')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('indexPatterns') is not None:
            self.index_patterns = m.get('indexPatterns')
        if m.get('template') is not None:
            temp_model = ListIndexTemplatesResponseBodyResultTemplate()
            self.template = temp_model.from_map(m['template'])
        return self


class ListIndexTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListIndexTemplatesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIndexTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListIndexTemplatesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListIndexTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIndexTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIndexTemplatesResponse, self).to_map()
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
            temp_model = ListIndexTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(self, page=None, size=None, description=None, instance_id=None, es_version=None,
                 resource_group_id=None, tags=None, vpc_id=None, zone_id=None, payment_type=None, instance_category=None):
        self.page = page  # type: int
        self.size = size  # type: int
        self.description = description  # type: str
        self.instance_id = instance_id  # type: str
        self.es_version = es_version  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tags = tags  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str
        self.payment_type = payment_type  # type: str
        self.instance_category = instance_category  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['tags'] = self.tags
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['zoneId'] = self.zone_id
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.instance_category is not None:
            result['instanceCategory'] = self.instance_category
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('instanceCategory') is not None:
            self.instance_category = m.get('instanceCategory')
        return self


class ListInstanceResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListInstanceResponseBodyResultTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyResultTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListInstanceResponseBodyResultClientNodeConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyResultClientNodeConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class ListInstanceResponseBodyResultElasticDataNodeConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_encryption=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_encryption = disk_encryption  # type: bool
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyResultElasticDataNodeConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class ListInstanceResponseBodyResultKibanaConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyResultKibanaConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class ListInstanceResponseBodyResultMasterConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyResultMasterConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class ListInstanceResponseBodyResultNetworkConfig(TeaModel):
    def __init__(self, vpc_id=None, vs_area=None, type=None, vswitch_id=None):
        self.vpc_id = vpc_id  # type: str
        self.vs_area = vs_area  # type: str
        self.type = type  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyResultNetworkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.type is not None:
            result['type'] = self.type
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class ListInstanceResponseBodyResultNodeSpec(TeaModel):
    def __init__(self, spec=None, disk=None, disk_encryption=None, disk_type=None):
        self.spec = spec  # type: str
        self.disk = disk  # type: int
        self.disk_encryption = disk_encryption  # type: bool
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyResultNodeSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class ListInstanceResponseBodyResult(TeaModel):
    def __init__(self, advanced_dedicate_master=None, node_amount=None, created_at=None, status=None,
                 dedicate_master=None, service_vpc=None, payment_type=None, resource_group_id=None, postpaid_service_status=None,
                 description=None, es_version=None, is_new_deployment=None, updated_at=None, instance_id=None, tags=None,
                 extend_configs=None, client_node_configuration=None, elastic_data_node_configuration=None,
                 kibana_configuration=None, master_configuration=None, network_config=None, node_spec=None):
        self.advanced_dedicate_master = advanced_dedicate_master  # type: bool
        self.node_amount = node_amount  # type: int
        self.created_at = created_at  # type: str
        self.status = status  # type: str
        self.dedicate_master = dedicate_master  # type: bool
        self.service_vpc = service_vpc  # type: bool
        self.payment_type = payment_type  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.postpaid_service_status = postpaid_service_status  # type: str
        self.description = description  # type: str
        self.es_version = es_version  # type: str
        self.is_new_deployment = is_new_deployment  # type: str
        self.updated_at = updated_at  # type: str
        self.instance_id = instance_id  # type: str
        self.tags = tags  # type: list[ListInstanceResponseBodyResultTags]
        self.extend_configs = extend_configs  # type: list[dict[str, any]]
        self.client_node_configuration = client_node_configuration  # type: ListInstanceResponseBodyResultClientNodeConfiguration
        self.elastic_data_node_configuration = elastic_data_node_configuration  # type: ListInstanceResponseBodyResultElasticDataNodeConfiguration
        self.kibana_configuration = kibana_configuration  # type: ListInstanceResponseBodyResultKibanaConfiguration
        self.master_configuration = master_configuration  # type: ListInstanceResponseBodyResultMasterConfiguration
        self.network_config = network_config  # type: ListInstanceResponseBodyResultNetworkConfig
        self.node_spec = node_spec  # type: ListInstanceResponseBodyResultNodeSpec

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.client_node_configuration:
            self.client_node_configuration.validate()
        if self.elastic_data_node_configuration:
            self.elastic_data_node_configuration.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_dedicate_master is not None:
            result['advancedDedicateMaster'] = self.advanced_dedicate_master
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.status is not None:
            result['status'] = self.status
        if self.dedicate_master is not None:
            result['dedicateMaster'] = self.dedicate_master
        if self.service_vpc is not None:
            result['serviceVpc'] = self.service_vpc
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.postpaid_service_status is not None:
            result['postpaidServiceStatus'] = self.postpaid_service_status
        if self.description is not None:
            result['description'] = self.description
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.is_new_deployment is not None:
            result['isNewDeployment'] = self.is_new_deployment
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.extend_configs is not None:
            result['extendConfigs'] = self.extend_configs
        if self.client_node_configuration is not None:
            result['clientNodeConfiguration'] = self.client_node_configuration.to_map()
        if self.elastic_data_node_configuration is not None:
            result['elasticDataNodeConfiguration'] = self.elastic_data_node_configuration.to_map()
        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()
        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('advancedDedicateMaster') is not None:
            self.advanced_dedicate_master = m.get('advancedDedicateMaster')
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('dedicateMaster') is not None:
            self.dedicate_master = m.get('dedicateMaster')
        if m.get('serviceVpc') is not None:
            self.service_vpc = m.get('serviceVpc')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('postpaidServiceStatus') is not None:
            self.postpaid_service_status = m.get('postpaidServiceStatus')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('isNewDeployment') is not None:
            self.is_new_deployment = m.get('isNewDeployment')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListInstanceResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('extendConfigs') is not None:
            self.extend_configs = m.get('extendConfigs')
        if m.get('clientNodeConfiguration') is not None:
            temp_model = ListInstanceResponseBodyResultClientNodeConfiguration()
            self.client_node_configuration = temp_model.from_map(m['clientNodeConfiguration'])
        if m.get('elasticDataNodeConfiguration') is not None:
            temp_model = ListInstanceResponseBodyResultElasticDataNodeConfiguration()
            self.elastic_data_node_configuration = temp_model.from_map(m['elasticDataNodeConfiguration'])
        if m.get('kibanaConfiguration') is not None:
            temp_model = ListInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m['kibanaConfiguration'])
        if m.get('masterConfiguration') is not None:
            temp_model = ListInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m['masterConfiguration'])
        if m.get('networkConfig') is not None:
            temp_model = ListInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('nodeSpec') is not None:
            temp_model = ListInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListInstanceResponseBodyHeaders
        self.result = result  # type: list[ListInstanceResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListInstanceResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListInstanceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceResponse, self).to_map()
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceIndicesRequest(TeaModel):
    def __init__(self, all=None, name=None, is_managed=None, is_openstore=None, page=None, size=None):
        self.all = all  # type: bool
        self.name = name  # type: str
        self.is_managed = is_managed  # type: bool
        self.is_openstore = is_openstore  # type: bool
        self.page = page  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceIndicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.name is not None:
            result['name'] = self.name
        if self.is_managed is not None:
            result['isManaged'] = self.is_managed
        if self.is_openstore is not None:
            result['isOpenstore'] = self.is_openstore
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')
        if m.get('isOpenstore') is not None:
            self.is_openstore = m.get('isOpenstore')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListInstanceIndicesResponseBodyHeaders(TeaModel):
    def __init__(self, x_managed_storage_size=None, x_managed_count=None, x_ossstorage_size=None, x_osscount=None):
        self.x_managed_storage_size = x_managed_storage_size  # type: long
        self.x_managed_count = x_managed_count  # type: int
        self.x_ossstorage_size = x_ossstorage_size  # type: long
        self.x_osscount = x_osscount  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceIndicesResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_managed_storage_size is not None:
            result['X-Managed-StorageSize'] = self.x_managed_storage_size
        if self.x_managed_count is not None:
            result['X-Managed-Count'] = self.x_managed_count
        if self.x_ossstorage_size is not None:
            result['X-OSS-StorageSize'] = self.x_ossstorage_size
        if self.x_osscount is not None:
            result['X-OSS-Count'] = self.x_osscount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Managed-StorageSize') is not None:
            self.x_managed_storage_size = m.get('X-Managed-StorageSize')
        if m.get('X-Managed-Count') is not None:
            self.x_managed_count = m.get('X-Managed-Count')
        if m.get('X-OSS-StorageSize') is not None:
            self.x_ossstorage_size = m.get('X-OSS-StorageSize')
        if m.get('X-OSS-Count') is not None:
            self.x_osscount = m.get('X-OSS-Count')
        return self


class ListInstanceIndicesResponseBodyResult(TeaModel):
    def __init__(self, is_managed=None, create_time=None, size=None, managed_status=None, name=None, health=None,
                 phase=None, ilm_explain=None):
        self.is_managed = is_managed  # type: str
        self.create_time = create_time  # type: str
        self.size = size  # type: long
        self.managed_status = managed_status  # type: str
        self.name = name  # type: str
        self.health = health  # type: str
        self.phase = phase  # type: str
        self.ilm_explain = ilm_explain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceIndicesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_managed is not None:
            result['isManaged'] = self.is_managed
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.size is not None:
            result['size'] = self.size
        if self.managed_status is not None:
            result['managedStatus'] = self.managed_status
        if self.name is not None:
            result['name'] = self.name
        if self.health is not None:
            result['health'] = self.health
        if self.phase is not None:
            result['phase'] = self.phase
        if self.ilm_explain is not None:
            result['ilmExplain'] = self.ilm_explain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('managedStatus') is not None:
            self.managed_status = m.get('managedStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('health') is not None:
            self.health = m.get('health')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('ilmExplain') is not None:
            self.ilm_explain = m.get('ilmExplain')
        return self


class ListInstanceIndicesResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListInstanceIndicesResponseBodyHeaders
        self.result = result  # type: list[ListInstanceIndicesResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceIndicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListInstanceIndicesResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListInstanceIndicesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceIndicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstanceIndicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceIndicesResponse, self).to_map()
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
            temp_model = ListInstanceIndicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKibanaPluginsRequest(TeaModel):
    def __init__(self, page=None, size=None):
        self.page = page  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListKibanaPluginsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListKibanaPluginsResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListKibanaPluginsResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListKibanaPluginsResponseBodyResult(TeaModel):
    def __init__(self, description=None, specification_url=None, state=None, source=None, name=None):
        self.description = description  # type: str
        self.specification_url = specification_url  # type: str
        self.state = state  # type: str
        self.source = source  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListKibanaPluginsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.specification_url is not None:
            result['specificationUrl'] = self.specification_url
        if self.state is not None:
            result['state'] = self.state
        if self.source is not None:
            result['source'] = self.source
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('specificationUrl') is not None:
            self.specification_url = m.get('specificationUrl')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListKibanaPluginsResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListKibanaPluginsResponseBodyHeaders
        self.result = result  # type: list[ListKibanaPluginsResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListKibanaPluginsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListKibanaPluginsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListKibanaPluginsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListKibanaPluginsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListKibanaPluginsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListKibanaPluginsResponse, self).to_map()
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
            temp_model = ListKibanaPluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogstashRequest(TeaModel):
    def __init__(self, page=None, size=None, description=None, instance_id=None, version=None, owner_id=None,
                 resource_group_id=None):
        self.page = page  # type: int
        self.size = size  # type: int
        self.description = description  # type: str
        self.instance_id = instance_id  # type: str
        self.version = version  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogstashRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.version is not None:
            result['version'] = self.version
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self


class ListLogstashResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogstashResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListLogstashResponseBodyResultTags(TeaModel):
    def __init__(self, tag_value=None, tag_key=None):
        self.tag_value = tag_value  # type: str
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogstashResponseBodyResultTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListLogstashResponseBodyResultNodeSpec(TeaModel):
    def __init__(self, spec=None, disk=None, disk_encryption=None, disk_type=None):
        self.spec = spec  # type: str
        self.disk = disk  # type: int
        self.disk_encryption = disk_encryption  # type: bool
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogstashResponseBodyResultNodeSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class ListLogstashResponseBodyResultNetworkConfig(TeaModel):
    def __init__(self, vpc_id=None, vs_area=None, type=None, vswitch_id=None):
        self.vpc_id = vpc_id  # type: str
        self.vs_area = vs_area  # type: str
        self.type = type  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogstashResponseBodyResultNetworkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.type is not None:
            result['type'] = self.type
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class ListLogstashResponseBodyResult(TeaModel):
    def __init__(self, payment_type=None, node_amount=None, description=None, created_at=None, status=None,
                 updated_at=None, instance_id=None, version=None, tags=None, node_spec=None, network_config=None):
        self.payment_type = payment_type  # type: str
        self.node_amount = node_amount  # type: int
        self.description = description  # type: str
        self.created_at = created_at  # type: str
        self.status = status  # type: str
        self.updated_at = updated_at  # type: str
        self.instance_id = instance_id  # type: str
        self.version = version  # type: str
        self.tags = tags  # type: list[ListLogstashResponseBodyResultTags]
        self.node_spec = node_spec  # type: ListLogstashResponseBodyResultNodeSpec
        self.network_config = network_config  # type: ListLogstashResponseBodyResultNetworkConfig

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.network_config:
            self.network_config.validate()

    def to_map(self):
        _map = super(ListLogstashResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.description is not None:
            result['description'] = self.description
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.version is not None:
            result['version'] = self.version
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('version') is not None:
            self.version = m.get('version')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListLogstashResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('nodeSpec') is not None:
            temp_model = ListLogstashResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('networkConfig') is not None:
            temp_model = ListLogstashResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        return self


class ListLogstashResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListLogstashResponseBodyHeaders
        self.result = result  # type: list[ListLogstashResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLogstashResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListLogstashResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListLogstashResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListLogstashResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListLogstashResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLogstashResponse, self).to_map()
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
            temp_model = ListLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogstashLogRequest(TeaModel):
    def __init__(self, type=None, query=None, begin_time=None, end_time=None, page=None, size=None):
        self.type = type  # type: str
        self.query = query  # type: str
        self.begin_time = begin_time  # type: long
        self.end_time = end_time  # type: long
        self.page = page  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogstashLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.query is not None:
            result['query'] = self.query
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListLogstashLogResponseBodyResult(TeaModel):
    def __init__(self, level=None, content=None, timestamp=None, instance_id=None, host=None):
        self.level = level  # type: str
        self.content = content  # type: str
        self.timestamp = timestamp  # type: long
        self.instance_id = instance_id  # type: str
        self.host = host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogstashLogResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['level'] = self.level
        if self.content is not None:
            result['content'] = self.content
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.host is not None:
            result['host'] = self.host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('host') is not None:
            self.host = m.get('host')
        return self


class ListLogstashLogResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListLogstashLogResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLogstashLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListLogstashLogResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListLogstashLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListLogstashLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLogstashLogResponse, self).to_map()
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
            temp_model = ListLogstashLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogstashPluginsRequest(TeaModel):
    def __init__(self, name=None, page=None, size=None, source=None):
        self.name = name  # type: str
        self.page = page  # type: int
        self.size = size  # type: int
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogstashPluginsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class ListLogstashPluginsResponseBodyResult(TeaModel):
    def __init__(self, description=None, specification_url=None, state=None, source=None, name=None):
        self.description = description  # type: str
        self.specification_url = specification_url  # type: str
        self.state = state  # type: str
        self.source = source  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogstashPluginsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.specification_url is not None:
            result['specificationUrl'] = self.specification_url
        if self.state is not None:
            result['state'] = self.state
        if self.source is not None:
            result['source'] = self.source
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('specificationUrl') is not None:
            self.specification_url = m.get('specificationUrl')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListLogstashPluginsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListLogstashPluginsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLogstashPluginsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListLogstashPluginsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListLogstashPluginsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListLogstashPluginsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLogstashPluginsResponse, self).to_map()
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
            temp_model = ListLogstashPluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(self, page=None, size=None, ecs_instance_ids=None, ecs_instance_name=None, tags=None):
        self.page = page  # type: int
        self.size = size  # type: int
        self.ecs_instance_ids = ecs_instance_ids  # type: str
        self.ecs_instance_name = ecs_instance_name  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.ecs_instance_ids is not None:
            result['ecsInstanceIds'] = self.ecs_instance_ids
        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('ecsInstanceIds') is not None:
            self.ecs_instance_ids = m.get('ecsInstanceIds')
        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class ListNodesResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListNodesResponseBodyResultTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesResponseBodyResultTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListNodesResponseBodyResultIpAddress(TeaModel):
    def __init__(self, ip_type=None, host=None):
        self.ip_type = ip_type  # type: str
        self.host = host  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesResponseBodyResultIpAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_type is not None:
            result['ipType'] = self.ip_type
        if self.host is not None:
            result['host'] = self.host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ipType') is not None:
            self.ip_type = m.get('ipType')
        if m.get('host') is not None:
            self.host = m.get('host')
        return self


class ListNodesResponseBodyResult(TeaModel):
    def __init__(self, cloud_assistant_status=None, ecs_instance_name=None, ecs_instance_id=None, os_type=None,
                 status=None, agent_status=None, tags=None, ip_address=None):
        self.cloud_assistant_status = cloud_assistant_status  # type: str
        self.ecs_instance_name = ecs_instance_name  # type: str
        self.ecs_instance_id = ecs_instance_id  # type: str
        self.os_type = os_type  # type: str
        self.status = status  # type: str
        self.agent_status = agent_status  # type: str
        self.tags = tags  # type: list[ListNodesResponseBodyResultTags]
        self.ip_address = ip_address  # type: list[ListNodesResponseBodyResultIpAddress]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ip_address:
            for k in self.ip_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_assistant_status is not None:
            result['cloudAssistantStatus'] = self.cloud_assistant_status
        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name
        if self.ecs_instance_id is not None:
            result['ecsInstanceId'] = self.ecs_instance_id
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.status is not None:
            result['status'] = self.status
        if self.agent_status is not None:
            result['agentStatus'] = self.agent_status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['ipAddress'] = []
        if self.ip_address is not None:
            for k in self.ip_address:
                result['ipAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cloudAssistantStatus') is not None:
            self.cloud_assistant_status = m.get('cloudAssistantStatus')
        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')
        if m.get('ecsInstanceId') is not None:
            self.ecs_instance_id = m.get('ecsInstanceId')
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('agentStatus') is not None:
            self.agent_status = m.get('agentStatus')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListNodesResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        self.ip_address = []
        if m.get('ipAddress') is not None:
            for k in m.get('ipAddress'):
                temp_model = ListNodesResponseBodyResultIpAddress()
                self.ip_address.append(temp_model.from_map(k))
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListNodesResponseBodyHeaders
        self.result = result  # type: list[ListNodesResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListNodesResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListNodesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodesResponse, self).to_map()
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
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineRequest(TeaModel):
    def __init__(self, pipeline_id=None, page=None, size=None):
        self.pipeline_id = pipeline_id  # type: str
        self.page = page  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListPipelineResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListPipelineResponseBodyResult(TeaModel):
    def __init__(self, pipeline_id=None, gmt_update_time=None, gmt_created_time=None, pipeline_status=None):
        self.pipeline_id = pipeline_id  # type: str
        self.gmt_update_time = gmt_update_time  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.pipeline_status = pipeline_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time
        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time
        if self.pipeline_status is not None:
            result['pipelineStatus'] = self.pipeline_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')
        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')
        if m.get('pipelineStatus') is not None:
            self.pipeline_status = m.get('pipelineStatus')
        return self


class ListPipelineResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListPipelineResponseBodyHeaders
        self.result = result  # type: list[ListPipelineResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListPipelineResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListPipelineResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListPipelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPipelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPipelineResponse, self).to_map()
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
            temp_model = ListPipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineIdsResponseBodyResult(TeaModel):
    def __init__(self, pipeline_id=None, available=None, code=None, message=None):
        self.pipeline_id = pipeline_id  # type: str
        self.available = available  # type: bool
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineIdsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.available is not None:
            result['available'] = self.available
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListPipelineIdsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListPipelineIdsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPipelineIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListPipelineIdsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListPipelineIdsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPipelineIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPipelineIdsResponse, self).to_map()
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
            temp_model = ListPipelineIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPluginsRequest(TeaModel):
    def __init__(self, name=None, page=None, size=None, source=None):
        self.name = name  # type: str
        self.page = page  # type: str
        self.size = size  # type: int
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPluginsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class ListPluginsResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPluginsResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListPluginsResponseBodyResult(TeaModel):
    def __init__(self, description=None, specification_url=None, state=None, source=None, name=None):
        self.description = description  # type: str
        self.specification_url = specification_url  # type: str
        self.state = state  # type: str
        self.source = source  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPluginsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.specification_url is not None:
            result['specificationUrl'] = self.specification_url
        if self.state is not None:
            result['state'] = self.state
        if self.source is not None:
            result['source'] = self.source
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('specificationUrl') is not None:
            self.specification_url = m.get('specificationUrl')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListPluginsResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListPluginsResponseBodyHeaders
        self.result = result  # type: list[ListPluginsResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPluginsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListPluginsResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListPluginsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListPluginsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPluginsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPluginsResponse, self).to_map()
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
            temp_model = ListPluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSearchLogRequest(TeaModel):
    def __init__(self, type=None, query=None, begin_time=None, end_time=None, page=None, size=None):
        self.type = type  # type: str
        self.query = query  # type: str
        self.begin_time = begin_time  # type: long
        self.end_time = end_time  # type: long
        self.page = page  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSearchLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.query is not None:
            result['query'] = self.query
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListSearchLogResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSearchLogResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListSearchLogResponseBodyResult(TeaModel):
    def __init__(self, level=None, host=None, content=None, timestamp=None, content_collection=None,
                 instance_id=None):
        self.level = level  # type: str
        self.host = host  # type: str
        self.content = content  # type: str
        self.timestamp = timestamp  # type: long
        self.content_collection = content_collection  # type: dict[str, any]
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSearchLogResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['level'] = self.level
        if self.host is not None:
            result['host'] = self.host
        if self.content is not None:
            result['content'] = self.content
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.content_collection is not None:
            result['contentCollection'] = self.content_collection
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('contentCollection') is not None:
            self.content_collection = m.get('contentCollection')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ListSearchLogResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, result=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListSearchLogResponseBodyHeaders
        self.result = result  # type: list[ListSearchLogResponseBodyResult]

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSearchLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListSearchLogResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListSearchLogResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSearchLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSearchLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSearchLogResponse, self).to_map()
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
            temp_model = ListSearchLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShardRecoveriesRequest(TeaModel):
    def __init__(self, active_only=None):
        self.active_only = active_only  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListShardRecoveriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_only is not None:
            result['activeOnly'] = self.active_only
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('activeOnly') is not None:
            self.active_only = m.get('activeOnly')
        return self


class ListShardRecoveriesResponseBodyResult(TeaModel):
    def __init__(self, index=None, source_host=None, source_node=None, files_total=None, bytes_percent=None,
                 translog_ops=None, translog_ops_percent=None, bytes_total=None, target_host=None, target_node=None,
                 files_percent=None, stage=None):
        self.index = index  # type: str
        self.source_host = source_host  # type: str
        self.source_node = source_node  # type: str
        self.files_total = files_total  # type: long
        self.bytes_percent = bytes_percent  # type: str
        self.translog_ops = translog_ops  # type: long
        self.translog_ops_percent = translog_ops_percent  # type: str
        self.bytes_total = bytes_total  # type: long
        self.target_host = target_host  # type: str
        self.target_node = target_node  # type: str
        self.files_percent = files_percent  # type: str
        self.stage = stage  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListShardRecoveriesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['index'] = self.index
        if self.source_host is not None:
            result['sourceHost'] = self.source_host
        if self.source_node is not None:
            result['sourceNode'] = self.source_node
        if self.files_total is not None:
            result['filesTotal'] = self.files_total
        if self.bytes_percent is not None:
            result['bytesPercent'] = self.bytes_percent
        if self.translog_ops is not None:
            result['translogOps'] = self.translog_ops
        if self.translog_ops_percent is not None:
            result['translogOpsPercent'] = self.translog_ops_percent
        if self.bytes_total is not None:
            result['bytesTotal'] = self.bytes_total
        if self.target_host is not None:
            result['targetHost'] = self.target_host
        if self.target_node is not None:
            result['targetNode'] = self.target_node
        if self.files_percent is not None:
            result['filesPercent'] = self.files_percent
        if self.stage is not None:
            result['stage'] = self.stage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('sourceHost') is not None:
            self.source_host = m.get('sourceHost')
        if m.get('sourceNode') is not None:
            self.source_node = m.get('sourceNode')
        if m.get('filesTotal') is not None:
            self.files_total = m.get('filesTotal')
        if m.get('bytesPercent') is not None:
            self.bytes_percent = m.get('bytesPercent')
        if m.get('translogOps') is not None:
            self.translog_ops = m.get('translogOps')
        if m.get('translogOpsPercent') is not None:
            self.translog_ops_percent = m.get('translogOpsPercent')
        if m.get('bytesTotal') is not None:
            self.bytes_total = m.get('bytesTotal')
        if m.get('targetHost') is not None:
            self.target_host = m.get('targetHost')
        if m.get('targetNode') is not None:
            self.target_node = m.get('targetNode')
        if m.get('filesPercent') is not None:
            self.files_percent = m.get('filesPercent')
        if m.get('stage') is not None:
            self.stage = m.get('stage')
        return self


class ListShardRecoveriesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListShardRecoveriesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListShardRecoveriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListShardRecoveriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListShardRecoveriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListShardRecoveriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListShardRecoveriesResponse, self).to_map()
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
            temp_model = ListShardRecoveriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotReposByInstanceIdResponseBodyResult(TeaModel):
    def __init__(self, snap_warehouse=None, repo_path=None, status=None, instance_id=None):
        self.snap_warehouse = snap_warehouse  # type: str
        self.repo_path = repo_path  # type: str
        self.status = status  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotReposByInstanceIdResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snap_warehouse is not None:
            result['snapWarehouse'] = self.snap_warehouse
        if self.repo_path is not None:
            result['repoPath'] = self.repo_path
        if self.status is not None:
            result['status'] = self.status
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('snapWarehouse') is not None:
            self.snap_warehouse = m.get('snapWarehouse')
        if m.get('repoPath') is not None:
            self.repo_path = m.get('repoPath')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class ListSnapshotReposByInstanceIdResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListSnapshotReposByInstanceIdResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSnapshotReposByInstanceIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListSnapshotReposByInstanceIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSnapshotReposByInstanceIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSnapshotReposByInstanceIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSnapshotReposByInstanceIdResponse, self).to_map()
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
            temp_model = ListSnapshotReposByInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, page=None, size=None, resource_type=None, next_token=None, resource_ids=None, tags=None):
        self.page = page  # type: int
        self.size = size  # type: int
        self.resource_type = resource_type  # type: str
        self.next_token = next_token  # type: str
        self.resource_ids = resource_ids  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListTagResourcesResponseBodyHeaders(TeaModel):
    def __init__(self, x_total_count=None):
        self.x_total_count = x_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, tag_value=None, resource_type=None, resource_id=None, tag_key=None):
        self.tag_value = tag_value  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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
    def __init__(self, page_size=None, request_id=None, headers=None, tag_resources=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.headers = headers  # type: ListTagResourcesResponseBodyHeaders
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Headers') is not None:
            temp_model = ListTagResourcesResponseBodyHeaders()
            self.headers = temp_model.from_map(m['Headers'])
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
    def __init__(self, page_size=None, resource_type=None):
        self.page_size = page_size  # type: int
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListTagsResponseBodyResult(TeaModel):
    def __init__(self, tag_value=None, tag_key=None):
        self.tag_value = tag_value  # type: str
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListTagsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListTagsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
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


class ListVpcEndpointsRequest(TeaModel):
    def __init__(self, size=None, page=None):
        self.size = size  # type: int
        self.page = page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['size'] = self.size
        if self.page is not None:
            result['page'] = self.page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('page') is not None:
            self.page = m.get('page')
        return self


class ListVpcEndpointsResponseBodyResult(TeaModel):
    def __init__(self, endpoint_business_status=None, service_id=None, endpoint_name=None, endpoint_id=None,
                 service_name=None, create_time=None, connection_status=None, endpoint_domain=None, endpoint_status=None):
        self.endpoint_business_status = endpoint_business_status  # type: str
        self.service_id = service_id  # type: str
        self.endpoint_name = endpoint_name  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.service_name = service_name  # type: str
        self.create_time = create_time  # type: str
        self.connection_status = connection_status  # type: str
        self.endpoint_domain = endpoint_domain  # type: str
        self.endpoint_status = endpoint_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_business_status is not None:
            result['endpointBusinessStatus'] = self.endpoint_business_status
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name
        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.connection_status is not None:
            result['connectionStatus'] = self.connection_status
        if self.endpoint_domain is not None:
            result['endpointDomain'] = self.endpoint_domain
        if self.endpoint_status is not None:
            result['endpointStatus'] = self.endpoint_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endpointBusinessStatus') is not None:
            self.endpoint_business_status = m.get('endpointBusinessStatus')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('connectionStatus') is not None:
            self.connection_status = m.get('connectionStatus')
        if m.get('endpointDomain') is not None:
            self.endpoint_domain = m.get('endpointDomain')
        if m.get('endpointStatus') is not None:
            self.endpoint_status = m.get('endpointStatus')
        return self


class ListVpcEndpointsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListVpcEndpointsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListVpcEndpointsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListVpcEndpointsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListVpcEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcEndpointsResponse, self).to_map()
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
            temp_model = ListVpcEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateToOtherZoneRequest(TeaModel):
    def __init__(self, dry_run=None):
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateToOtherZoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class MigrateToOtherZoneResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateToOtherZoneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MigrateToOtherZoneResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MigrateToOtherZoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MigrateToOtherZoneResponse, self).to_map()
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
            temp_model = MigrateToOtherZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeployMachineRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeployMachineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyDeployMachineResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeployMachineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDeployMachineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDeployMachineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDeployMachineResponse, self).to_map()
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
            temp_model = ModifyDeployMachineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElastictaskResponseBodyResultElasticExpansionTask(TeaModel):
    def __init__(self, trigger_type=None, replica_count=None, elastic_node_count=None, cron_expression=None,
                 target_indices=None):
        self.trigger_type = trigger_type  # type: str
        self.replica_count = replica_count  # type: int
        self.elastic_node_count = elastic_node_count  # type: int
        self.cron_expression = cron_expression  # type: str
        self.target_indices = target_indices  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyElastictaskResponseBodyResultElasticExpansionTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count
        if self.elastic_node_count is not None:
            result['elasticNodeCount'] = self.elastic_node_count
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.target_indices is not None:
            result['targetIndices'] = self.target_indices
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')
        if m.get('elasticNodeCount') is not None:
            self.elastic_node_count = m.get('elasticNodeCount')
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('targetIndices') is not None:
            self.target_indices = m.get('targetIndices')
        return self


class ModifyElastictaskResponseBodyResultElasticShrinkTask(TeaModel):
    def __init__(self, trigger_type=None, replica_count=None, elastic_node_count=None, cron_expression=None,
                 target_indices=None):
        self.trigger_type = trigger_type  # type: str
        self.replica_count = replica_count  # type: int
        self.elastic_node_count = elastic_node_count  # type: int
        self.cron_expression = cron_expression  # type: str
        self.target_indices = target_indices  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyElastictaskResponseBodyResultElasticShrinkTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count
        if self.elastic_node_count is not None:
            result['elasticNodeCount'] = self.elastic_node_count
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.target_indices is not None:
            result['targetIndices'] = self.target_indices
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')
        if m.get('elasticNodeCount') is not None:
            self.elastic_node_count = m.get('elasticNodeCount')
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('targetIndices') is not None:
            self.target_indices = m.get('targetIndices')
        return self


class ModifyElastictaskResponseBodyResult(TeaModel):
    def __init__(self, elastic_expansion_task=None, elastic_shrink_task=None):
        self.elastic_expansion_task = elastic_expansion_task  # type: ModifyElastictaskResponseBodyResultElasticExpansionTask
        self.elastic_shrink_task = elastic_shrink_task  # type: ModifyElastictaskResponseBodyResultElasticShrinkTask

    def validate(self):
        if self.elastic_expansion_task:
            self.elastic_expansion_task.validate()
        if self.elastic_shrink_task:
            self.elastic_shrink_task.validate()

    def to_map(self):
        _map = super(ModifyElastictaskResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_expansion_task is not None:
            result['elasticExpansionTask'] = self.elastic_expansion_task.to_map()
        if self.elastic_shrink_task is not None:
            result['elasticShrinkTask'] = self.elastic_shrink_task.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('elasticExpansionTask') is not None:
            temp_model = ModifyElastictaskResponseBodyResultElasticExpansionTask()
            self.elastic_expansion_task = temp_model.from_map(m['elasticExpansionTask'])
        if m.get('elasticShrinkTask') is not None:
            temp_model = ModifyElastictaskResponseBodyResultElasticShrinkTask()
            self.elastic_shrink_task = temp_model.from_map(m['elasticShrinkTask'])
        return self


class ModifyElastictaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ModifyElastictaskResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ModifyElastictaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ModifyElastictaskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ModifyElastictaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyElastictaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyElastictaskResponse, self).to_map()
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
            temp_model = ModifyElastictaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMaintainTimeRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyInstanceMaintainTimeResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
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


class ModifyWhiteIpsRequestWhiteIpGroup(TeaModel):
    def __init__(self, group_name=None, ips=None):
        self.group_name = group_name  # type: str
        self.ips = ips  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWhiteIpsRequestWhiteIpGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        return self


class ModifyWhiteIpsRequest(TeaModel):
    def __init__(self, client_token=None, node_type=None, network_type=None, modify_mode=None, white_ip_list=None,
                 white_ip_group=None):
        self.client_token = client_token  # type: str
        self.node_type = node_type  # type: str
        self.network_type = network_type  # type: str
        self.modify_mode = modify_mode  # type: str
        self.white_ip_list = white_ip_list  # type: list[str]
        self.white_ip_group = white_ip_group  # type: ModifyWhiteIpsRequestWhiteIpGroup

    def validate(self):
        if self.white_ip_group:
            self.white_ip_group.validate()

    def to_map(self):
        _map = super(ModifyWhiteIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode
        if self.white_ip_list is not None:
            result['whiteIpList'] = self.white_ip_list
        if self.white_ip_group is not None:
            result['whiteIpGroup'] = self.white_ip_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')
        if m.get('whiteIpList') is not None:
            self.white_ip_list = m.get('whiteIpList')
        if m.get('whiteIpGroup') is not None:
            temp_model = ModifyWhiteIpsRequestWhiteIpGroup()
            self.white_ip_group = temp_model.from_map(m['whiteIpGroup'])
        return self


class ModifyWhiteIpsResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWhiteIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWhiteIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyWhiteIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWhiteIpsResponse, self).to_map()
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
            temp_model = ModifyWhiteIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class MoveResourceGroupResponseBodyResultDictList(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBodyResultDictList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class MoveResourceGroupResponseBodyResultSynonymsDicts(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBodyResultSynonymsDicts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class MoveResourceGroupResponseBodyResultNodeSpec(TeaModel):
    def __init__(self, spec=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBodyResultNodeSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class MoveResourceGroupResponseBodyResultNetworkConfig(TeaModel):
    def __init__(self, vpc_id=None, vs_area=None, type=None, vswitch_id=None):
        self.vpc_id = vpc_id  # type: str
        self.vs_area = vs_area  # type: str
        self.type = type  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBodyResultNetworkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.type is not None:
            result['type'] = self.type
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class MoveResourceGroupResponseBodyResultKibanaConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBodyResultKibanaConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class MoveResourceGroupResponseBodyResultMasterConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBodyResultMasterConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class MoveResourceGroupResponseBodyResult(TeaModel):
    def __init__(self, node_amount=None, public_domain=None, created_at=None, status=None, public_port=None,
                 kibana_port=None, payment_type=None, domain=None, description=None, es_version=None, kibana_domain=None,
                 updated_at=None, instance_id=None, dict_list=None, synonyms_dicts=None, node_spec=None, network_config=None,
                 kibana_configuration=None, master_configuration=None):
        self.node_amount = node_amount  # type: int
        self.public_domain = public_domain  # type: str
        self.created_at = created_at  # type: str
        self.status = status  # type: str
        self.public_port = public_port  # type: int
        self.kibana_port = kibana_port  # type: int
        self.payment_type = payment_type  # type: str
        self.domain = domain  # type: str
        self.description = description  # type: str
        self.es_version = es_version  # type: str
        self.kibana_domain = kibana_domain  # type: str
        self.updated_at = updated_at  # type: str
        self.instance_id = instance_id  # type: str
        self.dict_list = dict_list  # type: list[MoveResourceGroupResponseBodyResultDictList]
        self.synonyms_dicts = synonyms_dicts  # type: list[MoveResourceGroupResponseBodyResultSynonymsDicts]
        self.node_spec = node_spec  # type: MoveResourceGroupResponseBodyResultNodeSpec
        self.network_config = network_config  # type: MoveResourceGroupResponseBodyResultNetworkConfig
        self.kibana_configuration = kibana_configuration  # type: MoveResourceGroupResponseBodyResultKibanaConfiguration
        self.master_configuration = master_configuration  # type: MoveResourceGroupResponseBodyResultMasterConfiguration

    def validate(self):
        if self.dict_list:
            for k in self.dict_list:
                if k:
                    k.validate()
        if self.synonyms_dicts:
            for k in self.synonyms_dicts:
                if k:
                    k.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.network_config:
            self.network_config.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()

    def to_map(self):
        _map = super(MoveResourceGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.status is not None:
            result['status'] = self.status
        if self.public_port is not None:
            result['publicPort'] = self.public_port
        if self.kibana_port is not None:
            result['kibanaPort'] = self.kibana_port
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.domain is not None:
            result['domain'] = self.domain
        if self.description is not None:
            result['description'] = self.description
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.kibana_domain is not None:
            result['kibanaDomain'] = self.kibana_domain
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['dictList'] = []
        if self.dict_list is not None:
            for k in self.dict_list:
                result['dictList'].append(k.to_map() if k else None)
        result['synonymsDicts'] = []
        if self.synonyms_dicts is not None:
            for k in self.synonyms_dicts:
                result['synonymsDicts'].append(k.to_map() if k else None)
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()
        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')
        if m.get('kibanaPort') is not None:
            self.kibana_port = m.get('kibanaPort')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('kibanaDomain') is not None:
            self.kibana_domain = m.get('kibanaDomain')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.dict_list = []
        if m.get('dictList') is not None:
            for k in m.get('dictList'):
                temp_model = MoveResourceGroupResponseBodyResultDictList()
                self.dict_list.append(temp_model.from_map(k))
        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k in m.get('synonymsDicts'):
                temp_model = MoveResourceGroupResponseBodyResultSynonymsDicts()
                self.synonyms_dicts.append(temp_model.from_map(k))
        if m.get('nodeSpec') is not None:
            temp_model = MoveResourceGroupResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('networkConfig') is not None:
            temp_model = MoveResourceGroupResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('kibanaConfiguration') is not None:
            temp_model = MoveResourceGroupResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m['kibanaConfiguration'])
        if m.get('masterConfiguration') is not None:
            temp_model = MoveResourceGroupResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m['masterConfiguration'])
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: MoveResourceGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(MoveResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = MoveResourceGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
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


class OpenDiagnosisRequest(TeaModel):
    def __init__(self, client_token=None, lang=None):
        self.client_token = client_token  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDiagnosisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class OpenDiagnosisResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenDiagnosisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenDiagnosisResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenDiagnosisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenDiagnosisResponse, self).to_map()
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
            temp_model = OpenDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenHttpsRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenHttpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class OpenHttpsResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenHttpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenHttpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenHttpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenHttpsResponse, self).to_map()
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
            temp_model = OpenHttpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostEmonTryAlarmRuleResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostEmonTryAlarmRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostEmonTryAlarmRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PostEmonTryAlarmRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostEmonTryAlarmRuleResponse, self).to_map()
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
            temp_model = PostEmonTryAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecommendTemplatesRequest(TeaModel):
    def __init__(self, usage_scenario=None):
        self.usage_scenario = usage_scenario  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecommendTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.usage_scenario is not None:
            result['usageScenario'] = self.usage_scenario
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('usageScenario') is not None:
            self.usage_scenario = m.get('usageScenario')
        return self


class RecommendTemplatesResponseBodyResult(TeaModel):
    def __init__(self, content=None, template_name=None):
        self.content = content  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecommendTemplatesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.template_name is not None:
            result['templateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        return self


class RecommendTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[RecommendTemplatesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecommendTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = RecommendTemplatesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class RecommendTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecommendTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecommendTemplatesResponse, self).to_map()
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
            temp_model = RecommendTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReinstallCollectorRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReinstallCollectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ReinstallCollectorResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReinstallCollectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReinstallCollectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReinstallCollectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReinstallCollectorResponse, self).to_map()
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
            temp_model = ReinstallCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
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


class RenewLogstashRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewLogstashRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class RenewLogstashResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewLogstashResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewLogstashResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RenewLogstashResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewLogstashResponse, self).to_map()
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
            temp_model = RenewLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartCollectorRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartCollectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RestartCollectorResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartCollectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartCollectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartCollectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartCollectorResponse, self).to_map()
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
            temp_model = RestartCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(self, force=None, client_token=None):
        self.force = force  # type: bool
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class RestartInstanceResponseBodyResultDictList(TeaModel):
    def __init__(self, file_size=None, type=None, name=None, source_type=None):
        self.file_size = file_size  # type: long
        self.type = type  # type: str
        self.name = name  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceResponseBodyResultDictList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.type is not None:
            result['type'] = self.type
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class RestartInstanceResponseBodyResultSynonymsDicts(TeaModel):
    def __init__(self, file_size=None, type=None, name=None, source_type=None):
        self.file_size = file_size  # type: long
        self.type = type  # type: str
        self.name = name  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceResponseBodyResultSynonymsDicts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.type is not None:
            result['type'] = self.type
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class RestartInstanceResponseBodyResultKibanaConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceResponseBodyResultKibanaConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class RestartInstanceResponseBodyResultMasterConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceResponseBodyResultMasterConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class RestartInstanceResponseBodyResultNetworkConfig(TeaModel):
    def __init__(self, vpc_id=None, vs_area=None, type=None, vswitch_id=None):
        self.vpc_id = vpc_id  # type: str
        self.vs_area = vs_area  # type: str
        self.type = type  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceResponseBodyResultNetworkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.type is not None:
            result['type'] = self.type
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class RestartInstanceResponseBodyResultNodeSpec(TeaModel):
    def __init__(self, spec=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstanceResponseBodyResultNodeSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class RestartInstanceResponseBodyResult(TeaModel):
    def __init__(self, node_amount=None, public_domain=None, created_at=None, status=None, kibana_port=None,
                 public_port=None, payment_type=None, domain=None, description=None, es_version=None, kibana_domain=None,
                 updated_at=None, instance_id=None, dict_list=None, synonyms_dicts=None, kibana_configuration=None,
                 master_configuration=None, network_config=None, node_spec=None):
        self.node_amount = node_amount  # type: int
        self.public_domain = public_domain  # type: str
        self.created_at = created_at  # type: str
        self.status = status  # type: str
        self.kibana_port = kibana_port  # type: int
        self.public_port = public_port  # type: int
        self.payment_type = payment_type  # type: str
        self.domain = domain  # type: str
        self.description = description  # type: str
        self.es_version = es_version  # type: str
        self.kibana_domain = kibana_domain  # type: str
        self.updated_at = updated_at  # type: str
        self.instance_id = instance_id  # type: str
        self.dict_list = dict_list  # type: list[RestartInstanceResponseBodyResultDictList]
        self.synonyms_dicts = synonyms_dicts  # type: list[RestartInstanceResponseBodyResultSynonymsDicts]
        self.kibana_configuration = kibana_configuration  # type: RestartInstanceResponseBodyResultKibanaConfiguration
        self.master_configuration = master_configuration  # type: RestartInstanceResponseBodyResultMasterConfiguration
        self.network_config = network_config  # type: RestartInstanceResponseBodyResultNetworkConfig
        self.node_spec = node_spec  # type: RestartInstanceResponseBodyResultNodeSpec

    def validate(self):
        if self.dict_list:
            for k in self.dict_list:
                if k:
                    k.validate()
        if self.synonyms_dicts:
            for k in self.synonyms_dicts:
                if k:
                    k.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()

    def to_map(self):
        _map = super(RestartInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.status is not None:
            result['status'] = self.status
        if self.kibana_port is not None:
            result['kibanaPort'] = self.kibana_port
        if self.public_port is not None:
            result['publicPort'] = self.public_port
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.domain is not None:
            result['domain'] = self.domain
        if self.description is not None:
            result['description'] = self.description
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.kibana_domain is not None:
            result['kibanaDomain'] = self.kibana_domain
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['dictList'] = []
        if self.dict_list is not None:
            for k in self.dict_list:
                result['dictList'].append(k.to_map() if k else None)
        result['synonymsDicts'] = []
        if self.synonyms_dicts is not None:
            for k in self.synonyms_dicts:
                result['synonymsDicts'].append(k.to_map() if k else None)
        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()
        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('kibanaPort') is not None:
            self.kibana_port = m.get('kibanaPort')
        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('kibanaDomain') is not None:
            self.kibana_domain = m.get('kibanaDomain')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.dict_list = []
        if m.get('dictList') is not None:
            for k in m.get('dictList'):
                temp_model = RestartInstanceResponseBodyResultDictList()
                self.dict_list.append(temp_model.from_map(k))
        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k in m.get('synonymsDicts'):
                temp_model = RestartInstanceResponseBodyResultSynonymsDicts()
                self.synonyms_dicts.append(temp_model.from_map(k))
        if m.get('kibanaConfiguration') is not None:
            temp_model = RestartInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m['kibanaConfiguration'])
        if m.get('masterConfiguration') is not None:
            temp_model = RestartInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m['masterConfiguration'])
        if m.get('networkConfig') is not None:
            temp_model = RestartInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('nodeSpec') is not None:
            temp_model = RestartInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        return self


class RestartInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: RestartInstanceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(RestartInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = RestartInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
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


class RestartLogstashRequest(TeaModel):
    def __init__(self, force=None, client_token=None):
        self.force = force  # type: bool
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartLogstashRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class RestartLogstashResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartLogstashResponseBody, self).to_map()
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


class RestartLogstashResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartLogstashResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartLogstashResponse, self).to_map()
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
            temp_model = RestartLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeElasticsearchTaskRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeElasticsearchTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ResumeElasticsearchTaskResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeElasticsearchTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResumeElasticsearchTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResumeElasticsearchTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeElasticsearchTaskResponse, self).to_map()
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
            temp_model = ResumeElasticsearchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeLogstashTaskRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeLogstashTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ResumeLogstashTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeLogstashTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ResumeLogstashTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResumeLogstashTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeLogstashTaskResponse, self).to_map()
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
            temp_model = ResumeLogstashTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RolloverDataStreamRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RolloverDataStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RolloverDataStreamResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RolloverDataStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RolloverDataStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RolloverDataStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RolloverDataStreamResponse, self).to_map()
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
            temp_model = RolloverDataStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunPipelinesRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunPipelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RunPipelinesResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunPipelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunPipelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RunPipelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RunPipelinesResponse, self).to_map()
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
            temp_model = RunPipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShrinkNodeRequest(TeaModel):
    def __init__(self, node_type=None, client_token=None, ignore_status=None):
        self.node_type = node_type  # type: str
        self.client_token = client_token  # type: str
        self.ignore_status = ignore_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShrinkNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.ignore_status is not None:
            result['ignoreStatus'] = self.ignore_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ignoreStatus') is not None:
            self.ignore_status = m.get('ignoreStatus')
        return self


class ShrinkNodeResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShrinkNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ShrinkNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ShrinkNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ShrinkNodeResponse, self).to_map()
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
            temp_model = ShrinkNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCollectorRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartCollectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StartCollectorResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartCollectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartCollectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartCollectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartCollectorResponse, self).to_map()
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
            temp_model = StartCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCollectorRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopCollectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StopCollectorResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopCollectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopCollectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopCollectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopCollectorResponse, self).to_map()
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
            temp_model = StopCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopPipelinesRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopPipelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StopPipelinesResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopPipelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopPipelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopPipelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopPipelinesResponse, self).to_map()
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
            temp_model = StopPipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
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


class TransferNodeRequest(TeaModel):
    def __init__(self, node_type=None, client_token=None):
        self.node_type = node_type  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class TransferNodeResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TransferNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TransferNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferNodeResponse, self).to_map()
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
            temp_model = TransferNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerNetworkRequest(TeaModel):
    def __init__(self, client_token=None, node_type=None, network_type=None, action_type=None):
        self.client_token = client_token  # type: str
        self.node_type = node_type  # type: str
        self.network_type = network_type  # type: str
        self.action_type = action_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerNetworkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.action_type is not None:
            result['actionType'] = self.action_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        return self


class TriggerNetworkResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerNetworkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TriggerNetworkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TriggerNetworkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TriggerNetworkResponse, self).to_map()
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
            temp_model = TriggerNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallKibanaPluginRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallKibanaPluginRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UninstallKibanaPluginResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallKibanaPluginResponseBody, self).to_map()
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


class UninstallKibanaPluginResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UninstallKibanaPluginResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UninstallKibanaPluginResponse, self).to_map()
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
            temp_model = UninstallKibanaPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallLogstashPluginRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallLogstashPluginRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UninstallLogstashPluginResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallLogstashPluginResponseBody, self).to_map()
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


class UninstallLogstashPluginResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UninstallLogstashPluginResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UninstallLogstashPluginResponse, self).to_map()
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
            temp_model = UninstallLogstashPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallPluginRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallPluginRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UninstallPluginResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallPluginResponseBody, self).to_map()
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


class UninstallPluginResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UninstallPluginResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UninstallPluginResponse, self).to_map()
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
            temp_model = UninstallPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, resource_ids=None, resource_type=None, tag_keys=None, all=None):
        self.resource_ids = resource_ids  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_keys = tag_keys  # type: str
        self.all = all  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAdminPasswordRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAdminPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateAdminPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAdminPasswordResponseBody, self).to_map()
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


class UpdateAdminPasswordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAdminPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAdminPasswordResponse, self).to_map()
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
            temp_model = UpdateAdminPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAdvancedSettingRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAdvancedSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateAdvancedSettingResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAdvancedSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAdvancedSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAdvancedSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAdvancedSettingResponse, self).to_map()
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
            temp_model = UpdateAdvancedSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAliwsDictRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAliwsDictRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateAliwsDictResponseBodyResult(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAliwsDictResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateAliwsDictResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[UpdateAliwsDictResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateAliwsDictResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = UpdateAliwsDictResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class UpdateAliwsDictResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAliwsDictResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAliwsDictResponse, self).to_map()
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
            temp_model = UpdateAliwsDictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBlackIpsRequest(TeaModel):
    def __init__(self, client_token=None, es_ipblacklist=None):
        self.client_token = client_token  # type: str
        self.es_ipblacklist = es_ipblacklist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBlackIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.es_ipblacklist is not None:
            result['esIPBlacklist'] = self.es_ipblacklist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('esIPBlacklist') is not None:
            self.es_ipblacklist = m.get('esIPBlacklist')
        return self


class UpdateBlackIpsResponseBodyResult(TeaModel):
    def __init__(self, es_ipblacklist=None):
        self.es_ipblacklist = es_ipblacklist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBlackIpsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.es_ipblacklist is not None:
            result['esIPBlacklist'] = self.es_ipblacklist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('esIPBlacklist') is not None:
            self.es_ipblacklist = m.get('esIPBlacklist')
        return self


class UpdateBlackIpsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateBlackIpsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateBlackIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateBlackIpsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateBlackIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateBlackIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBlackIpsResponse, self).to_map()
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
            temp_model = UpdateBlackIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCollectorRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCollectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateCollectorResponseBodyResultConfigs(TeaModel):
    def __init__(self, content=None, file_name=None):
        self.content = content  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCollectorResponseBodyResultConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class UpdateCollectorResponseBodyResultExtendConfigsMachines(TeaModel):
    def __init__(self, agent_status=None, instance_id=None):
        self.agent_status = agent_status  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCollectorResponseBodyResultExtendConfigsMachines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['agentStatus'] = self.agent_status
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('agentStatus') is not None:
            self.agent_status = m.get('agentStatus')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class UpdateCollectorResponseBodyResultExtendConfigs(TeaModel):
    def __init__(self, success_pods_count=None, protocol=None, user_name=None, total_pods_count=None, type=None,
                 kibana_host=None, enable_monitoring=None, config_type=None, instance_type=None, group_id=None, host=None,
                 instance_id=None, machines=None, hosts=None):
        self.success_pods_count = success_pods_count  # type: str
        self.protocol = protocol  # type: str
        self.user_name = user_name  # type: str
        self.total_pods_count = total_pods_count  # type: str
        self.type = type  # type: str
        self.kibana_host = kibana_host  # type: str
        self.enable_monitoring = enable_monitoring  # type: bool
        self.config_type = config_type  # type: str
        self.instance_type = instance_type  # type: str
        self.group_id = group_id  # type: str
        self.host = host  # type: str
        self.instance_id = instance_id  # type: str
        self.machines = machines  # type: list[UpdateCollectorResponseBodyResultExtendConfigsMachines]
        self.hosts = hosts  # type: list[str]

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCollectorResponseBodyResultExtendConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_pods_count is not None:
            result['successPodsCount'] = self.success_pods_count
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.total_pods_count is not None:
            result['totalPodsCount'] = self.total_pods_count
        if self.type is not None:
            result['type'] = self.type
        if self.kibana_host is not None:
            result['kibanaHost'] = self.kibana_host
        if self.enable_monitoring is not None:
            result['enableMonitoring'] = self.enable_monitoring
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.host is not None:
            result['host'] = self.host
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['machines'] = []
        if self.machines is not None:
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
        if self.hosts is not None:
            result['hosts'] = self.hosts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('successPodsCount') is not None:
            self.success_pods_count = m.get('successPodsCount')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('totalPodsCount') is not None:
            self.total_pods_count = m.get('totalPodsCount')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('kibanaHost') is not None:
            self.kibana_host = m.get('kibanaHost')
        if m.get('enableMonitoring') is not None:
            self.enable_monitoring = m.get('enableMonitoring')
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.machines = []
        if m.get('machines') is not None:
            for k in m.get('machines'):
                temp_model = UpdateCollectorResponseBodyResultExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k))
        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')
        return self


class UpdateCollectorResponseBodyResult(TeaModel):
    def __init__(self, res_id=None, gmt_update_time=None, dry_run=None, owner_id=None, vpc_id=None, res_type=None,
                 res_version=None, gmt_created_time=None, status=None, name=None, configs=None, extend_configs=None,
                 collector_paths=None):
        self.res_id = res_id  # type: str
        self.gmt_update_time = gmt_update_time  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_id = owner_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.res_type = res_type  # type: str
        self.res_version = res_version  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.status = status  # type: str
        self.name = name  # type: str
        self.configs = configs  # type: list[UpdateCollectorResponseBodyResultConfigs]
        self.extend_configs = extend_configs  # type: list[UpdateCollectorResponseBodyResultExtendConfigs]
        self.collector_paths = collector_paths  # type: list[str]

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCollectorResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_id is not None:
            result['resId'] = self.res_id
        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.res_type is not None:
            result['resType'] = self.res_type
        if self.res_version is not None:
            result['resVersion'] = self.res_version
        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['extendConfigs'].append(k.to_map() if k else None)
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resId') is not None:
            self.res_id = m.get('resId')
        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('resType') is not None:
            self.res_type = m.get('resType')
        if m.get('resVersion') is not None:
            self.res_version = m.get('resVersion')
        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = UpdateCollectorResponseBodyResultConfigs()
                self.configs.append(temp_model.from_map(k))
        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k in m.get('extendConfigs'):
                temp_model = UpdateCollectorResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
        if m.get('collectorPaths') is not None:
            self.collector_paths = m.get('collectorPaths')
        return self


class UpdateCollectorResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateCollectorResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateCollectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateCollectorResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateCollectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateCollectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCollectorResponse, self).to_map()
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
            temp_model = UpdateCollectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCollectorNameRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCollectorNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateCollectorNameResponseBodyResultConfigs(TeaModel):
    def __init__(self, content=None, file_name=None):
        self.content = content  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCollectorNameResponseBodyResultConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class UpdateCollectorNameResponseBodyResultExtendConfigsMachines(TeaModel):
    def __init__(self, agent_status=None, instance_id=None):
        self.agent_status = agent_status  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCollectorNameResponseBodyResultExtendConfigsMachines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['agentStatus'] = self.agent_status
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('agentStatus') is not None:
            self.agent_status = m.get('agentStatus')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class UpdateCollectorNameResponseBodyResultExtendConfigs(TeaModel):
    def __init__(self, success_pods_count=None, protocol=None, user_name=None, total_pods_count=None, type=None,
                 kibana_host=None, enable_monitoring=None, config_type=None, instance_type=None, group_id=None, host=None,
                 instance_id=None, machines=None, hosts=None):
        self.success_pods_count = success_pods_count  # type: str
        self.protocol = protocol  # type: str
        self.user_name = user_name  # type: str
        self.total_pods_count = total_pods_count  # type: str
        self.type = type  # type: str
        self.kibana_host = kibana_host  # type: str
        self.enable_monitoring = enable_monitoring  # type: bool
        self.config_type = config_type  # type: str
        self.instance_type = instance_type  # type: str
        self.group_id = group_id  # type: str
        self.host = host  # type: str
        self.instance_id = instance_id  # type: str
        self.machines = machines  # type: list[UpdateCollectorNameResponseBodyResultExtendConfigsMachines]
        self.hosts = hosts  # type: list[str]

    def validate(self):
        if self.machines:
            for k in self.machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCollectorNameResponseBodyResultExtendConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_pods_count is not None:
            result['successPodsCount'] = self.success_pods_count
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.total_pods_count is not None:
            result['totalPodsCount'] = self.total_pods_count
        if self.type is not None:
            result['type'] = self.type
        if self.kibana_host is not None:
            result['kibanaHost'] = self.kibana_host
        if self.enable_monitoring is not None:
            result['enableMonitoring'] = self.enable_monitoring
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.host is not None:
            result['host'] = self.host
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['machines'] = []
        if self.machines is not None:
            for k in self.machines:
                result['machines'].append(k.to_map() if k else None)
        if self.hosts is not None:
            result['hosts'] = self.hosts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('successPodsCount') is not None:
            self.success_pods_count = m.get('successPodsCount')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('totalPodsCount') is not None:
            self.total_pods_count = m.get('totalPodsCount')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('kibanaHost') is not None:
            self.kibana_host = m.get('kibanaHost')
        if m.get('enableMonitoring') is not None:
            self.enable_monitoring = m.get('enableMonitoring')
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.machines = []
        if m.get('machines') is not None:
            for k in m.get('machines'):
                temp_model = UpdateCollectorNameResponseBodyResultExtendConfigsMachines()
                self.machines.append(temp_model.from_map(k))
        if m.get('hosts') is not None:
            self.hosts = m.get('hosts')
        return self


class UpdateCollectorNameResponseBodyResult(TeaModel):
    def __init__(self, res_id=None, gmt_update_time=None, dry_run=None, owner_id=None, vpc_id=None, res_type=None,
                 res_version=None, gmt_created_time=None, status=None, name=None, configs=None, extend_configs=None,
                 collector_paths=None):
        self.res_id = res_id  # type: str
        self.gmt_update_time = gmt_update_time  # type: str
        self.dry_run = dry_run  # type: bool
        self.owner_id = owner_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.res_type = res_type  # type: str
        self.res_version = res_version  # type: str
        self.gmt_created_time = gmt_created_time  # type: str
        self.status = status  # type: str
        self.name = name  # type: str
        self.configs = configs  # type: list[UpdateCollectorNameResponseBodyResultConfigs]
        self.extend_configs = extend_configs  # type: list[UpdateCollectorNameResponseBodyResultExtendConfigs]
        self.collector_paths = collector_paths  # type: list[str]

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()
        if self.extend_configs:
            for k in self.extend_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCollectorNameResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.res_id is not None:
            result['resId'] = self.res_id
        if self.gmt_update_time is not None:
            result['gmtUpdateTime'] = self.gmt_update_time
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.res_type is not None:
            result['resType'] = self.res_type
        if self.res_version is not None:
            result['resVersion'] = self.res_version
        if self.gmt_created_time is not None:
            result['gmtCreatedTime'] = self.gmt_created_time
        if self.status is not None:
            result['status'] = self.status
        if self.name is not None:
            result['name'] = self.name
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        result['extendConfigs'] = []
        if self.extend_configs is not None:
            for k in self.extend_configs:
                result['extendConfigs'].append(k.to_map() if k else None)
        if self.collector_paths is not None:
            result['collectorPaths'] = self.collector_paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resId') is not None:
            self.res_id = m.get('resId')
        if m.get('gmtUpdateTime') is not None:
            self.gmt_update_time = m.get('gmtUpdateTime')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('resType') is not None:
            self.res_type = m.get('resType')
        if m.get('resVersion') is not None:
            self.res_version = m.get('resVersion')
        if m.get('gmtCreatedTime') is not None:
            self.gmt_created_time = m.get('gmtCreatedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = UpdateCollectorNameResponseBodyResultConfigs()
                self.configs.append(temp_model.from_map(k))
        self.extend_configs = []
        if m.get('extendConfigs') is not None:
            for k in m.get('extendConfigs'):
                temp_model = UpdateCollectorNameResponseBodyResultExtendConfigs()
                self.extend_configs.append(temp_model.from_map(k))
        if m.get('collectorPaths') is not None:
            self.collector_paths = m.get('collectorPaths')
        return self


class UpdateCollectorNameResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateCollectorNameResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateCollectorNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateCollectorNameResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateCollectorNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateCollectorNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCollectorNameResponse, self).to_map()
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
            temp_model = UpdateCollectorNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDescriptionRequest(TeaModel):
    def __init__(self, client_token=None, description=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateDescriptionResponseBodyResult(TeaModel):
    def __init__(self, description=None):
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDescriptionResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateDescriptionResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateDescriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateDescriptionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDescriptionResponse, self).to_map()
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
            temp_model = UpdateDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDiagnosisSettingsRequest(TeaModel):
    def __init__(self, client_token=None, lang=None):
        self.client_token = client_token  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDiagnosisSettingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.lang is not None:
            result['lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        return self


class UpdateDiagnosisSettingsResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDiagnosisSettingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDiagnosisSettingsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDiagnosisSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDiagnosisSettingsResponse, self).to_map()
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
            temp_model = UpdateDiagnosisSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDictRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDictRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateDictResponseBodyResult(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDictResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateDictResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[UpdateDictResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateDictResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = UpdateDictResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class UpdateDictResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateDictResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDictResponse, self).to_map()
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
            temp_model = UpdateDictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExtendConfigRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExtendConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateExtendConfigResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExtendConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateExtendConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateExtendConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateExtendConfigResponse, self).to_map()
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
            temp_model = UpdateExtendConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExtendfilesRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExtendfilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateExtendfilesResponseBodyResult(TeaModel):
    def __init__(self, file_size=None, name=None, source_type=None):
        self.file_size = file_size  # type: long
        self.name = name  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExtendfilesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.name is not None:
            result['name'] = self.name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        return self


class UpdateExtendfilesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[UpdateExtendfilesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateExtendfilesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = UpdateExtendfilesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class UpdateExtendfilesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateExtendfilesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateExtendfilesResponse, self).to_map()
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
            temp_model = UpdateExtendfilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHotIkDictsRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotIkDictsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateHotIkDictsResponseBodyResult(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHotIkDictsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateHotIkDictsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[UpdateHotIkDictsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateHotIkDictsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = UpdateHotIkDictsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class UpdateHotIkDictsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateHotIkDictsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHotIkDictsResponse, self).to_map()
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
            temp_model = UpdateHotIkDictsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateILMPolicyRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateILMPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateILMPolicyResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateILMPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateILMPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateILMPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateILMPolicyResponse, self).to_map()
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
            temp_model = UpdateILMPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIndexTemplateRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIndexTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateIndexTemplateResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIndexTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateIndexTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateIndexTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIndexTemplateResponse, self).to_map()
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
            temp_model = UpdateIndexTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(self, client_token=None, ignore_status=None, order_action_type=None):
        self.client_token = client_token  # type: str
        self.ignore_status = ignore_status  # type: bool
        self.order_action_type = order_action_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.ignore_status is not None:
            result['ignoreStatus'] = self.ignore_status
        if self.order_action_type is not None:
            result['orderActionType'] = self.order_action_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ignoreStatus') is not None:
            self.ignore_status = m.get('ignoreStatus')
        if m.get('orderActionType') is not None:
            self.order_action_type = m.get('orderActionType')
        return self


class UpdateInstanceResponseBodyResultDictList(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBodyResultDictList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateInstanceResponseBodyResultSynonymsDicts(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBodyResultSynonymsDicts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateInstanceResponseBodyResultNodeSpec(TeaModel):
    def __init__(self, spec=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBodyResultNodeSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class UpdateInstanceResponseBodyResultNetworkConfig(TeaModel):
    def __init__(self, vpc_id=None, vs_area=None, type=None, vswitch_id=None):
        self.vpc_id = vpc_id  # type: str
        self.vs_area = vs_area  # type: str
        self.type = type  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBodyResultNetworkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vs_area is not None:
            result['vsArea'] = self.vs_area
        if self.type is not None:
            result['type'] = self.type
        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')
        return self


class UpdateInstanceResponseBodyResultKibanaConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBodyResultKibanaConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class UpdateInstanceResponseBodyResultMasterConfiguration(TeaModel):
    def __init__(self, spec=None, amount=None, disk=None, disk_type=None):
        self.spec = spec  # type: str
        self.amount = amount  # type: int
        self.disk = disk  # type: int
        self.disk_type = disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBodyResultMasterConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.amount is not None:
            result['amount'] = self.amount
        if self.disk is not None:
            result['disk'] = self.disk
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('disk') is not None:
            self.disk = m.get('disk')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        return self


class UpdateInstanceResponseBodyResult(TeaModel):
    def __init__(self, node_amount=None, public_domain=None, created_at=None, status=None, public_port=None,
                 kibana_port=None, payment_type=None, domain=None, description=None, es_version=None, kibana_domain=None,
                 updated_at=None, instance_id=None, dict_list=None, synonyms_dicts=None, node_spec=None, network_config=None,
                 kibana_configuration=None, master_configuration=None):
        self.node_amount = node_amount  # type: int
        self.public_domain = public_domain  # type: str
        self.created_at = created_at  # type: str
        self.status = status  # type: str
        self.public_port = public_port  # type: int
        self.kibana_port = kibana_port  # type: int
        self.payment_type = payment_type  # type: str
        self.domain = domain  # type: str
        self.description = description  # type: str
        self.es_version = es_version  # type: str
        self.kibana_domain = kibana_domain  # type: str
        self.updated_at = updated_at  # type: str
        self.instance_id = instance_id  # type: str
        self.dict_list = dict_list  # type: list[UpdateInstanceResponseBodyResultDictList]
        self.synonyms_dicts = synonyms_dicts  # type: list[UpdateInstanceResponseBodyResultSynonymsDicts]
        self.node_spec = node_spec  # type: UpdateInstanceResponseBodyResultNodeSpec
        self.network_config = network_config  # type: UpdateInstanceResponseBodyResultNetworkConfig
        self.kibana_configuration = kibana_configuration  # type: UpdateInstanceResponseBodyResultKibanaConfiguration
        self.master_configuration = master_configuration  # type: UpdateInstanceResponseBodyResultMasterConfiguration

    def validate(self):
        if self.dict_list:
            for k in self.dict_list:
                if k:
                    k.validate()
        if self.synonyms_dicts:
            for k in self.synonyms_dicts:
                if k:
                    k.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.network_config:
            self.network_config.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()

    def to_map(self):
        _map = super(UpdateInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.status is not None:
            result['status'] = self.status
        if self.public_port is not None:
            result['publicPort'] = self.public_port
        if self.kibana_port is not None:
            result['kibanaPort'] = self.kibana_port
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.domain is not None:
            result['domain'] = self.domain
        if self.description is not None:
            result['description'] = self.description
        if self.es_version is not None:
            result['esVersion'] = self.es_version
        if self.kibana_domain is not None:
            result['kibanaDomain'] = self.kibana_domain
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['dictList'] = []
        if self.dict_list is not None:
            for k in self.dict_list:
                result['dictList'].append(k.to_map() if k else None)
        result['synonymsDicts'] = []
        if self.synonyms_dicts is not None:
            for k in self.synonyms_dicts:
                result['synonymsDicts'].append(k.to_map() if k else None)
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()
        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')
        if m.get('kibanaPort') is not None:
            self.kibana_port = m.get('kibanaPort')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')
        if m.get('kibanaDomain') is not None:
            self.kibana_domain = m.get('kibanaDomain')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.dict_list = []
        if m.get('dictList') is not None:
            for k in m.get('dictList'):
                temp_model = UpdateInstanceResponseBodyResultDictList()
                self.dict_list.append(temp_model.from_map(k))
        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k in m.get('synonymsDicts'):
                temp_model = UpdateInstanceResponseBodyResultSynonymsDicts()
                self.synonyms_dicts.append(temp_model.from_map(k))
        if m.get('nodeSpec') is not None:
            temp_model = UpdateInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m['nodeSpec'])
        if m.get('networkConfig') is not None:
            temp_model = UpdateInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        if m.get('kibanaConfiguration') is not None:
            temp_model = UpdateInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m['kibanaConfiguration'])
        if m.get('masterConfiguration') is not None:
            temp_model = UpdateInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m['masterConfiguration'])
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateInstanceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceResponse, self).to_map()
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceChargeTypeRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceChargeTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateInstanceChargeTypeResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceChargeTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceChargeTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateInstanceChargeTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceChargeTypeResponse, self).to_map()
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
            temp_model = UpdateInstanceChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceSettingsRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceSettingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateInstanceSettingsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceSettingsResponseBody, self).to_map()
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


class UpdateInstanceSettingsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateInstanceSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceSettingsResponse, self).to_map()
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
            temp_model = UpdateInstanceSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKibanaSettingsRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKibanaSettingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateKibanaSettingsResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKibanaSettingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateKibanaSettingsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateKibanaSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateKibanaSettingsResponse, self).to_map()
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
            temp_model = UpdateKibanaSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKibanaWhiteIpsRequest(TeaModel):
    def __init__(self, client_token=None, modify_mode=None):
        self.client_token = client_token  # type: str
        self.modify_mode = modify_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKibanaWhiteIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')
        return self


class UpdateKibanaWhiteIpsResponseBodyResult(TeaModel):
    def __init__(self, kibana_private_ipwhitelist=None, kibana_ipwhitelist=None):
        self.kibana_private_ipwhitelist = kibana_private_ipwhitelist  # type: list[str]
        self.kibana_ipwhitelist = kibana_ipwhitelist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKibanaWhiteIpsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kibana_private_ipwhitelist is not None:
            result['kibanaPrivateIPWhitelist'] = self.kibana_private_ipwhitelist
        if self.kibana_ipwhitelist is not None:
            result['kibanaIPWhitelist'] = self.kibana_ipwhitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('kibanaPrivateIPWhitelist') is not None:
            self.kibana_private_ipwhitelist = m.get('kibanaPrivateIPWhitelist')
        if m.get('kibanaIPWhitelist') is not None:
            self.kibana_ipwhitelist = m.get('kibanaIPWhitelist')
        return self


class UpdateKibanaWhiteIpsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateKibanaWhiteIpsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateKibanaWhiteIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateKibanaWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateKibanaWhiteIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateKibanaWhiteIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateKibanaWhiteIpsResponse, self).to_map()
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
            temp_model = UpdateKibanaWhiteIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLogstashRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLogstashRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateLogstashResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLogstashResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLogstashResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateLogstashResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLogstashResponse, self).to_map()
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
            temp_model = UpdateLogstashResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLogstashChargeTypeRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLogstashChargeTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateLogstashChargeTypeResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLogstashChargeTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLogstashChargeTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateLogstashChargeTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLogstashChargeTypeResponse, self).to_map()
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
            temp_model = UpdateLogstashChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLogstashDescriptionRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLogstashDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateLogstashDescriptionResponseBodyResult(TeaModel):
    def __init__(self, description=None):
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLogstashDescriptionResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateLogstashDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateLogstashDescriptionResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateLogstashDescriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateLogstashDescriptionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateLogstashDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateLogstashDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLogstashDescriptionResponse, self).to_map()
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
            temp_model = UpdateLogstashDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLogstashSettingsRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLogstashSettingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateLogstashSettingsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLogstashSettingsResponseBody, self).to_map()
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


class UpdateLogstashSettingsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateLogstashSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLogstashSettingsResponse, self).to_map()
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
            temp_model = UpdateLogstashSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelineManagementConfigRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePipelineManagementConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdatePipelineManagementConfigResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePipelineManagementConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePipelineManagementConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePipelineManagementConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePipelineManagementConfigResponse, self).to_map()
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
            temp_model = UpdatePipelineManagementConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelinesRequest(TeaModel):
    def __init__(self, trigger=None, client_token=None):
        self.trigger = trigger  # type: bool
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePipelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger is not None:
            result['trigger'] = self.trigger
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('trigger') is not None:
            self.trigger = m.get('trigger')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdatePipelinesResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePipelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePipelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePipelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePipelinesResponse, self).to_map()
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
            temp_model = UpdatePipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrivateNetworkWhiteIpsRequest(TeaModel):
    def __init__(self, client_token=None, modify_mode=None):
        self.client_token = client_token  # type: str
        self.modify_mode = modify_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrivateNetworkWhiteIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')
        return self


class UpdatePrivateNetworkWhiteIpsResponseBodyResult(TeaModel):
    def __init__(self, private_network_ip_white_list=None):
        self.private_network_ip_white_list = private_network_ip_white_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrivateNetworkWhiteIpsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_network_ip_white_list is not None:
            result['privateNetworkIpWhiteList'] = self.private_network_ip_white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('privateNetworkIpWhiteList') is not None:
            self.private_network_ip_white_list = m.get('privateNetworkIpWhiteList')
        return self


class UpdatePrivateNetworkWhiteIpsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdatePrivateNetworkWhiteIpsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdatePrivateNetworkWhiteIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdatePrivateNetworkWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdatePrivateNetworkWhiteIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePrivateNetworkWhiteIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePrivateNetworkWhiteIpsResponse, self).to_map()
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
            temp_model = UpdatePrivateNetworkWhiteIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePublicNetworkRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePublicNetworkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdatePublicNetworkResponseBodyResult(TeaModel):
    def __init__(self, enable_public=None):
        self.enable_public = enable_public  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePublicNetworkResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_public is not None:
            result['enablePublic'] = self.enable_public
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')
        return self


class UpdatePublicNetworkResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdatePublicNetworkResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdatePublicNetworkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdatePublicNetworkResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdatePublicNetworkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePublicNetworkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePublicNetworkResponse, self).to_map()
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
            temp_model = UpdatePublicNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePublicWhiteIpsRequest(TeaModel):
    def __init__(self, client_token=None, modify_mode=None):
        self.client_token = client_token  # type: str
        self.modify_mode = modify_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePublicWhiteIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')
        return self


class UpdatePublicWhiteIpsResponseBodyResult(TeaModel):
    def __init__(self, public_ip_whitelist=None):
        self.public_ip_whitelist = public_ip_whitelist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePublicWhiteIpsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public_ip_whitelist is not None:
            result['publicIpWhitelist'] = self.public_ip_whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('publicIpWhitelist') is not None:
            self.public_ip_whitelist = m.get('publicIpWhitelist')
        return self


class UpdatePublicWhiteIpsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdatePublicWhiteIpsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdatePublicWhiteIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdatePublicWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdatePublicWhiteIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePublicWhiteIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePublicWhiteIpsResponse, self).to_map()
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
            temp_model = UpdatePublicWhiteIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateReadWritePolicyRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReadWritePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateReadWritePolicyResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReadWritePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateReadWritePolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateReadWritePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateReadWritePolicyResponse, self).to_map()
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
            temp_model = UpdateReadWritePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSnapshotSettingResponseBodyResult(TeaModel):
    def __init__(self, quartz_regex=None, enable=None):
        self.quartz_regex = quartz_regex  # type: str
        self.enable = enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSnapshotSettingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quartz_regex is not None:
            result['quartzRegex'] = self.quartz_regex
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('quartzRegex') is not None:
            self.quartz_regex = m.get('quartzRegex')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class UpdateSnapshotSettingResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateSnapshotSettingResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateSnapshotSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateSnapshotSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateSnapshotSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSnapshotSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSnapshotSettingResponse, self).to_map()
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
            temp_model = UpdateSnapshotSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSynonymsDictsRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSynonymsDictsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class UpdateSynonymsDictsResponseBodyResult(TeaModel):
    def __init__(self, file_size=None, source_type=None, name=None, type=None):
        self.file_size = file_size  # type: long
        self.source_type = source_type  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSynonymsDictsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateSynonymsDictsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[UpdateSynonymsDictsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateSynonymsDictsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = UpdateSynonymsDictsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class UpdateSynonymsDictsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSynonymsDictsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSynonymsDictsResponse, self).to_map()
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
            temp_model = UpdateSynonymsDictsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTemplateResponse, self).to_map()
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
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWhiteIpsRequestWhiteIpGroup(TeaModel):
    def __init__(self, group_name=None, ips=None, white_ip_type=None):
        self.group_name = group_name  # type: str
        self.ips = ips  # type: list[str]
        self.white_ip_type = white_ip_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWhiteIpsRequestWhiteIpGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.ips is not None:
            result['ips'] = self.ips
        if self.white_ip_type is not None:
            result['whiteIpType'] = self.white_ip_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('ips') is not None:
            self.ips = m.get('ips')
        if m.get('whiteIpType') is not None:
            self.white_ip_type = m.get('whiteIpType')
        return self


class UpdateWhiteIpsRequest(TeaModel):
    def __init__(self, client_token=None, modify_mode=None, es_ipwhitelist=None, white_ip_group=None):
        self.client_token = client_token  # type: str
        self.modify_mode = modify_mode  # type: str
        self.es_ipwhitelist = es_ipwhitelist  # type: list[str]
        self.white_ip_group = white_ip_group  # type: UpdateWhiteIpsRequestWhiteIpGroup

    def validate(self):
        if self.white_ip_group:
            self.white_ip_group.validate()

    def to_map(self):
        _map = super(UpdateWhiteIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode
        if self.es_ipwhitelist is not None:
            result['esIPWhitelist'] = self.es_ipwhitelist
        if self.white_ip_group is not None:
            result['whiteIpGroup'] = self.white_ip_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')
        if m.get('esIPWhitelist') is not None:
            self.es_ipwhitelist = m.get('esIPWhitelist')
        if m.get('whiteIpGroup') is not None:
            temp_model = UpdateWhiteIpsRequestWhiteIpGroup()
            self.white_ip_group = temp_model.from_map(m['whiteIpGroup'])
        return self


class UpdateWhiteIpsResponseBodyResult(TeaModel):
    def __init__(self, es_ipwhitelist=None):
        self.es_ipwhitelist = es_ipwhitelist  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWhiteIpsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.es_ipwhitelist is not None:
            result['esIPWhitelist'] = self.es_ipwhitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('esIPWhitelist') is not None:
            self.es_ipwhitelist = m.get('esIPWhitelist')
        return self


class UpdateWhiteIpsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateWhiteIpsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateWhiteIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateWhiteIpsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateWhiteIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWhiteIpsResponse, self).to_map()
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
            temp_model = UpdateWhiteIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateXpackMonitorConfigRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateXpackMonitorConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateXpackMonitorConfigResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateXpackMonitorConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateXpackMonitorConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateXpackMonitorConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateXpackMonitorConfigResponse, self).to_map()
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
            temp_model = UpdateXpackMonitorConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeEngineVersionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, version=None, type=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.version = version  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeEngineVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        if self.version is not None:
            result['version'] = self.version
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpgradeEngineVersionResponseBodyResultValidateResult(TeaModel):
    def __init__(self, error_type=None, error_code=None, error_msg=None):
        self.error_type = error_type  # type: str
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeEngineVersionResponseBodyResultValidateResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_type is not None:
            result['errorType'] = self.error_type
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorType') is not None:
            self.error_type = m.get('errorType')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        return self


class UpgradeEngineVersionResponseBodyResult(TeaModel):
    def __init__(self, validate_type=None, status=None, validate_result=None):
        self.validate_type = validate_type  # type: str
        self.status = status  # type: str
        self.validate_result = validate_result  # type: UpgradeEngineVersionResponseBodyResultValidateResult

    def validate(self):
        if self.validate_result:
            self.validate_result.validate()

    def to_map(self):
        _map = super(UpgradeEngineVersionResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.validate_type is not None:
            result['validateType'] = self.validate_type
        if self.status is not None:
            result['status'] = self.status
        if self.validate_result is not None:
            result['validateResult'] = self.validate_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('validateType') is not None:
            self.validate_type = m.get('validateType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('validateResult') is not None:
            temp_model = UpgradeEngineVersionResponseBodyResultValidateResult()
            self.validate_result = temp_model.from_map(m['validateResult'])
        return self


class UpgradeEngineVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpgradeEngineVersionResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpgradeEngineVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpgradeEngineVersionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpgradeEngineVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeEngineVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeEngineVersionResponse, self).to_map()
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
            temp_model = UpgradeEngineVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateConnectionRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ValidateConnectionResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateConnectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValidateConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ValidateConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateConnectionResponse, self).to_map()
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
            temp_model = ValidateConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateShrinkNodesRequest(TeaModel):
    def __init__(self, node_type=None, ignore_status=None):
        self.node_type = node_type  # type: str
        self.ignore_status = ignore_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateShrinkNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.ignore_status is not None:
            result['ignoreStatus'] = self.ignore_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('ignoreStatus') is not None:
            self.ignore_status = m.get('ignoreStatus')
        return self


class ValidateShrinkNodesResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateShrinkNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValidateShrinkNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ValidateShrinkNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateShrinkNodesResponse, self).to_map()
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
            temp_model = ValidateShrinkNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateSlrPermissionRequest(TeaModel):
    def __init__(self, client_token=None, rolename=None):
        self.client_token = client_token  # type: str
        self.rolename = rolename  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateSlrPermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.rolename is not None:
            result['rolename'] = self.rolename
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('rolename') is not None:
            self.rolename = m.get('rolename')
        return self


class ValidateSlrPermissionResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateSlrPermissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValidateSlrPermissionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ValidateSlrPermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateSlrPermissionResponse, self).to_map()
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
            temp_model = ValidateSlrPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateTransferableNodesRequest(TeaModel):
    def __init__(self, node_type=None):
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateTransferableNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        return self


class ValidateTransferableNodesResponseBody(TeaModel):
    def __init__(self, result=None, request_id=None):
        self.result = result  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateTransferableNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValidateTransferableNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ValidateTransferableNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateTransferableNodesResponse, self).to_map()
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
            temp_model = ValidateTransferableNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


