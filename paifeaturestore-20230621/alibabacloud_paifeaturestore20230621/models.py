# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class FeatureViewConfigValue(TeaModel):
    def __init__(self, partitions=None, event_time=None, equal=None):
        self.partitions = partitions  # type: dict[str, FeatureViewConfigValuePartitionsValue]
        self.event_time = event_time  # type: str
        self.equal = equal  # type: bool

    def validate(self):
        if self.partitions:
            for v in self.partitions.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(FeatureViewConfigValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Partitions'] = {}
        if self.partitions is not None:
            for k, v in self.partitions.items():
                result['Partitions'][k] = v.to_map()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.equal is not None:
            result['Equal'] = self.equal
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.partitions = {}
        if m.get('Partitions') is not None:
            for k, v in m.get('Partitions').items():
                temp_model = FeatureViewConfigValuePartitionsValue()
                self.partitions[k] = temp_model.from_map(v)
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Equal') is not None:
            self.equal = m.get('Equal')
        return self


class FeatureViewConfigValuePartitionsValue(TeaModel):
    def __init__(self, value=None, values=None, start_value=None, end_value=None):
        self.value = value  # type: str
        self.values = values  # type: list[str]
        self.start_value = start_value  # type: str
        self.end_value = end_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FeatureViewConfigValuePartitionsValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.values is not None:
            result['Values'] = self.values
        if self.start_value is not None:
            result['StartValue'] = self.start_value
        if self.end_value is not None:
            result['EndValue'] = self.end_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('StartValue') is not None:
            self.start_value = m.get('StartValue')
        if m.get('EndValue') is not None:
            self.end_value = m.get('EndValue')
        return self


class ChangeProjectFeatureEntityHotIdVersionRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeProjectFeatureEntityHotIdVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ChangeProjectFeatureEntityHotIdVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeProjectFeatureEntityHotIdVersionResponseBody, self).to_map()
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


class ChangeProjectFeatureEntityHotIdVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeProjectFeatureEntityHotIdVersionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeProjectFeatureEntityHotIdVersionResponse, self).to_map()
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
            temp_model = ChangeProjectFeatureEntityHotIdVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckInstanceDatasourceRequest(TeaModel):
    def __init__(self, config=None, type=None, uri=None):
        self.config = config  # type: str
        self.type = type  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckInstanceDatasourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CheckInstanceDatasourceResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckInstanceDatasourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CheckInstanceDatasourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckInstanceDatasourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckInstanceDatasourceResponse, self).to_map()
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
            temp_model = CheckInstanceDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasourceRequest(TeaModel):
    def __init__(self, config=None, name=None, type=None, uri=None, workspace_id=None):
        self.config = config  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.uri = uri  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatasourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateDatasourceResponseBody(TeaModel):
    def __init__(self, datasource_id=None, request_id=None):
        self.datasource_id = datasource_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatasourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDatasourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDatasourceResponse, self).to_map()
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
            temp_model = CreateDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFeatureEntityRequest(TeaModel):
    def __init__(self, join_id=None, name=None, project_id=None):
        self.join_id = join_id  # type: str
        self.name = name  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFeatureEntityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateFeatureEntityResponseBody(TeaModel):
    def __init__(self, feature_entity_id=None, request_id=None):
        self.feature_entity_id = feature_entity_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFeatureEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFeatureEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFeatureEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFeatureEntityResponse, self).to_map()
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
            temp_model = CreateFeatureEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFeatureViewRequestFields(TeaModel):
    def __init__(self, attributes=None, name=None, type=None):
        self.attributes = attributes  # type: list[str]
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFeatureViewRequestFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFeatureViewRequest(TeaModel):
    def __init__(self, config=None, feature_entity_id=None, fields=None, name=None, project_id=None,
                 register_datasource_id=None, register_table=None, sync_online_table=None, ttl=None, tags=None, type=None,
                 write_method=None):
        self.config = config  # type: str
        self.feature_entity_id = feature_entity_id  # type: str
        self.fields = fields  # type: list[CreateFeatureViewRequestFields]
        self.name = name  # type: str
        self.project_id = project_id  # type: str
        self.register_datasource_id = register_datasource_id  # type: str
        self.register_table = register_table  # type: str
        self.sync_online_table = sync_online_table  # type: bool
        self.ttl = ttl  # type: int
        self.tags = tags  # type: list[str]
        self.type = type  # type: str
        self.write_method = write_method  # type: str

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateFeatureViewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.register_datasource_id is not None:
            result['RegisterDatasourceId'] = self.register_datasource_id
        if self.register_table is not None:
            result['RegisterTable'] = self.register_table
        if self.sync_online_table is not None:
            result['SyncOnlineTable'] = self.sync_online_table
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.write_method is not None:
            result['WriteMethod'] = self.write_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = CreateFeatureViewRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegisterDatasourceId') is not None:
            self.register_datasource_id = m.get('RegisterDatasourceId')
        if m.get('RegisterTable') is not None:
            self.register_table = m.get('RegisterTable')
        if m.get('SyncOnlineTable') is not None:
            self.sync_online_table = m.get('SyncOnlineTable')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WriteMethod') is not None:
            self.write_method = m.get('WriteMethod')
        return self


class CreateFeatureViewResponseBody(TeaModel):
    def __init__(self, feature_view_id=None, request_id=None):
        self.feature_view_id = feature_view_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFeatureViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFeatureViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFeatureViewResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFeatureViewResponse, self).to_map()
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
            temp_model = CreateFeatureViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, type=None):
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, code=None, instance_id=None, request_id=None):
        self.code = code  # type: str
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class CreateLabelTableRequestFields(TeaModel):
    def __init__(self, attributes=None, name=None, type=None):
        self.attributes = attributes  # type: list[str]
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLabelTableRequestFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateLabelTableRequest(TeaModel):
    def __init__(self, datasource_id=None, fields=None, name=None, project_id=None):
        self.datasource_id = datasource_id  # type: str
        self.fields = fields  # type: list[CreateLabelTableRequestFields]
        self.name = name  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateLabelTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = CreateLabelTableRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateLabelTableResponseBody(TeaModel):
    def __init__(self, label_table_id=None, request_id=None):
        self.label_table_id = label_table_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLabelTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLabelTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLabelTableResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLabelTableResponse, self).to_map()
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
            temp_model = CreateLabelTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelFeatureRequestFeatures(TeaModel):
    def __init__(self, alias_name=None, feature_view_id=None, name=None, type=None):
        self.alias_name = alias_name  # type: str
        self.feature_view_id = feature_view_id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModelFeatureRequestFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateModelFeatureRequest(TeaModel):
    def __init__(self, features=None, label_table_id=None, name=None, project_id=None,
                 sequence_feature_view_ids=None):
        self.features = features  # type: list[CreateModelFeatureRequestFeatures]
        self.label_table_id = label_table_id  # type: str
        self.name = name  # type: str
        self.project_id = project_id  # type: str
        self.sequence_feature_view_ids = sequence_feature_view_ids  # type: list[str]

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateModelFeatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sequence_feature_view_ids is not None:
            result['SequenceFeatureViewIds'] = self.sequence_feature_view_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = CreateModelFeatureRequestFeatures()
                self.features.append(temp_model.from_map(k))
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SequenceFeatureViewIds') is not None:
            self.sequence_feature_view_ids = m.get('SequenceFeatureViewIds')
        return self


class CreateModelFeatureResponseBody(TeaModel):
    def __init__(self, model_feature_id=None, request_id=None):
        self.model_feature_id = model_feature_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModelFeatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_feature_id is not None:
            result['ModelFeatureId'] = self.model_feature_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelFeatureId') is not None:
            self.model_feature_id = m.get('ModelFeatureId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateModelFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateModelFeatureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateModelFeatureResponse, self).to_map()
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
            temp_model = CreateModelFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelFeatureTrainingSetFGTableResponseBody(TeaModel):
    def __init__(self, training_set_fgtable_name=None, request_id=None):
        self.training_set_fgtable_name = training_set_fgtable_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModelFeatureTrainingSetFGTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.training_set_fgtable_name is not None:
            result['TrainingSetFGTableName'] = self.training_set_fgtable_name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrainingSetFGTableName') is not None:
            self.training_set_fgtable_name = m.get('TrainingSetFGTableName')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateModelFeatureTrainingSetFGTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateModelFeatureTrainingSetFGTableResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateModelFeatureTrainingSetFGTableResponse, self).to_map()
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
            temp_model = CreateModelFeatureTrainingSetFGTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, description=None, name=None, offline_datasource_id=None, offline_life_cycle=None,
                 online_datasource_id=None, workspace_id=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.offline_datasource_id = offline_datasource_id  # type: str
        self.offline_life_cycle = offline_life_cycle  # type: int
        self.online_datasource_id = online_datasource_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.offline_datasource_id is not None:
            result['OfflineDatasourceId'] = self.offline_datasource_id
        if self.offline_life_cycle is not None:
            result['OfflineLifeCycle'] = self.offline_life_cycle
        if self.online_datasource_id is not None:
            result['OnlineDatasourceId'] = self.online_datasource_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OfflineDatasourceId') is not None:
            self.offline_datasource_id = m.get('OfflineDatasourceId')
        if m.get('OfflineLifeCycle') is not None:
            self.offline_life_cycle = m.get('OfflineLifeCycle')
        if m.get('OnlineDatasourceId') is not None:
            self.online_datasource_id = m.get('OnlineDatasourceId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(self, project_id=None, request_id=None):
        self.project_id = project_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProjectResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceIdentityRoleRequest(TeaModel):
    def __init__(self, role_name=None):
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceIdentityRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateServiceIdentityRoleResponseBody(TeaModel):
    def __init__(self, code=None, request_id=None, role_name=None):
        self.code = code  # type: str
        self.request_id = request_id  # type: str
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceIdentityRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateServiceIdentityRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceIdentityRoleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceIdentityRoleResponse, self).to_map()
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
            temp_model = CreateServiceIdentityRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatasourceResponseBody, self).to_map()
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


class DeleteDatasourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDatasourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDatasourceResponse, self).to_map()
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
            temp_model = DeleteDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFeatureEntityResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFeatureEntityResponseBody, self).to_map()
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


class DeleteFeatureEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFeatureEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFeatureEntityResponse, self).to_map()
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
            temp_model = DeleteFeatureEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFeatureViewResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFeatureViewResponseBody, self).to_map()
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


class DeleteFeatureViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFeatureViewResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFeatureViewResponse, self).to_map()
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
            temp_model = DeleteFeatureViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLabelTableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLabelTableResponseBody, self).to_map()
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


class DeleteLabelTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLabelTableResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLabelTableResponse, self).to_map()
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
            temp_model = DeleteLabelTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelFeatureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteModelFeatureResponseBody, self).to_map()
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


class DeleteModelFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteModelFeatureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteModelFeatureResponse, self).to_map()
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
            temp_model = DeleteModelFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectResponseBody, self).to_map()
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


class DeleteProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteProjectResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProjectResponse, self).to_map()
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportModelFeatureTrainingSetFGTableRequestTrainingSetFgConfig(TeaModel):
    def __init__(self, fg_json_name=None, jar_name=None, partitions=None):
        self.fg_json_name = fg_json_name  # type: str
        self.jar_name = jar_name  # type: str
        self.partitions = partitions  # type: dict[str, dict]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportModelFeatureTrainingSetFGTableRequestTrainingSetFgConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fg_json_name is not None:
            result['FgJsonName'] = self.fg_json_name
        if self.jar_name is not None:
            result['JarName'] = self.jar_name
        if self.partitions is not None:
            result['Partitions'] = self.partitions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FgJsonName') is not None:
            self.fg_json_name = m.get('FgJsonName')
        if m.get('JarName') is not None:
            self.jar_name = m.get('JarName')
        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')
        return self


class ExportModelFeatureTrainingSetFGTableRequest(TeaModel):
    def __init__(self, training_set_fg_config=None):
        self.training_set_fg_config = training_set_fg_config  # type: ExportModelFeatureTrainingSetFGTableRequestTrainingSetFgConfig

    def validate(self):
        if self.training_set_fg_config:
            self.training_set_fg_config.validate()

    def to_map(self):
        _map = super(ExportModelFeatureTrainingSetFGTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.training_set_fg_config is not None:
            result['TrainingSetFgConfig'] = self.training_set_fg_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrainingSetFgConfig') is not None:
            temp_model = ExportModelFeatureTrainingSetFGTableRequestTrainingSetFgConfig()
            self.training_set_fg_config = temp_model.from_map(m['TrainingSetFgConfig'])
        return self


class ExportModelFeatureTrainingSetFGTableResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportModelFeatureTrainingSetFGTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ExportModelFeatureTrainingSetFGTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportModelFeatureTrainingSetFGTableResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportModelFeatureTrainingSetFGTableResponse, self).to_map()
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
            temp_model = ExportModelFeatureTrainingSetFGTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportModelFeatureTrainingSetTableRequestLabelInputConfig(TeaModel):
    def __init__(self, event_time=None, partitions=None):
        self.event_time = event_time  # type: str
        self.partitions = partitions  # type: dict[str, dict]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportModelFeatureTrainingSetTableRequestLabelInputConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.partitions is not None:
            result['Partitions'] = self.partitions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')
        return self


class ExportModelFeatureTrainingSetTableRequestTrainingSetConfig(TeaModel):
    def __init__(self, partitions=None):
        self.partitions = partitions  # type: dict[str, dict]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportModelFeatureTrainingSetTableRequestTrainingSetConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partitions is not None:
            result['Partitions'] = self.partitions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')
        return self


class ExportModelFeatureTrainingSetTableRequest(TeaModel):
    def __init__(self, feature_view_config=None, label_input_config=None, training_set_config=None):
        self.feature_view_config = feature_view_config  # type: dict[str, FeatureViewConfigValue]
        self.label_input_config = label_input_config  # type: ExportModelFeatureTrainingSetTableRequestLabelInputConfig
        self.training_set_config = training_set_config  # type: ExportModelFeatureTrainingSetTableRequestTrainingSetConfig

    def validate(self):
        if self.feature_view_config:
            for v in self.feature_view_config.values():
                if v:
                    v.validate()
        if self.label_input_config:
            self.label_input_config.validate()
        if self.training_set_config:
            self.training_set_config.validate()

    def to_map(self):
        _map = super(ExportModelFeatureTrainingSetTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureViewConfig'] = {}
        if self.feature_view_config is not None:
            for k, v in self.feature_view_config.items():
                result['FeatureViewConfig'][k] = v.to_map()
        if self.label_input_config is not None:
            result['LabelInputConfig'] = self.label_input_config.to_map()
        if self.training_set_config is not None:
            result['TrainingSetConfig'] = self.training_set_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.feature_view_config = {}
        if m.get('FeatureViewConfig') is not None:
            for k, v in m.get('FeatureViewConfig').items():
                temp_model = FeatureViewConfigValue()
                self.feature_view_config[k] = temp_model.from_map(v)
        if m.get('LabelInputConfig') is not None:
            temp_model = ExportModelFeatureTrainingSetTableRequestLabelInputConfig()
            self.label_input_config = temp_model.from_map(m['LabelInputConfig'])
        if m.get('TrainingSetConfig') is not None:
            temp_model = ExportModelFeatureTrainingSetTableRequestTrainingSetConfig()
            self.training_set_config = temp_model.from_map(m['TrainingSetConfig'])
        return self


class ExportModelFeatureTrainingSetTableResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportModelFeatureTrainingSetTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ExportModelFeatureTrainingSetTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportModelFeatureTrainingSetTableResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportModelFeatureTrainingSetTableResponse, self).to_map()
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
            temp_model = ExportModelFeatureTrainingSetTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasourceResponseBody(TeaModel):
    def __init__(self, config=None, datasource_id=None, gmt_create_time=None, gmt_modified_time=None, name=None,
                 request_id=None, type=None, uri=None, workspace_id=None):
        self.config = config  # type: str
        self.datasource_id = datasource_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.type = type  # type: str
        self.uri = uri  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDatasourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDatasourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDatasourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDatasourceResponse, self).to_map()
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
            temp_model = GetDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasourceTableResponseBodyFields(TeaModel):
    def __init__(self, attributes=None, name=None, type=None):
        self.attributes = attributes  # type: list[str]
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDatasourceTableResponseBodyFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetDatasourceTableResponseBody(TeaModel):
    def __init__(self, fields=None, request_id=None, table_name=None):
        self.fields = fields  # type: list[GetDatasourceTableResponseBodyFields]
        self.request_id = request_id  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDatasourceTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = GetDatasourceTableResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetDatasourceTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDatasourceTableResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDatasourceTableResponse, self).to_map()
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
            temp_model = GetDatasourceTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureEntityResponseBody(TeaModel):
    def __init__(self, gmt_create_time=None, join_id=None, name=None, owner=None, project_id=None, project_name=None,
                 request_id=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.join_id = join_id  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFeatureEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFeatureEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFeatureEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFeatureEntityResponse, self).to_map()
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
            temp_model = GetFeatureEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureViewResponseBodyFields(TeaModel):
    def __init__(self, attributes=None, name=None, type=None):
        self.attributes = attributes  # type: list[str]
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFeatureViewResponseBodyFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetFeatureViewResponseBody(TeaModel):
    def __init__(self, config=None, feature_entity_id=None, feature_entity_name=None, fields=None,
                 gmt_create_time=None, gmt_modified_time=None, gmt_sync_time=None, join_id=None, last_sync_config=None, name=None,
                 owner=None, project_id=None, project_name=None, publish_table_script=None, register_datasource_id=None,
                 register_datasource_name=None, register_table=None, request_id=None, sync_online_table=None, ttl=None, tags=None, type=None,
                 write_method=None):
        self.config = config  # type: str
        self.feature_entity_id = feature_entity_id  # type: str
        self.feature_entity_name = feature_entity_name  # type: str
        self.fields = fields  # type: list[GetFeatureViewResponseBodyFields]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.gmt_sync_time = gmt_sync_time  # type: str
        self.join_id = join_id  # type: str
        self.last_sync_config = last_sync_config  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.publish_table_script = publish_table_script  # type: str
        self.register_datasource_id = register_datasource_id  # type: str
        self.register_datasource_name = register_datasource_name  # type: str
        self.register_table = register_table  # type: str
        self.request_id = request_id  # type: str
        self.sync_online_table = sync_online_table  # type: bool
        self.ttl = ttl  # type: int
        self.tags = tags  # type: list[str]
        self.type = type  # type: str
        self.write_method = write_method  # type: str

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFeatureViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        if self.feature_entity_name is not None:
            result['FeatureEntityName'] = self.feature_entity_name
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.gmt_sync_time is not None:
            result['GmtSyncTime'] = self.gmt_sync_time
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.last_sync_config is not None:
            result['LastSyncConfig'] = self.last_sync_config
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.publish_table_script is not None:
            result['PublishTableScript'] = self.publish_table_script
        if self.register_datasource_id is not None:
            result['RegisterDatasourceId'] = self.register_datasource_id
        if self.register_datasource_name is not None:
            result['RegisterDatasourceName'] = self.register_datasource_name
        if self.register_table is not None:
            result['RegisterTable'] = self.register_table
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_online_table is not None:
            result['SyncOnlineTable'] = self.sync_online_table
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.write_method is not None:
            result['WriteMethod'] = self.write_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        if m.get('FeatureEntityName') is not None:
            self.feature_entity_name = m.get('FeatureEntityName')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = GetFeatureViewResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('GmtSyncTime') is not None:
            self.gmt_sync_time = m.get('GmtSyncTime')
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('LastSyncConfig') is not None:
            self.last_sync_config = m.get('LastSyncConfig')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('PublishTableScript') is not None:
            self.publish_table_script = m.get('PublishTableScript')
        if m.get('RegisterDatasourceId') is not None:
            self.register_datasource_id = m.get('RegisterDatasourceId')
        if m.get('RegisterDatasourceName') is not None:
            self.register_datasource_name = m.get('RegisterDatasourceName')
        if m.get('RegisterTable') is not None:
            self.register_table = m.get('RegisterTable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncOnlineTable') is not None:
            self.sync_online_table = m.get('SyncOnlineTable')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WriteMethod') is not None:
            self.write_method = m.get('WriteMethod')
        return self


class GetFeatureViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFeatureViewResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFeatureViewResponse, self).to_map()
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
            temp_model = GetFeatureViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, message=None, progress=None, region_id=None,
                 request_id=None, status=None, type=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.message = message  # type: str
        self.progress = progress  # type: float
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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


class GetLabelTableResponseBodyFields(TeaModel):
    def __init__(self, attributes=None, name=None, type=None):
        self.attributes = attributes  # type: list[str]
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLabelTableResponseBodyFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetLabelTableResponseBody(TeaModel):
    def __init__(self, datasource_id=None, datasource_name=None, fields=None, gmt_create_time=None,
                 gmt_modified_time=None, name=None, owner=None, project_id=None, project_name=None, related_model_features=None,
                 request_id=None):
        self.datasource_id = datasource_id  # type: str
        self.datasource_name = datasource_name  # type: str
        self.fields = fields  # type: list[GetLabelTableResponseBodyFields]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.related_model_features = related_model_features  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLabelTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.related_model_features is not None:
            result['RelatedModelFeatures'] = self.related_model_features
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = GetLabelTableResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RelatedModelFeatures') is not None:
            self.related_model_features = m.get('RelatedModelFeatures')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLabelTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLabelTableResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLabelTableResponse, self).to_map()
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
            temp_model = GetLabelTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelFeatureResponseBodyFeatures(TeaModel):
    def __init__(self, alias_name=None, feature_view_id=None, feature_view_name=None, name=None, type=None):
        self.alias_name = alias_name  # type: str
        self.feature_view_id = feature_view_id  # type: str
        self.feature_view_name = feature_view_name  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelFeatureResponseBodyFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.feature_view_name is not None:
            result['FeatureViewName'] = self.feature_view_name
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('FeatureViewName') is not None:
            self.feature_view_name = m.get('FeatureViewName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetModelFeatureResponseBodyRelationsDomains(TeaModel):
    def __init__(self, domain_type=None, id=None, name=None):
        self.domain_type = domain_type  # type: str
        # Domain ID。
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelFeatureResponseBodyRelationsDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetModelFeatureResponseBodyRelationsLinks(TeaModel):
    def __init__(self, from_=None, link=None, to=None):
        self.from_ = from_  # type: str
        self.link = link  # type: str
        self.to = to  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelFeatureResponseBodyRelationsLinks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.link is not None:
            result['Link'] = self.link
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class GetModelFeatureResponseBodyRelations(TeaModel):
    def __init__(self, domains=None, links=None):
        self.domains = domains  # type: list[GetModelFeatureResponseBodyRelationsDomains]
        self.links = links  # type: list[GetModelFeatureResponseBodyRelationsLinks]

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()
        if self.links:
            for k in self.links:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetModelFeatureResponseBodyRelations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        result['Links'] = []
        if self.links is not None:
            for k in self.links:
                result['Links'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = GetModelFeatureResponseBodyRelationsDomains()
                self.domains.append(temp_model.from_map(k))
        self.links = []
        if m.get('Links') is not None:
            for k in m.get('Links'):
                temp_model = GetModelFeatureResponseBodyRelationsLinks()
                self.links.append(temp_model.from_map(k))
        return self


class GetModelFeatureResponseBody(TeaModel):
    def __init__(self, export_training_set_table_script=None, features=None, gmt_create_time=None,
                 gmt_modified_time=None, label_table_id=None, label_table_name=None, name=None, owner=None, project_id=None,
                 project_name=None, relations=None, request_id=None, training_set_fgtable=None, training_set_table=None):
        self.export_training_set_table_script = export_training_set_table_script  # type: str
        self.features = features  # type: list[GetModelFeatureResponseBodyFeatures]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.label_table_id = label_table_id  # type: str
        self.label_table_name = label_table_name  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.relations = relations  # type: GetModelFeatureResponseBodyRelations
        self.request_id = request_id  # type: str
        self.training_set_fgtable = training_set_fgtable  # type: str
        self.training_set_table = training_set_table  # type: str

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()
        if self.relations:
            self.relations.validate()

    def to_map(self):
        _map = super(GetModelFeatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_training_set_table_script is not None:
            result['ExportTrainingSetTableScript'] = self.export_training_set_table_script
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.label_table_name is not None:
            result['LabelTableName'] = self.label_table_name
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.relations is not None:
            result['Relations'] = self.relations.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.training_set_fgtable is not None:
            result['TrainingSetFGTable'] = self.training_set_fgtable
        if self.training_set_table is not None:
            result['TrainingSetTable'] = self.training_set_table
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExportTrainingSetTableScript') is not None:
            self.export_training_set_table_script = m.get('ExportTrainingSetTableScript')
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = GetModelFeatureResponseBodyFeatures()
                self.features.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('LabelTableName') is not None:
            self.label_table_name = m.get('LabelTableName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Relations') is not None:
            temp_model = GetModelFeatureResponseBodyRelations()
            self.relations = temp_model.from_map(m['Relations'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrainingSetFGTable') is not None:
            self.training_set_fgtable = m.get('TrainingSetFGTable')
        if m.get('TrainingSetTable') is not None:
            self.training_set_table = m.get('TrainingSetTable')
        return self


class GetModelFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetModelFeatureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetModelFeatureResponse, self).to_map()
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
            temp_model = GetModelFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelFeatureFGFeatureResponseBodyLookupFeatures(TeaModel):
    def __init__(self, default_value=None, feature_name=None, key_feature_domain=None, key_feature_name=None,
                 map_feature_domain=None, map_feature_name=None, value_type=None):
        self.default_value = default_value  # type: str
        self.feature_name = feature_name  # type: str
        self.key_feature_domain = key_feature_domain  # type: str
        self.key_feature_name = key_feature_name  # type: str
        self.map_feature_domain = map_feature_domain  # type: str
        self.map_feature_name = map_feature_name  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelFeatureFGFeatureResponseBodyLookupFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.key_feature_domain is not None:
            result['KeyFeatureDomain'] = self.key_feature_domain
        if self.key_feature_name is not None:
            result['KeyFeatureName'] = self.key_feature_name
        if self.map_feature_domain is not None:
            result['MapFeatureDomain'] = self.map_feature_domain
        if self.map_feature_name is not None:
            result['MapFeatureName'] = self.map_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('KeyFeatureDomain') is not None:
            self.key_feature_domain = m.get('KeyFeatureDomain')
        if m.get('KeyFeatureName') is not None:
            self.key_feature_name = m.get('KeyFeatureName')
        if m.get('MapFeatureDomain') is not None:
            self.map_feature_domain = m.get('MapFeatureDomain')
        if m.get('MapFeatureName') is not None:
            self.map_feature_name = m.get('MapFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class GetModelFeatureFGFeatureResponseBodyRawFeatures(TeaModel):
    def __init__(self, default_value=None, feature_domain=None, feature_name=None, feature_type=None,
                 input_feature_name=None, value_type=None):
        self.default_value = default_value  # type: str
        self.feature_domain = feature_domain  # type: str
        self.feature_name = feature_name  # type: str
        self.feature_type = feature_type  # type: str
        self.input_feature_name = input_feature_name  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelFeatureFGFeatureResponseBodyRawFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_domain is not None:
            result['FeatureDomain'] = self.feature_domain
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.input_feature_name is not None:
            result['InputFeatureName'] = self.input_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureDomain') is not None:
            self.feature_domain = m.get('FeatureDomain')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('InputFeatureName') is not None:
            self.input_feature_name = m.get('InputFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class GetModelFeatureFGFeatureResponseBodySequenceFeaturesSubFeatures(TeaModel):
    def __init__(self, default_value=None, feature_domain=None, feature_name=None, feature_type=None,
                 input_feature_name=None, value_type=None):
        self.default_value = default_value  # type: str
        self.feature_domain = feature_domain  # type: str
        self.feature_name = feature_name  # type: str
        self.feature_type = feature_type  # type: str
        self.input_feature_name = input_feature_name  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelFeatureFGFeatureResponseBodySequenceFeaturesSubFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_domain is not None:
            result['FeatureDomain'] = self.feature_domain
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.input_feature_name is not None:
            result['InputFeatureName'] = self.input_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureDomain') is not None:
            self.feature_domain = m.get('FeatureDomain')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('InputFeatureName') is not None:
            self.input_feature_name = m.get('InputFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class GetModelFeatureFGFeatureResponseBodySequenceFeatures(TeaModel):
    def __init__(self, attribute_delim=None, feature_name=None, sequence_delim=None, sequence_length=None,
                 sub_features=None):
        self.attribute_delim = attribute_delim  # type: str
        self.feature_name = feature_name  # type: str
        self.sequence_delim = sequence_delim  # type: str
        self.sequence_length = sequence_length  # type: long
        self.sub_features = sub_features  # type: list[GetModelFeatureFGFeatureResponseBodySequenceFeaturesSubFeatures]

    def validate(self):
        if self.sub_features:
            for k in self.sub_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetModelFeatureFGFeatureResponseBodySequenceFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_delim is not None:
            result['AttributeDelim'] = self.attribute_delim
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.sequence_delim is not None:
            result['SequenceDelim'] = self.sequence_delim
        if self.sequence_length is not None:
            result['SequenceLength'] = self.sequence_length
        result['SubFeatures'] = []
        if self.sub_features is not None:
            for k in self.sub_features:
                result['SubFeatures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeDelim') is not None:
            self.attribute_delim = m.get('AttributeDelim')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('SequenceDelim') is not None:
            self.sequence_delim = m.get('SequenceDelim')
        if m.get('SequenceLength') is not None:
            self.sequence_length = m.get('SequenceLength')
        self.sub_features = []
        if m.get('SubFeatures') is not None:
            for k in m.get('SubFeatures'):
                temp_model = GetModelFeatureFGFeatureResponseBodySequenceFeaturesSubFeatures()
                self.sub_features.append(temp_model.from_map(k))
        return self


class GetModelFeatureFGFeatureResponseBody(TeaModel):
    def __init__(self, lookup_features=None, raw_features=None, request_id=None, reserves=None,
                 sequence_features=None):
        self.lookup_features = lookup_features  # type: list[GetModelFeatureFGFeatureResponseBodyLookupFeatures]
        self.raw_features = raw_features  # type: list[GetModelFeatureFGFeatureResponseBodyRawFeatures]
        self.request_id = request_id  # type: str
        self.reserves = reserves  # type: list[str]
        self.sequence_features = sequence_features  # type: list[GetModelFeatureFGFeatureResponseBodySequenceFeatures]

    def validate(self):
        if self.lookup_features:
            for k in self.lookup_features:
                if k:
                    k.validate()
        if self.raw_features:
            for k in self.raw_features:
                if k:
                    k.validate()
        if self.sequence_features:
            for k in self.sequence_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetModelFeatureFGFeatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LookupFeatures'] = []
        if self.lookup_features is not None:
            for k in self.lookup_features:
                result['LookupFeatures'].append(k.to_map() if k else None)
        result['RawFeatures'] = []
        if self.raw_features is not None:
            for k in self.raw_features:
                result['RawFeatures'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reserves is not None:
            result['Reserves'] = self.reserves
        result['SequenceFeatures'] = []
        if self.sequence_features is not None:
            for k in self.sequence_features:
                result['SequenceFeatures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.lookup_features = []
        if m.get('LookupFeatures') is not None:
            for k in m.get('LookupFeatures'):
                temp_model = GetModelFeatureFGFeatureResponseBodyLookupFeatures()
                self.lookup_features.append(temp_model.from_map(k))
        self.raw_features = []
        if m.get('RawFeatures') is not None:
            for k in m.get('RawFeatures'):
                temp_model = GetModelFeatureFGFeatureResponseBodyRawFeatures()
                self.raw_features.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Reserves') is not None:
            self.reserves = m.get('Reserves')
        self.sequence_features = []
        if m.get('SequenceFeatures') is not None:
            for k in m.get('SequenceFeatures'):
                temp_model = GetModelFeatureFGFeatureResponseBodySequenceFeatures()
                self.sequence_features.append(temp_model.from_map(k))
        return self


class GetModelFeatureFGFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetModelFeatureFGFeatureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetModelFeatureFGFeatureResponse, self).to_map()
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
            temp_model = GetModelFeatureFGFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelFeatureFGInfoResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelFeatureFGInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetModelFeatureFGInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetModelFeatureFGInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetModelFeatureFGInfoResponse, self).to_map()
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
            temp_model = GetModelFeatureFGInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(self, description=None, feature_entity_count=None, feature_view_count=None, gmt_create_time=None,
                 gmt_modified_time=None, model_count=None, name=None, offline_datasource_id=None, offline_datasource_name=None,
                 offline_datasource_type=None, offline_lifecycle=None, online_datasource_id=None, online_datasource_name=None,
                 online_datasource_type=None, owner=None, request_id=None):
        self.description = description  # type: str
        self.feature_entity_count = feature_entity_count  # type: int
        self.feature_view_count = feature_view_count  # type: int
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.model_count = model_count  # type: int
        self.name = name  # type: str
        self.offline_datasource_id = offline_datasource_id  # type: str
        self.offline_datasource_name = offline_datasource_name  # type: str
        self.offline_datasource_type = offline_datasource_type  # type: str
        self.offline_lifecycle = offline_lifecycle  # type: int
        self.online_datasource_id = online_datasource_id  # type: str
        self.online_datasource_name = online_datasource_name  # type: str
        self.online_datasource_type = online_datasource_type  # type: str
        self.owner = owner  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.feature_entity_count is not None:
            result['FeatureEntityCount'] = self.feature_entity_count
        if self.feature_view_count is not None:
            result['FeatureViewCount'] = self.feature_view_count
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.model_count is not None:
            result['ModelCount'] = self.model_count
        if self.name is not None:
            result['Name'] = self.name
        if self.offline_datasource_id is not None:
            result['OfflineDatasourceId'] = self.offline_datasource_id
        if self.offline_datasource_name is not None:
            result['OfflineDatasourceName'] = self.offline_datasource_name
        if self.offline_datasource_type is not None:
            result['OfflineDatasourceType'] = self.offline_datasource_type
        if self.offline_lifecycle is not None:
            result['OfflineLifecycle'] = self.offline_lifecycle
        if self.online_datasource_id is not None:
            result['OnlineDatasourceId'] = self.online_datasource_id
        if self.online_datasource_name is not None:
            result['OnlineDatasourceName'] = self.online_datasource_name
        if self.online_datasource_type is not None:
            result['OnlineDatasourceType'] = self.online_datasource_type
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FeatureEntityCount') is not None:
            self.feature_entity_count = m.get('FeatureEntityCount')
        if m.get('FeatureViewCount') is not None:
            self.feature_view_count = m.get('FeatureViewCount')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ModelCount') is not None:
            self.model_count = m.get('ModelCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OfflineDatasourceId') is not None:
            self.offline_datasource_id = m.get('OfflineDatasourceId')
        if m.get('OfflineDatasourceName') is not None:
            self.offline_datasource_name = m.get('OfflineDatasourceName')
        if m.get('OfflineDatasourceType') is not None:
            self.offline_datasource_type = m.get('OfflineDatasourceType')
        if m.get('OfflineLifecycle') is not None:
            self.offline_lifecycle = m.get('OfflineLifecycle')
        if m.get('OnlineDatasourceId') is not None:
            self.online_datasource_id = m.get('OnlineDatasourceId')
        if m.get('OnlineDatasourceName') is not None:
            self.online_datasource_name = m.get('OnlineDatasourceName')
        if m.get('OnlineDatasourceType') is not None:
            self.online_datasource_type = m.get('OnlineDatasourceType')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectResponse, self).to_map()
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
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectFeatureEntityResponseBody(TeaModel):
    def __init__(self, feature_entity_id=None, join_id=None, name=None, project_name=None, request_id=None,
                 workspace_id=None):
        self.feature_entity_id = feature_entity_id  # type: str
        self.join_id = join_id  # type: str
        self.name = name  # type: str
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectFeatureEntityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetProjectFeatureEntityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectFeatureEntityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectFeatureEntityResponse, self).to_map()
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
            temp_model = GetProjectFeatureEntityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectFeatureEntityHotIdsResponseBody(TeaModel):
    def __init__(self, count=None, hot_ids=None, next_seq_number=None, request_id=None):
        self.count = count  # type: int
        self.hot_ids = hot_ids  # type: str
        self.next_seq_number = next_seq_number  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectFeatureEntityHotIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.hot_ids is not None:
            result['HotIds'] = self.hot_ids
        if self.next_seq_number is not None:
            result['NextSeqNumber'] = self.next_seq_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HotIds') is not None:
            self.hot_ids = m.get('HotIds')
        if m.get('NextSeqNumber') is not None:
            self.next_seq_number = m.get('NextSeqNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProjectFeatureEntityHotIdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectFeatureEntityHotIdsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectFeatureEntityHotIdsResponse, self).to_map()
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
            temp_model = GetProjectFeatureEntityHotIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectFeatureViewResponseBodyFields(TeaModel):
    def __init__(self, attributes=None, name=None, type=None):
        self.attributes = attributes  # type: list[str]
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectFeatureViewResponseBodyFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetProjectFeatureViewResponseBody(TeaModel):
    def __init__(self, config=None, feature_entity_id=None, feature_entity_name=None, feature_view_id=None,
                 fields=None, gmt_sync_time=None, join_id=None, last_sync_config=None, name=None, owner=None,
                 project_id=None, project_name=None, register_datasource_id=None, register_table=None, request_id=None,
                 sync_online_table=None, ttl=None, tags=None, type=None, write_method=None):
        self.config = config  # type: str
        self.feature_entity_id = feature_entity_id  # type: str
        self.feature_entity_name = feature_entity_name  # type: str
        self.feature_view_id = feature_view_id  # type: str
        self.fields = fields  # type: list[GetProjectFeatureViewResponseBodyFields]
        self.gmt_sync_time = gmt_sync_time  # type: str
        self.join_id = join_id  # type: str
        self.last_sync_config = last_sync_config  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.register_datasource_id = register_datasource_id  # type: str
        self.register_table = register_table  # type: str
        self.request_id = request_id  # type: str
        self.sync_online_table = sync_online_table  # type: bool
        self.ttl = ttl  # type: int
        self.tags = tags  # type: list[str]
        self.type = type  # type: str
        self.write_method = write_method  # type: str

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProjectFeatureViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        if self.feature_entity_name is not None:
            result['FeatureEntityName'] = self.feature_entity_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.gmt_sync_time is not None:
            result['GmtSyncTime'] = self.gmt_sync_time
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.last_sync_config is not None:
            result['LastSyncConfig'] = self.last_sync_config
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.register_datasource_id is not None:
            result['RegisterDatasourceId'] = self.register_datasource_id
        if self.register_table is not None:
            result['RegisterTable'] = self.register_table
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_online_table is not None:
            result['SyncOnlineTable'] = self.sync_online_table
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.write_method is not None:
            result['WriteMethod'] = self.write_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        if m.get('FeatureEntityName') is not None:
            self.feature_entity_name = m.get('FeatureEntityName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = GetProjectFeatureViewResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('GmtSyncTime') is not None:
            self.gmt_sync_time = m.get('GmtSyncTime')
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('LastSyncConfig') is not None:
            self.last_sync_config = m.get('LastSyncConfig')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegisterDatasourceId') is not None:
            self.register_datasource_id = m.get('RegisterDatasourceId')
        if m.get('RegisterTable') is not None:
            self.register_table = m.get('RegisterTable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncOnlineTable') is not None:
            self.sync_online_table = m.get('SyncOnlineTable')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WriteMethod') is not None:
            self.write_method = m.get('WriteMethod')
        return self


class GetProjectFeatureViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectFeatureViewResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectFeatureViewResponse, self).to_map()
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
            temp_model = GetProjectFeatureViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectModelFeatureResponseBodyFeatures(TeaModel):
    def __init__(self, alias_name=None, feature_view_id=None, feature_view_name=None, name=None, type=None):
        self.alias_name = alias_name  # type: str
        self.feature_view_id = feature_view_id  # type: str
        self.feature_view_name = feature_view_name  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectModelFeatureResponseBodyFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.feature_view_name is not None:
            result['FeatureViewName'] = self.feature_view_name
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('FeatureViewName') is not None:
            self.feature_view_name = m.get('FeatureViewName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetProjectModelFeatureResponseBody(TeaModel):
    def __init__(self, features=None, gmt_create_time=None, gmt_modified_time=None, label_datasource_id=None,
                 label_datasource_table=None, label_event_time=None, label_table_id=None, model_feature_id=None, name=None, owner=None,
                 project_id=None, project_name=None, request_id=None, training_set_fgtable=None, training_set_table=None):
        self.features = features  # type: list[GetProjectModelFeatureResponseBodyFeatures]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.label_datasource_id = label_datasource_id  # type: str
        self.label_datasource_table = label_datasource_table  # type: str
        self.label_event_time = label_event_time  # type: str
        self.label_table_id = label_table_id  # type: str
        self.model_feature_id = model_feature_id  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str
        self.training_set_fgtable = training_set_fgtable  # type: str
        self.training_set_table = training_set_table  # type: str

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProjectModelFeatureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.label_datasource_id is not None:
            result['LabelDatasourceId'] = self.label_datasource_id
        if self.label_datasource_table is not None:
            result['LabelDatasourceTable'] = self.label_datasource_table
        if self.label_event_time is not None:
            result['LabelEventTime'] = self.label_event_time
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.model_feature_id is not None:
            result['ModelFeatureId'] = self.model_feature_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.training_set_fgtable is not None:
            result['TrainingSetFGTable'] = self.training_set_fgtable
        if self.training_set_table is not None:
            result['TrainingSetTable'] = self.training_set_table
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = GetProjectModelFeatureResponseBodyFeatures()
                self.features.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LabelDatasourceId') is not None:
            self.label_datasource_id = m.get('LabelDatasourceId')
        if m.get('LabelDatasourceTable') is not None:
            self.label_datasource_table = m.get('LabelDatasourceTable')
        if m.get('LabelEventTime') is not None:
            self.label_event_time = m.get('LabelEventTime')
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('ModelFeatureId') is not None:
            self.model_feature_id = m.get('ModelFeatureId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrainingSetFGTable') is not None:
            self.training_set_fgtable = m.get('TrainingSetFGTable')
        if m.get('TrainingSetTable') is not None:
            self.training_set_table = m.get('TrainingSetTable')
        return self


class GetProjectModelFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectModelFeatureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectModelFeatureResponse, self).to_map()
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
            temp_model = GetProjectModelFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceIdentityRoleResponseBody(TeaModel):
    def __init__(self, policy=None, request_id=None, role_name=None):
        self.policy = policy  # type: str
        self.request_id = request_id  # type: str
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceIdentityRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetServiceIdentityRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServiceIdentityRoleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceIdentityRoleResponse, self).to_map()
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
            temp_model = GetServiceIdentityRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(self, config=None, gmt_create_time=None, gmt_executed_time=None, gmt_finished_time=None,
                 gmt_modified_time=None, object_id=None, object_type=None, project_id=None, project_name=None, request_id=None,
                 running_config=None, status=None, type=None):
        self.config = config  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_executed_time = gmt_executed_time  # type: str
        self.gmt_finished_time = gmt_finished_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.object_id = object_id  # type: str
        self.object_type = object_type  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str
        self.running_config = running_config  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_executed_time is not None:
            result['GmtExecutedTime'] = self.gmt_executed_time
        if self.gmt_finished_time is not None:
            result['GmtFinishedTime'] = self.gmt_finished_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.running_config is not None:
            result['RunningConfig'] = self.running_config
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtExecutedTime') is not None:
            self.gmt_executed_time = m.get('GmtExecutedTime')
        if m.get('GmtFinishedTime') is not None:
            self.gmt_finished_time = m.get('GmtFinishedTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunningConfig') is not None:
            self.running_config = m.get('RunningConfig')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskResponse, self).to_map()
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
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasourceTablesRequest(TeaModel):
    def __init__(self, table_name=None):
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDatasourceTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListDatasourceTablesResponseBody(TeaModel):
    def __init__(self, request_id=None, tables=None, total_count=None):
        self.request_id = request_id  # type: str
        self.tables = tables  # type: list[str]
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDatasourceTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tables is not None:
            result['Tables'] = self.tables
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatasourceTablesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDatasourceTablesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDatasourceTablesResponse, self).to_map()
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
            temp_model = ListDatasourceTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasourcesRequest(TeaModel):
    def __init__(self, name=None, order=None, page_number=None, page_size=None, sort_by=None, type=None,
                 workspace_id=None):
        self.name = name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = sort_by  # type: str
        self.type = type  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDatasourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasourcesResponseBodyDatasources(TeaModel):
    def __init__(self, config=None, datasource_id=None, gmt_create_time=None, gmt_modified_time=None, name=None,
                 type=None, uri=None, workspace_id=None):
        self.config = config  # type: str
        self.datasource_id = datasource_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.uri = uri  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDatasourcesResponseBodyDatasources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDatasourcesResponseBody(TeaModel):
    def __init__(self, datasources=None, request_id=None, total_count=None):
        self.datasources = datasources  # type: list[ListDatasourcesResponseBodyDatasources]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.datasources:
            for k in self.datasources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDatasourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datasources'] = []
        if self.datasources is not None:
            for k in self.datasources:
                result['Datasources'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.datasources = []
        if m.get('Datasources') is not None:
            for k in m.get('Datasources'):
                temp_model = ListDatasourcesResponseBodyDatasources()
                self.datasources.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatasourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDatasourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDatasourcesResponse, self).to_map()
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
            temp_model = ListDatasourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureEntitiesRequest(TeaModel):
    def __init__(self, feature_entity_ids=None, name=None, order=None, owner=None, page_number=None, page_size=None,
                 project_id=None, sort_by=None):
        self.feature_entity_ids = feature_entity_ids  # type: list[str]
        self.name = name  # type: str
        self.order = order  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureEntitiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_ids is not None:
            result['FeatureEntityIds'] = self.feature_entity_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureEntityIds') is not None:
            self.feature_entity_ids = m.get('FeatureEntityIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListFeatureEntitiesShrinkRequest(TeaModel):
    def __init__(self, feature_entity_ids_shrink=None, name=None, order=None, owner=None, page_number=None,
                 page_size=None, project_id=None, sort_by=None):
        self.feature_entity_ids_shrink = feature_entity_ids_shrink  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureEntitiesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_ids_shrink is not None:
            result['FeatureEntityIds'] = self.feature_entity_ids_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureEntityIds') is not None:
            self.feature_entity_ids_shrink = m.get('FeatureEntityIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListFeatureEntitiesResponseBodyFeatureEntities(TeaModel):
    def __init__(self, feature_entity_id=None, gmt_create_time=None, join_id=None, name=None, owner=None,
                 project_id=None, project_name=None):
        self.feature_entity_id = feature_entity_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.join_id = join_id  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureEntitiesResponseBodyFeatureEntities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.join_id is not None:
            result['JoinId'] = self.join_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListFeatureEntitiesResponseBody(TeaModel):
    def __init__(self, feature_entities=None, request_id=None, total_count=None):
        self.feature_entities = feature_entities  # type: list[ListFeatureEntitiesResponseBodyFeatureEntities]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.feature_entities:
            for k in self.feature_entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFeatureEntitiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureEntities'] = []
        if self.feature_entities is not None:
            for k in self.feature_entities:
                result['FeatureEntities'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.feature_entities = []
        if m.get('FeatureEntities') is not None:
            for k in m.get('FeatureEntities'):
                temp_model = ListFeatureEntitiesResponseBodyFeatureEntities()
                self.feature_entities.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeatureEntitiesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFeatureEntitiesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFeatureEntitiesResponse, self).to_map()
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
            temp_model = ListFeatureEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureViewFieldRelationshipsResponseBodyRelationshipsModels(TeaModel):
    def __init__(self, model_id=None, model_name=None):
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureViewFieldRelationshipsResponseBodyRelationshipsModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class ListFeatureViewFieldRelationshipsResponseBodyRelationships(TeaModel):
    def __init__(self, feature_name=None, models=None, offline_table_name=None, online_table_name=None):
        self.feature_name = feature_name  # type: str
        self.models = models  # type: list[ListFeatureViewFieldRelationshipsResponseBodyRelationshipsModels]
        self.offline_table_name = offline_table_name  # type: str
        self.online_table_name = online_table_name  # type: str

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFeatureViewFieldRelationshipsResponseBodyRelationships, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        result['Models'] = []
        if self.models is not None:
            for k in self.models:
                result['Models'].append(k.to_map() if k else None)
        if self.offline_table_name is not None:
            result['OfflineTableName'] = self.offline_table_name
        if self.online_table_name is not None:
            result['OnlineTableName'] = self.online_table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        self.models = []
        if m.get('Models') is not None:
            for k in m.get('Models'):
                temp_model = ListFeatureViewFieldRelationshipsResponseBodyRelationshipsModels()
                self.models.append(temp_model.from_map(k))
        if m.get('OfflineTableName') is not None:
            self.offline_table_name = m.get('OfflineTableName')
        if m.get('OnlineTableName') is not None:
            self.online_table_name = m.get('OnlineTableName')
        return self


class ListFeatureViewFieldRelationshipsResponseBody(TeaModel):
    def __init__(self, relationships=None, request_id=None):
        self.relationships = relationships  # type: list[ListFeatureViewFieldRelationshipsResponseBodyRelationships]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.relationships:
            for k in self.relationships:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFeatureViewFieldRelationshipsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Relationships'] = []
        if self.relationships is not None:
            for k in self.relationships:
                result['Relationships'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.relationships = []
        if m.get('Relationships') is not None:
            for k in m.get('Relationships'):
                temp_model = ListFeatureViewFieldRelationshipsResponseBodyRelationships()
                self.relationships.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureViewFieldRelationshipsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFeatureViewFieldRelationshipsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFeatureViewFieldRelationshipsResponse, self).to_map()
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
            temp_model = ListFeatureViewFieldRelationshipsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureViewRelationshipsResponseBodyRelationshipsModels(TeaModel):
    def __init__(self, model_id=None, model_name=None):
        self.model_id = model_id  # type: str
        self.model_name = model_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureViewRelationshipsResponseBodyRelationshipsModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class ListFeatureViewRelationshipsResponseBodyRelationships(TeaModel):
    def __init__(self, feature_view_name=None, models=None, project_name=None):
        self.feature_view_name = feature_view_name  # type: str
        self.models = models  # type: list[ListFeatureViewRelationshipsResponseBodyRelationshipsModels]
        self.project_name = project_name  # type: str

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFeatureViewRelationshipsResponseBodyRelationships, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_view_name is not None:
            result['FeatureViewName'] = self.feature_view_name
        result['Models'] = []
        if self.models is not None:
            for k in self.models:
                result['Models'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureViewName') is not None:
            self.feature_view_name = m.get('FeatureViewName')
        self.models = []
        if m.get('Models') is not None:
            for k in m.get('Models'):
                temp_model = ListFeatureViewRelationshipsResponseBodyRelationshipsModels()
                self.models.append(temp_model.from_map(k))
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListFeatureViewRelationshipsResponseBody(TeaModel):
    def __init__(self, relationships=None, request_id=None):
        self.relationships = relationships  # type: list[ListFeatureViewRelationshipsResponseBodyRelationships]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.relationships:
            for k in self.relationships:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFeatureViewRelationshipsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Relationships'] = []
        if self.relationships is not None:
            for k in self.relationships:
                result['Relationships'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.relationships = []
        if m.get('Relationships') is not None:
            for k in m.get('Relationships'):
                temp_model = ListFeatureViewRelationshipsResponseBodyRelationships()
                self.relationships.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureViewRelationshipsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFeatureViewRelationshipsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFeatureViewRelationshipsResponse, self).to_map()
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
            temp_model = ListFeatureViewRelationshipsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureViewsRequest(TeaModel):
    def __init__(self, feature_name=None, feature_view_ids=None, name=None, order=None, owner=None, page_number=None,
                 page_size=None, project_id=None, sort_by=None, tag=None, type=None):
        self.feature_name = feature_name  # type: str
        self.feature_view_ids = feature_view_ids  # type: list[str]
        self.name = name  # type: str
        self.order = order  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.sort_by = sort_by  # type: str
        self.tag = tag  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureViewsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_view_ids is not None:
            result['FeatureViewIds'] = self.feature_view_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureViewIds') is not None:
            self.feature_view_ids = m.get('FeatureViewIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFeatureViewsShrinkRequest(TeaModel):
    def __init__(self, feature_name=None, feature_view_ids_shrink=None, name=None, order=None, owner=None,
                 page_number=None, page_size=None, project_id=None, sort_by=None, tag=None, type=None):
        self.feature_name = feature_name  # type: str
        self.feature_view_ids_shrink = feature_view_ids_shrink  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.sort_by = sort_by  # type: str
        self.tag = tag  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureViewsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_view_ids_shrink is not None:
            result['FeatureViewIds'] = self.feature_view_ids_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureViewIds') is not None:
            self.feature_view_ids_shrink = m.get('FeatureViewIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFeatureViewsResponseBodyFeatureViews(TeaModel):
    def __init__(self, feature_entity_name=None, feature_view_id=None, gmt_create_time=None,
                 gmt_modified_time=None, name=None, owner=None, project_id=None, project_name=None, register_datasource_id=None,
                 register_datasource_name=None, register_table=None, ttl=None, type=None):
        self.feature_entity_name = feature_entity_name  # type: str
        self.feature_view_id = feature_view_id  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.register_datasource_id = register_datasource_id  # type: str
        self.register_datasource_name = register_datasource_name  # type: str
        self.register_table = register_table  # type: str
        self.ttl = ttl  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureViewsResponseBodyFeatureViews, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_entity_name is not None:
            result['FeatureEntityName'] = self.feature_entity_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.register_datasource_id is not None:
            result['RegisterDatasourceId'] = self.register_datasource_id
        if self.register_datasource_name is not None:
            result['RegisterDatasourceName'] = self.register_datasource_name
        if self.register_table is not None:
            result['RegisterTable'] = self.register_table
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureEntityName') is not None:
            self.feature_entity_name = m.get('FeatureEntityName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegisterDatasourceId') is not None:
            self.register_datasource_id = m.get('RegisterDatasourceId')
        if m.get('RegisterDatasourceName') is not None:
            self.register_datasource_name = m.get('RegisterDatasourceName')
        if m.get('RegisterTable') is not None:
            self.register_table = m.get('RegisterTable')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFeatureViewsResponseBody(TeaModel):
    def __init__(self, feature_views=None, request_id=None, total_count=None):
        self.feature_views = feature_views  # type: list[ListFeatureViewsResponseBodyFeatureViews]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.feature_views:
            for k in self.feature_views:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFeatureViewsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureViews'] = []
        if self.feature_views is not None:
            for k in self.feature_views:
                result['FeatureViews'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.feature_views = []
        if m.get('FeatureViews') is not None:
            for k in m.get('FeatureViews'):
                temp_model = ListFeatureViewsResponseBodyFeatureViews()
                self.feature_views.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeatureViewsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFeatureViewsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFeatureViewsResponse, self).to_map()
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
            temp_model = ListFeatureViewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, order=None, page_number=None, page_size=None, sort_by=None, status=None):
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = sort_by  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, instance_id=None, region_id=None, status=None,
                 type=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None, total_count=None):
        self.instances = instances  # type: list[ListInstancesResponseBodyInstances]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListLabelTablesRequest(TeaModel):
    def __init__(self, label_table_ids=None, name=None, order=None, owner=None, page_number=None, page_size=None,
                 project_id=None, sort_by=None):
        self.label_table_ids = label_table_ids  # type: list[str]
        self.name = name  # type: str
        self.order = order  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.project_id = project_id  # type: str
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLabelTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_table_ids is not None:
            result['LabelTableIds'] = self.label_table_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LabelTableIds') is not None:
            self.label_table_ids = m.get('LabelTableIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListLabelTablesShrinkRequest(TeaModel):
    def __init__(self, label_table_ids_shrink=None, name=None, order=None, owner=None, page_number=None,
                 page_size=None, project_id=None, sort_by=None):
        self.label_table_ids_shrink = label_table_ids_shrink  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.project_id = project_id  # type: str
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLabelTablesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_table_ids_shrink is not None:
            result['LabelTableIds'] = self.label_table_ids_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LabelTableIds') is not None:
            self.label_table_ids_shrink = m.get('LabelTableIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListLabelTablesResponseBodyLabelTables(TeaModel):
    def __init__(self, datasource_id=None, datasource_name=None, gmt_create_time=None, gmt_modified_time=None,
                 label_table_id=None, name=None, owner=None, project_id=None, project_name=None):
        self.datasource_id = datasource_id  # type: str
        self.datasource_name = datasource_name  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.label_table_id = label_table_id  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLabelTablesResponseBodyLabelTables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListLabelTablesResponseBody(TeaModel):
    def __init__(self, label_tables=None, request_id=None, total_count=None):
        self.label_tables = label_tables  # type: list[ListLabelTablesResponseBodyLabelTables]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.label_tables:
            for k in self.label_tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLabelTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelTables'] = []
        if self.label_tables is not None:
            for k in self.label_tables:
                result['LabelTables'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.label_tables = []
        if m.get('LabelTables') is not None:
            for k in m.get('LabelTables'):
                temp_model = ListLabelTablesResponseBodyLabelTables()
                self.label_tables.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLabelTablesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLabelTablesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLabelTablesResponse, self).to_map()
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
            temp_model = ListLabelTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelFeatureAvailableFeaturesRequest(TeaModel):
    def __init__(self, feature_name=None):
        self.feature_name = feature_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelFeatureAvailableFeaturesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        return self


class ListModelFeatureAvailableFeaturesResponseBodyAvaliableFeatures(TeaModel):
    def __init__(self, name=None, source_name=None, source_type=None, type=None):
        self.name = name  # type: str
        self.source_name = source_name  # type: str
        self.source_type = source_type  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelFeatureAvailableFeaturesResponseBodyAvaliableFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListModelFeatureAvailableFeaturesResponseBody(TeaModel):
    def __init__(self, avaliable_features=None, total_count=None, request_id=None):
        self.avaliable_features = avaliable_features  # type: list[ListModelFeatureAvailableFeaturesResponseBodyAvaliableFeatures]
        self.total_count = total_count  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        if self.avaliable_features:
            for k in self.avaliable_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModelFeatureAvailableFeaturesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvaliableFeatures'] = []
        if self.avaliable_features is not None:
            for k in self.avaliable_features:
                result['AvaliableFeatures'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.avaliable_features = []
        if m.get('AvaliableFeatures') is not None:
            for k in m.get('AvaliableFeatures'):
                temp_model = ListModelFeatureAvailableFeaturesResponseBodyAvaliableFeatures()
                self.avaliable_features.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListModelFeatureAvailableFeaturesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModelFeatureAvailableFeaturesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModelFeatureAvailableFeaturesResponse, self).to_map()
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
            temp_model = ListModelFeatureAvailableFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelFeaturesRequest(TeaModel):
    def __init__(self, model_feature_ids=None, name=None, order=None, owner=None, page_number=None, page_size=None,
                 project_id=None, sort_by=None):
        self.model_feature_ids = model_feature_ids  # type: list[str]
        self.name = name  # type: str
        self.order = order  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelFeaturesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_feature_ids is not None:
            result['ModelFeatureIds'] = self.model_feature_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelFeatureIds') is not None:
            self.model_feature_ids = m.get('ModelFeatureIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListModelFeaturesShrinkRequest(TeaModel):
    def __init__(self, model_feature_ids_shrink=None, name=None, order=None, owner=None, page_number=None,
                 page_size=None, project_id=None, sort_by=None):
        self.model_feature_ids_shrink = model_feature_ids_shrink  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelFeaturesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_feature_ids_shrink is not None:
            result['ModelFeatureIds'] = self.model_feature_ids_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelFeatureIds') is not None:
            self.model_feature_ids_shrink = m.get('ModelFeatureIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListModelFeaturesResponseBodyModelFeatures(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, label_table_name=None, model_feature_id=None,
                 name=None, owner=None, project_id=None, project_name=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.label_table_name = label_table_name  # type: str
        self.model_feature_id = model_feature_id  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelFeaturesResponseBodyModelFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.label_table_name is not None:
            result['LabelTableName'] = self.label_table_name
        if self.model_feature_id is not None:
            result['ModelFeatureId'] = self.model_feature_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LabelTableName') is not None:
            self.label_table_name = m.get('LabelTableName')
        if m.get('ModelFeatureId') is not None:
            self.model_feature_id = m.get('ModelFeatureId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListModelFeaturesResponseBody(TeaModel):
    def __init__(self, model_features=None, request_id=None, total_count=None):
        self.model_features = model_features  # type: list[ListModelFeaturesResponseBodyModelFeatures]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.model_features:
            for k in self.model_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListModelFeaturesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModelFeatures'] = []
        if self.model_features is not None:
            for k in self.model_features:
                result['ModelFeatures'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.model_features = []
        if m.get('ModelFeatures') is not None:
            for k in m.get('ModelFeatures'):
                temp_model = ListModelFeaturesResponseBodyModelFeatures()
                self.model_features.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListModelFeaturesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListModelFeaturesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModelFeaturesResponse, self).to_map()
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
            temp_model = ListModelFeaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectFeatureViewOwnersResponseBody(TeaModel):
    def __init__(self, owners=None, request_id=None):
        self.owners = owners  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectFeatureViewOwnersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owners is not None:
            result['Owners'] = self.owners
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Owners') is not None:
            self.owners = m.get('Owners')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProjectFeatureViewOwnersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectFeatureViewOwnersResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectFeatureViewOwnersResponse, self).to_map()
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
            temp_model = ListProjectFeatureViewOwnersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectFeatureViewTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None):
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectFeatureViewTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListProjectFeatureViewTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectFeatureViewTagsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectFeatureViewTagsResponse, self).to_map()
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
            temp_model = ListProjectFeatureViewTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectFeatureViewsResponseBodyFeatureViewsFeatures(TeaModel):
    def __init__(self, attributes=None, name=None, type=None):
        self.attributes = attributes  # type: list[str]
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectFeatureViewsResponseBodyFeatureViewsFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListProjectFeatureViewsResponseBodyFeatureViews(TeaModel):
    def __init__(self, feature_view_id=None, features=None, name=None, type=None):
        self.feature_view_id = feature_view_id  # type: str
        self.features = features  # type: list[ListProjectFeatureViewsResponseBodyFeatureViewsFeatures]
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectFeatureViewsResponseBodyFeatureViews, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = ListProjectFeatureViewsResponseBodyFeatureViewsFeatures()
                self.features.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListProjectFeatureViewsResponseBody(TeaModel):
    def __init__(self, feature_views=None, request_id=None, total_count=None):
        self.feature_views = feature_views  # type: list[ListProjectFeatureViewsResponseBodyFeatureViews]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.feature_views:
            for k in self.feature_views:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectFeatureViewsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureViews'] = []
        if self.feature_views is not None:
            for k in self.feature_views:
                result['FeatureViews'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.feature_views = []
        if m.get('FeatureViews') is not None:
            for k in m.get('FeatureViews'):
                temp_model = ListProjectFeatureViewsResponseBodyFeatureViews()
                self.feature_views.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProjectFeatureViewsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectFeatureViewsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectFeatureViewsResponse, self).to_map()
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
            temp_model = ListProjectFeatureViewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(self, name=None, order=None, owner=None, page_number=None, page_size=None, project_ids=None,
                 sort_by=None, workspace_id=None):
        self.name = name  # type: str
        self.order = order  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_ids = project_ids  # type: list[str]
        self.sort_by = sort_by  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListProjectsShrinkRequest(TeaModel):
    def __init__(self, name=None, order=None, owner=None, page_number=None, page_size=None, project_ids_shrink=None,
                 sort_by=None, workspace_id=None):
        self.name = name  # type: str
        self.order = order  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_ids_shrink = project_ids_shrink  # type: str
        self.sort_by = sort_by  # type: str
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_ids_shrink is not None:
            result['ProjectIds'] = self.project_ids_shrink
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectIds') is not None:
            self.project_ids_shrink = m.get('ProjectIds')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListProjectsResponseBodyProjects(TeaModel):
    def __init__(self, description=None, feature_entity_count=None, feature_view_count=None, gmt_create_time=None,
                 gmt_modified_time=None, model_count=None, name=None, offline_datasource_id=None, offline_datasource_name=None,
                 offline_datasource_type=None, offline_lifecycle=None, online_datasource_id=None, online_datasource_name=None,
                 online_datasource_type=None, owner=None, project_id=None):
        self.description = description  # type: str
        self.feature_entity_count = feature_entity_count  # type: int
        self.feature_view_count = feature_view_count  # type: int
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.model_count = model_count  # type: int
        self.name = name  # type: str
        self.offline_datasource_id = offline_datasource_id  # type: str
        self.offline_datasource_name = offline_datasource_name  # type: str
        self.offline_datasource_type = offline_datasource_type  # type: str
        self.offline_lifecycle = offline_lifecycle  # type: int
        self.online_datasource_id = online_datasource_id  # type: str
        self.online_datasource_name = online_datasource_name  # type: str
        self.online_datasource_type = online_datasource_type  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyProjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.feature_entity_count is not None:
            result['FeatureEntityCount'] = self.feature_entity_count
        if self.feature_view_count is not None:
            result['FeatureViewCount'] = self.feature_view_count
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.model_count is not None:
            result['ModelCount'] = self.model_count
        if self.name is not None:
            result['Name'] = self.name
        if self.offline_datasource_id is not None:
            result['OfflineDatasourceId'] = self.offline_datasource_id
        if self.offline_datasource_name is not None:
            result['OfflineDatasourceName'] = self.offline_datasource_name
        if self.offline_datasource_type is not None:
            result['OfflineDatasourceType'] = self.offline_datasource_type
        if self.offline_lifecycle is not None:
            result['OfflineLifecycle'] = self.offline_lifecycle
        if self.online_datasource_id is not None:
            result['OnlineDatasourceId'] = self.online_datasource_id
        if self.online_datasource_name is not None:
            result['OnlineDatasourceName'] = self.online_datasource_name
        if self.online_datasource_type is not None:
            result['OnlineDatasourceType'] = self.online_datasource_type
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FeatureEntityCount') is not None:
            self.feature_entity_count = m.get('FeatureEntityCount')
        if m.get('FeatureViewCount') is not None:
            self.feature_view_count = m.get('FeatureViewCount')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ModelCount') is not None:
            self.model_count = m.get('ModelCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OfflineDatasourceId') is not None:
            self.offline_datasource_id = m.get('OfflineDatasourceId')
        if m.get('OfflineDatasourceName') is not None:
            self.offline_datasource_name = m.get('OfflineDatasourceName')
        if m.get('OfflineDatasourceType') is not None:
            self.offline_datasource_type = m.get('OfflineDatasourceType')
        if m.get('OfflineLifecycle') is not None:
            self.offline_lifecycle = m.get('OfflineLifecycle')
        if m.get('OnlineDatasourceId') is not None:
            self.online_datasource_id = m.get('OnlineDatasourceId')
        if m.get('OnlineDatasourceName') is not None:
            self.online_datasource_name = m.get('OnlineDatasourceName')
        if m.get('OnlineDatasourceType') is not None:
            self.online_datasource_type = m.get('OnlineDatasourceType')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(self, projects=None, request_id=None, total_count=None):
        self.projects = projects  # type: list[ListProjectsResponseBodyProjects]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = ListProjectsResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectsResponse, self).to_map()
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskLogsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTaskLogsResponseBody(TeaModel):
    def __init__(self, logs=None, request_id=None, total_count=None):
        self.logs = logs  # type: list[str]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaskLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTaskLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTaskLogsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTaskLogsResponse, self).to_map()
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
            temp_model = ListTaskLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(self, object_id=None, object_type=None, page_number=None, page_size=None, project_id=None,
                 status=None, task_ids=None, type=None):
        self.object_id = object_id  # type: str
        self.object_type = object_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.status = status  # type: str
        self.task_ids = task_ids  # type: list[str]
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(self, object_id=None, object_type=None, page_number=None, page_size=None, project_id=None,
                 status=None, task_ids_shrink=None, type=None):
        self.object_id = object_id  # type: str
        self.object_type = object_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.status = status  # type: str
        self.task_ids_shrink = task_ids_shrink  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_ids_shrink is not None:
            result['TaskIds'] = self.task_ids_shrink
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskIds') is not None:
            self.task_ids_shrink = m.get('TaskIds')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_executed_time=None, gmt_finished_time=None, object_id=None,
                 object_type=None, project_id=None, project_name=None, status=None, task_id=None, type=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_executed_time = gmt_executed_time  # type: str
        self.gmt_finished_time = gmt_finished_time  # type: str
        self.object_id = object_id  # type: str
        self.object_type = object_type  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_executed_time is not None:
            result['GmtExecutedTime'] = self.gmt_executed_time
        if self.gmt_finished_time is not None:
            result['GmtFinishedTime'] = self.gmt_finished_time
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtExecutedTime') is not None:
            self.gmt_executed_time = m.get('GmtExecutedTime')
        if m.get('GmtFinishedTime') is not None:
            self.gmt_finished_time = m.get('GmtFinishedTime')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, tasks=None, total_count=None):
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[ListTasksResponseBodyTasks]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTasksResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTasksResponse, self).to_map()
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
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishFeatureViewTableRequest(TeaModel):
    def __init__(self, config=None, event_time=None, mode=None, offline_to_online=None, partitions=None):
        self.config = config  # type: str
        self.event_time = event_time  # type: str
        self.mode = mode  # type: str
        self.offline_to_online = offline_to_online  # type: bool
        self.partitions = partitions  # type: dict[str, dict]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishFeatureViewTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.offline_to_online is not None:
            result['OfflineToOnline'] = self.offline_to_online
        if self.partitions is not None:
            result['Partitions'] = self.partitions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OfflineToOnline') is not None:
            self.offline_to_online = m.get('OfflineToOnline')
        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')
        return self


class PublishFeatureViewTableResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishFeatureViewTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class PublishFeatureViewTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishFeatureViewTableResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishFeatureViewTableResponse, self).to_map()
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
            temp_model = PublishFeatureViewTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasourceRequest(TeaModel):
    def __init__(self, config=None, name=None, uri=None):
        self.config = config  # type: str
        self.name = name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDatasourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class UpdateDatasourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDatasourceResponseBody, self).to_map()
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


class UpdateDatasourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDatasourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDatasourceResponse, self).to_map()
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
            temp_model = UpdateDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLabelTableRequestFields(TeaModel):
    def __init__(self, attributes=None, name=None, type=None):
        self.attributes = attributes  # type: list[str]
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLabelTableRequestFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateLabelTableRequest(TeaModel):
    def __init__(self, datasource_id=None, fields=None, name=None):
        self.datasource_id = datasource_id  # type: str
        self.fields = fields  # type: list[UpdateLabelTableRequestFields]
        self.name = name  # type: str

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateLabelTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = UpdateLabelTableRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateLabelTableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLabelTableResponseBody, self).to_map()
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


class UpdateLabelTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLabelTableResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLabelTableResponse, self).to_map()
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
            temp_model = UpdateLabelTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelFeatureRequestFeatures(TeaModel):
    def __init__(self, alias_name=None, feature_view_id=None, name=None, type=None):
        self.alias_name = alias_name  # type: str
        self.feature_view_id = feature_view_id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModelFeatureRequestFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateModelFeatureRequest(TeaModel):
    def __init__(self, features=None, label_table_id=None, sequence_feature_view_ids=None):
        self.features = features  # type: list[UpdateModelFeatureRequestFeatures]
        self.label_table_id = label_table_id  # type: str
        self.sequence_feature_view_ids = sequence_feature_view_ids  # type: list[str]

    def validate(self):
        if self.features:
            for k in self.features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateModelFeatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Features'] = []
        if self.features is not None:
            for k in self.features:
                result['Features'].append(k.to_map() if k else None)
        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id
        if self.sequence_feature_view_ids is not None:
            result['SequenceFeatureViewIds'] = self.sequence_feature_view_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k in m.get('Features'):
                temp_model = UpdateModelFeatureRequestFeatures()
                self.features.append(temp_model.from_map(k))
        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')
        if m.get('SequenceFeatureViewIds') is not None:
            self.sequence_feature_view_ids = m.get('SequenceFeatureViewIds')
        return self


class UpdateModelFeatureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModelFeatureResponseBody, self).to_map()
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


class UpdateModelFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateModelFeatureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateModelFeatureResponse, self).to_map()
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
            temp_model = UpdateModelFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelFeatureFGFeatureRequestLookupFeatures(TeaModel):
    def __init__(self, default_value=None, feature_name=None, key_feature_domain=None, key_feature_name=None,
                 map_feature_domain=None, map_feature_name=None, value_type=None):
        self.default_value = default_value  # type: str
        self.feature_name = feature_name  # type: str
        self.key_feature_domain = key_feature_domain  # type: str
        self.key_feature_name = key_feature_name  # type: str
        self.map_feature_domain = map_feature_domain  # type: str
        self.map_feature_name = map_feature_name  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModelFeatureFGFeatureRequestLookupFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.key_feature_domain is not None:
            result['KeyFeatureDomain'] = self.key_feature_domain
        if self.key_feature_name is not None:
            result['KeyFeatureName'] = self.key_feature_name
        if self.map_feature_domain is not None:
            result['MapFeatureDomain'] = self.map_feature_domain
        if self.map_feature_name is not None:
            result['MapFeatureName'] = self.map_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('KeyFeatureDomain') is not None:
            self.key_feature_domain = m.get('KeyFeatureDomain')
        if m.get('KeyFeatureName') is not None:
            self.key_feature_name = m.get('KeyFeatureName')
        if m.get('MapFeatureDomain') is not None:
            self.map_feature_domain = m.get('MapFeatureDomain')
        if m.get('MapFeatureName') is not None:
            self.map_feature_name = m.get('MapFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class UpdateModelFeatureFGFeatureRequestRawFeatures(TeaModel):
    def __init__(self, default_value=None, feature_domain=None, feature_name=None, feature_type=None,
                 input_feature_name=None, value_type=None):
        self.default_value = default_value  # type: str
        self.feature_domain = feature_domain  # type: str
        self.feature_name = feature_name  # type: str
        self.feature_type = feature_type  # type: str
        self.input_feature_name = input_feature_name  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModelFeatureFGFeatureRequestRawFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_domain is not None:
            result['FeatureDomain'] = self.feature_domain
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.input_feature_name is not None:
            result['InputFeatureName'] = self.input_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureDomain') is not None:
            self.feature_domain = m.get('FeatureDomain')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('InputFeatureName') is not None:
            self.input_feature_name = m.get('InputFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class UpdateModelFeatureFGFeatureRequestSequenceFeaturesSubFeatures(TeaModel):
    def __init__(self, default_value=None, feature_domain=None, feature_name=None, feature_type=None,
                 input_feature_name=None, value_type=None):
        self.default_value = default_value  # type: str
        self.feature_domain = feature_domain  # type: str
        self.feature_name = feature_name  # type: str
        self.feature_type = feature_type  # type: str
        self.input_feature_name = input_feature_name  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModelFeatureFGFeatureRequestSequenceFeaturesSubFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.feature_domain is not None:
            result['FeatureDomain'] = self.feature_domain
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type
        if self.input_feature_name is not None:
            result['InputFeatureName'] = self.input_feature_name
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('FeatureDomain') is not None:
            self.feature_domain = m.get('FeatureDomain')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')
        if m.get('InputFeatureName') is not None:
            self.input_feature_name = m.get('InputFeatureName')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class UpdateModelFeatureFGFeatureRequestSequenceFeatures(TeaModel):
    def __init__(self, attribute_delim=None, feature_name=None, sequence_delim=None, sequence_length=None,
                 sub_features=None):
        self.attribute_delim = attribute_delim  # type: str
        self.feature_name = feature_name  # type: str
        self.sequence_delim = sequence_delim  # type: str
        self.sequence_length = sequence_length  # type: long
        self.sub_features = sub_features  # type: list[UpdateModelFeatureFGFeatureRequestSequenceFeaturesSubFeatures]

    def validate(self):
        if self.sub_features:
            for k in self.sub_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateModelFeatureFGFeatureRequestSequenceFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_delim is not None:
            result['AttributeDelim'] = self.attribute_delim
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.sequence_delim is not None:
            result['SequenceDelim'] = self.sequence_delim
        if self.sequence_length is not None:
            result['SequenceLength'] = self.sequence_length
        result['SubFeatures'] = []
        if self.sub_features is not None:
            for k in self.sub_features:
                result['SubFeatures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeDelim') is not None:
            self.attribute_delim = m.get('AttributeDelim')
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('SequenceDelim') is not None:
            self.sequence_delim = m.get('SequenceDelim')
        if m.get('SequenceLength') is not None:
            self.sequence_length = m.get('SequenceLength')
        self.sub_features = []
        if m.get('SubFeatures') is not None:
            for k in m.get('SubFeatures'):
                temp_model = UpdateModelFeatureFGFeatureRequestSequenceFeaturesSubFeatures()
                self.sub_features.append(temp_model.from_map(k))
        return self


class UpdateModelFeatureFGFeatureRequest(TeaModel):
    def __init__(self, lookup_features=None, raw_features=None, reserves=None, sequence_features=None):
        self.lookup_features = lookup_features  # type: list[UpdateModelFeatureFGFeatureRequestLookupFeatures]
        self.raw_features = raw_features  # type: list[UpdateModelFeatureFGFeatureRequestRawFeatures]
        self.reserves = reserves  # type: list[str]
        self.sequence_features = sequence_features  # type: list[UpdateModelFeatureFGFeatureRequestSequenceFeatures]

    def validate(self):
        if self.lookup_features:
            for k in self.lookup_features:
                if k:
                    k.validate()
        if self.raw_features:
            for k in self.raw_features:
                if k:
                    k.validate()
        if self.sequence_features:
            for k in self.sequence_features:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateModelFeatureFGFeatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LookupFeatures'] = []
        if self.lookup_features is not None:
            for k in self.lookup_features:
                result['LookupFeatures'].append(k.to_map() if k else None)
        result['RawFeatures'] = []
        if self.raw_features is not None:
            for k in self.raw_features:
                result['RawFeatures'].append(k.to_map() if k else None)
        if self.reserves is not None:
            result['Reserves'] = self.reserves
        result['SequenceFeatures'] = []
        if self.sequence_features is not None:
            for k in self.sequence_features:
                result['SequenceFeatures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.lookup_features = []
        if m.get('LookupFeatures') is not None:
            for k in m.get('LookupFeatures'):
                temp_model = UpdateModelFeatureFGFeatureRequestLookupFeatures()
                self.lookup_features.append(temp_model.from_map(k))
        self.raw_features = []
        if m.get('RawFeatures') is not None:
            for k in m.get('RawFeatures'):
                temp_model = UpdateModelFeatureFGFeatureRequestRawFeatures()
                self.raw_features.append(temp_model.from_map(k))
        if m.get('Reserves') is not None:
            self.reserves = m.get('Reserves')
        self.sequence_features = []
        if m.get('SequenceFeatures') is not None:
            for k in m.get('SequenceFeatures'):
                temp_model = UpdateModelFeatureFGFeatureRequestSequenceFeatures()
                self.sequence_features.append(temp_model.from_map(k))
        return self


class UpdateModelFeatureFGFeatureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModelFeatureFGFeatureResponseBody, self).to_map()
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


class UpdateModelFeatureFGFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateModelFeatureFGFeatureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateModelFeatureFGFeatureResponse, self).to_map()
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
            temp_model = UpdateModelFeatureFGFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelFeatureFGInfoRequest(TeaModel):
    def __init__(self, content=None):
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModelFeatureFGInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class UpdateModelFeatureFGInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateModelFeatureFGInfoResponseBody, self).to_map()
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


class UpdateModelFeatureFGInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateModelFeatureFGInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateModelFeatureFGInfoResponse, self).to_map()
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
            temp_model = UpdateModelFeatureFGInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(self, description=None, name=None):
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectResponseBody, self).to_map()
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


class UpdateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProjectResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProjectResponse, self).to_map()
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteFeatureViewTableRequestUrlDatasource(TeaModel):
    def __init__(self, delimiter=None, omit_header=None, path=None):
        self.delimiter = delimiter  # type: str
        self.omit_header = omit_header  # type: bool
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteFeatureViewTableRequestUrlDatasource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.omit_header is not None:
            result['OmitHeader'] = self.omit_header
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('OmitHeader') is not None:
            self.omit_header = m.get('OmitHeader')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class WriteFeatureViewTableRequest(TeaModel):
    def __init__(self, mode=None, partitions=None, url_datasource=None):
        self.mode = mode  # type: str
        self.partitions = partitions  # type: dict[str, dict]
        self.url_datasource = url_datasource  # type: WriteFeatureViewTableRequestUrlDatasource

    def validate(self):
        if self.url_datasource:
            self.url_datasource.validate()

    def to_map(self):
        _map = super(WriteFeatureViewTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.partitions is not None:
            result['Partitions'] = self.partitions
        if self.url_datasource is not None:
            result['UrlDatasource'] = self.url_datasource.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')
        if m.get('UrlDatasource') is not None:
            temp_model = WriteFeatureViewTableRequestUrlDatasource()
            self.url_datasource = temp_model.from_map(m['UrlDatasource'])
        return self


class WriteFeatureViewTableResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteFeatureViewTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class WriteFeatureViewTableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: WriteFeatureViewTableResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WriteFeatureViewTableResponse, self).to_map()
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
            temp_model = WriteFeatureViewTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteProjectFeatureEntityHotIdsRequest(TeaModel):
    def __init__(self, hot_ids=None, version=None):
        self.hot_ids = hot_ids  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteProjectFeatureEntityHotIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hot_ids is not None:
            result['HotIds'] = self.hot_ids
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HotIds') is not None:
            self.hot_ids = m.get('HotIds')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class WriteProjectFeatureEntityHotIdsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteProjectFeatureEntityHotIdsResponseBody, self).to_map()
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


class WriteProjectFeatureEntityHotIdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: WriteProjectFeatureEntityHotIdsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WriteProjectFeatureEntityHotIdsResponse, self).to_map()
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
            temp_model = WriteProjectFeatureEntityHotIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


