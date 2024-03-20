# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ErrorResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ErrorResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class VariablesValueFuncValue(TeaModel):
    def __init__(self, func_class_name=None, template=None):
        # The class name.
        self.func_class_name = func_class_name  # type: str
        # The template of the variable.
        self.template = template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VariablesValueFuncValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.func_class_name is not None:
            result['funcClassName'] = self.func_class_name
        if self.template is not None:
            result['template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('funcClassName') is not None:
            self.func_class_name = m.get('funcClassName')
        if m.get('template') is not None:
            self.template = m.get('template')
        return self


class VariablesValue(TeaModel):
    def __init__(self, disable_modify=None, is_modify=None, value=None, description=None, template_value=None,
                 type=None, func_value=None):
        # Specifies whether the variable cannot be modified.
        self.disable_modify = disable_modify  # type: bool
        # Specifies whether the variable is modified.
        self.is_modify = is_modify  # type: bool
        # The value of the variable.
        self.value = value  # type: str
        # The description about the variable.
        self.description = description  # type: str
        # The value of the template.
        self.template_value = template_value  # type: str
        # The type of the variable. Valid values:
        # 
        # *   NORMAL: a normal variable
        # *   FUNCTION: a function variable
        self.type = type  # type: str
        # The function variable.
        self.func_value = func_value  # type: VariablesValueFuncValue

    def validate(self):
        if self.func_value:
            self.func_value.validate()

    def to_map(self):
        _map = super(VariablesValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_modify is not None:
            result['disableModify'] = self.disable_modify
        if self.is_modify is not None:
            result['isModify'] = self.is_modify
        if self.value is not None:
            result['value'] = self.value
        if self.description is not None:
            result['description'] = self.description
        if self.template_value is not None:
            result['templateValue'] = self.template_value
        if self.type is not None:
            result['type'] = self.type
        if self.func_value is not None:
            result['funcValue'] = self.func_value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('disableModify') is not None:
            self.disable_modify = m.get('disableModify')
        if m.get('isModify') is not None:
            self.is_modify = m.get('isModify')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('templateValue') is not None:
            self.template_value = m.get('templateValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('funcValue') is not None:
            temp_model = VariablesValueFuncValue()
            self.func_value = temp_model.from_map(m['funcValue'])
        return self


class BuildIndexRequest(TeaModel):
    def __init__(self, build_mode=None, data_source_name=None, data_source_type=None, data_time_sec=None,
                 domain=None, generation=None, partition=None):
        # The reindexing mode.
        self.build_mode = build_mode  # type: str
        # The name of the data source.
        self.data_source_name = data_source_name  # type: str
        # The type of the data source.
        self.data_source_type = data_source_type  # type: str
        # The timestamp in seconds. It is of the INT type. This parameter is required for the API-pushed data source.
        self.data_time_sec = data_time_sec  # type: int
        # The data center where the data source is deployed.
        self.domain = domain  # type: str
        # The data restoration version.
        self.generation = generation  # type: long
        # This parameter is required for the odps data source.
        self.partition = partition  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BuildIndexRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_mode is not None:
            result['buildMode'] = self.build_mode
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.domain is not None:
            result['domain'] = self.domain
        if self.generation is not None:
            result['generation'] = self.generation
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('buildMode') is not None:
            self.build_mode = m.get('buildMode')
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class BuildIndexResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The list of clusters
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BuildIndexResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class BuildIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BuildIndexResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BuildIndexResponse, self).to_map()
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
            temp_model = BuildIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequestDataNode(TeaModel):
    def __init__(self, number=None):
        # The number of data nodes
        self.number = number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestDataNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class CreateClusterRequestQueryNode(TeaModel):
    def __init__(self, number=None):
        # The number of nodes to query
        self.number = number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestQueryNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, auto_load=None, data_node=None, description=None, name=None, query_node=None):
        # The remarks of the query node
        self.auto_load = auto_load  # type: bool
        # The description of the data node
        self.data_node = data_node  # type: CreateClusterRequestDataNode
        # The description of the cluster
        self.description = description  # type: str
        # The name of the node
        self.name = name  # type: str
        # The description of the query node
        self.query_node = query_node  # type: CreateClusterRequestQueryNode

    def validate(self):
        if self.data_node:
            self.data_node.validate()
        if self.query_node:
            self.query_node.validate()

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_load is not None:
            result['autoLoad'] = self.auto_load
        if self.data_node is not None:
            result['dataNode'] = self.data_node.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.query_node is not None:
            result['queryNode'] = self.query_node.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoLoad') is not None:
            self.auto_load = m.get('autoLoad')
        if m.get('dataNode') is not None:
            temp_model = CreateClusterRequestDataNode()
            self.data_node = temp_model.from_map(m['dataNode'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('queryNode') is not None:
            temp_model = CreateClusterRequestQueryNode()
            self.query_node = temp_model.from_map(m['queryNode'])
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The result returned
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterResponse, self).to_map()
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSourceRequestConfig(TeaModel):
    def __init__(self, access_key=None, access_secret=None, bucket=None, endpoint=None, namespace=None,
                 oss_path=None, partition=None, path=None, project=None, table=None):
        self.access_key = access_key  # type: str
        self.access_secret = access_secret  # type: str
        self.bucket = bucket  # type: str
        self.endpoint = endpoint  # type: str
        self.namespace = namespace  # type: str
        self.oss_path = oss_path  # type: str
        self.partition = partition  # type: str
        self.path = path  # type: str
        self.project = project  # type: str
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataSourceRequestConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class CreateDataSourceRequestSaroConfig(TeaModel):
    def __init__(self, namespace=None, table_name=None):
        self.namespace = namespace  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataSourceRequestSaroConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class CreateDataSourceRequest(TeaModel):
    def __init__(self, auto_build_index=None, config=None, domain=None, name=None, saro_config=None, type=None,
                 dry_run=None):
        self.auto_build_index = auto_build_index  # type: bool
        self.config = config  # type: CreateDataSourceRequestConfig
        self.domain = domain  # type: str
        self.name = name  # type: str
        self.saro_config = saro_config  # type: CreateDataSourceRequestSaroConfig
        self.type = type  # type: str
        # Specifies whether to perform a dry run. This parameter is only used to check whether the data source is valid. Valid values: true and false.
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.config:
            self.config.validate()
        if self.saro_config:
            self.saro_config.validate()

    def to_map(self):
        _map = super(CreateDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.name is not None:
            result['name'] = self.name
        if self.saro_config is not None:
            result['saroConfig'] = self.saro_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = CreateDataSourceRequestConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('saroConfig') is not None:
            temp_model = CreateDataSourceRequestSaroConfig()
            self.saro_config = temp_model.from_map(m['saroConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateDataSourceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The returned results.
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateDataSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDataSourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataSourceResponse, self).to_map()
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
            temp_model = CreateDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIndexRequestDataSourceInfoConfig(TeaModel):
    def __init__(self, access_key=None, access_secret=None, bucket=None, endpoint=None, namespace=None,
                 oss_path=None, partition=None, path=None, project=None, table=None):
        # odps数据源ak
        self.access_key = access_key  # type: str
        # odps数据源ak secret
        self.access_secret = access_secret  # type: str
        self.bucket = bucket  # type: str
        # odps数据源的endpoint, oss数据源的endpoint
        self.endpoint = endpoint  # type: str
        self.namespace = namespace  # type: str
        self.oss_path = oss_path  # type: str
        # 数据源为odps时必填
        self.partition = partition  # type: str
        self.path = path  # type: str
        # odps数据源项目名称
        self.project = project  # type: str
        # 表名称
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIndexRequestDataSourceInfoConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class CreateIndexRequestDataSourceInfoSaroConfig(TeaModel):
    def __init__(self, namespace=None, table_name=None):
        self.namespace = namespace  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIndexRequestDataSourceInfoSaroConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class CreateIndexRequestDataSourceInfo(TeaModel):
    def __init__(self, auto_build_index=None, config=None, data_time_sec=None, domain=None, name=None,
                 process_partition_count=None, saro_config=None, type=None):
        # 是否开启自动全量
        self.auto_build_index = auto_build_index  # type: bool
        # odps相关
        self.config = config  # type: CreateIndexRequestDataSourceInfoConfig
        self.data_time_sec = data_time_sec  # type: int
        self.domain = domain  # type: str
        self.name = name  # type: str
        # 数据更新资源数
        self.process_partition_count = process_partition_count  # type: int
        self.saro_config = saro_config  # type: CreateIndexRequestDataSourceInfoSaroConfig
        # 数据源类型
        # odps
        # swift
        # saro
        # oss
        self.type = type  # type: str

    def validate(self):
        if self.config:
            self.config.validate()
        if self.saro_config:
            self.saro_config.validate()

    def to_map(self):
        _map = super(CreateIndexRequestDataSourceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.domain is not None:
            result['domain'] = self.domain
        if self.name is not None:
            result['name'] = self.name
        if self.process_partition_count is not None:
            result['processPartitionCount'] = self.process_partition_count
        if self.saro_config is not None:
            result['saroConfig'] = self.saro_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = CreateIndexRequestDataSourceInfoConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processPartitionCount') is not None:
            self.process_partition_count = m.get('processPartitionCount')
        if m.get('saroConfig') is not None:
            temp_model = CreateIndexRequestDataSourceInfoSaroConfig()
            self.saro_config = temp_model.from_map(m['saroConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateIndexRequest(TeaModel):
    def __init__(self, content=None, data_source=None, data_source_info=None, domain=None, extend=None, name=None,
                 partition=None, dry_run=None):
        # The content of the index.
        self.content = content  # type: str
        # The data source type. Valid values: odps, mns, flink, and streaming. This parameter can be ignored.
        self.data_source = data_source  # type: str
        # 数据源相关信息 （向量检索版新版本必填）
        self.data_source_info = data_source_info  # type: CreateIndexRequestDataSourceInfo
        # The data center where the data source is deployed.
        self.domain = domain  # type: str
        # 字段配置的扩展的内容
        # key: 向量字段(vector)、
        # 需embeding字段(embeding)
        self.extend = extend  # type: dict[str, any]
        # The name of the index.
        self.name = name  # type: str
        # The data partition.
        self.partition = partition  # type: int
        # 是否dryRun创建（仅校验数据源是否合法）。取值：-true 是 -false 否
        self.dry_run = dry_run  # type: bool

    def validate(self):
        if self.data_source_info:
            self.data_source_info.validate()

    def to_map(self):
        _map = super(CreateIndexRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.data_source_info is not None:
            result['dataSourceInfo'] = self.data_source_info.to_map()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.extend is not None:
            result['extend'] = self.extend
        if self.name is not None:
            result['name'] = self.name
        if self.partition is not None:
            result['partition'] = self.partition
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('dataSourceInfo') is not None:
            temp_model = CreateIndexRequestDataSourceInfo()
            self.data_source_info = temp_model.from_map(m['dataSourceInfo'])
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateIndexResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The information about the index
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIndexResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIndexResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIndexResponse, self).to_map()
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
            temp_model = CreateIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestComponents(TeaModel):
    def __init__(self, code=None, value=None):
        # The specification code, which must be consistent with values of the corresponding module parameters.
        self.code = code  # type: str
        # Values that you specify for the corresponding module components on the buy page.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateInstanceRequestOrder(TeaModel):
    def __init__(self, auto_renew=None, duration=None, pricing_cycle=None):
        # Specifies whether to enable auto-renewal. Valid values: true and false.
        self.auto_renew = auto_renew  # type: bool
        # The billing duration. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, and 12.
        self.duration = duration  # type: long
        # The unit of the billing duration. Valid values: Month and Year.
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.duration is not None:
            result['duration'] = self.duration
        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, charge_type=None, components=None, order=None):
        # The billing method of the instance. Valid values: PREPAY and POSTPAY. PREPAY indicates the instance is a subscription instance. When you set this parameter to PREPAY, make sure that your Alibaba Cloud account supports balance payment or credit card payment. Otherwise, the system returns the InvalidPayMethod error message. If you set this parameter to PREPAY, you must also specify the paymentInfo parameter. POSTPAY indicates that the instance is a pay-as-you-go instance. This billing method is not supported.
        self.charge_type = charge_type  # type: str
        # A list of instance-related specifications.
        self.components = components  # type: list[CreateInstanceRequestComponents]
        # The billing information.
        self.order = order  # type: CreateInstanceRequestOrder

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()
        if self.order:
            self.order.validate()

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        result['components'] = []
        if self.components is not None:
            for k in self.components:
                result['components'].append(k.to_map() if k else None)
        if self.order is not None:
            result['order'] = self.order.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        self.components = []
        if m.get('components') is not None:
            for k in m.get('components'):
                temp_model = CreateInstanceRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('order') is not None:
            temp_model = CreateInstanceRequestOrder()
            self.order = temp_model.from_map(m['order'])
        return self


class CreateInstanceResponseBodyResult(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the instance
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
        # The ID of the request
        self.request_id = request_id  # type: str
        # The result returned
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
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
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


class DeleteAdvanceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result.
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAdvanceConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteAdvanceConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAdvanceConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAdvanceConfigResponse, self).to_map()
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
            temp_model = DeleteAdvanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request
        self.request_id = request_id  # type: str
        # The result returned
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteDataSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDataSourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataSourceResponse, self).to_map()
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
            temp_model = DeleteDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIndexRequest(TeaModel):
    def __init__(self, data_source=None, delete_data_source=None):
        # The data source
        self.data_source = data_source  # type: str
        self.delete_data_source = delete_data_source  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIndexRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.delete_data_source is not None:
            result['deleteDataSource'] = self.delete_data_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('deleteDataSource') is not None:
            self.delete_data_source = m.get('deleteDataSource')
        return self


class DeleteIndexResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The information about the index
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIndexResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIndexResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIndexResponse, self).to_map()
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
            temp_model = DeleteIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIndexVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The result
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIndexVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteIndexVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIndexVersionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIndexVersionResponse, self).to_map()
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
            temp_model = DeleteIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request
        self.request_id = request_id  # type: str
        # The result returned
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
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


class ForceSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The information about the index
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForceSwitchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ForceSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ForceSwitchResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ForceSwitchResponse, self).to_map()
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
            temp_model = ForceSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAdvanceConfigRequest(TeaModel):
    def __init__(self, type=None):
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAdvanceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetAdvanceConfigResponseBodyResultFiles(TeaModel):
    def __init__(self, full_path_name=None, is_dir=None, is_template=None, name=None):
        # The name of the file path.
        self.full_path_name = full_path_name  # type: str
        # Indicates whether it is a directory.
        self.is_dir = is_dir  # type: bool
        # Indicates whether it is a template.
        self.is_template = is_template  # type: bool
        # The name.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAdvanceConfigResponseBodyResultFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetAdvanceConfigResponseBodyResult(TeaModel):
    def __init__(self, content=None, content_type=None, desc=None, files=None, name=None, status=None,
                 update_time=None):
        # The content of the configuration that is returned.
        self.content = content  # type: str
        # The type of the configuration content. Valid values: FILE, GIT, HTTP, and ODPS.
        self.content_type = content_type  # type: str
        # The description.
        self.desc = desc  # type: str
        # The information about files.
        self.files = files  # type: list[GetAdvanceConfigResponseBodyResultFiles]
        # The name.
        self.name = name  # type: str
        # The status.
        self.status = status  # type: str
        # The update time.
        self.update_time = update_time  # type: long

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAdvanceConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = GetAdvanceConfigResponseBodyResultFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetAdvanceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The returned results.
        self.result = result  # type: GetAdvanceConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetAdvanceConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetAdvanceConfigResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetAdvanceConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAdvanceConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAdvanceConfigResponse, self).to_map()
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
            temp_model = GetAdvanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAdvanceConfigFileRequest(TeaModel):
    def __init__(self, file_name=None):
        # The name of the file
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAdvanceConfigFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class GetAdvanceConfigFileResponseBodyResult(TeaModel):
    def __init__(self, content=None):
        # The content of the file
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAdvanceConfigFileResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class GetAdvanceConfigFileResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The result
        self.result = result  # type: GetAdvanceConfigFileResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetAdvanceConfigFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetAdvanceConfigFileResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetAdvanceConfigFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAdvanceConfigFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAdvanceConfigFileResponse, self).to_map()
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
            temp_model = GetAdvanceConfigFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterResponseBodyResultDataNode(TeaModel):
    def __init__(self, name=None, number=None, partition=None):
        # The name of the node.
        self.name = name  # type: str
        # The number of replicas.
        self.number = number  # type: int
        # The number of partitions.
        self.partition = partition  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterResponseBodyResultDataNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class GetClusterResponseBodyResultQueryNode(TeaModel):
    def __init__(self, name=None, number=None, partition=None):
        # The name of the node.
        self.name = name  # type: str
        # The number of nodes.
        self.number = number  # type: int
        # The number of replicas.
        self.partition = partition  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterResponseBodyResultQueryNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class GetClusterResponseBodyResult(TeaModel):
    def __init__(self, config_update_time=None, current_advance_config_version=None,
                 current_online_config_version=None, data_node=None, description=None, latest_advance_config_version=None,
                 latest_online_config_version=None, name=None, query_node=None, status=None):
        # The time when the cluster was updated.
        self.config_update_time = config_update_time  # type: str
        # The effective advanced configuration version.
        self.current_advance_config_version = current_advance_config_version  # type: str
        # The effective online configuration version.
        self.current_online_config_version = current_online_config_version  # type: str
        # The specifications of the data node.
        self.data_node = data_node  # type: GetClusterResponseBodyResultDataNode
        # The description of the cluster.
        self.description = description  # type: str
        # The latest advanced configuration version.
        self.latest_advance_config_version = latest_advance_config_version  # type: str
        # The latest online configuration version.
        self.latest_online_config_version = latest_online_config_version  # type: str
        # The name of the cluster.
        self.name = name  # type: str
        # The specifications of the query node.
        self.query_node = query_node  # type: GetClusterResponseBodyResultQueryNode
        # The creation status of the cluster. Valid values: NEW and PUBLISH. NEW indicates that the cluster is being created. PUBLISH indicates that the cluster is created.
        self.status = status  # type: str

    def validate(self):
        if self.data_node:
            self.data_node.validate()
        if self.query_node:
            self.query_node.validate()

    def to_map(self):
        _map = super(GetClusterResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_update_time is not None:
            result['configUpdateTime'] = self.config_update_time
        if self.current_advance_config_version is not None:
            result['currentAdvanceConfigVersion'] = self.current_advance_config_version
        if self.current_online_config_version is not None:
            result['currentOnlineConfigVersion'] = self.current_online_config_version
        if self.data_node is not None:
            result['dataNode'] = self.data_node.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.latest_advance_config_version is not None:
            result['latestAdvanceConfigVersion'] = self.latest_advance_config_version
        if self.latest_online_config_version is not None:
            result['latestOnlineConfigVersion'] = self.latest_online_config_version
        if self.name is not None:
            result['name'] = self.name
        if self.query_node is not None:
            result['queryNode'] = self.query_node.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configUpdateTime') is not None:
            self.config_update_time = m.get('configUpdateTime')
        if m.get('currentAdvanceConfigVersion') is not None:
            self.current_advance_config_version = m.get('currentAdvanceConfigVersion')
        if m.get('currentOnlineConfigVersion') is not None:
            self.current_online_config_version = m.get('currentOnlineConfigVersion')
        if m.get('dataNode') is not None:
            temp_model = GetClusterResponseBodyResultDataNode()
            self.data_node = temp_model.from_map(m['dataNode'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('latestAdvanceConfigVersion') is not None:
            self.latest_advance_config_version = m.get('latestAdvanceConfigVersion')
        if m.get('latestOnlineConfigVersion') is not None:
            self.latest_online_config_version = m.get('latestOnlineConfigVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('queryNode') is not None:
            temp_model = GetClusterResponseBodyResultQueryNode()
            self.query_node = temp_model.from_map(m['queryNode'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The list of the cluster details.
        self.result = result  # type: GetClusterResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetClusterResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClusterResponse, self).to_map()
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
            temp_model = GetClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodesConfigStatusList(TeaModel):
    def __init__(self, config_update_time=None, done_percent=None, done_size=None, name=None, total_size=None):
        # The time when the cluster was updated.
        self.config_update_time = config_update_time  # type: str
        # The overall progress.
        self.done_percent = done_percent  # type: int
        # The number of nodes that are configured.
        self.done_size = done_size  # type: int
        # The name of the cluster.
        self.name = name  # type: str
        # The total number of nodes that you specify when you create the cluster.
        self.total_size = total_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBodyResultDataNodesConfigStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_update_time is not None:
            result['configUpdateTime'] = self.config_update_time
        if self.done_percent is not None:
            result['donePercent'] = self.done_percent
        if self.done_size is not None:
            result['doneSize'] = self.done_size
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configUpdateTime') is not None:
            self.config_update_time = m.get('configUpdateTime')
        if m.get('donePercent') is not None:
            self.done_percent = m.get('donePercent')
        if m.get('doneSize') is not None:
            self.done_size = m.get('doneSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListAdvanceConfigInfo(TeaModel):
    def __init__(self, config_meta_name=None, version=None):
        # The name of the index configuration.
        self.config_meta_name = config_meta_name  # type: str
        # The version number.
        self.version = version  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListAdvanceConfigInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_meta_name is not None:
            result['configMetaName'] = self.config_meta_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configMetaName') is not None:
            self.config_meta_name = m.get('configMetaName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListIndexConfigInfo(TeaModel):
    def __init__(self, config_meta_name=None, version=None):
        # The name of the index configuration.
        self.config_meta_name = config_meta_name  # type: str
        # The version of the index template.
        self.version = version  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListIndexConfigInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_meta_name is not None:
            result['configMetaName'] = self.config_meta_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configMetaName') is not None:
            self.config_meta_name = m.get('configMetaName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusList(TeaModel):
    def __init__(self, advance_config_info=None, deploy_failed_worker=None, doc_size=None, done_percent=None,
                 done_size=None, error_msg=None, full_update_time=None, full_version=None, inc_update_time=None,
                 inc_version=None, index_config_info=None, index_size=None, lack_disk_worker=None, lack_mem_worker=None,
                 name=None, total_size=None):
        # The information about advanced configurations.
        self.advance_config_info = advance_config_info  # type: GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListAdvanceConfigInfo
        # The name of the worker that failed because of a deployment failure.
        self.deploy_failed_worker = deploy_failed_worker  # type: list[str]
        # The storage capacity. Unit: GB.
        self.doc_size = doc_size  # type: int
        # The overall progress.
        self.done_percent = done_percent  # type: int
        # The number of nodes that are configured.
        self.done_size = done_size  # type: int
        # The error message.
        self.error_msg = error_msg  # type: str
        # The time when the full data was updated.
        self.full_update_time = full_update_time  # type: str
        # The full version.
        self.full_version = full_version  # type: long
        # The time when the incremental data was updated.
        self.inc_update_time = inc_update_time  # type: str
        # The incremental version.
        self.inc_version = inc_version  # type: long
        # The configuration information of the index.
        self.index_config_info = index_config_info  # type: GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListIndexConfigInfo
        # The size of the index.
        self.index_size = index_size  # type: long
        # The name of the worker that failed because of insufficient disk space.
        self.lack_disk_worker = lack_disk_worker  # type: list[str]
        # The name of the worker that failed because of insufficient memory.
        self.lack_mem_worker = lack_mem_worker  # type: list[str]
        # The name of the node.
        self.name = name  # type: str
        # The total number of nodes that you specify when you create the cluster.
        self.total_size = total_size  # type: int

    def validate(self):
        if self.advance_config_info:
            self.advance_config_info.validate()
        if self.index_config_info:
            self.index_config_info.validate()

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_config_info is not None:
            result['advanceConfigInfo'] = self.advance_config_info.to_map()
        if self.deploy_failed_worker is not None:
            result['deployFailedWorker'] = self.deploy_failed_worker
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.done_percent is not None:
            result['donePercent'] = self.done_percent
        if self.done_size is not None:
            result['doneSize'] = self.done_size
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.full_update_time is not None:
            result['fullUpdateTime'] = self.full_update_time
        if self.full_version is not None:
            result['fullVersion'] = self.full_version
        if self.inc_update_time is not None:
            result['incUpdateTime'] = self.inc_update_time
        if self.inc_version is not None:
            result['incVersion'] = self.inc_version
        if self.index_config_info is not None:
            result['indexConfigInfo'] = self.index_config_info.to_map()
        if self.index_size is not None:
            result['indexSize'] = self.index_size
        if self.lack_disk_worker is not None:
            result['lackDiskWorker'] = self.lack_disk_worker
        if self.lack_mem_worker is not None:
            result['lackMemWorker'] = self.lack_mem_worker
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('advanceConfigInfo') is not None:
            temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListAdvanceConfigInfo()
            self.advance_config_info = temp_model.from_map(m['advanceConfigInfo'])
        if m.get('deployFailedWorker') is not None:
            self.deploy_failed_worker = m.get('deployFailedWorker')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('donePercent') is not None:
            self.done_percent = m.get('donePercent')
        if m.get('doneSize') is not None:
            self.done_size = m.get('doneSize')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('fullUpdateTime') is not None:
            self.full_update_time = m.get('fullUpdateTime')
        if m.get('fullVersion') is not None:
            self.full_version = m.get('fullVersion')
        if m.get('incUpdateTime') is not None:
            self.inc_update_time = m.get('incUpdateTime')
        if m.get('incVersion') is not None:
            self.inc_version = m.get('incVersion')
        if m.get('indexConfigInfo') is not None:
            temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusListIndexConfigInfo()
            self.index_config_info = temp_model.from_map(m['indexConfigInfo'])
        if m.get('indexSize') is not None:
            self.index_size = m.get('indexSize')
        if m.get('lackDiskWorker') is not None:
            self.lack_disk_worker = m.get('lackDiskWorker')
        if m.get('lackMemWorker') is not None:
            self.lack_mem_worker = m.get('lackMemWorker')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodesServiceStatus(TeaModel):
    def __init__(self, done_percent=None, done_size=None, name=None, total_size=None):
        # The overall progress.
        self.done_percent = done_percent  # type: int
        # The number of nodes being processed in the cluster.
        self.done_size = done_size  # type: int
        # The name.
        self.name = name  # type: str
        # The total number of nodes in the cluster.
        self.total_size = total_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBodyResultDataNodesServiceStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.done_percent is not None:
            result['donePercent'] = self.done_percent
        if self.done_size is not None:
            result['doneSize'] = self.done_size
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('donePercent') is not None:
            self.done_percent = m.get('donePercent')
        if m.get('doneSize') is not None:
            self.done_size = m.get('doneSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetClusterRunTimeInfoResponseBodyResultDataNodes(TeaModel):
    def __init__(self, config_status_list=None, data_status_list=None, service_status=None):
        # The configuration status list.
        self.config_status_list = config_status_list  # type: list[GetClusterRunTimeInfoResponseBodyResultDataNodesConfigStatusList]
        # The dataStatusList.
        self.data_status_list = data_status_list  # type: list[GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusList]
        # The service status.
        self.service_status = service_status  # type: GetClusterRunTimeInfoResponseBodyResultDataNodesServiceStatus

    def validate(self):
        if self.config_status_list:
            for k in self.config_status_list:
                if k:
                    k.validate()
        if self.data_status_list:
            for k in self.data_status_list:
                if k:
                    k.validate()
        if self.service_status:
            self.service_status.validate()

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBodyResultDataNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configStatusList'] = []
        if self.config_status_list is not None:
            for k in self.config_status_list:
                result['configStatusList'].append(k.to_map() if k else None)
        result['dataStatusList'] = []
        if self.data_status_list is not None:
            for k in self.data_status_list:
                result['dataStatusList'].append(k.to_map() if k else None)
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config_status_list = []
        if m.get('configStatusList') is not None:
            for k in m.get('configStatusList'):
                temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodesConfigStatusList()
                self.config_status_list.append(temp_model.from_map(k))
        self.data_status_list = []
        if m.get('dataStatusList') is not None:
            for k in m.get('dataStatusList'):
                temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodesDataStatusList()
                self.data_status_list.append(temp_model.from_map(k))
        if m.get('serviceStatus') is not None:
            temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodesServiceStatus()
            self.service_status = temp_model.from_map(m['serviceStatus'])
        return self


class GetClusterRunTimeInfoResponseBodyResultQueryNodeConfigStatusList(TeaModel):
    def __init__(self, config_update_time=None, done_percent=None, done_size=None, name=None, total_size=None):
        # The time when the cluster was updated.
        self.config_update_time = config_update_time  # type: str
        # The progress.
        self.done_percent = done_percent  # type: int
        # The number of nodes that are configured.
        self.done_size = done_size  # type: int
        # The name of the cluster.
        self.name = name  # type: str
        # The total number of nodes that you specify when you create the cluster.
        self.total_size = total_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBodyResultQueryNodeConfigStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_update_time is not None:
            result['configUpdateTime'] = self.config_update_time
        if self.done_percent is not None:
            result['donePercent'] = self.done_percent
        if self.done_size is not None:
            result['doneSize'] = self.done_size
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configUpdateTime') is not None:
            self.config_update_time = m.get('configUpdateTime')
        if m.get('donePercent') is not None:
            self.done_percent = m.get('donePercent')
        if m.get('doneSize') is not None:
            self.done_size = m.get('doneSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetClusterRunTimeInfoResponseBodyResultQueryNodeServiceStatus(TeaModel):
    def __init__(self, done_percent=None, done_size=None, name=None, total_size=None):
        # The progress.
        self.done_percent = done_percent  # type: int
        # The number of nodes that are configured.
        self.done_size = done_size  # type: int
        # The name of the cluster.
        self.name = name  # type: str
        # The total number of nodes that you specify when you create the cluster.
        self.total_size = total_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBodyResultQueryNodeServiceStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.done_percent is not None:
            result['donePercent'] = self.done_percent
        if self.done_size is not None:
            result['doneSize'] = self.done_size
        if self.name is not None:
            result['name'] = self.name
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('donePercent') is not None:
            self.done_percent = m.get('donePercent')
        if m.get('doneSize') is not None:
            self.done_size = m.get('doneSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetClusterRunTimeInfoResponseBodyResultQueryNode(TeaModel):
    def __init__(self, config_status_list=None, service_status=None):
        # The dataStatusList.
        self.config_status_list = config_status_list  # type: list[GetClusterRunTimeInfoResponseBodyResultQueryNodeConfigStatusList]
        # The service status.
        self.service_status = service_status  # type: GetClusterRunTimeInfoResponseBodyResultQueryNodeServiceStatus

    def validate(self):
        if self.config_status_list:
            for k in self.config_status_list:
                if k:
                    k.validate()
        if self.service_status:
            self.service_status.validate()

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBodyResultQueryNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configStatusList'] = []
        if self.config_status_list is not None:
            for k in self.config_status_list:
                result['configStatusList'].append(k.to_map() if k else None)
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config_status_list = []
        if m.get('configStatusList') is not None:
            for k in m.get('configStatusList'):
                temp_model = GetClusterRunTimeInfoResponseBodyResultQueryNodeConfigStatusList()
                self.config_status_list.append(temp_model.from_map(k))
        if m.get('serviceStatus') is not None:
            temp_model = GetClusterRunTimeInfoResponseBodyResultQueryNodeServiceStatus()
            self.service_status = temp_model.from_map(m['serviceStatus'])
        return self


class GetClusterRunTimeInfoResponseBodyResult(TeaModel):
    def __init__(self, cluster_name=None, data_nodes=None, query_node=None):
        # The name of the cluster.
        self.cluster_name = cluster_name  # type: str
        # The information about the data node.
        self.data_nodes = data_nodes  # type: list[GetClusterRunTimeInfoResponseBodyResultDataNodes]
        # The information about the query node.
        self.query_node = query_node  # type: GetClusterRunTimeInfoResponseBodyResultQueryNode

    def validate(self):
        if self.data_nodes:
            for k in self.data_nodes:
                if k:
                    k.validate()
        if self.query_node:
            self.query_node.validate()

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        result['dataNodes'] = []
        if self.data_nodes is not None:
            for k in self.data_nodes:
                result['dataNodes'].append(k.to_map() if k else None)
        if self.query_node is not None:
            result['queryNode'] = self.query_node.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        self.data_nodes = []
        if m.get('dataNodes') is not None:
            for k in m.get('dataNodes'):
                temp_model = GetClusterRunTimeInfoResponseBodyResultDataNodes()
                self.data_nodes.append(temp_model.from_map(k))
        if m.get('queryNode') is not None:
            temp_model = GetClusterRunTimeInfoResponseBodyResultQueryNode()
            self.query_node = temp_model.from_map(m['queryNode'])
        return self


class GetClusterRunTimeInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # The result set.
        self.result = result  # type: list[GetClusterRunTimeInfoResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetClusterRunTimeInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetClusterRunTimeInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetClusterRunTimeInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClusterRunTimeInfoResponse, self).to_map()
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
            temp_model = GetClusterRunTimeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSourceResponseBodyResult(TeaModel):
    def __init__(self, domain=None, indexes=None, last_ful_time=None, name=None, status=None, type=None):
        # The data center where the data source is deployed in offline mode
        self.domain = domain  # type: str
        # The list of index information
        self.indexes = indexes  # type: list[str]
        # The time when an index for full data was last built
        self.last_ful_time = last_ful_time  # type: long
        # The name of the data source
        self.name = name  # type: str
        # The state of the data source
        self.status = status  # type: str
        # The type of the data source
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.last_ful_time is not None:
            result['lastFulTime'] = self.last_ful_time
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('lastFulTime') is not None:
            self.last_ful_time = m.get('lastFulTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetDataSourceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # The list of information about the data source
        self.result = result  # type: GetDataSourceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetDataSourceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetDataSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDataSourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDataSourceResponse, self).to_map()
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
            temp_model = GetDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSourceDeployResponseBodyResultExtendHdfs(TeaModel):
    def __init__(self, path=None):
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceDeployResponseBodyResultExtendHdfs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class GetDataSourceDeployResponseBodyResultExtendOdps(TeaModel):
    def __init__(self, partitions=None):
        self.partitions = partitions  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceDeployResponseBodyResultExtendOdps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partitions is not None:
            result['partitions'] = self.partitions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')
        return self


class GetDataSourceDeployResponseBodyResultExtendOss(TeaModel):
    def __init__(self, path=None):
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceDeployResponseBodyResultExtendOss, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class GetDataSourceDeployResponseBodyResultExtendSaro(TeaModel):
    def __init__(self, path=None, version=None):
        self.path = path  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceDeployResponseBodyResultExtendSaro, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetDataSourceDeployResponseBodyResultExtend(TeaModel):
    def __init__(self, hdfs=None, odps=None, oss=None, saro=None):
        self.hdfs = hdfs  # type: GetDataSourceDeployResponseBodyResultExtendHdfs
        self.odps = odps  # type: GetDataSourceDeployResponseBodyResultExtendOdps
        self.oss = oss  # type: GetDataSourceDeployResponseBodyResultExtendOss
        self.saro = saro  # type: GetDataSourceDeployResponseBodyResultExtendSaro

    def validate(self):
        if self.hdfs:
            self.hdfs.validate()
        if self.odps:
            self.odps.validate()
        if self.oss:
            self.oss.validate()
        if self.saro:
            self.saro.validate()

    def to_map(self):
        _map = super(GetDataSourceDeployResponseBodyResultExtend, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hdfs is not None:
            result['hdfs'] = self.hdfs.to_map()
        if self.odps is not None:
            result['odps'] = self.odps.to_map()
        if self.oss is not None:
            result['oss'] = self.oss.to_map()
        if self.saro is not None:
            result['saro'] = self.saro.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('hdfs') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultExtendHdfs()
            self.hdfs = temp_model.from_map(m['hdfs'])
        if m.get('odps') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultExtendOdps()
            self.odps = temp_model.from_map(m['odps'])
        if m.get('oss') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultExtendOss()
            self.oss = temp_model.from_map(m['oss'])
        if m.get('saro') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultExtendSaro()
            self.saro = temp_model.from_map(m['saro'])
        return self


class GetDataSourceDeployResponseBodyResultProcessor(TeaModel):
    def __init__(self, args=None, resource=None):
        self.args = args  # type: str
        self.resource = resource  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceDeployResponseBodyResultProcessor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class GetDataSourceDeployResponseBodyResultStorage(TeaModel):
    def __init__(self, access_key=None, access_secret=None, bucket=None, endpoint=None, namespace=None,
                 oss_path=None, partition=None, path=None, project=None, table=None):
        self.access_key = access_key  # type: str
        self.access_secret = access_secret  # type: str
        self.bucket = bucket  # type: str
        self.endpoint = endpoint  # type: str
        self.namespace = namespace  # type: str
        self.oss_path = oss_path  # type: str
        self.partition = partition  # type: str
        self.path = path  # type: str
        self.project = project  # type: str
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceDeployResponseBodyResultStorage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetDataSourceDeployResponseBodyResultSwift(TeaModel):
    def __init__(self, topic=None, zk=None):
        self.topic = topic  # type: str
        self.zk = zk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceDeployResponseBodyResultSwift, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic is not None:
            result['topic'] = self.topic
        if self.zk is not None:
            result['zk'] = self.zk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('zk') is not None:
            self.zk = m.get('zk')
        return self


class GetDataSourceDeployResponseBodyResult(TeaModel):
    def __init__(self, auto_build_index=None, extend=None, processor=None, storage=None, swift=None):
        self.auto_build_index = auto_build_index  # type: bool
        self.extend = extend  # type: GetDataSourceDeployResponseBodyResultExtend
        self.processor = processor  # type: GetDataSourceDeployResponseBodyResultProcessor
        self.storage = storage  # type: GetDataSourceDeployResponseBodyResultStorage
        self.swift = swift  # type: GetDataSourceDeployResponseBodyResultSwift

    def validate(self):
        if self.extend:
            self.extend.validate()
        if self.processor:
            self.processor.validate()
        if self.storage:
            self.storage.validate()
        if self.swift:
            self.swift.validate()

    def to_map(self):
        _map = super(GetDataSourceDeployResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.extend is not None:
            result['extend'] = self.extend.to_map()
        if self.processor is not None:
            result['processor'] = self.processor.to_map()
        if self.storage is not None:
            result['storage'] = self.storage.to_map()
        if self.swift is not None:
            result['swift'] = self.swift.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('extend') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultExtend()
            self.extend = temp_model.from_map(m['extend'])
        if m.get('processor') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultProcessor()
            self.processor = temp_model.from_map(m['processor'])
        if m.get('storage') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultStorage()
            self.storage = temp_model.from_map(m['storage'])
        if m.get('swift') is not None:
            temp_model = GetDataSourceDeployResponseBodyResultSwift()
            self.swift = temp_model.from_map(m['swift'])
        return self


class GetDataSourceDeployResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: GetDataSourceDeployResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetDataSourceDeployResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetDataSourceDeployResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetDataSourceDeployResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDataSourceDeployResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDataSourceDeployResponse, self).to_map()
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
            temp_model = GetDataSourceDeployResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeployGraphResponseBodyResultGraphIndexMetas(TeaModel):
    def __init__(self, domain_name=None, name=None, table_deploy_id=None, table_name=None, tag=None, zone_name=None):
        self.domain_name = domain_name  # type: str
        self.name = name  # type: str
        self.table_deploy_id = table_deploy_id  # type: long
        self.table_name = table_name  # type: str
        self.tag = tag  # type: str
        self.zone_name = zone_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeployGraphResponseBodyResultGraphIndexMetas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.name is not None:
            result['name'] = self.name
        if self.table_deploy_id is not None:
            result['tableDeployId'] = self.table_deploy_id
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.tag is not None:
            result['tag'] = self.tag
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tableDeployId') is not None:
            self.table_deploy_id = m.get('tableDeployId')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self


class GetDeployGraphResponseBodyResultGraphOnlineMaster(TeaModel):
    def __init__(self, domain_name=None, hippo_id=None, id=None, name=None):
        self.domain_name = domain_name  # type: str
        self.hippo_id = hippo_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeployGraphResponseBodyResultGraphOnlineMaster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.hippo_id is not None:
            result['hippoId'] = self.hippo_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('hippoId') is not None:
            self.hippo_id = m.get('hippoId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetDeployGraphResponseBodyResultGraphTableMetas(TeaModel):
    def __init__(self, build_deploy_id=None, domain_name=None, name=None, table_deploy_id=None, tag=None, type=None):
        self.build_deploy_id = build_deploy_id  # type: long
        self.domain_name = domain_name  # type: str
        self.name = name  # type: str
        self.table_deploy_id = table_deploy_id  # type: long
        self.tag = tag  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeployGraphResponseBodyResultGraphTableMetas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_deploy_id is not None:
            result['buildDeployId'] = self.build_deploy_id
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.name is not None:
            result['name'] = self.name
        if self.table_deploy_id is not None:
            result['tableDeployId'] = self.table_deploy_id
        if self.tag is not None:
            result['tag'] = self.tag
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('buildDeployId') is not None:
            self.build_deploy_id = m.get('buildDeployId')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tableDeployId') is not None:
            self.table_deploy_id = m.get('tableDeployId')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetDeployGraphResponseBodyResultGraphZoneMetas(TeaModel):
    def __init__(self, domain_info=None, name=None, suez_admin_name=None, tag=None, type=None):
        self.domain_info = domain_info  # type: str
        self.name = name  # type: str
        self.suez_admin_name = suez_admin_name  # type: str
        self.tag = tag  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeployGraphResponseBodyResultGraphZoneMetas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_info is not None:
            result['domainInfo'] = self.domain_info
        if self.name is not None:
            result['name'] = self.name
        if self.suez_admin_name is not None:
            result['suezAdminName'] = self.suez_admin_name
        if self.tag is not None:
            result['tag'] = self.tag
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domainInfo') is not None:
            self.domain_info = m.get('domainInfo')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('suezAdminName') is not None:
            self.suez_admin_name = m.get('suezAdminName')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetDeployGraphResponseBodyResultGraph(TeaModel):
    def __init__(self, index_metas=None, online_master=None, table_index_relation=None, table_metas=None,
                 zone_index_relation=None, zone_metas=None):
        # 索引元信息
        self.index_metas = index_metas  # type: list[GetDeployGraphResponseBodyResultGraphIndexMetas]
        # 在线集群元信息
        self.online_master = online_master  # type: list[GetDeployGraphResponseBodyResultGraphOnlineMaster]
        # 数据源和索引关联关系
        self.table_index_relation = table_index_relation  # type: dict[str, list[str]]
        # 数据源元信息
        self.table_metas = table_metas  # type: list[GetDeployGraphResponseBodyResultGraphTableMetas]
        # zone和索引关联关系
        self.zone_index_relation = zone_index_relation  # type: dict[str, list[str]]
        # zone元信息
        self.zone_metas = zone_metas  # type: list[GetDeployGraphResponseBodyResultGraphZoneMetas]

    def validate(self):
        if self.index_metas:
            for k in self.index_metas:
                if k:
                    k.validate()
        if self.online_master:
            for k in self.online_master:
                if k:
                    k.validate()
        if self.table_metas:
            for k in self.table_metas:
                if k:
                    k.validate()
        if self.zone_metas:
            for k in self.zone_metas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDeployGraphResponseBodyResultGraph, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['indexMetas'] = []
        if self.index_metas is not None:
            for k in self.index_metas:
                result['indexMetas'].append(k.to_map() if k else None)
        result['onlineMaster'] = []
        if self.online_master is not None:
            for k in self.online_master:
                result['onlineMaster'].append(k.to_map() if k else None)
        if self.table_index_relation is not None:
            result['tableIndexRelation'] = self.table_index_relation
        result['tableMetas'] = []
        if self.table_metas is not None:
            for k in self.table_metas:
                result['tableMetas'].append(k.to_map() if k else None)
        if self.zone_index_relation is not None:
            result['zoneIndexRelation'] = self.zone_index_relation
        result['zoneMetas'] = []
        if self.zone_metas is not None:
            for k in self.zone_metas:
                result['zoneMetas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.index_metas = []
        if m.get('indexMetas') is not None:
            for k in m.get('indexMetas'):
                temp_model = GetDeployGraphResponseBodyResultGraphIndexMetas()
                self.index_metas.append(temp_model.from_map(k))
        self.online_master = []
        if m.get('onlineMaster') is not None:
            for k in m.get('onlineMaster'):
                temp_model = GetDeployGraphResponseBodyResultGraphOnlineMaster()
                self.online_master.append(temp_model.from_map(k))
        if m.get('tableIndexRelation') is not None:
            self.table_index_relation = m.get('tableIndexRelation')
        self.table_metas = []
        if m.get('tableMetas') is not None:
            for k in m.get('tableMetas'):
                temp_model = GetDeployGraphResponseBodyResultGraphTableMetas()
                self.table_metas.append(temp_model.from_map(k))
        if m.get('zoneIndexRelation') is not None:
            self.zone_index_relation = m.get('zoneIndexRelation')
        self.zone_metas = []
        if m.get('zoneMetas') is not None:
            for k in m.get('zoneMetas'):
                temp_model = GetDeployGraphResponseBodyResultGraphZoneMetas()
                self.zone_metas.append(temp_model.from_map(k))
        return self


class GetDeployGraphResponseBodyResult(TeaModel):
    def __init__(self, graph=None):
        self.graph = graph  # type: GetDeployGraphResponseBodyResultGraph

    def validate(self):
        if self.graph:
            self.graph.validate()

    def to_map(self):
        _map = super(GetDeployGraphResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.graph is not None:
            result['graph'] = self.graph.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('graph') is not None:
            temp_model = GetDeployGraphResponseBodyResultGraph()
            self.graph = temp_model.from_map(m['graph'])
        return self


class GetDeployGraphResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # The result returned
        self.result = result  # type: GetDeployGraphResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetDeployGraphResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetDeployGraphResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetDeployGraphResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeployGraphResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeployGraphResponse, self).to_map()
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
            temp_model = GetDeployGraphResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileRequest(TeaModel):
    def __init__(self, file_name=None):
        # The name of the file in full path
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class GetFileResponseBodyResult(TeaModel):
    def __init__(self, content=None, data_source=None, full_path_name=None, is_dir=None, name=None, partition=None):
        # The content of the file.
        self.content = content  # type: str
        # The data source.
        self.data_source = data_source  # type: str
        # The name of the full path.
        self.full_path_name = full_path_name  # type: str
        # Indicates whether it is a directory.
        self.is_dir = is_dir  # type: bool
        # The name of the file.
        self.name = name  # type: str
        # The number of shards.
        self.partition = partition  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.name is not None:
            result['name'] = self.name
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class GetFileResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The information about the index.
        self.result = result  # type: GetFileResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetFileResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFileResponse, self).to_map()
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
            temp_model = GetFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndexResponseBodyResultDataSourceInfoConfig(TeaModel):
    def __init__(self, access_key=None, access_secret=None, bucket=None, endpoint=None, namespace=None,
                 oss_path=None, partition=None, path=None, project=None, table=None):
        self.access_key = access_key  # type: str
        self.access_secret = access_secret  # type: str
        self.bucket = bucket  # type: str
        # A parameter related to MaxCompute.
        self.endpoint = endpoint  # type: str
        # A parameter related to SARO.
        self.namespace = namespace  # type: str
        # A parameter related to OSS.
        self.oss_path = oss_path  # type: str
        self.partition = partition  # type: str
        # A parameter related to Apsara File Storage for HDFS.
        self.path = path  # type: str
        self.project = project  # type: str
        # A parameter related to SARO and MaxCompute.
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIndexResponseBodyResultDataSourceInfoConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetIndexResponseBodyResultDataSourceInfoSaroConfig(TeaModel):
    def __init__(self, namespace=None, table_name=None):
        self.namespace = namespace  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIndexResponseBodyResultDataSourceInfoSaroConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class GetIndexResponseBodyResultDataSourceInfo(TeaModel):
    def __init__(self, auto_build_index=None, config=None, domain=None, name=None, process_partition_count=None,
                 saro_config=None, type=None):
        # Indicates whether the automatic full indexing feature is enabled.
        self.auto_build_index = auto_build_index  # type: bool
        # The configuration of MaxCompute data sources.
        self.config = config  # type: GetIndexResponseBodyResultDataSourceInfoConfig
        # The offline deployment name of the data source.
        self.domain = domain  # type: str
        # The name of the data source.
        self.name = name  # type: str
        # The number of resources used for data update.
        self.process_partition_count = process_partition_count  # type: int
        # The configuration of SARO data sources.
        self.saro_config = saro_config  # type: GetIndexResponseBodyResultDataSourceInfoSaroConfig
        # The type of the data source. Valid values: odps, swift, saro, oss, and unKnow.
        self.type = type  # type: str

    def validate(self):
        if self.config:
            self.config.validate()
        if self.saro_config:
            self.saro_config.validate()

    def to_map(self):
        _map = super(GetIndexResponseBodyResultDataSourceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.name is not None:
            result['name'] = self.name
        if self.process_partition_count is not None:
            result['processPartitionCount'] = self.process_partition_count
        if self.saro_config is not None:
            result['saroConfig'] = self.saro_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = GetIndexResponseBodyResultDataSourceInfoConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processPartitionCount') is not None:
            self.process_partition_count = m.get('processPartitionCount')
        if m.get('saroConfig') is not None:
            temp_model = GetIndexResponseBodyResultDataSourceInfoSaroConfig()
            self.saro_config = temp_model.from_map(m['saroConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetIndexResponseBodyResultVersionsFiles(TeaModel):
    def __init__(self, full_path_name=None, is_dir=None, is_template=None, name=None):
        # The full path of the file.
        self.full_path_name = full_path_name  # type: str
        # Indicates whether the file is a directory.
        self.is_dir = is_dir  # type: bool
        # Indicates whether the file is a template.
        self.is_template = is_template  # type: bool
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIndexResponseBodyResultVersionsFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetIndexResponseBodyResultVersions(TeaModel):
    def __init__(self, desc=None, files=None, name=None, status=None, update_time=None, version_id=None):
        # The description of the version.
        self.desc = desc  # type: str
        # The information about the files.
        self.files = files  # type: list[GetIndexResponseBodyResultVersionsFiles]
        # The name of the version.
        self.name = name  # type: str
        # The status of the version.
        self.status = status  # type: str
        # The last time when the version was updated.
        self.update_time = update_time  # type: long
        # The ID of the version.
        self.version_id = version_id  # type: int

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetIndexResponseBodyResultVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = GetIndexResponseBodyResultVersionsFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class GetIndexResponseBodyResult(TeaModel):
    def __init__(self, content=None, data_source=None, data_source_info=None, description=None, domain=None,
                 full_update_time=None, full_version=None, inc_update_time=None, index_size=None, index_status=None, name=None,
                 partition=None, versions=None):
        # The content of the index.
        self.content = content  # type: str
        self.data_source = data_source  # type: str
        # The information about the data source.
        self.data_source_info = data_source_info  # type: GetIndexResponseBodyResultDataSourceInfo
        # The remarks.
        self.description = description  # type: str
        self.domain = domain  # type: str
        # The last time when full data in the index was updated.
        self.full_update_time = full_update_time  # type: str
        # The version of the data.
        self.full_version = full_version  # type: long
        # The last time when incremental data in the index was updated.
        self.inc_update_time = inc_update_time  # type: str
        # The index size.
        self.index_size = index_size  # type: long
        # The status of the index. Valid values: NEW, PUBLISH, IN_USE, NOT_USE, STOP_USE, and RESTORE_USE. After a Retrieval Engine Edition instance is created, it enters the IN_USE state.
        self.index_status = index_status  # type: str
        self.name = name  # type: str
        # The number of shards.
        self.partition = partition  # type: int
        # The information about the versions.
        self.versions = versions  # type: list[GetIndexResponseBodyResultVersions]

    def validate(self):
        if self.data_source_info:
            self.data_source_info.validate()
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetIndexResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.data_source_info is not None:
            result['dataSourceInfo'] = self.data_source_info.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.full_update_time is not None:
            result['fullUpdateTime'] = self.full_update_time
        if self.full_version is not None:
            result['fullVersion'] = self.full_version
        if self.inc_update_time is not None:
            result['incUpdateTime'] = self.inc_update_time
        if self.index_size is not None:
            result['indexSize'] = self.index_size
        if self.index_status is not None:
            result['indexStatus'] = self.index_status
        if self.name is not None:
            result['name'] = self.name
        if self.partition is not None:
            result['partition'] = self.partition
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('dataSourceInfo') is not None:
            temp_model = GetIndexResponseBodyResultDataSourceInfo()
            self.data_source_info = temp_model.from_map(m['dataSourceInfo'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('fullUpdateTime') is not None:
            self.full_update_time = m.get('fullUpdateTime')
        if m.get('fullVersion') is not None:
            self.full_version = m.get('fullVersion')
        if m.get('incUpdateTime') is not None:
            self.inc_update_time = m.get('incUpdateTime')
        if m.get('indexSize') is not None:
            self.index_size = m.get('indexSize')
        if m.get('indexStatus') is not None:
            self.index_status = m.get('indexStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = GetIndexResponseBodyResultVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class GetIndexResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the index.
        self.result = result  # type: GetIndexResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetIndexResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetIndexResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIndexResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIndexResponse, self).to_map()
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
            temp_model = GetIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndexVersionResponseBodyResultIndexVersions(TeaModel):
    def __init__(self, build_deploy_id=None, current_version=None, index_name=None, versions=None):
        # The ID of the index deployed in offline mode
        self.build_deploy_id = build_deploy_id  # type: str
        self.current_version = current_version  # type: long
        # The name of the index table
        self.index_name = index_name  # type: str
        # The version of the index
        self.versions = versions  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIndexVersionResponseBodyResultIndexVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_deploy_id is not None:
            result['buildDeployId'] = self.build_deploy_id
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.versions is not None:
            result['versions'] = self.versions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('buildDeployId') is not None:
            self.build_deploy_id = m.get('buildDeployId')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('versions') is not None:
            self.versions = m.get('versions')
        return self


class GetIndexVersionResponseBodyResult(TeaModel):
    def __init__(self, cluster=None, index_versions=None):
        # The name of the cluster
        self.cluster = cluster  # type: str
        # The time when the cluster was updated
        self.index_versions = index_versions  # type: list[GetIndexVersionResponseBodyResultIndexVersions]

    def validate(self):
        if self.index_versions:
            for k in self.index_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetIndexVersionResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        result['indexVersions'] = []
        if self.index_versions is not None:
            for k in self.index_versions:
                result['indexVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        self.index_versions = []
        if m.get('indexVersions') is not None:
            for k in m.get('indexVersions'):
                temp_model = GetIndexVersionResponseBodyResultIndexVersions()
                self.index_versions.append(temp_model.from_map(k))
        return self


class GetIndexVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The list of cluster details
        self.result = result  # type: GetIndexVersionResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetIndexVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetIndexVersionResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetIndexVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIndexVersionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIndexVersionResponse, self).to_map()
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
            temp_model = GetIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyResultTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签键
        self.key = key  # type: str
        # 标签值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyResultTags, self).to_map()
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


class GetInstanceResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, commodity_code=None, create_time=None, description=None, expired_time=None,
                 in_debt=None, instance_id=None, lock_mode=None, resource_group_id=None, status=None, tags=None,
                 update_time=None):
        # The billing method.
        self.charge_type = charge_type  # type: str
        # The product code.
        self.commodity_code = commodity_code  # type: str
        # The time when the instance was created.
        self.create_time = create_time  # type: str
        # The description of the instance.
        self.description = description  # type: str
        # The expiration time.
        self.expired_time = expired_time  # type: str
        # Indicates whether an overdue payment is involved.
        self.in_debt = in_debt  # type: bool
        # The ID of the resource.
        self.instance_id = instance_id  # type: str
        # The lock status.
        self.lock_mode = lock_mode  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The status of the instance. Valid values:
        # 
        # *   INIT: being initialized
        # *   WAIT_CONFIG: to be configured
        # *   CONFIG_UPDATING: configuration taking effect
        # *   READY: normal
        self.status = status  # type: str
        # 标签。
        self.tags = tags  # type: list[GetInstanceResponseBodyResultTags]
        # The time when the instance was last updated.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.in_debt is not None:
            result['inDebt'] = self.in_debt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('inDebt') is not None:
            self.in_debt = m.get('inDebt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = GetInstanceResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result returned.
        self.result = result  # type: GetInstanceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceResponseBody

    def validate(self):
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


class GetNodeConfigRequest(TeaModel):
    def __init__(self, cluster_name=None, name=None, type=None):
        # The name of the cluster
        self.cluster_name = cluster_name  # type: str
        # The name of the cluster.
        self.name = name  # type: str
        # The type of the node. Valid values: qrs, search, index, and cluster. qrs indicates a query node, search indicates a data node, index indicates an index node, and cluster indicates a cluster node.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNodeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetNodeConfigResponseBodyResult(TeaModel):
    def __init__(self, active=None, data_duplicate_number=None, data_fragment_number=None, flow_ratio=None,
                 min_service_percent=None, published=None):
        # Indicates whether the expression is the default one.
        self.active = active  # type: bool
        # The number of data replicas.
        self.data_duplicate_number = data_duplicate_number  # type: int
        # The number of data shards.
        self.data_fragment_number = data_fragment_number  # type: int
        self.flow_ratio = flow_ratio  # type: int
        # The minimum service ratio.
        self.min_service_percent = min_service_percent  # type: int
        # Indicates whether the node is associated with the cluster.
        self.published = published  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNodeConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.data_duplicate_number is not None:
            result['dataDuplicateNumber'] = self.data_duplicate_number
        if self.data_fragment_number is not None:
            result['dataFragmentNumber'] = self.data_fragment_number
        if self.flow_ratio is not None:
            result['flowRatio'] = self.flow_ratio
        if self.min_service_percent is not None:
            result['minServicePercent'] = self.min_service_percent
        if self.published is not None:
            result['published'] = self.published
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('dataDuplicateNumber') is not None:
            self.data_duplicate_number = m.get('dataDuplicateNumber')
        if m.get('dataFragmentNumber') is not None:
            self.data_fragment_number = m.get('dataFragmentNumber')
        if m.get('flowRatio') is not None:
            self.flow_ratio = m.get('flowRatio')
        if m.get('minServicePercent') is not None:
            self.min_service_percent = m.get('minServicePercent')
        if m.get('published') is not None:
            self.published = m.get('published')
        return self


class GetNodeConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # The result set.
        self.result = result  # type: GetNodeConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetNodeConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetNodeConfigResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetNodeConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNodeConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNodeConfigResponse, self).to_map()
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
            temp_model = GetNodeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAdvanceConfigDirRequest(TeaModel):
    def __init__(self, dir_name=None):
        # The name of the directory
        self.dir_name = dir_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvanceConfigDirRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dir_name is not None:
            result['dirName'] = self.dir_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dirName') is not None:
            self.dir_name = m.get('dirName')
        return self


class ListAdvanceConfigDirResponseBodyResult(TeaModel):
    def __init__(self, full_path_name=None, is_dir=None, is_template=None, name=None):
        # The name of the absolute path.
        self.full_path_name = full_path_name  # type: str
        # Indicates whether it is a directory. Valid values: true and false. true indicates that it is a directory, and false indicates that it is not a directory.
        self.is_dir = is_dir  # type: bool
        # Indicates whether it is a template. Valid values: **true** and **false**. true indicates that it is a template, and false indicates that it is not a template.
        self.is_template = is_template  # type: bool
        # The name of the cluster.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvanceConfigDirResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListAdvanceConfigDirResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The file list in the advanced configuration directory.
        self.result = result  # type: list[ListAdvanceConfigDirResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAdvanceConfigDirResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListAdvanceConfigDirResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAdvanceConfigDirResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAdvanceConfigDirResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAdvanceConfigDirResponse, self).to_map()
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
            temp_model = ListAdvanceConfigDirResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAdvanceConfigsRequest(TeaModel):
    def __init__(self, data_source_name=None, index_name=None, type=None):
        self.data_source_name = data_source_name  # type: str
        self.index_name = index_name  # type: str
        # The type of the advanced configurations. Valid values: online and offline. - online The default value is offline.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvanceConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAdvanceConfigsResponseBodyResultFiles(TeaModel):
    def __init__(self, full_path_name=None, is_dir=None, is_template=None, name=None):
        # The name of the absolute path.
        self.full_path_name = full_path_name  # type: str
        # Indicates whether it is a directory. Valid values: true and false. true indicates that it is a directory, and false indicates that it is not a directory.
        self.is_dir = is_dir  # type: bool
        # Indicates whether it is a template. Valid values: true and false. true indicates that it is a directory, and false indicates that it is not a directory.
        self.is_template = is_template  # type: bool
        # The name of the file.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAdvanceConfigsResponseBodyResultFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListAdvanceConfigsResponseBodyResult(TeaModel):
    def __init__(self, content=None, content_type=None, desc=None, files=None, name=None, status=None,
                 update_time=None):
        self.content = content  # type: str
        self.content_type = content_type  # type: str
        # The description.
        self.desc = desc  # type: str
        # The list of file names.
        self.files = files  # type: list[ListAdvanceConfigsResponseBodyResultFiles]
        # The name of the advanced configuration.
        self.name = name  # type: str
        # The state of the advanced configuration. Valid values: drafting, used, unused, and trash. drafting indicates that the advanced configuration is a draft. used indicates that the advanced configuration is in use. unused indicates that the advanced configuration is unused. trash indicates that the advanced configuration is being deleted.
        self.status = status  # type: str
        # The update time.
        self.update_time = update_time  # type: long

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAdvanceConfigsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = ListAdvanceConfigsResponseBodyResultFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListAdvanceConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The list of advanced configurations.
        self.result = result  # type: list[ListAdvanceConfigsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAdvanceConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListAdvanceConfigsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAdvanceConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAdvanceConfigsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAdvanceConfigsResponse, self).to_map()
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
            temp_model = ListAdvanceConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterNamesResponseBodyResult(TeaModel):
    def __init__(self, description=None, id=None, name=None):
        # The description of the cluster
        self.description = description  # type: str
        # The ID of the cluster
        self.id = id  # type: long
        # The name of the cluster
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterNamesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListClusterNamesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The result set
        self.result = result  # type: ListClusterNamesResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListClusterNamesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListClusterNamesResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListClusterNamesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClusterNamesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterNamesResponse, self).to_map()
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
            temp_model = ListClusterNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterTasksResponseBodyResultTags(TeaModel):
    def __init__(self, msg=None, tag_level=None):
        # The content of the tag.
        self.msg = msg  # type: str
        # The level of the tag.
        self.tag_level = tag_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterTasksResponseBodyResultTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.tag_level is not None:
            result['tagLevel'] = self.tag_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('tagLevel') is not None:
            self.tag_level = m.get('tagLevel')
        return self


class ListClusterTasksResponseBodyResultTaskNodes(TeaModel):
    def __init__(self, finish_date=None, index=None, name=None, status=None):
        # The date when the task was completed.
        self.finish_date = finish_date  # type: str
        # The sequence number of the task.
        self.index = index  # type: long
        # The name of the task.
        self.name = name  # type: str
        # The status of the task.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterTasksResponseBodyResultTaskNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_date is not None:
            result['finishDate'] = self.finish_date
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('finishDate') is not None:
            self.finish_date = m.get('finishDate')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListClusterTasksResponseBodyResult(TeaModel):
    def __init__(self, extra_attribute=None, field_3=None, fsm_id=None, group_type=None, name=None, status=None,
                 tags=None, task_nodes=None, time=None, type=None, user=None):
        # The additional attributes of the card.
        self.extra_attribute = extra_attribute  # type: str
        # The field3 field that is passed through when you create a state machine.
        self.field_3 = field_3  # type: str
        # fsmId
        self.fsm_id = fsm_id  # type: str
        # Indicates whether the change is a data source task change or a cluster task change.
        self.group_type = group_type  # type: str
        # The task name on the card.
        self.name = name  # type: str
        # The overall status of FSM.
        self.status = status  # type: str
        # The status tag of the progress bar chart.
        self.tags = tags  # type: list[ListClusterTasksResponseBodyResultTags]
        # The information about the task.
        self.task_nodes = task_nodes  # type: list[ListClusterTasksResponseBodyResultTaskNodes]
        # The timestamp of the task on the card.
        self.time = time  # type: str
        # The type of the task on the card.
        self.type = type  # type: str
        # The user who triggered the FSM process.
        self.user = user  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.task_nodes:
            for k in self.task_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterTasksResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_attribute is not None:
            result['extraAttribute'] = self.extra_attribute
        if self.field_3 is not None:
            result['field3'] = self.field_3
        if self.fsm_id is not None:
            result['fsmId'] = self.fsm_id
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['taskNodes'] = []
        if self.task_nodes is not None:
            for k in self.task_nodes:
                result['taskNodes'].append(k.to_map() if k else None)
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('extraAttribute') is not None:
            self.extra_attribute = m.get('extraAttribute')
        if m.get('field3') is not None:
            self.field_3 = m.get('field3')
        if m.get('fsmId') is not None:
            self.fsm_id = m.get('fsmId')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListClusterTasksResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        self.task_nodes = []
        if m.get('taskNodes') is not None:
            for k in m.get('taskNodes'):
                temp_model = ListClusterTasksResponseBodyResultTaskNodes()
                self.task_nodes.append(temp_model.from_map(k))
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ListClusterTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The information about the index.
        self.result = result  # type: list[ListClusterTasksResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListClusterTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListClusterTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClusterTasksResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterTasksResponse, self).to_map()
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
            temp_model = ListClusterTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersResponseBodyResultDataNode(TeaModel):
    def __init__(self, name=None, number=None, partition=None):
        # The name of the node.
        self.name = name  # type: str
        # The number of nodes.
        self.number = number  # type: int
        # The partition ID of the node.
        self.partition = partition  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyResultDataNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class ListClustersResponseBodyResultQueryNode(TeaModel):
    def __init__(self, name=None, number=None, partition=None):
        # The name of the node.
        self.name = name  # type: str
        # The number of nodes.
        self.number = number  # type: int
        # The number o replicas.
        self.partition = partition  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyResultQueryNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        if self.partition is not None:
            result['partition'] = self.partition
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        return self


class ListClustersResponseBodyResult(TeaModel):
    def __init__(self, config_update_time=None, current_advance_config_version=None,
                 current_offline_dict_config_version=None, current_online_config_version=None, current_online_query_config_version=None,
                 data_node=None, description=None, latest_advance_config_version=None,
                 latest_offline_dict_config_version=None, latest_online_config_version=None, latest_online_query_config_version=None, name=None,
                 query_node=None, status=None):
        # The time when the configuration was updated.
        self.config_update_time = config_update_time  # type: str
        # The effective advanced version.
        self.current_advance_config_version = current_advance_config_version  # type: str
        # 词典配置生效版本
        self.current_offline_dict_config_version = current_offline_dict_config_version  # type: str
        # The effective online configuration version.
        self.current_online_config_version = current_online_config_version  # type: str
        # 查询配置生效版本
        self.current_online_query_config_version = current_online_query_config_version  # type: str
        # The information about the node in the cluster.
        self.data_node = data_node  # type: ListClustersResponseBodyResultDataNode
        # The description of the cluster.
        self.description = description  # type: str
        # The latest advanced configuration version.
        self.latest_advance_config_version = latest_advance_config_version  # type: str
        # 词典配置最新版本
        self.latest_offline_dict_config_version = latest_offline_dict_config_version  # type: str
        # The latest online configuration version.
        self.latest_online_config_version = latest_online_config_version  # type: str
        # 查询配置最新版本
        self.latest_online_query_config_version = latest_online_query_config_version  # type: str
        # The name of the cluster.
        self.name = name  # type: str
        # The query node of the cluster.
        self.query_node = query_node  # type: ListClustersResponseBodyResultQueryNode
        # The status of the cluster. Valid values: running, starting, stopping, and stopped. running indicates the cluster is running, starting indicates the cluster is starting, stopping indicates the cluster is stopping, and stopped indicates the cluster has stopped.
        self.status = status  # type: str

    def validate(self):
        if self.data_node:
            self.data_node.validate()
        if self.query_node:
            self.query_node.validate()

    def to_map(self):
        _map = super(ListClustersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_update_time is not None:
            result['configUpdateTime'] = self.config_update_time
        if self.current_advance_config_version is not None:
            result['currentAdvanceConfigVersion'] = self.current_advance_config_version
        if self.current_offline_dict_config_version is not None:
            result['currentOfflineDictConfigVersion'] = self.current_offline_dict_config_version
        if self.current_online_config_version is not None:
            result['currentOnlineConfigVersion'] = self.current_online_config_version
        if self.current_online_query_config_version is not None:
            result['currentOnlineQueryConfigVersion'] = self.current_online_query_config_version
        if self.data_node is not None:
            result['dataNode'] = self.data_node.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.latest_advance_config_version is not None:
            result['latestAdvanceConfigVersion'] = self.latest_advance_config_version
        if self.latest_offline_dict_config_version is not None:
            result['latestOfflineDictConfigVersion'] = self.latest_offline_dict_config_version
        if self.latest_online_config_version is not None:
            result['latestOnlineConfigVersion'] = self.latest_online_config_version
        if self.latest_online_query_config_version is not None:
            result['latestOnlineQueryConfigVersion'] = self.latest_online_query_config_version
        if self.name is not None:
            result['name'] = self.name
        if self.query_node is not None:
            result['queryNode'] = self.query_node.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configUpdateTime') is not None:
            self.config_update_time = m.get('configUpdateTime')
        if m.get('currentAdvanceConfigVersion') is not None:
            self.current_advance_config_version = m.get('currentAdvanceConfigVersion')
        if m.get('currentOfflineDictConfigVersion') is not None:
            self.current_offline_dict_config_version = m.get('currentOfflineDictConfigVersion')
        if m.get('currentOnlineConfigVersion') is not None:
            self.current_online_config_version = m.get('currentOnlineConfigVersion')
        if m.get('currentOnlineQueryConfigVersion') is not None:
            self.current_online_query_config_version = m.get('currentOnlineQueryConfigVersion')
        if m.get('dataNode') is not None:
            temp_model = ListClustersResponseBodyResultDataNode()
            self.data_node = temp_model.from_map(m['dataNode'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('latestAdvanceConfigVersion') is not None:
            self.latest_advance_config_version = m.get('latestAdvanceConfigVersion')
        if m.get('latestOfflineDictConfigVersion') is not None:
            self.latest_offline_dict_config_version = m.get('latestOfflineDictConfigVersion')
        if m.get('latestOnlineConfigVersion') is not None:
            self.latest_online_config_version = m.get('latestOnlineConfigVersion')
        if m.get('latestOnlineQueryConfigVersion') is not None:
            self.latest_online_query_config_version = m.get('latestOnlineQueryConfigVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('queryNode') is not None:
            temp_model = ListClustersResponseBodyResultQueryNode()
            self.query_node = temp_model.from_map(m['queryNode'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The list of clusters.
        self.result = result  # type: list[ListClustersResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListClustersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClustersResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClustersResponse, self).to_map()
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
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceSchemasResponseBodyResultPrimaryKey(TeaModel):
    def __init__(self, has_primary_key_attribute=None, is_primary_key=None, is_primary_key_sorted=None):
        # Indicates whether it has the primary key property. **true** indicates that it has the primary key property, and **false** indicates that it does not have the primary key property.
        self.has_primary_key_attribute = has_primary_key_attribute  # type: bool
        # Indicates whether it is the primary key. Valid values: true and false. **true** indicates that it is the primary key, and **false** indicates that it is not the primary key.
        self.is_primary_key = is_primary_key  # type: bool
        # Indicates whether data is sorted based on the primary key. Valid values: true and false. **true** indicates that data is sorted based on the primary key, and **false** indicates that data is not sorted based on the primary key.
        self.is_primary_key_sorted = is_primary_key_sorted  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceSchemasResponseBodyResultPrimaryKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_primary_key_attribute is not None:
            result['hasPrimaryKeyAttribute'] = self.has_primary_key_attribute
        if self.is_primary_key is not None:
            result['isPrimaryKey'] = self.is_primary_key
        if self.is_primary_key_sorted is not None:
            result['isPrimaryKeySorted'] = self.is_primary_key_sorted
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('hasPrimaryKeyAttribute') is not None:
            self.has_primary_key_attribute = m.get('hasPrimaryKeyAttribute')
        if m.get('isPrimaryKey') is not None:
            self.is_primary_key = m.get('isPrimaryKey')
        if m.get('isPrimaryKeySorted') is not None:
            self.is_primary_key_sorted = m.get('isPrimaryKeySorted')
        return self


class ListDataSourceSchemasResponseBodyResult(TeaModel):
    def __init__(self, add_index=None, attribute=None, custom=None, name=None, primary_key=None, summary=None,
                 type=None):
        # Indicates whether the index properties are added. Valid values: true and false. **true** indicates that the index properties are added, and **false** indicates that the index properties are not added.
        self.add_index = add_index  # type: bool
        # Indicates whether it is an attribute field. Valid values: true and false. **true** indicates that it is an attribute field, and **false** indicates that it is not an attribute field.
        self.attribute = attribute  # type: bool
        # Indicates whether it is a custom field. Valid values: true and false. **true** indicates that it is a custom field, and **false** indicates that it is not a custom field.
        self.custom = custom  # type: bool
        # The name of the field.
        self.name = name  # type: str
        # The primary key.
        self.primary_key = primary_key  # type: ListDataSourceSchemasResponseBodyResultPrimaryKey
        # Indicates whether the information can be displayed. Valid values: true and false. **true** indicates that the information can be displayed, and **false** indicates that the information cannot be displayed.
        self.summary = summary  # type: bool
        # The type of the field.
        self.type = type  # type: str

    def validate(self):
        if self.primary_key:
            self.primary_key.validate()

    def to_map(self):
        _map = super(ListDataSourceSchemasResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_index is not None:
            result['addIndex'] = self.add_index
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.custom is not None:
            result['custom'] = self.custom
        if self.name is not None:
            result['name'] = self.name
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key.to_map()
        if self.summary is not None:
            result['summary'] = self.summary
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('addIndex') is not None:
            self.add_index = m.get('addIndex')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('custom') is not None:
            self.custom = m.get('custom')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('primaryKey') is not None:
            temp_model = ListDataSourceSchemasResponseBodyResultPrimaryKey()
            self.primary_key = temp_model.from_map(m['primaryKey'])
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDataSourceSchemasResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result returned.
        self.result = result  # type: list[ListDataSourceSchemasResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourceSchemasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataSourceSchemasResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataSourceSchemasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataSourceSchemasResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourceSchemasResponse, self).to_map()
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
            temp_model = ListDataSourceSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTasksResponseBodyResultTags(TeaModel):
    def __init__(self, msg=None, tag_level=None):
        # The content of the tag.
        self.msg = msg  # type: str
        # The level of the tag.
        self.tag_level = tag_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceTasksResponseBodyResultTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.tag_level is not None:
            result['tagLevel'] = self.tag_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('tagLevel') is not None:
            self.tag_level = m.get('tagLevel')
        return self


class ListDataSourceTasksResponseBodyResultTaskNodes(TeaModel):
    def __init__(self, finish_date=None, index=None, name=None, status=None):
        # The date when the task was completed.
        self.finish_date = finish_date  # type: str
        # The sequence number of the task.
        self.index = index  # type: long
        # The name of the task.
        self.name = name  # type: str
        # The status of the task.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceTasksResponseBodyResultTaskNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_date is not None:
            result['finishDate'] = self.finish_date
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('finishDate') is not None:
            self.finish_date = m.get('finishDate')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListDataSourceTasksResponseBodyResult(TeaModel):
    def __init__(self, extra_attribute=None, field_3=None, fsm_id=None, group_type=None, name=None, status=None,
                 tags=None, task_nodes=None, time=None, type=None, user=None):
        # The additional attributes of the card.
        self.extra_attribute = extra_attribute  # type: str
        # The field3 field that is passed through when you create a state machine.
        self.field_3 = field_3  # type: str
        # fsmId
        self.fsm_id = fsm_id  # type: str
        # Indicates whether the change is a data source task change or a cluster task change.
        self.group_type = group_type  # type: str
        # The task name on the card.
        self.name = name  # type: str
        # The overall status of FSM.
        self.status = status  # type: str
        # The status tag of the progress bar chart.
        self.tags = tags  # type: list[ListDataSourceTasksResponseBodyResultTags]
        # The information about the task.
        self.task_nodes = task_nodes  # type: list[ListDataSourceTasksResponseBodyResultTaskNodes]
        # The timestamp of the task on the card.
        self.time = time  # type: str
        # The type of the task on the card.
        self.type = type  # type: str
        # The user who triggered the finite-state machine (FSM) process.
        self.user = user  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.task_nodes:
            for k in self.task_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourceTasksResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_attribute is not None:
            result['extraAttribute'] = self.extra_attribute
        if self.field_3 is not None:
            result['field3'] = self.field_3
        if self.fsm_id is not None:
            result['fsmId'] = self.fsm_id
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['taskNodes'] = []
        if self.task_nodes is not None:
            for k in self.task_nodes:
                result['taskNodes'].append(k.to_map() if k else None)
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('extraAttribute') is not None:
            self.extra_attribute = m.get('extraAttribute')
        if m.get('field3') is not None:
            self.field_3 = m.get('field3')
        if m.get('fsmId') is not None:
            self.fsm_id = m.get('fsmId')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListDataSourceTasksResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        self.task_nodes = []
        if m.get('taskNodes') is not None:
            for k in m.get('taskNodes'):
                temp_model = ListDataSourceTasksResponseBodyResultTaskNodes()
                self.task_nodes.append(temp_model.from_map(k))
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class ListDataSourceTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The information about the index.
        self.result = result  # type: list[ListDataSourceTasksResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourceTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataSourceTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataSourceTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataSourceTasksResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourceTasksResponse, self).to_map()
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
            temp_model = ListDataSourceTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourcesResponseBodyResult(TeaModel):
    def __init__(self, domain=None, indexes=None, last_ful_time=None, name=None, status=None, type=None):
        # The data center where the data source is deployed in offline mode.
        self.domain = domain  # type: str
        # The information about indexes.
        self.indexes = indexes  # type: list[str]
        # The time when an index for full data was last built.
        self.last_ful_time = last_ful_time  # type: long
        # The name of the data source.
        self.name = name  # type: str
        # The state of the data source.
        self.status = status  # type: str
        # The type of the data source.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourcesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.last_ful_time is not None:
            result['lastFulTime'] = self.last_ful_time
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('lastFulTime') is not None:
            self.last_ful_time = m.get('lastFulTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result returned.
        self.result = result  # type: list[ListDataSourcesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataSourcesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDataSourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourcesResponse, self).to_map()
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
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDateSourceGenerationsRequest(TeaModel):
    def __init__(self, domain_name=None, valid_status=None):
        # The data center where the data source is deployed.
        self.domain_name = domain_name  # type: str
        # The valid state of the data source. Valid values: true and false. The default value of this parameter is true.
        # 
        # 1.  true indicates that the generations that have not expired and of which the tasks have been executed are returned.
        # 2.  false indicates that all generations are returned.
        self.valid_status = valid_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDateSourceGenerationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.valid_status is not None:
            result['validStatus'] = self.valid_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('validStatus') is not None:
            self.valid_status = m.get('validStatus')
        return self


class ListDateSourceGenerationsResponseBodyResult(TeaModel):
    def __init__(self, build_deploy_id=None, create_time=None, data_dump_root=None, generation=None, partition=None,
                 status=None, timestamp=None):
        # buildDeployId
        self.build_deploy_id = build_deploy_id  # type: int
        # The time to start index building.
        self.create_time = create_time  # type: long
        # The directory where the index file created by using the dump table is saved.
        self.data_dump_root = data_dump_root  # type: str
        # The primary key of the generation.
        self.generation = generation  # type: long
        # Key indicates the name of the index. value indicates the number of shards.
        self.partition = partition  # type: dict[str, int]
        # The status.
        self.status = status  # type: str
        # The timestamp when the offline indexing was initiated.
        self.timestamp = timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDateSourceGenerationsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_deploy_id is not None:
            result['buildDeployId'] = self.build_deploy_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_dump_root is not None:
            result['dataDumpRoot'] = self.data_dump_root
        if self.generation is not None:
            result['generation'] = self.generation
        if self.partition is not None:
            result['partition'] = self.partition
        if self.status is not None:
            result['status'] = self.status
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('buildDeployId') is not None:
            self.build_deploy_id = m.get('buildDeployId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataDumpRoot') is not None:
            self.data_dump_root = m.get('dataDumpRoot')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class ListDateSourceGenerationsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # List
        self.result = result  # type: list[ListDateSourceGenerationsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDateSourceGenerationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDateSourceGenerationsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDateSourceGenerationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDateSourceGenerationsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDateSourceGenerationsResponse, self).to_map()
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
            temp_model = ListDateSourceGenerationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexesRequest(TeaModel):
    def __init__(self, new_mode=None):
        # 是否为新版本控制台页面
        self.new_mode = new_mode  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIndexesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_mode is not None:
            result['newMode'] = self.new_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('newMode') is not None:
            self.new_mode = m.get('newMode')
        return self


class ListIndexesResponseBodyResultDataSourceInfoConfig(TeaModel):
    def __init__(self, access_key=None, access_secret=None, bucket=None, endpoint=None, namespace=None,
                 oss_path=None, partition=None, path=None, project=None, table=None):
        # odps数据源ak
        self.access_key = access_key  # type: str
        # odps数据源ak secret
        self.access_secret = access_secret  # type: str
        # oss命名空间
        self.bucket = bucket  # type: str
        # odps相关
        self.endpoint = endpoint  # type: str
        # saro相关
        self.namespace = namespace  # type: str
        # oss数据源相关
        self.oss_path = oss_path  # type: str
        # 数据分片
        self.partition = partition  # type: str
        # hdfs相关
        self.path = path  # type: str
        # odps数据源项目名称
        self.project = project  # type: str
        # saro、odps相关
        self.table = table  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIndexesResponseBodyResultDataSourceInfoConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.access_secret is not None:
            result['accessSecret'] = self.access_secret
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.oss_path is not None:
            result['ossPath'] = self.oss_path
        if self.partition is not None:
            result['partition'] = self.partition
        if self.path is not None:
            result['path'] = self.path
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('accessSecret') is not None:
            self.access_secret = m.get('accessSecret')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class ListIndexesResponseBodyResultDataSourceInfoSaroConfig(TeaModel):
    def __init__(self, namespace=None, table_name=None):
        # saro数据源的namespace
        self.namespace = namespace  # type: str
        # saro数据表名称
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIndexesResponseBodyResultDataSourceInfoSaroConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class ListIndexesResponseBodyResultDataSourceInfo(TeaModel):
    def __init__(self, auto_build_index=None, config=None, domain=None, name=None, process_partition_count=None,
                 saro_config=None, type=None):
        # 是否开启自动全量
        self.auto_build_index = auto_build_index  # type: bool
        # odps 数据源配置
        self.config = config  # type: ListIndexesResponseBodyResultDataSourceInfoConfig
        # 离线部署
        self.domain = domain  # type: str
        # 数据源名
        self.name = name  # type: str
        # 数据更新资源数
        self.process_partition_count = process_partition_count  # type: int
        # saro数据源配置
        self.saro_config = saro_config  # type: ListIndexesResponseBodyResultDataSourceInfoSaroConfig
        # 数据源类型 (odps, swift, saro, oss, unKnow)
        self.type = type  # type: str

    def validate(self):
        if self.config:
            self.config.validate()
        if self.saro_config:
            self.saro_config.validate()

    def to_map(self):
        _map = super(ListIndexesResponseBodyResultDataSourceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build_index is not None:
            result['autoBuildIndex'] = self.auto_build_index
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.name is not None:
            result['name'] = self.name
        if self.process_partition_count is not None:
            result['processPartitionCount'] = self.process_partition_count
        if self.saro_config is not None:
            result['saroConfig'] = self.saro_config.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('autoBuildIndex') is not None:
            self.auto_build_index = m.get('autoBuildIndex')
        if m.get('config') is not None:
            temp_model = ListIndexesResponseBodyResultDataSourceInfoConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processPartitionCount') is not None:
            self.process_partition_count = m.get('processPartitionCount')
        if m.get('saroConfig') is not None:
            temp_model = ListIndexesResponseBodyResultDataSourceInfoSaroConfig()
            self.saro_config = temp_model.from_map(m['saroConfig'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListIndexesResponseBodyResultVersionsFiles(TeaModel):
    def __init__(self, full_path_name=None, is_dir=None, is_template=None, name=None):
        # The name of the directory for the index.
        self.full_path_name = full_path_name  # type: str
        # Indicates whether a directory exists.
        self.is_dir = is_dir  # type: bool
        # Indicates whether it is a template.
        self.is_template = is_template  # type: bool
        # The name of the file.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIndexesResponseBodyResultVersionsFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_path_name is not None:
            result['fullPathName'] = self.full_path_name
        if self.is_dir is not None:
            result['isDir'] = self.is_dir
        if self.is_template is not None:
            result['isTemplate'] = self.is_template
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fullPathName') is not None:
            self.full_path_name = m.get('fullPathName')
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')
        if m.get('isTemplate') is not None:
            self.is_template = m.get('isTemplate')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListIndexesResponseBodyResultVersions(TeaModel):
    def __init__(self, desc=None, files=None, name=None, status=None, update_time=None, version_id=None):
        # The description.
        self.desc = desc  # type: str
        # The list of file names.
        self.files = files  # type: list[ListIndexesResponseBodyResultVersionsFiles]
        # The name of the version.
        self.name = name  # type: str
        # The state of the version. Valid values: drafting, used, unused and trash. drafting indicates that the version is a draft, used indicates that the version is used online, unused indicates that the version is not used, and trash indicates that the version is being deleted.
        self.status = status  # type: str
        # The time when the version was updated.
        self.update_time = update_time  # type: long
        # The ID of the version. The value of this parameter is null for the edit version.
        self.version_id = version_id  # type: int

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIndexesResponseBodyResultVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = ListIndexesResponseBodyResultVersionsFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListIndexesResponseBodyResult(TeaModel):
    def __init__(self, content=None, data_source=None, data_source_info=None, description=None, domain=None,
                 full_update_time=None, full_version=None, inc_update_time=None, index_size=None, index_status=None, name=None,
                 partition=None, versions=None):
        # schema JSON
        self.content = content  # type: str
        # The data source.
        self.data_source = data_source  # type: str
        # 数据源相关信息
        self.data_source_info = data_source_info  # type: ListIndexesResponseBodyResultDataSourceInfo
        # 备注
        self.description = description  # type: str
        # The name of the data center where the data source is deployed.
        self.domain = domain  # type: str
        # 全量切换时间
        self.full_update_time = full_update_time  # type: str
        # 全量版本  即：索引版本
        self.full_version = full_version  # type: long
        # 增量更新时间
        self.inc_update_time = inc_update_time  # type: str
        # 索引大小
        self.index_size = index_size  # type: long
        # NEW, PUBLISH
        self.index_status = index_status  # type: str
        # The name of the index.
        self.name = name  # type: str
        # 数据分片
        self.partition = partition  # type: int
        # The list of version information.
        self.versions = versions  # type: list[ListIndexesResponseBodyResultVersions]

    def validate(self):
        if self.data_source_info:
            self.data_source_info.validate()
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIndexesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.data_source is not None:
            result['dataSource'] = self.data_source
        if self.data_source_info is not None:
            result['dataSourceInfo'] = self.data_source_info.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.full_update_time is not None:
            result['fullUpdateTime'] = self.full_update_time
        if self.full_version is not None:
            result['fullVersion'] = self.full_version
        if self.inc_update_time is not None:
            result['incUpdateTime'] = self.inc_update_time
        if self.index_size is not None:
            result['indexSize'] = self.index_size
        if self.index_status is not None:
            result['indexStatus'] = self.index_status
        if self.name is not None:
            result['name'] = self.name
        if self.partition is not None:
            result['partition'] = self.partition
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('dataSource') is not None:
            self.data_source = m.get('dataSource')
        if m.get('dataSourceInfo') is not None:
            temp_model = ListIndexesResponseBodyResultDataSourceInfo()
            self.data_source_info = temp_model.from_map(m['dataSourceInfo'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('fullUpdateTime') is not None:
            self.full_update_time = m.get('fullUpdateTime')
        if m.get('fullVersion') is not None:
            self.full_version = m.get('fullVersion')
        if m.get('incUpdateTime') is not None:
            self.inc_update_time = m.get('incUpdateTime')
        if m.get('indexSize') is not None:
            self.index_size = m.get('indexSize')
        if m.get('indexStatus') is not None:
            self.index_status = m.get('indexStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = ListIndexesResponseBodyResultVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListIndexesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The index list.
        self.result = result  # type: list[ListIndexesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIndexesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListIndexesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListIndexesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIndexesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIndexesResponse, self).to_map()
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
            temp_model = ListIndexesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceSpecsRequest(TeaModel):
    def __init__(self, type=None):
        # The node type. Valid values: qrs, search, index, and cluster. qrs indicates a query node, search indicates a data node, index indicates an index node, and cluster indicates a cluster.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceSpecsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListInstanceSpecsResponseBodyResult(TeaModel):
    def __init__(self, cpu=None, max_disk=None, mem=None, min_disk=None):
        # None
        self.cpu = cpu  # type: int
        # 单数据节点存储空间最大值
        self.max_disk = max_disk  # type: int
        # Unit: GB
        self.mem = mem  # type: int
        # 单数据节点存储空间最小值
        self.min_disk = min_disk  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceSpecsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.max_disk is not None:
            result['maxDisk'] = self.max_disk
        if self.mem is not None:
            result['mem'] = self.mem
        if self.min_disk is not None:
            result['minDisk'] = self.min_disk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('maxDisk') is not None:
            self.max_disk = m.get('maxDisk')
        if m.get('mem') is not None:
            self.mem = m.get('mem')
        if m.get('minDisk') is not None:
            self.min_disk = m.get('minDisk')
        return self


class ListInstanceSpecsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # List
        self.result = result  # type: list[ListInstanceSpecsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceSpecsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInstanceSpecsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInstanceSpecsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstanceSpecsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceSpecsResponse, self).to_map()
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
            temp_model = ListInstanceSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequestTags, self).to_map()
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
    def __init__(self, description=None, edition=None, instance_id=None, page_number=None, page_size=None,
                 resource_group_id=None, tags=None):
        # The description of the instance. You can use this description to filter instances. Fuzzy match is supported.
        self.description = description  # type: str
        # The Instance type, vector (vector index version),engine (recall engine version)
        self.edition = edition  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The tag dictionary.
        self.tags = tags  # type: list[ListInstancesRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.edition is not None:
            result['edition'] = self.edition
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('edition') is not None:
            self.edition = m.get('edition')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListInstancesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListInstancesShrinkRequest(TeaModel):
    def __init__(self, description=None, edition=None, instance_id=None, page_number=None, page_size=None,
                 resource_group_id=None, tags_shrink=None):
        # The description of the instance. You can use this description to filter instances. Fuzzy match is supported.
        self.description = description  # type: str
        # The Instance type, vector (vector index version),engine (recall engine version)
        self.edition = edition  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size  # type: int
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The tag dictionary.
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.edition is not None:
            result['edition'] = self.edition
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('edition') is not None:
            self.edition = m.get('edition')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        return self


class ListInstancesResponseBodyResultNetwork(TeaModel):
    def __init__(self, endpoint=None, v_switch_id=None, vpc_id=None):
        # The access point of the gateway
        self.endpoint = endpoint  # type: str
        # The ID of the virtual switch
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the Virtual Private Cloud (VPC) network
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyResultNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class ListInstancesResponseBodyResultTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyResultTags, self).to_map()
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


class ListInstancesResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, commodity_code=None, create_time=None, description=None, expired_time=None,
                 in_debt=None, instance_id=None, lock_mode=None, network=None, resource_group_id=None, status=None,
                 tags=None, update_time=None):
        # The billing method
        self.charge_type = charge_type  # type: str
        # The product code
        self.commodity_code = commodity_code  # type: str
        # The time when the instance was created
        self.create_time = create_time  # type: str
        # The description of the instance
        self.description = description  # type: str
        # The expiration time
        self.expired_time = expired_time  # type: str
        # Indicates whether an overdue payment is involved
        self.in_debt = in_debt  # type: bool
        # The ID of the resource
        self.instance_id = instance_id  # type: str
        # The lock status
        self.lock_mode = lock_mode  # type: str
        # Information about the instance of the network search engine
        self.network = network  # type: ListInstancesResponseBodyResultNetwork
        # The ID of the resource group
        self.resource_group_id = resource_group_id  # type: str
        # The status of the instance
        self.status = status  # type: str
        # The result returned.
        self.tags = tags  # type: list[ListInstancesResponseBodyResultTags]
        # The time when the instance was last updated
        self.update_time = update_time  # type: str

    def validate(self):
        if self.network:
            self.network.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.in_debt is not None:
            result['inDebt'] = self.in_debt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.network is not None:
            result['network'] = self.network.to_map()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('inDebt') is not None:
            self.in_debt = m.get('inDebt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('network') is not None:
            temp_model = ListInstancesResponseBodyResultNetwork()
            self.network = temp_model.from_map(m['network'])
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListInstancesResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        # The ID of the request
        self.request_id = request_id  # type: str
        # The result returned
        self.result = result  # type: list[ListInstancesResponseBodyResult]
        # The total number of entries returned
        self.total_count = total_count  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInstancesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancesResponseBody

    def validate(self):
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


class ListOnlineConfigsRequest(TeaModel):
    def __init__(self, domain=None):
        # The name of the domain
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOnlineConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class ListOnlineConfigsResponseBodyResult(TeaModel):
    def __init__(self, config=None, index_name=None):
        # The configuration information
        self.config = config  # type: str
        # The name of the index
        self.index_name = index_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOnlineConfigsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.index_name is not None:
            result['indexName'] = self.index_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        return self


class ListOnlineConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # List
        self.result = result  # type: list[ListOnlineConfigsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOnlineConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListOnlineConfigsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListOnlineConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOnlineConfigsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOnlineConfigsResponse, self).to_map()
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
            temp_model = ListOnlineConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryResultRequest(TeaModel):
    def __init__(self, query=None, sql=None):
        # The query statement
        self.query = query  # type: str
        # The SQL statement that is executed in the query
        self.sql = sql  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueryResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        if self.sql is not None:
            result['sql'] = self.sql
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sql') is not None:
            self.sql = m.get('sql')
        return self


class ListQueryResultResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueryResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListQueryResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQueryResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQueryResultResponse, self).to_map()
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
            temp_model = ListQueryResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAdvanceConfigFileRequest(TeaModel):
    def __init__(self, content=None, variables=None, file_name=None):
        # The content of the file.
        self.content = content  # type: str
        # The variable.
        self.variables = variables  # type: dict[str, VariablesValue]
        # The name of the file.
        self.file_name = file_name  # type: str

    def validate(self):
        if self.variables:
            for v in self.variables.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(ModifyAdvanceConfigFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        result['variables'] = {}
        if self.variables is not None:
            for k, v in self.variables.items():
                result['variables'][k] = v.to_map()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        self.variables = {}
        if m.get('variables') is not None:
            for k, v in m.get('variables').items():
                temp_model = VariablesValue()
                self.variables[k] = temp_model.from_map(v)
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class ModifyAdvanceConfigFileResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The result.
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAdvanceConfigFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyAdvanceConfigFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAdvanceConfigFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAdvanceConfigFileResponse, self).to_map()
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
            temp_model = ModifyAdvanceConfigFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterDescRequest(TeaModel):
    def __init__(self, body=None):
        # The parameters in the request body
        self.body = body  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterDescRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ModifyClusterDescResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request
        self.request_id = request_id  # type: str
        # Map
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterDescResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyClusterDescResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyClusterDescResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyClusterDescResponse, self).to_map()
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
            temp_model = ModifyClusterDescResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterOfflineConfigRequest(TeaModel):
    def __init__(self, build_mode=None, config=None, data_source_name=None, data_source_type=None,
                 data_time_sec=None, domain=None, generation=None, partition=None, push_mode=None):
        # The mode of reindexing. Valid values: api and indexRecover. api indicates to push incremental data to a data source by calling the API operations. indexRecover indicates that the data source is restored from the index.
        self.build_mode = build_mode  # type: str
        # The configuration name, which is stored as a key.
        self.config = config  # type: dict[str, int]
        # The name of the data source.
        self.data_source_name = data_source_name  # type: str
        # The type of the data source. Valid values: odps, swift, saro, and unKnow.
        self.data_source_type = data_source_type  # type: str
        # This parameter is required when index building by using API data sources is triggered.
        self.data_time_sec = data_time_sec  # type: int
        # The domain where the data source is deployed.
        self.domain = domain  # type: str
        # The data restoration version.
        self.generation = generation  # type: long
        # This parameter is required when index building for full data in a MaxCompute data source is triggered.
        self.partition = partition  # type: str
        self.push_mode = push_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterOfflineConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_mode is not None:
            result['buildMode'] = self.build_mode
        if self.config is not None:
            result['config'] = self.config
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type
        if self.data_time_sec is not None:
            result['dataTimeSec'] = self.data_time_sec
        if self.domain is not None:
            result['domain'] = self.domain
        if self.generation is not None:
            result['generation'] = self.generation
        if self.partition is not None:
            result['partition'] = self.partition
        if self.push_mode is not None:
            result['pushMode'] = self.push_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('buildMode') is not None:
            self.build_mode = m.get('buildMode')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')
        if m.get('dataTimeSec') is not None:
            self.data_time_sec = m.get('dataTimeSec')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('pushMode') is not None:
            self.push_mode = m.get('pushMode')
        return self


class ModifyClusterOfflineConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request
        self.request_id = request_id  # type: str
        # The result
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterOfflineConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyClusterOfflineConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyClusterOfflineConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyClusterOfflineConfigResponse, self).to_map()
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
            temp_model = ModifyClusterOfflineConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterOnlineConfigRequest(TeaModel):
    def __init__(self, clusters=None, config=None):
        # The information about the cluster
        self.clusters = clusters  # type: list[str]
        # 配置信息
        self.config = config  # type: dict[str, int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterOnlineConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['clusters'] = self.clusters
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusters') is not None:
            self.clusters = m.get('clusters')
        if m.get('config') is not None:
            self.config = m.get('config')
        return self


class ModifyClusterOnlineConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request
        self.request_id = request_id  # type: str
        # Map
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterOnlineConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyClusterOnlineConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyClusterOnlineConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyClusterOnlineConfigResponse, self).to_map()
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
            temp_model = ModifyClusterOnlineConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceRequest(TeaModel):
    def __init__(self, body=None, dry_run=None):
        # The request body.
        self.body = body  # type: dict[str, any]
        # Specifies whether the data source is created by using the dryRun feature. This parameter only checks whether the data source is valid. Valid values: true and false. true indicates that the data source is created by using the dryRun feature, and false indicates that the data source is not created by using the dryRun feature.
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyDataSourceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request
        self.request_id = request_id  # type: str
        # The result returned
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyDataSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDataSourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDataSourceResponse, self).to_map()
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
            temp_model = ModifyDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFileRequest(TeaModel):
    def __init__(self, content=None, partition=None, file_name=None):
        # The content of the file.
        self.content = content  # type: str
        # The data partition. This parameter is required if the dataSourceType parameter is set to odps.
        self.partition = partition  # type: int
        # The name of the file in the full path
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.partition is not None:
            result['partition'] = self.partition
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class ModifyFileResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The information about the index
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFileResponse, self).to_map()
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
            temp_model = ModifyFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIndexPartitionRequestIndexInfos(TeaModel):
    def __init__(self, index_name=None, parallel_num=None, partition_count=None):
        # The name of the index.
        self.index_name = index_name  # type: str
        # The number of concurrency. The default value is 1.
        self.parallel_num = parallel_num  # type: int
        # The number of shards of the index.
        self.partition_count = partition_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIndexPartitionRequestIndexInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.parallel_num is not None:
            result['parallelNum'] = self.parallel_num
        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('parallelNum') is not None:
            self.parallel_num = m.get('parallelNum')
        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')
        return self


class ModifyIndexPartitionRequest(TeaModel):
    def __init__(self, data_source_name=None, domain_name=None, generation=None, index_infos=None):
        # The name of the data source.
        self.data_source_name = data_source_name  # type: str
        # The name of the data center.
        self.domain_name = domain_name  # type: str
        # The primary key of generation.
        self.generation = generation  # type: long
        # The information about shards of the index.
        self.index_infos = index_infos  # type: list[ModifyIndexPartitionRequestIndexInfos]

    def validate(self):
        if self.index_infos:
            for k in self.index_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyIndexPartitionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.generation is not None:
            result['generation'] = self.generation
        result['indexInfos'] = []
        if self.index_infos is not None:
            for k in self.index_infos:
                result['indexInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        self.index_infos = []
        if m.get('indexInfos') is not None:
            for k in m.get('indexInfos'):
                temp_model = ModifyIndexPartitionRequestIndexInfos()
                self.index_infos.append(temp_model.from_map(k))
        return self


class ModifyIndexPartitionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # Map
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIndexPartitionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyIndexPartitionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyIndexPartitionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyIndexPartitionResponse, self).to_map()
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
            temp_model = ModifyIndexPartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIndexVersionRequestBody(TeaModel):
    def __init__(self, build_deploy_id=None, index_name=None, version=None):
        # The ID of the index deployed in offline mode.
        self.build_deploy_id = build_deploy_id  # type: str
        # The name of the index.
        self.index_name = index_name  # type: str
        # The version of the index.
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIndexVersionRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_deploy_id is not None:
            result['buildDeployId'] = self.build_deploy_id
        if self.index_name is not None:
            result['indexName'] = self.index_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('buildDeployId') is not None:
            self.build_deploy_id = m.get('buildDeployId')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ModifyIndexVersionRequest(TeaModel):
    def __init__(self, body=None):
        # The keyword used to search for a version. Fuzzy match is supported.
        self.body = body  # type: list[ModifyIndexVersionRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyIndexVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = ModifyIndexVersionRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class ModifyIndexVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # result
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIndexVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyIndexVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyIndexVersionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyIndexVersionResponse, self).to_map()
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
            temp_model = ModifyIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodeConfigRequest(TeaModel):
    def __init__(self, active=None, data_duplicate_number=None, data_fragment_number=None, flow_ratio=None,
                 min_service_percent=None, published=None, cluster_name=None, data_source_name=None, name=None, type=None):
        self.active = active  # type: bool
        self.data_duplicate_number = data_duplicate_number  # type: int
        self.data_fragment_number = data_fragment_number  # type: int
        self.flow_ratio = flow_ratio  # type: int
        self.min_service_percent = min_service_percent  # type: int
        self.published = published  # type: bool
        # The name of the cluster.
        self.cluster_name = cluster_name  # type: str
        # The name of the data source. Valid values: search and not_search. search indicates to search data. not_search indicates not to search data.
        self.data_source_name = data_source_name  # type: str
        # The original name of the node.
        self.name = name  # type: str
        # The type of the algorithm. Valid values: pop, cp, hot, hint, and suggest.
        # 
        # *   pop indicates the popularity model.
        # *   cp indicates the category prediction model.
        # *   hot indicates the top search model.
        # *   hint indicates the hint model.
        # *   suggest indicates the drop-down suggestion model.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.data_duplicate_number is not None:
            result['dataDuplicateNumber'] = self.data_duplicate_number
        if self.data_fragment_number is not None:
            result['dataFragmentNumber'] = self.data_fragment_number
        if self.flow_ratio is not None:
            result['flowRatio'] = self.flow_ratio
        if self.min_service_percent is not None:
            result['minServicePercent'] = self.min_service_percent
        if self.published is not None:
            result['published'] = self.published
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('dataDuplicateNumber') is not None:
            self.data_duplicate_number = m.get('dataDuplicateNumber')
        if m.get('dataFragmentNumber') is not None:
            self.data_fragment_number = m.get('dataFragmentNumber')
        if m.get('flowRatio') is not None:
            self.flow_ratio = m.get('flowRatio')
        if m.get('minServicePercent') is not None:
            self.min_service_percent = m.get('minServicePercent')
        if m.get('published') is not None:
            self.published = m.get('published')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ModifyNodeConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The information about the index
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodeConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyNodeConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyNodeConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNodeConfigResponse, self).to_map()
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
            temp_model = ModifyNodeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOnlineConfigRequest(TeaModel):
    def __init__(self, body=None):
        # ashortdescriptionofstruct
        self.body = body  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOnlineConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ModifyOnlineConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # Map
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOnlineConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyOnlineConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyOnlineConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyOnlineConfigResponse, self).to_map()
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
            temp_model = ModifyOnlineConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPasswordRequest(TeaModel):
    def __init__(self, password=None, username=None):
        # The password
        self.password = password  # type: str
        # The username
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ModifyPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request
        self.request_id = request_id  # type: str
        # The result
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPasswordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPasswordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPasswordResponse, self).to_map()
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
            temp_model = ModifyPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishAdvanceConfigRequest(TeaModel):
    def __init__(self, body=None):
        # The structure of the request
        self.body = body  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishAdvanceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class PublishAdvanceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request
        self.request_id = request_id  # type: str
        # The result returned
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishAdvanceConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PublishAdvanceConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishAdvanceConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishAdvanceConfigResponse, self).to_map()
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
            temp_model = PublishAdvanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishIndexVersionRequest(TeaModel):
    def __init__(self, body=None):
        # The query result
        self.body = body  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishIndexVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class PublishIndexVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The information about the index
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishIndexVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PublishIndexVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishIndexVersionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishIndexVersionResponse, self).to_map()
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
            temp_model = PublishIndexVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverIndexRequest(TeaModel):
    def __init__(self, build_deploy_id=None, data_source_name=None, generation=None, index_name=None):
        # The ID of the index deployed in offline mode.
        self.build_deploy_id = build_deploy_id  # type: int
        # The name of the data source
        self.data_source_name = data_source_name  # type: str
        # The primary key of generation.
        self.generation = generation  # type: str
        # The name of the index
        self.index_name = index_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoverIndexRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_deploy_id is not None:
            result['buildDeployId'] = self.build_deploy_id
        if self.data_source_name is not None:
            result['dataSourceName'] = self.data_source_name
        if self.generation is not None:
            result['generation'] = self.generation
        if self.index_name is not None:
            result['indexName'] = self.index_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('buildDeployId') is not None:
            self.build_deploy_id = m.get('buildDeployId')
        if m.get('dataSourceName') is not None:
            self.data_source_name = m.get('dataSourceName')
        if m.get('generation') is not None:
            self.generation = m.get('generation')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        return self


class RecoverIndexResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result returned by data search.
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoverIndexResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RecoverIndexResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecoverIndexResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecoverIndexResponse, self).to_map()
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
            temp_model = RecoverIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The result
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveClusterResponse, self).to_map()
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
            temp_model = RemoveClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # id of request
        self.request_id = request_id  # type: str
        # The information about the index
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class StopTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopTaskResponse, self).to_map()
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
            temp_model = StopTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequestComponents(TeaModel):
    def __init__(self, code=None, value=None):
        # The specification code, which must be consistent with the values of the corresponding module parameters.
        self.code = code  # type: str
        # The value of the specification.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequestComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(self, components=None, description=None, order_type=None):
        # A list of instance-related specifications.
        self.components = components  # type: list[UpdateInstanceRequestComponents]
        # The description of the instance.
        self.description = description  # type: str
        # Valid values: UPGRADE and DOWNGRADE. UPGRADE indicates to upgrade the instance specifications. DOWNGRADE indicates to downgrade the instance specifications.
        self.order_type = order_type  # type: str

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['components'] = []
        if self.components is not None:
            for k in self.components:
                result['components'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.order_type is not None:
            result['orderType'] = self.order_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.components = []
        if m.get('components') is not None:
            for k in m.get('components'):
                temp_model = UpdateInstanceRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        return self


class UpdateInstanceResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, commodity_code=None, create_time=None, description=None, expired_time=None,
                 in_debt=None, instance_id=None, lock_mode=None, resource_group_id=None, status=None, update_time=None):
        # The billing method
        self.charge_type = charge_type  # type: str
        # The product code
        self.commodity_code = commodity_code  # type: str
        # The time when the instance was created
        self.create_time = create_time  # type: str
        # The description of the instance
        self.description = description  # type: str
        # The time when the instance expires
        self.expired_time = expired_time  # type: str
        # Indicates whether an overdue payment is involved
        self.in_debt = in_debt  # type: bool
        # The ID of the resource
        self.instance_id = instance_id  # type: str
        # The lock status
        self.lock_mode = lock_mode  # type: str
        # The ID of the resource group
        self.resource_group_id = resource_group_id  # type: str
        # The status of the instance
        self.status = status  # type: str
        # The time when the instance was last updated
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.in_debt is not None:
            result['inDebt'] = self.in_debt
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('inDebt') is not None:
            self.in_debt = m.get('inDebt')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request
        self.request_id = request_id  # type: str
        # The result returned
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
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceResponse, self).to_map()
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


