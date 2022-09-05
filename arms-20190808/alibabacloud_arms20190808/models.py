# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CallChainInfo(TeaModel):
    def __init__(self, additional_info=None, app_name=None, app_type=None, children=None, have_span=None,
                 log_map=None, log_time=None, parent_span_id=None, pid=None, region_id=None, result_code=None, rpc=None,
                 rpc_id=None, rpc_type=None, server_ip=None, span=None, span_id=None, tag_map=None, trace_id=None):
        self.additional_info = additional_info  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.children = children  # type: list[CallChainInfo]
        self.have_span = have_span  # type: bool
        self.log_map = log_map  # type: dict[str, dict]
        self.log_time = log_time  # type: long
        self.parent_span_id = parent_span_id  # type: str
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.result_code = result_code  # type: str
        self.rpc = rpc  # type: str
        self.rpc_id = rpc_id  # type: str
        self.rpc_type = rpc_type  # type: long
        self.server_ip = server_ip  # type: str
        self.span = span  # type: long
        self.span_id = span_id  # type: str
        self.tag_map = tag_map  # type: dict[str, str]
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CallChainInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_info is not None:
            result['AdditionalInfo'] = self.additional_info
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        result['Children'] = []
        if self.children is not None:
            for k in self.children:
                result['Children'].append(k.to_map() if k else None)
        if self.have_span is not None:
            result['HaveSpan'] = self.have_span
        if self.log_map is not None:
            result['LogMap'] = self.log_map
        if self.log_time is not None:
            result['LogTime'] = self.log_time
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.rpc is not None:
            result['Rpc'] = self.rpc
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.span is not None:
            result['Span'] = self.span
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        if self.tag_map is not None:
            result['TagMap'] = self.tag_map
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionalInfo') is not None:
            self.additional_info = m.get('AdditionalInfo')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        self.children = []
        if m.get('Children') is not None:
            for k in m.get('Children'):
                temp_model = CallChainInfo()
                self.children.append(temp_model.from_map(k))
        if m.get('HaveSpan') is not None:
            self.have_span = m.get('HaveSpan')
        if m.get('LogMap') is not None:
            self.log_map = m.get('LogMap')
        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('Rpc') is not None:
            self.rpc = m.get('Rpc')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Span') is not None:
            self.span = m.get('Span')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        if m.get('TagMap') is not None:
            self.tag_map = m.get('TagMap')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class AddAliClusterIdsToPrometheusGlobalViewRequest(TeaModel):
    def __init__(self, cluster_ids=None, global_view_cluster_id=None, group_name=None, region_id=None):
        self.cluster_ids = cluster_ids  # type: str
        self.global_view_cluster_id = global_view_cluster_id  # type: str
        self.group_name = group_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAliClusterIdsToPrometheusGlobalViewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddAliClusterIdsToPrometheusGlobalViewResponseBodyData(TeaModel):
    def __init__(self, info=None, msg=None, success=None):
        self.info = info  # type: str
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAliClusterIdsToPrometheusGlobalViewResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAliClusterIdsToPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AddAliClusterIdsToPrometheusGlobalViewResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddAliClusterIdsToPrometheusGlobalViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AddAliClusterIdsToPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddAliClusterIdsToPrometheusGlobalViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddAliClusterIdsToPrometheusGlobalViewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAliClusterIdsToPrometheusGlobalViewResponse, self).to_map()
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
            temp_model = AddAliClusterIdsToPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGrafanaRequest(TeaModel):
    def __init__(self, cluster_id=None, integration=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.integration = integration  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGrafanaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddGrafanaResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGrafanaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddGrafanaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddGrafanaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGrafanaResponse, self).to_map()
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
            temp_model = AddGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddIntegrationRequest(TeaModel):
    def __init__(self, cluster_id=None, integration=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.integration = integration  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIntegrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddIntegrationResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIntegrationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddIntegrationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddIntegrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddIntegrationResponse, self).to_map()
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
            temp_model = AddIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddPrometheusGlobalViewRequest(TeaModel):
    def __init__(self, clusters=None, group_name=None, region_id=None):
        self.clusters = clusters  # type: str
        self.group_name = group_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddPrometheusGlobalViewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddPrometheusGlobalViewResponseBodyData(TeaModel):
    def __init__(self, info=None, msg=None, success=None):
        self.info = info  # type: str
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddPrometheusGlobalViewResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AddPrometheusGlobalViewResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddPrometheusGlobalViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AddPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddPrometheusGlobalViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddPrometheusGlobalViewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddPrometheusGlobalViewResponse, self).to_map()
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
            temp_model = AddPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddPrometheusGlobalViewByAliClusterIdsRequest(TeaModel):
    def __init__(self, cluster_ids=None, group_name=None, product_code=None, region_id=None):
        self.cluster_ids = cluster_ids  # type: str
        self.group_name = group_name  # type: str
        self.product_code = product_code  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddPrometheusGlobalViewByAliClusterIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddPrometheusGlobalViewByAliClusterIdsResponseBodyData(TeaModel):
    def __init__(self, info=None, msg=None, success=None):
        self.info = info  # type: str
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddPrometheusGlobalViewByAliClusterIdsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddPrometheusGlobalViewByAliClusterIdsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AddPrometheusGlobalViewByAliClusterIdsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddPrometheusGlobalViewByAliClusterIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AddPrometheusGlobalViewByAliClusterIdsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddPrometheusGlobalViewByAliClusterIdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddPrometheusGlobalViewByAliClusterIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddPrometheusGlobalViewByAliClusterIdsResponse, self).to_map()
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
            temp_model = AddPrometheusGlobalViewByAliClusterIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddPrometheusInstanceRequest(TeaModel):
    def __init__(self, name=None, region_id=None, type=None):
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddPrometheusInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddPrometheusInstanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddPrometheusInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddPrometheusInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddPrometheusInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddPrometheusInstanceResponse, self).to_map()
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
            temp_model = AddPrometheusInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRecordingRuleRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None, rule_yaml=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str
        self.rule_yaml = rule_yaml  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRecordingRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_yaml is not None:
            result['RuleYaml'] = self.rule_yaml
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleYaml') is not None:
            self.rule_yaml = m.get('RuleYaml')
        return self


class AddRecordingRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRecordingRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddRecordingRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddRecordingRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRecordingRuleResponse, self).to_map()
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
            temp_model = AddRecordingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppendInstancesToPrometheusGlobalViewRequest(TeaModel):
    def __init__(self, clusters=None, global_view_cluster_id=None, group_name=None, region_id=None):
        self.clusters = clusters  # type: str
        self.global_view_cluster_id = global_view_cluster_id  # type: str
        self.group_name = group_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppendInstancesToPrometheusGlobalViewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AppendInstancesToPrometheusGlobalViewResponseBodyData(TeaModel):
    def __init__(self, info=None, msg=None, success=None):
        self.info = info  # type: str
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppendInstancesToPrometheusGlobalViewResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AppendInstancesToPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: AppendInstancesToPrometheusGlobalViewResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppendInstancesToPrometheusGlobalViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AppendInstancesToPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppendInstancesToPrometheusGlobalViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AppendInstancesToPrometheusGlobalViewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppendInstancesToPrometheusGlobalViewResponse, self).to_map()
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
            temp_model = AppendInstancesToPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyScenarioRequest(TeaModel):
    def __init__(self, app_id=None, config=None, name=None, region_id=None, scenario=None, sign=None, sn_dump=None,
                 sn_force=None, sn_stat=None, sn_transfer=None, update_option=None):
        self.app_id = app_id  # type: str
        self.config = config  # type: dict[str, any]
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.scenario = scenario  # type: str
        self.sign = sign  # type: str
        self.sn_dump = sn_dump  # type: bool
        self.sn_force = sn_force  # type: bool
        self.sn_stat = sn_stat  # type: bool
        self.sn_transfer = sn_transfer  # type: bool
        self.update_option = update_option  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyScenarioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.sn_dump is not None:
            result['SnDump'] = self.sn_dump
        if self.sn_force is not None:
            result['SnForce'] = self.sn_force
        if self.sn_stat is not None:
            result['SnStat'] = self.sn_stat
        if self.sn_transfer is not None:
            result['SnTransfer'] = self.sn_transfer
        if self.update_option is not None:
            result['UpdateOption'] = self.update_option
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SnDump') is not None:
            self.sn_dump = m.get('SnDump')
        if m.get('SnForce') is not None:
            self.sn_force = m.get('SnForce')
        if m.get('SnStat') is not None:
            self.sn_stat = m.get('SnStat')
        if m.get('SnTransfer') is not None:
            self.sn_transfer = m.get('SnTransfer')
        if m.get('UpdateOption') is not None:
            self.update_option = m.get('UpdateOption')
        return self


class ApplyScenarioShrinkRequest(TeaModel):
    def __init__(self, app_id=None, config_shrink=None, name=None, region_id=None, scenario=None, sign=None,
                 sn_dump=None, sn_force=None, sn_stat=None, sn_transfer=None, update_option=None):
        self.app_id = app_id  # type: str
        self.config_shrink = config_shrink  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.scenario = scenario  # type: str
        self.sign = sign  # type: str
        self.sn_dump = sn_dump  # type: bool
        self.sn_force = sn_force  # type: bool
        self.sn_stat = sn_stat  # type: bool
        self.sn_transfer = sn_transfer  # type: bool
        self.update_option = update_option  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyScenarioShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.sn_dump is not None:
            result['SnDump'] = self.sn_dump
        if self.sn_force is not None:
            result['SnForce'] = self.sn_force
        if self.sn_stat is not None:
            result['SnStat'] = self.sn_stat
        if self.sn_transfer is not None:
            result['SnTransfer'] = self.sn_transfer
        if self.update_option is not None:
            result['UpdateOption'] = self.update_option
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SnDump') is not None:
            self.sn_dump = m.get('SnDump')
        if m.get('SnForce') is not None:
            self.sn_force = m.get('SnForce')
        if m.get('SnStat') is not None:
            self.sn_stat = m.get('SnStat')
        if m.get('SnTransfer') is not None:
            self.sn_transfer = m.get('SnTransfer')
        if m.get('UpdateOption') is not None:
            self.update_option = m.get('UpdateOption')
        return self


class ApplyScenarioResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyScenarioResponseBody, self).to_map()
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


class ApplyScenarioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyScenarioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyScenarioResponse, self).to_map()
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
            temp_model = ApplyScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceStatusRequest(TeaModel):
    def __init__(self, region_id=None, svc_code=None):
        self.region_id = region_id  # type: str
        self.svc_code = svc_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.svc_code is not None:
            result['SvcCode'] = self.svc_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SvcCode') is not None:
            self.svc_code = m.get('SvcCode')
        return self


class CheckServiceStatusResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckServiceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckServiceStatusResponse, self).to_map()
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
            temp_model = CheckServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigAppRequest(TeaModel):
    def __init__(self, app_ids=None, enable=None, region_id=None):
        self.app_ids = app_ids  # type: str
        self.enable = enable  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigAppResponse, self).to_map()
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
            temp_model = ConfigAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlertContactRequest(TeaModel):
    def __init__(self, contact_name=None, ding_robot_webhook_url=None, email=None, phone_num=None, region_id=None,
                 system_noc=None):
        self.contact_name = contact_name  # type: str
        self.ding_robot_webhook_url = ding_robot_webhook_url  # type: str
        self.email = email  # type: str
        self.phone_num = phone_num  # type: str
        self.region_id = region_id  # type: str
        self.system_noc = system_noc  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlertContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.ding_robot_webhook_url is not None:
            result['DingRobotWebhookUrl'] = self.ding_robot_webhook_url
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('DingRobotWebhookUrl') is not None:
            self.ding_robot_webhook_url = m.get('DingRobotWebhookUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        return self


class CreateAlertContactResponseBody(TeaModel):
    def __init__(self, contact_id=None, request_id=None):
        self.contact_id = contact_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlertContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAlertContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAlertContactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlertContactResponse, self).to_map()
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
            temp_model = CreateAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlertContactGroupRequest(TeaModel):
    def __init__(self, contact_group_name=None, contact_ids=None, region_id=None):
        self.contact_group_name = contact_group_name  # type: str
        self.contact_ids = contact_ids  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlertContactGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateAlertContactGroupResponseBody(TeaModel):
    def __init__(self, contact_group_id=None, request_id=None):
        self.contact_group_id = contact_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlertContactGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAlertContactGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAlertContactGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlertContactGroupResponse, self).to_map()
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
            temp_model = CreateAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDispatchRuleRequest(TeaModel):
    def __init__(self, dispatch_rule=None, region_id=None):
        self.dispatch_rule = dispatch_rule  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDispatchRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            self.dispatch_rule = m.get('DispatchRule')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateDispatchRuleResponseBody(TeaModel):
    def __init__(self, dispatch_rule_id=None, request_id=None):
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDispatchRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDispatchRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDispatchRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDispatchRuleResponse, self).to_map()
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
            temp_model = CreateDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntegrationRequest(TeaModel):
    def __init__(self, auto_recover=None, description=None, integration_name=None, integration_product_type=None,
                 recover_time=None):
        self.auto_recover = auto_recover  # type: bool
        self.description = description  # type: str
        self.integration_name = integration_name  # type: str
        self.integration_product_type = integration_product_type  # type: str
        self.recover_time = recover_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntegrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_recover is not None:
            result['AutoRecover'] = self.auto_recover
        if self.description is not None:
            result['Description'] = self.description
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_product_type is not None:
            result['IntegrationProductType'] = self.integration_product_type
        if self.recover_time is not None:
            result['RecoverTime'] = self.recover_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRecover') is not None:
            self.auto_recover = m.get('AutoRecover')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationProductType') is not None:
            self.integration_product_type = m.get('IntegrationProductType')
        if m.get('RecoverTime') is not None:
            self.recover_time = m.get('RecoverTime')
        return self


class CreateIntegrationResponseBodyIntegration(TeaModel):
    def __init__(self, auto_recover=None, description=None, integration_id=None, integration_name=None,
                 integration_product_type=None, recover_time=None):
        self.auto_recover = auto_recover  # type: bool
        self.description = description  # type: str
        self.integration_id = integration_id  # type: long
        self.integration_name = integration_name  # type: str
        self.integration_product_type = integration_product_type  # type: str
        self.recover_time = recover_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntegrationResponseBodyIntegration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_recover is not None:
            result['AutoRecover'] = self.auto_recover
        if self.description is not None:
            result['Description'] = self.description
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_product_type is not None:
            result['IntegrationProductType'] = self.integration_product_type
        if self.recover_time is not None:
            result['RecoverTime'] = self.recover_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRecover') is not None:
            self.auto_recover = m.get('AutoRecover')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationProductType') is not None:
            self.integration_product_type = m.get('IntegrationProductType')
        if m.get('RecoverTime') is not None:
            self.recover_time = m.get('RecoverTime')
        return self


class CreateIntegrationResponseBody(TeaModel):
    def __init__(self, integration=None, request_id=None):
        self.integration = integration  # type: CreateIntegrationResponseBodyIntegration
        self.request_id = request_id  # type: str

    def validate(self):
        if self.integration:
            self.integration.validate()

    def to_map(self):
        _map = super(CreateIntegrationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.integration is not None:
            result['Integration'] = self.integration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Integration') is not None:
            temp_model = CreateIntegrationResponseBodyIntegration()
            self.integration = temp_model.from_map(m['Integration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIntegrationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIntegrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIntegrationResponse, self).to_map()
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
            temp_model = CreateIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateAlertRuleRequest(TeaModel):
    def __init__(self, alert_check_type=None, alert_group=None, alert_id=None, alert_name=None,
                 alert_rule_content=None, alert_status=None, alert_type=None, annotations=None, auto_add_new_application=None,
                 cluster_id=None, duration=None, filters=None, labels=None, level=None, message=None, metrics_key=None,
                 metrics_type=None, notify_strategy=None, pids=None, prom_ql=None, region_id=None):
        self.alert_check_type = alert_check_type  # type: str
        self.alert_group = alert_group  # type: long
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.alert_rule_content = alert_rule_content  # type: str
        self.alert_status = alert_status  # type: str
        self.alert_type = alert_type  # type: str
        self.annotations = annotations  # type: str
        self.auto_add_new_application = auto_add_new_application  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.duration = duration  # type: long
        self.filters = filters  # type: str
        self.labels = labels  # type: str
        self.level = level  # type: str
        self.message = message  # type: str
        self.metrics_key = metrics_key  # type: str
        self.metrics_type = metrics_type  # type: str
        self.notify_strategy = notify_strategy  # type: str
        self.pids = pids  # type: str
        self.prom_ql = prom_ql  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_check_type is not None:
            result['AlertCheckType'] = self.alert_check_type
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_rule_content is not None:
            result['AlertRuleContent'] = self.alert_rule_content
        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.auto_add_new_application is not None:
            result['AutoAddNewApplication'] = self.auto_add_new_application
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.metrics_key is not None:
            result['MetricsKey'] = self.metrics_key
        if self.metrics_type is not None:
            result['MetricsType'] = self.metrics_type
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.pids is not None:
            result['Pids'] = self.pids
        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertCheckType') is not None:
            self.alert_check_type = m.get('AlertCheckType')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertRuleContent') is not None:
            self.alert_rule_content = m.get('AlertRuleContent')
        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('AutoAddNewApplication') is not None:
            self.auto_add_new_application = m.get('AutoAddNewApplication')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MetricsKey') is not None:
            self.metrics_key = m.get('MetricsKey')
        if m.get('MetricsType') is not None:
            self.metrics_type = m.get('MetricsType')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContentAlertRuleItems(TeaModel):
    def __init__(self, aggregate=None, metric_key=None, n=None, operator=None, value=None):
        self.aggregate = aggregate  # type: str
        self.metric_key = metric_key  # type: str
        self.n = n  # type: float
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContentAlertRuleItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregate is not None:
            result['Aggregate'] = self.aggregate
        if self.metric_key is not None:
            result['MetricKey'] = self.metric_key
        if self.n is not None:
            result['N'] = self.n
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aggregate') is not None:
            self.aggregate = m.get('Aggregate')
        if m.get('MetricKey') is not None:
            self.metric_key = m.get('MetricKey')
        if m.get('N') is not None:
            self.n = m.get('N')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContent(TeaModel):
    def __init__(self, alert_rule_items=None, condition=None):
        self.alert_rule_items = alert_rule_items  # type: list[CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContentAlertRuleItems]
        self.condition = condition  # type: str

    def validate(self):
        if self.alert_rule_items:
            for k in self.alert_rule_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertRuleItems'] = []
        if self.alert_rule_items is not None:
            for k in self.alert_rule_items:
                result['AlertRuleItems'].append(k.to_map() if k else None)
        if self.condition is not None:
            result['Condition'] = self.condition
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alert_rule_items = []
        if m.get('AlertRuleItems') is not None:
            for k in m.get('AlertRuleItems'):
                temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContentAlertRuleItems()
                self.alert_rule_items.append(temp_model.from_map(k))
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleResponseBodyAlertRuleAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersCustomSLSFilters(TeaModel):
    def __init__(self, key=None, opt=None, show=None, t=None, value=None):
        self.key = key  # type: str
        self.opt = opt  # type: str
        self.show = show  # type: bool
        self.t = t  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersCustomSLSFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.opt is not None:
            result['Opt'] = self.opt
        if self.show is not None:
            result['Show'] = self.show
        if self.t is not None:
            result['T'] = self.t
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Opt') is not None:
            self.opt = m.get('Opt')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('T') is not None:
            self.t = m.get('T')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersDimFilters(TeaModel):
    def __init__(self, filter_key=None, filter_opt=None, filter_values=None):
        self.filter_key = filter_key  # type: str
        self.filter_opt = filter_opt  # type: str
        self.filter_values = filter_values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersDimFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_opt is not None:
            result['FilterOpt'] = self.filter_opt
        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterOpt') is not None:
            self.filter_opt = m.get('FilterOpt')
        if m.get('FilterValues') is not None:
            self.filter_values = m.get('FilterValues')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleFilters(TeaModel):
    def __init__(self, custom_slsfilters=None, custom_slsgroup_by_dimensions=None, custom_slswheres=None,
                 dim_filters=None):
        self.custom_slsfilters = custom_slsfilters  # type: list[CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersCustomSLSFilters]
        self.custom_slsgroup_by_dimensions = custom_slsgroup_by_dimensions  # type: list[str]
        self.custom_slswheres = custom_slswheres  # type: list[str]
        self.dim_filters = dim_filters  # type: list[CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersDimFilters]

    def validate(self):
        if self.custom_slsfilters:
            for k in self.custom_slsfilters:
                if k:
                    k.validate()
        if self.dim_filters:
            for k in self.dim_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleResponseBodyAlertRuleFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomSLSFilters'] = []
        if self.custom_slsfilters is not None:
            for k in self.custom_slsfilters:
                result['CustomSLSFilters'].append(k.to_map() if k else None)
        if self.custom_slsgroup_by_dimensions is not None:
            result['CustomSLSGroupByDimensions'] = self.custom_slsgroup_by_dimensions
        if self.custom_slswheres is not None:
            result['CustomSLSWheres'] = self.custom_slswheres
        result['DimFilters'] = []
        if self.dim_filters is not None:
            for k in self.dim_filters:
                result['DimFilters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_slsfilters = []
        if m.get('CustomSLSFilters') is not None:
            for k in m.get('CustomSLSFilters'):
                temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersCustomSLSFilters()
                self.custom_slsfilters.append(temp_model.from_map(k))
        if m.get('CustomSLSGroupByDimensions') is not None:
            self.custom_slsgroup_by_dimensions = m.get('CustomSLSGroupByDimensions')
        if m.get('CustomSLSWheres') is not None:
            self.custom_slswheres = m.get('CustomSLSWheres')
        self.dim_filters = []
        if m.get('DimFilters') is not None:
            for k in m.get('DimFilters'):
                temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersDimFilters()
                self.dim_filters.append(temp_model.from_map(k))
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleResponseBodyAlertRuleLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRule(TeaModel):
    def __init__(self, alert_check_type=None, alert_group=None, alert_id=None, alert_name=None,
                 alert_rule_content=None, alert_status=None, alert_type=None, annotations=None, auto_add_new_application=None,
                 cluster_id=None, created_time=None, duration=None, extend=None, filters=None, labels=None, level=None,
                 message=None, metrics_type=None, notify_strategy=None, pids=None, prom_ql=None, region_id=None,
                 updated_time=None, user_id=None):
        self.alert_check_type = alert_check_type  # type: str
        self.alert_group = alert_group  # type: long
        self.alert_id = alert_id  # type: float
        self.alert_name = alert_name  # type: str
        self.alert_rule_content = alert_rule_content  # type: CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContent
        self.alert_status = alert_status  # type: str
        self.alert_type = alert_type  # type: str
        self.annotations = annotations  # type: list[CreateOrUpdateAlertRuleResponseBodyAlertRuleAnnotations]
        self.auto_add_new_application = auto_add_new_application  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.created_time = created_time  # type: long
        self.duration = duration  # type: str
        self.extend = extend  # type: str
        self.filters = filters  # type: CreateOrUpdateAlertRuleResponseBodyAlertRuleFilters
        self.labels = labels  # type: list[CreateOrUpdateAlertRuleResponseBodyAlertRuleLabels]
        self.level = level  # type: str
        self.message = message  # type: str
        self.metrics_type = metrics_type  # type: str
        self.notify_strategy = notify_strategy  # type: str
        self.pids = pids  # type: list[str]
        self.prom_ql = prom_ql  # type: str
        self.region_id = region_id  # type: str
        self.updated_time = updated_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        if self.alert_rule_content:
            self.alert_rule_content.validate()
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.filters:
            self.filters.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleResponseBodyAlertRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_check_type is not None:
            result['AlertCheckType'] = self.alert_check_type
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_rule_content is not None:
            result['AlertRuleContent'] = self.alert_rule_content.to_map()
        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.auto_add_new_application is not None:
            result['AutoAddNewApplication'] = self.auto_add_new_application
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.filters is not None:
            result['Filters'] = self.filters.to_map()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.metrics_type is not None:
            result['MetricsType'] = self.metrics_type
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.pids is not None:
            result['Pids'] = self.pids
        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertCheckType') is not None:
            self.alert_check_type = m.get('AlertCheckType')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertRuleContent') is not None:
            temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContent()
            self.alert_rule_content = temp_model.from_map(m['AlertRuleContent'])
        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('AutoAddNewApplication') is not None:
            self.auto_add_new_application = m.get('AutoAddNewApplication')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Filters') is not None:
            temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleFilters()
            self.filters = temp_model.from_map(m['Filters'])
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MetricsType') is not None:
            self.metrics_type = m.get('MetricsType')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateOrUpdateAlertRuleResponseBody(TeaModel):
    def __init__(self, alert_rule=None, request_id=None):
        self.alert_rule = alert_rule  # type: CreateOrUpdateAlertRuleResponseBodyAlertRule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.alert_rule:
            self.alert_rule.validate()

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertRule') is not None:
            temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRule()
            self.alert_rule = temp_model.from_map(m['AlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOrUpdateAlertRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrUpdateAlertRuleResponse, self).to_map()
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
            temp_model = CreateOrUpdateAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateContactRequest(TeaModel):
    def __init__(self, contact_id=None, contact_name=None, email=None, phone=None, reissue_send_notice=None):
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.email = email  # type: str
        self.phone = phone  # type: str
        self.reissue_send_notice = reissue_send_notice  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.reissue_send_notice is not None:
            result['ReissueSendNotice'] = self.reissue_send_notice
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ReissueSendNotice') is not None:
            self.reissue_send_notice = m.get('ReissueSendNotice')
        return self


class CreateOrUpdateContactResponseBodyAlertContact(TeaModel):
    def __init__(self, contact_id=None, contact_name=None, email=None, is_verify=None, phone=None,
                 reissue_send_notice=None):
        self.contact_id = contact_id  # type: float
        self.contact_name = contact_name  # type: str
        self.email = email  # type: str
        self.is_verify = is_verify  # type: bool
        self.phone = phone  # type: str
        self.reissue_send_notice = reissue_send_notice  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateContactResponseBodyAlertContact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.is_verify is not None:
            result['IsVerify'] = self.is_verify
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.reissue_send_notice is not None:
            result['ReissueSendNotice'] = self.reissue_send_notice
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IsVerify') is not None:
            self.is_verify = m.get('IsVerify')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ReissueSendNotice') is not None:
            self.reissue_send_notice = m.get('ReissueSendNotice')
        return self


class CreateOrUpdateContactResponseBody(TeaModel):
    def __init__(self, alert_contact=None, request_id=None):
        self.alert_contact = alert_contact  # type: CreateOrUpdateContactResponseBodyAlertContact
        self.request_id = request_id  # type: str

    def validate(self):
        if self.alert_contact:
            self.alert_contact.validate()

    def to_map(self):
        _map = super(CreateOrUpdateContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_contact is not None:
            result['AlertContact'] = self.alert_contact.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertContact') is not None:
            temp_model = CreateOrUpdateContactResponseBodyAlertContact()
            self.alert_contact = temp_model.from_map(m['AlertContact'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOrUpdateContactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrUpdateContactResponse, self).to_map()
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
            temp_model = CreateOrUpdateContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateContactGroupRequest(TeaModel):
    def __init__(self, contact_group_id=None, contact_group_name=None, contact_ids=None):
        self.contact_group_id = contact_group_id  # type: long
        self.contact_group_name = contact_group_name  # type: str
        self.contact_ids = contact_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateContactGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        return self


class CreateOrUpdateContactGroupResponseBodyAlertContactGroup(TeaModel):
    def __init__(self, contact_group_id=None, contact_group_name=None, contact_ids=None):
        self.contact_group_id = contact_group_id  # type: float
        self.contact_group_name = contact_group_name  # type: str
        self.contact_ids = contact_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateContactGroupResponseBodyAlertContactGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        return self


class CreateOrUpdateContactGroupResponseBody(TeaModel):
    def __init__(self, alert_contact_group=None, request_id=None):
        self.alert_contact_group = alert_contact_group  # type: CreateOrUpdateContactGroupResponseBodyAlertContactGroup
        self.request_id = request_id  # type: str

    def validate(self):
        if self.alert_contact_group:
            self.alert_contact_group.validate()

    def to_map(self):
        _map = super(CreateOrUpdateContactGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_contact_group is not None:
            result['AlertContactGroup'] = self.alert_contact_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertContactGroup') is not None:
            temp_model = CreateOrUpdateContactGroupResponseBodyAlertContactGroup()
            self.alert_contact_group = temp_model.from_map(m['AlertContactGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateContactGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOrUpdateContactGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrUpdateContactGroupResponse, self).to_map()
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
            temp_model = CreateOrUpdateContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateEventBridgeIntegrationRequest(TeaModel):
    def __init__(self, access_key=None, access_secret=None, description=None, endpoint=None, event_bus_name=None,
                 event_bus_region_id=None, id=None, name=None, source=None):
        self.access_key = access_key  # type: str
        self.access_secret = access_secret  # type: str
        self.description = description  # type: str
        self.endpoint = endpoint  # type: str
        self.event_bus_name = event_bus_name  # type: str
        self.event_bus_region_id = event_bus_region_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateEventBridgeIntegrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_bus_region_id is not None:
            result['EventBusRegionId'] = self.event_bus_region_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventBusRegionId') is not None:
            self.event_bus_region_id = m.get('EventBusRegionId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateOrUpdateEventBridgeIntegrationResponseBodyEventBridgeIntegration(TeaModel):
    def __init__(self, access_key=None, access_secret=None, description=None, endpoint=None, event_bus_name=None,
                 event_bus_region_id=None, id=None, name=None, source=None):
        self.access_key = access_key  # type: str
        self.access_secret = access_secret  # type: str
        self.description = description  # type: str
        self.endpoint = endpoint  # type: str
        self.event_bus_name = event_bus_name  # type: str
        self.event_bus_region_id = event_bus_region_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateEventBridgeIntegrationResponseBodyEventBridgeIntegration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_bus_region_id is not None:
            result['EventBusRegionId'] = self.event_bus_region_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventBusRegionId') is not None:
            self.event_bus_region_id = m.get('EventBusRegionId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateOrUpdateEventBridgeIntegrationResponseBody(TeaModel):
    def __init__(self, event_bridge_integration=None, request_id=None):
        self.event_bridge_integration = event_bridge_integration  # type: CreateOrUpdateEventBridgeIntegrationResponseBodyEventBridgeIntegration
        self.request_id = request_id  # type: str

    def validate(self):
        if self.event_bridge_integration:
            self.event_bridge_integration.validate()

    def to_map(self):
        _map = super(CreateOrUpdateEventBridgeIntegrationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bridge_integration is not None:
            result['EventBridgeIntegration'] = self.event_bridge_integration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventBridgeIntegration') is not None:
            temp_model = CreateOrUpdateEventBridgeIntegrationResponseBodyEventBridgeIntegration()
            self.event_bridge_integration = temp_model.from_map(m['EventBridgeIntegration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateEventBridgeIntegrationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOrUpdateEventBridgeIntegrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrUpdateEventBridgeIntegrationResponse, self).to_map()
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
            temp_model = CreateOrUpdateEventBridgeIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateIMRobotRequest(TeaModel):
    def __init__(self, card_template=None, daily_noc=None, daily_noc_time=None, enable_outgoing=None,
                 robot_address=None, robot_id=None, robot_name=None, token=None, type=None):
        self.card_template = card_template  # type: str
        self.daily_noc = daily_noc  # type: bool
        self.daily_noc_time = daily_noc_time  # type: str
        self.enable_outgoing = enable_outgoing  # type: bool
        self.robot_address = robot_address  # type: str
        self.robot_id = robot_id  # type: long
        self.robot_name = robot_name  # type: str
        self.token = token  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateIMRobotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_template is not None:
            result['CardTemplate'] = self.card_template
        if self.daily_noc is not None:
            result['DailyNoc'] = self.daily_noc
        if self.daily_noc_time is not None:
            result['DailyNocTime'] = self.daily_noc_time
        if self.enable_outgoing is not None:
            result['EnableOutgoing'] = self.enable_outgoing
        if self.robot_address is not None:
            result['RobotAddress'] = self.robot_address
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardTemplate') is not None:
            self.card_template = m.get('CardTemplate')
        if m.get('DailyNoc') is not None:
            self.daily_noc = m.get('DailyNoc')
        if m.get('DailyNocTime') is not None:
            self.daily_noc_time = m.get('DailyNocTime')
        if m.get('EnableOutgoing') is not None:
            self.enable_outgoing = m.get('EnableOutgoing')
        if m.get('RobotAddress') is not None:
            self.robot_address = m.get('RobotAddress')
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateOrUpdateIMRobotResponseBodyAlertRobot(TeaModel):
    def __init__(self, card_template=None, daily_noc=None, daily_noc_time=None, enable_outgoing=None,
                 robot_address=None, robot_id=None, robot_name=None, token=None, type=None):
        self.card_template = card_template  # type: str
        self.daily_noc = daily_noc  # type: bool
        self.daily_noc_time = daily_noc_time  # type: str
        self.enable_outgoing = enable_outgoing  # type: bool
        self.robot_address = robot_address  # type: str
        self.robot_id = robot_id  # type: float
        self.robot_name = robot_name  # type: str
        self.token = token  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateIMRobotResponseBodyAlertRobot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_template is not None:
            result['CardTemplate'] = self.card_template
        if self.daily_noc is not None:
            result['DailyNoc'] = self.daily_noc
        if self.daily_noc_time is not None:
            result['DailyNocTime'] = self.daily_noc_time
        if self.enable_outgoing is not None:
            result['EnableOutgoing'] = self.enable_outgoing
        if self.robot_address is not None:
            result['RobotAddress'] = self.robot_address
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardTemplate') is not None:
            self.card_template = m.get('CardTemplate')
        if m.get('DailyNoc') is not None:
            self.daily_noc = m.get('DailyNoc')
        if m.get('DailyNocTime') is not None:
            self.daily_noc_time = m.get('DailyNocTime')
        if m.get('EnableOutgoing') is not None:
            self.enable_outgoing = m.get('EnableOutgoing')
        if m.get('RobotAddress') is not None:
            self.robot_address = m.get('RobotAddress')
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateOrUpdateIMRobotResponseBody(TeaModel):
    def __init__(self, alert_robot=None, request_id=None):
        self.alert_robot = alert_robot  # type: CreateOrUpdateIMRobotResponseBodyAlertRobot
        self.request_id = request_id  # type: str

    def validate(self):
        if self.alert_robot:
            self.alert_robot.validate()

    def to_map(self):
        _map = super(CreateOrUpdateIMRobotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_robot is not None:
            result['AlertRobot'] = self.alert_robot.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertRobot') is not None:
            temp_model = CreateOrUpdateIMRobotResponseBodyAlertRobot()
            self.alert_robot = temp_model.from_map(m['AlertRobot'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateIMRobotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOrUpdateIMRobotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrUpdateIMRobotResponse, self).to_map()
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
            temp_model = CreateOrUpdateIMRobotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateNotificationPolicyRequest(TeaModel):
    def __init__(self, escalation_policy_id=None, group_rule=None, id=None, integration_id=None,
                 matching_rules=None, name=None, notify_rule=None, notify_template=None, region_id=None, repeat=None,
                 repeat_interval=None, send_recover_message=None):
        self.escalation_policy_id = escalation_policy_id  # type: long
        self.group_rule = group_rule  # type: str
        self.id = id  # type: long
        self.integration_id = integration_id  # type: long
        self.matching_rules = matching_rules  # type: str
        self.name = name  # type: str
        self.notify_rule = notify_rule  # type: str
        self.notify_template = notify_template  # type: str
        self.region_id = region_id  # type: str
        self.repeat = repeat  # type: bool
        self.repeat_interval = repeat_interval  # type: long
        self.send_recover_message = send_recover_message  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateNotificationPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_policy_id is not None:
            result['EscalationPolicyId'] = self.escalation_policy_id
        if self.group_rule is not None:
            result['GroupRule'] = self.group_rule
        if self.id is not None:
            result['Id'] = self.id
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        if self.matching_rules is not None:
            result['MatchingRules'] = self.matching_rules
        if self.name is not None:
            result['Name'] = self.name
        if self.notify_rule is not None:
            result['NotifyRule'] = self.notify_rule
        if self.notify_template is not None:
            result['NotifyTemplate'] = self.notify_template
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat is not None:
            result['Repeat'] = self.repeat
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        if self.send_recover_message is not None:
            result['SendRecoverMessage'] = self.send_recover_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EscalationPolicyId') is not None:
            self.escalation_policy_id = m.get('EscalationPolicyId')
        if m.get('GroupRule') is not None:
            self.group_rule = m.get('GroupRule')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        if m.get('MatchingRules') is not None:
            self.matching_rules = m.get('MatchingRules')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotifyRule') is not None:
            self.notify_rule = m.get('NotifyRule')
        if m.get('NotifyTemplate') is not None:
            self.notify_template = m.get('NotifyTemplate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Repeat') is not None:
            self.repeat = m.get('Repeat')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        if m.get('SendRecoverMessage') is not None:
            self.send_recover_message = m.get('SendRecoverMessage')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyGroupRule(TeaModel):
    def __init__(self, group_interval=None, group_wait=None, grouping_fields=None):
        self.group_interval = group_interval  # type: long
        self.group_wait = group_wait  # type: long
        self.grouping_fields = grouping_fields  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyGroupRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_interval is not None:
            result['GroupInterval'] = self.group_interval
        if self.group_wait is not None:
            result['GroupWait'] = self.group_wait
        if self.grouping_fields is not None:
            result['GroupingFields'] = self.grouping_fields
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupInterval') is not None:
            self.group_interval = m.get('GroupInterval')
        if m.get('GroupWait') is not None:
            self.group_wait = m.get('GroupWait')
        if m.get('GroupingFields') is not None:
            self.grouping_fields = m.get('GroupingFields')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRulesMatchingConditions(TeaModel):
    def __init__(self, key=None, operator=None, value=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRulesMatchingConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRules(TeaModel):
    def __init__(self, matching_conditions=None):
        self.matching_conditions = matching_conditions  # type: list[CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRulesMatchingConditions]

    def validate(self):
        if self.matching_conditions:
            for k in self.matching_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchingConditions'] = []
        if self.matching_conditions is not None:
            for k in self.matching_conditions:
                result['MatchingConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.matching_conditions = []
        if m.get('MatchingConditions') is not None:
            for k in m.get('MatchingConditions'):
                temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k))
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRuleNotifyObjects(TeaModel):
    def __init__(self, notify_object_id=None, notify_object_name=None, notify_object_type=None):
        self.notify_object_id = notify_object_id  # type: long
        self.notify_object_name = notify_object_name  # type: str
        self.notify_object_type = notify_object_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRuleNotifyObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_object_id is not None:
            result['NotifyObjectId'] = self.notify_object_id
        if self.notify_object_name is not None:
            result['NotifyObjectName'] = self.notify_object_name
        if self.notify_object_type is not None:
            result['NotifyObjectType'] = self.notify_object_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotifyObjectId') is not None:
            self.notify_object_id = m.get('NotifyObjectId')
        if m.get('NotifyObjectName') is not None:
            self.notify_object_name = m.get('NotifyObjectName')
        if m.get('NotifyObjectType') is not None:
            self.notify_object_type = m.get('NotifyObjectType')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRule(TeaModel):
    def __init__(self, notify_channels=None, notify_end_time=None, notify_objects=None, notify_start_time=None):
        self.notify_channels = notify_channels  # type: list[str]
        self.notify_end_time = notify_end_time  # type: str
        self.notify_objects = notify_objects  # type: list[CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRuleNotifyObjects]
        self.notify_start_time = notify_start_time  # type: str

    def validate(self):
        if self.notify_objects:
            for k in self.notify_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.notify_end_time is not None:
            result['NotifyEndTime'] = self.notify_end_time
        result['NotifyObjects'] = []
        if self.notify_objects is not None:
            for k in self.notify_objects:
                result['NotifyObjects'].append(k.to_map() if k else None)
        if self.notify_start_time is not None:
            result['NotifyStartTime'] = self.notify_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('NotifyEndTime') is not None:
            self.notify_end_time = m.get('NotifyEndTime')
        self.notify_objects = []
        if m.get('NotifyObjects') is not None:
            for k in m.get('NotifyObjects'):
                temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRuleNotifyObjects()
                self.notify_objects.append(temp_model.from_map(k))
        if m.get('NotifyStartTime') is not None:
            self.notify_start_time = m.get('NotifyStartTime')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyTemplate(TeaModel):
    def __init__(self, email_content=None, email_recover_content=None, email_recover_title=None, email_title=None,
                 robot_content=None, sms_content=None, sms_recover_content=None, tts_content=None, tts_recover_content=None):
        self.email_content = email_content  # type: str
        self.email_recover_content = email_recover_content  # type: str
        self.email_recover_title = email_recover_title  # type: str
        self.email_title = email_title  # type: str
        self.robot_content = robot_content  # type: str
        self.sms_content = sms_content  # type: str
        self.sms_recover_content = sms_recover_content  # type: str
        self.tts_content = tts_content  # type: str
        self.tts_recover_content = tts_recover_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email_content is not None:
            result['EmailContent'] = self.email_content
        if self.email_recover_content is not None:
            result['EmailRecoverContent'] = self.email_recover_content
        if self.email_recover_title is not None:
            result['EmailRecoverTitle'] = self.email_recover_title
        if self.email_title is not None:
            result['EmailTitle'] = self.email_title
        if self.robot_content is not None:
            result['RobotContent'] = self.robot_content
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.sms_recover_content is not None:
            result['SmsRecoverContent'] = self.sms_recover_content
        if self.tts_content is not None:
            result['TtsContent'] = self.tts_content
        if self.tts_recover_content is not None:
            result['TtsRecoverContent'] = self.tts_recover_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmailContent') is not None:
            self.email_content = m.get('EmailContent')
        if m.get('EmailRecoverContent') is not None:
            self.email_recover_content = m.get('EmailRecoverContent')
        if m.get('EmailRecoverTitle') is not None:
            self.email_recover_title = m.get('EmailRecoverTitle')
        if m.get('EmailTitle') is not None:
            self.email_title = m.get('EmailTitle')
        if m.get('RobotContent') is not None:
            self.robot_content = m.get('RobotContent')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('SmsRecoverContent') is not None:
            self.sms_recover_content = m.get('SmsRecoverContent')
        if m.get('TtsContent') is not None:
            self.tts_content = m.get('TtsContent')
        if m.get('TtsRecoverContent') is not None:
            self.tts_recover_content = m.get('TtsRecoverContent')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicy(TeaModel):
    def __init__(self, escalation_policy_id=None, group_rule=None, id=None, integration_id=None,
                 matching_rules=None, name=None, notify_rule=None, notify_template=None, repeat=None, repeat_interval=None,
                 send_recover_message=None):
        self.escalation_policy_id = escalation_policy_id  # type: long
        self.group_rule = group_rule  # type: CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyGroupRule
        self.id = id  # type: long
        self.integration_id = integration_id  # type: long
        self.matching_rules = matching_rules  # type: list[CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRules]
        self.name = name  # type: str
        self.notify_rule = notify_rule  # type: CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRule
        self.notify_template = notify_template  # type: CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyTemplate
        self.repeat = repeat  # type: bool
        self.repeat_interval = repeat_interval  # type: long
        self.send_recover_message = send_recover_message  # type: bool

    def validate(self):
        if self.group_rule:
            self.group_rule.validate()
        if self.matching_rules:
            for k in self.matching_rules:
                if k:
                    k.validate()
        if self.notify_rule:
            self.notify_rule.validate()
        if self.notify_template:
            self.notify_template.validate()

    def to_map(self):
        _map = super(CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_policy_id is not None:
            result['EscalationPolicyId'] = self.escalation_policy_id
        if self.group_rule is not None:
            result['GroupRule'] = self.group_rule.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        result['MatchingRules'] = []
        if self.matching_rules is not None:
            for k in self.matching_rules:
                result['MatchingRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.notify_rule is not None:
            result['NotifyRule'] = self.notify_rule.to_map()
        if self.notify_template is not None:
            result['NotifyTemplate'] = self.notify_template.to_map()
        if self.repeat is not None:
            result['Repeat'] = self.repeat
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        if self.send_recover_message is not None:
            result['SendRecoverMessage'] = self.send_recover_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EscalationPolicyId') is not None:
            self.escalation_policy_id = m.get('EscalationPolicyId')
        if m.get('GroupRule') is not None:
            temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyGroupRule()
            self.group_rule = temp_model.from_map(m['GroupRule'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        self.matching_rules = []
        if m.get('MatchingRules') is not None:
            for k in m.get('MatchingRules'):
                temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRules()
                self.matching_rules.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotifyRule') is not None:
            temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRule()
            self.notify_rule = temp_model.from_map(m['NotifyRule'])
        if m.get('NotifyTemplate') is not None:
            temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyTemplate()
            self.notify_template = temp_model.from_map(m['NotifyTemplate'])
        if m.get('Repeat') is not None:
            self.repeat = m.get('Repeat')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        if m.get('SendRecoverMessage') is not None:
            self.send_recover_message = m.get('SendRecoverMessage')
        return self


class CreateOrUpdateNotificationPolicyResponseBody(TeaModel):
    def __init__(self, notification_policy=None, request_id=None):
        self.notification_policy = notification_policy  # type: CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicy
        self.request_id = request_id  # type: str

    def validate(self):
        if self.notification_policy:
            self.notification_policy.validate()

    def to_map(self):
        _map = super(CreateOrUpdateNotificationPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_policy is not None:
            result['NotificationPolicy'] = self.notification_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotificationPolicy') is not None:
            temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicy()
            self.notification_policy = temp_model.from_map(m['NotificationPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateNotificationPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOrUpdateNotificationPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrUpdateNotificationPolicyResponse, self).to_map()
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
            temp_model = CreateOrUpdateNotificationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateSilencePolicyRequest(TeaModel):
    def __init__(self, id=None, matching_rules=None, name=None, region_id=None):
        self.id = id  # type: long
        self.matching_rules = matching_rules  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateSilencePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.matching_rules is not None:
            result['MatchingRules'] = self.matching_rules
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchingRules') is not None:
            self.matching_rules = m.get('MatchingRules')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRulesMatchingConditions(TeaModel):
    def __init__(self, key=None, operator=None, value=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRulesMatchingConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRules(TeaModel):
    def __init__(self, matching_conditions=None):
        self.matching_conditions = matching_conditions  # type: list[CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRulesMatchingConditions]

    def validate(self):
        if self.matching_conditions:
            for k in self.matching_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchingConditions'] = []
        if self.matching_conditions is not None:
            for k in self.matching_conditions:
                result['MatchingConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.matching_conditions = []
        if m.get('MatchingConditions') is not None:
            for k in m.get('MatchingConditions'):
                temp_model = CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k))
        return self


class CreateOrUpdateSilencePolicyResponseBodySilencePolicy(TeaModel):
    def __init__(self, id=None, matching_rules=None, name=None):
        self.id = id  # type: long
        self.matching_rules = matching_rules  # type: list[CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRules]
        self.name = name  # type: str

    def validate(self):
        if self.matching_rules:
            for k in self.matching_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOrUpdateSilencePolicyResponseBodySilencePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['MatchingRules'] = []
        if self.matching_rules is not None:
            for k in self.matching_rules:
                result['MatchingRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.matching_rules = []
        if m.get('MatchingRules') is not None:
            for k in m.get('MatchingRules'):
                temp_model = CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRules()
                self.matching_rules.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateOrUpdateSilencePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, silence_policy=None):
        self.request_id = request_id  # type: str
        self.silence_policy = silence_policy  # type: CreateOrUpdateSilencePolicyResponseBodySilencePolicy

    def validate(self):
        if self.silence_policy:
            self.silence_policy.validate()

    def to_map(self):
        _map = super(CreateOrUpdateSilencePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.silence_policy is not None:
            result['SilencePolicy'] = self.silence_policy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SilencePolicy') is not None:
            temp_model = CreateOrUpdateSilencePolicyResponseBodySilencePolicy()
            self.silence_policy = temp_model.from_map(m['SilencePolicy'])
        return self


class CreateOrUpdateSilencePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOrUpdateSilencePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrUpdateSilencePolicyResponse, self).to_map()
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
            temp_model = CreateOrUpdateSilencePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateWebhookContactRequest(TeaModel):
    def __init__(self, biz_headers=None, biz_params=None, body=None, method=None, recover_body=None, url=None,
                 webhook_id=None, webhook_name=None):
        self.biz_headers = biz_headers  # type: str
        self.biz_params = biz_params  # type: str
        self.body = body  # type: str
        self.method = method  # type: str
        self.recover_body = recover_body  # type: str
        self.url = url  # type: str
        self.webhook_id = webhook_id  # type: long
        self.webhook_name = webhook_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateWebhookContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_headers is not None:
            result['BizHeaders'] = self.biz_headers
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params
        if self.body is not None:
            result['Body'] = self.body
        if self.method is not None:
            result['Method'] = self.method
        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body
        if self.url is not None:
            result['Url'] = self.url
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizHeaders') is not None:
            self.biz_headers = m.get('BizHeaders')
        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class CreateOrUpdateWebhookContactResponseBodyWebhookContactWebhook(TeaModel):
    def __init__(self, biz_headers=None, biz_params=None, body=None, method=None, recover_body=None, url=None):
        self.biz_headers = biz_headers  # type: str
        self.biz_params = biz_params  # type: str
        self.body = body  # type: str
        self.method = method  # type: str
        self.recover_body = recover_body  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateWebhookContactResponseBodyWebhookContactWebhook, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_headers is not None:
            result['BizHeaders'] = self.biz_headers
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params
        if self.body is not None:
            result['Body'] = self.body
        if self.method is not None:
            result['Method'] = self.method
        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizHeaders') is not None:
            self.biz_headers = m.get('BizHeaders')
        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateOrUpdateWebhookContactResponseBodyWebhookContact(TeaModel):
    def __init__(self, webhook=None, webhook_id=None, webhook_name=None):
        self.webhook = webhook  # type: CreateOrUpdateWebhookContactResponseBodyWebhookContactWebhook
        self.webhook_id = webhook_id  # type: float
        self.webhook_name = webhook_name  # type: str

    def validate(self):
        if self.webhook:
            self.webhook.validate()

    def to_map(self):
        _map = super(CreateOrUpdateWebhookContactResponseBodyWebhookContact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.webhook is not None:
            result['Webhook'] = self.webhook.to_map()
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Webhook') is not None:
            temp_model = CreateOrUpdateWebhookContactResponseBodyWebhookContactWebhook()
            self.webhook = temp_model.from_map(m['Webhook'])
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class CreateOrUpdateWebhookContactResponseBody(TeaModel):
    def __init__(self, request_id=None, webhook_contact=None):
        self.request_id = request_id  # type: str
        self.webhook_contact = webhook_contact  # type: CreateOrUpdateWebhookContactResponseBodyWebhookContact

    def validate(self):
        if self.webhook_contact:
            self.webhook_contact.validate()

    def to_map(self):
        _map = super(CreateOrUpdateWebhookContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.webhook_contact is not None:
            result['WebhookContact'] = self.webhook_contact.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WebhookContact') is not None:
            temp_model = CreateOrUpdateWebhookContactResponseBodyWebhookContact()
            self.webhook_contact = temp_model.from_map(m['WebhookContact'])
        return self


class CreateOrUpdateWebhookContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOrUpdateWebhookContactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrUpdateWebhookContactResponse, self).to_map()
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
            temp_model = CreateOrUpdateWebhookContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrometheusAlertRuleRequest(TeaModel):
    def __init__(self, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None, duration=None,
                 expression=None, labels=None, message=None, notify_type=None, region_id=None, type=None):
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: str
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: str
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None,
                 duration=None, expression=None, labels=None, message=None, notify_type=None, status=None, type=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: list[CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations]
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: list[CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels]
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.status = status  # type: int
        self.type = type  # type: str

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreatePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(self, prometheus_alert_rule=None, request_id=None):
        self.prometheus_alert_rule = prometheus_alert_rule  # type: CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prometheus_alert_rule:
            self.prometheus_alert_rule.validate()

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus_alert_rule is not None:
            result['PrometheusAlertRule'] = self.prometheus_alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrometheusAlertRule') is not None:
            temp_model = CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule()
            self.prometheus_alert_rule = temp_model.from_map(m['PrometheusAlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePrometheusAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePrometheusAlertRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleResponse, self).to_map()
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
            temp_model = CreatePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRetcodeAppRequest(TeaModel):
    def __init__(self, region_id=None, retcode_app_name=None, retcode_app_type=None):
        self.region_id = region_id  # type: str
        self.retcode_app_name = retcode_app_name  # type: str
        self.retcode_app_type = retcode_app_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRetcodeAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retcode_app_name is not None:
            result['RetcodeAppName'] = self.retcode_app_name
        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetcodeAppName') is not None:
            self.retcode_app_name = m.get('RetcodeAppName')
        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')
        return self


class CreateRetcodeAppResponseBodyRetcodeAppDataBean(TeaModel):
    def __init__(self, app_id=None, pid=None):
        self.app_id = app_id  # type: long
        self.pid = pid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRetcodeAppResponseBodyRetcodeAppDataBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class CreateRetcodeAppResponseBody(TeaModel):
    def __init__(self, request_id=None, retcode_app_data_bean=None):
        self.request_id = request_id  # type: str
        self.retcode_app_data_bean = retcode_app_data_bean  # type: CreateRetcodeAppResponseBodyRetcodeAppDataBean

    def validate(self):
        if self.retcode_app_data_bean:
            self.retcode_app_data_bean.validate()

    def to_map(self):
        _map = super(CreateRetcodeAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retcode_app_data_bean is not None:
            result['RetcodeAppDataBean'] = self.retcode_app_data_bean.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetcodeAppDataBean') is not None:
            temp_model = CreateRetcodeAppResponseBodyRetcodeAppDataBean()
            self.retcode_app_data_bean = temp_model.from_map(m['RetcodeAppDataBean'])
        return self


class CreateRetcodeAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRetcodeAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRetcodeAppResponse, self).to_map()
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
            temp_model = CreateRetcodeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSyntheticTaskRequestCommonParamAlertList(TeaModel):
    def __init__(self, is_critical=None, name=None, symbols=None):
        self.is_critical = is_critical  # type: long
        self.name = name  # type: str
        self.symbols = symbols  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestCommonParamAlertList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_critical is not None:
            result['IsCritical'] = self.is_critical
        if self.name is not None:
            result['Name'] = self.name
        if self.symbols is not None:
            result['Symbols'] = self.symbols
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsCritical') is not None:
            self.is_critical = m.get('IsCritical')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Symbols') is not None:
            self.symbols = m.get('Symbols')
        return self


class CreateSyntheticTaskRequestCommonParam(TeaModel):
    def __init__(self, alarm_flag=None, alert_list=None, alert_notifier_id=None, alert_policy_id=None,
                 monitor_samples=None, start_execution_time=None):
        self.alarm_flag = alarm_flag  # type: str
        self.alert_list = alert_list  # type: list[CreateSyntheticTaskRequestCommonParamAlertList]
        self.alert_notifier_id = alert_notifier_id  # type: str
        self.alert_policy_id = alert_policy_id  # type: str
        self.monitor_samples = monitor_samples  # type: long
        self.start_execution_time = start_execution_time  # type: long

    def validate(self):
        if self.alert_list:
            for k in self.alert_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestCommonParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_flag is not None:
            result['AlarmFlag'] = self.alarm_flag
        result['AlertList'] = []
        if self.alert_list is not None:
            for k in self.alert_list:
                result['AlertList'].append(k.to_map() if k else None)
        if self.alert_notifier_id is not None:
            result['AlertNotifierId'] = self.alert_notifier_id
        if self.alert_policy_id is not None:
            result['AlertPolicyId'] = self.alert_policy_id
        if self.monitor_samples is not None:
            result['MonitorSamples'] = self.monitor_samples
        if self.start_execution_time is not None:
            result['StartExecutionTime'] = self.start_execution_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmFlag') is not None:
            self.alarm_flag = m.get('AlarmFlag')
        self.alert_list = []
        if m.get('AlertList') is not None:
            for k in m.get('AlertList'):
                temp_model = CreateSyntheticTaskRequestCommonParamAlertList()
                self.alert_list.append(temp_model.from_map(k))
        if m.get('AlertNotifierId') is not None:
            self.alert_notifier_id = m.get('AlertNotifierId')
        if m.get('AlertPolicyId') is not None:
            self.alert_policy_id = m.get('AlertPolicyId')
        if m.get('MonitorSamples') is not None:
            self.monitor_samples = m.get('MonitorSamples')
        if m.get('StartExecutionTime') is not None:
            self.start_execution_time = m.get('StartExecutionTime')
        return self


class CreateSyntheticTaskRequestDownload(TeaModel):
    def __init__(self, connection_timeout=None, download_custom_header_content=None, download_custom_host=None,
                 download_custom_host_ip=None, download_ignore_certificate_error=None, download_kernel=None, download_redirection=None,
                 download_transmission_size=None, monitor_timeout=None, quick_protocol=None, validate_keywords=None, verify_way=None,
                 white_list=None):
        self.connection_timeout = connection_timeout  # type: float
        self.download_custom_header_content = download_custom_header_content  # type: str
        self.download_custom_host = download_custom_host  # type: long
        self.download_custom_host_ip = download_custom_host_ip  # type: str
        self.download_ignore_certificate_error = download_ignore_certificate_error  # type: str
        self.download_kernel = download_kernel  # type: long
        self.download_redirection = download_redirection  # type: long
        self.download_transmission_size = download_transmission_size  # type: long
        self.monitor_timeout = monitor_timeout  # type: long
        self.quick_protocol = quick_protocol  # type: str
        self.validate_keywords = validate_keywords  # type: str
        self.verify_way = verify_way  # type: long
        self.white_list = white_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestDownload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_timeout is not None:
            result['ConnectionTimeout'] = self.connection_timeout
        if self.download_custom_header_content is not None:
            result['DownloadCustomHeaderContent'] = self.download_custom_header_content
        if self.download_custom_host is not None:
            result['DownloadCustomHost'] = self.download_custom_host
        if self.download_custom_host_ip is not None:
            result['DownloadCustomHostIp'] = self.download_custom_host_ip
        if self.download_ignore_certificate_error is not None:
            result['DownloadIgnoreCertificateError'] = self.download_ignore_certificate_error
        if self.download_kernel is not None:
            result['DownloadKernel'] = self.download_kernel
        if self.download_redirection is not None:
            result['DownloadRedirection'] = self.download_redirection
        if self.download_transmission_size is not None:
            result['DownloadTransmissionSize'] = self.download_transmission_size
        if self.monitor_timeout is not None:
            result['MonitorTimeout'] = self.monitor_timeout
        if self.quick_protocol is not None:
            result['QuickProtocol'] = self.quick_protocol
        if self.validate_keywords is not None:
            result['ValidateKeywords'] = self.validate_keywords
        if self.verify_way is not None:
            result['VerifyWay'] = self.verify_way
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionTimeout') is not None:
            self.connection_timeout = m.get('ConnectionTimeout')
        if m.get('DownloadCustomHeaderContent') is not None:
            self.download_custom_header_content = m.get('DownloadCustomHeaderContent')
        if m.get('DownloadCustomHost') is not None:
            self.download_custom_host = m.get('DownloadCustomHost')
        if m.get('DownloadCustomHostIp') is not None:
            self.download_custom_host_ip = m.get('DownloadCustomHostIp')
        if m.get('DownloadIgnoreCertificateError') is not None:
            self.download_ignore_certificate_error = m.get('DownloadIgnoreCertificateError')
        if m.get('DownloadKernel') is not None:
            self.download_kernel = m.get('DownloadKernel')
        if m.get('DownloadRedirection') is not None:
            self.download_redirection = m.get('DownloadRedirection')
        if m.get('DownloadTransmissionSize') is not None:
            self.download_transmission_size = m.get('DownloadTransmissionSize')
        if m.get('MonitorTimeout') is not None:
            self.monitor_timeout = m.get('MonitorTimeout')
        if m.get('QuickProtocol') is not None:
            self.quick_protocol = m.get('QuickProtocol')
        if m.get('ValidateKeywords') is not None:
            self.validate_keywords = m.get('ValidateKeywords')
        if m.get('VerifyWay') is not None:
            self.verify_way = m.get('VerifyWay')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class CreateSyntheticTaskRequestExtendInterval(TeaModel):
    def __init__(self, days=None, end_hour=None, end_minute=None, end_time=None, start_hour=None, start_minute=None,
                 start_time=None):
        self.days = days  # type: list[long]
        self.end_hour = end_hour  # type: long
        self.end_minute = end_minute  # type: long
        self.end_time = end_time  # type: str
        self.start_hour = start_hour  # type: long
        self.start_minute = start_minute  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestExtendInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days is not None:
            result['Days'] = self.days
        if self.end_hour is not None:
            result['EndHour'] = self.end_hour
        if self.end_minute is not None:
            result['EndMinute'] = self.end_minute
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_hour is not None:
            result['StartHour'] = self.start_hour
        if self.start_minute is not None:
            result['StartMinute'] = self.start_minute
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('EndHour') is not None:
            self.end_hour = m.get('EndHour')
        if m.get('EndMinute') is not None:
            self.end_minute = m.get('EndMinute')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartHour') is not None:
            self.start_hour = m.get('StartHour')
        if m.get('StartMinute') is not None:
            self.start_minute = m.get('StartMinute')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateSyntheticTaskRequestMonitorList(TeaModel):
    def __init__(self, city_code=None, monitor_type=None, net_service_id=None):
        self.city_code = city_code  # type: long
        self.monitor_type = monitor_type  # type: long
        self.net_service_id = net_service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestMonitorList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.net_service_id is not None:
            result['NetServiceId'] = self.net_service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('NetServiceId') is not None:
            self.net_service_id = m.get('NetServiceId')
        return self


class CreateSyntheticTaskRequestNavigation(TeaModel):
    def __init__(self, dnshijack_white_list=None, element_blacklist=None, execute_active_x=None,
                 execute_application=None, execute_script=None, filter_invalid_ip=None, flow_hijack_jump_times=None,
                 flow_hijack_logo=None, monitor_timeout=None, nav_automatic_scrolling=None, nav_custom_header=None,
                 nav_custom_header_content=None, nav_custom_host=None, nav_custom_host_ip=None, nav_disable_cache=None,
                 nav_disable_compression=None, nav_ignore_certificate_error=None, nav_redirection=None, nav_return_element=None,
                 page_tamper=None, process_name=None, quicdomain=None, quicversion=None, request_header=None,
                 response_header=None, slow_element_threshold=None, verify_string_blacklist=None, verify_string_white_list=None,
                 wait_completion_time=None):
        self.dnshijack_white_list = dnshijack_white_list  # type: str
        self.element_blacklist = element_blacklist  # type: str
        self.execute_active_x = execute_active_x  # type: long
        self.execute_application = execute_application  # type: long
        self.execute_script = execute_script  # type: long
        self.filter_invalid_ip = filter_invalid_ip  # type: long
        self.flow_hijack_jump_times = flow_hijack_jump_times  # type: long
        self.flow_hijack_logo = flow_hijack_logo  # type: str
        self.monitor_timeout = monitor_timeout  # type: str
        self.nav_automatic_scrolling = nav_automatic_scrolling  # type: str
        self.nav_custom_header = nav_custom_header  # type: str
        self.nav_custom_header_content = nav_custom_header_content  # type: str
        self.nav_custom_host = nav_custom_host  # type: long
        self.nav_custom_host_ip = nav_custom_host_ip  # type: str
        self.nav_disable_cache = nav_disable_cache  # type: long
        self.nav_disable_compression = nav_disable_compression  # type: str
        self.nav_ignore_certificate_error = nav_ignore_certificate_error  # type: long
        self.nav_redirection = nav_redirection  # type: long
        self.nav_return_element = nav_return_element  # type: long
        self.page_tamper = page_tamper  # type: str
        self.process_name = process_name  # type: str
        self.quicdomain = quicdomain  # type: str
        self.quicversion = quicversion  # type: long
        self.request_header = request_header  # type: long
        self.response_header = response_header  # type: long
        self.slow_element_threshold = slow_element_threshold  # type: float
        self.verify_string_blacklist = verify_string_blacklist  # type: str
        self.verify_string_white_list = verify_string_white_list  # type: str
        self.wait_completion_time = wait_completion_time  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestNavigation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnshijack_white_list is not None:
            result['DNSHijackWhiteList'] = self.dnshijack_white_list
        if self.element_blacklist is not None:
            result['ElementBlacklist'] = self.element_blacklist
        if self.execute_active_x is not None:
            result['ExecuteActiveX'] = self.execute_active_x
        if self.execute_application is not None:
            result['ExecuteApplication'] = self.execute_application
        if self.execute_script is not None:
            result['ExecuteScript'] = self.execute_script
        if self.filter_invalid_ip is not None:
            result['FilterInvalidIP'] = self.filter_invalid_ip
        if self.flow_hijack_jump_times is not None:
            result['FlowHijackJumpTimes'] = self.flow_hijack_jump_times
        if self.flow_hijack_logo is not None:
            result['FlowHijackLogo'] = self.flow_hijack_logo
        if self.monitor_timeout is not None:
            result['MonitorTimeout'] = self.monitor_timeout
        if self.nav_automatic_scrolling is not None:
            result['NavAutomaticScrolling'] = self.nav_automatic_scrolling
        if self.nav_custom_header is not None:
            result['NavCustomHeader'] = self.nav_custom_header
        if self.nav_custom_header_content is not None:
            result['NavCustomHeaderContent'] = self.nav_custom_header_content
        if self.nav_custom_host is not None:
            result['NavCustomHost'] = self.nav_custom_host
        if self.nav_custom_host_ip is not None:
            result['NavCustomHostIp'] = self.nav_custom_host_ip
        if self.nav_disable_cache is not None:
            result['NavDisableCache'] = self.nav_disable_cache
        if self.nav_disable_compression is not None:
            result['NavDisableCompression'] = self.nav_disable_compression
        if self.nav_ignore_certificate_error is not None:
            result['NavIgnoreCertificateError'] = self.nav_ignore_certificate_error
        if self.nav_redirection is not None:
            result['NavRedirection'] = self.nav_redirection
        if self.nav_return_element is not None:
            result['NavReturnElement'] = self.nav_return_element
        if self.page_tamper is not None:
            result['PageTamper'] = self.page_tamper
        if self.process_name is not None:
            result['ProcessName'] = self.process_name
        if self.quicdomain is not None:
            result['QUICDomain'] = self.quicdomain
        if self.quicversion is not None:
            result['QUICVersion'] = self.quicversion
        if self.request_header is not None:
            result['RequestHeader'] = self.request_header
        if self.response_header is not None:
            result['ResponseHeader'] = self.response_header
        if self.slow_element_threshold is not None:
            result['SlowElementThreshold'] = self.slow_element_threshold
        if self.verify_string_blacklist is not None:
            result['VerifyStringBlacklist'] = self.verify_string_blacklist
        if self.verify_string_white_list is not None:
            result['VerifyStringWhiteList'] = self.verify_string_white_list
        if self.wait_completion_time is not None:
            result['WaitCompletionTime'] = self.wait_completion_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DNSHijackWhiteList') is not None:
            self.dnshijack_white_list = m.get('DNSHijackWhiteList')
        if m.get('ElementBlacklist') is not None:
            self.element_blacklist = m.get('ElementBlacklist')
        if m.get('ExecuteActiveX') is not None:
            self.execute_active_x = m.get('ExecuteActiveX')
        if m.get('ExecuteApplication') is not None:
            self.execute_application = m.get('ExecuteApplication')
        if m.get('ExecuteScript') is not None:
            self.execute_script = m.get('ExecuteScript')
        if m.get('FilterInvalidIP') is not None:
            self.filter_invalid_ip = m.get('FilterInvalidIP')
        if m.get('FlowHijackJumpTimes') is not None:
            self.flow_hijack_jump_times = m.get('FlowHijackJumpTimes')
        if m.get('FlowHijackLogo') is not None:
            self.flow_hijack_logo = m.get('FlowHijackLogo')
        if m.get('MonitorTimeout') is not None:
            self.monitor_timeout = m.get('MonitorTimeout')
        if m.get('NavAutomaticScrolling') is not None:
            self.nav_automatic_scrolling = m.get('NavAutomaticScrolling')
        if m.get('NavCustomHeader') is not None:
            self.nav_custom_header = m.get('NavCustomHeader')
        if m.get('NavCustomHeaderContent') is not None:
            self.nav_custom_header_content = m.get('NavCustomHeaderContent')
        if m.get('NavCustomHost') is not None:
            self.nav_custom_host = m.get('NavCustomHost')
        if m.get('NavCustomHostIp') is not None:
            self.nav_custom_host_ip = m.get('NavCustomHostIp')
        if m.get('NavDisableCache') is not None:
            self.nav_disable_cache = m.get('NavDisableCache')
        if m.get('NavDisableCompression') is not None:
            self.nav_disable_compression = m.get('NavDisableCompression')
        if m.get('NavIgnoreCertificateError') is not None:
            self.nav_ignore_certificate_error = m.get('NavIgnoreCertificateError')
        if m.get('NavRedirection') is not None:
            self.nav_redirection = m.get('NavRedirection')
        if m.get('NavReturnElement') is not None:
            self.nav_return_element = m.get('NavReturnElement')
        if m.get('PageTamper') is not None:
            self.page_tamper = m.get('PageTamper')
        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')
        if m.get('QUICDomain') is not None:
            self.quicdomain = m.get('QUICDomain')
        if m.get('QUICVersion') is not None:
            self.quicversion = m.get('QUICVersion')
        if m.get('RequestHeader') is not None:
            self.request_header = m.get('RequestHeader')
        if m.get('ResponseHeader') is not None:
            self.response_header = m.get('ResponseHeader')
        if m.get('SlowElementThreshold') is not None:
            self.slow_element_threshold = m.get('SlowElementThreshold')
        if m.get('VerifyStringBlacklist') is not None:
            self.verify_string_blacklist = m.get('VerifyStringBlacklist')
        if m.get('VerifyStringWhiteList') is not None:
            self.verify_string_white_list = m.get('VerifyStringWhiteList')
        if m.get('WaitCompletionTime') is not None:
            self.wait_completion_time = m.get('WaitCompletionTime')
        return self


class CreateSyntheticTaskRequestNet(TeaModel):
    def __init__(self, net_dnsns=None, net_dnsquery_method=None, net_dnsserver=None, net_dnsswitch=None,
                 net_dnstimeout=None, net_dig_switch=None, net_icmpactive=None, net_icmpdata_cut=None, net_icmpinterval=None,
                 net_icmpnum=None, net_icmpsize=None, net_icmpswitch=None, net_icmptimeout=None, net_trace_route_num=None,
                 net_trace_route_switch=None, net_trace_route_timeout=None, white_list=None):
        self.net_dnsns = net_dnsns  # type: str
        self.net_dnsquery_method = net_dnsquery_method  # type: long
        self.net_dnsserver = net_dnsserver  # type: long
        self.net_dnsswitch = net_dnsswitch  # type: long
        self.net_dnstimeout = net_dnstimeout  # type: long
        self.net_dig_switch = net_dig_switch  # type: long
        self.net_icmpactive = net_icmpactive  # type: long
        self.net_icmpdata_cut = net_icmpdata_cut  # type: long
        self.net_icmpinterval = net_icmpinterval  # type: long
        self.net_icmpnum = net_icmpnum  # type: long
        self.net_icmpsize = net_icmpsize  # type: long
        self.net_icmpswitch = net_icmpswitch  # type: long
        self.net_icmptimeout = net_icmptimeout  # type: long
        self.net_trace_route_num = net_trace_route_num  # type: long
        self.net_trace_route_switch = net_trace_route_switch  # type: long
        self.net_trace_route_timeout = net_trace_route_timeout  # type: long
        self.white_list = white_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestNet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_dnsns is not None:
            result['NetDNSNs'] = self.net_dnsns
        if self.net_dnsquery_method is not None:
            result['NetDNSQueryMethod'] = self.net_dnsquery_method
        if self.net_dnsserver is not None:
            result['NetDNSServer'] = self.net_dnsserver
        if self.net_dnsswitch is not None:
            result['NetDNSSwitch'] = self.net_dnsswitch
        if self.net_dnstimeout is not None:
            result['NetDNSTimeout'] = self.net_dnstimeout
        if self.net_dig_switch is not None:
            result['NetDigSwitch'] = self.net_dig_switch
        if self.net_icmpactive is not None:
            result['NetICMPActive'] = self.net_icmpactive
        if self.net_icmpdata_cut is not None:
            result['NetICMPDataCut'] = self.net_icmpdata_cut
        if self.net_icmpinterval is not None:
            result['NetICMPInterval'] = self.net_icmpinterval
        if self.net_icmpnum is not None:
            result['NetICMPNum'] = self.net_icmpnum
        if self.net_icmpsize is not None:
            result['NetICMPSize'] = self.net_icmpsize
        if self.net_icmpswitch is not None:
            result['NetICMPSwitch'] = self.net_icmpswitch
        if self.net_icmptimeout is not None:
            result['NetICMPTimeout'] = self.net_icmptimeout
        if self.net_trace_route_num is not None:
            result['NetTraceRouteNum'] = self.net_trace_route_num
        if self.net_trace_route_switch is not None:
            result['NetTraceRouteSwitch'] = self.net_trace_route_switch
        if self.net_trace_route_timeout is not None:
            result['NetTraceRouteTimeout'] = self.net_trace_route_timeout
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetDNSNs') is not None:
            self.net_dnsns = m.get('NetDNSNs')
        if m.get('NetDNSQueryMethod') is not None:
            self.net_dnsquery_method = m.get('NetDNSQueryMethod')
        if m.get('NetDNSServer') is not None:
            self.net_dnsserver = m.get('NetDNSServer')
        if m.get('NetDNSSwitch') is not None:
            self.net_dnsswitch = m.get('NetDNSSwitch')
        if m.get('NetDNSTimeout') is not None:
            self.net_dnstimeout = m.get('NetDNSTimeout')
        if m.get('NetDigSwitch') is not None:
            self.net_dig_switch = m.get('NetDigSwitch')
        if m.get('NetICMPActive') is not None:
            self.net_icmpactive = m.get('NetICMPActive')
        if m.get('NetICMPDataCut') is not None:
            self.net_icmpdata_cut = m.get('NetICMPDataCut')
        if m.get('NetICMPInterval') is not None:
            self.net_icmpinterval = m.get('NetICMPInterval')
        if m.get('NetICMPNum') is not None:
            self.net_icmpnum = m.get('NetICMPNum')
        if m.get('NetICMPSize') is not None:
            self.net_icmpsize = m.get('NetICMPSize')
        if m.get('NetICMPSwitch') is not None:
            self.net_icmpswitch = m.get('NetICMPSwitch')
        if m.get('NetICMPTimeout') is not None:
            self.net_icmptimeout = m.get('NetICMPTimeout')
        if m.get('NetTraceRouteNum') is not None:
            self.net_trace_route_num = m.get('NetTraceRouteNum')
        if m.get('NetTraceRouteSwitch') is not None:
            self.net_trace_route_switch = m.get('NetTraceRouteSwitch')
        if m.get('NetTraceRouteTimeout') is not None:
            self.net_trace_route_timeout = m.get('NetTraceRouteTimeout')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class CreateSyntheticTaskRequestProtocolRequestContentBodyFormData(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestProtocolRequestContentBodyFormData, self).to_map()
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


class CreateSyntheticTaskRequestProtocolRequestContentBodyUrlEncoding(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestProtocolRequestContentBodyUrlEncoding, self).to_map()
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


class CreateSyntheticTaskRequestProtocolRequestContentBody(TeaModel):
    def __init__(self, form_data=None, language=None, mode=None, raw=None, url_encoding=None):
        self.form_data = form_data  # type: list[CreateSyntheticTaskRequestProtocolRequestContentBodyFormData]
        self.language = language  # type: str
        self.mode = mode  # type: str
        self.raw = raw  # type: str
        self.url_encoding = url_encoding  # type: list[CreateSyntheticTaskRequestProtocolRequestContentBodyUrlEncoding]

    def validate(self):
        if self.form_data:
            for k in self.form_data:
                if k:
                    k.validate()
        if self.url_encoding:
            for k in self.url_encoding:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestProtocolRequestContentBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FormData'] = []
        if self.form_data is not None:
            for k in self.form_data:
                result['FormData'].append(k.to_map() if k else None)
        if self.language is not None:
            result['Language'] = self.language
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.raw is not None:
            result['Raw'] = self.raw
        result['UrlEncoding'] = []
        if self.url_encoding is not None:
            for k in self.url_encoding:
                result['UrlEncoding'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.form_data = []
        if m.get('FormData') is not None:
            for k in m.get('FormData'):
                temp_model = CreateSyntheticTaskRequestProtocolRequestContentBodyFormData()
                self.form_data.append(temp_model.from_map(k))
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Raw') is not None:
            self.raw = m.get('Raw')
        self.url_encoding = []
        if m.get('UrlEncoding') is not None:
            for k in m.get('UrlEncoding'):
                temp_model = CreateSyntheticTaskRequestProtocolRequestContentBodyUrlEncoding()
                self.url_encoding.append(temp_model.from_map(k))
        return self


class CreateSyntheticTaskRequestProtocolRequestContentHeader(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestProtocolRequestContentHeader, self).to_map()
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


class CreateSyntheticTaskRequestProtocolRequestContent(TeaModel):
    def __init__(self, body=None, header=None, method=None):
        self.body = body  # type: CreateSyntheticTaskRequestProtocolRequestContentBody
        self.header = header  # type: list[CreateSyntheticTaskRequestProtocolRequestContentHeader]
        self.method = method  # type: str

    def validate(self):
        if self.body:
            self.body.validate()
        if self.header:
            for k in self.header:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestProtocolRequestContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        result['Header'] = []
        if self.header is not None:
            for k in self.header:
                result['Header'].append(k.to_map() if k else None)
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CreateSyntheticTaskRequestProtocolRequestContentBody()
            self.body = temp_model.from_map(m['Body'])
        self.header = []
        if m.get('Header') is not None:
            for k in m.get('Header'):
                temp_model = CreateSyntheticTaskRequestProtocolRequestContentHeader()
                self.header.append(temp_model.from_map(k))
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class CreateSyntheticTaskRequestProtocol(TeaModel):
    def __init__(self, character_encoding=None, custom_host=None, custom_host_ip=None,
                 protocol_connection_time=None, protocol_monitor_timeout=None, received_data_size=None, request_content=None,
                 verify_content=None, verify_way=None):
        self.character_encoding = character_encoding  # type: long
        self.custom_host = custom_host  # type: long
        self.custom_host_ip = custom_host_ip  # type: str
        self.protocol_connection_time = protocol_connection_time  # type: long
        self.protocol_monitor_timeout = protocol_monitor_timeout  # type: str
        self.received_data_size = received_data_size  # type: long
        self.request_content = request_content  # type: CreateSyntheticTaskRequestProtocolRequestContent
        self.verify_content = verify_content  # type: str
        self.verify_way = verify_way  # type: long

    def validate(self):
        if self.request_content:
            self.request_content.validate()

    def to_map(self):
        _map = super(CreateSyntheticTaskRequestProtocol, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_encoding is not None:
            result['CharacterEncoding'] = self.character_encoding
        if self.custom_host is not None:
            result['CustomHost'] = self.custom_host
        if self.custom_host_ip is not None:
            result['CustomHostIp'] = self.custom_host_ip
        if self.protocol_connection_time is not None:
            result['ProtocolConnectionTime'] = self.protocol_connection_time
        if self.protocol_monitor_timeout is not None:
            result['ProtocolMonitorTimeout'] = self.protocol_monitor_timeout
        if self.received_data_size is not None:
            result['ReceivedDataSize'] = self.received_data_size
        if self.request_content is not None:
            result['RequestContent'] = self.request_content.to_map()
        if self.verify_content is not None:
            result['VerifyContent'] = self.verify_content
        if self.verify_way is not None:
            result['VerifyWay'] = self.verify_way
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterEncoding') is not None:
            self.character_encoding = m.get('CharacterEncoding')
        if m.get('CustomHost') is not None:
            self.custom_host = m.get('CustomHost')
        if m.get('CustomHostIp') is not None:
            self.custom_host_ip = m.get('CustomHostIp')
        if m.get('ProtocolConnectionTime') is not None:
            self.protocol_connection_time = m.get('ProtocolConnectionTime')
        if m.get('ProtocolMonitorTimeout') is not None:
            self.protocol_monitor_timeout = m.get('ProtocolMonitorTimeout')
        if m.get('ReceivedDataSize') is not None:
            self.received_data_size = m.get('ReceivedDataSize')
        if m.get('RequestContent') is not None:
            temp_model = CreateSyntheticTaskRequestProtocolRequestContent()
            self.request_content = temp_model.from_map(m['RequestContent'])
        if m.get('VerifyContent') is not None:
            self.verify_content = m.get('VerifyContent')
        if m.get('VerifyWay') is not None:
            self.verify_way = m.get('VerifyWay')
        return self


class CreateSyntheticTaskRequest(TeaModel):
    def __init__(self, common_param=None, download=None, extend_interval=None, interval_time=None,
                 interval_type=None, ip_type=None, monitor_list=None, navigation=None, net=None, protocol=None, region_id=None,
                 task_name=None, task_type=None, update_task=None, url=None):
        self.common_param = common_param  # type: CreateSyntheticTaskRequestCommonParam
        self.download = download  # type: CreateSyntheticTaskRequestDownload
        self.extend_interval = extend_interval  # type: CreateSyntheticTaskRequestExtendInterval
        self.interval_time = interval_time  # type: str
        self.interval_type = interval_type  # type: str
        self.ip_type = ip_type  # type: long
        self.monitor_list = monitor_list  # type: list[CreateSyntheticTaskRequestMonitorList]
        self.navigation = navigation  # type: CreateSyntheticTaskRequestNavigation
        self.net = net  # type: CreateSyntheticTaskRequestNet
        self.protocol = protocol  # type: CreateSyntheticTaskRequestProtocol
        self.region_id = region_id  # type: str
        self.task_name = task_name  # type: str
        self.task_type = task_type  # type: long
        self.update_task = update_task  # type: bool
        self.url = url  # type: str

    def validate(self):
        if self.common_param:
            self.common_param.validate()
        if self.download:
            self.download.validate()
        if self.extend_interval:
            self.extend_interval.validate()
        if self.monitor_list:
            for k in self.monitor_list:
                if k:
                    k.validate()
        if self.navigation:
            self.navigation.validate()
        if self.net:
            self.net.validate()
        if self.protocol:
            self.protocol.validate()

    def to_map(self):
        _map = super(CreateSyntheticTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_param is not None:
            result['CommonParam'] = self.common_param.to_map()
        if self.download is not None:
            result['Download'] = self.download.to_map()
        if self.extend_interval is not None:
            result['ExtendInterval'] = self.extend_interval.to_map()
        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time
        if self.interval_type is not None:
            result['IntervalType'] = self.interval_type
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        result['MonitorList'] = []
        if self.monitor_list is not None:
            for k in self.monitor_list:
                result['MonitorList'].append(k.to_map() if k else None)
        if self.navigation is not None:
            result['Navigation'] = self.navigation.to_map()
        if self.net is not None:
            result['Net'] = self.net.to_map()
        if self.protocol is not None:
            result['Protocol'] = self.protocol.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_task is not None:
            result['UpdateTask'] = self.update_task
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommonParam') is not None:
            temp_model = CreateSyntheticTaskRequestCommonParam()
            self.common_param = temp_model.from_map(m['CommonParam'])
        if m.get('Download') is not None:
            temp_model = CreateSyntheticTaskRequestDownload()
            self.download = temp_model.from_map(m['Download'])
        if m.get('ExtendInterval') is not None:
            temp_model = CreateSyntheticTaskRequestExtendInterval()
            self.extend_interval = temp_model.from_map(m['ExtendInterval'])
        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')
        if m.get('IntervalType') is not None:
            self.interval_type = m.get('IntervalType')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        self.monitor_list = []
        if m.get('MonitorList') is not None:
            for k in m.get('MonitorList'):
                temp_model = CreateSyntheticTaskRequestMonitorList()
                self.monitor_list.append(temp_model.from_map(k))
        if m.get('Navigation') is not None:
            temp_model = CreateSyntheticTaskRequestNavigation()
            self.navigation = temp_model.from_map(m['Navigation'])
        if m.get('Net') is not None:
            temp_model = CreateSyntheticTaskRequestNet()
            self.net = temp_model.from_map(m['Net'])
        if m.get('Protocol') is not None:
            temp_model = CreateSyntheticTaskRequestProtocol()
            self.protocol = temp_model.from_map(m['Protocol'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTask') is not None:
            self.update_task = m.get('UpdateTask')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateSyntheticTaskShrinkRequest(TeaModel):
    def __init__(self, common_param_shrink=None, download_shrink=None, extend_interval_shrink=None,
                 interval_time=None, interval_type=None, ip_type=None, monitor_list_shrink=None, navigation_shrink=None,
                 net_shrink=None, protocol_shrink=None, region_id=None, task_name=None, task_type=None, update_task=None,
                 url=None):
        self.common_param_shrink = common_param_shrink  # type: str
        self.download_shrink = download_shrink  # type: str
        self.extend_interval_shrink = extend_interval_shrink  # type: str
        self.interval_time = interval_time  # type: str
        self.interval_type = interval_type  # type: str
        self.ip_type = ip_type  # type: long
        self.monitor_list_shrink = monitor_list_shrink  # type: str
        self.navigation_shrink = navigation_shrink  # type: str
        self.net_shrink = net_shrink  # type: str
        self.protocol_shrink = protocol_shrink  # type: str
        self.region_id = region_id  # type: str
        self.task_name = task_name  # type: str
        self.task_type = task_type  # type: long
        self.update_task = update_task  # type: bool
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_param_shrink is not None:
            result['CommonParam'] = self.common_param_shrink
        if self.download_shrink is not None:
            result['Download'] = self.download_shrink
        if self.extend_interval_shrink is not None:
            result['ExtendInterval'] = self.extend_interval_shrink
        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time
        if self.interval_type is not None:
            result['IntervalType'] = self.interval_type
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.monitor_list_shrink is not None:
            result['MonitorList'] = self.monitor_list_shrink
        if self.navigation_shrink is not None:
            result['Navigation'] = self.navigation_shrink
        if self.net_shrink is not None:
            result['Net'] = self.net_shrink
        if self.protocol_shrink is not None:
            result['Protocol'] = self.protocol_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_task is not None:
            result['UpdateTask'] = self.update_task
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommonParam') is not None:
            self.common_param_shrink = m.get('CommonParam')
        if m.get('Download') is not None:
            self.download_shrink = m.get('Download')
        if m.get('ExtendInterval') is not None:
            self.extend_interval_shrink = m.get('ExtendInterval')
        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')
        if m.get('IntervalType') is not None:
            self.interval_type = m.get('IntervalType')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('MonitorList') is not None:
            self.monitor_list_shrink = m.get('MonitorList')
        if m.get('Navigation') is not None:
            self.navigation_shrink = m.get('Navigation')
        if m.get('Net') is not None:
            self.net_shrink = m.get('Net')
        if m.get('Protocol') is not None:
            self.protocol_shrink = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTask') is not None:
            self.update_task = m.get('UpdateTask')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateSyntheticTaskResponseBodyData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSyntheticTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateSyntheticTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateSyntheticTaskResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateSyntheticTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateSyntheticTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSyntheticTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSyntheticTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSyntheticTaskResponse, self).to_map()
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
            temp_model = CreateSyntheticTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebhookRequest(TeaModel):
    def __init__(self, body=None, contact_name=None, http_headers=None, http_params=None, method=None,
                 recover_body=None, region_id=None, url=None):
        self.body = body  # type: str
        self.contact_name = contact_name  # type: str
        self.http_headers = http_headers  # type: str
        self.http_params = http_params  # type: str
        self.method = method  # type: str
        self.recover_body = recover_body  # type: str
        self.region_id = region_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.http_headers is not None:
            result['HttpHeaders'] = self.http_headers
        if self.http_params is not None:
            result['HttpParams'] = self.http_params
        if self.method is not None:
            result['Method'] = self.method
        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('HttpHeaders') is not None:
            self.http_headers = m.get('HttpHeaders')
        if m.get('HttpParams') is not None:
            self.http_params = m.get('HttpParams')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateWebhookResponseBody(TeaModel):
    def __init__(self, contact_id=None, request_id=None):
        self.contact_id = contact_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWebhookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWebhookResponse, self).to_map()
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
            temp_model = CreateWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelAuthTokenRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DelAuthTokenRequest, self).to_map()
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


class DelAuthTokenResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DelAuthTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DelAuthTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DelAuthTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DelAuthTokenResponse, self).to_map()
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
            temp_model = DelAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertContactRequest(TeaModel):
    def __init__(self, contact_id=None, region_id=None):
        self.contact_id = contact_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertContactResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAlertContactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlertContactResponse, self).to_map()
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
            temp_model = DeleteAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertContactGroupRequest(TeaModel):
    def __init__(self, contact_group_id=None, region_id=None):
        self.contact_group_id = contact_group_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertContactGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertContactGroupResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertContactGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertContactGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAlertContactGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlertContactGroupResponse, self).to_map()
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
            temp_model = DeleteAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertRuleRequest(TeaModel):
    def __init__(self, alert_id=None):
        self.alert_id = alert_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        return self


class DeleteAlertRuleResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAlertRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlertRuleResponse, self).to_map()
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
            temp_model = DeleteAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertRulesRequest(TeaModel):
    def __init__(self, alert_ids=None, region_id=None):
        self.alert_ids = alert_ids  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertRulesResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAlertRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlertRulesResponse, self).to_map()
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
            temp_model = DeleteAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCmsExporterRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCmsExporterRequest, self).to_map()
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


class DeleteCmsExporterResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCmsExporterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCmsExporterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCmsExporterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCmsExporterResponse, self).to_map()
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
            temp_model = DeleteCmsExporterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContactRequest(TeaModel):
    def __init__(self, contact_id=None):
        self.contact_id = contact_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        return self


class DeleteContactResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteContactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteContactResponse, self).to_map()
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
            temp_model = DeleteContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContactGroupRequest(TeaModel):
    def __init__(self, contact_group_id=None):
        self.contact_group_id = contact_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteContactGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        return self


class DeleteContactGroupResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteContactGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteContactGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteContactGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteContactGroupResponse, self).to_map()
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
            temp_model = DeleteContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDispatchRuleRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDispatchRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDispatchRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDispatchRuleResponseBody, self).to_map()
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


class DeleteDispatchRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDispatchRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDispatchRuleResponse, self).to_map()
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
            temp_model = DeleteDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventBridgeIntegrationRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventBridgeIntegrationRequest, self).to_map()
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


class DeleteEventBridgeIntegrationResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventBridgeIntegrationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEventBridgeIntegrationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEventBridgeIntegrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEventBridgeIntegrationResponse, self).to_map()
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
            temp_model = DeleteEventBridgeIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGrafanaResourceRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGrafanaResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteGrafanaResourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGrafanaResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGrafanaResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGrafanaResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGrafanaResourceResponse, self).to_map()
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
            temp_model = DeleteGrafanaResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIMRobotRequest(TeaModel):
    def __init__(self, robot_id=None):
        self.robot_id = robot_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIMRobotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        return self


class DeleteIMRobotResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIMRobotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIMRobotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIMRobotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIMRobotResponse, self).to_map()
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
            temp_model = DeleteIMRobotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIntegrationRequest(TeaModel):
    def __init__(self, cluster_id=None, integration=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.integration = integration  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIntegrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIntegrationResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIntegrationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIntegrationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIntegrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIntegrationResponse, self).to_map()
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
            temp_model = DeleteIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIntegrationsRequest(TeaModel):
    def __init__(self, integration_id=None):
        self.integration_id = integration_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIntegrationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        return self


class DeleteIntegrationsResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIntegrationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIntegrationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIntegrationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIntegrationsResponse, self).to_map()
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
            temp_model = DeleteIntegrationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNotificationPolicyRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNotificationPolicyRequest, self).to_map()
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


class DeleteNotificationPolicyResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNotificationPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNotificationPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNotificationPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNotificationPolicyResponse, self).to_map()
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
            temp_model = DeleteNotificationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrometheusAlertRuleRequest(TeaModel):
    def __init__(self, alert_id=None):
        self.alert_id = alert_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrometheusAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        return self


class DeletePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrometheusAlertRuleResponseBody, self).to_map()
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


class DeletePrometheusAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePrometheusAlertRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePrometheusAlertRuleResponse, self).to_map()
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
            temp_model = DeletePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrometheusGlobalViewRequest(TeaModel):
    def __init__(self, global_view_cluster_id=None, region_id=None):
        self.global_view_cluster_id = global_view_cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrometheusGlobalViewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeletePrometheusGlobalViewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrometheusGlobalViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePrometheusGlobalViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePrometheusGlobalViewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePrometheusGlobalViewResponse, self).to_map()
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
            temp_model = DeletePrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRetcodeAppRequest(TeaModel):
    def __init__(self, app_id=None, region_id=None):
        self.app_id = app_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRetcodeAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteRetcodeAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRetcodeAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRetcodeAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRetcodeAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRetcodeAppResponse, self).to_map()
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
            temp_model = DeleteRetcodeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScenarioRequest(TeaModel):
    def __init__(self, region_id=None, scenario_id=None):
        self.region_id = region_id  # type: str
        self.scenario_id = scenario_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScenarioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        return self


class DeleteScenarioResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScenarioResponseBody, self).to_map()
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


class DeleteScenarioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteScenarioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteScenarioResponse, self).to_map()
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
            temp_model = DeleteScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSilencePolicyRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSilencePolicyRequest, self).to_map()
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


class DeleteSilencePolicyResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSilencePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSilencePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSilencePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSilencePolicyResponse, self).to_map()
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
            temp_model = DeleteSilencePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSourceMapRequest(TeaModel):
    def __init__(self, fid_list=None, pid=None, region_id=None):
        self.fid_list = fid_list  # type: list[str]
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSourceMapRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fid_list is not None:
            result['FidList'] = self.fid_list
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FidList') is not None:
            self.fid_list = m.get('FidList')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteSourceMapShrinkRequest(TeaModel):
    def __init__(self, fid_list_shrink=None, pid=None, region_id=None):
        self.fid_list_shrink = fid_list_shrink  # type: str
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSourceMapShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fid_list_shrink is not None:
            result['FidList'] = self.fid_list_shrink
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FidList') is not None:
            self.fid_list_shrink = m.get('FidList')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteSourceMapResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSourceMapResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSourceMapResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSourceMapResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSourceMapResponse, self).to_map()
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
            temp_model = DeleteSourceMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSyntheticTaskRequest(TeaModel):
    def __init__(self, region_id=None, task_ids=None):
        self.region_id = region_id  # type: str
        self.task_ids = task_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSyntheticTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class DeleteSyntheticTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSyntheticTaskResponseBody, self).to_map()
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


class DeleteSyntheticTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSyntheticTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSyntheticTaskResponse, self).to_map()
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
            temp_model = DeleteSyntheticTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTraceAppRequest(TeaModel):
    def __init__(self, app_id=None, pid=None, region_id=None, type=None):
        self.app_id = app_id  # type: str
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTraceAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DeleteTraceAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTraceAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTraceAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTraceAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTraceAppResponse, self).to_map()
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
            temp_model = DeleteTraceAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebhookContactRequest(TeaModel):
    def __init__(self, webhook_id=None):
        self.webhook_id = webhook_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebhookContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        return self


class DeleteWebhookContactResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebhookContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWebhookContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWebhookContactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWebhookContactResponse, self).to_map()
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
            temp_model = DeleteWebhookContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContactGroupsRequest(TeaModel):
    def __init__(self, contact_group_name=None, is_detail=None, page=None, size=None):
        self.contact_group_name = contact_group_name  # type: str
        self.is_detail = is_detail  # type: bool
        self.page = page  # type: long
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContactGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeContactGroupsResponseBodyPageBeanAlertContactGroupsContacts(TeaModel):
    def __init__(self, contact_id=None, contact_name=None, email=None, phone=None):
        self.contact_id = contact_id  # type: float
        self.contact_name = contact_name  # type: str
        self.email = email  # type: str
        self.phone = phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContactGroupsResponseBodyPageBeanAlertContactGroupsContacts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class DescribeContactGroupsResponseBodyPageBeanAlertContactGroups(TeaModel):
    def __init__(self, contact_group_id=None, contact_group_name=None, contacts=None):
        self.contact_group_id = contact_group_id  # type: float
        self.contact_group_name = contact_group_name  # type: str
        self.contacts = contacts  # type: list[DescribeContactGroupsResponseBodyPageBeanAlertContactGroupsContacts]

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContactGroupsResponseBodyPageBeanAlertContactGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = DescribeContactGroupsResponseBodyPageBeanAlertContactGroupsContacts()
                self.contacts.append(temp_model.from_map(k))
        return self


class DescribeContactGroupsResponseBodyPageBean(TeaModel):
    def __init__(self, alert_contact_groups=None, page=None, size=None, total=None):
        self.alert_contact_groups = alert_contact_groups  # type: list[DescribeContactGroupsResponseBodyPageBeanAlertContactGroups]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.alert_contact_groups:
            for k in self.alert_contact_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContactGroupsResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertContactGroups'] = []
        if self.alert_contact_groups is not None:
            for k in self.alert_contact_groups:
                result['AlertContactGroups'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alert_contact_groups = []
        if m.get('AlertContactGroups') is not None:
            for k in m.get('AlertContactGroups'):
                temp_model = DescribeContactGroupsResponseBodyPageBeanAlertContactGroups()
                self.alert_contact_groups.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeContactGroupsResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: DescribeContactGroupsResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(DescribeContactGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = DescribeContactGroupsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContactGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeContactGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContactGroupsResponse, self).to_map()
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
            temp_model = DescribeContactGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContactsRequest(TeaModel):
    def __init__(self, contact_name=None, email=None, page=None, phone=None, size=None):
        self.contact_name = contact_name  # type: str
        self.email = email  # type: str
        self.page = page  # type: long
        self.phone = phone  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContactsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.page is not None:
            result['Page'] = self.page
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeContactsResponseBodyPageBeanAlertContacts(TeaModel):
    def __init__(self, contact_id=None, contact_name=None, email=None, is_verify=None, phone=None,
                 reissue_send_notice=None):
        self.contact_id = contact_id  # type: float
        self.contact_name = contact_name  # type: str
        self.email = email  # type: str
        self.is_verify = is_verify  # type: bool
        self.phone = phone  # type: str
        self.reissue_send_notice = reissue_send_notice  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContactsResponseBodyPageBeanAlertContacts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.is_verify is not None:
            result['IsVerify'] = self.is_verify
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.reissue_send_notice is not None:
            result['ReissueSendNotice'] = self.reissue_send_notice
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IsVerify') is not None:
            self.is_verify = m.get('IsVerify')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ReissueSendNotice') is not None:
            self.reissue_send_notice = m.get('ReissueSendNotice')
        return self


class DescribeContactsResponseBodyPageBean(TeaModel):
    def __init__(self, alert_contacts=None, page=None, size=None, total=None):
        self.alert_contacts = alert_contacts  # type: list[DescribeContactsResponseBodyPageBeanAlertContacts]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.alert_contacts:
            for k in self.alert_contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContactsResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertContacts'] = []
        if self.alert_contacts is not None:
            for k in self.alert_contacts:
                result['AlertContacts'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alert_contacts = []
        if m.get('AlertContacts') is not None:
            for k in m.get('AlertContacts'):
                temp_model = DescribeContactsResponseBodyPageBeanAlertContacts()
                self.alert_contacts.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeContactsResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: DescribeContactsResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(DescribeContactsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = DescribeContactsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContactsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeContactsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContactsResponse, self).to_map()
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
            temp_model = DescribeContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDispatchRuleRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDispatchRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleGroupRules(TeaModel):
    def __init__(self, group_id=None, group_interval=None, group_wait_time=None, grouping_fields=None,
                 repeat_interval=None):
        self.group_id = group_id  # type: long
        self.group_interval = group_interval  # type: long
        self.group_wait_time = group_wait_time  # type: long
        self.grouping_fields = grouping_fields  # type: list[str]
        self.repeat_interval = repeat_interval  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleGroupRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_interval is not None:
            result['GroupInterval'] = self.group_interval
        if self.group_wait_time is not None:
            result['GroupWaitTime'] = self.group_wait_time
        if self.grouping_fields is not None:
            result['GroupingFields'] = self.grouping_fields
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupInterval') is not None:
            self.group_interval = m.get('GroupInterval')
        if m.get('GroupWaitTime') is not None:
            self.group_wait_time = m.get('GroupWaitTime')
        if m.get('GroupingFields') is not None:
            self.grouping_fields = m.get('GroupingFields')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions(TeaModel):
    def __init__(self, key=None, operator=None, value=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups(TeaModel):
    def __init__(self, label_match_expressions=None):
        self.label_match_expressions = label_match_expressions  # type: list[DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions]

    def validate(self):
        if self.label_match_expressions:
            for k in self.label_match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelMatchExpressions'] = []
        if self.label_match_expressions is not None:
            for k in self.label_match_expressions:
                result['LabelMatchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.label_match_expressions = []
        if m.get('LabelMatchExpressions') is not None:
            for k in m.get('LabelMatchExpressions'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions()
                self.label_match_expressions.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid(TeaModel):
    def __init__(self, label_match_expression_groups=None):
        self.label_match_expression_groups = label_match_expression_groups  # type: list[DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups]

    def validate(self):
        if self.label_match_expression_groups:
            for k in self.label_match_expression_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelMatchExpressionGroups'] = []
        if self.label_match_expression_groups is not None:
            for k in self.label_match_expression_groups:
                result['LabelMatchExpressionGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.label_match_expression_groups = []
        if m.get('LabelMatchExpressionGroups') is not None:
            for k in m.get('LabelMatchExpressionGroups'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups()
                self.label_match_expression_groups.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects(TeaModel):
    def __init__(self, name=None, notify_object_id=None, notify_type=None):
        self.name = name  # type: str
        self.notify_object_id = notify_object_id  # type: str
        self.notify_type = notify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.notify_object_id is not None:
            result['NotifyObjectId'] = self.notify_object_id
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotifyObjectId') is not None:
            self.notify_object_id = m.get('NotifyObjectId')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules(TeaModel):
    def __init__(self, notify_channels=None, notify_objects=None):
        self.notify_channels = notify_channels  # type: list[str]
        self.notify_objects = notify_objects  # type: list[DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects]

    def validate(self):
        if self.notify_objects:
            for k in self.notify_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        result['NotifyObjects'] = []
        if self.notify_objects is not None:
            for k in self.notify_objects:
                result['NotifyObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        self.notify_objects = []
        if m.get('NotifyObjects') is not None:
            for k in m.get('NotifyObjects'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects()
                self.notify_objects.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRule(TeaModel):
    def __init__(self, dispatch_type=None, group_rules=None, is_recover=None, label_match_expression_grid=None,
                 name=None, notify_rules=None, rule_id=None, state=None):
        self.dispatch_type = dispatch_type  # type: str
        self.group_rules = group_rules  # type: list[DescribeDispatchRuleResponseBodyDispatchRuleGroupRules]
        self.is_recover = is_recover  # type: bool
        self.label_match_expression_grid = label_match_expression_grid  # type: DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid
        self.name = name  # type: str
        self.notify_rules = notify_rules  # type: list[DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules]
        self.rule_id = rule_id  # type: long
        self.state = state  # type: str

    def validate(self):
        if self.group_rules:
            for k in self.group_rules:
                if k:
                    k.validate()
        if self.label_match_expression_grid:
            self.label_match_expression_grid.validate()
        if self.notify_rules:
            for k in self.notify_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_type is not None:
            result['DispatchType'] = self.dispatch_type
        result['GroupRules'] = []
        if self.group_rules is not None:
            for k in self.group_rules:
                result['GroupRules'].append(k.to_map() if k else None)
        if self.is_recover is not None:
            result['IsRecover'] = self.is_recover
        if self.label_match_expression_grid is not None:
            result['LabelMatchExpressionGrid'] = self.label_match_expression_grid.to_map()
        if self.name is not None:
            result['Name'] = self.name
        result['NotifyRules'] = []
        if self.notify_rules is not None:
            for k in self.notify_rules:
                result['NotifyRules'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DispatchType') is not None:
            self.dispatch_type = m.get('DispatchType')
        self.group_rules = []
        if m.get('GroupRules') is not None:
            for k in m.get('GroupRules'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleGroupRules()
                self.group_rules.append(temp_model.from_map(k))
        if m.get('IsRecover') is not None:
            self.is_recover = m.get('IsRecover')
        if m.get('LabelMatchExpressionGrid') is not None:
            temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid()
            self.label_match_expression_grid = temp_model.from_map(m['LabelMatchExpressionGrid'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.notify_rules = []
        if m.get('NotifyRules') is not None:
            for k in m.get('NotifyRules'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules()
                self.notify_rules.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeDispatchRuleResponseBody(TeaModel):
    def __init__(self, dispatch_rule=None, request_id=None):
        self.dispatch_rule = dispatch_rule  # type: DescribeDispatchRuleResponseBodyDispatchRule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dispatch_rule:
            self.dispatch_rule.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            temp_model = DescribeDispatchRuleResponseBodyDispatchRule()
            self.dispatch_rule = temp_model.from_map(m['DispatchRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDispatchRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDispatchRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponse, self).to_map()
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
            temp_model = DescribeDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIMRobotsRequest(TeaModel):
    def __init__(self, page=None, robot_name=None, size=None):
        self.page = page  # type: long
        self.robot_name = robot_name  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIMRobotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeIMRobotsResponseBodyPageBeanAlertIMRobots(TeaModel):
    def __init__(self, daily_noc=None, daily_noc_time=None, robot_addr=None, robot_id=None, robot_name=None,
                 type=None):
        self.daily_noc = daily_noc  # type: bool
        self.daily_noc_time = daily_noc_time  # type: str
        self.robot_addr = robot_addr  # type: str
        self.robot_id = robot_id  # type: float
        self.robot_name = robot_name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIMRobotsResponseBodyPageBeanAlertIMRobots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.daily_noc is not None:
            result['DailyNoc'] = self.daily_noc
        if self.daily_noc_time is not None:
            result['DailyNocTime'] = self.daily_noc_time
        if self.robot_addr is not None:
            result['RobotAddr'] = self.robot_addr
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DailyNoc') is not None:
            self.daily_noc = m.get('DailyNoc')
        if m.get('DailyNocTime') is not None:
            self.daily_noc_time = m.get('DailyNocTime')
        if m.get('RobotAddr') is not None:
            self.robot_addr = m.get('RobotAddr')
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeIMRobotsResponseBodyPageBean(TeaModel):
    def __init__(self, alert_imrobots=None, page=None, size=None, total=None):
        self.alert_imrobots = alert_imrobots  # type: list[DescribeIMRobotsResponseBodyPageBeanAlertIMRobots]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.alert_imrobots:
            for k in self.alert_imrobots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIMRobotsResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertIMRobots'] = []
        if self.alert_imrobots is not None:
            for k in self.alert_imrobots:
                result['AlertIMRobots'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alert_imrobots = []
        if m.get('AlertIMRobots') is not None:
            for k in m.get('AlertIMRobots'):
                temp_model = DescribeIMRobotsResponseBodyPageBeanAlertIMRobots()
                self.alert_imrobots.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeIMRobotsResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: DescribeIMRobotsResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(DescribeIMRobotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = DescribeIMRobotsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIMRobotsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIMRobotsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIMRobotsResponse, self).to_map()
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
            temp_model = DescribeIMRobotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePrometheusAlertRuleRequest(TeaModel):
    def __init__(self, alert_id=None):
        self.alert_id = alert_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        return self


class DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None,
                 duration=None, expression=None, labels=None, message=None, notify_type=None, status=None, type=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: list[DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations]
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: list[DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels]
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.status = status  # type: int
        self.type = type  # type: str

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(self, prometheus_alert_rule=None, request_id=None):
        self.prometheus_alert_rule = prometheus_alert_rule  # type: DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prometheus_alert_rule:
            self.prometheus_alert_rule.validate()

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus_alert_rule is not None:
            result['PrometheusAlertRule'] = self.prometheus_alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrometheusAlertRule') is not None:
            temp_model = DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule()
            self.prometheus_alert_rule = temp_model.from_map(m['PrometheusAlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePrometheusAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePrometheusAlertRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleResponse, self).to_map()
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
            temp_model = DescribePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTraceLicenseKeyRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTraceLicenseKeyRequest, self).to_map()
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


class DescribeTraceLicenseKeyResponseBody(TeaModel):
    def __init__(self, license_key=None, request_id=None):
        self.license_key = license_key  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTraceLicenseKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTraceLicenseKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTraceLicenseKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTraceLicenseKeyResponse, self).to_map()
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
            temp_model = DescribeTraceLicenseKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebhookContactsRequest(TeaModel):
    def __init__(self, page=None, size=None, webhook_name=None):
        self.page = page  # type: long
        self.size = size  # type: long
        self.webhook_name = webhook_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebhookContactsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class DescribeWebhookContactsResponseBodyPageBeanWebhookContactsWebhook(TeaModel):
    def __init__(self, biz_headers=None, biz_params=None, body=None, method=None, recover_body=None, url=None):
        self.biz_headers = biz_headers  # type: dict[str, any]
        self.biz_params = biz_params  # type: dict[str, any]
        self.body = body  # type: str
        self.method = method  # type: str
        self.recover_body = recover_body  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebhookContactsResponseBodyPageBeanWebhookContactsWebhook, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_headers is not None:
            result['BizHeaders'] = self.biz_headers
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params
        if self.body is not None:
            result['Body'] = self.body
        if self.method is not None:
            result['Method'] = self.method
        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizHeaders') is not None:
            self.biz_headers = m.get('BizHeaders')
        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeWebhookContactsResponseBodyPageBeanWebhookContacts(TeaModel):
    def __init__(self, webhook=None, webhook_id=None, webhook_name=None):
        self.webhook = webhook  # type: DescribeWebhookContactsResponseBodyPageBeanWebhookContactsWebhook
        self.webhook_id = webhook_id  # type: float
        self.webhook_name = webhook_name  # type: str

    def validate(self):
        if self.webhook:
            self.webhook.validate()

    def to_map(self):
        _map = super(DescribeWebhookContactsResponseBodyPageBeanWebhookContacts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.webhook is not None:
            result['Webhook'] = self.webhook.to_map()
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Webhook') is not None:
            temp_model = DescribeWebhookContactsResponseBodyPageBeanWebhookContactsWebhook()
            self.webhook = temp_model.from_map(m['Webhook'])
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class DescribeWebhookContactsResponseBodyPageBean(TeaModel):
    def __init__(self, page=None, size=None, total=None, webhook_contacts=None):
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long
        self.webhook_contacts = webhook_contacts  # type: list[DescribeWebhookContactsResponseBodyPageBeanWebhookContacts]

    def validate(self):
        if self.webhook_contacts:
            for k in self.webhook_contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebhookContactsResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        result['WebhookContacts'] = []
        if self.webhook_contacts is not None:
            for k in self.webhook_contacts:
                result['WebhookContacts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.webhook_contacts = []
        if m.get('WebhookContacts') is not None:
            for k in m.get('WebhookContacts'):
                temp_model = DescribeWebhookContactsResponseBodyPageBeanWebhookContacts()
                self.webhook_contacts.append(temp_model.from_map(k))
        return self


class DescribeWebhookContactsResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: DescribeWebhookContactsResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(DescribeWebhookContactsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = DescribeWebhookContactsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebhookContactsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebhookContactsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebhookContactsResponse, self).to_map()
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
            temp_model = DescribeWebhookContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentDownloadUrlRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentDownloadUrlRequest, self).to_map()
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


class GetAgentDownloadUrlResponseBody(TeaModel):
    def __init__(self, arms_agent_download_url=None, request_id=None):
        self.arms_agent_download_url = arms_agent_download_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentDownloadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arms_agent_download_url is not None:
            result['ArmsAgentDownloadUrl'] = self.arms_agent_download_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArmsAgentDownloadUrl') is not None:
            self.arms_agent_download_url = m.get('ArmsAgentDownloadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAgentDownloadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAgentDownloadUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentDownloadUrlResponse, self).to_map()
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
            temp_model = GetAgentDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlertRulesRequest(TeaModel):
    def __init__(self, alert_ids=None, alert_names=None, alert_status=None, alert_type=None, cluster_id=None,
                 page=None, region_id=None, size=None):
        self.alert_ids = alert_ids  # type: str
        self.alert_names = alert_names  # type: str
        self.alert_status = alert_status  # type: str
        self.alert_type = alert_type  # type: str
        self.cluster_id = cluster_id  # type: str
        self.page = page  # type: long
        self.region_id = region_id  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlertRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids
        if self.alert_names is not None:
            result['AlertNames'] = self.alert_names
        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page is not None:
            result['Page'] = self.page
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')
        if m.get('AlertNames') is not None:
            self.alert_names = m.get('AlertNames')
        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContentAlertRuleItems(TeaModel):
    def __init__(self, aggregate=None, metric_key=None, n=None, operator=None, value=None):
        self.aggregate = aggregate  # type: str
        self.metric_key = metric_key  # type: str
        self.n = n  # type: float
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContentAlertRuleItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregate is not None:
            result['Aggregate'] = self.aggregate
        if self.metric_key is not None:
            result['MetricKey'] = self.metric_key
        if self.n is not None:
            result['N'] = self.n
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aggregate') is not None:
            self.aggregate = m.get('Aggregate')
        if m.get('MetricKey') is not None:
            self.metric_key = m.get('MetricKey')
        if m.get('N') is not None:
            self.n = m.get('N')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContent(TeaModel):
    def __init__(self, alert_rule_items=None, condition=None):
        self.alert_rule_items = alert_rule_items  # type: list[GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContentAlertRuleItems]
        self.condition = condition  # type: str

    def validate(self):
        if self.alert_rule_items:
            for k in self.alert_rule_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertRuleItems'] = []
        if self.alert_rule_items is not None:
            for k in self.alert_rule_items:
                result['AlertRuleItems'].append(k.to_map() if k else None)
        if self.condition is not None:
            result['Condition'] = self.condition
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alert_rule_items = []
        if m.get('AlertRuleItems') is not None:
            for k in m.get('AlertRuleItems'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContentAlertRuleItems()
                self.alert_rule_items.append(temp_model.from_map(k))
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlertRulesResponseBodyPageBeanAlertRulesAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesFiltersCustomSLSFilters(TeaModel):
    def __init__(self, key=None, opt=None, show=None, t=None, value=None):
        self.key = key  # type: str
        self.opt = opt  # type: str
        self.show = show  # type: bool
        self.t = t  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlertRulesResponseBodyPageBeanAlertRulesFiltersCustomSLSFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.opt is not None:
            result['Opt'] = self.opt
        if self.show is not None:
            result['Show'] = self.show
        if self.t is not None:
            result['T'] = self.t
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Opt') is not None:
            self.opt = m.get('Opt')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('T') is not None:
            self.t = m.get('T')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesFiltersDimFilters(TeaModel):
    def __init__(self, filter_key=None, filter_opt=None, filter_values=None):
        self.filter_key = filter_key  # type: str
        self.filter_opt = filter_opt  # type: str
        self.filter_values = filter_values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlertRulesResponseBodyPageBeanAlertRulesFiltersDimFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_opt is not None:
            result['FilterOpt'] = self.filter_opt
        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterOpt') is not None:
            self.filter_opt = m.get('FilterOpt')
        if m.get('FilterValues') is not None:
            self.filter_values = m.get('FilterValues')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesFilters(TeaModel):
    def __init__(self, custom_slsfilters=None, custom_slsgroup_by_dimensions=None, custom_slswheres=None,
                 dim_filters=None):
        self.custom_slsfilters = custom_slsfilters  # type: list[GetAlertRulesResponseBodyPageBeanAlertRulesFiltersCustomSLSFilters]
        self.custom_slsgroup_by_dimensions = custom_slsgroup_by_dimensions  # type: list[str]
        self.custom_slswheres = custom_slswheres  # type: list[str]
        self.dim_filters = dim_filters  # type: list[GetAlertRulesResponseBodyPageBeanAlertRulesFiltersDimFilters]

    def validate(self):
        if self.custom_slsfilters:
            for k in self.custom_slsfilters:
                if k:
                    k.validate()
        if self.dim_filters:
            for k in self.dim_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAlertRulesResponseBodyPageBeanAlertRulesFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomSLSFilters'] = []
        if self.custom_slsfilters is not None:
            for k in self.custom_slsfilters:
                result['CustomSLSFilters'].append(k.to_map() if k else None)
        if self.custom_slsgroup_by_dimensions is not None:
            result['CustomSLSGroupByDimensions'] = self.custom_slsgroup_by_dimensions
        if self.custom_slswheres is not None:
            result['CustomSLSWheres'] = self.custom_slswheres
        result['DimFilters'] = []
        if self.dim_filters is not None:
            for k in self.dim_filters:
                result['DimFilters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_slsfilters = []
        if m.get('CustomSLSFilters') is not None:
            for k in m.get('CustomSLSFilters'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesFiltersCustomSLSFilters()
                self.custom_slsfilters.append(temp_model.from_map(k))
        if m.get('CustomSLSGroupByDimensions') is not None:
            self.custom_slsgroup_by_dimensions = m.get('CustomSLSGroupByDimensions')
        if m.get('CustomSLSWheres') is not None:
            self.custom_slswheres = m.get('CustomSLSWheres')
        self.dim_filters = []
        if m.get('DimFilters') is not None:
            for k in m.get('DimFilters'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesFiltersDimFilters()
                self.dim_filters.append(temp_model.from_map(k))
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAlertRulesResponseBodyPageBeanAlertRulesLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRules(TeaModel):
    def __init__(self, alert_check_type=None, alert_group=None, alert_id=None, alert_name=None,
                 alert_rule_content=None, alert_status=None, alert_type=None, annotations=None, auto_add_new_application=None,
                 cluster_id=None, created_time=None, duration=None, extend=None, filters=None, labels=None, level=None,
                 message=None, metrics_type=None, notify_strategy=None, pids=None, prom_ql=None, region_id=None,
                 updated_time=None, user_id=None):
        self.alert_check_type = alert_check_type  # type: str
        self.alert_group = alert_group  # type: long
        self.alert_id = alert_id  # type: float
        self.alert_name = alert_name  # type: str
        self.alert_rule_content = alert_rule_content  # type: GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContent
        self.alert_status = alert_status  # type: str
        self.alert_type = alert_type  # type: str
        self.annotations = annotations  # type: list[GetAlertRulesResponseBodyPageBeanAlertRulesAnnotations]
        self.auto_add_new_application = auto_add_new_application  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.created_time = created_time  # type: long
        self.duration = duration  # type: str
        self.extend = extend  # type: str
        self.filters = filters  # type: GetAlertRulesResponseBodyPageBeanAlertRulesFilters
        self.labels = labels  # type: list[GetAlertRulesResponseBodyPageBeanAlertRulesLabels]
        self.level = level  # type: str
        self.message = message  # type: str
        self.metrics_type = metrics_type  # type: str
        self.notify_strategy = notify_strategy  # type: str
        self.pids = pids  # type: list[str]
        self.prom_ql = prom_ql  # type: str
        self.region_id = region_id  # type: str
        self.updated_time = updated_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        if self.alert_rule_content:
            self.alert_rule_content.validate()
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.filters:
            self.filters.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAlertRulesResponseBodyPageBeanAlertRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_check_type is not None:
            result['AlertCheckType'] = self.alert_check_type
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_rule_content is not None:
            result['AlertRuleContent'] = self.alert_rule_content.to_map()
        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.auto_add_new_application is not None:
            result['AutoAddNewApplication'] = self.auto_add_new_application
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.filters is not None:
            result['Filters'] = self.filters.to_map()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.metrics_type is not None:
            result['MetricsType'] = self.metrics_type
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.pids is not None:
            result['Pids'] = self.pids
        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertCheckType') is not None:
            self.alert_check_type = m.get('AlertCheckType')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertRuleContent') is not None:
            temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContent()
            self.alert_rule_content = temp_model.from_map(m['AlertRuleContent'])
        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('AutoAddNewApplication') is not None:
            self.auto_add_new_application = m.get('AutoAddNewApplication')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Filters') is not None:
            temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesFilters()
            self.filters = temp_model.from_map(m['Filters'])
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MetricsType') is not None:
            self.metrics_type = m.get('MetricsType')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetAlertRulesResponseBodyPageBean(TeaModel):
    def __init__(self, alert_rules=None, page=None, size=None, total=None):
        self.alert_rules = alert_rules  # type: list[GetAlertRulesResponseBodyPageBeanAlertRules]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.alert_rules:
            for k in self.alert_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAlertRulesResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertRules'] = []
        if self.alert_rules is not None:
            for k in self.alert_rules:
                result['AlertRules'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alert_rules = []
        if m.get('AlertRules') is not None:
            for k in m.get('AlertRules'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRules()
                self.alert_rules.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAlertRulesResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: GetAlertRulesResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(GetAlertRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = GetAlertRulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAlertRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAlertRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAlertRulesResponse, self).to_map()
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
            temp_model = GetAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppApiByPageRequest(TeaModel):
    def __init__(self, current_page=None, end_time=None, interval_mills=None, pid=None, page_size=None,
                 region_id=None, start_time=None):
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.interval_mills = interval_mills  # type: int
        self.pid = pid  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppApiByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval_mills is not None:
            result['IntervalMills'] = self.interval_mills
        if self.pid is not None:
            result['PId'] = self.pid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IntervalMills') is not None:
            self.interval_mills = m.get('IntervalMills')
        if m.get('PId') is not None:
            self.pid = m.get('PId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetAppApiByPageResponseBodyData(TeaModel):
    def __init__(self, items=None, page=None, page_size=None, total=None):
        self.items = items  # type: list[dict[str, any]]
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppApiByPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAppApiByPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetAppApiByPageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAppApiByPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetAppApiByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAppApiByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppApiByPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppApiByPageResponse, self).to_map()
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
            temp_model = GetAppApiByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthTokenRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthTokenRequest, self).to_map()
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


class GetAuthTokenResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuthTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAuthTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuthTokenResponse, self).to_map()
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
            temp_model = GetAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterAllUrlRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterAllUrlRequest, self).to_map()
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


class GetClusterAllUrlResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterAllUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetClusterAllUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetClusterAllUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClusterAllUrlResponse, self).to_map()
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
            temp_model = GetClusterAllUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExploreUrlRequest(TeaModel):
    def __init__(self, cluster_id=None, expression=None, region_id=None, type=None):
        self.cluster_id = cluster_id  # type: str
        self.expression = expression  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExploreUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetExploreUrlResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExploreUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExploreUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetExploreUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExploreUrlResponse, self).to_map()
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
            temp_model = GetExploreUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIntegrationStateRequest(TeaModel):
    def __init__(self, cluster_id=None, integration=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.integration = integration  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIntegrationStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIntegrationStateResponseBody(TeaModel):
    def __init__(self, request_id=None, state=None):
        self.request_id = request_id  # type: str
        self.state = state  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIntegrationStateResponseBody, self).to_map()
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


class GetIntegrationStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIntegrationStateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIntegrationStateResponse, self).to_map()
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
            temp_model = GetIntegrationStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetManagedPrometheusStatusRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_type = cluster_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetManagedPrometheusStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetManagedPrometheusStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetManagedPrometheusStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetManagedPrometheusStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetManagedPrometheusStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetManagedPrometheusStatusResponse, self).to_map()
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
            temp_model = GetManagedPrometheusStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultipleTraceRequest(TeaModel):
    def __init__(self, region_id=None, trace_ids=None):
        self.region_id = region_id  # type: str
        self.trace_ids = trace_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMultipleTraceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_ids is not None:
            result['TraceIDs'] = self.trace_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceIDs') is not None:
            self.trace_ids = m.get('TraceIDs')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList, self).to_map()
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


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList(TeaModel):
    def __init__(self, tag_entry_list=None, timestamp=None):
        self.tag_entry_list = tag_entry_list  # type: list[GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList]
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList, self).to_map()
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


class GetMultipleTraceResponseBodyMultiCallChainInfosSpans(TeaModel):
    def __init__(self, duration=None, have_stack=None, log_event_list=None, operation_name=None,
                 parent_span_id=None, result_code=None, rpc_id=None, rpc_type=None, service_ip=None, service_name=None,
                 span_id=None, tag_entry_list=None, timestamp=None, trace_id=None):
        self.duration = duration  # type: long
        self.have_stack = have_stack  # type: bool
        self.log_event_list = log_event_list  # type: list[GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList]
        self.operation_name = operation_name  # type: str
        self.parent_span_id = parent_span_id  # type: str
        self.result_code = result_code  # type: str
        self.rpc_id = rpc_id  # type: str
        self.rpc_type = rpc_type  # type: int
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.span_id = span_id  # type: str
        self.tag_entry_list = tag_entry_list  # type: list[GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList]
        self.timestamp = timestamp  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.log_event_list:
            for k in self.log_event_list:
                if k:
                    k.validate()
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMultipleTraceResponseBodyMultiCallChainInfosSpans, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        result['LogEventList'] = []
        if self.log_event_list is not None:
            for k in self.log_event_list:
                result['LogEventList'].append(k.to_map() if k else None)
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        self.log_event_list = []
        if m.get('LogEventList') is not None:
            for k in m.get('LogEventList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k))
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfos(TeaModel):
    def __init__(self, spans=None, trace_id=None):
        self.spans = spans  # type: list[GetMultipleTraceResponseBodyMultiCallChainInfosSpans]
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.spans:
            for k in self.spans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMultipleTraceResponseBodyMultiCallChainInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Spans'] = []
        if self.spans is not None:
            for k in self.spans:
                result['Spans'].append(k.to_map() if k else None)
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.spans = []
        if m.get('Spans') is not None:
            for k in m.get('Spans'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpans()
                self.spans.append(temp_model.from_map(k))
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetMultipleTraceResponseBody(TeaModel):
    def __init__(self, multi_call_chain_infos=None, request_id=None):
        self.multi_call_chain_infos = multi_call_chain_infos  # type: list[GetMultipleTraceResponseBodyMultiCallChainInfos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.multi_call_chain_infos:
            for k in self.multi_call_chain_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMultipleTraceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MultiCallChainInfos'] = []
        if self.multi_call_chain_infos is not None:
            for k in self.multi_call_chain_infos:
                result['MultiCallChainInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.multi_call_chain_infos = []
        if m.get('MultiCallChainInfos') is not None:
            for k in m.get('MultiCallChainInfos'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfos()
                self.multi_call_chain_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMultipleTraceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMultipleTraceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMultipleTraceResponse, self).to_map()
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
            temp_model = GetMultipleTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOnCallSchedulesDetailRequest(TeaModel):
    def __init__(self, end_time=None, id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.id = id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntriesSimpleContact(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntriesSimpleContact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntries(TeaModel):
    def __init__(self, end=None, simple_contact=None, start=None):
        self.end = end  # type: str
        self.simple_contact = simple_contact  # type: GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntriesSimpleContact
        self.start = start  # type: str

    def validate(self):
        if self.simple_contact:
            self.simple_contact.validate()

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.simple_contact is not None:
            result['SimpleContact'] = self.simple_contact.to_map()
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SimpleContact') is not None:
            temp_model = GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntriesSimpleContact()
            self.simple_contact = temp_model.from_map(m['SimpleContact'])
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntriesSimpleContact(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntriesSimpleContact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntries(TeaModel):
    def __init__(self, start=None, end=None, simple_contact=None):
        self.start = start  # type: str
        self.end = end  # type: str
        self.simple_contact = simple_contact  # type: GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntriesSimpleContact

    def validate(self):
        if self.simple_contact:
            self.simple_contact.validate()

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.end is not None:
            result['End'] = self.end
        if self.simple_contact is not None:
            result['SimpleContact'] = self.simple_contact.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SimpleContact') is not None:
            temp_model = GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntriesSimpleContact()
            self.simple_contact = temp_model.from_map(m['SimpleContact'])
        return self


class GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntriesSimpleContact(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntriesSimpleContact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntries(TeaModel):
    def __init__(self, end=None, simple_contact=None, start=None):
        self.end = end  # type: str
        self.simple_contact = simple_contact  # type: GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntriesSimpleContact
        self.start = start  # type: str

    def validate(self):
        if self.simple_contact:
            self.simple_contact.validate()

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.simple_contact is not None:
            result['SimpleContact'] = self.simple_contact.to_map()
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('SimpleContact') is not None:
            temp_model = GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntriesSimpleContact()
            self.simple_contact = temp_model.from_map(m['SimpleContact'])
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetOnCallSchedulesDetailResponseBodyDataScheduleLayersRestrictions(TeaModel):
    def __init__(self, end_time_of_day=None, restriction_type=None, start_time_of_day=None):
        self.end_time_of_day = end_time_of_day  # type: str
        self.restriction_type = restriction_type  # type: str
        self.start_time_of_day = start_time_of_day  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponseBodyDataScheduleLayersRestrictions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time_of_day is not None:
            result['EndTimeOfDay'] = self.end_time_of_day
        if self.restriction_type is not None:
            result['RestrictionType'] = self.restriction_type
        if self.start_time_of_day is not None:
            result['StartTimeOfDay'] = self.start_time_of_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimeOfDay') is not None:
            self.end_time_of_day = m.get('EndTimeOfDay')
        if m.get('RestrictionType') is not None:
            self.restriction_type = m.get('RestrictionType')
        if m.get('StartTimeOfDay') is not None:
            self.start_time_of_day = m.get('StartTimeOfDay')
        return self


class GetOnCallSchedulesDetailResponseBodyDataScheduleLayers(TeaModel):
    def __init__(self, contact_ids=None, restrictions=None, rotation_type=None, shift_length=None, start_time=None):
        self.contact_ids = contact_ids  # type: list[long]
        self.restrictions = restrictions  # type: list[GetOnCallSchedulesDetailResponseBodyDataScheduleLayersRestrictions]
        self.rotation_type = rotation_type  # type: str
        self.shift_length = shift_length  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        if self.restrictions:
            for k in self.restrictions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponseBodyDataScheduleLayers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        result['Restrictions'] = []
        if self.restrictions is not None:
            for k in self.restrictions:
                result['Restrictions'].append(k.to_map() if k else None)
        if self.rotation_type is not None:
            result['RotationType'] = self.rotation_type
        if self.shift_length is not None:
            result['ShiftLength'] = self.shift_length
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        self.restrictions = []
        if m.get('Restrictions') is not None:
            for k in m.get('Restrictions'):
                temp_model = GetOnCallSchedulesDetailResponseBodyDataScheduleLayersRestrictions()
                self.restrictions.append(temp_model.from_map(k))
        if m.get('RotationType') is not None:
            self.rotation_type = m.get('RotationType')
        if m.get('ShiftLength') is not None:
            self.shift_length = m.get('ShiftLength')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetOnCallSchedulesDetailResponseBodyData(TeaModel):
    def __init__(self, alert_robot_id=None, description=None, id=None, name=None, rendered_finnal_entries=None,
                 rendered_layer_entries=None, rendered_substitude_entries=None, schedule_layers=None):
        self.alert_robot_id = alert_robot_id  # type: long
        self.description = description  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.rendered_finnal_entries = rendered_finnal_entries  # type: list[GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntries]
        self.rendered_layer_entries = rendered_layer_entries  # type: list[list[GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntries]]
        self.rendered_substitude_entries = rendered_substitude_entries  # type: list[GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntries]
        self.schedule_layers = schedule_layers  # type: list[GetOnCallSchedulesDetailResponseBodyDataScheduleLayers]

    def validate(self):
        if self.rendered_finnal_entries:
            for k in self.rendered_finnal_entries:
                if k:
                    k.validate()
        if self.rendered_layer_entries:
            for k in self.rendered_layer_entries:
                for k1 in k:
                    if k1:
                        k1.validate()
        if self.rendered_substitude_entries:
            for k in self.rendered_substitude_entries:
                if k:
                    k.validate()
        if self.schedule_layers:
            for k in self.schedule_layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_robot_id is not None:
            result['AlertRobotId'] = self.alert_robot_id
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        result['RenderedFinnalEntries'] = []
        if self.rendered_finnal_entries is not None:
            for k in self.rendered_finnal_entries:
                result['RenderedFinnalEntries'].append(k.to_map() if k else None)
        result['RenderedLayerEntries'] = []
        if self.rendered_layer_entries is not None:
            for k in self.rendered_layer_entries:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['renderedLayerEntries'].append(l1)
        result['RenderedSubstitudeEntries'] = []
        if self.rendered_substitude_entries is not None:
            for k in self.rendered_substitude_entries:
                result['RenderedSubstitudeEntries'].append(k.to_map() if k else None)
        result['ScheduleLayers'] = []
        if self.schedule_layers is not None:
            for k in self.schedule_layers:
                result['ScheduleLayers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertRobotId') is not None:
            self.alert_robot_id = m.get('AlertRobotId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.rendered_finnal_entries = []
        if m.get('RenderedFinnalEntries') is not None:
            for k in m.get('RenderedFinnalEntries'):
                temp_model = GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntries()
                self.rendered_finnal_entries.append(temp_model.from_map(k))
        self.rendered_layer_entries = []
        if m.get('RenderedLayerEntries') is not None:
            for k in m.get('RenderedLayerEntries'):
                l1 = []
                for k1 in k:
                    temp_model = GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntries()
                    l1.append(temp_model.from_map(k1))
                self.rendered_layer_entries.append(l1)
        self.rendered_substitude_entries = []
        if m.get('RenderedSubstitudeEntries') is not None:
            for k in m.get('RenderedSubstitudeEntries'):
                temp_model = GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntries()
                self.rendered_substitude_entries.append(temp_model.from_map(k))
        self.schedule_layers = []
        if m.get('ScheduleLayers') is not None:
            for k in m.get('ScheduleLayers'):
                temp_model = GetOnCallSchedulesDetailResponseBodyDataScheduleLayers()
                self.schedule_layers.append(temp_model.from_map(k))
        return self


class GetOnCallSchedulesDetailResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetOnCallSchedulesDetailResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetOnCallSchedulesDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOnCallSchedulesDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOnCallSchedulesDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOnCallSchedulesDetailResponse, self).to_map()
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
            temp_model = GetOnCallSchedulesDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrometheusApiTokenRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrometheusApiTokenRequest, self).to_map()
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


class GetPrometheusApiTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, token=None):
        self.request_id = request_id  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrometheusApiTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetPrometheusApiTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPrometheusApiTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPrometheusApiTokenResponse, self).to_map()
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
            temp_model = GetPrometheusApiTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrometheusGlobalViewRequest(TeaModel):
    def __init__(self, global_view_cluster_id=None, region_id=None):
        self.global_view_cluster_id = global_view_cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrometheusGlobalViewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrometheusGlobalViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPrometheusGlobalViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPrometheusGlobalViewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPrometheusGlobalViewResponse, self).to_map()
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
            temp_model = GetPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecordingRuleRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRecordingRuleRequest, self).to_map()
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


class GetRecordingRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRecordingRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRecordingRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRecordingRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRecordingRuleResponse, self).to_map()
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
            temp_model = GetRecordingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRetcodeShareUrlRequest(TeaModel):
    def __init__(self, pid=None):
        self.pid = pid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRetcodeShareUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class GetRetcodeShareUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, url=None):
        self.request_id = request_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRetcodeShareUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetRetcodeShareUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRetcodeShareUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRetcodeShareUrlResponse, self).to_map()
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
            temp_model = GetRetcodeShareUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSourceMapInfoRequest(TeaModel):
    def __init__(self, ascending_sequence=None, edition=None, id=None, keyword=None, order_field=None,
                 region_id=None):
        self.ascending_sequence = ascending_sequence  # type: bool
        self.edition = edition  # type: str
        self.id = id  # type: str
        self.keyword = keyword  # type: str
        self.order_field = order_field  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSourceMapInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ascending_sequence is not None:
            result['AscendingSequence'] = self.ascending_sequence
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.id is not None:
            result['ID'] = self.id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AscendingSequence') is not None:
            self.ascending_sequence = m.get('AscendingSequence')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetSourceMapInfoResponseBodySourceMapList(TeaModel):
    def __init__(self, fid=None, file_name=None, size=None, upload_time=None, version=None):
        self.fid = fid  # type: str
        self.file_name = file_name  # type: str
        self.size = size  # type: str
        self.upload_time = upload_time  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSourceMapInfoResponseBodySourceMapList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fid is not None:
            result['Fid'] = self.fid
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.size is not None:
            result['Size'] = self.size
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fid') is not None:
            self.fid = m.get('Fid')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetSourceMapInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, source_map_list=None):
        self.request_id = request_id  # type: str
        self.source_map_list = source_map_list  # type: list[GetSourceMapInfoResponseBodySourceMapList]

    def validate(self):
        if self.source_map_list:
            for k in self.source_map_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSourceMapInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SourceMapList'] = []
        if self.source_map_list is not None:
            for k in self.source_map_list:
                result['SourceMapList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.source_map_list = []
        if m.get('SourceMapList') is not None:
            for k in m.get('SourceMapList'):
                temp_model = GetSourceMapInfoResponseBodySourceMapList()
                self.source_map_list.append(temp_model.from_map(k))
        return self


class GetSourceMapInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSourceMapInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSourceMapInfoResponse, self).to_map()
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
            temp_model = GetSourceMapInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackRequest(TeaModel):
    def __init__(self, end_time=None, pid=None, region_id=None, rpc_id=None, start_time=None, trace_id=None):
        self.end_time = end_time  # type: long
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.rpc_id = rpc_id  # type: str
        self.start_time = start_time  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rpc_id is not None:
            result['RpcID'] = self.rpc_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RpcID') is not None:
            self.rpc_id = m.get('RpcID')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetStackResponseBodyStackInfoExtInfo(TeaModel):
    def __init__(self, info=None, type=None):
        self.info = info  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackResponseBodyStackInfoExtInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetStackResponseBodyStackInfo(TeaModel):
    def __init__(self, api=None, duration=None, exception=None, ext_info=None, line=None, rpc_id=None,
                 service_name=None, start_time=None):
        self.api = api  # type: str
        self.duration = duration  # type: long
        self.exception = exception  # type: str
        self.ext_info = ext_info  # type: GetStackResponseBodyStackInfoExtInfo
        self.line = line  # type: str
        self.rpc_id = rpc_id  # type: str
        self.service_name = service_name  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()

    def to_map(self):
        _map = super(GetStackResponseBodyStackInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['Api'] = self.api
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.exception is not None:
            result['Exception'] = self.exception
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info.to_map()
        if self.line is not None:
            result['Line'] = self.line
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Exception') is not None:
            self.exception = m.get('Exception')
        if m.get('ExtInfo') is not None:
            temp_model = GetStackResponseBodyStackInfoExtInfo()
            self.ext_info = temp_model.from_map(m['ExtInfo'])
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetStackResponseBody(TeaModel):
    def __init__(self, request_id=None, stack_info=None):
        self.request_id = request_id  # type: str
        self.stack_info = stack_info  # type: list[GetStackResponseBodyStackInfo]

    def validate(self):
        if self.stack_info:
            for k in self.stack_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetStackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StackInfo'] = []
        if self.stack_info is not None:
            for k in self.stack_info:
                result['StackInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stack_info = []
        if m.get('StackInfo') is not None:
            for k in m.get('StackInfo'):
                temp_model = GetStackResponseBodyStackInfo()
                self.stack_info.append(temp_model.from_map(k))
        return self


class GetStackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStackResponse, self).to_map()
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
            temp_model = GetStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSyntheticTaskDetailRequest(TeaModel):
    def __init__(self, region_id=None, task_id=None):
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetSyntheticTaskDetailResponseBodyTaskDetailDownload(TeaModel):
    def __init__(self, connection_timeout=None, download_custom_header_content=None, download_custom_host=None,
                 download_custom_host_ip=None, download_kernel=None, download_redirect=None, download_transmission_size=None,
                 monitor_timeout=None, quick_protocol=None, validate_keywords=None, verify_way=None, white_list=None):
        self.connection_timeout = connection_timeout  # type: long
        self.download_custom_header_content = download_custom_header_content  # type: str
        self.download_custom_host = download_custom_host  # type: long
        self.download_custom_host_ip = download_custom_host_ip  # type: str
        self.download_kernel = download_kernel  # type: long
        self.download_redirect = download_redirect  # type: long
        self.download_transmission_size = download_transmission_size  # type: long
        self.monitor_timeout = monitor_timeout  # type: long
        self.quick_protocol = quick_protocol  # type: str
        self.validate_keywords = validate_keywords  # type: str
        self.verify_way = verify_way  # type: long
        self.white_list = white_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailDownload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_timeout is not None:
            result['ConnectionTimeout'] = self.connection_timeout
        if self.download_custom_header_content is not None:
            result['DownloadCustomHeaderContent'] = self.download_custom_header_content
        if self.download_custom_host is not None:
            result['DownloadCustomHost'] = self.download_custom_host
        if self.download_custom_host_ip is not None:
            result['DownloadCustomHostIp'] = self.download_custom_host_ip
        if self.download_kernel is not None:
            result['DownloadKernel'] = self.download_kernel
        if self.download_redirect is not None:
            result['DownloadRedirect'] = self.download_redirect
        if self.download_transmission_size is not None:
            result['DownloadTransmissionSize'] = self.download_transmission_size
        if self.monitor_timeout is not None:
            result['MonitorTimeout'] = self.monitor_timeout
        if self.quick_protocol is not None:
            result['QuickProtocol'] = self.quick_protocol
        if self.validate_keywords is not None:
            result['ValidateKeywords'] = self.validate_keywords
        if self.verify_way is not None:
            result['VerifyWay'] = self.verify_way
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionTimeout') is not None:
            self.connection_timeout = m.get('ConnectionTimeout')
        if m.get('DownloadCustomHeaderContent') is not None:
            self.download_custom_header_content = m.get('DownloadCustomHeaderContent')
        if m.get('DownloadCustomHost') is not None:
            self.download_custom_host = m.get('DownloadCustomHost')
        if m.get('DownloadCustomHostIp') is not None:
            self.download_custom_host_ip = m.get('DownloadCustomHostIp')
        if m.get('DownloadKernel') is not None:
            self.download_kernel = m.get('DownloadKernel')
        if m.get('DownloadRedirect') is not None:
            self.download_redirect = m.get('DownloadRedirect')
        if m.get('DownloadTransmissionSize') is not None:
            self.download_transmission_size = m.get('DownloadTransmissionSize')
        if m.get('MonitorTimeout') is not None:
            self.monitor_timeout = m.get('MonitorTimeout')
        if m.get('QuickProtocol') is not None:
            self.quick_protocol = m.get('QuickProtocol')
        if m.get('ValidateKeywords') is not None:
            self.validate_keywords = m.get('ValidateKeywords')
        if m.get('VerifyWay') is not None:
            self.verify_way = m.get('VerifyWay')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class GetSyntheticTaskDetailResponseBodyTaskDetailExtendInterval(TeaModel):
    def __init__(self, days=None, end_minute=None, end_time=None, endhour=None, start_hour=None, start_minute=None,
                 start_time=None):
        self.days = days  # type: list[long]
        self.end_minute = end_minute  # type: long
        self.end_time = end_time  # type: str
        self.endhour = endhour  # type: long
        self.start_hour = start_hour  # type: long
        self.start_minute = start_minute  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailExtendInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days is not None:
            result['Days'] = self.days
        if self.end_minute is not None:
            result['EndMinute'] = self.end_minute
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.endhour is not None:
            result['Endhour'] = self.endhour
        if self.start_hour is not None:
            result['StartHour'] = self.start_hour
        if self.start_minute is not None:
            result['StartMinute'] = self.start_minute
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('EndMinute') is not None:
            self.end_minute = m.get('EndMinute')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Endhour') is not None:
            self.endhour = m.get('Endhour')
        if m.get('StartHour') is not None:
            self.start_hour = m.get('StartHour')
        if m.get('StartMinute') is not None:
            self.start_minute = m.get('StartMinute')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetSyntheticTaskDetailResponseBodyTaskDetailMinotorList(TeaModel):
    def __init__(self, city_code=None, monitor_type=None, net_service_id=None, send_count=None):
        self.city_code = city_code  # type: long
        self.monitor_type = monitor_type  # type: long
        self.net_service_id = net_service_id  # type: long
        self.send_count = send_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailMinotorList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.net_service_id is not None:
            result['NetServiceId'] = self.net_service_id
        if self.send_count is not None:
            result['SendCount'] = self.send_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('NetServiceId') is not None:
            self.net_service_id = m.get('NetServiceId')
        if m.get('SendCount') is not None:
            self.send_count = m.get('SendCount')
        return self


class GetSyntheticTaskDetailResponseBodyTaskDetailNav(TeaModel):
    def __init__(self, dns_hijack_whitelist=None, element_blacklist=None, execute_active_x=None,
                 execute_applet=None, execute_script=None, filter_invalid_ip=None, flow_hijack_jump_times=None,
                 flow_hijack_logo=None, monitor_timeout=None, nav_automatic_scrolling=None, nav_custom_header=None,
                 nav_custom_header_content=None, nav_custom_host=None, nav_custom_host_ip=None, nav_disable_cache=None,
                 nav_disable_compression=None, nav_ignore_certificate_error=None, nav_redirect=None, nav_return_element=None,
                 page_tampering=None, process_name=None, quic_domain=None, quic_version=None, request_header=None,
                 slow_element_threshold=None, verify_string_blacklist=None, verify_string_whitelist=None, wait_completion_time=None):
        self.dns_hijack_whitelist = dns_hijack_whitelist  # type: str
        self.element_blacklist = element_blacklist  # type: str
        self.execute_active_x = execute_active_x  # type: long
        self.execute_applet = execute_applet  # type: long
        self.execute_script = execute_script  # type: long
        self.filter_invalid_ip = filter_invalid_ip  # type: long
        self.flow_hijack_jump_times = flow_hijack_jump_times  # type: long
        self.flow_hijack_logo = flow_hijack_logo  # type: str
        self.monitor_timeout = monitor_timeout  # type: long
        self.nav_automatic_scrolling = nav_automatic_scrolling  # type: long
        self.nav_custom_header = nav_custom_header  # type: str
        self.nav_custom_header_content = nav_custom_header_content  # type: str
        self.nav_custom_host = nav_custom_host  # type: long
        self.nav_custom_host_ip = nav_custom_host_ip  # type: str
        self.nav_disable_cache = nav_disable_cache  # type: long
        self.nav_disable_compression = nav_disable_compression  # type: long
        self.nav_ignore_certificate_error = nav_ignore_certificate_error  # type: long
        self.nav_redirect = nav_redirect  # type: long
        self.nav_return_element = nav_return_element  # type: long
        self.page_tampering = page_tampering  # type: str
        self.process_name = process_name  # type: str
        self.quic_domain = quic_domain  # type: str
        self.quic_version = quic_version  # type: long
        self.request_header = request_header  # type: long
        self.slow_element_threshold = slow_element_threshold  # type: long
        self.verify_string_blacklist = verify_string_blacklist  # type: str
        self.verify_string_whitelist = verify_string_whitelist  # type: str
        self.wait_completion_time = wait_completion_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailNav, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_hijack_whitelist is not None:
            result['DnsHijackWhitelist'] = self.dns_hijack_whitelist
        if self.element_blacklist is not None:
            result['ElementBlacklist'] = self.element_blacklist
        if self.execute_active_x is not None:
            result['ExecuteActiveX'] = self.execute_active_x
        if self.execute_applet is not None:
            result['ExecuteApplet'] = self.execute_applet
        if self.execute_script is not None:
            result['ExecuteScript'] = self.execute_script
        if self.filter_invalid_ip is not None:
            result['FilterInvalidIP'] = self.filter_invalid_ip
        if self.flow_hijack_jump_times is not None:
            result['FlowHijackJumpTimes'] = self.flow_hijack_jump_times
        if self.flow_hijack_logo is not None:
            result['FlowHijackLogo'] = self.flow_hijack_logo
        if self.monitor_timeout is not None:
            result['MonitorTimeout'] = self.monitor_timeout
        if self.nav_automatic_scrolling is not None:
            result['NavAutomaticScrolling'] = self.nav_automatic_scrolling
        if self.nav_custom_header is not None:
            result['NavCustomHeader'] = self.nav_custom_header
        if self.nav_custom_header_content is not None:
            result['NavCustomHeaderContent'] = self.nav_custom_header_content
        if self.nav_custom_host is not None:
            result['NavCustomHost'] = self.nav_custom_host
        if self.nav_custom_host_ip is not None:
            result['NavCustomHostIp'] = self.nav_custom_host_ip
        if self.nav_disable_cache is not None:
            result['NavDisableCache'] = self.nav_disable_cache
        if self.nav_disable_compression is not None:
            result['NavDisableCompression'] = self.nav_disable_compression
        if self.nav_ignore_certificate_error is not None:
            result['NavIgnoreCertificateError'] = self.nav_ignore_certificate_error
        if self.nav_redirect is not None:
            result['NavRedirect'] = self.nav_redirect
        if self.nav_return_element is not None:
            result['NavReturnElement'] = self.nav_return_element
        if self.page_tampering is not None:
            result['PageTampering'] = self.page_tampering
        if self.process_name is not None:
            result['ProcessName'] = self.process_name
        if self.quic_domain is not None:
            result['QuicDomain'] = self.quic_domain
        if self.quic_version is not None:
            result['QuicVersion'] = self.quic_version
        if self.request_header is not None:
            result['RequestHeader'] = self.request_header
        if self.slow_element_threshold is not None:
            result['SlowElementThreshold'] = self.slow_element_threshold
        if self.verify_string_blacklist is not None:
            result['VerifyStringBlacklist'] = self.verify_string_blacklist
        if self.verify_string_whitelist is not None:
            result['VerifyStringWhitelist'] = self.verify_string_whitelist
        if self.wait_completion_time is not None:
            result['WaitCompletionTime'] = self.wait_completion_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsHijackWhitelist') is not None:
            self.dns_hijack_whitelist = m.get('DnsHijackWhitelist')
        if m.get('ElementBlacklist') is not None:
            self.element_blacklist = m.get('ElementBlacklist')
        if m.get('ExecuteActiveX') is not None:
            self.execute_active_x = m.get('ExecuteActiveX')
        if m.get('ExecuteApplet') is not None:
            self.execute_applet = m.get('ExecuteApplet')
        if m.get('ExecuteScript') is not None:
            self.execute_script = m.get('ExecuteScript')
        if m.get('FilterInvalidIP') is not None:
            self.filter_invalid_ip = m.get('FilterInvalidIP')
        if m.get('FlowHijackJumpTimes') is not None:
            self.flow_hijack_jump_times = m.get('FlowHijackJumpTimes')
        if m.get('FlowHijackLogo') is not None:
            self.flow_hijack_logo = m.get('FlowHijackLogo')
        if m.get('MonitorTimeout') is not None:
            self.monitor_timeout = m.get('MonitorTimeout')
        if m.get('NavAutomaticScrolling') is not None:
            self.nav_automatic_scrolling = m.get('NavAutomaticScrolling')
        if m.get('NavCustomHeader') is not None:
            self.nav_custom_header = m.get('NavCustomHeader')
        if m.get('NavCustomHeaderContent') is not None:
            self.nav_custom_header_content = m.get('NavCustomHeaderContent')
        if m.get('NavCustomHost') is not None:
            self.nav_custom_host = m.get('NavCustomHost')
        if m.get('NavCustomHostIp') is not None:
            self.nav_custom_host_ip = m.get('NavCustomHostIp')
        if m.get('NavDisableCache') is not None:
            self.nav_disable_cache = m.get('NavDisableCache')
        if m.get('NavDisableCompression') is not None:
            self.nav_disable_compression = m.get('NavDisableCompression')
        if m.get('NavIgnoreCertificateError') is not None:
            self.nav_ignore_certificate_error = m.get('NavIgnoreCertificateError')
        if m.get('NavRedirect') is not None:
            self.nav_redirect = m.get('NavRedirect')
        if m.get('NavReturnElement') is not None:
            self.nav_return_element = m.get('NavReturnElement')
        if m.get('PageTampering') is not None:
            self.page_tampering = m.get('PageTampering')
        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')
        if m.get('QuicDomain') is not None:
            self.quic_domain = m.get('QuicDomain')
        if m.get('QuicVersion') is not None:
            self.quic_version = m.get('QuicVersion')
        if m.get('RequestHeader') is not None:
            self.request_header = m.get('RequestHeader')
        if m.get('SlowElementThreshold') is not None:
            self.slow_element_threshold = m.get('SlowElementThreshold')
        if m.get('VerifyStringBlacklist') is not None:
            self.verify_string_blacklist = m.get('VerifyStringBlacklist')
        if m.get('VerifyStringWhitelist') is not None:
            self.verify_string_whitelist = m.get('VerifyStringWhitelist')
        if m.get('WaitCompletionTime') is not None:
            self.wait_completion_time = m.get('WaitCompletionTime')
        return self


class GetSyntheticTaskDetailResponseBodyTaskDetailNet(TeaModel):
    def __init__(self, net_dig_switch=None, net_dns_ns=None, net_dns_query_method=None, net_dns_server=None,
                 net_dns_switch=None, net_icmp_active=None, net_icmp_data_cut=None, net_icmp_interval=None, net_icmp_num=None,
                 net_icmp_size=None, net_icmp_switch=None, net_icmp_timeout=None, net_trace_route_num=None,
                 net_trace_route_switch=None, net_trace_route_timeout=None, white_list=None):
        self.net_dig_switch = net_dig_switch  # type: long
        self.net_dns_ns = net_dns_ns  # type: str
        self.net_dns_query_method = net_dns_query_method  # type: str
        self.net_dns_server = net_dns_server  # type: long
        self.net_dns_switch = net_dns_switch  # type: long
        self.net_icmp_active = net_icmp_active  # type: long
        self.net_icmp_data_cut = net_icmp_data_cut  # type: long
        self.net_icmp_interval = net_icmp_interval  # type: long
        self.net_icmp_num = net_icmp_num  # type: long
        self.net_icmp_size = net_icmp_size  # type: long
        self.net_icmp_switch = net_icmp_switch  # type: long
        self.net_icmp_timeout = net_icmp_timeout  # type: long
        self.net_trace_route_num = net_trace_route_num  # type: long
        self.net_trace_route_switch = net_trace_route_switch  # type: long
        self.net_trace_route_timeout = net_trace_route_timeout  # type: long
        self.white_list = white_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailNet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_dig_switch is not None:
            result['NetDigSwitch'] = self.net_dig_switch
        if self.net_dns_ns is not None:
            result['NetDnsNs'] = self.net_dns_ns
        if self.net_dns_query_method is not None:
            result['NetDnsQueryMethod'] = self.net_dns_query_method
        if self.net_dns_server is not None:
            result['NetDnsServer'] = self.net_dns_server
        if self.net_dns_switch is not None:
            result['NetDnsSwitch'] = self.net_dns_switch
        if self.net_icmp_active is not None:
            result['NetIcmpActive'] = self.net_icmp_active
        if self.net_icmp_data_cut is not None:
            result['NetIcmpDataCut'] = self.net_icmp_data_cut
        if self.net_icmp_interval is not None:
            result['NetIcmpInterval'] = self.net_icmp_interval
        if self.net_icmp_num is not None:
            result['NetIcmpNum'] = self.net_icmp_num
        if self.net_icmp_size is not None:
            result['NetIcmpSize'] = self.net_icmp_size
        if self.net_icmp_switch is not None:
            result['NetIcmpSwitch'] = self.net_icmp_switch
        if self.net_icmp_timeout is not None:
            result['NetIcmpTimeout'] = self.net_icmp_timeout
        if self.net_trace_route_num is not None:
            result['NetTraceRouteNum'] = self.net_trace_route_num
        if self.net_trace_route_switch is not None:
            result['NetTraceRouteSwitch'] = self.net_trace_route_switch
        if self.net_trace_route_timeout is not None:
            result['NetTraceRouteTimeout'] = self.net_trace_route_timeout
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetDigSwitch') is not None:
            self.net_dig_switch = m.get('NetDigSwitch')
        if m.get('NetDnsNs') is not None:
            self.net_dns_ns = m.get('NetDnsNs')
        if m.get('NetDnsQueryMethod') is not None:
            self.net_dns_query_method = m.get('NetDnsQueryMethod')
        if m.get('NetDnsServer') is not None:
            self.net_dns_server = m.get('NetDnsServer')
        if m.get('NetDnsSwitch') is not None:
            self.net_dns_switch = m.get('NetDnsSwitch')
        if m.get('NetIcmpActive') is not None:
            self.net_icmp_active = m.get('NetIcmpActive')
        if m.get('NetIcmpDataCut') is not None:
            self.net_icmp_data_cut = m.get('NetIcmpDataCut')
        if m.get('NetIcmpInterval') is not None:
            self.net_icmp_interval = m.get('NetIcmpInterval')
        if m.get('NetIcmpNum') is not None:
            self.net_icmp_num = m.get('NetIcmpNum')
        if m.get('NetIcmpSize') is not None:
            self.net_icmp_size = m.get('NetIcmpSize')
        if m.get('NetIcmpSwitch') is not None:
            self.net_icmp_switch = m.get('NetIcmpSwitch')
        if m.get('NetIcmpTimeout') is not None:
            self.net_icmp_timeout = m.get('NetIcmpTimeout')
        if m.get('NetTraceRouteNum') is not None:
            self.net_trace_route_num = m.get('NetTraceRouteNum')
        if m.get('NetTraceRouteSwitch') is not None:
            self.net_trace_route_switch = m.get('NetTraceRouteSwitch')
        if m.get('NetTraceRouteTimeout') is not None:
            self.net_trace_route_timeout = m.get('NetTraceRouteTimeout')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyFormdata(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyFormdata, self).to_map()
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


class GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyUrlencoded(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyUrlencoded, self).to_map()
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


class GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBody(TeaModel):
    def __init__(self, formdata=None, language=None, mode=None, raw=None, urlencoded=None):
        self.formdata = formdata  # type: GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyFormdata
        self.language = language  # type: str
        self.mode = mode  # type: str
        self.raw = raw  # type: str
        self.urlencoded = urlencoded  # type: GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyUrlencoded

    def validate(self):
        if self.formdata:
            self.formdata.validate()
        if self.urlencoded:
            self.urlencoded.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.formdata is not None:
            result['Formdata'] = self.formdata.to_map()
        if self.language is not None:
            result['Language'] = self.language
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.raw is not None:
            result['Raw'] = self.raw
        if self.urlencoded is not None:
            result['Urlencoded'] = self.urlencoded.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Formdata') is not None:
            temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyFormdata()
            self.formdata = temp_model.from_map(m['Formdata'])
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Raw') is not None:
            self.raw = m.get('Raw')
        if m.get('Urlencoded') is not None:
            temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyUrlencoded()
            self.urlencoded = temp_model.from_map(m['Urlencoded'])
        return self


class GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentHeader(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentHeader, self).to_map()
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


class GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContent(TeaModel):
    def __init__(self, body=None, header=None, method=None):
        self.body = body  # type: GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBody
        self.header = header  # type: list[GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentHeader]
        self.method = method  # type: str

    def validate(self):
        if self.body:
            self.body.validate()
        if self.header:
            for k in self.header:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        result['Header'] = []
        if self.header is not None:
            for k in self.header:
                result['Header'].append(k.to_map() if k else None)
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBody()
            self.body = temp_model.from_map(m['Body'])
        self.header = []
        if m.get('Header') is not None:
            for k in m.get('Header'):
                temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentHeader()
                self.header.append(temp_model.from_map(k))
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class GetSyntheticTaskDetailResponseBodyTaskDetailProtocol(TeaModel):
    def __init__(self, character_encoding=None, custom_host=None, custom_host_ip=None,
                 protocol_connection_timeout=None, protocol_monitor_timeout=None, received_data_size=None, request_content=None,
                 verify_content=None, verify_way=None):
        self.character_encoding = character_encoding  # type: long
        self.custom_host = custom_host  # type: long
        self.custom_host_ip = custom_host_ip  # type: str
        self.protocol_connection_timeout = protocol_connection_timeout  # type: long
        self.protocol_monitor_timeout = protocol_monitor_timeout  # type: long
        self.received_data_size = received_data_size  # type: long
        self.request_content = request_content  # type: GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContent
        self.verify_content = verify_content  # type: str
        self.verify_way = verify_way  # type: long

    def validate(self):
        if self.request_content:
            self.request_content.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetailProtocol, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_encoding is not None:
            result['CharacterEncoding'] = self.character_encoding
        if self.custom_host is not None:
            result['CustomHost'] = self.custom_host
        if self.custom_host_ip is not None:
            result['CustomHostIp'] = self.custom_host_ip
        if self.protocol_connection_timeout is not None:
            result['ProtocolConnectionTimeout'] = self.protocol_connection_timeout
        if self.protocol_monitor_timeout is not None:
            result['ProtocolMonitorTimeout'] = self.protocol_monitor_timeout
        if self.received_data_size is not None:
            result['ReceivedDataSize'] = self.received_data_size
        if self.request_content is not None:
            result['RequestContent'] = self.request_content.to_map()
        if self.verify_content is not None:
            result['VerifyContent'] = self.verify_content
        if self.verify_way is not None:
            result['VerifyWay'] = self.verify_way
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterEncoding') is not None:
            self.character_encoding = m.get('CharacterEncoding')
        if m.get('CustomHost') is not None:
            self.custom_host = m.get('CustomHost')
        if m.get('CustomHostIp') is not None:
            self.custom_host_ip = m.get('CustomHostIp')
        if m.get('ProtocolConnectionTimeout') is not None:
            self.protocol_connection_timeout = m.get('ProtocolConnectionTimeout')
        if m.get('ProtocolMonitorTimeout') is not None:
            self.protocol_monitor_timeout = m.get('ProtocolMonitorTimeout')
        if m.get('ReceivedDataSize') is not None:
            self.received_data_size = m.get('ReceivedDataSize')
        if m.get('RequestContent') is not None:
            temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContent()
            self.request_content = temp_model.from_map(m['RequestContent'])
        if m.get('VerifyContent') is not None:
            self.verify_content = m.get('VerifyContent')
        if m.get('VerifyWay') is not None:
            self.verify_way = m.get('VerifyWay')
        return self


class GetSyntheticTaskDetailResponseBodyTaskDetail(TeaModel):
    def __init__(self, download=None, extend_interval=None, interval_time=None, interval_type=None, ip_type=None,
                 minotor_list=None, nav=None, net=None, protocol=None, task_id=None, task_name=None, task_type=None, url=None):
        self.download = download  # type: GetSyntheticTaskDetailResponseBodyTaskDetailDownload
        self.extend_interval = extend_interval  # type: GetSyntheticTaskDetailResponseBodyTaskDetailExtendInterval
        self.interval_time = interval_time  # type: long
        self.interval_type = interval_type  # type: long
        self.ip_type = ip_type  # type: long
        self.minotor_list = minotor_list  # type: list[GetSyntheticTaskDetailResponseBodyTaskDetailMinotorList]
        self.nav = nav  # type: GetSyntheticTaskDetailResponseBodyTaskDetailNav
        self.net = net  # type: GetSyntheticTaskDetailResponseBodyTaskDetailNet
        self.protocol = protocol  # type: GetSyntheticTaskDetailResponseBodyTaskDetailProtocol
        self.task_id = task_id  # type: long
        self.task_name = task_name  # type: str
        self.task_type = task_type  # type: long
        self.url = url  # type: str

    def validate(self):
        if self.download:
            self.download.validate()
        if self.extend_interval:
            self.extend_interval.validate()
        if self.minotor_list:
            for k in self.minotor_list:
                if k:
                    k.validate()
        if self.nav:
            self.nav.validate()
        if self.net:
            self.net.validate()
        if self.protocol:
            self.protocol.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBodyTaskDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download is not None:
            result['Download'] = self.download.to_map()
        if self.extend_interval is not None:
            result['ExtendInterval'] = self.extend_interval.to_map()
        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time
        if self.interval_type is not None:
            result['IntervalType'] = self.interval_type
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        result['MinotorList'] = []
        if self.minotor_list is not None:
            for k in self.minotor_list:
                result['MinotorList'].append(k.to_map() if k else None)
        if self.nav is not None:
            result['Nav'] = self.nav.to_map()
        if self.net is not None:
            result['Net'] = self.net.to_map()
        if self.protocol is not None:
            result['Protocol'] = self.protocol.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Download') is not None:
            temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailDownload()
            self.download = temp_model.from_map(m['Download'])
        if m.get('ExtendInterval') is not None:
            temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailExtendInterval()
            self.extend_interval = temp_model.from_map(m['ExtendInterval'])
        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')
        if m.get('IntervalType') is not None:
            self.interval_type = m.get('IntervalType')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        self.minotor_list = []
        if m.get('MinotorList') is not None:
            for k in m.get('MinotorList'):
                temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailMinotorList()
                self.minotor_list.append(temp_model.from_map(k))
        if m.get('Nav') is not None:
            temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailNav()
            self.nav = temp_model.from_map(m['Nav'])
        if m.get('Net') is not None:
            temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailNet()
            self.net = temp_model.from_map(m['Net'])
        if m.get('Protocol') is not None:
            temp_model = GetSyntheticTaskDetailResponseBodyTaskDetailProtocol()
            self.protocol = temp_model.from_map(m['Protocol'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetSyntheticTaskDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, task_detail=None):
        self.request_id = request_id  # type: str
        self.task_detail = task_detail  # type: GetSyntheticTaskDetailResponseBodyTaskDetail

    def validate(self):
        if self.task_detail:
            self.task_detail.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskDetail') is not None:
            temp_model = GetSyntheticTaskDetailResponseBodyTaskDetail()
            self.task_detail = temp_model.from_map(m['TaskDetail'])
        return self


class GetSyntheticTaskDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSyntheticTaskDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskDetailResponse, self).to_map()
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
            temp_model = GetSyntheticTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSyntheticTaskListRequest(TeaModel):
    def __init__(self, direction=None, order=None, page_num=None, page_size=None, region_id=None, task_name=None,
                 task_status=None, task_type=None, url=None):
        self.direction = direction  # type: str
        self.order = order  # type: str
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.region_id = region_id  # type: str
        self.task_name = task_name  # type: str
        self.task_status = task_status  # type: str
        self.task_type = task_type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.order is not None:
            result['Order'] = self.order
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetSyntheticTaskListResponseBodyPageInfoList(TeaModel):
    def __init__(self, create_time=None, monitor_number=None, task_id=None, task_name=None, task_status=None,
                 task_type=None, task_type_name=None, url=None, usable=None):
        self.create_time = create_time  # type: str
        self.monitor_number = monitor_number  # type: long
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str
        self.task_status = task_status  # type: str
        self.task_type = task_type  # type: long
        self.task_type_name = task_type_name  # type: str
        self.url = url  # type: str
        self.usable = usable  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskListResponseBodyPageInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.monitor_number is not None:
            result['MonitorNumber'] = self.monitor_number
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_name is not None:
            result['TaskTypeName'] = self.task_type_name
        if self.url is not None:
            result['Url'] = self.url
        if self.usable is not None:
            result['Usable'] = self.usable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MonitorNumber') is not None:
            self.monitor_number = m.get('MonitorNumber')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeName') is not None:
            self.task_type_name = m.get('TaskTypeName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Usable') is not None:
            self.usable = m.get('Usable')
        return self


class GetSyntheticTaskListResponseBodyPageInfo(TeaModel):
    def __init__(self, has_next_page=None, has_previous_page=None, is_first_page=None, is_last_page=None, list=None,
                 navigate_first_page=None, navigate_last_page=None, navigate_page_nums=None, next_page=None, pages=None, prepage=None,
                 size=None, total=None):
        self.has_next_page = has_next_page  # type: str
        self.has_previous_page = has_previous_page  # type: bool
        self.is_first_page = is_first_page  # type: bool
        self.is_last_page = is_last_page  # type: bool
        self.list = list  # type: list[GetSyntheticTaskListResponseBodyPageInfoList]
        self.navigate_first_page = navigate_first_page  # type: str
        self.navigate_last_page = navigate_last_page  # type: str
        self.navigate_page_nums = navigate_page_nums  # type: str
        self.next_page = next_page  # type: str
        self.pages = pages  # type: str
        self.prepage = prepage  # type: str
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskListResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_next_page is not None:
            result['HasNextPage'] = self.has_next_page
        if self.has_previous_page is not None:
            result['HasPreviousPage'] = self.has_previous_page
        if self.is_first_page is not None:
            result['IsFirstPage'] = self.is_first_page
        if self.is_last_page is not None:
            result['IsLastPage'] = self.is_last_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.navigate_first_page is not None:
            result['NavigateFirstPage'] = self.navigate_first_page
        if self.navigate_last_page is not None:
            result['NavigateLastPage'] = self.navigate_last_page
        if self.navigate_page_nums is not None:
            result['NavigatePageNums'] = self.navigate_page_nums
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.prepage is not None:
            result['Prepage'] = self.prepage
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasNextPage') is not None:
            self.has_next_page = m.get('HasNextPage')
        if m.get('HasPreviousPage') is not None:
            self.has_previous_page = m.get('HasPreviousPage')
        if m.get('IsFirstPage') is not None:
            self.is_first_page = m.get('IsFirstPage')
        if m.get('IsLastPage') is not None:
            self.is_last_page = m.get('IsLastPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetSyntheticTaskListResponseBodyPageInfoList()
                self.list.append(temp_model.from_map(k))
        if m.get('NavigateFirstPage') is not None:
            self.navigate_first_page = m.get('NavigateFirstPage')
        if m.get('NavigateLastPage') is not None:
            self.navigate_last_page = m.get('NavigateLastPage')
        if m.get('NavigatePageNums') is not None:
            self.navigate_page_nums = m.get('NavigatePageNums')
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('Prepage') is not None:
            self.prepage = m.get('Prepage')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetSyntheticTaskListResponseBody(TeaModel):
    def __init__(self, page_info=None, request_id=None):
        self.page_info = page_info  # type: GetSyntheticTaskListResponseBodyPageInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = GetSyntheticTaskListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSyntheticTaskListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSyntheticTaskListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskListResponse, self).to_map()
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
            temp_model = GetSyntheticTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSyntheticTaskMonitorsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskMonitorsRequest, self).to_map()
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


class GetSyntheticTaskMonitorsResponseBodyData(TeaModel):
    def __init__(self, busy=None, city=None, city_code=None, client_type=None, district=None, net_service_id=None,
                 net_service_name=None):
        self.busy = busy  # type: long
        self.city = city  # type: str
        self.city_code = city_code  # type: long
        self.client_type = client_type  # type: long
        self.district = district  # type: str
        self.net_service_id = net_service_id  # type: long
        self.net_service_name = net_service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSyntheticTaskMonitorsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.busy is not None:
            result['Busy'] = self.busy
        if self.city is not None:
            result['City'] = self.city
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.district is not None:
            result['District'] = self.district
        if self.net_service_id is not None:
            result['NetServiceId'] = self.net_service_id
        if self.net_service_name is not None:
            result['NetServiceName'] = self.net_service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Busy') is not None:
            self.busy = m.get('Busy')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('NetServiceId') is not None:
            self.net_service_id = m.get('NetServiceId')
        if m.get('NetServiceName') is not None:
            self.net_service_name = m.get('NetServiceName')
        return self


class GetSyntheticTaskMonitorsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetSyntheticTaskMonitorsResponseBodyData]
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskMonitorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSyntheticTaskMonitorsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSyntheticTaskMonitorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSyntheticTaskMonitorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSyntheticTaskMonitorsResponse, self).to_map()
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
            temp_model = GetSyntheticTaskMonitorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceRequest(TeaModel):
    def __init__(self, end_time=None, region_id=None, start_time=None, trace_id=None):
        self.end_time = end_time  # type: long
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBodySpansLogEventListTagEntryList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceResponseBodySpansLogEventListTagEntryList, self).to_map()
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


class GetTraceResponseBodySpansLogEventList(TeaModel):
    def __init__(self, tag_entry_list=None, timestamp=None):
        self.tag_entry_list = tag_entry_list  # type: list[GetTraceResponseBodySpansLogEventListTagEntryList]
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodySpansLogEventList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetTraceResponseBodySpansLogEventListTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetTraceResponseBodySpansTagEntryList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceResponseBodySpansTagEntryList, self).to_map()
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


class GetTraceResponseBodySpans(TeaModel):
    def __init__(self, children=None, duration=None, have_stack=None, log_event_list=None, operation_name=None,
                 parent_span_id=None, result_code=None, rpc_id=None, rpc_type=None, service_ip=None, service_name=None,
                 span_id=None, tag_entry_list=None, timestamp=None, trace_id=None):
        self.children = children  # type: list[dict[str, any]]
        self.duration = duration  # type: long
        self.have_stack = have_stack  # type: bool
        self.log_event_list = log_event_list  # type: list[GetTraceResponseBodySpansLogEventList]
        self.operation_name = operation_name  # type: str
        self.parent_span_id = parent_span_id  # type: str
        self.result_code = result_code  # type: str
        self.rpc_id = rpc_id  # type: str
        self.rpc_type = rpc_type  # type: int
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.span_id = span_id  # type: str
        self.tag_entry_list = tag_entry_list  # type: list[GetTraceResponseBodySpansTagEntryList]
        self.timestamp = timestamp  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.log_event_list:
            for k in self.log_event_list:
                if k:
                    k.validate()
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodySpans, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.children is not None:
            result['Children'] = self.children
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        result['LogEventList'] = []
        if self.log_event_list is not None:
            for k in self.log_event_list:
                result['LogEventList'].append(k.to_map() if k else None)
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Children') is not None:
            self.children = m.get('Children')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        self.log_event_list = []
        if m.get('LogEventList') is not None:
            for k in m.get('LogEventList'):
                temp_model = GetTraceResponseBodySpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k))
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetTraceResponseBodySpansTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBody(TeaModel):
    def __init__(self, request_id=None, spans=None):
        self.request_id = request_id  # type: str
        self.spans = spans  # type: list[GetTraceResponseBodySpans]

    def validate(self):
        if self.spans:
            for k in self.spans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Spans'] = []
        if self.spans is not None:
            for k in self.spans:
                result['Spans'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spans = []
        if m.get('Spans') is not None:
            for k in m.get('Spans'):
                temp_model = GetTraceResponseBodySpans()
                self.spans.append(temp_model.from_map(k))
        return self


class GetTraceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTraceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTraceResponse, self).to_map()
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
            temp_model = GetTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceAppRequest(TeaModel):
    def __init__(self, pid=None, region_id=None):
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetTraceAppResponseBodyTraceApp(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, labels=None, pid=None, region_id=None, show=None,
                 type=None, update_time=None, user_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.labels = labels  # type: list[str]
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.show = show  # type: bool
        self.type = type  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceAppResponseBodyTraceApp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetTraceAppResponseBody(TeaModel):
    def __init__(self, request_id=None, trace_app=None):
        self.request_id = request_id  # type: str
        self.trace_app = trace_app  # type: GetTraceAppResponseBodyTraceApp

    def validate(self):
        if self.trace_app:
            self.trace_app.validate()

    def to_map(self):
        _map = super(GetTraceAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_app is not None:
            result['TraceApp'] = self.trace_app.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceApp') is not None:
            temp_model = GetTraceAppResponseBodyTraceApp()
            self.trace_app = temp_model.from_map(m['TraceApp'])
        return self


class GetTraceAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTraceAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTraceAppResponse, self).to_map()
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
            temp_model = GetTraceAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportAppAlertRulesRequest(TeaModel):
    def __init__(self, contact_group_ids=None, is_auto_start=None, pids=None, region_id=None,
                 templage_alert_config=None, template_alert_id=None):
        self.contact_group_ids = contact_group_ids  # type: str
        self.is_auto_start = is_auto_start  # type: bool
        self.pids = pids  # type: str
        self.region_id = region_id  # type: str
        self.templage_alert_config = templage_alert_config  # type: str
        self.template_alert_id = template_alert_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportAppAlertRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start
        if self.pids is not None:
            result['Pids'] = self.pids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config
        if self.template_alert_id is not None:
            result['TemplateAlertId'] = self.template_alert_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')
        if m.get('TemplateAlertId') is not None:
            self.template_alert_id = m.get('TemplateAlertId')
        return self


class ImportAppAlertRulesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportAppAlertRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportAppAlertRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportAppAlertRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportAppAlertRulesResponse, self).to_map()
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
            temp_model = ImportAppAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallCmsExporterRequest(TeaModel):
    def __init__(self, cluster_id=None, cms_args=None, direct_args=None, enable_tag=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cms_args = cms_args  # type: str
        self.direct_args = direct_args  # type: str
        self.enable_tag = enable_tag  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallCmsExporterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cms_args is not None:
            result['CmsArgs'] = self.cms_args
        if self.direct_args is not None:
            result['DirectArgs'] = self.direct_args
        if self.enable_tag is not None:
            result['EnableTag'] = self.enable_tag
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CmsArgs') is not None:
            self.cms_args = m.get('CmsArgs')
        if m.get('DirectArgs') is not None:
            self.direct_args = m.get('DirectArgs')
        if m.get('EnableTag') is not None:
            self.enable_tag = m.get('EnableTag')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class InstallCmsExporterResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallCmsExporterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InstallCmsExporterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InstallCmsExporterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallCmsExporterResponse, self).to_map()
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
            temp_model = InstallCmsExporterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallManagedPrometheusRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, kube_config=None, region_id=None, security_group_id=None,
                 v_switch_id=None, vpc_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_type = cluster_type  # type: str
        self.kube_config = kube_config  # type: str
        self.region_id = region_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallManagedPrometheusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.kube_config is not None:
            result['KubeConfig'] = self.kube_config
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('KubeConfig') is not None:
            self.kube_config = m.get('KubeConfig')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class InstallManagedPrometheusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallManagedPrometheusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InstallManagedPrometheusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InstallManagedPrometheusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallManagedPrometheusResponse, self).to_map()
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
            temp_model = InstallManagedPrometheusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListActivatedAlertsRequest(TeaModel):
    def __init__(self, current_page=None, filter=None, page_size=None, region_id=None):
        self.current_page = current_page  # type: int
        self.filter = filter  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListActivatedAlertsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListActivatedAlertsResponseBodyPageAlertsDispatchRules(TeaModel):
    def __init__(self, rule_id=None, rule_name=None):
        self.rule_id = rule_id  # type: int
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListActivatedAlertsResponseBodyPageAlertsDispatchRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListActivatedAlertsResponseBodyPageAlerts(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, alert_type=None, count=None, create_time=None,
                 dispatch_rules=None, ends_at=None, expand_fields=None, integration_name=None, integration_type=None,
                 involved_object_kind=None, involved_object_name=None, message=None, severity=None, starts_at=None, status=None):
        self.alert_id = alert_id  # type: str
        self.alert_name = alert_name  # type: str
        self.alert_type = alert_type  # type: str
        self.count = count  # type: int
        self.create_time = create_time  # type: long
        self.dispatch_rules = dispatch_rules  # type: list[ListActivatedAlertsResponseBodyPageAlertsDispatchRules]
        self.ends_at = ends_at  # type: long
        self.expand_fields = expand_fields  # type: dict[str, any]
        self.integration_name = integration_name  # type: str
        self.integration_type = integration_type  # type: str
        self.involved_object_kind = involved_object_kind  # type: str
        self.involved_object_name = involved_object_name  # type: str
        self.message = message  # type: str
        self.severity = severity  # type: str
        self.starts_at = starts_at  # type: long
        self.status = status  # type: str

    def validate(self):
        if self.dispatch_rules:
            for k in self.dispatch_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListActivatedAlertsResponseBodyPageAlerts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.count is not None:
            result['Count'] = self.count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DispatchRules'] = []
        if self.dispatch_rules is not None:
            for k in self.dispatch_rules:
                result['DispatchRules'].append(k.to_map() if k else None)
        if self.ends_at is not None:
            result['EndsAt'] = self.ends_at
        if self.expand_fields is not None:
            result['ExpandFields'] = self.expand_fields
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type
        if self.involved_object_kind is not None:
            result['InvolvedObjectKind'] = self.involved_object_kind
        if self.involved_object_name is not None:
            result['InvolvedObjectName'] = self.involved_object_name
        if self.message is not None:
            result['Message'] = self.message
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.starts_at is not None:
            result['StartsAt'] = self.starts_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.dispatch_rules = []
        if m.get('DispatchRules') is not None:
            for k in m.get('DispatchRules'):
                temp_model = ListActivatedAlertsResponseBodyPageAlertsDispatchRules()
                self.dispatch_rules.append(temp_model.from_map(k))
        if m.get('EndsAt') is not None:
            self.ends_at = m.get('EndsAt')
        if m.get('ExpandFields') is not None:
            self.expand_fields = m.get('ExpandFields')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')
        if m.get('InvolvedObjectKind') is not None:
            self.involved_object_kind = m.get('InvolvedObjectKind')
        if m.get('InvolvedObjectName') is not None:
            self.involved_object_name = m.get('InvolvedObjectName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartsAt') is not None:
            self.starts_at = m.get('StartsAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListActivatedAlertsResponseBodyPage(TeaModel):
    def __init__(self, alerts=None, page=None, page_size=None, total=None):
        self.alerts = alerts  # type: list[ListActivatedAlertsResponseBodyPageAlerts]
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.alerts:
            for k in self.alerts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListActivatedAlertsResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alerts'] = []
        if self.alerts is not None:
            for k in self.alerts:
                result['Alerts'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alerts = []
        if m.get('Alerts') is not None:
            for k in m.get('Alerts'):
                temp_model = ListActivatedAlertsResponseBodyPageAlerts()
                self.alerts.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListActivatedAlertsResponseBody(TeaModel):
    def __init__(self, page=None, request_id=None):
        self.page = page  # type: ListActivatedAlertsResponseBodyPage
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListActivatedAlertsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = ListActivatedAlertsResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListActivatedAlertsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListActivatedAlertsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListActivatedAlertsResponse, self).to_map()
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
            temp_model = ListActivatedAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlertEventsRequest(TeaModel):
    def __init__(self, alert_name=None, end_time=None, matching_conditions=None, page=None, size=None,
                 start_time=None, status=None):
        self.alert_name = alert_name  # type: str
        self.end_time = end_time  # type: str
        self.matching_conditions = matching_conditions  # type: str
        self.page = page  # type: long
        self.size = size  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlertEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.matching_conditions is not None:
            result['MatchingConditions'] = self.matching_conditions
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MatchingConditions') is not None:
            self.matching_conditions = m.get('MatchingConditions')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAlertEventsResponseBodyPageBeanEventsAlarms(TeaModel):
    def __init__(self, alarm_id=None, alarm_name=None, create_time=None, state=None):
        self.alarm_id = alarm_id  # type: long
        self.alarm_name = alarm_name  # type: str
        self.create_time = create_time  # type: str
        self.state = state  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlertEventsResponseBodyPageBeanEventsAlarms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListAlertEventsResponseBodyPageBeanEvents(TeaModel):
    def __init__(self, alarms=None, alert_name=None, annotations=None, description=None, end_time=None,
                 generator_url=None, integration_name=None, integration_type=None, labels=None, receive_time=None, severity=None,
                 start_time=None, status=None):
        self.alarms = alarms  # type: list[ListAlertEventsResponseBodyPageBeanEventsAlarms]
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: str
        self.generator_url = generator_url  # type: str
        self.integration_name = integration_name  # type: str
        self.integration_type = integration_type  # type: str
        self.labels = labels  # type: str
        self.receive_time = receive_time  # type: str
        self.severity = severity  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.alarms:
            for k in self.alarms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlertEventsResponseBodyPageBeanEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alarms'] = []
        if self.alarms is not None:
            for k in self.alarms:
                result['Alarms'].append(k.to_map() if k else None)
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.generator_url is not None:
            result['GeneratorURL'] = self.generator_url
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.receive_time is not None:
            result['ReceiveTime'] = self.receive_time
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alarms = []
        if m.get('Alarms') is not None:
            for k in m.get('Alarms'):
                temp_model = ListAlertEventsResponseBodyPageBeanEventsAlarms()
                self.alarms.append(temp_model.from_map(k))
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GeneratorURL') is not None:
            self.generator_url = m.get('GeneratorURL')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ReceiveTime') is not None:
            self.receive_time = m.get('ReceiveTime')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAlertEventsResponseBodyPageBean(TeaModel):
    def __init__(self, events=None, page=None, size=None, total=None):
        self.events = events  # type: list[ListAlertEventsResponseBodyPageBeanEvents]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlertEventsResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = ListAlertEventsResponseBodyPageBeanEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAlertEventsResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: ListAlertEventsResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(ListAlertEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListAlertEventsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAlertEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAlertEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlertEventsResponse, self).to_map()
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
            temp_model = ListAlertEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlertsRequest(TeaModel):
    def __init__(self, alert_name=None, dispatch_rule_id=None, end_time=None, integration_type=None, page=None,
                 severity=None, show_activities=None, show_events=None, size=None, start_time=None, state=None):
        self.alert_name = alert_name  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.end_time = end_time  # type: str
        self.integration_type = integration_type  # type: str
        self.page = page  # type: long
        self.severity = severity  # type: str
        self.show_activities = show_activities  # type: bool
        self.show_events = show_events  # type: bool
        self.size = size  # type: long
        self.start_time = start_time  # type: str
        self.state = state  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlertsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type
        if self.page is not None:
            result['Page'] = self.page
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.show_activities is not None:
            result['ShowActivities'] = self.show_activities
        if self.show_events is not None:
            result['ShowEvents'] = self.show_events
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('ShowActivities') is not None:
            self.show_activities = m.get('ShowActivities')
        if m.get('ShowEvents') is not None:
            self.show_events = m.get('ShowEvents')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListAlertsResponseBodyPageBeanListAlertsActivities(TeaModel):
    def __init__(self, content=None, description=None, handler_name=None, time=None, type=None):
        self.content = content  # type: str
        self.description = description  # type: str
        self.handler_name = handler_name  # type: str
        self.time = time  # type: str
        self.type = type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlertsResponseBodyPageBeanListAlertsActivities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.handler_name is not None:
            result['HandlerName'] = self.handler_name
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HandlerName') is not None:
            self.handler_name = m.get('HandlerName')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAlertsResponseBodyPageBeanListAlertsAlertEvents(TeaModel):
    def __init__(self, alert_name=None, annotations=None, description=None, end_time=None, generator_url=None,
                 integration_name=None, integration_type=None, labels=None, receive_time=None, severity=None, start_time=None,
                 state=None):
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: str
        self.generator_url = generator_url  # type: str
        self.integration_name = integration_name  # type: str
        self.integration_type = integration_type  # type: str
        self.labels = labels  # type: str
        self.receive_time = receive_time  # type: str
        self.severity = severity  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlertsResponseBodyPageBeanListAlertsAlertEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.generator_url is not None:
            result['GeneratorURL'] = self.generator_url
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.receive_time is not None:
            result['ReceiveTime'] = self.receive_time
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GeneratorURL') is not None:
            self.generator_url = m.get('GeneratorURL')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ReceiveTime') is not None:
            self.receive_time = m.get('ReceiveTime')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListAlertsResponseBodyPageBeanListAlerts(TeaModel):
    def __init__(self, activities=None, alert_events=None, alert_id=None, alert_name=None, create_time=None,
                 dispatch_rule_id=None, dispatch_rule_name=None, severity=None, state=None):
        self.activities = activities  # type: list[ListAlertsResponseBodyPageBeanListAlertsActivities]
        self.alert_events = alert_events  # type: list[ListAlertsResponseBodyPageBeanListAlertsAlertEvents]
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.create_time = create_time  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: float
        self.dispatch_rule_name = dispatch_rule_name  # type: str
        self.severity = severity  # type: str
        self.state = state  # type: long

    def validate(self):
        if self.activities:
            for k in self.activities:
                if k:
                    k.validate()
        if self.alert_events:
            for k in self.alert_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlertsResponseBodyPageBeanListAlerts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Activities'] = []
        if self.activities is not None:
            for k in self.activities:
                result['Activities'].append(k.to_map() if k else None)
        result['AlertEvents'] = []
        if self.alert_events is not None:
            for k in self.alert_events:
                result['AlertEvents'].append(k.to_map() if k else None)
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.dispatch_rule_name is not None:
            result['DispatchRuleName'] = self.dispatch_rule_name
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.activities = []
        if m.get('Activities') is not None:
            for k in m.get('Activities'):
                temp_model = ListAlertsResponseBodyPageBeanListAlertsActivities()
                self.activities.append(temp_model.from_map(k))
        self.alert_events = []
        if m.get('AlertEvents') is not None:
            for k in m.get('AlertEvents'):
                temp_model = ListAlertsResponseBodyPageBeanListAlertsAlertEvents()
                self.alert_events.append(temp_model.from_map(k))
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('DispatchRuleName') is not None:
            self.dispatch_rule_name = m.get('DispatchRuleName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListAlertsResponseBodyPageBean(TeaModel):
    def __init__(self, list_alerts=None, page=None, size=None, total=None):
        self.list_alerts = list_alerts  # type: list[ListAlertsResponseBodyPageBeanListAlerts]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.list_alerts:
            for k in self.list_alerts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlertsResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListAlerts'] = []
        if self.list_alerts is not None:
            for k in self.list_alerts:
                result['ListAlerts'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list_alerts = []
        if m.get('ListAlerts') is not None:
            for k in m.get('ListAlerts'):
                temp_model = ListAlertsResponseBodyPageBeanListAlerts()
                self.list_alerts.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAlertsResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: ListAlertsResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(ListAlertsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListAlertsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAlertsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAlertsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlertsResponse, self).to_map()
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
            temp_model = ListAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterFromGrafanaRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterFromGrafanaRequest, self).to_map()
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


class ListClusterFromGrafanaResponseBodyPromClusterList(TeaModel):
    def __init__(self, agent_status=None, cluster_id=None, cluster_name=None, cluster_type=None, controller_id=None,
                 create_time=None, extra=None, id=None, install_time=None, is_controller_installed=None,
                 last_heart_beat_time=None, node_num=None, options=None, plugins_json_array=None, region_id=None, state_json=None,
                 update_time=None, user_id=None):
        self.agent_status = agent_status  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.controller_id = controller_id  # type: str
        self.create_time = create_time  # type: long
        self.extra = extra  # type: str
        self.id = id  # type: long
        self.install_time = install_time  # type: long
        self.is_controller_installed = is_controller_installed  # type: bool
        self.last_heart_beat_time = last_heart_beat_time  # type: long
        self.node_num = node_num  # type: int
        self.options = options  # type: str
        self.plugins_json_array = plugins_json_array  # type: str
        self.region_id = region_id  # type: str
        self.state_json = state_json  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterFromGrafanaResponseBodyPromClusterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.controller_id is not None:
            result['ControllerId'] = self.controller_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.id is not None:
            result['Id'] = self.id
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.is_controller_installed is not None:
            result['IsControllerInstalled'] = self.is_controller_installed
        if self.last_heart_beat_time is not None:
            result['LastHeartBeatTime'] = self.last_heart_beat_time
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.options is not None:
            result['Options'] = self.options
        if self.plugins_json_array is not None:
            result['PluginsJsonArray'] = self.plugins_json_array
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state_json is not None:
            result['StateJson'] = self.state_json
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ControllerId') is not None:
            self.controller_id = m.get('ControllerId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('IsControllerInstalled') is not None:
            self.is_controller_installed = m.get('IsControllerInstalled')
        if m.get('LastHeartBeatTime') is not None:
            self.last_heart_beat_time = m.get('LastHeartBeatTime')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('PluginsJsonArray') is not None:
            self.plugins_json_array = m.get('PluginsJsonArray')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StateJson') is not None:
            self.state_json = m.get('StateJson')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListClusterFromGrafanaResponseBody(TeaModel):
    def __init__(self, prom_cluster_list=None, request_id=None):
        self.prom_cluster_list = prom_cluster_list  # type: list[ListClusterFromGrafanaResponseBodyPromClusterList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prom_cluster_list:
            for k in self.prom_cluster_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterFromGrafanaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PromClusterList'] = []
        if self.prom_cluster_list is not None:
            for k in self.prom_cluster_list:
                result['PromClusterList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prom_cluster_list = []
        if m.get('PromClusterList') is not None:
            for k in m.get('PromClusterList'):
                temp_model = ListClusterFromGrafanaResponseBodyPromClusterList()
                self.prom_cluster_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClusterFromGrafanaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClusterFromGrafanaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterFromGrafanaResponse, self).to_map()
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
            temp_model = ListClusterFromGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCmsInstancesRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None, type_filter=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str
        self.type_filter = type_filter  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCmsInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type_filter is not None:
            result['TypeFilter'] = self.type_filter
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TypeFilter') is not None:
            self.type_filter = m.get('TypeFilter')
        return self


class ListCmsInstancesResponseBodyDataProducts(TeaModel):
    def __init__(self, descr=None, id=None, instance=None, name=None, prod=None, source=None, state=None, time=None,
                 type=None, url=None):
        self.descr = descr  # type: str
        self.id = id  # type: str
        self.instance = instance  # type: str
        self.name = name  # type: str
        self.prod = prod  # type: str
        self.source = source  # type: str
        self.state = state  # type: str
        self.time = time  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCmsInstancesResponseBodyDataProducts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.descr is not None:
            result['Descr'] = self.descr
        if self.id is not None:
            result['Id'] = self.id
        if self.instance is not None:
            result['Instance'] = self.instance
        if self.name is not None:
            result['Name'] = self.name
        if self.prod is not None:
            result['Prod'] = self.prod
        if self.source is not None:
            result['Source'] = self.source
        if self.state is not None:
            result['State'] = self.state
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Descr') is not None:
            self.descr = m.get('Descr')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Instance') is not None:
            self.instance = m.get('Instance')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Prod') is not None:
            self.prod = m.get('Prod')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListCmsInstancesResponseBodyData(TeaModel):
    def __init__(self, enable_tag=None, products=None):
        self.enable_tag = enable_tag  # type: bool
        self.products = products  # type: list[ListCmsInstancesResponseBodyDataProducts]

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCmsInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tag is not None:
            result['EnableTag'] = self.enable_tag
        result['Products'] = []
        if self.products is not None:
            for k in self.products:
                result['Products'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableTag') is not None:
            self.enable_tag = m.get('EnableTag')
        self.products = []
        if m.get('Products') is not None:
            for k in m.get('Products'):
                temp_model = ListCmsInstancesResponseBodyDataProducts()
                self.products.append(temp_model.from_map(k))
        return self


class ListCmsInstancesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListCmsInstancesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCmsInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListCmsInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCmsInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCmsInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCmsInstancesResponse, self).to_map()
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
            temp_model = ListCmsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardsRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, dashboard_name=None, language=None, product=None,
                 recreate_switch=None, region_id=None, title=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_type = cluster_type  # type: str
        self.dashboard_name = dashboard_name  # type: str
        self.language = language  # type: str
        self.product = product  # type: str
        self.recreate_switch = recreate_switch  # type: bool
        self.region_id = region_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDashboardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.dashboard_name is not None:
            result['DashboardName'] = self.dashboard_name
        if self.language is not None:
            result['Language'] = self.language
        if self.product is not None:
            result['Product'] = self.product
        if self.recreate_switch is not None:
            result['RecreateSwitch'] = self.recreate_switch
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('DashboardName') is not None:
            self.dashboard_name = m.get('DashboardName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RecreateSwitch') is not None:
            self.recreate_switch = m.get('RecreateSwitch')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListDashboardsResponseBodyDashboardVosI18nChild(TeaModel):
    def __init__(self, dashboard_type=None, exporter=None, http_url=None, https_url=None, id=None,
                 is_arms_exporter=None, kind=None, language=None, name=None, need_update=None, tags=None, time=None, title=None,
                 type=None, uid=None, url=None, version=None):
        self.dashboard_type = dashboard_type  # type: str
        self.exporter = exporter  # type: str
        self.http_url = http_url  # type: str
        self.https_url = https_url  # type: str
        self.id = id  # type: str
        self.is_arms_exporter = is_arms_exporter  # type: bool
        self.kind = kind  # type: str
        self.language = language  # type: str
        self.name = name  # type: str
        self.need_update = need_update  # type: bool
        self.tags = tags  # type: list[str]
        self.time = time  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.uid = uid  # type: str
        self.url = url  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDashboardsResponseBodyDashboardVosI18nChild, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_type is not None:
            result['DashboardType'] = self.dashboard_type
        if self.exporter is not None:
            result['Exporter'] = self.exporter
        if self.http_url is not None:
            result['HttpUrl'] = self.http_url
        if self.https_url is not None:
            result['HttpsUrl'] = self.https_url
        if self.id is not None:
            result['Id'] = self.id
        if self.is_arms_exporter is not None:
            result['IsArmsExporter'] = self.is_arms_exporter
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.need_update is not None:
            result['NeedUpdate'] = self.need_update
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.time is not None:
            result['Time'] = self.time
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.url is not None:
            result['Url'] = self.url
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DashboardType') is not None:
            self.dashboard_type = m.get('DashboardType')
        if m.get('Exporter') is not None:
            self.exporter = m.get('Exporter')
        if m.get('HttpUrl') is not None:
            self.http_url = m.get('HttpUrl')
        if m.get('HttpsUrl') is not None:
            self.https_url = m.get('HttpsUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsArmsExporter') is not None:
            self.is_arms_exporter = m.get('IsArmsExporter')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedUpdate') is not None:
            self.need_update = m.get('NeedUpdate')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListDashboardsResponseBodyDashboardVos(TeaModel):
    def __init__(self, dashboard_type=None, exporter=None, http_url=None, https_url=None, i_18n_child=None, id=None,
                 is_arms_exporter=None, kind=None, language=None, name=None, need_update=None, tags=None, time=None, title=None,
                 type=None, uid=None, url=None, version=None):
        self.dashboard_type = dashboard_type  # type: str
        self.exporter = exporter  # type: str
        self.http_url = http_url  # type: str
        self.https_url = https_url  # type: str
        self.i_18n_child = i_18n_child  # type: ListDashboardsResponseBodyDashboardVosI18nChild
        self.id = id  # type: str
        self.is_arms_exporter = is_arms_exporter  # type: bool
        self.kind = kind  # type: str
        self.language = language  # type: str
        self.name = name  # type: str
        self.need_update = need_update  # type: bool
        self.tags = tags  # type: list[str]
        self.time = time  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.uid = uid  # type: str
        self.url = url  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.i_18n_child:
            self.i_18n_child.validate()

    def to_map(self):
        _map = super(ListDashboardsResponseBodyDashboardVos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_type is not None:
            result['DashboardType'] = self.dashboard_type
        if self.exporter is not None:
            result['Exporter'] = self.exporter
        if self.http_url is not None:
            result['HttpUrl'] = self.http_url
        if self.https_url is not None:
            result['HttpsUrl'] = self.https_url
        if self.i_18n_child is not None:
            result['I18nChild'] = self.i_18n_child.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_arms_exporter is not None:
            result['IsArmsExporter'] = self.is_arms_exporter
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.need_update is not None:
            result['NeedUpdate'] = self.need_update
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.time is not None:
            result['Time'] = self.time
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.url is not None:
            result['Url'] = self.url
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DashboardType') is not None:
            self.dashboard_type = m.get('DashboardType')
        if m.get('Exporter') is not None:
            self.exporter = m.get('Exporter')
        if m.get('HttpUrl') is not None:
            self.http_url = m.get('HttpUrl')
        if m.get('HttpsUrl') is not None:
            self.https_url = m.get('HttpsUrl')
        if m.get('I18nChild') is not None:
            temp_model = ListDashboardsResponseBodyDashboardVosI18nChild()
            self.i_18n_child = temp_model.from_map(m['I18nChild'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsArmsExporter') is not None:
            self.is_arms_exporter = m.get('IsArmsExporter')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedUpdate') is not None:
            self.need_update = m.get('NeedUpdate')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListDashboardsResponseBody(TeaModel):
    def __init__(self, dashboard_vos=None, request_id=None):
        self.dashboard_vos = dashboard_vos  # type: list[ListDashboardsResponseBodyDashboardVos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dashboard_vos:
            for k in self.dashboard_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDashboardsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DashboardVos'] = []
        if self.dashboard_vos is not None:
            for k in self.dashboard_vos:
                result['DashboardVos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dashboard_vos = []
        if m.get('DashboardVos') is not None:
            for k in m.get('DashboardVos'):
                temp_model = ListDashboardsResponseBodyDashboardVos()
                self.dashboard_vos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDashboardsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDashboardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDashboardsResponse, self).to_map()
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
            temp_model = ListDashboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardsByNameRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, dash_board_name=None, dash_board_version=None,
                 data_source_type=None, group_name=None, only_query=None, product_code=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_type = cluster_type  # type: str
        self.dash_board_name = dash_board_name  # type: str
        self.dash_board_version = dash_board_version  # type: str
        self.data_source_type = data_source_type  # type: str
        self.group_name = group_name  # type: str
        self.only_query = only_query  # type: bool
        self.product_code = product_code  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDashboardsByNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.dash_board_name is not None:
            result['DashBoardName'] = self.dash_board_name
        if self.dash_board_version is not None:
            result['DashBoardVersion'] = self.dash_board_version
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.only_query is not None:
            result['OnlyQuery'] = self.only_query
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('DashBoardName') is not None:
            self.dash_board_name = m.get('DashBoardName')
        if m.get('DashBoardVersion') is not None:
            self.dash_board_version = m.get('DashBoardVersion')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OnlyQuery') is not None:
            self.only_query = m.get('OnlyQuery')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDashboardsByNameResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDashboardsByNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDashboardsByNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDashboardsByNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDashboardsByNameResponse, self).to_map()
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
            temp_model = ListDashboardsByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDispatchRuleRequest(TeaModel):
    def __init__(self, name=None, region_id=None, system=None):
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.system = system  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDispatchRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system is not None:
            result['System'] = self.system
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('System') is not None:
            self.system = m.get('System')
        return self


class ListDispatchRuleResponseBodyDispatchRules(TeaModel):
    def __init__(self, name=None, rule_id=None, state=None):
        self.name = name  # type: str
        self.rule_id = rule_id  # type: long
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDispatchRuleResponseBodyDispatchRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListDispatchRuleResponseBody(TeaModel):
    def __init__(self, dispatch_rules=None, request_id=None):
        self.dispatch_rules = dispatch_rules  # type: list[ListDispatchRuleResponseBodyDispatchRules]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dispatch_rules:
            for k in self.dispatch_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDispatchRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DispatchRules'] = []
        if self.dispatch_rules is not None:
            for k in self.dispatch_rules:
                result['DispatchRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dispatch_rules = []
        if m.get('DispatchRules') is not None:
            for k in m.get('DispatchRules'):
                temp_model = ListDispatchRuleResponseBodyDispatchRules()
                self.dispatch_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDispatchRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDispatchRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDispatchRuleResponse, self).to_map()
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
            temp_model = ListDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEscalationPoliciesRequest(TeaModel):
    def __init__(self, name=None, page=None, size=None):
        self.name = name  # type: str
        self.page = page  # type: long
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEscalationPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListEscalationPoliciesResponseBodyPageBeanEscalationPolicies(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEscalationPoliciesResponseBodyPageBeanEscalationPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListEscalationPoliciesResponseBodyPageBean(TeaModel):
    def __init__(self, escalation_policies=None, page=None, size=None, total=None):
        self.escalation_policies = escalation_policies  # type: list[ListEscalationPoliciesResponseBodyPageBeanEscalationPolicies]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.escalation_policies:
            for k in self.escalation_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEscalationPoliciesResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EscalationPolicies'] = []
        if self.escalation_policies is not None:
            for k in self.escalation_policies:
                result['EscalationPolicies'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.escalation_policies = []
        if m.get('EscalationPolicies') is not None:
            for k in m.get('EscalationPolicies'):
                temp_model = ListEscalationPoliciesResponseBodyPageBeanEscalationPolicies()
                self.escalation_policies.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEscalationPoliciesResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: ListEscalationPoliciesResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(ListEscalationPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListEscalationPoliciesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEscalationPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEscalationPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEscalationPoliciesResponse, self).to_map()
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
            temp_model = ListEscalationPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventBridgeIntegrationsRequest(TeaModel):
    def __init__(self, name=None, page=None, size=None):
        self.name = name  # type: str
        self.page = page  # type: long
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventBridgeIntegrationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListEventBridgeIntegrationsResponseBodyPageBeanEventBridgeIntegrations(TeaModel):
    def __init__(self, description=None, id=None, name=None):
        self.description = description  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventBridgeIntegrationsResponseBodyPageBeanEventBridgeIntegrations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListEventBridgeIntegrationsResponseBodyPageBean(TeaModel):
    def __init__(self, event_bridge_integrations=None, page=None, size=None, total=None):
        self.event_bridge_integrations = event_bridge_integrations  # type: list[ListEventBridgeIntegrationsResponseBodyPageBeanEventBridgeIntegrations]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.event_bridge_integrations:
            for k in self.event_bridge_integrations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEventBridgeIntegrationsResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventBridgeIntegrations'] = []
        if self.event_bridge_integrations is not None:
            for k in self.event_bridge_integrations:
                result['EventBridgeIntegrations'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_bridge_integrations = []
        if m.get('EventBridgeIntegrations') is not None:
            for k in m.get('EventBridgeIntegrations'):
                temp_model = ListEventBridgeIntegrationsResponseBodyPageBeanEventBridgeIntegrations()
                self.event_bridge_integrations.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEventBridgeIntegrationsResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: ListEventBridgeIntegrationsResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(ListEventBridgeIntegrationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListEventBridgeIntegrationsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEventBridgeIntegrationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEventBridgeIntegrationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEventBridgeIntegrationsResponse, self).to_map()
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
            temp_model = ListEventBridgeIntegrationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInsightsEventsRequest(TeaModel):
    def __init__(self, end_time=None, insights_types=None, pid=None, region_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.insights_types = insights_types  # type: str
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInsightsEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.insights_types is not None:
            result['InsightsTypes'] = self.insights_types
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InsightsTypes') is not None:
            self.insights_types = m.get('InsightsTypes')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListInsightsEventsResponseBodyInsightsEvents(TeaModel):
    def __init__(self, date=None, desc=None, level=None, pid=None, title=None, type=None):
        self.date = date  # type: long
        self.desc = desc  # type: str
        self.level = level  # type: str
        self.pid = pid  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInsightsEventsResponseBodyInsightsEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.level is not None:
            result['Level'] = self.level
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInsightsEventsResponseBody(TeaModel):
    def __init__(self, insights_events=None, request_id=None):
        self.insights_events = insights_events  # type: list[ListInsightsEventsResponseBodyInsightsEvents]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.insights_events:
            for k in self.insights_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInsightsEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InsightsEvents'] = []
        if self.insights_events is not None:
            for k in self.insights_events:
                result['InsightsEvents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.insights_events = []
        if m.get('InsightsEvents') is not None:
            for k in m.get('InsightsEvents'):
                temp_model = ListInsightsEventsResponseBodyInsightsEvents()
                self.insights_events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInsightsEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInsightsEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInsightsEventsResponse, self).to_map()
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
            temp_model = ListInsightsEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntegrationRequest(TeaModel):
    def __init__(self, integration_name=None, integration_product_type=None, is_detail=None, page=None, size=None):
        self.integration_name = integration_name  # type: str
        self.integration_product_type = integration_product_type  # type: str
        self.is_detail = is_detail  # type: bool
        self.page = page  # type: long
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntegrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_product_type is not None:
            result['IntegrationProductType'] = self.integration_product_type
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationProductType') is not None:
            self.integration_product_type = m.get('IntegrationProductType')
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListIntegrationResponseBodyPageInfoIntegrationsIntegrationDetail(TeaModel):
    def __init__(self, auto_recover=None, description=None, duplicate_key=None, extended_field_redefine_rules=None,
                 field_redefine_rules=None, initiative_recover_field=None, initiative_recover_value=None, recover_time=None, stat=None):
        self.auto_recover = auto_recover  # type: bool
        self.description = description  # type: str
        self.duplicate_key = duplicate_key  # type: str
        self.extended_field_redefine_rules = extended_field_redefine_rules  # type: list[dict[str, any]]
        self.field_redefine_rules = field_redefine_rules  # type: list[dict[str, any]]
        self.initiative_recover_field = initiative_recover_field  # type: str
        self.initiative_recover_value = initiative_recover_value  # type: str
        self.recover_time = recover_time  # type: long
        self.stat = stat  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntegrationResponseBodyPageInfoIntegrationsIntegrationDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_recover is not None:
            result['AutoRecover'] = self.auto_recover
        if self.description is not None:
            result['Description'] = self.description
        if self.duplicate_key is not None:
            result['DuplicateKey'] = self.duplicate_key
        if self.extended_field_redefine_rules is not None:
            result['ExtendedFieldRedefineRules'] = self.extended_field_redefine_rules
        if self.field_redefine_rules is not None:
            result['FieldRedefineRules'] = self.field_redefine_rules
        if self.initiative_recover_field is not None:
            result['InitiativeRecoverField'] = self.initiative_recover_field
        if self.initiative_recover_value is not None:
            result['InitiativeRecoverValue'] = self.initiative_recover_value
        if self.recover_time is not None:
            result['RecoverTime'] = self.recover_time
        if self.stat is not None:
            result['Stat'] = self.stat
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRecover') is not None:
            self.auto_recover = m.get('AutoRecover')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DuplicateKey') is not None:
            self.duplicate_key = m.get('DuplicateKey')
        if m.get('ExtendedFieldRedefineRules') is not None:
            self.extended_field_redefine_rules = m.get('ExtendedFieldRedefineRules')
        if m.get('FieldRedefineRules') is not None:
            self.field_redefine_rules = m.get('FieldRedefineRules')
        if m.get('InitiativeRecoverField') is not None:
            self.initiative_recover_field = m.get('InitiativeRecoverField')
        if m.get('InitiativeRecoverValue') is not None:
            self.initiative_recover_value = m.get('InitiativeRecoverValue')
        if m.get('RecoverTime') is not None:
            self.recover_time = m.get('RecoverTime')
        if m.get('Stat') is not None:
            self.stat = m.get('Stat')
        return self


class ListIntegrationResponseBodyPageInfoIntegrations(TeaModel):
    def __init__(self, api_endpoint=None, create_time=None, integration_detail=None, integration_id=None,
                 integration_name=None, integration_product_type=None, liveness=None, short_token=None, state=None):
        self.api_endpoint = api_endpoint  # type: str
        self.create_time = create_time  # type: str
        self.integration_detail = integration_detail  # type: ListIntegrationResponseBodyPageInfoIntegrationsIntegrationDetail
        self.integration_id = integration_id  # type: long
        self.integration_name = integration_name  # type: str
        self.integration_product_type = integration_product_type  # type: str
        self.liveness = liveness  # type: str
        self.short_token = short_token  # type: str
        self.state = state  # type: bool

    def validate(self):
        if self.integration_detail:
            self.integration_detail.validate()

    def to_map(self):
        _map = super(ListIntegrationResponseBodyPageInfoIntegrations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_endpoint is not None:
            result['ApiEndpoint'] = self.api_endpoint
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.integration_detail is not None:
            result['IntegrationDetail'] = self.integration_detail.to_map()
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_product_type is not None:
            result['IntegrationProductType'] = self.integration_product_type
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.short_token is not None:
            result['ShortToken'] = self.short_token
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiEndpoint') is not None:
            self.api_endpoint = m.get('ApiEndpoint')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntegrationDetail') is not None:
            temp_model = ListIntegrationResponseBodyPageInfoIntegrationsIntegrationDetail()
            self.integration_detail = temp_model.from_map(m['IntegrationDetail'])
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationProductType') is not None:
            self.integration_product_type = m.get('IntegrationProductType')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('ShortToken') is not None:
            self.short_token = m.get('ShortToken')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListIntegrationResponseBodyPageInfo(TeaModel):
    def __init__(self, integrations=None, page=None, size=None, total=None):
        self.integrations = integrations  # type: list[ListIntegrationResponseBodyPageInfoIntegrations]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.integrations:
            for k in self.integrations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIntegrationResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Integrations'] = []
        if self.integrations is not None:
            for k in self.integrations:
                result['Integrations'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.integrations = []
        if m.get('Integrations') is not None:
            for k in m.get('Integrations'):
                temp_model = ListIntegrationResponseBodyPageInfoIntegrations()
                self.integrations.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListIntegrationResponseBody(TeaModel):
    def __init__(self, page_info=None, request_id=None):
        self.page_info = page_info  # type: ListIntegrationResponseBodyPageInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(ListIntegrationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = ListIntegrationResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListIntegrationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIntegrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIntegrationResponse, self).to_map()
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
            temp_model = ListIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotificationPoliciesRequest(TeaModel):
    def __init__(self, is_detail=None, name=None, page=None, region_id=None, size=None):
        self.is_detail = is_detail  # type: bool
        self.name = name  # type: str
        self.page = page  # type: long
        self.region_id = region_id  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotificationPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesGroupRule(TeaModel):
    def __init__(self, group_interval=None, group_wait=None, grouping_fields=None):
        self.group_interval = group_interval  # type: long
        self.group_wait = group_wait  # type: long
        self.grouping_fields = grouping_fields  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesGroupRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_interval is not None:
            result['GroupInterval'] = self.group_interval
        if self.group_wait is not None:
            result['GroupWait'] = self.group_wait
        if self.grouping_fields is not None:
            result['GroupingFields'] = self.grouping_fields
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupInterval') is not None:
            self.group_interval = m.get('GroupInterval')
        if m.get('GroupWait') is not None:
            self.group_wait = m.get('GroupWait')
        if m.get('GroupingFields') is not None:
            self.grouping_fields = m.get('GroupingFields')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRulesMatchingConditions(TeaModel):
    def __init__(self, key=None, operator=None, value=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRulesMatchingConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRules(TeaModel):
    def __init__(self, matching_conditions=None):
        self.matching_conditions = matching_conditions  # type: list[ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRulesMatchingConditions]

    def validate(self):
        if self.matching_conditions:
            for k in self.matching_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchingConditions'] = []
        if self.matching_conditions is not None:
            for k in self.matching_conditions:
                result['MatchingConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.matching_conditions = []
        if m.get('MatchingConditions') is not None:
            for k in m.get('MatchingConditions'):
                temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k))
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRuleNotifyObjects(TeaModel):
    def __init__(self, notify_object_id=None, notify_object_name=None, notify_object_type=None):
        self.notify_object_id = notify_object_id  # type: long
        self.notify_object_name = notify_object_name  # type: str
        self.notify_object_type = notify_object_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRuleNotifyObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_object_id is not None:
            result['NotifyObjectId'] = self.notify_object_id
        if self.notify_object_name is not None:
            result['NotifyObjectName'] = self.notify_object_name
        if self.notify_object_type is not None:
            result['NotifyObjectType'] = self.notify_object_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotifyObjectId') is not None:
            self.notify_object_id = m.get('NotifyObjectId')
        if m.get('NotifyObjectName') is not None:
            self.notify_object_name = m.get('NotifyObjectName')
        if m.get('NotifyObjectType') is not None:
            self.notify_object_type = m.get('NotifyObjectType')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRule(TeaModel):
    def __init__(self, notify_channels=None, notify_end_time=None, notify_objects=None, notify_start_time=None):
        self.notify_channels = notify_channels  # type: list[str]
        self.notify_end_time = notify_end_time  # type: str
        self.notify_objects = notify_objects  # type: list[ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRuleNotifyObjects]
        self.notify_start_time = notify_start_time  # type: str

    def validate(self):
        if self.notify_objects:
            for k in self.notify_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.notify_end_time is not None:
            result['NotifyEndTime'] = self.notify_end_time
        result['NotifyObjects'] = []
        if self.notify_objects is not None:
            for k in self.notify_objects:
                result['NotifyObjects'].append(k.to_map() if k else None)
        if self.notify_start_time is not None:
            result['NotifyStartTime'] = self.notify_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('NotifyEndTime') is not None:
            self.notify_end_time = m.get('NotifyEndTime')
        self.notify_objects = []
        if m.get('NotifyObjects') is not None:
            for k in m.get('NotifyObjects'):
                temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRuleNotifyObjects()
                self.notify_objects.append(temp_model.from_map(k))
        if m.get('NotifyStartTime') is not None:
            self.notify_start_time = m.get('NotifyStartTime')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyTemplate(TeaModel):
    def __init__(self, email_content=None, email_recover_content=None, email_recover_title=None, email_title=None,
                 robot_content=None, sms_content=None, sms_recover_content=None, tts_content=None, tts_recover_content=None):
        self.email_content = email_content  # type: str
        self.email_recover_content = email_recover_content  # type: str
        self.email_recover_title = email_recover_title  # type: str
        self.email_title = email_title  # type: str
        self.robot_content = robot_content  # type: str
        self.sms_content = sms_content  # type: str
        self.sms_recover_content = sms_recover_content  # type: str
        self.tts_content = tts_content  # type: str
        self.tts_recover_content = tts_recover_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email_content is not None:
            result['EmailContent'] = self.email_content
        if self.email_recover_content is not None:
            result['EmailRecoverContent'] = self.email_recover_content
        if self.email_recover_title is not None:
            result['EmailRecoverTitle'] = self.email_recover_title
        if self.email_title is not None:
            result['EmailTitle'] = self.email_title
        if self.robot_content is not None:
            result['RobotContent'] = self.robot_content
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.sms_recover_content is not None:
            result['SmsRecoverContent'] = self.sms_recover_content
        if self.tts_content is not None:
            result['TtsContent'] = self.tts_content
        if self.tts_recover_content is not None:
            result['TtsRecoverContent'] = self.tts_recover_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EmailContent') is not None:
            self.email_content = m.get('EmailContent')
        if m.get('EmailRecoverContent') is not None:
            self.email_recover_content = m.get('EmailRecoverContent')
        if m.get('EmailRecoverTitle') is not None:
            self.email_recover_title = m.get('EmailRecoverTitle')
        if m.get('EmailTitle') is not None:
            self.email_title = m.get('EmailTitle')
        if m.get('RobotContent') is not None:
            self.robot_content = m.get('RobotContent')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('SmsRecoverContent') is not None:
            self.sms_recover_content = m.get('SmsRecoverContent')
        if m.get('TtsContent') is not None:
            self.tts_content = m.get('TtsContent')
        if m.get('TtsRecoverContent') is not None:
            self.tts_recover_content = m.get('TtsRecoverContent')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPolicies(TeaModel):
    def __init__(self, escalation_policy_id=None, group_rule=None, id=None, integration_id=None,
                 matching_rules=None, name=None, notify_rule=None, notify_template=None, repeat=None, repeat_interval=None,
                 send_recover_message=None):
        self.escalation_policy_id = escalation_policy_id  # type: long
        self.group_rule = group_rule  # type: ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesGroupRule
        self.id = id  # type: long
        self.integration_id = integration_id  # type: long
        self.matching_rules = matching_rules  # type: list[ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRules]
        self.name = name  # type: str
        self.notify_rule = notify_rule  # type: ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRule
        self.notify_template = notify_template  # type: ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyTemplate
        self.repeat = repeat  # type: bool
        self.repeat_interval = repeat_interval  # type: long
        self.send_recover_message = send_recover_message  # type: bool

    def validate(self):
        if self.group_rule:
            self.group_rule.validate()
        if self.matching_rules:
            for k in self.matching_rules:
                if k:
                    k.validate()
        if self.notify_rule:
            self.notify_rule.validate()
        if self.notify_template:
            self.notify_template.validate()

    def to_map(self):
        _map = super(ListNotificationPoliciesResponseBodyPageBeanNotificationPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_policy_id is not None:
            result['EscalationPolicyId'] = self.escalation_policy_id
        if self.group_rule is not None:
            result['GroupRule'] = self.group_rule.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        result['MatchingRules'] = []
        if self.matching_rules is not None:
            for k in self.matching_rules:
                result['MatchingRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.notify_rule is not None:
            result['NotifyRule'] = self.notify_rule.to_map()
        if self.notify_template is not None:
            result['NotifyTemplate'] = self.notify_template.to_map()
        if self.repeat is not None:
            result['Repeat'] = self.repeat
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        if self.send_recover_message is not None:
            result['SendRecoverMessage'] = self.send_recover_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EscalationPolicyId') is not None:
            self.escalation_policy_id = m.get('EscalationPolicyId')
        if m.get('GroupRule') is not None:
            temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesGroupRule()
            self.group_rule = temp_model.from_map(m['GroupRule'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        self.matching_rules = []
        if m.get('MatchingRules') is not None:
            for k in m.get('MatchingRules'):
                temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRules()
                self.matching_rules.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotifyRule') is not None:
            temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRule()
            self.notify_rule = temp_model.from_map(m['NotifyRule'])
        if m.get('NotifyTemplate') is not None:
            temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyTemplate()
            self.notify_template = temp_model.from_map(m['NotifyTemplate'])
        if m.get('Repeat') is not None:
            self.repeat = m.get('Repeat')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        if m.get('SendRecoverMessage') is not None:
            self.send_recover_message = m.get('SendRecoverMessage')
        return self


class ListNotificationPoliciesResponseBodyPageBean(TeaModel):
    def __init__(self, notification_policies=None, page=None, size=None, total=None):
        self.notification_policies = notification_policies  # type: list[ListNotificationPoliciesResponseBodyPageBeanNotificationPolicies]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.notification_policies:
            for k in self.notification_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNotificationPoliciesResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotificationPolicies'] = []
        if self.notification_policies is not None:
            for k in self.notification_policies:
                result['NotificationPolicies'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.notification_policies = []
        if m.get('NotificationPolicies') is not None:
            for k in m.get('NotificationPolicies'):
                temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPolicies()
                self.notification_policies.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListNotificationPoliciesResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: ListNotificationPoliciesResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(ListNotificationPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListNotificationPoliciesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNotificationPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNotificationPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNotificationPoliciesResponse, self).to_map()
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
            temp_model = ListNotificationPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOnCallSchedulesRequest(TeaModel):
    def __init__(self, name=None, page=None, size=None):
        self.name = name  # type: str
        self.page = page  # type: long
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOnCallSchedulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListOnCallSchedulesResponseBodyPageBeanOnCallSchedules(TeaModel):
    def __init__(self, description=None, id=None, name=None):
        self.description = description  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOnCallSchedulesResponseBodyPageBeanOnCallSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListOnCallSchedulesResponseBodyPageBean(TeaModel):
    def __init__(self, on_call_schedules=None, page=None, size=None, total=None):
        self.on_call_schedules = on_call_schedules  # type: list[ListOnCallSchedulesResponseBodyPageBeanOnCallSchedules]
        self.page = page  # type: long
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.on_call_schedules:
            for k in self.on_call_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOnCallSchedulesResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OnCallSchedules'] = []
        if self.on_call_schedules is not None:
            for k in self.on_call_schedules:
                result['OnCallSchedules'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.on_call_schedules = []
        if m.get('OnCallSchedules') is not None:
            for k in m.get('OnCallSchedules'):
                temp_model = ListOnCallSchedulesResponseBodyPageBeanOnCallSchedules()
                self.on_call_schedules.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListOnCallSchedulesResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: ListOnCallSchedulesResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(ListOnCallSchedulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListOnCallSchedulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOnCallSchedulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOnCallSchedulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOnCallSchedulesResponse, self).to_map()
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
            temp_model = ListOnCallSchedulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrometheusAlertRulesRequest(TeaModel):
    def __init__(self, cluster_id=None, match_expressions=None, name=None, region_id=None, status=None, type=None):
        self.cluster_id = cluster_id  # type: str
        self.match_expressions = match_expressions  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.match_expressions is not None:
            result['MatchExpressions'] = self.match_expressions
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MatchExpressions') is not None:
            self.match_expressions = m.get('MatchExpressions')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertRulesResponseBodyPrometheusAlertRules(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None,
                 duration=None, expression=None, labels=None, message=None, notify_type=None, status=None, type=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: list[ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations]
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: list[ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels]
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.status = status  # type: int
        self.type = type  # type: str

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertRulesResponseBodyPrometheusAlertRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPrometheusAlertRulesResponseBody(TeaModel):
    def __init__(self, prometheus_alert_rules=None, request_id=None):
        self.prometheus_alert_rules = prometheus_alert_rules  # type: list[ListPrometheusAlertRulesResponseBodyPrometheusAlertRules]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prometheus_alert_rules:
            for k in self.prometheus_alert_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrometheusAlertRules'] = []
        if self.prometheus_alert_rules is not None:
            for k in self.prometheus_alert_rules:
                result['PrometheusAlertRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prometheus_alert_rules = []
        if m.get('PrometheusAlertRules') is not None:
            for k in m.get('PrometheusAlertRules'):
                temp_model = ListPrometheusAlertRulesResponseBodyPrometheusAlertRules()
                self.prometheus_alert_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrometheusAlertRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrometheusAlertRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertRulesResponse, self).to_map()
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
            temp_model = ListPrometheusAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrometheusAlertTemplatesRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesRequest, self).to_map()
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


class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates(TeaModel):
    def __init__(self, alert_name=None, annotations=None, description=None, duration=None, expression=None,
                 labels=None, type=None, version=None):
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: list[ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations]
        self.description = description  # type: str
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: list[ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels]
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListPrometheusAlertTemplatesResponseBody(TeaModel):
    def __init__(self, prometheus_alert_templates=None, request_id=None):
        self.prometheus_alert_templates = prometheus_alert_templates  # type: list[ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prometheus_alert_templates:
            for k in self.prometheus_alert_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrometheusAlertTemplates'] = []
        if self.prometheus_alert_templates is not None:
            for k in self.prometheus_alert_templates:
                result['PrometheusAlertTemplates'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prometheus_alert_templates = []
        if m.get('PrometheusAlertTemplates') is not None:
            for k in m.get('PrometheusAlertTemplates'):
                temp_model = ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates()
                self.prometheus_alert_templates.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrometheusAlertTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrometheusAlertTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesResponse, self).to_map()
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
            temp_model = ListPrometheusAlertTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrometheusGlobalViewRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusGlobalViewRequest, self).to_map()
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


class ListPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusGlobalViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrometheusGlobalViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrometheusGlobalViewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrometheusGlobalViewResponse, self).to_map()
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
            temp_model = ListPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrometheusInstancesRequest(TeaModel):
    def __init__(self, region_id=None, show_global_view=None):
        self.region_id = region_id  # type: str
        self.show_global_view = show_global_view  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show_global_view is not None:
            result['ShowGlobalView'] = self.show_global_view
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShowGlobalView') is not None:
            self.show_global_view = m.get('ShowGlobalView')
        return self


class ListPrometheusInstancesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrometheusInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrometheusInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrometheusInstancesResponse, self).to_map()
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
            temp_model = ListPrometheusInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRetcodeAppsRequest(TeaModel):
    def __init__(self, region_id=None, security_token=None):
        self.region_id = region_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRetcodeAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ListRetcodeAppsResponseBodyRetcodeApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, pid=None, retcode_app_type=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.pid = pid  # type: str
        self.retcode_app_type = retcode_app_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRetcodeAppsResponseBodyRetcodeApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')
        return self


class ListRetcodeAppsResponseBody(TeaModel):
    def __init__(self, request_id=None, retcode_apps=None):
        self.request_id = request_id  # type: str
        self.retcode_apps = retcode_apps  # type: list[ListRetcodeAppsResponseBodyRetcodeApps]

    def validate(self):
        if self.retcode_apps:
            for k in self.retcode_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRetcodeAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RetcodeApps'] = []
        if self.retcode_apps is not None:
            for k in self.retcode_apps:
                result['RetcodeApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.retcode_apps = []
        if m.get('RetcodeApps') is not None:
            for k in m.get('RetcodeApps'):
                temp_model = ListRetcodeAppsResponseBodyRetcodeApps()
                self.retcode_apps.append(temp_model.from_map(k))
        return self


class ListRetcodeAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRetcodeAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRetcodeAppsResponse, self).to_map()
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
            temp_model = ListRetcodeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenarioRequest(TeaModel):
    def __init__(self, app_id=None, name=None, region_id=None, scenario=None, sign=None):
        self.app_id = app_id  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.scenario = scenario  # type: str
        self.sign = sign  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListScenarioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class ListScenarioResponseBodyArmsScenarios(TeaModel):
    def __init__(self, app_id=None, create_time=None, extensions=None, id=None, name=None, region_id=None, sign=None,
                 update_time=None, user_id=None):
        self.app_id = app_id  # type: str
        self.create_time = create_time  # type: str
        self.extensions = extensions  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.sign = sign  # type: str
        self.update_time = update_time  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListScenarioResponseBodyArmsScenarios, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListScenarioResponseBody(TeaModel):
    def __init__(self, arms_scenarios=None, request_id=None):
        self.arms_scenarios = arms_scenarios  # type: list[ListScenarioResponseBodyArmsScenarios]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.arms_scenarios:
            for k in self.arms_scenarios:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListScenarioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ArmsScenarios'] = []
        if self.arms_scenarios is not None:
            for k in self.arms_scenarios:
                result['ArmsScenarios'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.arms_scenarios = []
        if m.get('ArmsScenarios') is not None:
            for k in m.get('ArmsScenarios'):
                temp_model = ListScenarioResponseBodyArmsScenarios()
                self.arms_scenarios.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListScenarioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListScenarioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListScenarioResponse, self).to_map()
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
            temp_model = ListScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSilencePoliciesRequest(TeaModel):
    def __init__(self, is_detail=None, name=None, page=None, region_id=None, size=None):
        self.is_detail = is_detail  # type: bool
        self.name = name  # type: str
        self.page = page  # type: long
        self.region_id = region_id  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSilencePoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRulesMatchingConditions(TeaModel):
    def __init__(self, key=None, operator=None, value=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRulesMatchingConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRules(TeaModel):
    def __init__(self, matching_conditions=None):
        self.matching_conditions = matching_conditions  # type: list[ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRulesMatchingConditions]

    def validate(self):
        if self.matching_conditions:
            for k in self.matching_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchingConditions'] = []
        if self.matching_conditions is not None:
            for k in self.matching_conditions:
                result['MatchingConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.matching_conditions = []
        if m.get('MatchingConditions') is not None:
            for k in m.get('MatchingConditions'):
                temp_model = ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k))
        return self


class ListSilencePoliciesResponseBodyPageBeanSilencePolicies(TeaModel):
    def __init__(self, id=None, matching_rules=None, name=None):
        self.id = id  # type: long
        self.matching_rules = matching_rules  # type: list[ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRules]
        self.name = name  # type: str

    def validate(self):
        if self.matching_rules:
            for k in self.matching_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSilencePoliciesResponseBodyPageBeanSilencePolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['MatchingRules'] = []
        if self.matching_rules is not None:
            for k in self.matching_rules:
                result['MatchingRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.matching_rules = []
        if m.get('MatchingRules') is not None:
            for k in m.get('MatchingRules'):
                temp_model = ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRules()
                self.matching_rules.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListSilencePoliciesResponseBodyPageBean(TeaModel):
    def __init__(self, page=None, silence_policies=None, size=None, total=None):
        self.page = page  # type: long
        self.silence_policies = silence_policies  # type: list[ListSilencePoliciesResponseBodyPageBeanSilencePolicies]
        self.size = size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.silence_policies:
            for k in self.silence_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSilencePoliciesResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        result['SilencePolicies'] = []
        if self.silence_policies is not None:
            for k in self.silence_policies:
                result['SilencePolicies'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        self.silence_policies = []
        if m.get('SilencePolicies') is not None:
            for k in m.get('SilencePolicies'):
                temp_model = ListSilencePoliciesResponseBodyPageBeanSilencePolicies()
                self.silence_policies.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSilencePoliciesResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: ListSilencePoliciesResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(ListSilencePoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListSilencePoliciesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSilencePoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSilencePoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSilencePoliciesResponse, self).to_map()
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
            temp_model = ListSilencePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTraceAppsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTraceAppsRequest, self).to_map()
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


class ListTraceAppsResponseBodyTraceApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, labels=None, pid=None, region_id=None, show=None,
                 type=None, update_time=None, user_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.labels = labels  # type: list[str]
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.show = show  # type: bool
        self.type = type  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTraceAppsResponseBodyTraceApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListTraceAppsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, trace_apps=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_apps = trace_apps  # type: list[ListTraceAppsResponseBodyTraceApps]

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTraceAppsResponseBody, self).to_map()
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
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
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
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = ListTraceAppsResponseBodyTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        return self


class ListTraceAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTraceAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTraceAppsResponse, self).to_map()
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
            temp_model = ListTraceAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManageGetRecordingRuleRequest(TeaModel):
    def __init__(self, cluster_id=None, query_user_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.query_user_id = query_user_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ManageGetRecordingRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.query_user_id is not None:
            result['QueryUserId'] = self.query_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueryUserId') is not None:
            self.query_user_id = m.get('QueryUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ManageGetRecordingRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ManageGetRecordingRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ManageGetRecordingRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ManageGetRecordingRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ManageGetRecordingRuleResponse, self).to_map()
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
            temp_model = ManageGetRecordingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManageRecordingRuleRequest(TeaModel):
    def __init__(self, cluster_id=None, query_user_id=None, region_id=None, rule_yaml=None):
        self.cluster_id = cluster_id  # type: str
        self.query_user_id = query_user_id  # type: str
        self.region_id = region_id  # type: str
        self.rule_yaml = rule_yaml  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ManageRecordingRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.query_user_id is not None:
            result['QueryUserId'] = self.query_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_yaml is not None:
            result['RuleYaml'] = self.rule_yaml
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueryUserId') is not None:
            self.query_user_id = m.get('QueryUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleYaml') is not None:
            self.rule_yaml = m.get('RuleYaml')
        return self


class ManageRecordingRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ManageRecordingRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ManageRecordingRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ManageRecordingRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ManageRecordingRuleResponse, self).to_map()
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
            temp_model = ManageRecordingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenArmsDefaultSLRRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenArmsDefaultSLRRequest, self).to_map()
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


class OpenArmsDefaultSLRResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenArmsDefaultSLRResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenArmsDefaultSLRResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenArmsDefaultSLRResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenArmsDefaultSLRResponse, self).to_map()
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
            temp_model = OpenArmsDefaultSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenArmsServiceSecondVersionRequest(TeaModel):
    def __init__(self, region_id=None, type=None):
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenArmsServiceSecondVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OpenArmsServiceSecondVersionResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenArmsServiceSecondVersionResponseBody, self).to_map()
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


class OpenArmsServiceSecondVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenArmsServiceSecondVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenArmsServiceSecondVersionResponse, self).to_map()
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
            temp_model = OpenArmsServiceSecondVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenVClusterRequest(TeaModel):
    def __init__(self, cluster_type=None, length=None, product=None, recreate_switch=None, region_id=None):
        self.cluster_type = cluster_type  # type: str
        self.length = length  # type: int
        self.product = product  # type: str
        self.recreate_switch = recreate_switch  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenVClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.length is not None:
            result['Length'] = self.length
        if self.product is not None:
            result['Product'] = self.product
        if self.recreate_switch is not None:
            result['RecreateSwitch'] = self.recreate_switch
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RecreateSwitch') is not None:
            self.recreate_switch = m.get('RecreateSwitch')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenVClusterResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenVClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenVClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenVClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenVClusterResponse, self).to_map()
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
            temp_model = OpenVClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenXtraceDefaultSLRRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenXtraceDefaultSLRRequest, self).to_map()
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


class OpenXtraceDefaultSLRResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenXtraceDefaultSLRResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenXtraceDefaultSLRResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenXtraceDefaultSLRResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenXtraceDefaultSLRResponse, self).to_map()
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
            temp_model = OpenXtraceDefaultSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricByPageRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMetricByPageRequestFilters, self).to_map()
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


class QueryMetricByPageRequest(TeaModel):
    def __init__(self, current_page=None, custom_filters=None, dimensions=None, end_time=None, filters=None,
                 interval_in_sec=None, measures=None, metric=None, order=None, order_by=None, page_size=None, start_time=None):
        self.current_page = current_page  # type: int
        self.custom_filters = custom_filters  # type: list[str]
        self.dimensions = dimensions  # type: list[str]
        self.end_time = end_time  # type: long
        self.filters = filters  # type: list[QueryMetricByPageRequestFilters]
        self.interval_in_sec = interval_in_sec  # type: int
        self.measures = measures  # type: list[str]
        self.metric = metric  # type: str
        self.order = order  # type: str
        self.order_by = order_by  # type: str
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: long

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMetricByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.custom_filters is not None:
            result['CustomFilters'] = self.custom_filters
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.order is not None:
            result['Order'] = self.order
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('CustomFilters') is not None:
            self.custom_filters = m.get('CustomFilters')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = QueryMetricByPageRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryMetricByPageResponseBodyData(TeaModel):
    def __init__(self, items=None, page=None, page_size=None, total=None):
        self.items = items  # type: list[dict[str, any]]
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMetricByPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryMetricByPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryMetricByPageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryMetricByPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = QueryMetricByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMetricByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMetricByPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMetricByPageResponse, self).to_map()
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
            temp_model = QueryMetricByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPromInstallStatusRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPromInstallStatusRequest, self).to_map()
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


class QueryPromInstallStatusResponseBodyData(TeaModel):
    def __init__(self, is_controller_installed=None):
        self.is_controller_installed = is_controller_installed  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPromInstallStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_controller_installed is not None:
            result['isControllerInstalled'] = self.is_controller_installed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('isControllerInstalled') is not None:
            self.is_controller_installed = m.get('isControllerInstalled')
        return self


class QueryPromInstallStatusResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: QueryPromInstallStatusResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryPromInstallStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryPromInstallStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPromInstallStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPromInstallStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPromInstallStatusResponse, self).to_map()
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
            temp_model = QueryPromInstallStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReleaseMetricRequest(TeaModel):
    def __init__(self, change_order_id=None, create_time=None, metric_type=None, pid=None, proxy_user_id=None,
                 release_end_time=None, release_start_time=None, service=None):
        self.change_order_id = change_order_id  # type: str
        self.create_time = create_time  # type: long
        self.metric_type = metric_type  # type: str
        self.pid = pid  # type: str
        self.proxy_user_id = proxy_user_id  # type: str
        self.release_end_time = release_end_time  # type: long
        self.release_start_time = release_start_time  # type: long
        self.service = service  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryReleaseMetricRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.release_end_time is not None:
            result['ReleaseEndTime'] = self.release_end_time
        if self.release_start_time is not None:
            result['ReleaseStartTime'] = self.release_start_time
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ReleaseEndTime') is not None:
            self.release_end_time = m.get('ReleaseEndTime')
        if m.get('ReleaseStartTime') is not None:
            self.release_start_time = m.get('ReleaseStartTime')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class QueryReleaseMetricResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryReleaseMetricResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryReleaseMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryReleaseMetricResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryReleaseMetricResponse, self).to_map()
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
            temp_model = QueryReleaseMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAliClusterIdsFromPrometheusGlobalViewRequest(TeaModel):
    def __init__(self, cluster_ids=None, global_view_cluster_id=None, group_name=None, region_id=None):
        self.cluster_ids = cluster_ids  # type: str
        self.global_view_cluster_id = global_view_cluster_id  # type: str
        self.group_name = group_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveAliClusterIdsFromPrometheusGlobalViewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveAliClusterIdsFromPrometheusGlobalViewResponseBodyData(TeaModel):
    def __init__(self, info=None, msg=None, success=None):
        self.info = info  # type: str
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveAliClusterIdsFromPrometheusGlobalViewResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveAliClusterIdsFromPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RemoveAliClusterIdsFromPrometheusGlobalViewResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RemoveAliClusterIdsFromPrometheusGlobalViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RemoveAliClusterIdsFromPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveAliClusterIdsFromPrometheusGlobalViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveAliClusterIdsFromPrometheusGlobalViewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveAliClusterIdsFromPrometheusGlobalViewResponse, self).to_map()
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
            temp_model = RemoveAliClusterIdsFromPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSourcesFromPrometheusGlobalViewRequest(TeaModel):
    def __init__(self, global_view_cluster_id=None, group_name=None, region_id=None, source_names=None):
        self.global_view_cluster_id = global_view_cluster_id  # type: str
        self.group_name = group_name  # type: str
        self.region_id = region_id  # type: str
        self.source_names = source_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSourcesFromPrometheusGlobalViewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_names is not None:
            result['SourceNames'] = self.source_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceNames') is not None:
            self.source_names = m.get('SourceNames')
        return self


class RemoveSourcesFromPrometheusGlobalViewResponseBodyData(TeaModel):
    def __init__(self, info=None, msg=None, success=None):
        self.info = info  # type: str
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSourcesFromPrometheusGlobalViewResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveSourcesFromPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RemoveSourcesFromPrometheusGlobalViewResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RemoveSourcesFromPrometheusGlobalViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RemoveSourcesFromPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveSourcesFromPrometheusGlobalViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveSourcesFromPrometheusGlobalViewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveSourcesFromPrometheusGlobalViewResponse, self).to_map()
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
            temp_model = RemoveSourcesFromPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTraceAppConfigRequestSettings(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTraceAppConfigRequestSettings, self).to_map()
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


class SaveTraceAppConfigRequest(TeaModel):
    def __init__(self, pid=None, settings=None):
        self.pid = pid  # type: str
        self.settings = settings  # type: list[SaveTraceAppConfigRequestSettings]

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveTraceAppConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        result['Settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['Settings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        self.settings = []
        if m.get('Settings') is not None:
            for k in m.get('Settings'):
                temp_model = SaveTraceAppConfigRequestSettings()
                self.settings.append(temp_model.from_map(k))
        return self


class SaveTraceAppConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTraceAppConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveTraceAppConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveTraceAppConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTraceAppConfigResponse, self).to_map()
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
            temp_model = SaveTraceAppConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertContactRequest(TeaModel):
    def __init__(self, contact_ids=None, contact_name=None, current_page=None, email=None, page_size=None,
                 phone=None, region_id=None):
        self.contact_ids = contact_ids  # type: str
        self.contact_name = contact_name  # type: str
        self.current_page = current_page  # type: str
        self.email = email  # type: str
        self.page_size = page_size  # type: str
        self.phone = phone  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.email is not None:
            result['Email'] = self.email
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchAlertContactResponseBodyPageBeanContacts(TeaModel):
    def __init__(self, contact_id=None, contact_name=None, content=None, create_time=None, ding_robot=None,
                 email=None, phone=None, system_noc=None, update_time=None, user_id=None, webhook=None):
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.content = content  # type: str
        self.create_time = create_time  # type: long
        self.ding_robot = ding_robot  # type: str
        self.email = email  # type: str
        self.phone = phone  # type: str
        self.system_noc = system_noc  # type: bool
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str
        self.webhook = webhook  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertContactResponseBodyPageBeanContacts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class SearchAlertContactResponseBodyPageBean(TeaModel):
    def __init__(self, contacts=None, page_number=None, page_size=None, total_count=None):
        self.contacts = contacts  # type: list[SearchAlertContactResponseBodyPageBeanContacts]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertContactResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = SearchAlertContactResponseBodyPageBeanContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertContactResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchAlertContactResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchAlertContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertContactResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchAlertContactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchAlertContactResponse, self).to_map()
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
            temp_model = SearchAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertContactGroupRequest(TeaModel):
    def __init__(self, contact_group_ids=None, contact_group_name=None, contact_id=None, contact_name=None,
                 is_detail=None, region_id=None):
        self.contact_group_ids = contact_group_ids  # type: str
        self.contact_group_name = contact_group_name  # type: str
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.is_detail = is_detail  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertContactGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchAlertContactGroupResponseBodyContactGroupsContacts(TeaModel):
    def __init__(self, contact_id=None, contact_name=None, create_time=None, ding_robot=None, email=None, phone=None,
                 system_noc=None, update_time=None, user_id=None):
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.create_time = create_time  # type: long
        self.ding_robot = ding_robot  # type: str
        self.email = email  # type: str
        self.phone = phone  # type: str
        self.system_noc = system_noc  # type: bool
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertContactGroupResponseBodyContactGroupsContacts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertContactGroupResponseBodyContactGroups(TeaModel):
    def __init__(self, contact_group_id=None, contact_group_name=None, contacts=None, create_time=None,
                 update_time=None, user_id=None):
        self.contact_group_id = contact_group_id  # type: long
        self.contact_group_name = contact_group_name  # type: str
        self.contacts = contacts  # type: list[SearchAlertContactGroupResponseBodyContactGroupsContacts]
        self.create_time = create_time  # type: long
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertContactGroupResponseBodyContactGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = SearchAlertContactGroupResponseBodyContactGroupsContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertContactGroupResponseBody(TeaModel):
    def __init__(self, contact_groups=None, request_id=None):
        self.contact_groups = contact_groups  # type: list[SearchAlertContactGroupResponseBodyContactGroups]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.contact_groups:
            for k in self.contact_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertContactGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactGroups'] = []
        if self.contact_groups is not None:
            for k in self.contact_groups:
                result['ContactGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contact_groups = []
        if m.get('ContactGroups') is not None:
            for k in m.get('ContactGroups'):
                temp_model = SearchAlertContactGroupResponseBodyContactGroups()
                self.contact_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertContactGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchAlertContactGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchAlertContactGroupResponse, self).to_map()
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
            temp_model = SearchAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertHistoriesRequest(TeaModel):
    def __init__(self, alert_id=None, alert_type=None, current_page=None, end_time=None, page_size=None,
                 region_id=None, start_time=None):
        self.alert_id = alert_id  # type: long
        self.alert_type = alert_type  # type: int
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertHistoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchAlertHistoriesResponseBodyPageBeanAlarmHistories(TeaModel):
    def __init__(self, alarm_content=None, alarm_response_code=None, alarm_sources=None, alarm_time=None,
                 alarm_type=None, emails=None, id=None, phones=None, strategy_id=None, target=None, user_id=None):
        self.alarm_content = alarm_content  # type: str
        self.alarm_response_code = alarm_response_code  # type: int
        self.alarm_sources = alarm_sources  # type: str
        self.alarm_time = alarm_time  # type: long
        self.alarm_type = alarm_type  # type: int
        self.emails = emails  # type: str
        self.id = id  # type: long
        self.phones = phones  # type: str
        self.strategy_id = strategy_id  # type: str
        self.target = target  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertHistoriesResponseBodyPageBeanAlarmHistories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_content is not None:
            result['AlarmContent'] = self.alarm_content
        if self.alarm_response_code is not None:
            result['AlarmResponseCode'] = self.alarm_response_code
        if self.alarm_sources is not None:
            result['AlarmSources'] = self.alarm_sources
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.id is not None:
            result['Id'] = self.id
        if self.phones is not None:
            result['Phones'] = self.phones
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.target is not None:
            result['Target'] = self.target
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmContent') is not None:
            self.alarm_content = m.get('AlarmContent')
        if m.get('AlarmResponseCode') is not None:
            self.alarm_response_code = m.get('AlarmResponseCode')
        if m.get('AlarmSources') is not None:
            self.alarm_sources = m.get('AlarmSources')
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Phones') is not None:
            self.phones = m.get('Phones')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertHistoriesResponseBodyPageBean(TeaModel):
    def __init__(self, alarm_histories=None, page_number=None, page_size=None, total_count=None):
        self.alarm_histories = alarm_histories  # type: list[SearchAlertHistoriesResponseBodyPageBeanAlarmHistories]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.alarm_histories:
            for k in self.alarm_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertHistoriesResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmHistories'] = []
        if self.alarm_histories is not None:
            for k in self.alarm_histories:
                result['AlarmHistories'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alarm_histories = []
        if m.get('AlarmHistories') is not None:
            for k in m.get('AlarmHistories'):
                temp_model = SearchAlertHistoriesResponseBodyPageBeanAlarmHistories()
                self.alarm_histories.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertHistoriesResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchAlertHistoriesResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchAlertHistoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertHistoriesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertHistoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchAlertHistoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchAlertHistoriesResponse, self).to_map()
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
            temp_model = SearchAlertHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertRulesRequest(TeaModel):
    def __init__(self, app_type=None, current_page=None, page_size=None, pid=None, region_id=None,
                 system_region_id=None, title=None, type=None):
        self.app_type = app_type  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.system_region_id = system_region_id  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_region_id is not None:
            result['SystemRegionId'] = self.system_region_id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemRegionId') is not None:
            self.system_region_id = m.get('SystemRegionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext(TeaModel):
    def __init__(self, alarm_content_sub_title=None, alarm_content_template=None, content=None, sub_title=None):
        self.alarm_content_sub_title = alarm_content_sub_title  # type: str
        self.alarm_content_template = alarm_content_template  # type: str
        self.content = content  # type: str
        self.sub_title = sub_title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_content_sub_title is not None:
            result['AlarmContentSubTitle'] = self.alarm_content_sub_title
        if self.alarm_content_template is not None:
            result['AlarmContentTemplate'] = self.alarm_content_template
        if self.content is not None:
            result['Content'] = self.content
        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmContentSubTitle') is not None:
            self.alarm_content_sub_title = m.get('AlarmContentSubTitle')
        if m.get('AlarmContentTemplate') is not None:
            self.alarm_content_template = m.get('AlarmContentTemplate')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules(TeaModel):
    def __init__(self, aggregates=None, alias=None, measure=None, nvalue=None, operator=None, value=None):
        self.aggregates = aggregates  # type: str
        self.alias = alias  # type: str
        self.measure = measure  # type: str
        self.nvalue = nvalue  # type: int
        self.operator = operator  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.measure is not None:
            result['Measure'] = self.measure
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Measure') is not None:
            self.measure = m.get('Measure')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule(TeaModel):
    def __init__(self, operator=None, rules=None):
        self.operator = operator  # type: str
        self.rules = rules  # type: list[SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['Operator'] = self.operator
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules()
                self.rules.append(temp_model.from_map(k))
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam(TeaModel):
    def __init__(self, app_group_id=None, app_id=None, dimensions=None, pid=None, type=None):
        self.app_group_id = app_group_id  # type: str
        self.app_id = app_id  # type: str
        self.dimensions = dimensions  # type: list[SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions]
        self.pid = pid  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesNotice(TeaModel):
    def __init__(self, end_time=None, notice_end_time=None, notice_start_time=None, start_time=None):
        self.end_time = end_time  # type: long
        self.notice_end_time = notice_end_time  # type: long
        self.notice_start_time = notice_start_time  # type: long
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesNotice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.notice_end_time is not None:
            result['NoticeEndTime'] = self.notice_end_time
        if self.notice_start_time is not None:
            result['NoticeStartTime'] = self.notice_start_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NoticeEndTime') is not None:
            self.notice_end_time = m.get('NoticeEndTime')
        if m.get('NoticeStartTime') is not None:
            self.notice_start_time = m.get('NoticeStartTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRules(TeaModel):
    def __init__(self, alarm_context=None, alert_level=None, alert_rule=None, alert_title=None, alert_type=None,
                 alert_version=None, alert_ways=None, config=None, contact_group_id_list=None, contact_group_ids=None,
                 create_time=None, host_by_alert_manager=None, id=None, metric_param=None, notice=None, region_id=None,
                 status=None, task_id=None, task_status=None, title=None, update_time=None, user_id=None):
        self.alarm_context = alarm_context  # type: SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext
        self.alert_level = alert_level  # type: str
        self.alert_rule = alert_rule  # type: SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule
        self.alert_title = alert_title  # type: str
        self.alert_type = alert_type  # type: int
        self.alert_version = alert_version  # type: int
        self.alert_ways = alert_ways  # type: list[str]
        self.config = config  # type: str
        self.contact_group_id_list = contact_group_id_list  # type: str
        self.contact_group_ids = contact_group_ids  # type: str
        self.create_time = create_time  # type: long
        self.host_by_alert_manager = host_by_alert_manager  # type: bool
        self.id = id  # type: long
        self.metric_param = metric_param  # type: SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam
        self.notice = notice  # type: SearchAlertRulesResponseBodyPageBeanAlertRulesNotice
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: long
        self.task_status = task_status  # type: str
        self.title = title  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        if self.alarm_context:
            self.alarm_context.validate()
        if self.alert_rule:
            self.alert_rule.validate()
        if self.metric_param:
            self.metric_param.validate()
        if self.notice:
            self.notice.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_context is not None:
            result['AlarmContext'] = self.alarm_context.to_map()
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule.to_map()
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_version is not None:
            result['AlertVersion'] = self.alert_version
        if self.alert_ways is not None:
            result['AlertWays'] = self.alert_ways
        if self.config is not None:
            result['Config'] = self.config
        if self.contact_group_id_list is not None:
            result['ContactGroupIdList'] = self.contact_group_id_list
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.host_by_alert_manager is not None:
            result['HostByAlertManager'] = self.host_by_alert_manager
        if self.id is not None:
            result['Id'] = self.id
        if self.metric_param is not None:
            result['MetricParam'] = self.metric_param.to_map()
        if self.notice is not None:
            result['Notice'] = self.notice.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmContext') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext()
            self.alarm_context = temp_model.from_map(m['AlarmContext'])
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertRule') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule()
            self.alert_rule = temp_model.from_map(m['AlertRule'])
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertVersion') is not None:
            self.alert_version = m.get('AlertVersion')
        if m.get('AlertWays') is not None:
            self.alert_ways = m.get('AlertWays')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ContactGroupIdList') is not None:
            self.contact_group_id_list = m.get('ContactGroupIdList')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HostByAlertManager') is not None:
            self.host_by_alert_manager = m.get('HostByAlertManager')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetricParam') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam()
            self.metric_param = temp_model.from_map(m['MetricParam'])
        if m.get('Notice') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesNotice()
            self.notice = temp_model.from_map(m['Notice'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertRulesResponseBodyPageBean(TeaModel):
    def __init__(self, alert_rules=None, page_number=None, page_size=None, total_count=None):
        self.alert_rules = alert_rules  # type: list[SearchAlertRulesResponseBodyPageBeanAlertRules]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.alert_rules:
            for k in self.alert_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertRules'] = []
        if self.alert_rules is not None:
            for k in self.alert_rules:
                result['AlertRules'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alert_rules = []
        if m.get('AlertRules') is not None:
            for k in m.get('AlertRules'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRules()
                self.alert_rules.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertRulesResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchAlertRulesResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchAlertRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponse, self).to_map()
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
            temp_model = SearchAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEventsRequest(TeaModel):
    def __init__(self, alert_id=None, alert_type=None, app_type=None, current_page=None, end_time=None,
                 is_trigger=None, page_size=None, pid=None, region_id=None, start_time=None):
        self.alert_id = alert_id  # type: long
        self.alert_type = alert_type  # type: int
        self.app_type = app_type  # type: str
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.is_trigger = is_trigger  # type: int
        self.page_size = page_size  # type: int
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_trigger is not None:
            result['IsTrigger'] = self.is_trigger
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsTrigger') is not None:
            self.is_trigger = m.get('IsTrigger')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchEventsResponseBodyPageBeanEvent(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, alert_rule=None, alert_type=None, event_level=None,
                 event_time=None, id=None, links=None, message=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.alert_rule = alert_rule  # type: str
        self.alert_type = alert_type  # type: int
        self.event_level = event_level  # type: str
        self.event_time = event_time  # type: long
        self.id = id  # type: long
        self.links = links  # type: list[str]
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchEventsResponseBodyPageBeanEvent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.id is not None:
            result['Id'] = self.id
        if self.links is not None:
            result['Links'] = self.links
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertRule') is not None:
            self.alert_rule = m.get('AlertRule')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SearchEventsResponseBodyPageBean(TeaModel):
    def __init__(self, event=None, page_number=None, page_size=None, total_count=None):
        self.event = event  # type: list[SearchEventsResponseBodyPageBeanEvent]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.event:
            for k in self.event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchEventsResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Event'] = []
        if self.event is not None:
            for k in self.event:
                result['Event'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event = []
        if m.get('Event') is not None:
            for k in m.get('Event'):
                temp_model = SearchEventsResponseBodyPageBeanEvent()
                self.event.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchEventsResponseBody(TeaModel):
    def __init__(self, is_trigger=None, page_bean=None, request_id=None):
        self.is_trigger = is_trigger  # type: int
        self.page_bean = page_bean  # type: SearchEventsResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_trigger is not None:
            result['IsTrigger'] = self.is_trigger
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsTrigger') is not None:
            self.is_trigger = m.get('IsTrigger')
        if m.get('PageBean') is not None:
            temp_model = SearchEventsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchEventsResponse, self).to_map()
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
            temp_model = SearchEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchRetcodeAppByPageRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None, retcode_app_name=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.retcode_app_name = retcode_app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchRetcodeAppByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retcode_app_name is not None:
            result['RetcodeAppName'] = self.retcode_app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetcodeAppName') is not None:
            self.retcode_app_name = m.get('RetcodeAppName')
        return self


class SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, pid=None, region_id=None, retcode_app_type=None,
                 type=None, update_time=None, user_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.retcode_app_type = retcode_app_type  # type: str
        self.type = type  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchRetcodeAppByPageResponseBodyPageBean(TeaModel):
    def __init__(self, page_number=None, page_size=None, retcode_apps=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.retcode_apps = retcode_apps  # type: list[SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.retcode_apps:
            for k in self.retcode_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchRetcodeAppByPageResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['RetcodeApps'] = []
        if self.retcode_apps is not None:
            for k in self.retcode_apps:
                result['RetcodeApps'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.retcode_apps = []
        if m.get('RetcodeApps') is not None:
            for k in m.get('RetcodeApps'):
                temp_model = SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps()
                self.retcode_apps.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchRetcodeAppByPageResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchRetcodeAppByPageResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchRetcodeAppByPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchRetcodeAppByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchRetcodeAppByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchRetcodeAppByPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchRetcodeAppByPageResponse, self).to_map()
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
            temp_model = SearchRetcodeAppByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTraceAppByNameRequest(TeaModel):
    def __init__(self, region_id=None, trace_app_name=None):
        self.region_id = region_id  # type: str
        self.trace_app_name = trace_app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTraceAppByNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_app_name is not None:
            result['TraceAppName'] = self.trace_app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceAppName') is not None:
            self.trace_app_name = m.get('TraceAppName')
        return self


class SearchTraceAppByNameResponseBodyTraceApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, labels=None, pid=None, region_id=None, show=None,
                 type=None, update_time=None, user_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.labels = labels  # type: list[str]
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.show = show  # type: bool
        self.type = type  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTraceAppByNameResponseBodyTraceApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchTraceAppByNameResponseBody(TeaModel):
    def __init__(self, request_id=None, trace_apps=None):
        self.request_id = request_id  # type: str
        self.trace_apps = trace_apps  # type: list[SearchTraceAppByNameResponseBodyTraceApps]

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTraceAppByNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = SearchTraceAppByNameResponseBodyTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        return self


class SearchTraceAppByNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchTraceAppByNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTraceAppByNameResponse, self).to_map()
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
            temp_model = SearchTraceAppByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTraceAppByPageRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None, trace_app_name=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.trace_app_name = trace_app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTraceAppByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_app_name is not None:
            result['TraceAppName'] = self.trace_app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceAppName') is not None:
            self.trace_app_name = m.get('TraceAppName')
        return self


class SearchTraceAppByPageResponseBodyPageBeanTraceApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, labels=None, pid=None, region_id=None, show=None,
                 type=None, update_time=None, user_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.labels = labels  # type: list[str]
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.show = show  # type: bool
        self.type = type  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTraceAppByPageResponseBodyPageBeanTraceApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchTraceAppByPageResponseBodyPageBean(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, trace_apps=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.trace_apps = trace_apps  # type: list[SearchTraceAppByPageResponseBodyPageBeanTraceApps]

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTraceAppByPageResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = SearchTraceAppByPageResponseBodyPageBeanTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        return self


class SearchTraceAppByPageResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchTraceAppByPageResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchTraceAppByPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchTraceAppByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTraceAppByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchTraceAppByPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTraceAppByPageResponse, self).to_map()
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
            temp_model = SearchTraceAppByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesRequestExclusionFilters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesRequestExclusionFilters, self).to_map()
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


class SearchTracesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesRequestTag, self).to_map()
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


class SearchTracesRequest(TeaModel):
    def __init__(self, end_time=None, exclusion_filters=None, min_duration=None, operation_name=None, pid=None,
                 region_id=None, reverse=None, service_ip=None, service_name=None, start_time=None, tag=None):
        self.end_time = end_time  # type: long
        self.exclusion_filters = exclusion_filters  # type: list[SearchTracesRequestExclusionFilters]
        self.min_duration = min_duration  # type: long
        self.operation_name = operation_name  # type: str
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.reverse = reverse  # type: bool
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.start_time = start_time  # type: long
        self.tag = tag  # type: list[SearchTracesRequestTag]

    def validate(self):
        if self.exclusion_filters:
            for k in self.exclusion_filters:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTracesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['ExclusionFilters'] = []
        if self.exclusion_filters is not None:
            for k in self.exclusion_filters:
                result['ExclusionFilters'].append(k.to_map() if k else None)
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.exclusion_filters = []
        if m.get('ExclusionFilters') is not None:
            for k in m.get('ExclusionFilters'):
                temp_model = SearchTracesRequestExclusionFilters()
                self.exclusion_filters.append(temp_model.from_map(k))
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = SearchTracesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class SearchTracesResponseBodyTraceInfos(TeaModel):
    def __init__(self, duration=None, operation_name=None, service_ip=None, service_name=None, timestamp=None,
                 trace_id=None):
        self.duration = duration  # type: long
        self.operation_name = operation_name  # type: str
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.timestamp = timestamp  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesResponseBodyTraceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesResponseBody(TeaModel):
    def __init__(self, request_id=None, trace_infos=None):
        self.request_id = request_id  # type: str
        self.trace_infos = trace_infos  # type: list[SearchTracesResponseBodyTraceInfos]

    def validate(self):
        if self.trace_infos:
            for k in self.trace_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTracesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TraceInfos'] = []
        if self.trace_infos is not None:
            for k in self.trace_infos:
                result['TraceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trace_infos = []
        if m.get('TraceInfos') is not None:
            for k in m.get('TraceInfos'):
                temp_model = SearchTracesResponseBodyTraceInfos()
                self.trace_infos.append(temp_model.from_map(k))
        return self


class SearchTracesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchTracesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTracesResponse, self).to_map()
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
            temp_model = SearchTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesByPageRequestExclusionFilters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesByPageRequestExclusionFilters, self).to_map()
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


class SearchTracesByPageRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesByPageRequestTags, self).to_map()
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


class SearchTracesByPageRequest(TeaModel):
    def __init__(self, end_time=None, exclusion_filters=None, min_duration=None, operation_name=None,
                 page_number=None, page_size=None, pid=None, region_id=None, reverse=None, service_ip=None, service_name=None,
                 start_time=None, tags=None):
        self.end_time = end_time  # type: long
        self.exclusion_filters = exclusion_filters  # type: list[SearchTracesByPageRequestExclusionFilters]
        self.min_duration = min_duration  # type: long
        self.operation_name = operation_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.reverse = reverse  # type: bool
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.start_time = start_time  # type: long
        self.tags = tags  # type: list[SearchTracesByPageRequestTags]

    def validate(self):
        if self.exclusion_filters:
            for k in self.exclusion_filters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTracesByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['ExclusionFilters'] = []
        if self.exclusion_filters is not None:
            for k in self.exclusion_filters:
                result['ExclusionFilters'].append(k.to_map() if k else None)
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.exclusion_filters = []
        if m.get('ExclusionFilters') is not None:
            for k in m.get('ExclusionFilters'):
                temp_model = SearchTracesByPageRequestExclusionFilters()
                self.exclusion_filters.append(temp_model.from_map(k))
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = SearchTracesByPageRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class SearchTracesByPageResponseBodyPageBeanTraceInfos(TeaModel):
    def __init__(self, duration=None, operation_name=None, service_ip=None, service_name=None, timestamp=None,
                 trace_id=None):
        self.duration = duration  # type: long
        self.operation_name = operation_name  # type: str
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.timestamp = timestamp  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesByPageResponseBodyPageBeanTraceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesByPageResponseBodyPageBean(TeaModel):
    def __init__(self, page_number=None, page_size=None, total=None, trace_infos=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.trace_infos = trace_infos  # type: list[SearchTracesByPageResponseBodyPageBeanTraceInfos]

    def validate(self):
        if self.trace_infos:
            for k in self.trace_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTracesByPageResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['TraceInfos'] = []
        if self.trace_infos is not None:
            for k in self.trace_infos:
                result['TraceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.trace_infos = []
        if m.get('TraceInfos') is not None:
            for k in m.get('TraceInfos'):
                temp_model = SearchTracesByPageResponseBodyPageBeanTraceInfos()
                self.trace_infos.append(temp_model.from_map(k))
        return self


class SearchTracesByPageResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchTracesByPageResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchTracesByPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchTracesByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTracesByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchTracesByPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTracesByPageResponse, self).to_map()
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
            temp_model = SearchTracesByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTTSVerifyLinkRequest(TeaModel):
    def __init__(self, contact_id=None, phone=None):
        self.contact_id = contact_id  # type: long
        self.phone = phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTTSVerifyLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class SendTTSVerifyLinkResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTTSVerifyLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendTTSVerifyLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendTTSVerifyLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendTTSVerifyLinkResponse, self).to_map()
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
            temp_model = SendTTSVerifyLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRetcodeShareStatusRequest(TeaModel):
    def __init__(self, pid=None, status=None):
        self.pid = pid  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRetcodeShareStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetRetcodeShareStatusResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRetcodeShareStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetRetcodeShareStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetRetcodeShareStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetRetcodeShareStatusResponse, self).to_map()
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
            temp_model = SetRetcodeShareStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAlertRequest(TeaModel):
    def __init__(self, alert_id=None, region_id=None):
        self.alert_id = alert_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartAlertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartAlertResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartAlertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartAlertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartAlertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartAlertResponse, self).to_map()
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
            temp_model = StartAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAlertRequest(TeaModel):
    def __init__(self, alert_id=None, region_id=None):
        self.alert_id = alert_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAlertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopAlertResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAlertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAlertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopAlertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopAlertResponse, self).to_map()
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
            temp_model = StopAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchSyntheticTaskStatusRequest(TeaModel):
    def __init__(self, switch_status=None, task_ids=None):
        self.switch_status = switch_status  # type: long
        self.task_ids = task_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchSyntheticTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class SwitchSyntheticTaskStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchSyntheticTaskStatusResponseBody, self).to_map()
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


class SwitchSyntheticTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchSyntheticTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchSyntheticTaskStatusResponse, self).to_map()
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
            temp_model = SwitchSyntheticTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncRecordingRulesRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None, target_clusters=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str
        self.target_clusters = target_clusters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncRecordingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.target_clusters is not None:
            result['TargetClusters'] = self.target_clusters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TargetClusters') is not None:
            self.target_clusters = m.get('TargetClusters')
        return self


class SyncRecordingRulesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncRecordingRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SyncRecordingRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SyncRecordingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncRecordingRulesResponse, self).to_map()
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
            temp_model = SyncRecordingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TurnOnSecondSwitchRequest(TeaModel):
    def __init__(self, pid=None, proxy_user_id=None, release_start_time=None):
        self.pid = pid  # type: str
        self.proxy_user_id = proxy_user_id  # type: str
        self.release_start_time = release_start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TurnOnSecondSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.release_start_time is not None:
            result['ReleaseStartTime'] = self.release_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ReleaseStartTime') is not None:
            self.release_start_time = m.get('ReleaseStartTime')
        return self


class TurnOnSecondSwitchResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TurnOnSecondSwitchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TurnOnSecondSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TurnOnSecondSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TurnOnSecondSwitchResponse, self).to_map()
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
            temp_model = TurnOnSecondSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallManagedPrometheusRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, region_id=None, vpc_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_type = cluster_type  # type: str
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallManagedPrometheusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UninstallManagedPrometheusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallManagedPrometheusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UninstallManagedPrometheusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UninstallManagedPrometheusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UninstallManagedPrometheusResponse, self).to_map()
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
            temp_model = UninstallManagedPrometheusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallPromClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallPromClusterRequest, self).to_map()
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


class UninstallPromClusterResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallPromClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UninstallPromClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UninstallPromClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UninstallPromClusterResponse, self).to_map()
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
            temp_model = UninstallPromClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertContactRequest(TeaModel):
    def __init__(self, contact_id=None, contact_name=None, ding_robot_webhook_url=None, email=None, phone_num=None,
                 region_id=None, system_noc=None):
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.ding_robot_webhook_url = ding_robot_webhook_url  # type: str
        self.email = email  # type: str
        self.phone_num = phone_num  # type: str
        self.region_id = region_id  # type: str
        self.system_noc = system_noc  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.ding_robot_webhook_url is not None:
            result['DingRobotWebhookUrl'] = self.ding_robot_webhook_url
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('DingRobotWebhookUrl') is not None:
            self.ding_robot_webhook_url = m.get('DingRobotWebhookUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        return self


class UpdateAlertContactResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlertContactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlertContactResponse, self).to_map()
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
            temp_model = UpdateAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertContactGroupRequest(TeaModel):
    def __init__(self, contact_group_id=None, contact_group_name=None, contact_ids=None, region_id=None):
        self.contact_group_id = contact_group_id  # type: long
        self.contact_group_name = contact_group_name  # type: str
        self.contact_ids = contact_ids  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertContactGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAlertContactGroupResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertContactGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertContactGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlertContactGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlertContactGroupResponse, self).to_map()
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
            temp_model = UpdateAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertRuleRequest(TeaModel):
    def __init__(self, alert_id=None, contact_group_ids=None, is_auto_start=None, region_id=None,
                 templage_alert_config=None):
        self.alert_id = alert_id  # type: long
        self.contact_group_ids = contact_group_ids  # type: str
        self.is_auto_start = is_auto_start  # type: bool
        self.region_id = region_id  # type: str
        self.templage_alert_config = templage_alert_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')
        return self


class UpdateAlertRuleResponseBody(TeaModel):
    def __init__(self, alert_id=None, data=None, request_id=None):
        self.alert_id = alert_id  # type: long
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlertRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlertRuleResponse, self).to_map()
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
            temp_model = UpdateAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDispatchRuleRequest(TeaModel):
    def __init__(self, dispatch_rule=None, region_id=None):
        self.dispatch_rule = dispatch_rule  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDispatchRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            self.dispatch_rule = m.get('DispatchRule')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateDispatchRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDispatchRuleResponseBody, self).to_map()
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


class UpdateDispatchRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDispatchRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDispatchRuleResponse, self).to_map()
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
            temp_model = UpdateDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIntegrationRequest(TeaModel):
    def __init__(self, api_endpoint=None, auto_recover=None, description=None, duplicate_key=None,
                 extended_field_redefine_rules=None, field_redefine_rules=None, initiative_recover_field=None, initiative_recover_value=None,
                 integration_id=None, integration_name=None, integration_product_type=None, liveness=None, recover_time=None,
                 short_token=None, stat=None, state=None):
        self.api_endpoint = api_endpoint  # type: str
        self.auto_recover = auto_recover  # type: bool
        self.description = description  # type: str
        self.duplicate_key = duplicate_key  # type: str
        self.extended_field_redefine_rules = extended_field_redefine_rules  # type: str
        self.field_redefine_rules = field_redefine_rules  # type: str
        self.initiative_recover_field = initiative_recover_field  # type: str
        self.initiative_recover_value = initiative_recover_value  # type: str
        self.integration_id = integration_id  # type: long
        self.integration_name = integration_name  # type: str
        self.integration_product_type = integration_product_type  # type: str
        self.liveness = liveness  # type: str
        self.recover_time = recover_time  # type: long
        self.short_token = short_token  # type: str
        self.stat = stat  # type: str
        self.state = state  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIntegrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_endpoint is not None:
            result['ApiEndpoint'] = self.api_endpoint
        if self.auto_recover is not None:
            result['AutoRecover'] = self.auto_recover
        if self.description is not None:
            result['Description'] = self.description
        if self.duplicate_key is not None:
            result['DuplicateKey'] = self.duplicate_key
        if self.extended_field_redefine_rules is not None:
            result['ExtendedFieldRedefineRules'] = self.extended_field_redefine_rules
        if self.field_redefine_rules is not None:
            result['FieldRedefineRules'] = self.field_redefine_rules
        if self.initiative_recover_field is not None:
            result['InitiativeRecoverField'] = self.initiative_recover_field
        if self.initiative_recover_value is not None:
            result['InitiativeRecoverValue'] = self.initiative_recover_value
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_product_type is not None:
            result['IntegrationProductType'] = self.integration_product_type
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.recover_time is not None:
            result['RecoverTime'] = self.recover_time
        if self.short_token is not None:
            result['ShortToken'] = self.short_token
        if self.stat is not None:
            result['Stat'] = self.stat
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiEndpoint') is not None:
            self.api_endpoint = m.get('ApiEndpoint')
        if m.get('AutoRecover') is not None:
            self.auto_recover = m.get('AutoRecover')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DuplicateKey') is not None:
            self.duplicate_key = m.get('DuplicateKey')
        if m.get('ExtendedFieldRedefineRules') is not None:
            self.extended_field_redefine_rules = m.get('ExtendedFieldRedefineRules')
        if m.get('FieldRedefineRules') is not None:
            self.field_redefine_rules = m.get('FieldRedefineRules')
        if m.get('InitiativeRecoverField') is not None:
            self.initiative_recover_field = m.get('InitiativeRecoverField')
        if m.get('InitiativeRecoverValue') is not None:
            self.initiative_recover_value = m.get('InitiativeRecoverValue')
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationProductType') is not None:
            self.integration_product_type = m.get('IntegrationProductType')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('RecoverTime') is not None:
            self.recover_time = m.get('RecoverTime')
        if m.get('ShortToken') is not None:
            self.short_token = m.get('ShortToken')
        if m.get('Stat') is not None:
            self.stat = m.get('Stat')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class UpdateIntegrationResponseBodyIntegration(TeaModel):
    def __init__(self, api_endpoint=None, auto_recover=None, description=None, duplicate_key=None,
                 extended_field_redefine_rules=None, field_redefine_rules=None, initiative_recover_field=None, initiative_recover_value=None,
                 integration_id=None, integration_name=None, integration_product_type=None, liveness=None, recover_time=None,
                 short_token=None, stat=None, state=None):
        self.api_endpoint = api_endpoint  # type: str
        self.auto_recover = auto_recover  # type: bool
        self.description = description  # type: str
        self.duplicate_key = duplicate_key  # type: str
        self.extended_field_redefine_rules = extended_field_redefine_rules  # type: list[dict[str, any]]
        self.field_redefine_rules = field_redefine_rules  # type: list[dict[str, any]]
        self.initiative_recover_field = initiative_recover_field  # type: str
        self.initiative_recover_value = initiative_recover_value  # type: str
        self.integration_id = integration_id  # type: long
        self.integration_name = integration_name  # type: str
        self.integration_product_type = integration_product_type  # type: str
        self.liveness = liveness  # type: str
        self.recover_time = recover_time  # type: long
        self.short_token = short_token  # type: str
        self.stat = stat  # type: list[long]
        self.state = state  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIntegrationResponseBodyIntegration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_endpoint is not None:
            result['ApiEndpoint'] = self.api_endpoint
        if self.auto_recover is not None:
            result['AutoRecover'] = self.auto_recover
        if self.description is not None:
            result['Description'] = self.description
        if self.duplicate_key is not None:
            result['DuplicateKey'] = self.duplicate_key
        if self.extended_field_redefine_rules is not None:
            result['ExtendedFieldRedefineRules'] = self.extended_field_redefine_rules
        if self.field_redefine_rules is not None:
            result['FieldRedefineRules'] = self.field_redefine_rules
        if self.initiative_recover_field is not None:
            result['InitiativeRecoverField'] = self.initiative_recover_field
        if self.initiative_recover_value is not None:
            result['InitiativeRecoverValue'] = self.initiative_recover_value
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_product_type is not None:
            result['IntegrationProductType'] = self.integration_product_type
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.recover_time is not None:
            result['RecoverTime'] = self.recover_time
        if self.short_token is not None:
            result['ShortToken'] = self.short_token
        if self.stat is not None:
            result['Stat'] = self.stat
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiEndpoint') is not None:
            self.api_endpoint = m.get('ApiEndpoint')
        if m.get('AutoRecover') is not None:
            self.auto_recover = m.get('AutoRecover')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DuplicateKey') is not None:
            self.duplicate_key = m.get('DuplicateKey')
        if m.get('ExtendedFieldRedefineRules') is not None:
            self.extended_field_redefine_rules = m.get('ExtendedFieldRedefineRules')
        if m.get('FieldRedefineRules') is not None:
            self.field_redefine_rules = m.get('FieldRedefineRules')
        if m.get('InitiativeRecoverField') is not None:
            self.initiative_recover_field = m.get('InitiativeRecoverField')
        if m.get('InitiativeRecoverValue') is not None:
            self.initiative_recover_value = m.get('InitiativeRecoverValue')
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationProductType') is not None:
            self.integration_product_type = m.get('IntegrationProductType')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('RecoverTime') is not None:
            self.recover_time = m.get('RecoverTime')
        if m.get('ShortToken') is not None:
            self.short_token = m.get('ShortToken')
        if m.get('Stat') is not None:
            self.stat = m.get('Stat')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class UpdateIntegrationResponseBody(TeaModel):
    def __init__(self, integration=None, request_id=None):
        self.integration = integration  # type: UpdateIntegrationResponseBodyIntegration
        self.request_id = request_id  # type: str

    def validate(self):
        if self.integration:
            self.integration.validate()

    def to_map(self):
        _map = super(UpdateIntegrationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.integration is not None:
            result['Integration'] = self.integration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Integration') is not None:
            temp_model = UpdateIntegrationResponseBodyIntegration()
            self.integration = temp_model.from_map(m['Integration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateIntegrationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateIntegrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIntegrationResponse, self).to_map()
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
            temp_model = UpdateIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrometheusAlertRuleRequest(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None,
                 duration=None, expression=None, labels=None, message=None, notify_type=None, region_id=None, type=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: str
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: str
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None,
                 duration=None, expression=None, labels=None, message=None, notify_type=None, status=None, type=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: list[UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations]
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: list[UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels]
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.status = status  # type: int
        self.type = type  # type: str

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdatePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(self, prometheus_alert_rule=None, request_id=None):
        self.prometheus_alert_rule = prometheus_alert_rule  # type: UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prometheus_alert_rule:
            self.prometheus_alert_rule.validate()

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus_alert_rule is not None:
            result['PrometheusAlertRule'] = self.prometheus_alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrometheusAlertRule') is not None:
            temp_model = UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule()
            self.prometheus_alert_rule = temp_model.from_map(m['PrometheusAlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePrometheusAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePrometheusAlertRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleResponse, self).to_map()
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
            temp_model = UpdatePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebhookRequest(TeaModel):
    def __init__(self, body=None, contact_id=None, contact_name=None, http_headers=None, http_params=None,
                 method=None, recover_body=None, region_id=None, url=None):
        self.body = body  # type: str
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.http_headers = http_headers  # type: str
        self.http_params = http_params  # type: str
        self.method = method  # type: str
        self.recover_body = recover_body  # type: str
        self.region_id = region_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.http_headers is not None:
            result['HttpHeaders'] = self.http_headers
        if self.http_params is not None:
            result['HttpParams'] = self.http_params
        if self.method is not None:
            result['Method'] = self.method
        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('HttpHeaders') is not None:
            self.http_headers = m.get('HttpHeaders')
        if m.get('HttpParams') is not None:
            self.http_params = m.get('HttpParams')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateWebhookResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWebhookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWebhookResponse, self).to_map()
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
            temp_model = UpdateWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadRequest(TeaModel):
    def __init__(self, edition=None, file=None, file_name=None, pid=None, region_id=None, version=None):
        self.edition = edition  # type: str
        self.file = file  # type: str
        self.file_name = file_name  # type: str
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.file is not None:
            result['File'] = self.file
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('File') is not None:
            self.file = m.get('File')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UploadResponseBodyUploadResult(TeaModel):
    def __init__(self, fid=None, file_name=None, upload_time=None):
        self.fid = fid  # type: str
        self.file_name = file_name  # type: str
        self.upload_time = upload_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadResponseBodyUploadResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fid is not None:
            result['Fid'] = self.fid
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fid') is not None:
            self.fid = m.get('Fid')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        return self


class UploadResponseBody(TeaModel):
    def __init__(self, request_id=None, upload_result=None):
        self.request_id = request_id  # type: str
        self.upload_result = upload_result  # type: UploadResponseBodyUploadResult

    def validate(self):
        if self.upload_result:
            self.upload_result.validate()

    def to_map(self):
        _map = super(UploadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_result is not None:
            result['UploadResult'] = self.upload_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadResult') is not None:
            temp_model = UploadResponseBodyUploadResult()
            self.upload_result = temp_model.from_map(m['UploadResult'])
        return self


class UploadResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadResponse, self).to_map()
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
            temp_model = UploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


